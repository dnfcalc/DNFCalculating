#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# File      : calc_core
# DateTime  : 2020/6/10 0010 21:30
# Author    : Chen Ji
# Email     : fzls.zju@gmail.com
# -------------------------------
from .copy import *
from multiprocessing import Queue
from typing import List
from PublicReference.utils.minheap import MinHeap, expected_qsize
import copy

class CalcData():
    def __init__(self):
        self.是输出职业 = True
        self.智慧产物限制 = 3

        self.minheap_queue = None  # type: Queue
        self.角色属性A = None  # type: 角色属性

        # 被分配的计算范围
        self.mode_index = 0  # 0-极速模式，1-套装模式，2-散件模式
        self.start_index = 0  # 在并发搜索任务组中分配到的开始序号：极速模式和套装模式时，任务组定义为按照原搜索组合算法得到的有效穿戴组合等；散件模式时，定义为0-level层串行搜索形成的所有子树
        self.end_index = 0  # 在并发搜索任务组中分配到的结束序号，描述同上

        # 原始数据
        self.装备选择状态: list[int] = []  # 各个装备的选择状况，第i个位置为0表示装备i未选择，否则表示已选择
        self.拥有百变怪 = False  # 是否勾选了百变怪
        self.神话属性选项: list[int] = [] # 每个神话四个选项，第4*k~4*k+3下标表示第k个神话的词条选择（k从0开始计数）
        self.改造产物选项: list[int] = []

        # 根据原始数据在计算线程计算出的一些数据
        self.有效武器列表 = []
        self.有效防具套装 = []
        self.有效首饰套装 = []
        self.有效特殊套装 = []
        self.有效上链左套装 = []
        self.有效镯下右套装 = []
        self.有效环鞋指套装 = []
        self.有效总套装列表 = [self.有效防具套装, self.有效首饰套装, self.有效特殊套装, self.有效上链左套装, self.有效镯下右套装, self.有效环鞋指套装]

        self.有效部位列表 = []

        # 最终结果
        self.minheap = None  # type: MinHeap

    def pre_calc_needed_data(self):
        from PublicReference.equipment.equ_list import 总套装列表, 部位列表, 装备列表

        self.有效武器列表.clear()
        for j in range(0, 6):
            self.有效总套装列表[j].clear()

        self.有效部位列表.clear()
        for i in range(0, 12):
            self.有效部位列表.append([])

        for i in range(0, len(self.装备选择状态)):
            if self.装备选择状态[i] == 1:
                if 装备列表[i].部位 == '武器':
                    self.有效武器列表.append(装备列表[i].名称)
                for j in range(0, 6):
                    if (装备列表[i].所属套装 in 总套装列表[j]) and (装备列表[i].所属套装 not in self.有效总套装列表[j]):
                        self.有效总套装列表[j].append(装备列表[i].所属套装)
                self.有效部位列表[部位列表.index(装备列表[i].部位)].append(装备列表[i].名称)

        count = 0
        count2 = 0
        for i in 装备列表:
            if i.品质 == '神话':
                if self.是输出职业 == True:
                    i.属性1选择 = self.神话属性选项[count * 4 + 0]
                    i.属性2选择 = self.神话属性选项[count * 4 + 1]
                    i.属性3选择 = self.神话属性选项[count * 4 + 2]
                    i.属性4选择 = self.神话属性选项[count * 4 + 3]
                else:
                    i.属性1选择_BUFF = self.神话属性选项[count * 4 + 0]
                    i.属性2选择_BUFF = self.神话属性选项[count * 4 + 1]
                    i.属性3选择_BUFF = self.神话属性选项[count * 4 + 2]
                    i.属性4选择_BUFF = self.神话属性选项[count * 4 + 3]
                count += 1
            if  self.是输出职业 == True and i.所属套装 == '智慧产物':
                i.属性1选择 = self.改造产物选项[count2 * 4 + 0]
                i.属性2选择 = self.改造产物选项[count2 * 4 + 1]
                i.属性3选择 = self.改造产物选项[count2 * 4 + 2]
                i.属性4选择 = self.改造产物选项[count2 * 4 + 3]
        pass


def calc_core(data: CalcData):
    """

    :type minheap_queue: Queue
    :type 角色属性A: 角色属性
    :type 有效穿戴组合: List[str]
    :type 有效穿戴套装: List[str]
    :type 百变怪列表: str
    """
    # 计算伤害具体算法

    # 根据装备选择情况，预计算一些数据
    data.pre_calc_needed_data()

    # 寻找本任务对应的各个组合并调用计算函数
    if data.mode_index in [0, 1]:
        calc_speed_and_set_mode(data)
    else:
        calc_single_mode(data)

    # 全部计算完后，将剩余结果传入结果队列
    data.minheap_queue.put(deepcopy(data.minheap))

def calc_speed_and_set_mode(data):
    from PublicReference.equipment.equ_list import 套装映射, 部位列表, 装备列表
    套装组合 = []
    套装适用 = []

    for a in data.有效防具套装:
        for b in data.有效首饰套装:
            for c in data.有效特殊套装:
                # 533
                套装组合.append([a, a, a, a, a, b, b, b, c, c, c]);
                套装适用.append([a + '[2]', a + '[3]', a + '[5]', b + '[2]', b + '[3]', c + '[2]', c + '[3]'])

    for a in data.有效防具套装:
        for d in data.有效上链左套装:
            for e in data.有效镯下右套装:
                for f in data.有效环鞋指套装:
                    # 3332
                    套装组合.append([d, a, e, a, f, e, d, f, f, d, e]);
                    套装适用.append([a + '[2]', d + '[2]', d + '[3]', e + '[2]', e + '[3]', f + '[2]', f + '[3]'])
                    套装组合.append([a, a, e, a, f, e, d, f, f, d, e]);
                    套装适用.append([a + '[2]', d + '[2]', a + '[3]', e + '[2]', e + '[3]', f + '[2]', f + '[3]'])
                    套装组合.append([d, a, a, a, f, e, d, f, f, d, e]);
                    套装适用.append([a + '[2]', d + '[2]', d + '[3]', e + '[2]', a + '[3]', f + '[2]', f + '[3]'])
                    套装组合.append([d, a, e, a, a, e, d, f, f, d, e]);
                    套装适用.append([a + '[2]', d + '[2]', d + '[3]', e + '[2]', e + '[3]', f + '[2]', a + '[3]'])

    if data.mode_index == 1:
        for a in data.有效防具套装:
            for b in data.有效首饰套装:
                for c in data.有效特殊套装:
                    for d in data.有效防具套装:
                        if d != a:
                            # 2333 占套装模式90%计算量
                            套装组合.append([a, a, a, d, d, b, b, b, c, c, c])
                            套装组合.append([a, a, d, a, d, b, b, b, c, c, c])
                            套装组合.append([a, d, a, a, d, b, b, b, c, c, c])
                            套装组合.append([d, a, a, a, d, b, b, b, c, c, c])
                            套装组合.append([a, a, d, d, a, b, b, b, c, c, c])
                            套装组合.append([a, d, a, d, a, b, b, b, c, c, c])
                            套装组合.append([d, a, a, d, a, b, b, b, c, c, c])
                            套装组合.append([a, d, d, a, a, b, b, b, c, c, c])
                            套装组合.append([d, a, d, a, a, b, b, b, c, c, c])
                            套装组合.append([d, d, a, a, a, b, b, b, c, c, c])
                            for x in range(0, 10):
                                套装适用.append([a + '[2]', a + '[3]', d + '[2]', b + '[2]', b + '[3]', c + '[2]', c + '[3]'])

    # 极速模式与套装模式
    count = -1
    current_index = -1
    for temp in 套装组合:
        count += 1
        for k in [-1, 0, 5, 8]:
            temp1 = []
            sign = 0
            if data.拥有百变怪:
                sign2 = '空'
            else:
                sign2 = '无'
            for x in range(0, 11):
                品质 = '-史诗-'
                if k == x:
                    品质 = '-神话-'
                index = 套装映射[temp[x] + 品质 + 部位列表[x]]
                if data.装备选择状态[index] == 1:
                    sign += 1
                else:
                    if sign2 == '空' and 装备列表[index].品质 != '神话' and 装备列表[index].所属套装 not in ['精灵使的权能', '大自然的呼吸', '能量主宰']:
                        sign += 1
                        sign2 = 装备列表[index].名称
                temp1.append(装备列表[index].名称)
            if sign == 11:
                for i in data.有效武器列表:
                    current_index += 1
                    if current_index < data.start_index:
                        # 尚未到本工作线程需要计算的范围
                        continue
                    if current_index > data.end_index:
                        # 本工作线程需要计算的范围已全部完成，直接退出
                        return
                    calc_damage(temp1 + [i], 套装适用[count], sign2, data)
                    # logger.warning("consumer {} {} {} - {}".format(
                    #     data.mode_index, data.start_index, data.end_index, current_index
                    #))
    pass

#11层循环顺序
顺序 = [5, 8, 1, 3, 2, 4, 6, 9, 7, 10]
顺序字典 = {0: 0, 5: 1, 8: 2, 1: 3, 3: 4, 2: 5, 4: 6, 6: 7, 9: 8, 7: 9, 10: 10}

def 筛选(名称, x, 装备, 套装, 神话, 种类, data):
    from PublicReference.equipment.equ_list import 装备序号, 装备列表

    i = 装备序号[名称]
    装备[x] = 名称

    for k in 顺序[顺序字典[x]:]:
        套装[k] = '无'
    
    temp = 装备列表[i].所属套装
    if temp == '智慧产物':
        try: temp = 装备列表[i].所属套装2
        except: pass
    套装[x] = temp

    count = []
    num = 0
    for j in 套装:
        if j == '智慧产物':
            num += 1
            if num > 种类[1]: return 1
        elif (j != '无') and (j not in count):
            count.append(j)

    if len(count) > 种类[0]: return 1
    elif x == 10 and 种类[0] > 4: 种类[0] = max(min(种类[0], len(count)), 4)

    if x == 0:
        神话[5] = 0; 神话[8] = 0
    elif x == 5:
        神话[8] = 0
    
    if 装备列表[i].品质 == '神话': 
        神话[x] = 1
        if sum(神话) > 1: return 1
    else:
        神话[x] = 0

    return 0

def calc_single_mode(data):
    from PublicReference.equipment.equ_list import 装备序号, 套装序号, 装备列表
    current_index = -1
    装备 = ['无'] * 12
    套装 = ['无'] * 11
    神话 = [0] * 11
    种类 = [11, data.智慧产物限制]

    for a1 in data.有效部位列表[0]:
        if 筛选(a1, 0, 装备, 套装, 神话, 种类, data): continue
        for a2 in data.有效部位列表[5]:
            if 筛选(a2, 5, 装备, 套装, 神话, 种类, data): continue
            for a3 in data.有效部位列表[8]:
                if 筛选(a3, 8, 装备, 套装, 神话, 种类, data): continue
                for a4 in data.有效部位列表[1]:
                    if 筛选(a4, 1, 装备, 套装, 神话, 种类, data): continue
                    current_index += 1
                    if current_index < data.start_index: continue # 尚未到本工作线程需要计算的范围
                    if current_index > data.end_index: return # 本工作线程需要计算的范围已全部完成，直接退出
                    for a5 in data.有效部位列表[3]:
                        if 筛选(a5, 3, 装备, 套装, 神话, 种类, data): continue
                        for a6 in data.有效部位列表[2]:
                            if 筛选(a6, 2, 装备, 套装, 神话, 种类, data): continue
                            for a7 in data.有效部位列表[4]:
                                if 筛选(a7, 4, 装备, 套装, 神话, 种类, data): continue
                                for a8 in data.有效部位列表[6]:
                                    if 筛选(a8, 6, 装备, 套装, 神话, 种类, data): continue
                                    for a9 in data.有效部位列表[9]:
                                        if 筛选(a9, 9, 装备, 套装, 神话, 种类, data): continue
                                        for a10 in data.有效部位列表[7]:
                                            if 筛选(a10, 7, 装备, 套装, 神话, 种类, data): continue
                                            for a11 in data.有效部位列表[10]:
                                                if 筛选(a11, 10, 装备, 套装, 神话, 种类, data): continue
                                                套装字典 = {}
                                                for i in 套装:
                                                    if i != '智慧产物' and i != '无':
                                                        套装字典[i] = 套装字典.get(i, 0) + 1
                                                套装名称 = []
                                                for i in 套装字典.keys():
                                                    if 套装字典[i] >= 2 and (i + '[2]') in 套装序号.keys():
                                                        套装名称.append(i + '[2]')
                                                    if 套装字典[i] >= 3 and (i + '[3]') in 套装序号.keys():
                                                        套装名称.append(i + '[3]')
                                                    if 套装字典[i] >= 5 and (i + '[5]') in 套装序号.keys():
                                                        套装名称.append(i + '[5]')
                                                for a12 in data.有效部位列表[11]:
                                                    装备[11] = a12
                                                    calc_damage(装备, 套装名称, '空', data)
    pass


def calc_damage(有效穿戴组合, 有效穿戴套装, 百变怪, data: CalcData):
    角色属性A = deepcopy(data.角色属性A)

    角色属性A.穿戴装备(有效穿戴组合, 有效穿戴套装)
    if data.是输出职业:
        damage = 角色属性A.伤害计算()
    else:
        damage = 角色属性A.BUFF计算(2)

    data.minheap.add((damage,) + tuple(角色属性A.装备栏) + (damage,) + tuple(角色属性A.套装栏) + (百变怪,))
    data.minheap.processed_result_count += 1

    if data.minheap.processed_result_count >= data.minheap.batch_size:
        # 动态调整批量大小
        if data.minheap_queue.qsize() > expected_qsize:
            data.minheap.update_batch_size()
        # 同步
        data.minheap_queue.put(deepcopy(data.minheap))
        # 重置
        data.minheap.reset()
