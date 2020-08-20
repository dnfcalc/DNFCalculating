import multiprocessing
import queue
import threading
import time
import os
import math

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PublicReference import logger
from PublicReference.calc_core import CalcData
from PublicReference.common import format_time
from PublicReference.minheap import MinHeap, MinHeapWithQueue, batch_size
from PublicReference.producer_consumer import producer, producer_data, 工作线程数, 每个工作线程应处理的任务数
from PublicReference.宠物 import *
from PublicReference.称号 import *
from PublicReference.装备 import *
from PublicReference.基础函数 import *
from PublicReference.辟邪玉 import *
from PublicReference.选项设置 import *
from PublicReference.copy import *

class 技能:
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    等级 = 0
    基础等级 = 0
    等级溢出 = 0
    自定义描述 = 0

    关联技能 = ['无']
    关联技能2 = ['无']
    关联技能3 = ['无']
    冷却关联技能 = ['无']
    冷却关联技能2 = ['无']
    冷却关联技能3 = ['无']

    def 等级加成(self, x):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                if self.基础等级 != self.等级上限 and self.关联技能 != ['无']:
                    self.等级溢出 = 1
            else:
                self.等级 += x

class 主动技能(技能):
    #只扩展了技能的三条属性，第一条技能hit默认1,2、3条hit默认为0，需要手动赋值
    #如果需要继续扩展，可以在各自职业类内继承后自行扩展，同时需要重写下等效百分比函数
    #固伤在填写基础及成长的时候需要注意，技能面板/独立得到的成长及数值需要*100
    基础 = 0.0
    成长 = 0.0
    攻击次数 = 1.0
    基础2 = 0.0
    成长2 = 0.0
    攻击次数2 = 0.0
    基础3 = 0.0
    成长3 = 0.0
    攻击次数3 = 0.0
    CD = 0.0
    TP成长 = 0.0
    TP上限 = 0
    TP等级 = 0
    是否主动 = 1
    是否有伤害 = 1
    恢复 = 1.0
    倍率 = 1.0
    被动倍率 = 1.0
    基础释放次数 = 0
    演出时间 = 0
    是否有护石 = 0
    护石选项 = ['魔界']

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)
                        
    def 等效CD(self, 武器类型):
        # Will修改
        return round(self.CD  / self.恢复, 1)

class 被动技能(技能):
    是否主动 = 0
    是否有伤害 = 0
    关联技能 = ['所有']

符文效果选项 = ['无', '攻击+5%,CD+3%', 'CD-4%', '攻击+3%', '攻击-3%,CD-6%', '攻击+3%,CD+2%', 'CD-3%', '攻击+2%', '攻击-2%,CD-4%',
    '攻击+2%,CD+1%', 'CD-2%', '攻击+1%', '攻击-1%,CD-3%', '攻击+6%,CD+4%', 'CD-5%', '攻击+4%', '攻击-4%,CD-7%']

部位字典 = {"上衣":0, "头肩":1, "下装":2, "腰带":3, "鞋":4, "手镯":5, "项链":6, "戒指":7, "耳环":8, "辅助装备":9, "魔法石":10, "武器":11}

颜色 = {'神话':'#E0502F', '史诗':'#FFB400', '传说':'#FF7800'}

刀魂之卡赞数据 = [0, 31, 40, 48, 58, 67, 79, 90, 103, 116, 131, 145, 161, 178, 194, 212, 230, 250, 270, 292, 313]

复选框样式 = "QCheckBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QCheckBox:hover{background-color:rgba(65,105,225,0.8)}"
不可勾选复选框样式 = "QCheckBox{font-size:12px;color:white;background-color:grey;border:1px;border-radius:3px} QCheckBox:hover{background-color:rgba(65,105,225,0.8)}"
按钮样式 = 'QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:10px} QPushButton:hover{background-color:rgba(65,105,225,0.8)}'
不可点击按钮样式 = 'QPushButton{font-size:12px;color:white;background-color:grey;border:1px;border-radius:10px}'
下拉框样式 = "QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(65,105,225,0.8)} QComboBox QAbstractItemView::item {height: 18px;}"
不可选择下拉框样式 = "QComboBox{font-size:12px;color:white;background-color:grey;border:1px;border-radius:5px;}  QComboBox QAbstractItemView::item {height: 18px;}"
标签样式 = "QLabel{font-size:12px;color:white}"

class MyQComboBox(QComboBox):
    def __init__(self,窗口):
        super().__init__(窗口)
        self.setView(QListView())
        self.setStyleSheet(下拉框样式)

堆大小上限 = 100

class 角色属性():

    实际名称 = ''
    角色 = ''
    职业 = ''

    武器选项 = []
    
    伤害类型选择 = []
    
    伤害类型 = ''
    防具类型 = ''
    防具精通属性 = [] 

    主BUFF = 1.0
    系统奶 = False
    年宠技能 = False
    白兔子技能 = False
    斗神之吼秘药 = False
    称号触发 = False
    战术技能BUFF = False
    兵法技攻BUFF = False

    #基础属性(含唤醒)
    基础力量 = 0
    基础智力 = 0
    基础体力 = 0
    基础精神 = 0
    
    #适用系统奶加成
    力量 = 0
    智力 = 0
    体力 = 0
    精神 = 0

    #人物基础 + 唤醒
    物理攻击力 = 65
    魔法攻击力 = 65
    独立攻击力 = 1045
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    
    #不适用系统奶加成
    进图力量 = 0.0
    进图智力 = 0.0
    进图物理攻击力 = 0
    进图魔法攻击力 = 0
    进图独立攻击力 = 0
    进图属强 = 0

    #红阵，远古记忆 -1表示没有该技能
    远古记忆 = -1
    刀魂之卡赞 = -1

    百分比力智 = 0.0
    百分比三攻 = 0.0
    伤害增加 = 0.0
    黄字 = 0.0 #冲突属性
    附加伤害 = 0.0
    属性附加 = 0.0
    暴击伤害 = 0.0
    爆伤 = 0.0 #冲突属性
    最终伤害 = 0.0
    技能攻击力 = 1.0
    持续伤害 = 0.0
    加算冷却缩减 = 0.0
    百分比减防 = 0.0
    固定减防 = 0

    攻击速度 = 0.00
    移动速度 = 0.00
    释放速度 = 0.00
    命中率 = 0.0
    回避率 = 0.0
    物理暴击率 = 0.00
    魔法暴击率 = 0.00

    技能栏 = []
    技能序号 = dict()

    红色宠物装备 = '默认'

    装备栏 = []
    套装栏 = []
    武器类型 = ''

    是否增幅 = [0] * 12
    强化等级 = [12] * 12
    改造等级 = [5] * 12
    武器锻造等级 = 0

    时间输入 = 0
    次数输入 = []
    宠物次数 = []
    技能切装 = []
    装备切装 = []
    开启切装 = 0
    切装修正 = []

    特色选项 = 0

    转甲选项 = 0
    
    #0英雄 1传说
    角色熟练度 = 0
    #0 1 2 3 4 5 6
    技能栏空位 = 6
    #0数学期望 1黄字+35% 2爆伤+35% 3白字+35% 4终伤+35% 5三攻+35%
    命运的抉择 = 0
    #0数学期望 123456
    天命无常 = 0
    #0数学期望 1 HP高于70% 2 HP在70~30% 3 HP低于30%
    悲剧的残骸 = 0
    #0数学期望 1 5%属性附加 2 10%技能攻击力 3 15%技能攻击力
    先知者的预言 = 0
    #0无霸体状态 1 霸体状态 2 无伤状态 
    贫瘠沙漠的遗产 = 1
    #0数学期望 1 7效果 2 77效果 3 777效果
    幸运三角 = 0
    #0过充电状态 1过负荷状态
    擎天战甲 = 0
    #0.00~1.00
    持续伤害计算比例 = 0
    #0 120+ 1 120-100 2 100-80 3 80-60 4 60-40 5 40-
    军神的隐秘遗产 = 0
    #0太极天帝剑：阳  1太极天帝剑：阴  
    太极天帝剑 = 0
    #0绿色生命的面容：无  1绿色生命的面容：阴暗面
    绿色生命的面容 = 1

    护石第一栏 = '无'
    护石第二栏 = '无'
    护石第三栏 = '无'

    攻击属性 = 0
    
    #是否为图内状态
    状态 = 0
 
    #辟邪玉属性
    附加伤害增加增幅 = 1.0
    属性附加伤害增加增幅 = 1.0
    技能伤害增加增幅 = 1.0
    暴击伤害增加增幅 = 1.0
    伤害增加增幅 = 1.0
    最终伤害增加增幅 = 1.0
    力量智力增加增幅 = 1.0
    物理魔法攻击力增加增幅 = 1.0
    所有属性强化增加 = 1.0

    def 附加伤害加成(self, x):
        self.附加伤害 += self.附加伤害增加增幅 * x 

    def 属性附加加成(self, x):
        self.属性附加 += self.属性附加伤害增加增幅 * x 

    def 技能攻击力加成(self, x):
        self.技能攻击力 *= 1 + self.技能伤害增加增幅 * x 

    def 暴击伤害加成(self, x):
        self.暴击伤害 += self.暴击伤害增加增幅 * x 

    def 伤害增加加成(self, x):
        self.伤害增加 += self.伤害增加增幅 * x 

    def 最终伤害加成(self, x):
        self.最终伤害 += self.最终伤害增加增幅 * x 

    def 百分比力智加成(self, x):
        self.百分比力智 += self.力量智力增加增幅 * x 

    def 百分比三攻加成(self, x):
        self.百分比三攻 += self.物理魔法攻击力增加增幅 * x 

    def 火属性强化加成(self, x):
        if self.状态 == 0:
            self.火属性强化 += self.所有属性强化增加 * x 
        else:
            self.火属性强化 += int(self.所有属性强化增加 * x) 

    def 冰属性强化加成(self, x):
        if self.状态 == 0:
            self.冰属性强化 += self.所有属性强化增加 * x 
        else:
            self.冰属性强化 += int(self.所有属性强化增加 * x) 

    def 光属性强化加成(self, x):
        if self.状态 == 0:
            self.光属性强化 += self.所有属性强化增加 * x 
        else:
            self.光属性强化 += int(self.所有属性强化增加 * x) 

    def 暗属性强化加成(self, x):
        if self.状态 == 0:
            self.暗属性强化 += self.所有属性强化增加 * x 
        else:
            self.暗属性强化 += int(self.所有属性强化增加 * x) 

    def 所有属性强化加成(self, x):
        if self.状态 == 0:
            temp = self.所有属性强化增加 * x 
        else:
            temp = int(self.所有属性强化增加 * x)
        self.所有属性强化(temp)

    def 穿戴装备(self, 装备, 套装):
        self.装备栏 = 装备
        self.套装栏 = 套装
        self.武器类型 = 装备列表[装备序号[self.装备栏[11]]].类型

    def 防具精通计算(self, i):
        temp = 装备列表[装备序号[self.装备栏[i]]]
        if temp.等级 == 100:
            if temp.所属套装 != '智慧产物':
                return 精通计算(temp.等级,temp.品质,self.强化等级[i],部位列表[i])
            else:
                return 精通计算(temp.等级,temp.品质,0,部位列表[i])
        elif temp.等级 > 85:
            计算等级 = temp.等级
            if temp.所属套装 == '兵法之神':
                if self.装备检查('过往时光的轮回'): 计算等级 = 100 
            return 精通计算(计算等级,temp.品质,self.强化等级[i],部位列表[i])
        else:
            计算等级 = temp.等级
            if temp.所属套装 == '战术之王的御敌':
                if self.装备检查('战术之王的战术指挥棒'): 计算等级 = 100
            elif temp.所属套装 == '魔战无双':   
                if self.装备检查('聚魔漩涡'): 计算等级 = 100
            x = 精通计算(计算等级,temp.品质,self.强化等级[i],部位列表[i])
            if self.转甲选项 == 1:
                return round(x, 2)
            else:
                return round(0.4 * x, 2)

    def 防具基础(self):
        for i in [0,1,2,3,4]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            if temp.等级 > 85 or self.转甲选项 == 1:
                self.力量 += temp.力量[self.防具类型]
                self.智力 += temp.智力[self.防具类型]
            else:
                self.力量 += temp.力量[temp.类型]
                self.智力 += temp.智力[temp.类型]

            精通数值 = self.防具精通计算(i)
            if '力量' in self.防具精通属性:
                self.力量 += 精通数值
            if '智力' in self.防具精通属性:
                self.智力 += 精通数值
                 
    def 装备基础(self):
        self.防具基础()
        for i in [9,10]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            if temp.所属套装 != '智慧产物':
                x = 左右计算(temp.等级,temp.品质,self.强化等级[i])
                self.力量 += x
                self.智力 += x

        for i in range(0,12):
            temp = 装备列表[装备序号[self.装备栏[i]]]
            if self.是否增幅[i] and temp.所属套装 != '智慧产物':
                x = 增幅计算(temp.等级,temp.品质,self.强化等级[i])
                if '物理' in self.伤害类型 or '力量' in self.伤害类型:
                    self.力量 += x
                else:
                    self.智力 += x
        
        temp = 装备列表[装备序号[self.装备栏[11]]]
        if temp.所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(temp.等级,temp.品质,self.强化等级[11],self.武器类型,'物理')
            self.魔法攻击力 += 武器计算(temp.等级,temp.品质,self.强化等级[11],self.武器类型,'魔法')
            self.独立攻击力 += 锻造计算(temp.等级,temp.品质,self.武器锻造等级)
        
        temp = 装备列表[装备序号[self.装备栏[8]]]
        if temp.所属套装 != '智慧产物':
            x = 耳环计算(temp.等级,temp.品质,self.强化等级[8])
            self.物理攻击力 += x
            self.魔法攻击力 += x
            self.独立攻击力 += x

        for i in [5,6,7,8,9,10,11]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            self.力量 += temp.力量
            self.智力 += temp.智力
            self.物理攻击力 += temp.物理攻击力
            self.魔法攻击力 += temp.魔法攻击力
            self.独立攻击力 += temp.独立攻击力

    def 获取增幅(self, 部位):
        return self.是否增幅[部位列表.index(部位)]

    def 获取强化(self, 部位):
        return self.强化等级[部位列表.index(部位)]

    def 获取改造(self, 部位):
        return self.改造等级[部位列表.index(部位)]

    def 装备检查(self, 装备名称):
        for i in self.装备栏:
            if i == 装备名称:
                return True
        return False

    def 所有属性强化(self, x):
        self.火属性强化 += x
        self.冰属性强化 += x
        self.光属性强化 += x
        self.暗属性强化 += x

    def 技能等级加成(self, 加成类型, minLv, maxLv, lv):
        lv = int(lv)

        if self.远古记忆 > 0:
            if minLv <= 15 and maxLv >= 15:
                self.远古记忆 = min(20, self.远古记忆 + lv)

        if self.刀魂之卡赞 > 0:
            if minLv <= 5 and maxLv >= 5:
                self.刀魂之卡赞 = min(20, self.刀魂之卡赞 + lv)

        for i in self.技能栏:
            if i.所在等级 >= minLv and i.所在等级 <= maxLv:
                if 加成类型 == '所有':
                    i.等级加成(lv)
                else:
                    if i.是否主动 == 1:
                        i.等级加成(lv)

    def 单技能等级加成(self, 名称, lv):
        for i in self.技能栏:
            if i.名称 == 名称:
                i.等级加成(lv)

    def 技能冷却缩减(self, min, max, x):
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max:
                if i.是否有伤害 == 1:
                    i.CD *= (1 - x)

    def 技能恢复加成(self, min, max, x):
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max:
                if i.是否有伤害 == 1:
                    i.恢复 += x

    def 技能倍率加成(self, lv, x):
        for i in self.技能栏:
            if i.所在等级 == lv:
                if i.是否有伤害 == 1:
                    i.倍率 *= (1 + x * self.技能伤害增加增幅)

    def 单技能修改(self, 名称, 倍率, CD):
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if i.名称 == 名称:
                    i.倍率 *= 倍率
                    i.CD *= CD

    def 面板力量(self):
        if self.系统奶 == False:
            return int(int((self.力量 + self.进图力量)) * (1 + self.百分比力智))
        else:
            return int(int((self.力量 + int((self.力量 - self.基础力量) * 1.35 + 7664) +self.进图力量)) * (1 + self.百分比力智))

    def 面板智力(self):
        if self.系统奶 == False:
            return int(int((self.智力 + self.进图智力)) * (1 + self.百分比力智))
        else:
            return int(int((self.智力 + int((self.智力 - self.基础智力) * 1.35 + 7664) +self.进图智力)) * (1 + self.百分比力智))

    def 面板物理攻击力(self, x = 0):
        面板物理攻击 = (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻) * (1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        for i in self.技能栏:
            try : 
                面板物理攻击 *= i.物理攻击力倍率(self.武器类型)
            except : 
                pass
            try : 
                面板物理攻击 *= i.物理攻击力倍率进图(self.武器类型)
            except : 
                pass
        if x == 1:
            return 面板物理攻击
        else:
            return 面板物理攻击 * (self.面板力量() / 250 + 1) 

    def 面板魔法攻击力(self, x = 0):
        面板魔法攻击 = (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻) * (1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        for i in self.技能栏:
            try : 
                面板魔法攻击 *= i.魔法攻击力倍率(self.武器类型)
            except : 
                pass
            try : 
                面板魔法攻击 *= i.魔法攻击力倍率进图(self.武器类型)
            except : 
                pass
        if x == 1:
            return 面板魔法攻击
        else:
            return 面板魔法攻击 * (self.面板智力() / 250 + 1) 

    def 面板独立攻击力(self):
        面板独立攻击 = (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻)
        for i in self.技能栏:
            try :
                面板独立攻击 *= i.独立攻击力倍率(self.武器类型)
            except :
                pass
            try : 
                面板独立攻击 *= i.独立攻击力倍率进图(self.武器类型)
            except : 
                pass
        return 面板独立攻击

    def 加算冷却计算(self):
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                i.CD *= (1 - self.加算冷却缩减)

    # Will添加
    def CD倍率计算(self):
        for i in self.技能栏:
            if i.冷却关联技能 !=['无']:
                if i.冷却关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率(self.武器类型)
                else:
                    for k in i.冷却关联技能:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率(self.武器类型)
            if i.冷却关联技能2 !=['无']:
                if i.冷却关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率2(self.武器类型)
                else:
                    for k in i.冷却关联技能2:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率2(self.武器类型)
            if i.冷却关联技能3 !=['无']:
                if i.冷却关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率3(self.武器类型)
                else:
                    for k in i.冷却关联技能3:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率3(self.武器类型)

    def 被动倍率计算(self):
        if self.远古记忆 > 0:
            self.进图智力 += self.远古记忆 * 15
        if self.刀魂之卡赞 > 0:
            self.进图力量 += 刀魂之卡赞数据[self.刀魂之卡赞]
            self.进图智力 += 刀魂之卡赞数据[self.刀魂之卡赞]
        for i in self.技能栏:
            if i.关联技能 != ['无']:
                if i.关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率(self.武器类型)
                else :
                    for k in i.关联技能:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率(self.武器类型)
            # Will添加
            if i.关联技能2 != ['无']:
                if i.关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率2(self.武器类型)
                else :
                    for k in i.关联技能2:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率2(self.武器类型)
            # Will添加
            if i.关联技能3 != ['无']:
                if i.关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率3(self.武器类型)
                else :
                    for k in i.关联技能3:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率3(self.武器类型)
    
    def 宠物装备判断(self, 属性倍率):

        if self.伤害类型 == '物理百分比':
            面板 = self.面板力量() / 250 + 1
        elif self.伤害类型 == '魔法百分比':
            面板 = self.面板智力() / 250 + 1
        elif self.伤害类型 == '物理固伤':
            面板 = self.面板力量() / 250 + 1
        elif self.伤害类型 == '魔法固伤':
            面板 = self.面板智力() / 250 + 1

        #8%白字
        temp1 = 面板 * (1 + int(self.伤害增加 * 100) / 100) * (1 + self.附加伤害 + self.属性附加 * 属性倍率 + 0.08 * self.附加伤害增加增幅)
        
        #7%黄字
        temp2 = 面板 * (1 + int((self.伤害增加 + 0.07 * self.伤害增加增幅) * 100) / 100) * (1 + self.附加伤害 + self.属性附加 * 属性倍率)

        self.百分比力智加成(0.07)
        if self.伤害类型 == '物理百分比':
            面板 = self.面板力量() / 250 + 1
        elif self.伤害类型 == '魔法百分比':
            面板 = self.面板智力() / 250 + 1
        elif self.伤害类型 == '物理固伤':
            面板 = self.面板力量() / 250 + 1
        elif self.伤害类型 == '魔法固伤':
            面板 = self.面板智力() / 250 + 1
        self.百分比力智加成(-0.07)

        #7%力智
        temp3 = 面板 * (1 + int(self.伤害增加 * 100) / 100) * (1 + self.附加伤害 + self.属性附加 * 属性倍率)

        #判断
        maxtemp = max(temp1, temp2, temp3)
        if temp1 == maxtemp:
            self.附加伤害加成(0.08)
            self.红色宠物装备 = '8%白字'
        elif temp2 == maxtemp:
            self.伤害增加加成(0.07)
            self.红色宠物装备 = '7%黄字'
        elif temp3 == maxtemp:
            self.百分比力智加成(0.07)
            self.红色宠物装备 = '7%力智'

    def 伤害指数计算(self):
        
        防御 = max(防御输入 - self.固定减防, 0) * (1 - self.百分比减防)
        基准倍率 = 1.5 * self.主BUFF * (1 - 防御 / (防御+ 20000))

        #避免出现浮点数取整BUG
        self.伤害增加 += 0.00000001

        if self.攻击属性 == 0:
            属性倍率=1.05+0.0045*int(max(self.火属性强化 - 火抗输入,self.冰属性强化 - 冰抗输入,self.光属性强化 - 光抗输入,self.暗属性强化 - 暗抗输入))
        elif self.攻击属性 == 1:
            属性倍率=1.05+0.0045*int(self.火属性强化 - 火抗输入)
        elif self.攻击属性 == 2:
            属性倍率=1.05+0.0045*int(self.冰属性强化 - 冰抗输入)
        elif self.攻击属性 == 3:
            属性倍率=1.05+0.0045*int(self.光属性强化 - 光抗输入)
        elif self.攻击属性 == 4:
            属性倍率=1.05+0.0045*int(self.暗属性强化 - 暗抗输入)

        if self.红色宠物装备 == '自适应':
            self.宠物装备判断(属性倍率)

        if self.伤害类型 == '物理百分比':
            面板 = int((self.面板力量()/250+1) * (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻))
        elif self.伤害类型 == '魔法百分比':
            面板 = int((self.面板智力()/250+1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻))
        elif self.伤害类型 == '物理固伤':
            面板 = int((self.面板力量()/250+1) * (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻))
        elif self.伤害类型 == '魔法固伤':
            面板 = int((self.面板智力()/250+1) * (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻))
        
        增伤倍率=1+int(self.伤害增加*100)/100
        增伤倍率*=1+self.暴击伤害
        增伤倍率*=1+self.最终伤害
        增伤倍率*=self.技能攻击力
        增伤倍率*=1+self.持续伤害*self.持续伤害计算比例
        增伤倍率*=1+self.附加伤害+self.属性附加*属性倍率
        self.伤害指数=面板*属性倍率*增伤倍率*基准倍率/100

    def 切装判断(self):
        for i in self.装备切装:
            if i != '无':
                return True
        return False

    def 装备替换(self):
        Q = deepcopy(self)
        P = deepcopy(self)
        
        for i in range(12):
            if P.装备切装[i] != '无':
                P.装备栏[i] = P.装备切装[i]

        套装 = []
        套装字典 = {}
        for i in P.装备栏:
            j = 装备列表[装备序号[i]].所属套装
            if j == '智慧产物':
                try:
                    k = 装备列表[装备序号[i]].所属套装2
                    套装字典[k] = 套装字典.get(k, 0) + 1
                except:
                    pass
            elif j != '无':
                套装字典[j] = 套装字典.get(j, 0) + 1

        for i in 套装字典.keys():
            if 套装字典[i] >= 2 and (i + '[2]') in 套装序号.keys():
                套装.append(i + '[2]')
            if 套装字典[i] >= 3 and (i + '[3]') in 套装序号.keys():
                套装.append(i + '[3]')
            if 套装字典[i] >= 5 and (i + '[5]') in 套装序号.keys():
                套装.append(i + '[5]')
        
        P.套装栏 = deepcopy(套装)
        P.武器类型 = 装备列表[装备序号[P.装备栏[11]]].类型
        P.力量 += P.切装修正[0]
        P.智力 += P.切装修正[1]
        P.物理攻击力 += P.切装修正[2]
        P.魔法攻击力 += P.切装修正[3]
        P.独立攻击力 += P.切装修正[4]
        P.所有属性强化加成(P.切装修正[5])

        return [Q, P]

    def 伤害计算(self, x = 0):
        if self.开启切装 == 1 and self.切装判断():
            temp = self.装备替换()
            A = temp[0].数据计算(1, 1)  #身上装备计算
            B = temp[1].数据计算(1, 0)  #切装装备计算
            self.预处理()
            for i in range(len(self.技能栏)):
                self.技能栏[i] = deepcopy(temp[self.技能切装[i]].技能栏[i])
            C = []
            总伤害 = 0
            for i in range(len(A)):
                C.append(A[i] if (self.技能切装[int(i / 4)] == 0) else B[i])
                if i % 4 == 1:
                    总伤害 += C[i]
            if x == 0:
                return 总伤害
            else:
                for i in range(int(len(A) / 4)):
                    if 总伤害 != 0:
                        C[i * 4 + 3] = C[i * 4 + 1] / 总伤害 * 100
                    else:
                        C[i * 4 + 3] = 0  
                return C
        else:
            self.技能切装 = [0] * len(self.技能栏)
            return self.数据计算(x)
            
    def 预处理(self):
        self.装备属性计算()
        self.所有属性强化(self.进图属强)
        self.CD倍率计算()
        self.加算冷却计算()
        self.被动倍率计算()
        self.伤害指数计算()

    def 数据计算(self, x = 0, y = -1):
        self.预处理()
        技能释放次数=[]
        技能单次伤害=[]
        技能总伤害=[]
    
        #技能单次伤害计算
        for i in self.技能栏:
            if i.是否有伤害==1 and self.技能切装[self.技能序号[i.名称]] != y:
                技能单次伤害.append(i.等效百分比(self.武器类型)*self.伤害指数*i.被动倍率)
            else:
                技能单次伤害.append(0)

        #技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                if self.次数输入[self.技能序号[i.名称]] =='/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型) + 1 +i.基础释放次数))
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)
    
        #单技能伤害合计
    
        for i in self.技能栏:
            if i.是否有伤害==1 and 技能释放次数[self.技能序号[i.名称]] != 0:
                技能总伤害.append(技能单次伤害[self.技能序号[i.名称]]*技能释放次数[self.技能序号[i.名称]]*(1+self.白兔子技能*0.20+self.年宠技能*0.10*self.宠物次数[self.技能序号[i.名称]]/技能释放次数[self.技能序号[i.名称]]+self.斗神之吼秘药*0.12))
            else:
                技能总伤害.append(0)
    
        总伤害=0
        for i in self.技能栏:
            总伤害+=技能总伤害[self.技能序号[i.名称]]
        
        if x==0:
            return 总伤害
    
        if x==1:
            详细数据=[]
            for i in range(0,len(self.技能栏)):
                详细数据.append(技能释放次数[i])
                详细数据.append(技能总伤害[i])
                if 技能释放次数[i]!=0:
                    详细数据.append(技能总伤害[i]/技能释放次数[i])
                else:
                    详细数据.append(0)
                if 总伤害!=0:
                    详细数据.append(技能总伤害[i]/总伤害*100)
                else:
                    详细数据.append(0)
            return 详细数据

    def 站街力量(self):
        return int(self.力量)

    def 站街智力(self):
        return int(self.智力)

    def 站街物理攻击力(self, x = 0):
        站街物理攻击 = self.物理攻击力
        for i in self.技能栏:
            try : 
                站街物理攻击 *= i.物理攻击力倍率(self.武器类型)
            except : 
                pass
        if x == 1:
            return 站街物理攻击
        else:
            return 站街物理攻击 * (self.站街力量() / 250 + 1)

    def 站街魔法攻击力(self, x = 0):
        站街魔法攻击 =  self.魔法攻击力
        for i in self.技能栏:
            try : 
                站街魔法攻击 *= i.魔法攻击力倍率(self.武器类型)
            except : 
                pass
        if x == 1:
            return 站街魔法攻击
        else:
            return 站街魔法攻击 * (self.站街智力() / 250 + 1)

    def 站街独立攻击力(self):
        站街独立攻击 = self.独立攻击力
        for i in self.技能栏:
            try : 
                站街独立攻击 *= i.独立攻击力倍率(self.武器类型)
            except : 
                pass
        return 站街独立攻击
    
    #一键修正站街三攻倍率
    def 站街物理攻击力倍率(self):
        站街物理攻击倍率 =  1.0
        for i in self.技能栏:
            try :
                站街物理攻击倍率 *= i.物理攻击力倍率(self.武器类型)
            except :
                pass
        return 站街物理攻击倍率

    def 站街魔法攻击力倍率(self):
        站街魔法攻击倍率 =  1.0
        for i in self.技能栏:
            try :
                站街魔法攻击倍率 *= i.魔法攻击力倍率(self.武器类型)
            except :
                pass
        return 站街魔法攻击倍率

    def 站街独立攻击力倍率(self):
        站街独立攻击倍率 = 1.0
        for i in self.技能栏:
            try :
                站街独立攻击倍率 *= i.独立攻击力倍率(self.武器类型)
            except :
                pass
        return 站街独立攻击倍率

    def 等级溢出判断(self, 装备, 套装):
        self.穿戴装备(装备, 套装)
        self.装备词条计算()
        temp = []
        for i in self.技能栏:
            if i.等级溢出 == 1:
                temp.append(i.名称)
        return temp

    def 装备词条计算(self):
        for i in range(11):
            装备列表[装备序号[self.装备栏[i]]].城镇属性(self)

        if 武器序号 == -1:
            装备列表[装备序号[self.装备栏[11]]].城镇属性(self)
        else:
            装备列表[武器序号].城镇属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].城镇属性(self)

        #进图触发属强向下取整
        self.状态 = 1
        for i in range(11):
            装备列表[装备序号[self.装备栏[i]]].进图属性(self)

        if 武器序号 == -1:
            装备列表[装备序号[self.装备栏[11]]].进图属性(self)
        else:
            装备列表[武器序号].进图属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].进图属性(self)
        self.状态 = 0

        #冲突属性计算
        self.伤害增加加成(self.黄字)
        self.暴击伤害加成(self.爆伤)
        
        #光环属性计算
        if self.战术技能BUFF:
            self.技能等级加成('所有', 60, 80, 3)
        if self.兵法技攻BUFF:
            self.技能攻击力加成(0.10)

    def 装备属性计算(self):
        self.装备基础()
        self.装备词条计算()
    
    def 其它属性计算(self):
        for i in range(11):
            装备列表[装备序号[self.装备栏[i]]].其它属性(self)

        if 武器序号 == -1:
            装备列表[装备序号[self.装备栏[11]]].其它属性(self)
        else:
            装备列表[武器序号].其它属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].其它属性(self)

class 角色窗口(QWidget):
    calc_done_signal = pyqtSignal()
    update_remaining_signal = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()

        self.calc_done_signal.connect(self.calc_done)
        self.update_remaining_signal.connect(self.update_remaining)

        self.窗口属性输入()
        self.界面()
        self.布局界面()

        #创建配置文件夹
        path = './ResourceFiles/'+self.角色属性A.实际名称 + '/set'
        if not os.path.exists(path):
            os.makedirs(path) 

        #判断从哪读取数据
        if os.path.exists(path + '/attr.ini'):
            self.载入配置()
        else:
            self.载入配置('reset')
            
        self.click_window(0)

    def 关闭窗口(self):
        self.close()

    def closeEvent(self, event):
        self.保存配置()
        self.排行窗口列表.clear()
        super().closeEvent(event)

    def 窗口属性输入(self):
        pass
    
    def 界面(self):
        self.setWindowTitle(self.角色属性A.实际名称 + "搭配计算器 （点击标签栏按钮切换界面）")
        self.icon = QIcon('./ResourceFiles/'+self.角色属性A.实际名称 + '/技能/BUFF.png')
        self.setWindowIcon(self.icon)

        self.setStyleSheet('''QToolTip { 
                   background-color: black; 
                   color: white; 
                   border: 0px
                   }''')

        #窗口大小
        count = 0
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                count += 1
        self.窗口高度 = max(55 + 30 * count, 680)
        self.setFixedSize(1120, self.窗口高度)

        背景颜色 = QLabel(self)
        背景颜色.resize(self.width(),self.height())
        背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1)}")

        主背景透明度 = QGraphicsOpacityEffect()
        主背景透明度.setOpacity(0.15)
        self.主背景图片 = QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/bg.jpg")
        主背景 = QLabel(self)
        主背景.setPixmap(self.主背景图片)
        主背景.move(0, int((self.height() - 1230) / 6))
        主背景.setGraphicsEffect(主背景透明度)

        self.技能图片 = []
        for i in self.角色属性A.技能栏:
            path = './ResourceFiles/'+self.角色属性A.实际名称 + "/技能/" + i.名称 + ".png"
            self.技能图片.append(QPixmap(path))
        
        self.输出窗口列表 = []
        self.排行窗口列表 = []

        self.当前页面 = 0
        self.全选状态 = 0

        self.装备图片 = []
        self.遮罩透明度 = []
        self.装备图片按钮 = []
        for i in 装备列表:
            self.遮罩透明度.append(QGraphicsOpacityEffect())
            self.装备图片按钮.append('')
        self.装备选择状态 = []
        self.装备条件选择 = []
        for i in 装备列表:
            path = './ResourceFiles/img/装备/' + str(装备序号[i.名称]) + '.gif'
            self.装备图片.append(QMovie(path))
            self.装备选择状态.append(0)
        self.输出背景图片 = QPixmap('./ResourceFiles/img/输出背景.png')
        self.有效防具套装 = []
        self.有效首饰套装 = []
        self.有效特殊套装 = []
        self.有效上链左套装 = []
        self.有效镯下右套装 = []
        self.有效环鞋指套装 = []
        self.有效总套装列表 = [self.有效防具套装, self.有效首饰套装, self.有效特殊套装, self.有效上链左套装, self.有效镯下右套装, self.有效环鞋指套装]
        self.有效武器列表 = []
        self.组合名称选择 = []
        self.有效穿戴组合 = []
        self.有效穿戴套装 = []
        self.百变怪列表 = []
        self.有效部位列表 = []
        self.排行数据 = []

        # 工具栏
        self.frame_tool = QFrame(self)
        self.frame_tool.setGeometry(0, 0, self.width(), 24)

        self.页面名称 = ["装备/选择/打造", "技能/符文/其它", "基础/细节/修正","神话属性修正","自选装备计算"]
        self.页面数量 = len(self.页面名称)
        self.btn_group = QButtonGroup(self.frame_tool)
        self.window_btn = []
        for i in range(0, self.页面数量):
            self.window_btn.append(QToolButton(self.frame_tool))
            self.window_btn[-1].setText(self.页面名称[i])
            self.window_btn[-1].resize(int(self.width() / self.页面数量), 24)
            self.window_btn[-1].move(self.window_btn[-1].width() * i, 0)
            self.window_btn[-1].clicked.connect(lambda state, index = i: self.click_window(index))
            self.btn_group.addButton(self.window_btn[-1], i)

        # 2. 工作区域
        self.main_frame = QFrame(self)
        self.main_frame.setGeometry(0, 25, self.width(), self.height() - self.frame_tool.height())

        # 创建堆叠布局
        self.stacked_layout = QStackedLayout(self.main_frame)
        
        self.main_frame1 = QMainWindow()
        self.main_frame2 = QMainWindow()
        self.main_frame3 = QMainWindow()
        self.main_frame4 = QMainWindow()
        self.main_frame5 = QMainWindow()

        self.界面1()
        self.界面2()
        self.界面3()
        self.界面4()
        self.界面5()
    
    def 布局界面(self):
        # 把布局界面放进去
        self.stacked_layout.addWidget(self.main_frame1)
        self.stacked_layout.addWidget(self.main_frame2)
        self.stacked_layout.addWidget(self.main_frame3)
        self.stacked_layout.addWidget(self.main_frame4)
        self.stacked_layout.addWidget(self.main_frame5)

    def 界面1(self):
        # 第一个布局界面
        self.一键站街设置输入 = []

        水平间距 = [0, 350, 640]
        counter1 = 0
        for 布局列表 in [防具套装, 上链左套装 + 镯下右套装 + 环鞋指套装 , 首饰套装 + 特殊套装]:
            counter2 = 0
            for 名称 in 布局列表:
                for i in 套装列表:
                    if i.名称 == 名称 and i.件数 == 2:
                        self.按钮 = QPushButton(i.名称, self.main_frame1)
                        self.按钮.move(水平间距[counter1] + 10, 10 + counter2 * 32)
                        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
                        self.按钮.resize(120, 28)
                        self.按钮.clicked.connect(lambda state, index = i.名称: self.套装按钮点击事件(index))
                        temp = ''
                        temp += '<font size="3" face="宋体"><font color="#78FF1E">' + i.名称 + '[2]</font><br>'
                        temp += 套装列表[套装序号[i.名称 + '[2]']].装备描述(self.角色属性A)[:-4]
                        temp += '<br><font color="#78FF1E">' + i.名称 + '[3]</font><br>'
                        temp += 套装列表[套装序号[i.名称 + '[3]']].装备描述(self.角色属性A)[:-4]
                        try:
                            x = 套装列表[套装序号[i.名称 + '[5]']].装备描述(self.角色属性A)[:-4]
                            temp += '<br><font color="#78FF1E">' + i.名称 + '[5]</font><br>'
                            temp +=  x           
                        except:
                            pass
                        temp += '</font>'
                        self.按钮.setToolTip(temp)            
                        counter3 = 0
                        for 品质 in ['神话', '史诗']:
                            for 部位 in ['上衣', '头肩', '下装', '鞋', '腰带', '项链', '手镯', '戒指', '辅助装备', '魔法石', '耳环']:
                                for j in range(0,len(装备列表)):
                                    if 装备列表[j].所属套装 == i.名称 and 装备列表[j].品质 == 品质 and 装备列表[j].部位 == 部位 :
                                        self.图片 = QLabel(self.main_frame1)
                                        self.图片.setMovie(self.装备图片[j])
                                        self.装备图片[j].start()
                                        self.图片.resize(28, 28)
                                        self.图片.move(水平间距[counter1] + 150 + 32 * counter3, 10 + counter2 * 32)
                                        self.按钮 = QPushButton(self.main_frame1)
                                        self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                                        self.按钮.resize(28, 28)
                                        self.按钮.setToolTip('<font size="3" face="宋体"><font color="' + 颜色[装备列表[j].品质] + '">' +装备列表[j].名称+'</font><br>'+ 装备列表[j].类型 + '-' + 装备列表[j].部位 + '<br>' + 装备列表[j].装备描述(self.角色属性A)[:-4] + '</font>')
                                        self.遮罩透明度[j].setOpacity(0.5)
                                        self.按钮.setGraphicsEffect(self.遮罩透明度[j])
                                        self.按钮.clicked.connect(lambda state, index = j: self.装备图标点击事件(index, 10))
                                        self.装备图片按钮[j] = self.按钮
                                        self.装备图片按钮[j].move(水平间距[counter1] + 150 + 32 * counter3, 10 + counter2 * 32)
                                        counter3 += 1
                counter2 += 1
            counter1 += 1
        
        counter5 = 8
        self.按钮 = QPushButton('武器列表', self.main_frame1)
        self.按钮.move(650, 15 + counter5 * 32)
        self.按钮.resize(265,28)
        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
        self.按钮.clicked.connect(lambda state, index = '无': self.套装按钮点击事件(index))
        
        counter4 = 0
        counter5 += 1
        for i in 装备列表:
            if i.部位 == '武器' and i.类型 in self.角色属性A.武器选项 and i.模式 == 0:
                self.图片 = QLabel(self.main_frame1)
                self.图片.setMovie(self.装备图片[装备序号[i.名称]])
                self.装备图片[装备序号[i.名称]].start()
                self.图片.resize(28, 28)
                self.图片.move(657 + 55 * counter4, 15 + counter5 * 32)
                self.按钮 = QPushButton(self.main_frame1)
                self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.按钮.resize(28, 28)
                self.按钮.setToolTip('<font size="3" face="宋体"><font color="' + 颜色[i.品质] + '">' +i.名称+'</font><br>'+ i.类型 + '-' + i.部位 + '<br>' + i.装备描述(self.角色属性A)[:-4] + '</font>')
                self.遮罩透明度[装备序号[i.名称]].setOpacity(0.5)
                self.按钮.setGraphicsEffect(self.遮罩透明度[装备序号[i.名称]])
                self.按钮.clicked.connect(lambda state, index = 装备序号[i.名称]: self.装备图标点击事件(index, 10))
                self.装备图片按钮[装备序号[i.名称]] = self.按钮
                self.装备图片按钮[装备序号[i.名称]].move(657 + 55 * counter4, 15 + counter5 * 32)
                counter4 += 1
                if counter4 % 5 == 0:
                    counter5 += 1
                    counter4 = 0
        
        if counter4 != 0:
            counter5 += 1
        self.按钮 = QPushButton('智慧产物', self.main_frame1)
        self.按钮.move(650, 20 + counter5 * 32)
        self.按钮.resize(265,28)
        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
        self.按钮.clicked.connect(lambda state, index = '智慧产物': self.套装按钮点击事件(index))
        
        counter4 = 0
        counter5 += 1
        for i in 装备列表:
            if i.所属套装 == '智慧产物' and i.部位 != '武器' and i.模式 == 0:
                self.图片 = QLabel(self.main_frame1)
                self.图片.setMovie(self.装备图片[装备序号[i.名称]])
                self.装备图片[装备序号[i.名称]].start()
                self.图片.resize(28, 28)
                self.图片.move(657 + 55 * counter4, 20 + counter5 * 32)
                self.按钮 = QPushButton(self.main_frame1)
                self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.按钮.resize(28, 28)
                self.按钮.setToolTip('<font size="3" face="宋体"><font color="' + 颜色[i.品质] + '">' +i.名称+'</font><br>'+ i.类型 + '-' + i.部位 + '<br>' + i.装备描述(self.角色属性A)[:-4] + '</font>')
                self.遮罩透明度[装备序号[i.名称]].setOpacity(0.5)
                self.按钮.setGraphicsEffect(self.遮罩透明度[装备序号[i.名称]])
                self.按钮.clicked.connect(lambda state, index = 装备序号[i.名称]: self.装备图标点击事件(index, 10))
                self.装备图片按钮[装备序号[i.名称]] = self.按钮
                self.装备图片按钮[装备序号[i.名称]].move(657 + 55 * counter4, 20 + counter5 * 32)
                counter4 += 1
                if counter4 % 5 == 0:
                    counter5 += 1
                    counter4 = 0
        
        标签 = QLabel('装备条件设置', self.main_frame1)
        标签.move(940, 5)
        标签.resize(170,20)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        self.装备条件选择.clear()
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['角色熟练度：英雄', '角色熟练度：传说'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['技能栏空位：0', '技能栏空位：1', '技能栏空位：2', '技能栏空位：3', '技能栏空位：4', '技能栏空位：5', '技能栏空位：6'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['命运的抉择：数学期望', '命运的抉择：黄字+35%', '命运的抉择：爆伤+35%', '命运的抉择：白字+35%', '命运的抉择：终伤+35%', '命运的抉择：三攻+35%'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['骰子：数学期望', '骰子：1点', '骰子：2点', '骰子：3点', '骰子：4点', '骰子：5点', '骰子：6点'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['悲剧的残骸：数学期望', '悲剧的残骸：HP高于70%', '悲剧的残骸：HP70-30%', '悲剧的残骸：HP低于30%'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['先知者预言：数学期望', '先知者预言：属白+5%', '先知者预言：技攻+10%', '先知者预言：技攻+15%'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['贫瘠沙漠的遗产：无', '贫瘠沙漠的遗产：霸体', '贫瘠沙漠的遗产：无伤'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['幸运三角：数学期望', '幸运三角：7效果', '幸运三角：77效果', '幸运三角：777效果'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['擎天战甲：过充电状态', '擎天战甲：过负荷状态'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        for i in range(101):
            self.装备条件选择[-1].addItem('持续伤害适用：' + str(100 - i) + '%')
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['军神的隐秘遗产：120%以上', '军神的隐秘遗产：120-100%', '军神的隐秘遗产：100-80%', '军神的隐秘遗产：80-60%', '军神的隐秘遗产：60-40%', '军神的隐秘遗产：40%以下'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['太极天帝剑：阳', '太极天帝剑：阴'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['绿色生命的面容：无', '绿色生命的面容：阴暗面'])
        for i in range(0, len(self.装备条件选择)):
            self.装备条件选择[i].resize(170, 20)
            self.装备条件选择[i].move(940, 30 + 28 * i)


        self.装备打造选项=[]
        counter = 0
        for i in 部位列表:
            x = QLabel(i, self.main_frame1)
            x.resize(50,20)
            x.setAlignment(Qt.AlignCenter)
            x.setStyleSheet(标签样式)
            if counter < 5:
                x.move(10 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(270 , 500 + (counter - 5) * 25)
                else:
                    x.resize(95,20)
                    x.move(550 , 500 + (counter - 11) * 30)
            counter += 1

        counter = 0
        for i in 部位列表:
            x = MyQComboBox(self.main_frame1)
            x.addItems(['强化','增幅'])
            x.resize(55,20)
            self.装备打造选项.append(x)
            if counter < 5:
                x.move(60 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(330 , 500 + (counter - 5) * 25)
                else:
                    x.move(540 , 500 + (counter - 10) * 30)
            counter += 1
            
        counter = 0
        for i in 部位列表:
            x = MyQComboBox(self.main_frame1)
            for j in range(0,32):
                x.addItem(str(j))
            x.resize(50,20)
            self.装备打造选项.append(x)
            if counter < 5:
                x.move(120 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(390 , 500 + (counter - 5) * 25)
                else:
                    x.move(600 , 500 + (counter - 10) * 30)
            counter += 1

        counter = 0
        for i in 部位列表:
            x = MyQComboBox(self.main_frame1)
            for j in range(0,32):
                x.addItem('改造+' + str(j))
            x.resize(75,20)
            self.装备打造选项.append(x)
            if counter < 5:
                x.move(180 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(450 , 500 + (counter - 5) * 25)
                else:
                    x.resize(110,20)
                    x.move(540 , 500 + (counter - 9) * 30)
            counter += 1

        x = MyQComboBox(self.main_frame1)
        for j in range(0,11):
            x.addItem('锻造+' + str(j))
        x.resize(110,20)
        x.move(540 , 504 + (counter - 9) * 30)
        self.装备打造选项.append(x)

        x = MyQComboBox(self.main_frame1)
        x.addItems(self.角色属性A.伤害类型选择)
        x.resize(110,20)
        x.move(540 , 504 + (counter - 8) * 30)
        self.装备打造选项.append(x)

        self.称号 = MyQComboBox(self.main_frame1)
        for i in 称号列表:
            self.称号.addItem(i.名称)
        
        self.宠物 = MyQComboBox(self.main_frame1)
        for i in 宠物列表:
            self.宠物.addItem(i.名称)

        x = QLabel('称号&宠物选择：', self.main_frame1)
        x.resize(130,20)
        x.move(360 , 400)
        x.setAlignment(Qt.AlignCenter)
        x.setStyleSheet(标签样式)
        
        counter = 0
        for x in [self.称号, self.宠物]:
            x.resize(160,20)
            x.move(350 , 430 + counter * 30)
            counter += 1    

        x = QPushButton('一键全选', self.main_frame1)
        x.clicked.connect(lambda state, index = 1: self.批量选择(index))
        x.move(520 , 400)
        x.resize(105, 24)
        x.setStyleSheet(按钮样式)

        x = QPushButton('一键清空',self.main_frame1)
        x.clicked.connect(lambda state, index = 0: self.批量选择(index))
        x.move(520 , 430)
        x.resize(105, 24)
        x.setStyleSheet(按钮样式)

        x = QPushButton('打造↑',self.main_frame1)
        x.clicked.connect(lambda state: self.批量打造(1))
        x.move(520 , 460)
        x.resize(50, 24)
        x.setStyleSheet(按钮样式)

        x = QPushButton('打造↓',self.main_frame1)
        x.clicked.connect(lambda state: self.批量打造(-1))
        x.move(575 , 460)
        x.resize(50, 24)
        x.setStyleSheet(按钮样式)

        self.百变怪选项 = QCheckBox('百变怪   ', self.main_frame1)
        self.百变怪选项.move(660, 613)
        self.百变怪选项.resize(80, 24)
        self.百变怪选项.setToolTip('<font size="3" face="宋体">仅在极速模式和套装模式下生效</font>')
        self.百变怪选项.setStyleSheet(复选框样式)

        self.计算模式选择 = MyQComboBox(self.main_frame1)
        self.计算模式选择.addItems(['计算模式：极速模式', '计算模式：套装模式', '计算模式：单件模式'])
        self.计算模式选择.move(750, 613)
        self.计算模式选择.resize(235, 24)
        self.计算模式选择.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QComboBox:hover{background-color:rgba(65,105,225,0.8)}")
        self.计算模式选择.setToolTip('<font size="3" face="宋体">极速模式：533和3332(散搭) (不含智慧产物)<br><br>套装模式：533、3332(散搭)和3233(双防具) (不含智慧产物)<br><br>单件模式：所有组合 (不含百变怪)</font>')
        
        self.最大使用线程数 = 工作线程数

        self.线程数选择 = MyQComboBox(self.main_frame1)
        self.线程数选择.move(660, 580)
        self.线程数选择.resize(80, 24)
        for i in range(工作线程数, 0, -1):
            self.线程数选择.addItem('进程:' + str(i))

        self.攻击属性选项 = MyQComboBox(self.main_frame1)
        self.攻击属性选项.move(750, 580)
        self.攻击属性选项.resize(120, 24)
        self.攻击属性选项.addItem('攻击属性：最高')
        self.攻击属性选项.addItem('攻击属性：火')
        self.攻击属性选项.addItem('攻击属性：冰')
        self.攻击属性选项.addItem('攻击属性：光')
        self.攻击属性选项.addItem('攻击属性：暗')

        self.神话排名选项 = QCheckBox('神话排名模式', self.main_frame1)
        self.神话排名选项.move(880, 580)
        self.神话排名选项.resize(100, 24)
        self.神话排名选项.setToolTip('<font size="3" face="宋体">仅显示有神话的组合，且每件神话装备只会出现一次</font>')
        self.神话排名选项.setStyleSheet(复选框样式)

        self.显示选项 = QCheckBox('亿为单位显示', self.main_frame1)
        self.显示选项.move(990, 580)
        self.显示选项.resize(100, 24)
        self.显示选项.setStyleSheet(复选框样式)

        #一键修正按钮添加
        一键站街修正名称 = ['站街力智', '站街三攻', '站街属强']
        for i in range(0, len(一键站街修正名称)):
            名称 = QLabel(一键站街修正名称[i], self.main_frame1)
            名称.setAlignment(Qt.AlignCenter)
            名称.move(940 + i*57, 400)
            名称.resize(52, 25)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            self.一键站街设置输入.append(QLineEdit(self.main_frame1))
            self.一键站街设置输入[i].setAlignment(Qt.AlignCenter)
            self.一键站街设置输入[i].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            self.一键站街设置输入[i].resize(52, 22)
            self.一键站街设置输入[i].move(940 + i*57, 430)

        一键修正按钮 = QPushButton('一键修正面板细节', self.main_frame1)
        一键修正按钮.clicked.connect(lambda state: self.一键修正())
        一键修正按钮.move(940, 460)
        一键修正按钮.resize(170, 25)
        一键修正按钮.setStyleSheet(按钮样式)

        self.红色宠物装备 = QCheckBox('红色宠物装备', self.main_frame1)
        self.红色宠物装备.move(1010, 505)
        self.红色宠物装备.resize(100, 24)
        self.红色宠物装备.setStyleSheet(复选框样式)
        self.红色宠物装备.setToolTip('<font size="3" face="宋体">7%黄字，7%力智，8%白字取最高值<br><br>勾选后禁用第三页红色宠物装备白字数值输入</font>')
        
        self.禁用存档 = QCheckBox('禁用自动存档', self.main_frame1)
        self.禁用存档.move(1010, 540)
        self.禁用存档.resize(100, 24)
        self.禁用存档.setStyleSheet(复选框样式)

        self.韩服面板 = QCheckBox('韩服面板', self.main_frame1)
        self.韩服面板.move(920, 540)
        self.韩服面板.resize(80, 24)
        self.韩服面板.setStyleSheet(复选框样式)

        重置按钮 = QPushButton('全局重置', self.main_frame1)
        重置按钮.clicked.connect(lambda state: self.全局重置())
        重置按钮.move(920, 505)
        重置按钮.resize(80, 24)
        重置按钮.setStyleSheet(按钮样式)
        
        self.计算按钮1 = QPushButton('开始计算', self.main_frame1)
        self.计算按钮1.clicked.connect(lambda state: self.计算())
        self.计算按钮1.move(990, 610)
        self.计算按钮1.resize(100, 30)
        self.计算按钮1.setStyleSheet(按钮样式)

    def 界面2(self):
        # 第二个布局界面
        
        #技能等级、TP、次数输入、宠物次数
        self.BUFF输入 = QLineEdit(self.main_frame2)
        self.时间输入 = MyQComboBox(self.main_frame2)
        self.护石栏 = []
        for i in range(3):
            self.护石栏.append(MyQComboBox(self.main_frame2))
        self.符文 = []
        self.符文效果 = []

        self.觉醒选择状态 = 2
        
        self.等级调整 = []
        self.TP输入 = []
        self.次数输入 = []
        self.宠物次数 = []

        if 切装模式 == 1:
            self.技能切装 = []
        
        count = 0
        for i in self.角色属性A.技能栏:
            i.等级 = i.基础等级
            self.等级调整.append(MyQComboBox(self.main_frame2))
            self.等级调整[count].currentIndexChanged.connect(lambda state, index = count:self.等级调整标注(index))
            count += 1
            if i.是否有伤害 == 1 and i.TP上限 != 0:
                self.TP输入.append(MyQComboBox(self.main_frame2))
            else:
                self.TP输入.append('')
            if i.是否有伤害 == 1:
                self.次数输入.append(MyQComboBox(self.main_frame2))
                self.宠物次数.append(MyQComboBox(self.main_frame2))
                if 切装模式 == 1:self.技能切装.append(QCheckBox(self.main_frame2))
            else:
                self.次数输入.append('')
                self.宠物次数.append('')
                if 切装模式 == 1:self.技能切装.append('')
        
        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.所在等级 == 50 or i.所在等级 == 85:
                for j in range(0, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
            else:
                for j in range(- i.基础等级, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
        
            if i.是否有伤害 == 1 and i.TP上限 != 0:
                for j in range(0, i.TP上限+1):
                    self.TP输入[序号].addItem(str(j))
        
            if i.是否有伤害 == 1:
                self.次数输入[序号].addItem('/CD')
                for j in range(0, 100):
                    self.次数输入[序号].addItem(str(j))
                    self.宠物次数[序号].addItem(str(j))
        
        #三觉强化选择
        self.一觉遮罩透明度 = QGraphicsOpacityEffect()
        self.一觉遮罩透明度.setOpacity(0.5)
        self.二觉遮罩透明度 = QGraphicsOpacityEffect()
        self.二觉遮罩透明度.setOpacity(0.0)

        横坐标=10
        纵坐标=0
        横坐标偏移量=60
        纵坐标偏移量=30
        词条框宽度=48
        行高 = 20
        
        counter=0
        for i in ["契约满级","等级调整"," TP等级","释放次数","宠物次数"]:
            x=QLabel(i, self.main_frame2)
            x.move(横坐标+横坐标偏移量-30+50*counter,纵坐标)
            x.setStyleSheet(标签样式)
            counter+=1
        
        纵坐标+=20
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                x=QLabel(self.main_frame2)
                x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
                x.resize(28,28)
                tempstr='<font face="宋体"><font color="#FF6666">'+i.名称 +i.备注 +'</font><br>'
                tempstr+='所在等级：'+str(i.所在等级)+'<br>'
                tempstr+='等级上限：'+str(i.等级上限)
                if i.是否主动 == 1:
                    tempstr+='<br>百分比：'+str(int(i.等效百分比(self.角色属性A.武器类型)))+'%'
                    if i.TP上限 !=0:
                        tempstr+='<br>TP成长：'+str(int(i.TP成长*100))+'%'
                        tempstr+='<br>TP上限：'+str(i.TP上限)
                tempstr += '</font>'
                x.setToolTip(tempstr)
                x.move(横坐标,纵坐标+7)
                横坐标+=40
                x=QLabel('Lv'+str(i.基础等级), self.main_frame2)
                x.resize(40,28)
                x.move(横坐标,纵坐标+7)
                x.setStyleSheet(标签样式)
                横坐标+=40
                self.等级调整[self.角色属性A.技能序号[i.名称]].resize(词条框宽度,行高)
                self.等级调整[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标+10)
                横坐标-=80
                纵坐标+=纵坐标偏移量
        
        横坐标=横坐标+80+50
        纵坐标=30
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                if i.TP上限!=0:
                    self.TP输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                    self.TP输入[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标)
                纵坐标+=纵坐标偏移量
        
        横坐标=横坐标+50
        纵坐标=30
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                self.次数输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                self.次数输入[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标)
                self.宠物次数[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                self.宠物次数[self.角色属性A.技能序号[i.名称]].move(横坐标+50,纵坐标)
                if 切装模式 == 1:self.技能切装[self.角色属性A.技能序号[i.名称]].move(横坐标+55+词条框宽度,纵坐标 - 5)
                纵坐标+=纵坐标偏移量

        横坐标=横坐标+130
        纵坐标=20
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 0:
                x=QLabel(self.main_frame2)
                x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
                x.resize(28,28)
                tempstr='<font face="宋体"><font color="#FF6666">'+i.名称 +i.备注 +'</font><br>'
                tempstr+='所在等级：'+str(i.所在等级)+'<br>'
                tempstr+='等级上限：'+str(i.等级上限)
                tempstr += '</font>'
                x.setToolTip(tempstr)
                x.move(横坐标,纵坐标+7)
                横坐标+=40
                x=QLabel('Lv'+str(i.基础等级), self.main_frame2)
                x.resize(40,28)
                x.move(横坐标,纵坐标+7)
                x.setStyleSheet(标签样式)
                横坐标+=40
                self.等级调整[self.角色属性A.技能序号[i.名称]].resize(词条框宽度,行高)
                self.等级调整[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标+10)
                横坐标-=80
                纵坐标+=纵坐标偏移量
        
        x=横坐标+20;y=纵坐标+60
        self.觉醒选择=QLabel(self.main_frame2)
        self.觉醒选择.setPixmap(QPixmap('./ResourceFiles/img/觉醒选择.png'))
        self.觉醒选择.resize(120,100)
        self.觉醒选择.move(x,y-20)
        
        self.BUFF=QLabel(self.main_frame2)
        self.BUFF.setPixmap(QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/技能/BUFF.png"))
        self.BUFF.resize(28,28)
        self.BUFF.move(x-2,y-40)
        self.BUFF.setToolTip('<font size="3" face="宋体">最高值参考：' + str('%.1f' % ((self.角色属性A.主BUFF - 1) * 100)) + '</font>')
        
        self.BUFF输入.setText(str('%.1f' % ((self.角色属性A.主BUFF - 1) * 100)))
        self.BUFF输入.resize(50, 25)
        self.BUFF输入.move(x+38,y-38)
        self.BUFF输入.setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QLineEdit:hover{background-color:rgba(65,105,225,0.8)}")
        self.BUFF输入.setAlignment(Qt.AlignCenter)
        
        self.一觉图片=QLabel(self.main_frame2)
        self.一觉图片.setPixmap(self.技能图片[self.一觉序号])
        self.一觉图片.resize(28,28)
        self.一觉图片.move(x+7,y+8)
        self.二觉图片=QLabel(self.main_frame2)
        self.二觉图片.setPixmap(self.技能图片[self.二觉序号])
        self.二觉图片.resize(28,28)
        self.二觉图片.move(x+52,y+8)
        self.一觉遮罩=QPushButton(self.main_frame2)
        self.一觉遮罩.resize(38,50)
        self.一觉遮罩.move(x+2,y+5)
        self.一觉遮罩.setStyleSheet("QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}")
        self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
        self.一觉遮罩.clicked.connect(lambda state, index = 1:self.强化觉醒选择(index))
        self.二觉遮罩=QPushButton(self.main_frame2)
        self.二觉遮罩.resize(38,50)
        self.二觉遮罩.move(x+47,y+5)
        self.二觉遮罩.setStyleSheet("QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}")
        self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)
        self.二觉遮罩.clicked.connect(lambda state, index = 2:self.强化觉醒选择(index))

        for i in range(3):
            self.护石栏[i].addItems(self.护石选项)
        self.护石类型选项 = []

        for i in range(0,9):
            self.符文.append(MyQComboBox(self.main_frame2))
            self.符文[i].addItems(self.符文选项)
            self.符文效果.append(MyQComboBox(self.main_frame2))
            self.符文效果[i].addItems(符文效果选项)
        
        横坐标=480;纵坐标=20;行高=18
        x=QLabel("护石1 (上)", self.main_frame2)
        x.move(横坐标,纵坐标 - 6)
        x.setStyleSheet(标签样式)
        y = MyQComboBox(self.main_frame2)
        y.move(横坐标 + 65,纵坐标)
        y.resize(65, 行高)
        self.护石类型选项.append(y)     
        纵坐标+=21
        self.护石栏[0].move(横坐标,纵坐标)
        self.护石栏[0].resize(130, 行高)
        self.护石栏[0].currentIndexChanged.connect(lambda state, index = 0:self.护石类型选项更新(index))
        纵坐标+=25
        for i in range(0,3):
            tempstr='符文'+str(i+1)+'选择: '
            x=QLabel(tempstr, self.main_frame2)
            x.move(横坐标,纵坐标-5)
            x.setStyleSheet(标签样式)
            纵坐标+=21
            self.符文[i].move(横坐标,纵坐标)
            self.符文[i].resize(130, 行高)
            self.符文[i].activated.connect(lambda state, index = i :self.符文技能更改(index))
            纵坐标+=21
            self.符文效果[i].move(横坐标,纵坐标)
            self.符文效果[i].resize(130,行高)
            self.符文效果[i].activated.connect(lambda state, index = i :self.符文效果更改(index))
            纵坐标+=25
        
        横坐标=650;纵坐标=20
        x=QLabel("护石2 (下)", self.main_frame2)
        x.move(横坐标,纵坐标 - 6)
        x.setStyleSheet(标签样式)
        y = MyQComboBox(self.main_frame2)
        y.move(横坐标 + 65,纵坐标)
        y.resize(65, 行高)
        self.护石类型选项.append(y)  
        纵坐标+=21
        self.护石栏[1].move(横坐标,纵坐标)
        self.护石栏[1].resize(130, 行高)
        self.护石栏[1].currentIndexChanged.connect(lambda state, index = 1:self.护石类型选项更新(index))
        纵坐标+=25
        for i in range(3,6):
            tempstr='符文'+str(i+1)+'选择: '
            x=QLabel(tempstr, self.main_frame2)
            x.move(横坐标,纵坐标-5)
            x.setStyleSheet(标签样式)
            纵坐标+=21
            self.符文[i].move(横坐标,纵坐标)
            self.符文[i].resize(130, 行高)
            纵坐标+=21
            self.符文效果[i].move(横坐标,纵坐标)
            self.符文效果[i].resize(130,行高)
            纵坐标+=25

        横坐标=820;纵坐标=20
        x=QLabel("护石3 (韩)", self.main_frame2)
        x.move(横坐标,纵坐标 - 6)
        x.setStyleSheet(标签样式)
        y = MyQComboBox(self.main_frame2)
        y.move(横坐标 + 65,纵坐标)
        y.resize(65, 行高)
        self.护石类型选项.append(y)  
        纵坐标+=21
        self.护石栏[2].move(横坐标,纵坐标)
        self.护石栏[2].resize(130, 行高)
        self.护石栏[2].currentIndexChanged.connect(lambda state, index = 2:self.护石类型选项更新(index))
        纵坐标+=25
        for i in range(6,9):
            tempstr='符文'+str(i+1)+'选择: '
            x=QLabel(tempstr, self.main_frame2)
            x.move(横坐标,纵坐标-5)
            x.setStyleSheet(标签样式)
            纵坐标+=21
            self.符文[i].move(横坐标,纵坐标)
            self.符文[i].resize(130, 行高)
            纵坐标+=21
            self.符文效果[i].move(横坐标,纵坐标)
            self.符文效果[i].resize(130,行高)
            纵坐标+=25
        
        for i in range(3):
            self.护石类型选项[i].addItem('魔界')
            self.护石类型选项[i].currentIndexChanged.connect(lambda state, index = i:self.护石描述更新(index))

        标签 = QLabel('辟邪玉计算 （鼠标悬停查看算法）',self.main_frame2)
        标签.setStyleSheet(标签样式 + 'QLabel{font-size:13px;}')
        标签.resize(300,20)
        标签.move(480,275)
        标签.setAlignment(Qt.AlignCenter)

        temp = '<font face="宋体">假定基础伤害为100，词条1=50%，词条2=50%：<br><br>'
        temp += '5%黄字增幅，佩戴前：200，佩戴后：205<br>'
        temp += '爆伤终伤白字属白力智三攻同上，黄字向下取整<br>'
        temp += '技攻辟邪玉加成等级技攻(歧路腰类)<br>不加成具体技能技攻(歧路鞋类)<br><br>'
        temp += '3%技攻增幅，佩戴前：100*1.5*1.5=225<br>佩戴后：100*1.515*1.515=229.5225<br><br>'
        temp += '属强增幅：唤醒(13)婚房(8)药剂和技能属强不享受加成<br>'
        temp += '进图触发属强单独计算向下取整<br><br>'
        temp += '<font color="#B99460">属白增幅分对应属性，计算器未作区分<br>双属性附加(星之海)需手动计算并在第三页修正<br><br>计算方式仅供参考，请以实际游戏为准！</font></font>'

        标签.setToolTip(temp)

        self.辟邪玉选择 = []
        self.辟邪玉数值 = []
        for i in range(4):
            x = MyQComboBox(self.main_frame2) 
            for j in 辟邪玉列表:
                x.addItem(j.名称)
            x.resize(200,20)
            x.move(480,300 + i * 25)
            x.currentIndexChanged.connect(lambda state, index = i:self.辟邪玉数值选项更新(index))
            self.辟邪玉选择.append(x)
            y = MyQComboBox(self.main_frame2) 
            y.resize(80,20)
            y.move(700,300 + i * 25)
            self.辟邪玉数值.append(y)

        横坐标=805;纵坐标=275
        名称 = ['奈克斯', '暗杀者', '卢克西', '守门将', '罗德斯']
        self.希洛克套装按钮 = []
        self.希洛克单件按钮 = []
        self.希洛克遮罩透明度 = []
        self.希洛克选择状态 = [0] * 15 
        count = 0
        for i in 名称:
            self.希洛克套装按钮.append(QPushButton(i, self.main_frame2))
            self.希洛克套装按钮[count].setStyleSheet(按钮样式)
            self.希洛克套装按钮[count].resize(50,22)
            self.希洛克套装按钮[count].move(横坐标, 纵坐标 + 4 + count * 32)
            self.希洛克套装按钮[count].clicked.connect(lambda state, index = (count + 1) * 100:self.希洛克选择(index))
            for j in range(3):
                序号 = count * 3 + j
                图片 = QLabel(self.main_frame2)
                图片.setPixmap(QPixmap('./ResourceFiles/img/希洛克/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标+ 60 + j * 30, 纵坐标 + count * 32)
                self.希洛克遮罩透明度.append(QGraphicsOpacityEffect())
                self.希洛克遮罩透明度[序号].setOpacity(0.5)
                self.希洛克单件按钮.append(QPushButton(self.main_frame2))
                self.希洛克单件按钮[序号].setStyleSheet("background-color: rgb(0, 0, 0)")
                self.希洛克单件按钮[序号].resize(28, 28)
                self.希洛克单件按钮[序号].move(横坐标+ 60 + j * 30, 纵坐标 + count * 32)
                self.希洛克单件按钮[序号].setGraphicsEffect(self.希洛克遮罩透明度[序号])
                self.希洛克单件按钮[序号].clicked.connect(lambda state, index = 序号:self.希洛克选择(index))
            count += 1

        self.守门将属强 = MyQComboBox(self.main_frame2)
        for i in range(7):
            self.守门将属强.addItem('守门将属强：' + str(15 + i * 5))
        self.守门将属强.resize(120,20)
        self.守门将属强.setCurrentIndex(3)
        self.守门将属强.move(横坐标 + 12, 纵坐标 + 3 + count * 32)
                
        self.复选框列表 = []
        for i in 选项设置列表:
            self.复选框列表.append(QCheckBox(i.名称, self.main_frame2))

        counter=0

        for i in self.复选框列表:
            i.setStyleSheet(复选框样式)
            i.resize(125,20)
            i.move(980,10 + counter * 24)
            if counter < 7 and 调试开关 == 0:
                i.setChecked(True)
            counter+=1
        
        sign = 0
        if self.初始属性.远古记忆 != -1:
            i = QLabel(self.main_frame2)
            i.setPixmap(QPixmap('./ResourceFiles/img/远古记忆.png'))
            i.resize(28,28)
            i.move(1000, 15 + counter * 24)
            self.远古记忆 = MyQComboBox(self.main_frame2)
            self.远古记忆.currentIndexChanged.connect(lambda state, index = 100:self.等级调整标注(index))
            for i in range(12):
                self.远古记忆.addItem(str(i))
            self.远古记忆.resize(50,20)
            self.远古记忆.move(1035, 19 + counter * 24)
            sign = 30

        if self.初始属性.刀魂之卡赞 != -1:
            i = QLabel(self.main_frame2)
            i.setPixmap(QPixmap('./ResourceFiles/img/刀魂之卡赞.png'))
            i.resize(28,28)
            i.move(1000, 15 + sign + counter * 24)
            self.刀魂之卡赞 = MyQComboBox(self.main_frame2)
            self.刀魂之卡赞.currentIndexChanged.connect(lambda state, index = 200:self.等级调整标注(index))
            for i in range(12):
                self.刀魂之卡赞.addItem(str(i))
            self.刀魂之卡赞.resize(50,20)
            self.刀魂之卡赞.move(1035, 19 + sign + counter * 24)

        x=QLabel("时间输入：", self.main_frame2)
        x.move(850, self.height() - 62)
        x.resize(70, 20)
        x.setStyleSheet(标签样式)
        self.时间输入.addItems(['1', '10', '15', '20', '25', '30', '60'])
        self.时间输入.move(920, self.height() - 63)
        self.时间输入.resize(50, 20)

        self.特色选项 = QCheckBox('禁用国服等级', self.main_frame2)
        self.特色选项.move(990, self.height() - 100)
        self.特色选项.resize(100, 24)
        self.特色选项.setStyleSheet(复选框样式)
        self.特色选项.setToolTip('<font size="3" face="宋体">包含防具3宝珠+称号宝珠+光环&宠物的技能等级</font>')
        self.特色选项.stateChanged.connect(lambda state:self.特色选项提醒())

        self.计算按钮2 = QPushButton('开始计算', self.main_frame2)
        self.计算按钮2.clicked.connect(lambda state: self.计算())
        self.计算按钮2.move(990, self.height() - 70)
        self.计算按钮2.resize(100, 30)
        self.计算按钮2.setStyleSheet(按钮样式)

    def 界面3(self):
        # 第三个布局界面
        self.属性设置输入 = []
        self.技能设置输入 = []

        宽度 = 43
        距离 = 10
        
        列名称1 = ["力量", "智力", "物攻", "魔攻", "独立", "属强", "白字"]
        行名称1 = ["工会属性", "训练官BUFF", "戒指", "婚房", "冒险团", "晶体契约", "收集箱", "勋章", "名称装饰卡", "副武器/盾牌", "快捷栏纹章", "  宠物装备-红  ", "  宠物装备-蓝  ", "  宠物装备-绿  ", "宠物附魔", "站街修正", "进图修正"]
        名称 = QLabel("基础细节",self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
        名称.resize(80, 25)
        名称.move(10, 距离)
       
        for i in range(0, 7):
            名称 = QLabel(列名称1[i],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(宽度, 25)
            名称.move(95 + i*(宽度 + 5), 距离)
    
        for j in range(0, 17):
            名称 = QLabel(行名称1[j],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            if j in [1, 5, 10, 16]:
                名称.setStyleSheet("QLabel{font-size:12px;color:yellow;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            else:
                名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(80, 25)
            名称.move(10, 距离 + 30 + j*30)
        
        #1 5 10 16 为站街属性
        for i in range(0, 7):
            Linelist = []
            for j in range(0, 17):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                if j in [1, 5, 10, 16]:
                    Linelist[j].setStyleSheet("QLineEdit{font-size:12px;color:yellow;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                else:
                    Linelist[j].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(95 + i*(宽度 + 5), 距离 + 30 + j*30)
            self.属性设置输入.append(Linelist)
    
        列名称2 = ["力量", "智力", "物攻", "魔攻", "独立", "属强", "徽力智", "徽三攻", "终伤", "技能"]
        行名称2 = ["上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "左槽", "右槽", "耳环", "武器", "称号", "光环", "武器装扮", "皮肤", "时装"]

        self.列名称 = 列名称1 + 列名称2
        self.行名称 = 行名称1 + 行名称2

        名称 = QLabel(" 附魔&徽章 ",self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
        名称.resize(80, 25)
        名称.move(140+7*宽度, 距离)
        for i in range(0, 10):
            名称 = QLabel(列名称2[i],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            if i == 9:
                名称.resize(150, 25)
            else:
                名称.resize(宽度, 25)
            名称.move(225+7*宽度 + i*(宽度 + 5),  距离)
    
        for j in range(0, 17):
            名称 = QLabel(行名称2[j],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(80, 25)
            名称.move(140+7*宽度, 距离 + 30 + j*30)
    
        for i in range(0, 9):
            Linelist = []
            for j in range(0, 17):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(225+7*宽度 + i*(宽度 + 5), 距离 + 30 + j*30)
            self.属性设置输入.append(Linelist)
    
        for j in range(0, 17):
            self.技能设置输入.append(MyQComboBox(self.main_frame3))
            self.技能设置输入[j].addItem('无')
            self.技能设置输入[j].setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            self.技能设置输入[j].resize(150, 22)
            self.技能设置输入[j].move(225+7*宽度 + 9*(宽度 + 5), 距离 + 30 + j*30)
    
        for j in [2, 3, 4]:
            self.技能设置输入[j].addItems(['Lv1-30(主动)Lv+1', 'Lv1-50(主动)Lv+1'])

        self.技能设置输入[2].addItem('Lv1-35(主动)Lv+1')
    
        for j in [8, 9, 16]:
            for i in self.角色属性A.技能栏:
                self.技能设置输入[j].addItem(i.名称+'Lv+1')
        self.技能设置输入[12].addItem('Lv1-50(主动)Lv+1')
        self.技能设置输入[13].addItems(['Lv1-30(所有)Lv+1', 'Lv1-50(所有)Lv+1', 'Lv1-20(所有)Lv+1', 'Lv20-30(所有)Lv+1'])

        self.技能设置输入[12].addItem('Lv1-35(主动)Lv+1')

        self.修正列表名称 = ['力智%', '三攻%', '黄字', '白字', '属白', '爆伤', '终伤', '技攻']
        
        距离 = 20
        Linelist = []
        
        for i in range(0, len(self.修正列表名称)):
            名称 = QLabel(self.修正列表名称[i],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(45, 25)
            名称.move(距离 + i*50, 570)
            Linelist.append(QLineEdit(self.main_frame3))
            Linelist[i].setAlignment(Qt.AlignCenter)
            Linelist[i].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            Linelist[i].resize(45, 22)
            Linelist[i].move(距离 + i*50, 610)
        self.属性设置输入.append(Linelist)
        
        count = 0
        self.时装选项 = []
        for i in ['头部', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']:
            名称 = QLabel(i,self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(60, 25)
            名称.move(450 + count*65, 570)
            self.时装选项.append(MyQComboBox(self.main_frame3))
            self.时装选项[count].addItems(['高级', '节日', '稀有', '神器'])
            self.时装选项[count].resize(60, 22)
            self.时装选项[count].move(450 + count*65, 610)
            self.时装选项[count].currentIndexChanged.connect(lambda state, index = count:self.时装选项更新(index))
            count += 1

        self.时装选项.append(MyQComboBox(self.main_frame3))
        self.时装选项[8].addItems(['高级套装[8]', '节日套装[8]', '稀有套装[8]', '神器套装[8]'])
        self.时装选项[8].resize(100, 22)
        self.时装选项[8].move(990, 570)
        self.时装选项[8].currentIndexChanged.connect(lambda state, index = 8:self.时装选项更新(index))

        self.计算按钮3 = QPushButton('开始计算', self.main_frame3)
        self.计算按钮3.clicked.connect(lambda state: self.计算())
        self.计算按钮3.move(990, 610)
        self.计算按钮3.resize(100, 30)
        self.计算按钮3.setStyleSheet(按钮样式)

    def 界面4(self):
        #第四个布局
        self.神话属性选项 = []
        self.神话属性图片 = []

        for j in range(len(装备列表)):
            if 装备列表[j].品质 == '神话':
                self.神话属性图片.append(QLabel(self.main_frame4))
                self.神话属性图片[-1].setMovie(self.装备图片[j])
                self.神话属性图片[-1].setToolTip('<font size="3" face="宋体">' + 装备列表[j].名称 + '<br>'+ 装备列表[j].类型 + '-' + 装备列表[j].部位 + '</font>')
                self.神话属性图片[-1].resize(28, 28)
                self.神话属性图片[-1].move(-1000, -1000)
                self.装备图片[j].start()

        for i in range(4 * 35):
            self.神话属性选项.append(MyQComboBox(self.main_frame4))
            self.神话属性选项[i].resize(140, 18)
            self.神话属性选项[i].move(-1000, -1000)
            self.神话属性选项[i].currentIndexChanged.connect(lambda state, index = i:self.神话属性选项颜色更新(index))
        
        count = 0
        for i in 装备列表:
            if i.品质 == '神话':
                描述列表 = [i.属性1描述, i.属性2描述, i.属性3描述, i.属性4描述]
                范围列表 = [i.属性1范围, i.属性2范围, i.属性3范围, i.属性4范围]
                for j in range(4):
                    if 描述列表[j] != '无':
                        for k in range(范围列表[j][0], 范围列表[j][1] - 1, -1):
                            if (k % 范围列表[j][2]) == 0 or k == 范围列表[j][0]:
                                temp = 描述列表[j] + str(k)
                                if 范围列表[j][2] == 1:
                                    temp += '%'
                                self.神话属性选项[count * 4 + j].addItem(temp)
                    else:
                        self.神话属性选项[count * 4 + j].addItem('无')
                count += 1

    def 界面5(self):
        #第五个布局
        标签 = QLabel('单件选择', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(240, 25)
        标签.move(70, 20)

        self.图片显示 = []
        self.图片列表 = []

        count = 0
        self.自选装备 = []
        if 切装模式 == 1:
            self.装备切装 = []
            self.切装修正属性 = []
        for i in 部位列表:
            标签 = QLabel(i, self.main_frame5)
            标签.setAlignment(Qt.AlignCenter)
            标签.setStyleSheet(标签样式)
            标签.resize(60, 25)
            标签.move(10, 50 + 30 * count)
            self.自选装备.append(MyQComboBox(self.main_frame5))
            self.自选装备[count].resize(240, 22)
            self.自选装备[count].move(70, 50 + 30 * count)
            self.自选装备[count].currentIndexChanged.connect(lambda state, index = count:self.自选装备更改(index))
            if 切装模式 == 1:
                self.装备切装.append(QCheckBox(self.main_frame5))
                self.装备切装[count].move(320, 45 + 30 * count)
            for j in 装备列表:
                if j.部位 == i:
                    if i == '武器':
                        if j.类型 in self.角色属性A.武器选项:
                            self.自选装备[count].addItem(j.名称)
                    else:
                        self.自选装备[count].addItem(j.名称)
            count += 1
        
        if 切装模式 == 1:
            num = 0
            for i in ['力量', '智力', '物攻', '魔攻', '独立', '属强']:
                标签 = QLabel(i, self.main_frame5)
                标签.setAlignment(Qt.AlignCenter)
                标签.setStyleSheet(标签样式)
                标签.resize(45, 25)
                标签.move(30 + 50 * num, 60 + 30 * count)
                self.切装修正属性.append(QLineEdit(self.main_frame5))
                self.切装修正属性[num].setAlignment(Qt.AlignCenter)
                self.切装修正属性[num].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                self.切装修正属性[num].resize(45, 22)
                self.切装修正属性[num].move(30 + 50 * num, 85 + 30 * count)
                num += 1

        self.计算标识 = 1
        
        横坐标 = 355
        标签 = QLabel('批量选择', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(160, 25)
        标签.move(横坐标, 20)

        套装类型 = ['防具', '首饰', '特殊', '上链左', '镯下右', '环鞋指']
        count = 0
        self.自选套装 = []
        for i in 套装类型:
            self.自选套装.append(MyQComboBox(self.main_frame5))
            套装名称 = []
            for j in 套装列表:
                if j.名称 not in 套装名称 and j.类型 == i:
                    套装名称.append(j.名称)
            self.自选套装[count].addItems(套装名称)
            self.自选套装[count].resize(160, 22)
            self.自选套装[count].move(横坐标, 50 + 30 * count)
            self.自选套装[count].activated.connect(lambda state, index = count:self.自选套装更改(index))
            count += 1
      
        self.神话部位选项 = MyQComboBox(self.main_frame5)
        self.神话部位选项.addItems(['神话部位：无', '神话部位：上衣', '神话部位：手镯', '神话部位：耳环'])
        self.神话部位选项.resize(160, 22)
        self.神话部位选项.move(横坐标, 50 + 30 * count)
        self.神话部位选项.activated.connect(lambda state:self.神话部位更改())
        
        count += 1
        self.改造套装 = MyQComboBox(self.main_frame5)
        for n in 装备列表:
            try:
                self.改造套装.addItem(n.关联套装)
            except:
                pass
        self.改造套装.resize(160, 22)
        self.改造套装.move(横坐标, 50 + 30 * count)
        self.改造套装.activated.connect(lambda state:self.改造套装更改())

        count += 1   
        self.转甲选项 = QCheckBox('85SS转甲',self.main_frame5)
        self.转甲选项.resize(80, 22)
        self.转甲选项.move(横坐标 + 40, 50 + 30 * count)
        self.转甲选项.setChecked(True)
        self.转甲选项.setStyleSheet(复选框样式)
        self.转甲选项.stateChanged.connect(lambda state: self.自选计算(1))

        count += 1
        #一键修正按钮添加
        一键站街修正名称 = ['站街力智', '站街三攻', '站街属强']
        for i in range(0, len(一键站街修正名称)):
            名称 = QLabel(一键站街修正名称[i], self.main_frame5)
            名称.setAlignment(Qt.AlignCenter)
            名称.move(横坐标 - 5 + i*57, 50 + 30 * count)
            名称.resize(52, 25)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            self.一键站街设置输入.append(QLineEdit(self.main_frame5))
            self.一键站街设置输入[i + 3].setAlignment(Qt.AlignCenter)
            self.一键站街设置输入[i + 3].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            self.一键站街设置输入[i + 3].resize(52, 22)
            self.一键站街设置输入[i + 3].move(横坐标 - 5 + i*57, 80 + 30 * count)
        
        count += 2
        一键修正按钮 = QPushButton('一键修正面板细节', self.main_frame5)
        一键修正按钮.clicked.connect(lambda state: self.一键修正(1))
        一键修正按钮.move(横坐标 - 5 , 50 + 30 * count)
        一键修正按钮.resize(165, 25)
        一键修正按钮.setStyleSheet(按钮样式)

        标签 = QLabel('辟邪玉提升率(理论值仅供参考)', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(200, 25)
        标签.move(525, 20)

        self.辟邪玉提升率1 = []
        self.辟邪玉提升率2 = []
        count = 0
        for i in 辟邪玉列表:
            if i.名称 != '无':
                if i.最大值 != 1:
                    temp = i.名称 + '+' + str(i.最大值) + '%'
                else:
                    temp = i.名称 + '+' + str(i.最大值)
                self.辟邪玉提升率1.append(QLabel(temp, self.main_frame5))
                self.辟邪玉提升率1[count].setAlignment(Qt.AlignCenter)
                self.辟邪玉提升率1[count].setStyleSheet(标签样式)
                self.辟邪玉提升率1[count].resize(180, 25)
                self.辟邪玉提升率1[count].move(520, 50 + 30 * count)
                self.辟邪玉提升率2.append(QLabel('0.00%', self.main_frame5))
                self.辟邪玉提升率2[count].setAlignment(Qt.AlignCenter)
                self.辟邪玉提升率2[count].setStyleSheet(标签样式)
                self.辟邪玉提升率2[count].resize(30, 25)
                self.辟邪玉提升率2[count].move(710, 50 + 30 * count)
                count += 1

        初始x = 805
        初始y = 20
        图片显示 = QLabel(self.main_frame5)
        图片显示.setPixmap(self.输出背景图片)
        图片显示.setAlignment(Qt.AlignTop)
        图片显示.resize(268, 564)
        图片显示.move(初始x, 初始y)
        人物 = QLabel(self.main_frame5)
        图片 = QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(初始x + 90 + int(45 - 图片.width() / 2), 初始y + 40)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)

        偏移量=187
        x坐标=[32,0,0,32,0,偏移量,偏移量+32,偏移量+32,偏移量,偏移量,偏移量+32,32]
        y坐标=[0,0,32,32,64,0,0,32,64,32,64,64]
        
        for i in range(12):
            self.图片列表.append(self.装备图片[装备序号[self.自选装备[i].currentText()]])
            self.图片显示.append(QLabel(self.main_frame5))
            self.图片显示[i].setMovie(self.图片列表[i])
            self.图片列表[i].start()
            self.图片显示[i].resize(26,26)
            self.图片显示[i].move(初始x + 10 + x坐标[i], 初始y + 31 + y坐标[i])
            self.图片显示[i].setAlignment(Qt.AlignCenter) 


        self.面板显示=[]
        for i in range(0,17):
            self.面板显示.append(QLabel(self.main_frame5)) 

        const = 139 + 初始y
        count = 0
        for i in  [9,10,0,1]:
            self.面板显示[i].move(20 + 初始x,const + count * 18)
            count += 1
        count = 0
        for i in  [11,12,2,3]:
            self.面板显示[i].move(150 + 初始x,const + count * 18)
            count += 1
        self.面板显示[4].move(150 + 初始x,const + count * 18)
        count = 5
        for i in  [5,6,7,8]:
            self.面板显示[i].move(150 + 初始x,const + count * 18)
            count += 1
        count = 5
        for i in  [13,14,15,16]:
            self.面板显示[i].move(20 + 初始x,const + count * 18)
            count += 1
        for i in range(0,len(self.面板显示)):
            if i >= 9:
                self.面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            else:
                self.面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(150,255,30)}")
            self.面板显示[i].resize(100,18)
            self.面板显示[i].setAlignment(Qt.AlignRight)  

        self.词条显示=[]
        for i in range(0,12):
            self.词条显示.append(QLabel(self.main_frame5))     

        j = 312 + 初始y
        for i in self.词条显示:
            i.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            i.move(20 + 初始x, j)
            i.resize(180,17)
            i.setAlignment(Qt.AlignLeft)
            j+=17

        self.总伤害=QLabel(self.main_frame5)
        self.总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        self.总伤害.resize(250,36)
        self.总伤害.move(10 + 初始x, 520 + 初始y)
        self.总伤害.setAlignment(Qt.AlignCenter) 

        self.套装名称显示=[]
        for i in range(0,10):
            self.套装名称显示.append(QLabel(self.main_frame5))
            self.套装名称显示[i].move(114 + 初始x, 133 + 180 + 20 * i + 初始y)
            self.套装名称显示[i].resize(150,18)
            self.套装名称显示[i].setAlignment(Qt.AlignCenter)   

        自选计算按钮 = QPushButton('查看详情', self.main_frame5)
        自选计算按钮.clicked.connect(lambda state: self.自选计算())
        自选计算按钮.move(995, 610)
        自选计算按钮.resize(80, 28)
        自选计算按钮.setStyleSheet(按钮样式)
        
        self.基准值 = []

        设置基准值 = QPushButton('设为基准', self.main_frame5)
        设置基准值.clicked.connect(lambda state: self.基准值设置())
        设置基准值.move(900, 610)
        设置基准值.resize(80, 28)
        设置基准值.setStyleSheet(按钮样式)

        清空基准值 = QPushButton('清空基准', self.main_frame5)
        清空基准值.clicked.connect(lambda state: self.基准值设置(1))
        清空基准值.move(805, 610)
        清空基准值.resize(80, 28)
        清空基准值.setStyleSheet(按钮样式)

        self.对比格式 = QCheckBox('数值对比', self.main_frame5)
        self.对比格式.stateChanged.connect(lambda state: self.自选计算(1))
        self.对比格式.move(720, 612)
        self.对比格式.resize(70, 24)
        self.对比格式.setStyleSheet(复选框样式)
    
    def 护石描述更新(self, x):
        try:
            self.护石栏[x].setToolTip('<font face="宋体">' + self.初始属性.技能栏[self.初始属性.技能序号[self.护石栏[x].currentText()]].护石描述(self.护石类型选项[x].currentIndex()) + '</font></font>')
        except:
            self.护石栏[x].setToolTip('<font face="宋体">暂缺</font>')
                    
    def 护石类型选项更新(self, x):
        self.护石类型选项[x].clear()
        if self.护石栏[x].currentText() != '无':
            try:
                self.护石类型选项[x].addItems(self.初始属性.技能栏[self.初始属性.技能序号[self.护石栏[x].currentText()]].护石选项)
            except:
                self.护石类型选项[x].addItem('魔界')
                self.护石栏[x].setCurrentIndex(0)
        else:
            self.护石类型选项[x].addItem('魔界')

    def 符文技能更改(self, i):
        if i == 0:
            for i in range(1, 9):
                self.符文[i].setCurrentIndex(self.符文[0].currentIndex())
        else:
            self.符文[i + 3].setCurrentIndex(self.符文[i].currentIndex())
            self.符文[i + 6].setCurrentIndex(self.符文[i].currentIndex())

    def 符文效果更改(self, i):
        self.符文效果[i + 3].setCurrentIndex(self.符文效果[i].currentIndex())
        self.符文效果[i + 6].setCurrentIndex(self.符文效果[i].currentIndex())

    def 基准值设置(self, x = 0):
        self.基准值.clear()
        if x == 0:
            装备 = []
            for i in self.自选装备:
                装备.append(i.currentText())
            
            套装 = []
            套装字典 = {}
            for i in 装备:
                j = 装备列表[装备序号[i]].所属套装
                if j == '智慧产物':
                    try:
                        k = 装备列表[装备序号[i]].所属套装2
                        套装字典[k] = 套装字典.get(k, 0) + 1
                    except:
                        pass
                elif j != '无':
                    套装字典[j] = 套装字典.get(j, 0) + 1
    
            for i in 套装字典.keys():
                if 套装字典[i] >= 2 and (i + '[2]') in 套装序号.keys():
                    套装.append(i + '[2]')
                if 套装字典[i] >= 3 and (i + '[3]') in 套装序号.keys():
                    套装.append(i + '[3]')
                if 套装字典[i] >= 5 and (i + '[5]') in 套装序号.keys():
                    套装.append(i + '[5]')

            A = deepcopy(self.初始属性)
            self.输入属性(A)
            A.穿戴装备(装备,套装)
            B = deepcopy(A)
            self.排行窗口列表.clear()
            self.排行数据.clear()
            self.排行数据.append(装备 + [0] + 套装 + ['无'])
            self.输出界面(0, '基准值')
            self.基准值 = [A.伤害计算(0), B.伤害计算(1)]
            
        self.自选计算(1)
        
    def 希洛克选择(self, index, x = 0):
        if x == 1:
            for i in range(15):
                self.希洛克遮罩透明度[i].setOpacity(0.5)
                self.希洛克选择状态[i] = 0
            return
        if index >= 100:
            序号 = int(index / 100 - 1)
            count = 0
            for i in range(序号 * 3, 序号 * 3 + 3):
                count += self.希洛克选择状态[i]
            if count != 3:
                for i in range(15):
                    if i in range(序号 * 3, 序号 * 3 + 3):
                        self.希洛克遮罩透明度[i].setOpacity(0)
                        self.希洛克选择状态[i] = 1
                    else:
                        self.希洛克遮罩透明度[i].setOpacity(0.5)
                        self.希洛克选择状态[i] = 0
            else:
                for i in range(序号 * 3, 序号 * 3 + 3):
                    self.希洛克遮罩透明度[i].setOpacity(0.5)
                    self.希洛克选择状态[i] = 0
        else:
            if self.希洛克选择状态[index] == 0:
                for i in range(5):
                    序号 = i * 3 + index % 3
                    if self.希洛克选择状态[序号] == 1:
                        self.希洛克遮罩透明度[序号].setOpacity(0.5)
                        self.希洛克选择状态[序号] = 0
                self.希洛克遮罩透明度[index].setOpacity(0)
                self.希洛克选择状态[index] = 1
            else:
                self.希洛克遮罩透明度[index].setOpacity(0.5)
                self.希洛克选择状态[index] = 0

    def 特色选项提醒(self):
        if self.特色选项.isChecked():
             QMessageBox.information(self,"警告",  "等级禁用将会影响<font color='#FF0000'>远古记忆、红阵</font>等级导致差值偏大。<br>如有需要请勾选奶和系统奶或将远古记忆、红阵设置为0再做对比。")
        else:
            return

    def 全局重置(self):
        box = QMessageBox(QMessageBox.Warning, "提示", "是否恢复默认设置？")
        box.setWindowIcon(self.icon)
        yes = box.addButton(self.tr("确定"), QMessageBox.YesRole)
        no = box.addButton(self.tr("取消"), QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton() == yes:
            self.载入配置('reset')

    def 改造套装更改(self):
        self.计算标识 = 0
        名称列表 = []
        部位序号 = []
        for n in 装备列表:
            try:
                if n.关联套装 == self.改造套装.currentText():
                    名称列表.append(n.名称)
                    部位序号.append(部位字典[n.部位])
            except:
                pass
            try:
                if n.所属套装 == self.改造套装.currentText().split('[')[0]:
                    名称列表.append(n.名称)
                    部位序号.append(部位字典[n.部位])
            except:
                pass
        if self.改造套装.currentText() == '兵法之神[5]':
            for n in 装备列表:
                try:
                    if n.所属套装 in ['无相轮回的希望', '流逝轮回的记忆'] and n.部位 != '辅助装备':
                        名称列表.append(n.名称)
                        部位序号.append(部位字典[n.部位])
                except:
                    pass                 
        for n in 部位序号:
            x = -1
            for i in 装备列表:
                if 部位列表[n] == i.部位:
                    x += 1 
                    if i.名称 in 名称列表:
                        self.自选装备[n].setCurrentIndex(x)
        self.计算标识 = 1
        self.自选计算(1)

    def 神话部位更改(self):
        self.计算标识 = 0
        部位 = [-1, 0, 5, 8]
        序号 = 部位[self.神话部位选项.currentIndex()]
        if 序号 != -1:
            当前 = 装备列表[装备序号[self.自选装备[序号].currentText()]]
            x = -1
            for i in 装备列表:
                if 当前.部位 == i.部位:
                    x += 1 
                    if i.品质 == '神话' and i.所属套装 == 当前.所属套装:
                        self.自选装备[序号].setCurrentIndex(x)
        for k in [0, 5, 8]:
            if k != 序号:
                当前 = 装备列表[装备序号[self.自选装备[k].currentText()]]
                if 当前.品质 == '神话':
                    x = -1
                    for i in 装备列表:
                        if 当前.部位 == i.部位:
                            x += 1 
                            if i.品质 == '史诗' and i.所属套装 == 当前.所属套装:
                                self.自选装备[k].setCurrentIndex(x)
        self.计算标识 = 1
        self.自选计算(1)         
        
    def 自选装备更改(self, index = 0):
        try:
            self.图片列表[index] = self.装备图片[装备序号[self.自选装备[index].currentText()]]
            self.图片显示[index].setMovie(self.图片列表[index])
            self.图片列表[index].start()
        except:
            pass
        
        if self.当前页面 == 4 and self.计算标识 == 1:
            self.自选计算(1)

    def 自选套装更改(self, index):
        self.计算标识 = 0
        name = self.自选套装[index].currentText()
        for i in range(11):
            x = -1
            for j in 装备列表:
                if j.部位 == 部位列表[i]:
                    x += 1
                    try:
                        if j.所属套装2 == name:
                            self.自选装备[i].setCurrentIndex(x)
                            break
                    except:
                        if j.所属套装 == name and j.品质 != '神话':
                            self.自选装备[i].setCurrentIndex(x)
                            break
        self.计算标识 = 1
        self.自选计算(1)  
                    
    def 等级调整标注(self, index):
        低等级 = "QComboBox{font-size:12px;color:white;background-color:rgba(34,157,70,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(5,185,65,0.8)} QComboBox QAbstractItemView::item {height: 18px;}"
        未调整 = "QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(65,105,225,0.8)} QComboBox QAbstractItemView::item {height: 18px;}"
        高等级 = "QComboBox{font-size:12px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(225,5,65,0.8)} QComboBox QAbstractItemView::item {height: 18px;}"
        警告 = "技能等级调整指调整<font color='#FF0000'>学习等级</font>(非实际等级)<br>一般用于修正天空下装技能，一二觉时装切装<br>其余等级加成会自动计算，请勿手动调整"
        if index < 100:
            try:
                x = int(self.等级调整[index].currentText())
            except:
                x = 1
            if x > 0:
                self.等级调整[index].setStyleSheet(高等级)
            if x > 1:
                QMessageBox.information(self,"警告",  警告) 
            if x < 0:
                self.等级调整[index].setStyleSheet(低等级)
            if x == 0:
                self.等级调整[index].setStyleSheet(未调整)
        elif index == 100:
            try:
                x = int(self.远古记忆.currentText())
            except:
                x = 11
            if x == 11:
                self.远古记忆.setStyleSheet(高等级)
            if x < 10:
                self.远古记忆.setStyleSheet(低等级)
            if x == 10:
                self.远古记忆.setStyleSheet(未调整)
        elif index == 200:
            try:
                x = int(self.刀魂之卡赞.currentText())
            except:
                x = 11
            if x == 11:
                self.刀魂之卡赞.setStyleSheet(高等级)
            if x < 10:
                self.刀魂之卡赞.setStyleSheet(低等级)
            if x == 10:
                self.刀魂之卡赞.setStyleSheet(未调整)      
            
    def 时装选项更新(self, index):
        if index == 8:
            count = 0
            for i in self.时装选项:
                if count != 8:
                    i.setCurrentIndex(self.时装选项[8].currentIndex())
                count += 1
            return
        else:
            力量, 智力, 属强 = 0, 0, 0
            套装字典 = {'高级':0, '节日':0, '稀有':0, '神器':0}
            for i in range(8):
                套装字典[self.时装选项[i].currentText()] = 套装字典.get(self.时装选项[i].currentText(), 0) + 1
            #套装属性
            神器 = 套装字典['神器']
            稀有 = 套装字典['稀有'] + 神器
            if 套装字典['高级'] >= 3:
                力量 += 10; 智力 += 10
            if 稀有 >= 3 and 神器 < 3:
                力量 += 40; 智力 += 40
            if 套装字典['神器'] >= 3:
                力量 += 50; 智力 += 50
            if 套装字典['高级'] >= 8:
                力量 += 10; 智力 += 10
            if 套装字典['节日'] >= 8:
                力量 += 25; 智力 += 25
            if 稀有 >= 8 and 神器 < 8:
                力量 += 40; 智力 += 40; 属强 += 6
            if 套装字典['神器'] >= 8:
                力量 += 50; 智力 += 50; 属强 += 10
            数据 = [45, 45, 55, 65]
            智力 += 数据[self.时装选项[0].currentIndex()] #头部
            智力 += 数据[self.时装选项[1].currentIndex()] #帽子
            力量 += 数据[self.时装选项[7].currentIndex()] #鞋子
            数据 = [0, 0, 55, 65]
            力量 += 数据[self.时装选项[5].currentIndex()] #腰带
            数据 = [0, 6, 0, 0]
            属强 += 数据[self.时装选项[4].currentIndex()] #上衣

            数据 = [0, 20, 0, 0]
            智力 += 数据[self.时装选项[6].currentIndex()] #下装
            力量 += 数据[self.时装选项[6].currentIndex()] #下装

            self.属性设置输入[7][16].setText(str(力量))
            self.属性设置输入[8][16].setText(str(智力))
            self.属性设置输入[12][16].setText(str(属强))
 
    def 辟邪玉数值选项更新(self, index):
        self.辟邪玉数值[index].clear()
        x = self.辟邪玉选择[index].currentIndex()
        temp = 辟邪玉列表[x].最大值 * 10
        while temp >= 辟邪玉列表[x].最小值 * 10:
            if 辟邪玉列表[x].间隔 == 1:
                self.辟邪玉数值[index].addItem(str(int(temp/10)))
            else:
                self.辟邪玉数值[index].addItem(str('%.1f' % (temp/10)) + '%')
            temp -= 辟邪玉列表[x].间隔 * 10

    def 辟邪玉属性计算(self, 属性):
        for i in range(4):
            x = self.辟邪玉选择[i].currentIndex()
            if self.辟邪玉数值[i].currentIndex() >= 0:
                辟邪玉列表[x].当前值 = float(self.辟邪玉数值[i].currentText().replace('%',''))
            辟邪玉列表[x].穿戴属性(属性)

    def 装备图标点击事件(self, index, sign, x = 1):
        if 装备列表[index].模式 == 0:
            #改变状态
            if sign == 10:
                if self.装备选择状态[index] == 0:
                    self.遮罩透明度[index].setOpacity(0.0)
                    self.装备选择状态[index] = 1
                else:
                    self.遮罩透明度[index].setOpacity(0.5)
                    self.装备选择状态[index] = 0
            #点亮
            if sign == 1:
                self.遮罩透明度[index].setOpacity(0.0)
                self.装备选择状态[index] = 1
            #熄灭
            if sign == 0:
                self.遮罩透明度[index].setOpacity(0.5)
                self.装备选择状态[index] = 0
            self.装备图片按钮[index].setGraphicsEffect(self.遮罩透明度[index])

            if x == 1:
                self.计算模式选择.setItemText(0, '计算模式：极速模式  组合：' + self.组合数量计算(0))
                self.计算模式选择.setItemText(1, '计算模式：套装模式  组合：' + self.组合数量计算(1))
                self.计算模式选择.setItemText(2, '计算模式：单件模式  组合：' + self.组合数量计算(2))

    def 套装按钮点击事件(self, index):
        count1 = 0
        count2 = 0
        for i in 装备列表:
            if i.所属套装 == index and index != '无' and i.部位 != '武器':
                count1 += self.装备选择状态[装备序号[i.名称]] 
            if i.类型 in self.角色属性A.武器选项 and index == '无':
                count2 += self.装备选择状态[装备序号[i.名称]]
        for i in 装备列表:
            if i.所属套装 == index and index != '无' and i.部位 != '武器':
                self.装备图标点击事件(装备序号[i.名称], 0 if count1 > 0 else 1)
            if i.类型 in self.角色属性A.武器选项 and index == '无':
                self.装备图标点击事件(装备序号[i.名称], 0 if count2 > 0 else 1)

    def 组合数量计算(self, sign, x = 0):
        if sign == 0 or sign == 1:
            self.有效武器列表.clear()
            for j in range(0, 6):
                self.有效总套装列表[j].clear()
            for i in range(0, len(self.装备选择状态)):
                if self.装备选择状态[i] == 1:
                    for j in range(0, 6):
                        if (装备列表[i].所属套装 in 总套装列表[j]) and (装备列表[i].所属套装 not in self.有效总套装列表[j]):
                            self.有效总套装列表[j].append(装备列表[i].所属套装)
                    if 装备列表[i].部位 == '武器':
                        self.有效武器列表.append(装备列表[i].名称)
            if sign == 0:
                counter = (len(self.有效防具套装)*len(self.有效首饰套装)*len(self.有效特殊套装)+len(self.有效防具套装)*len(self.有效上链左套装)*len(self.有效镯下右套装)*len(self.有效环鞋指套装)*4)*4*len(self.有效武器列表)
            if sign == 1:
                counter = (len(self.有效防具套装)*len(self.有效首饰套装)*len(self.有效特殊套装)+len(self.有效防具套装)*len(self.有效上链左套装)*len(self.有效镯下右套装)*len(self.有效环鞋指套装)*4+len(self.有效防具套装)*len(self.有效首饰套装)*len(self.有效特殊套装)*(len(self.有效防具套装)-1)*10)*4*len(self.有效武器列表)
    
        if sign == 2:
            self.有效部位列表.clear()
            for i in range(0, 12):
                self.有效部位列表.append([])
            for i in range(0, len(self.装备选择状态)):
                if self.装备选择状态[i] == 1:
                    self.有效部位列表[部位列表.index(装备列表[i].部位)].append(装备列表[i].名称)
        
            counter = 0
            for a1 in self.有效部位列表[0]:
                for a2 in self.有效部位列表[5]:
                    for a3 in self.有效部位列表[8]:
                        神话数量 = 0
                        for i in [a1, a2, a3]:
                            if 装备列表[装备序号[i]].品质 == '神话':
                                神话数量 += 1
                        if 神话数量 <= 1:
                            counter += 1
            for i in [1, 3, 2, 4, 6, 9, 7, 10, 11]:
                counter *= len(self.有效部位列表[i])

        if x == 0:
            if counter <= 9999 :
                return str(counter)
            else:
                num = -1
                while counter >= 10000:
                    counter /= 10000
                    num += 1
                name = ['万', '亿', '万亿']
                return str(round(counter, 2)) + name[num]
        if x == 1:
            return counter

    def 强化觉醒选择(self, index):
        self.觉醒选择状态=index
        if index==1:  
            self.一觉遮罩透明度.setOpacity(0.0)
            self.二觉遮罩透明度.setOpacity(0.5)
        if index==2:
            self.一觉遮罩透明度.setOpacity(0.5)
            self.二觉遮罩透明度.setOpacity(0.0)       
    
        self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
        self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)

    def 批量选择(self, index):
        if index == 1:
            if self.全选状态 == 1:
                self.全选状态 = 0
            else:
                self.全选状态 = 1
            if sum(self.装备选择状态[74:244]) == 170:
                self.批量选择(0)

        for i in 装备列表:
            if i.部位 != '武器':
                if i.品质 != '神话' or index == 0 or self.全选状态 == 0:
                    self.装备图标点击事件(装备序号[i.名称], index, x = 0)
            else:
                if i.类型 in self.角色属性A.武器选项:
                    self.装备图标点击事件(装备序号[i.名称], index, x = 0)

        self.装备图标点击事件(74, index)
    
    def 批量打造(self, x):
        for i in range(12):
            y = max(min(self.装备打造选项[i + 12].currentIndex() + x, 31), 0)
            self.装备打造选项[i + 12].setCurrentIndex(y)

    def 载入配置(self, path = 'set'):
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ3.ini', 'r', encoding='utf-8').readlines()
            self.称号.setCurrentIndex(int(setfile[0].replace('\n', '')))
            self.宠物.setCurrentIndex(int(setfile[1].replace('\n', '')))
            self.计算模式选择.setCurrentIndex(int(setfile[2].replace('\n', '')))
            # 百变怪 && 神话排名 && 显示选项 && 时装选项
            if int(setfile[3].replace('\n', '')):
                self.百变怪选项.setChecked(True)
            if int(setfile[4].replace('\n', '')):
                self.神话排名选项.setChecked(True)
            if int(setfile[5].replace('\n', '')):
                self.显示选项.setChecked(True)
            for i in range(0,len(self.时装选项)):
                self.时装选项[i].setCurrentIndex(int(setfile[i + 6].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/attr.ini', 'r', encoding='utf-8').readlines()
            for i in range(0, 17):
                for j in range(0, len(self.属性设置输入[i])):
                    self.属性设置输入[i][j].setText(setfile[i].replace('\n', '').split(',')[j])
        
            for j in range(0, 17):
                self.技能设置输入[j].setCurrentIndex(int(setfile[17].replace('\n', '').split(',')[j]))
        except:
            pass

        try:
            self.批量选择(0)#先清空
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ.ini', 'r', encoding='utf-8').readlines()
            for i in range(0, len(装备列表)):
                if setfile[i].replace('\n', '') == '1':
                    self.装备图标点击事件(i, 1)
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ1.ini', 'r', encoding='utf-8').readlines()
            for i in range(0,len(self.装备打造选项)):
                self.装备打造选项[i].setCurrentIndex(int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ2.ini', 'r', encoding='utf-8').readlines()
            for i in range(0,len(self.装备条件选择)):
                self.装备条件选择[i].setCurrentIndex(int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill1.ini', 'r', encoding='utf-8').readlines()
            num = 0
            self.BUFF输入.setText(setfile[num].replace('\n', '')); num += 1
            self.时间输入.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石栏[0].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石栏[1].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            for i in range(0,6):
                self.符文[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.符文效果[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.强化觉醒选择(int(setfile[num].replace('\n', ''))); num += 1
            if self.初始属性.远古记忆 != -1:
                self.远古记忆.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            if self.初始属性.刀魂之卡赞 != -1:
                self.刀魂之卡赞.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石栏[2].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            for i in range(6,9):
                self.符文[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.符文效果[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            for i in range(3):
                self.护石类型选项[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill2.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in self.角色属性A.技能栏:
                序号 = self.角色属性A.技能序号[i.名称]
                self.等级调整[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                if i.是否有伤害 == 1 and i.TP上限 != 0:
                    self.TP输入[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                if i.是否有伤害 == 1:
                    self.次数输入[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                    self.宠物次数[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill3.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(4):
                self.辟邪玉选择[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.辟邪玉数值[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.希洛克选择(0, 1)
            for i in range(15):
                if setfile[num].replace('\n', '') == '1':
                    self.希洛克选择(i)
                num += 1
            self.守门将属强.setCurrentIndex(int(setfile[num].replace('\n', '')));num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill0.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(len(self.复选框列表)):
                if int(setfile[num].replace('\n', '')) == 1:
                    self.复选框列表[i].setChecked(True)
                else:
                    self.复选框列表[i].setChecked(False)
                num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ4.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(4 * 35):
                self.神话属性选项[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ5.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(12):
                self.自选装备[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass
        
        if 切装模式 == 1:
            try:
                setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ6.ini', 'r', encoding='utf-8').readlines()
                num = 0
                for i in range(12):
                    if setfile[num].replace('\n', '') == '1': self.装备切装[i].setChecked(True)
                    num += 1
                for i in self.角色属性A.技能栏:
                    序号 = self.角色属性A.技能序号[i.名称]
                    if i.是否有伤害 == 1:
                        if setfile[num].replace('\n', '') == '1': self.技能切装[序号].setChecked(True)
                        num += 1
            except:
                pass

    def 保存配置(self, path = 'set'):
        if self.禁用存档.isChecked():
            return
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ3.ini', 'w', encoding='utf-8')
            setfile.write(str(self.称号.currentIndex())+'\n')
            setfile.write(str(self.宠物.currentIndex())+'\n')
            setfile.write(str(self.计算模式选择.currentIndex())+'\n')
            # 百变怪 && 神话排名 && 显示选项 && 时装选择
            setfile.write(str(int(self.百变怪选项.isChecked())) + '\n')
            setfile.write(str(int(self.神话排名选项.isChecked())) + '\n')
            setfile.write(str(int(self.显示选项.isChecked())) + '\n')
            for i in range(0, len(self.时装选项)):
                setfile.write(str(self.时装选项[i].currentIndex()) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/attr.ini', 'w', encoding='utf-8')
            for i in range(0, 17):
                for j in range(0, len(self.属性设置输入[i])):
                    setfile.write(self.属性设置输入[i][j].text()+',')
                setfile.write('\n')
        
            for j in range(0, 17):
                setfile.write(str(self.技能设置输入[j].currentIndex())+',')
            setfile.write('\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ.ini', 'w', encoding='utf-8')
            for i in range(0, len(装备列表)):
                setfile.write(str(self.装备选择状态[i])+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ1.ini', 'w', encoding='utf-8')
            for i in range(0,len(self.装备打造选项)):
                setfile.write(str(self.装备打造选项[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ2.ini', 'w', encoding='utf-8')
            for i in range(0,len(self.装备条件选择)):
                setfile.write(str(self.装备条件选择[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill1.ini', 'w', encoding='utf-8')
            setfile.write(self.BUFF输入.text()+'\n')
            setfile.write(str(self.时间输入.currentIndex())+'\n')
            setfile.write(str(self.护石栏[0].currentIndex())+'\n')
            setfile.write(str(self.护石栏[1].currentIndex())+'\n')
            for i in range(0,6):
                setfile.write(str(self.符文[i].currentIndex())+'\n')
                setfile.write(str(self.符文效果[i].currentIndex())+'\n')
            setfile.write(str(self.觉醒选择状态)+'\n')
            if self.初始属性.远古记忆 != -1:
                setfile.write(str(self.远古记忆.currentIndex())+'\n')
            if self.初始属性.刀魂之卡赞 != -1:
                setfile.write(str(self.刀魂之卡赞.currentIndex())+'\n')
            setfile.write(str(self.护石栏[2].currentIndex())+'\n')
            for i in range(6,9):
                setfile.write(str(self.符文[i].currentIndex())+'\n')
                setfile.write(str(self.符文效果[i].currentIndex())+'\n')
            for i in range(3):
                setfile.write(str(self.护石类型选项[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill2.ini', 'w', encoding='utf-8')
            for i in self.角色属性A.技能栏:
                序号 = self.角色属性A.技能序号[i.名称]
                setfile.write(str(self.等级调整[序号].currentIndex())+'\n')
                if i.是否有伤害 == 1 and i.TP上限 != 0:
                    setfile.write(str(self.TP输入[序号].currentIndex())+'\n')
                if i.是否有伤害 == 1:
                    setfile.write(str(self.次数输入[序号].currentIndex())+'\n')
                    setfile.write(str(self.宠物次数[序号].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill3.ini', 'w', encoding='utf-8')
            for i in range(4):
                setfile.write(str(self.辟邪玉选择[i].currentIndex())+'\n')
                setfile.write(str(self.辟邪玉数值[i].currentIndex())+'\n')
            for i in range(15):
                setfile.write(str(self.希洛克选择状态[i])+'\n')
            setfile.write(str(self.守门将属强.currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill0.ini', 'w', encoding='utf-8')
            for i in range(len(self.复选框列表)):
                if self.复选框列表[i].isChecked():
                    setfile.write('1\n')
                else:
                    setfile.write('0\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ4.ini', 'w', encoding='utf-8')
            for i in range(4 * 35):
                setfile.write(str(self.神话属性选项[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ5.ini', 'w', encoding='utf-8')
            for i in range(12):
                setfile.write(str(self.自选装备[i].currentIndex())+'\n')
        except:
            pass
        
        if 切装模式 == 1:
            try:
                setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ6.ini', 'w', encoding='utf-8')
                for i in self.装备切装:
                    if i.isChecked():
                        setfile.write('1\n')
                    else:
                        setfile.write('0\n')
    
                for i in self.角色属性A.技能栏:
                    序号 = self.角色属性A.技能序号[i.名称]
                    if i.是否有伤害 == 1:
                        if self.技能切装[序号].isChecked():
                            setfile.write('1\n')
                        else:
                            setfile.write('0\n')
            except:
                pass
    
    def 神话属性选项颜色更新(self, index):
        i = self.神话属性选项[index]
        if i.currentIndex() != 0:
            i.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(225,5,65,0.8)} QComboBox QAbstractItemView::item {height: 18px;}")
        else:
            i.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(65,105,225,0.8)} QComboBox QAbstractItemView::item {height: 18px;}")

    def click_window(self, index):
        self.当前页面 = index
        if self.stacked_layout.currentIndex() != index:
            self.stacked_layout.setCurrentIndex(index)
        for i in self.window_btn:
            i.setStyleSheet('QToolButton{font-size:13px;color:white;background-color:rgba(70,130,200,0.8)} QToolButton:hover{background-color:rgba(40,100,235,0.8)}')
        self.window_btn[index].setStyleSheet('QToolButton{font-size:13px;color:white;background-color:rgba(200,30,30,0.8)} QToolButton:hover{background-color:rgba(235,0,0,0.8)}')

        if index == 3:
            count1 = 0
            count2 = 0
            num = 0
            自选装备名称 = []
            for i in self.自选装备:
                自选装备名称.append(i.currentText())
            for j in range(len(装备列表)):
                if 装备列表[j].品质 == '神话':
                    if self.装备选择状态[j] == 1 or 装备列表[j].名称 in 自选装备名称:
                        self.神话属性图片[num].move(int(self.width() / 7 * (count1 % 7+ 0.42)), int(self.height() / 5.2 * (count2 + 0.05)))
                        for i in range(4):
                            self.神话属性选项[num * 4 + i].move(int(self.width() / 7 * (count1 % 7) + 12), int(self.height() / 5.2 * (count2 + 0.05)) + i * 22 + 32)
                        count1 += 1
                        if count1 % 7 == 0:
                            count2 += 1
                    else:
                        self.神话属性图片[num].move(-1000,-1000)
                        for i in range(4):
                            self.神话属性选项[num * 4 + i].move(-1000,-1000)
                    num += 1
        if index == 4:
            self.自选计算(1)

    def 修正套装计算(self, x):
        self.有效穿戴组合.clear()
        self.有效穿戴套装.clear()
        装备 = []
        套装 = []
        套装字典 = {}
        if x == 0:
            for i in self.有效部位列表:
                装备.append(i[0])
        elif x == 1:
            for i in self.自选装备:
                装备.append(i.currentText())         
  
        for i in 装备:
            j = 装备列表[装备序号[i]].所属套装
            if j == '智慧产物':
                try:
                    k = 装备列表[装备序号[i]].所属套装2
                    套装字典[k] = 套装字典.get(k, 0) + 1
                except:
                    pass
            elif j != '无':
                套装字典[j] = 套装字典.get(j, 0) + 1

        for i in 套装字典.keys():
            if 套装字典[i] >= 2 and (i + '[2]') in 套装序号.keys():
                套装.append(i + '[2]')
            if 套装字典[i] >= 3 and (i + '[3]') in 套装序号.keys():
                套装.append(i + '[3]')
            if 套装字典[i] >= 5 and (i + '[5]') in 套装序号.keys():
                套装.append(i + '[5]')
        
        self.有效穿戴组合.append(装备)
        self.有效穿戴套装.append(套装)

    #一键修正计算
    def 一键修正(self, x = 0):
        if x == 0:
            if self.组合计算(2) == 0:
                QMessageBox.information(self,"错误",  "请勾选齐全身上穿戴的装备")
                return
            if self.组合计算(2) > 1:
                QMessageBox.information(self,"错误",  "请勿勾选身上未穿戴的装备")
                return
        self.修正套装计算(x)
        self.角色属性B = deepcopy(self.初始属性)
        self.角色属性B.技能栏 = deepcopy(self.初始属性.技能栏)
        self.输入属性(self.角色属性B)
        self.角色属性B.穿戴装备(self.有效穿戴组合[0],self.有效穿戴套装[0])
        for i in self.角色属性B.装备栏:
            装备列表[装备序号[i]].城镇属性(self.角色属性B)
        for i in self.角色属性B.套装栏:
            套装列表[套装序号[i]].城镇属性(self.角色属性B)
        self.角色属性B.装备基础()
        self.角色属性B.被动倍率计算()
        self.面板修正(self.角色属性B.伤害类型, x * 3)

    def 面板修正(self, 类型, x):
        数据 = []
        原始数据 = []
        名称 = ['力智', '三攻', '属强']
        for i in range(3):
            try:
                if self.一键站街设置输入[i + x].text() != '':
                    数据.append(int(self.一键站街设置输入[i + x].text()))
                else:
                    数据.append(0)
            except:
                QMessageBox.information(self, "错误", 名称[i] + "输入格式错误，已重置为空")
                self.一键站街设置输入[i + x].setText('')
                数据.append(0)
        
        if sum(数据) == 0:
            return

        if 数据[0] != 0 and 数据[1] == 0:
            QMessageBox.information(self,"错误",  "请输入三攻")
            return
            
        for i in range(5):
            if self.属性设置输入[i][15].text() != '':
                原始数据.append(int(self.属性设置输入[i][15].text()))
            else:
                原始数据.append(0)
        if 数据[1] != 0:
            if 类型 == '物理百分比': self.物理百分比修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街力量()), 数据[1], 原始数据[0], 原始数据[2])
            elif 类型 == '魔法百分比': self.魔法百分比修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街智力()), 数据[1], 原始数据[1], 原始数据[3])
            elif 类型 == '物理固伤': self.物理固伤修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街力量()), 数据[1], 原始数据[0], 原始数据[4])
            elif 类型 == '魔法固伤': self.魔法固伤修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街智力()), 数据[1], 原始数据[1], 原始数据[4])

        if 数据[2] != 0:
            self.属强修正(数据[2])
        self.click_window(2)
        QMessageBox.information(self,"自动修正计算完毕",  "仅对站街修正进行了修改，使面板与输入一致<br>请自行核对其它页面 非力智三攻属强 条目")

    def 物理百分比修正(self, 输入力智, 输入三攻, 修正力量2, 修正物理攻击力2):
        修正前力量 = self.角色属性B.力量
        修正前物理攻击力 =self.角色属性B.物理攻击力
        站街物理攻击倍率 = self.角色属性B.站街物理攻击力倍率()
        j = round(输入三攻/站街物理攻击倍率/(输入力智 / 250 + 1),0)
        if self.初始属性.实际名称 == '黑暗武士':
            self.角色属性B.力量 = 输入力智 / self.角色属性B.技能栏[38].力智倍率()
            修正力量 = int(输入力智 / self.角色属性B.技能栏[38].力智倍率() + 1) - int(修正前力量)
        else:
            self.角色属性B.力量 = 输入力智
            修正力量 = 输入力智- int(修正前力量)
        #验证
        站街实际三攻 = int(j)
        for k in range(int(j)-2,int(j)+3):
            self.角色属性B.物理攻击力 = float(k)
            验证物理攻击力1 = int(self.角色属性B.站街物理攻击力())
            self.角色属性B.物理攻击力 = float(k+1)
            验证物理攻击力2 = int(self.角色属性B.站街物理攻击力())
            if 验证物理攻击力1 <= 输入三攻 and 验证物理攻击力2 > 输入三攻:
                站街实际三攻 = float(k)
        修正物理攻击力 = 站街实际三攻 - 修正前物理攻击力
        self.属性设置输入[0][15].setText(str(int(修正力量 + 修正力量2)))
        self.属性设置输入[2][15].setText(str(int(修正物理攻击力 + 修正物理攻击力2)))

    def 魔法百分比修正(self, 输入力智, 输入三攻, 修正智力2, 修正魔法攻击力2):
        修正前智力 = self.角色属性B.智力
        修正前魔法攻击力 =self.角色属性B.魔法攻击力
        站街魔法攻击倍率 = self.角色属性B.站街魔法攻击力倍率()
        j = round(输入三攻/站街魔法攻击倍率/(输入力智 / 250 + 1),0)
        if self.初始属性.实际名称 == '黑暗武士':
            self.角色属性B.智力 = 输入力智 / self.角色属性B.技能栏[38].力智倍率()
            修正智力 = int(输入力智 / self.角色属性B.技能栏[38].力智倍率() + 1) - int(修正前智力)
        else:
            self.角色属性B.智力 = 输入力智
            修正智力 = 输入力智 - int(修正前智力)
        #验证
        站街实际三攻 = int(j)
        for k in range(int(j)-2,int(j)+3):
            self.角色属性B.魔法攻击力 = float(k)
            验证魔法攻击力1 = int(self.角色属性B.站街魔法攻击力())
            self.角色属性B.魔法攻击力 = float(k+1)
            验证魔法攻击力2 = int(self.角色属性B.站街魔法攻击力())
            if 验证魔法攻击力1 <= 输入三攻 and 验证魔法攻击力2 > 输入三攻:
                站街实际三攻 = float(k)
        修正魔法攻击力 = 站街实际三攻 - 修正前魔法攻击力
        self.属性设置输入[1][15].setText(str(int(修正智力 + 修正智力2)))
        self.属性设置输入[3][15].setText(str(int(修正魔法攻击力 + 修正魔法攻击力2)))

    def 物理固伤修正(self, 输入力智, 输入三攻, 修正力量2, 修正独立攻击力2):
        修正前力量 = self.角色属性B.力量
        修正前独立攻击力 =self.角色属性B.独立攻击力
        修正力量 = 输入力智 - int(修正前力量)
        站街独立攻击倍率 = self.角色属性B.站街独立攻击力倍率()
        j = round(输入三攻/站街独立攻击倍率,0)
        #验证
        站街实际三攻 = int(j)
        for k in range(int(j)-2,int(j)+3):
            self.角色属性B.独立攻击力 = float(k)
            验证独立攻击力1 = int(self.角色属性B.站街独立攻击力())
            self.角色属性B.独立攻击力 = float(k+1)
            验证独立攻击力2 = int(self.角色属性B.站街独立攻击力())
            if 验证独立攻击力1 <= 输入三攻 and 验证独立攻击力2 > 输入三攻:
                站街实际三攻 = float(k)
        修正独立攻击力 = 站街实际三攻 - 修正前独立攻击力
        self.属性设置输入[0][15].setText(str(int(修正力量 + 修正力量2)))
        self.属性设置输入[4][15].setText(str(int(修正独立攻击力 + 修正独立攻击力2)))

    def 魔法固伤修正(self, 输入力智, 输入三攻, 修正智力2, 修正独立攻击力2):
        修正前智力 = self.角色属性B.智力
        修正前独立攻击力 = self.角色属性B.独立攻击力
        修正智力 = 输入力智 - int(修正前智力)
        站街独立攻击倍率 = self.角色属性B.站街独立攻击力倍率()
        j = round(输入三攻 / 站街独立攻击倍率, 0)
        # 验证
        站街实际三攻 = int(j)
        for k in range(int(j) - 2, int(j) + 3):
            self.角色属性B.独立攻击力 = float(k)
            验证独立攻击力1 = int(self.角色属性B.站街独立攻击力())
            self.角色属性B.独立攻击力 = float(k + 1)
            验证独立攻击力2 = int(self.角色属性B.站街独立攻击力())
            if 验证独立攻击力1 <= 输入三攻 and 验证独立攻击力2 > 输入三攻:
                站街实际三攻 = float(k)
        修正独立攻击力 = 站街实际三攻 - 修正前独立攻击力
        self.属性设置输入[1][15].setText(str(int(修正智力 + 修正智力2)))
        self.属性设置输入[4][15].setText(str(int(修正独立攻击力 + 修正独立攻击力2)))

    def 属强修正(self, 输入属强):
        try:
            站街火强 = self.角色属性B.火属性强化加成() + self.角色属性B.火属性强化
        except:
            站街火强 = self.角色属性B.火属性强化
        try:
            站街冰强 = self.角色属性B.冰属性强化加成() + self.角色属性B.冰属性强化
        except:
            站街冰强 = self.角色属性B.冰属性强化
        try:
            站街光强 = self.角色属性B.光属性强化加成() + self.角色属性B.光属性强化
        except:
            站街光强 = self.角色属性B.光属性强化
        try:
            站街暗强 = self.角色属性B.暗属性强化加成() + self.角色属性B.暗属性强化
        except:
            站街暗强 = self.角色属性B.暗属性强化

        if self.属性设置输入[5][15].text() != '':
            修改前 = float(self.属性设置输入[5][15].text())
        else:
            修改前 = 0

        修正前属强 = int(max(站街火强, 站街冰强, 站街光强, 站街暗强))
        
        for k in range(-2,3):
            temp = int((输入属强 + k - 修正前属强) / self.角色属性B.所有属性强化增加)
            y = 修正前属强 + temp * self.角色属性B.所有属性强化增加
            if int(y) == 输入属强:
                break

        修改后 = temp + 修改前
        self.属性设置输入[5][15].setText(str(int(修改后)))

    def 神话数量判断(self, x = 0):
        count = 0
        for j in range(len(装备列表)):
            if 装备列表[j].品质 == '神话':
                if self.装备选择状态[j] == 1:
                    count += 1
        if x == 0:
            if count != 0:
                return False
            else:
                return True
        else:
            return count

    #计算
    def 计算(self):
        self.保存配置()
        self.角色属性A = deepcopy(self.初始属性)
        self.输入属性(self.角色属性A)
        self.角色属性A.开启切装 = 切装模式
        if 调试开关 == 1:
            self.输出界面(-1)
            return
        if self.神话数量判断() and self.神话排名选项.isChecked():
            QMessageBox.information(self,"错误",  "请勾选神话装备或取消勾选神话排名模式选项") 
            return
        self.有效部位列表备份 = []
        if self.组合计算(self.计算模式选择.currentIndex()) == 0:
            if self.计算模式选择.currentIndex() == 2 and 补全模式 != 0:
                self.有效部位列表备份 = deepcopy(self.有效部位列表)
                num = 0
                for i in self.有效部位列表:
                    if len(i) == 0 or (补全模式 == 2 and self.自选装备[num].currentText() not in i):
                        i.append(self.自选装备[num].currentText())
                    num += 1
            elif self.计算模式选择.currentIndex() == 0 and self.组合计算(1) != 0:
                QMessageBox.information(self, "错误", "已更换为套装模式，请再次计算")
                self.计算模式选择.setCurrentIndex(1)
                return
            elif self.计算模式选择.currentIndex() != 2 and self.组合计算(2) != 0:
                QMessageBox.information(self, "错误", "请更换为单件模式，并再次计算")
                return
            else:
                QMessageBox.information(self,"错误",  "无有效组合，请重新选择装备")
                return
        self.计算按钮1.setEnabled(False)
        self.计算按钮1.setStyleSheet(不可点击按钮样式)
        self.计算按钮2.setEnabled(False)
        self.计算按钮2.setStyleSheet(不可点击按钮样式)
        self.计算按钮3.setEnabled(False)
        self.计算按钮3.setStyleSheet(不可点击按钮样式)
        threading.Thread(target=self.计算线程, daemon=True).start()

    def 单件模式前四层组合(self):
        count = 0
        for a1 in self.有效部位列表[0]:
            for a2 in self.有效部位列表[5]:
                for a3 in self.有效部位列表[8]:
                    神话数量 = 0
                    for i in [a1, a2, a3]:
                        if 装备列表[装备序号[i]].品质 == '神话':
                            神话数量 += 1
                    if 神话数量 <= 1:
                        count += 1
        return count * len(self.有效部位列表[1])

    def 计算线程(self):
        logger.info("开始计算")
        self.最大使用线程数 = 工作线程数 - self.线程数选择.currentIndex()
        # -------------------------------------多线程计算流程开始-------------------------------------

        startTime = time.time()
        finished = False
        producer_data.calc_index += 1
        producer_data.produced_count = 0

        def log_result_queue_info(log_func, msg, mq: MinHeapWithQueue):
            log_func("calc#{}: {}: {} remaining_qize={} sync_batch_size={} processed_result={}, speed={:.2f}/s totalWork={}".format(
                producer_data.calc_index,
                mq.name, msg, mq.minheap_queue.qsize(), mq.minheap.batch_size, mq.minheap.processed_result_count, mq.process_results_per_second(), producer_data.produced_count
           ))
            self.update_remaining_signal.emit(str(mq.minheap.processed_result_count))

        def try_fetch_result(mq: MinHeapWithQueue):
            idx = 1
            while True:
                try:
                    minheap_to_merge = mq.minheap_queue.get(block=False)
                    mq.minheap.merge(minheap_to_merge)

                    if mq.minheap.processed_result_count >= 1000 * idx:
                        log_result_queue_info(logger.info, "try_fetch_result periodly report", mq)
                        idx = mq.minheap.processed_result_count // 1000 + 1
                except queue.Empty as error:
                    break

        def try_fetch_result_in_background(mq: MinHeapWithQueue):
            while not finished:
                log_result_queue_info(logger.info, "try_fetch_result_in_background", mq)
                try_fetch_result(mq)
                time.sleep(0.5)

        save_top_n = 堆大小上限
        if self.神话排名选项.isChecked() or 武器排名 == 1:
            save_top_n = 2 << 64

        mq = MinHeapWithQueue("排行", MinHeap(save_top_n, batch_size), multiprocessing.Manager().Queue())

        # 异步排行线程
        fetch_result_thread = threading.Thread(target=try_fetch_result_in_background, args=(mq,), daemon=True)
        fetch_result_thread.start()

        # 异步计算搭配
        mode_index = self.计算模式选择.currentIndex()
        total_task_count = self.组合计算(self.计算模式选择.currentIndex())
        if mode_index == 2:
            # 散件模式时
            total_task_count = self.单件模式前四层组合()

        batch_task_count = min(每个工作线程应处理的任务数 * 工作线程数, total_task_count, self.最大使用线程数)

        start_index, end_index = 0, 0
        task_batch_size = total_task_count // batch_task_count
        reminder = total_task_count % batch_task_count
        for i in range(batch_task_count):
            end_index = start_index + task_batch_size - 1
            if i < reminder:
                end_index+=1

            calc_data = CalcData()

            calc_data.是输出职业 = True

            calc_data.minheap_queue = mq.minheap_queue
            calc_data.角色属性A = deepcopy(self.角色属性A)
            calc_data.角色属性A.装备切装 = copy(self.角色属性A.装备切装)
            calc_data.角色属性A.技能切装 = copy(self.角色属性A.技能切装)
            calc_data.角色属性A.切装修正 = copy(self.角色属性A.切装修正)
            calc_data.角色属性A.宠物次数 = copy(self.角色属性A.宠物次数)
            calc_data.角色属性A.强化等级 = copy(self.角色属性A.强化等级)
            calc_data.角色属性A.改造等级 = copy(self.角色属性A.改造等级)
            calc_data.角色属性A.是否增幅 = copy(self.角色属性A.是否增幅)
            calc_data.角色属性A.次数输入 = copy(self.角色属性A.次数输入)

            calc_data.mode_index = mode_index
            calc_data.start_index = start_index
            calc_data.end_index = end_index

            calc_data.装备选择状态 = copy(self.装备选择状态)
            for i in self.有效部位列表:
                for j in i:
                    calc_data.装备选择状态[装备序号[j]] = 1
            if len(self.有效部位列表备份) != 0:
                self.有效部位列表 = deepcopy(self.有效部位列表备份)
            calc_data.拥有百变怪 = self.百变怪选项.isChecked()
            calc_data.神话属性选项 = [cb.currentIndex() for cb in self.神话属性选项]

            calc_data.minheap = MinHeap(save_top_n, batch_size)

            producer(calc_data)

            start_index = end_index + 1

        # 等到所有工作处理完成
        producer_data.work_queue.join()
        finished = True

        logger.warning("所有工作线程均已完成计算，总计用时={}".format(format_time(time.time() - startTime)))

        # 等待异步排行线程退出
        fetch_result_thread.join()

        # 最终将剩余结果（若有）也加入排序
        log_result_queue_info(logger.info, "after join", mq)
        try_fetch_result(mq)
        log_result_queue_info(logger.info, "after final", mq)

        # -------------------------------------多线程计算流程结束-------------------------------------

        self.排行数据.clear()
        self.伤害列表 = mq.minheap.getTop()
        if self.神话排名选项.isChecked():
            神话列表 = []
            for i in range(len(self.伤害列表)):
                tempstr = self.伤害列表[i][1:]
                for j in [0,5,8]:
                    if 装备列表[装备序号[tempstr[j]]].品质=='神话' and tempstr[j] not in 神话列表:
                        神话列表.append(tempstr[j])
                        self.排行数据.append(tempstr)
                if len(神话列表) >= self.神话数量判断(1):
                    break
        elif 武器排名 == 1:
            武器列表 = []
            for i in range(len(self.伤害列表)):
                tempstr = self.伤害列表[i][1:]
                if 装备列表[装备序号[tempstr[11]]].部位=='武器' and tempstr[11] not in 武器列表:
                    武器列表.append(tempstr[11])
                    self.排行数据.append(tempstr)
                if len(武器列表) >= len(self.有效武器列表):
                    break            
        else:
            for i in range(len(self.伤害列表)):
                self.排行数据.append(self.伤害列表[i][1:])

        totoalCostTime = time.time() - startTime
        logger.info((
            "计算完毕\n"
            "工作线程数={} 总计耗时={}"
       ).format(
            工作线程数, format_time(totoalCostTime),
       ))

        self.calc_done_signal.emit()

    def 数量显示(self, counter):
        if counter <= 9999 :
            return str(counter)
        else:
            counter /= 10000
            return ('%.2f' % counter) + '万'

    def update_remaining(self, count):
        temp = self.数量显示(int(count))
        self.计算按钮1.setText("完成:" + temp)
        self.计算按钮2.setText("完成:" + temp)
        self.计算按钮3.setText("完成:" + temp)

    def calc_done(self):
        self.计算按钮1.setText("开始计算")
        self.计算按钮1.setEnabled(True)
        self.计算按钮1.setStyleSheet(按钮样式)
        self.计算按钮2.setText("开始计算")
        self.计算按钮2.setEnabled(True)
        self.计算按钮2.setStyleSheet(按钮样式)
        self.计算按钮3.setText("开始计算")
        self.计算按钮3.setEnabled(True)
        self.计算按钮3.setStyleSheet(按钮样式)
        if len(self.排行数据) == 0:
            QMessageBox.information(self,"计算错误",  "无有效组合")
            return
        if len(self.排行数据) == 1:
            self.输出界面(0)
        else:
            self.排行界面()

    def 自选计算(self, x = 0):
        if x == 0:
            self.保存配置()
            self.排行窗口列表.clear()
            self.排行数据.clear()

        self.角色属性A = deepcopy(self.初始属性)
        if x == 0:
            self.输入属性(self.角色属性A)
        else:
            self.输入属性(self.角色属性A, 1)
        
        装备 = []
        for i in self.自选装备:
            装备.append(i.currentText())
        
        套装 = []
        套装字典 = {}
        for i in 装备:
            j = 装备列表[装备序号[i]].所属套装
            if j == '智慧产物':
                try:
                    k = 装备列表[装备序号[i]].所属套装2
                    套装字典[k] = 套装字典.get(k, 0) + 1
                except:
                    pass
            elif j != '无':
                套装字典[j] = 套装字典.get(j, 0) + 1

        for i in 套装字典.keys():
            if 套装字典[i] >= 2 and (i + '[2]') in 套装序号.keys():
                套装.append(i + '[2]')
            if 套装字典[i] >= 3 and (i + '[3]') in 套装序号.keys():
                套装.append(i + '[3]')
            if 套装字典[i] >= 5 and (i + '[5]') in 套装序号.keys():
                套装.append(i + '[5]')
        
        if x != 0:
            伤害列表 = []
            for i in range(len(辟邪玉列表)):
                temp = deepcopy(self.初始属性)
                self.输入属性(temp, 100 + i)
                temp.穿戴装备(装备,套装)
                伤害列表.append(temp.伤害计算(0))

            提升率 = []
            for i in range(1, len(伤害列表)):
                if 伤害列表[0] != 0:
                    提升率.append(伤害列表[i] / 伤害列表[0] - 1)
                else:
                    提升率.append(0)

            提升率排序 = copy(提升率)
            提升率排序.sort(reverse=True)

            for i in range(0, len(提升率)):
                temp = str('%.2f' % (提升率[i] * 100)) + '%'
                self.辟邪玉提升率2[i].setText(temp)
                x = 提升率排序.index(提升率[i]) / len(提升率) * 10 - 2
                y = 1 / (1 + math.exp(-x))
                颜色 = (int(255 - 80 * y), int(245 - 100 * y), int(0 + 150 * y))
                self.辟邪玉提升率1[i].setStyleSheet('QLabel{font-size:12px;color:rgb'+ str(颜色) + '}')
                self.辟邪玉提升率2[i].setStyleSheet('QLabel{font-size:12px;color:rgb'+ str(颜色) + '}')

            self.角色属性A = deepcopy(self.初始属性)
            self.输入属性(self.角色属性A)
            C = self.站街计算(装备, 套装)
            B = deepcopy(self.角色属性A)
            B.穿戴装备(装备,套装)
            B.其它属性计算()

            总伤害数值 = B.伤害计算(0)
            if len(self.基准值) != 0:
                self.总伤害.setText(self.百分比输出(总伤害数值, self.基准值[0]))
            else:
                self.总伤害.setText(self.格式化输出(str(int(总伤害数值))))

            if self.韩服面板.isChecked():
                y = 1
            else:
                y = 0

            tempstr = self.装备描述计算(B)
            for l in range(12):
                self.图片显示[l].setToolTip(tempstr[l])

            self.面板显示[0].setText(str(int(B.面板力量())))
            self.面板显示[1].setText(str(int(B.面板物理攻击力(y))))
            self.面板显示[2].setText(str(int(B.面板智力())))
            self.面板显示[3].setText(str(int(B.面板魔法攻击力(y))))

            self.面板显示[5].setText(str(int(B.火属性强化)))
            self.面板显示[6].setText(str(int(B.冰属性强化)))
            self.面板显示[7].setText(str(int(B.光属性强化)))
            self.面板显示[8].setText(str(int(B.暗属性强化)))

            tempstr = '<font color="#FFFFFF">'+str(int(C.站街独立攻击力()))+'</font>   '
            tempstr += '<font color="#96FF32">'+str(int(B.面板独立攻击力()))+'</font>'
            self.面板显示[4].setText(tempstr)

            self.面板显示[9].setText(str(int(C.站街力量())))
            self.面板显示[10].setText(str(int(C.站街物理攻击力(y))))
            self.面板显示[11].setText(str(int(C.站街智力())))
            self.面板显示[12].setText(str(int(C.站街魔法攻击力(y))))

            self.面板显示[13].setText(str(int(C.火属性强化)))
            self.面板显示[14].setText(str(int(C.冰属性强化)))
            self.面板显示[15].setText(str(int(C.光属性强化)))
            self.面板显示[16].setText(str(int(C.暗属性强化)))

            if B.攻击属性 == 0:
                属性倍率=1.05+0.0045*max(B.火属性强化 - 火抗输入,B.冰属性强化 - 冰抗输入,B.光属性强化 - 光抗输入,B.暗属性强化 - 暗抗输入)
            elif B.攻击属性 == 1:
                属性倍率=1.05+0.0045*(B.火属性强化 - 火抗输入)
            elif B.攻击属性 == 2:
                属性倍率=1.05+0.0045*(B.冰属性强化 - 冰抗输入)
            elif B.攻击属性 == 3:
                属性倍率=1.05+0.0045*(B.光属性强化 - 光抗输入)
            elif B.攻击属性 == 4:
                属性倍率=1.05+0.0045*(B.暗属性强化 - 暗抗输入)

            属白换算 = B.属性附加 * 属性倍率
            tempstr=[]
            tempstr.append('力智：'+str(int(round(B.百分比力智*100,0)))+'%') 
            tempstr.append('三攻：'+str(int(round(B.百分比三攻*100,0)))+'%') 
            tempstr.append('黄字：'+str(int(round(B.伤害增加*100,0)))+'%')
            temp = '白字：'+str(int(round(B.附加伤害*100,0))) +'%'
            if 属白换算 != 0:
                temp += ' ('+str(int(round(属白换算*100+B.附加伤害*100,0)))+'%)'
            tempstr.append(temp)
            temp = '属白：'+str(int(round(B.属性附加*100,0)))+'%'
            if 属白换算 != 0:
                temp += ' ('+str(int(round(属白换算*100,0)))+'%)'
            tempstr.append(temp)
            tempstr.append('爆伤：'+str(int(round(B.暴击伤害*100,0)))+'%')
            tempstr.append('终伤：'+str(int(round(B.最终伤害*100,0)))+'%')
            tempstr.append('技攻：'+str(int(round(B.技能攻击力*100-100,0)))+'%')
            tempstr.append('持续：'+str(int(round(B.持续伤害*100,0)))+'%') 
            tempstr.append('攻速：'+str(int(round(B.攻击速度*100,0)))+'%') 
            tempstr.append('释放：'+str(int(round(B.释放速度*100,0)))+'%') 
            tempstr.append('移速：'+str(int(round(B.移动速度*100,0)))+'%')

            count = 0
            for i in tempstr:
                self.词条显示[count].setText(i)
                count += 1

            for i in self.套装名称显示:
                i.setText('')
            count = 0

            self.套装名称显示[count].setText(self.称号.currentText())
            self.套装名称显示[count].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            self.套装名称显示[count].setToolTip('<font size="3" face="宋体"><font color="#78FF1E">' + self.称号.currentText() + '</font><br>' + 称号列表[self.称号.currentIndex()].装备描述(B)[:-4] + '</font>')
            count += 1

            self.套装名称显示[count].setText(self.宠物.currentText())
            self.套装名称显示[count].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            self.套装名称显示[count].setToolTip('<font size="3" face="宋体"><font color="#78FF1E">' + self.宠物.currentText() + '</font><br>' + 宠物列表[self.宠物.currentIndex()].装备描述(B)[:-4] + '</font>')
            count += 1


            self.套装名称显示[count].setText(装备[11])
            self.套装名称显示[count].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            count += 1

            神话所在套装 = []
            for i in range(0,11):
                if 装备列表[装备序号[装备[i]]].品质 == '神话':
                    神话所在套装.append(装备列表[装备序号[装备[i]]].所属套装)
            for i in range(0,len(套装)):
                self.套装名称显示[count].setText(套装[i])
                if 套装[i].split('[')[0] in 神话所在套装:
                    self.套装名称显示[count].setStyleSheet("QLabel{font-size:12px;color:rgb(226,150,146)}")   
                else:
                    self.套装名称显示[count].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")  
                self.套装名称显示[count].setToolTip('<font size="3" face="宋体"><font color="#78FF1E">'+套装[i]+'</font><br>'+套装列表[套装序号[套装[i]]].装备描述(B)[:-4]+'</font>')
                count += 1

        if x == 0:
            self.排行数据.append(装备 + [0] + 套装 + ['无'])
            self.输出界面(0)

    def 排行界面(self):
        self.排行窗口列表.clear()
        滚动排行 = QMainWindow()
        滚动排行.setStyleSheet('''QToolTip { 
           background-color: black; 
           color: white; 
           border: 0px
           }''')
        self.排行窗口列表.append(滚动排行)
        滚动排行.resize(630,530)
        滚动排行.setMinimumSize(630,530)
        滚动排行.setMaximumSize(630,1230)
        滚动排行.setWindowTitle('当前模板配装排行（点击伤害数字查看详情）')  
        滚动排行.setWindowIcon(self.icon)  
    
        背景颜色=QLabel(滚动排行)
        背景颜色.resize(630,1230)
        背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1.0)}")
    
        排行背景透明度=QGraphicsOpacityEffect()
        排行背景透明度.setOpacity(0.15)
        排行背景=QLabel(滚动排行)
        排行背景.resize(630,1230)
        排行背景.setPixmap(self.主背景图片)
        排行背景.setAlignment(Qt.AlignCenter)
        排行背景.setGraphicsEffect(排行背景透明度)
    
        wrapper = QWidget()
        滚动排行.setCentralWidget(wrapper)
        滚动排行.topFiller = QWidget()
        滚动排行.topFiller.setMinimumSize(570, 50*len(self.排行数据)+30)
    
        if len(self.排行数据)>10:
            初始x=-10
        else:
            初始x=0
        初始y=15
        x间隔=30
        y间隔=50
    
        最高伤害 = self.排行数据[0][12]

        技能选项 = []
        for i in self.技能设置输入:
            技能选项.append(i.currentText().replace('Lv+1', ''))

        if 输出数据 == 1:
            setfile = open('./'+self.角色属性A.实际名称 + '.csv', 'w', encoding='gbk')
        for i in range(0,len(self.排行数据)):
            if 输出数据 == 1:
                temp = ''
                for j in range(13):
                    temp += str(self.排行数据[i][j]) + ','
                temp += self.角色属性A.实际名称 + ','
                temp += 装备列表[装备序号[self.排行数据[i][11]]].类型
                setfile.write(temp + '\n')
            图片列表 = []
            for j in range(0,12):
                图片列表.append(self.装备图片[装备序号[self.排行数据[i][j]]])
            水平间距=[1,2,3,4,5,6.5,7.5,8.5,10,11,12,13.5]
            for j in range(0,12):
                装备 = 装备列表[装备序号[self.排行数据[i][j]]]
                图标=QLabel(滚动排行.topFiller)
                图标.setMovie(图片列表[j])
                图片列表[j].start()
                图标.move(int(初始x+x间隔*水平间距[j]),int(初始y+i*y间隔))
                if self.排行数据[i][j] == self.排行数据[i][-1]:
                    图标=QLabel(滚动排行.topFiller)
                    图标.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                    图标.resize(28,28)
                    图标.move(int(初始x+x间隔*水平间距[j]),int(初始y+i*y间隔))
                图标.setToolTip('<font size="3" face="宋体"><font color="' + 颜色[装备.品质] + '">' +装备.名称+'</font><br>'+ 装备.类型 + '-' + 装备.部位 + '<br>' + 装备.装备描述(self.角色属性A)[:-4] + '</font>')
                
            伤害量 = str(int(round(self.排行数据[i][12]/100000000,0)))
            if 最高伤害!=0:
                百分比=str(round(self.排行数据[i][12]/最高伤害*100,1))+'%'
            else:
                百分比=' 0.0%'
    
            if 百分比=='100.0%':
                详情按钮=QtWidgets.QPushButton(伤害量+' |'+百分比,滚动排行.topFiller)
            else:
                详情按钮=QtWidgets.QPushButton(伤害量+' | '+百分比,滚动排行.topFiller)
    
            详情按钮.clicked.connect(lambda state, index= i: self.输出界面(index))
            
            详情按钮.move(int(初始x+x间隔*15),int(初始y+i*y间隔))
            详情按钮.resize(120,30)
            temp = deepcopy(self.角色属性A)
            技能等级溢出 = temp.等级溢出判断(self.排行数据[i][0:12], self.排行数据[i][13:(len(self.排行数据[i]) - 1)])
            if  len(技能等级溢出) != 0:
                可调整技能 = ''
                不可调整技能 = ''
                for n in 技能等级溢出:
                    if n in 技能选项:
                        可调整技能 += n + ' '
                    else:
                        不可调整技能 += n + ' '
                if 可调整技能 != '':
                    详情按钮.setToolTip('<font size="3" face="宋体"><font color="#FF6666">' + 可调整技能 + 不可调整技能 + '</font>等级溢出，修改白金徽章或时装可以提高伤害。</font>')
                    详情按钮.setStyleSheet('QPushButton{font-size:14px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:10px} QPushButton:hover{background-color:rgba(225,5,65,0.8)}')
                else:
                    详情按钮.setStyleSheet(按钮样式+"QPushButton{font-size:14px}")
                    详情按钮.setToolTip('<font size="3" face="宋体"><font color="#FF6666">' + 不可调整技能 + '</font>等级溢出</font>')
            else:
                详情按钮.setStyleSheet(按钮样式+"QPushButton{font-size:14px}")
                详情按钮.setToolTip('<font size="3" face="宋体">点击查看详情</font>')
        滚动排行.scroll = QScrollArea()
        滚动排行.scroll.setStyleSheet("QScrollArea {background-color:transparent}")
        滚动排行.scroll.viewport().setStyleSheet("background-color:transparent")
        滚动排行.scroll.setWidget(滚动排行.topFiller)
        滚动排行.vbox = QVBoxLayout()
        滚动排行.vbox.addWidget(滚动排行.scroll)
        wrapper.setLayout(滚动排行.vbox)
    
        滚动排行.show()

    def 格式化输出(self, 数字文本, x = 0):
        if x == 1:
            返回值 = str('%.2f' % round(int(数字文本)/100000000,2))
        elif self.显示选项.isChecked():
            返回值 = str('%.2f' % round(int(数字文本)/100000000,2)) + '亿'
        else:
            返回值=''
            for i in range(0,len(数字文本)):
                if len(数字文本)%3==2 and i%3==2:
                    返回值+=','
                if len(数字文本)%3==1 and i%3==1:
                    返回值+=','
                if len(数字文本)%3==0 and i%3==0:
                    if i!=0:
                        返回值+=','
                返回值+=str(数字文本[i])
        return 返回值

    def 站街计算(self,装备名称,套装名称):
        C = deepcopy(self.角色属性A)
        C.穿戴装备(装备名称,套装名称)
        for i in C.装备栏:
            装备列表[装备序号[i]].城镇属性(C)
        for i in C.套装栏:
            套装列表[套装序号[i]].城镇属性(C)
        C.装备基础()
        C.被动倍率计算()

        return C

    def 装备描述计算(self, 属性):
        tempstr = []
        for i in range(0,12):
            装备 =  装备列表[装备序号[属性.装备栏[i]]]
            tempstr.append('<font size="3" face="宋体"><font color="' + 颜色[装备.品质] + '">' +装备.名称+'</font><br>')
            if 装备.所属套装 != '无':
                if 装备.所属套装 != '智慧产物':
                    y = ' ' + 装备.所属套装
                else:
                    try:
                        y = ' ' + 装备.所属套装2
                    except:
                        y = ' '
            else:
                y = ' '
            if i == 11:
                y += ' ' + 装备.类型
            tempstr[i] += 'Lv' + str(装备.等级) + ' ' + 装备.品质 + y

            if i < 5:
                x = 属性.防具精通计算(i)
                y = '<br>精通:'
                for n in 属性.防具精通属性:
                    y += n + ' '
                tempstr[i] += y + '+' + str(x)

            if 装备.所属套装 != '智慧产物':  
                if 属性.强化等级[i]!=0:
                    if i==8:
                        tempstr[i]+='<br><font color="#68D5ED">+'+str(属性.强化等级[i])+' 强化: '
                        tempstr[i]+='三攻 + '+str(耳环计算(装备.等级,装备.品质,属性.强化等级[i]))+'</font>'
                    if i in [9,10]:
                        tempstr[i]+='<br><font color="#68D5ED">+'+str(属性.强化等级[i])+' 强化: '
                        tempstr[i]+='四维 + '+str(左右计算(装备.等级,装备.品质,属性.强化等级[i])) +'</font>'
                    if i==11:
                        tempstr[i]+='<br><font color="#68D5ED">+'+str(属性.强化等级[i])+' 强化: '
                        tempstr[i]+='物理攻击力 + '+str(武器计算(装备.等级,装备.品质,属性.强化等级[i],装备.类型,'物理'))+'</font><br>'
                        tempstr[i]+='<font color="#68D5ED">+'+str(属性.强化等级[i])+' 强化: '
                        tempstr[i]+='魔法攻击力 + '+str(武器计算(装备.等级,装备.品质,属性.强化等级[i],装备.类型,'魔法'))+'</font>'

                if 属性.武器锻造等级!=0:
                    if i==11:
                        tempstr[i]+='<br><font color="#68D5ED">+'+str(属性.武器锻造等级)+'   锻造: '
                        tempstr[i]+='独立攻击力 + '+str(锻造计算(装备.等级,装备.品质,属性.武器锻造等级))+'</font>'

                if 属性.是否增幅[i]==1:
                    if tempstr[i] !='':
                        tempstr[i]+='<br>'
                    tempstr[i]+='<font color="#FF00FF">+'+str(属性.强化等级[i])+' 增幅: '
                    if '物理' in 属性.伤害类型 or '力量' in 属性.伤害类型:
                        tempstr[i]+='异次元力量 + '+str(增幅计算(装备.等级,装备.品质,属性.强化等级[i]))+'</font>'
                    else:
                        tempstr[i]+='异次元智力 + '+str(增幅计算(装备.等级,装备.品质,属性.强化等级[i]))+'</font>'

            if tempstr[i] != '':
                tempstr[i] += '<br>'
            tempstr[i] += 装备.装备描述(属性)[:-4]
            tempstr[i] += '</font>'
        return tempstr
    
    def 百分比输出(self, A, B):
        if B == 0:
            return self.格式化输出(str(int(A)))
        temp1 = A - B
        temp2 = round((A / B - 1) * 100, 2)
        if self.对比格式.isChecked():
            if temp1 == 0:
                return '<font face="宋体">无变化</font>'
            elif temp1 > 0:
                return '<font face="宋体" color= "#96FF1E">+' + self.格式化输出(str(int(temp1)), 1) + ' (' + str('%.2f' % abs(temp2)) + '%)</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + self.格式化输出(str(int(temp1)), 1) + ' (' + str('%.2f' % abs(temp2)) + '%)</font>'
        else:
            if temp2 == 0:
                return '<font face="宋体">无变化</font>'
            elif temp2 > 0:
                return '<font face="宋体" color= "#96FF1E">+' + str('%.2f' % temp2) + '%</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + str('%.2f' % temp2) + '%</font>'

    def 输出界面(self, index, name = ''):
        #调试模式下 index为-1
        flag = 1
        if index < 0:
            flag = 0
            index = 0
            武器名称 = ''
            for i in 装备列表:
                if i.类型 == self.角色属性A.武器选项[0]:
                    武器名称 = i.名称
                    break
            self.排行数据.append(['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的心之所念', '军神的遗书', '军神的庇护宝石', 武器名称, 0, '噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]', '无'])

        装备名称 = []
        套装名称 = []
        百变怪 = self.排行数据[index][-1]
        for i in range(0, 12):
            装备名称.append(self.排行数据[index][i])
        for i in range(13,len(self.排行数据[index])-1):
            套装名称.append(self.排行数据[index][i])
        self.角色属性B = deepcopy(self.角色属性A)
        self.角色属性B.穿戴装备(装备名称,套装名称)

        if flag == 1:
            C = self.站街计算(装备名称,套装名称)
            self.角色属性B.其它属性计算()
        else:
            C = deepcopy(self.角色属性A)
            C.穿戴装备(装备名称,套装名称)
            C.被动倍率计算()

        统计详情 = self.角色属性B.伤害计算(1)

        #最大输出界面限制
        if len(self.输出窗口列表)>=10:
            del self.输出窗口列表[0]
    
        输出窗口 = QWidget()
        输出窗口.setStyleSheet('''QToolTip { 
           background-color: black; 
           color: white; 
           border: 0px
           }''')
        self.输出窗口列表.append(输出窗口)
        输出窗口.setFixedSize(788, 564)
        temp = ''
        if name == '':
            temp += '详细数据'
        else:
            temp += name
        temp += '（最多显示前18个技能）'
        输出窗口.setWindowTitle(temp)
        输出窗口.setWindowIcon(self.icon)  
        QLabel(输出窗口).setPixmap(self.输出背景图片)
        人物 = QLabel(输出窗口)
        图片 = QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(90 + int(45 - 图片.width() / 2), 40)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)
      
        excel=[]
        for i in range(0,len(self.角色属性B.技能栏)):
            excel.append(统计详情[i*4+1])
        excel.sort()

        if self.韩服面板.isChecked():
            x = 1
        else:
            x = 0

        面板显示=[]
        for i in range(0,17):
            面板显示.append(QLabel(输出窗口))        
    
        面板显示[0].setText(str(int(self.角色属性B.面板力量())))
        面板显示[1].setText(str(int(self.角色属性B.面板物理攻击力(x))))
        面板显示[2].setText(str(int(self.角色属性B.面板智力())))
        面板显示[3].setText(str(int(self.角色属性B.面板魔法攻击力(x))))
        
        面板显示[5].setText(str(int(self.角色属性B.火属性强化)))
        面板显示[6].setText(str(int(self.角色属性B.冰属性强化)))
        面板显示[7].setText(str(int(self.角色属性B.光属性强化)))
        面板显示[8].setText(str(int(self.角色属性B.暗属性强化)))
        
        tempstr = '<font color="#FFFFFF">'+str(int(C.站街独立攻击力()))+'</font>   '
        tempstr += '<font color="#96FF1E">'+str(int(self.角色属性B.面板独立攻击力()))+'</font>'
        面板显示[4].setText(tempstr)

        面板显示[9].setText(str(int(C.站街力量())))
        面板显示[10].setText(str(int(C.站街物理攻击力(x))))
        面板显示[11].setText(str(int(C.站街智力())))
        面板显示[12].setText(str(int(C.站街魔法攻击力(x))))
        
        面板显示[13].setText(str(int(C.火属性强化)))
        面板显示[14].setText(str(int(C.冰属性强化)))
        面板显示[15].setText(str(int(C.光属性强化)))
        面板显示[16].setText(str(int(C.暗属性强化)))
        
        const = 139
        count = 0
        for i in  [9,10,0,1]:
            面板显示[i].move(20,const + count * 18)
            count += 1

        count = 0
        for i in  [11,12,2,3]:
            面板显示[i].move(150,const + count * 18)
            count += 1

        面板显示[4].move(150,const + count * 18)

        count = 5
        for i in  [5,6,7,8]:
            面板显示[i].move(150,const + count * 18)
            count += 1

        count = 5
        for i in  [13,14,15,16]:
            面板显示[i].move(20,const + count * 18)
            count += 1
      
        for i in range(0,len(面板显示)):
            if i >= 9:
                面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            else:
                面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(150,255,30)}")
            面板显示[i].resize(100,18)
            面板显示[i].setAlignment(Qt.AlignRight)

        if self.角色属性B.攻击属性 == 0:
            属性倍率=1.05+0.0045*max(self.角色属性B.火属性强化 - 火抗输入,self.角色属性B.冰属性强化 - 冰抗输入,self.角色属性B.光属性强化 - 光抗输入,self.角色属性B.暗属性强化 - 暗抗输入)
        elif self.角色属性B.攻击属性 == 1:
            属性倍率=1.05+0.0045*(self.角色属性B.火属性强化 - 火抗输入)
        elif self.角色属性B.攻击属性 == 2:
            属性倍率=1.05+0.0045*(self.角色属性B.冰属性强化 - 冰抗输入)
        elif self.角色属性B.攻击属性 == 3:
            属性倍率=1.05+0.0045*(self.角色属性B.光属性强化 - 光抗输入)
        elif self.角色属性B.攻击属性 == 4:
            属性倍率=1.05+0.0045*(self.角色属性B.暗属性强化 - 暗抗输入)

        属白换算 = self.角色属性B.属性附加 * 属性倍率
        tempstr=[]
        tempstr.append('力智：'+str(int(round(self.角色属性B.百分比力智*100,0)))+'%') 
        tempstr.append('三攻：'+str(int(round(self.角色属性B.百分比三攻*100,0)))+'%') 
        tempstr.append('黄字：'+str(int(round(self.角色属性B.伤害增加*100,0)))+'%')
        
        temp = '白字：'+str(int(round(self.角色属性B.附加伤害*100,0))) +'%'
        if 属白换算 != 0:
            temp += ' ('+str(int(round(属白换算*100+self.角色属性B.附加伤害*100,0)))+'%)'
        tempstr.append(temp)

        temp = '属白：'+str(int(round(self.角色属性B.属性附加*100,0)))+'%'
        if 属白换算 != 0:
            temp += ' ('+str(int(round(属白换算*100,0)))+'%)'

        tempstr.append(temp)

        tempstr.append('爆伤：'+str(int(round(self.角色属性B.暴击伤害*100,0)))+'%')
        tempstr.append('终伤：'+str(int(round(self.角色属性B.最终伤害*100,0)))+'%')
        tempstr.append('技攻：'+str(int(round(self.角色属性B.技能攻击力*100-100,0)))+'%')
        tempstr.append('持续：'+str(int(round(self.角色属性B.持续伤害*100,0)))+'%') 
        tempstr.append('攻速：'+str(int(round(self.角色属性B.攻击速度*100,0)))+'%') 
        tempstr.append('释放：'+str(int(round(self.角色属性B.释放速度*100,0)))+'%') 
        tempstr.append('移速：'+str(int(round(self.角色属性B.移动速度*100,0)))+'%') 

        j=312
        for i in tempstr:
            templab=QLabel(输出窗口)
            templab.setText(i)
            templab.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            templab.move(20,j)
            templab.resize(180,17)
            templab.setAlignment(Qt.AlignLeft)
            j+=17

        位置 = 313
        间隔 = 20
        if self.角色属性B.红色宠物装备 != '默认':
            套装名称.append('红宠：' + self.角色属性B.红色宠物装备)
            位置 -= 5
            间隔 -= 1
        
        适用称号名称=QLabel(self.称号.currentText(),输出窗口)
        适用称号名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用称号名称.move(114, 位置)
        适用称号名称.resize(150,18)
        适用称号名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔
        适用称号名称.setToolTip('<font size="3" face="宋体"><font color="#78FF1E">' + self.称号.currentText()+'</font><br>'+称号列表[self.称号.currentIndex()].装备描述(self.角色属性B)[:-4]+'</font>')

        适用宠物名称=QLabel(self.宠物.currentText(),输出窗口)
        适用宠物名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用宠物名称.move(114, 位置)
        适用宠物名称.resize(150,18)
        适用宠物名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔
        适用宠物名称.setToolTip('<font size="3" face="宋体"><font color="#78FF1E">' + self.宠物.currentText()+'</font><br>'+宠物列表[self.宠物.currentIndex()].装备描述(self.角色属性B)[:-4]+'</font>')

        适用武器名称=QLabel(装备名称[11],输出窗口)
        适用武器名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用武器名称.move(114, 位置)
        适用武器名称.resize(150,18)
        适用武器名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔

        神话所在套装 = []
        for i in range(0,11):
            if 装备列表[装备序号[装备名称[i]]].品质 == '神话':
                神话所在套装.append(装备列表[装备序号[装备名称[i]]].所属套装)
        for i in range(0,len(套装名称)):
            适用套装名称=QLabel(输出窗口)
            适用套装名称.setText(套装名称[i])
            适用套装名称.move(114,位置+i*间隔)
            适用套装名称.resize(150,18)
            适用套装名称.setAlignment(Qt.AlignCenter)  
            if 套装名称[i].split('[')[0] in 神话所在套装:
                适用套装名称.setStyleSheet("QLabel{font-size:12px;color:rgb(226,150,146)}")   
            else:
                适用套装名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            sign = 1
            if self.角色属性B.红色宠物装备 != '默认':
                if i == len(套装名称) - 1:
                    sign = 0
            if sign == 1:
                适用套装名称.setToolTip('<font size="3" face="宋体"><font color="#78FF1E">'+套装名称[i]+'</font><br>'+套装列表[套装序号[套装名称[i]]].装备描述(self.角色属性B)[:-4]+'</font>')
  
        实际技能等级=[]
        技能等效CD=[]
        for i in self.角色属性B.技能栏:
            实际技能等级.append(i.等级)
            if i.是否有伤害==1:
                技能等效CD.append(i.等效CD(self.角色属性B.武器类型))
            else:
                技能等效CD.append(0)
    
        总伤害数值=0

        count = 0
        for i in range(0,len(self.角色属性B.技能栏)):
            if 统计详情[i*4 + 1] != 0:
                count += 1
        count = min(18, count)
        self.行高 = min(int(440 / count),30)        
        
        伤害列表 = []
        for i in range(0,len(self.角色属性B.技能栏)):
            伤害列表.append(统计详情[i*4+1])
            总伤害数值 += 统计详情[i*4+1]
        伤害列表.sort(reverse = True)
        for i in range(0,len(self.角色属性B.技能栏)):
            if 伤害列表.index(统计详情[i * 4 + 1]) >= count:
                统计详情[i * 4 + 1] = 0

        if len(self.基准值) != 0:
            显示模式 = 1
        else:
            显示模式 = 0

        for i in range(0,len(self.角色属性B.技能栏)):
            j=len(self.角色属性B.技能栏)-1-excel.index(统计详情[i*4+1])
            if 统计详情[i*4 + 1] != 0:
                每行详情=[]
                for k in range(0,7):
                    每行详情.append(QLabel(输出窗口))
                #图片
                每行详情[0].setPixmap(self.技能图片[i])
                每行详情[0].resize(28,min(28,self.行高 - 2)) 
                try:
                    tempstr='<font face="宋体"><font color="#FF6666">'+self.角色属性B.技能栏[i].名称+self.角色属性B.技能栏[i].备注+ '</font><br>'
                    tempstr+='百分比：'+str(int(self.角色属性B.技能栏[i].等效百分比(self.角色属性B.武器类型) / self.角色属性B.技能栏[i].倍率))+'%<br>'
                    tempstr+='被动倍率：'+str(round(self.角色属性B.技能栏[i].被动倍率*100,1))+'%<br>'
                    if self.角色属性B.技能栏[i].倍率!=0:
                        tempstr+='其它倍率：'+str(round(self.角色属性B.技能栏[i].倍率*100,1))+'%<br>'
                    tempstr+='CD显示：'+str(round(self.角色属性B.技能栏[i].等效CD(self.角色属性B.武器类型) * self.角色属性B.技能栏[i].恢复,2))+'s<br>'
                    tempstr+='CD恢复：'+str(round(self.角色属性B.技能栏[i].恢复*100,1))+'%</font>'
                    每行详情[0].setToolTip(tempstr)
                except:
                    pass
    
                每行详情[0].move(302, 50 + j * self.行高)
                #等级
                每行详情[1].setText('Lv.'+str(实际技能等级[i]))
                每行详情[1].move(337, 50 + j * self.行高)
                每行详情[1].resize(30,min(28,self.行高)) 
                #CD
                每行详情[2].setText(str(技能等效CD[i])+'s')
                每行详情[2].move(380, 50 + j * self.行高)
                每行详情[2].resize(36,min(28,self.行高))
                #次数
                每行详情[3].setText(str(统计详情[i*4]))
                每行详情[3].move(418, 50 + j * self.行高)
                每行详情[3].resize(30,min(28,self.行高)) 
                #总伤害
                if 显示模式 == 1:
                    每行详情[4].setText(self.百分比输出(统计详情[i*4+1], self.基准值[1][i*4+1]))
                else:
                    每行详情[4].setText(self.格式化输出(str(int(统计详情[i*4+1]))))
                每行详情[4].move(448, 50 + j * self.行高)
                每行详情[4].resize(108,min(28,self.行高)) 
                #平均伤害
                if 显示模式 == 1:
                    每行详情[5].setText(self.百分比输出(统计详情[i*4+2], self.基准值[1][i*4+2]))
                else:
                    每行详情[5].setText(self.格式化输出(str(int(统计详情[i*4+2]))))
                每行详情[5].move(555, 50 + j * self.行高) 
                每行详情[5].resize(108,min(28,self.行高)) 
                #占比
                每行详情[6].setText(str(round(统计详情[i*4+3],1))+'%')
                每行详情[6].move(660, 50 + j * self.行高)
                每行详情[6].resize(108,min(28,self.行高))
     
                for l in range(1,7):
                    每行详情[l].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
                    每行详情[l].setAlignment(Qt.AlignCenter) 
    
        #被动详情
        num=0
        for i in range(0,len(self.角色属性B.技能栏)):
            # Will修改
            tempstr = ''
            if self.角色属性B.技能栏[i].所在等级 != 100 or self.角色属性B.技能栏[i].是否主动 == 0:
                if self.角色属性B.技能栏[i].等级 > 0:
                    if self.角色属性B.技能栏[i].自定义描述 == 1:
                        tempstr+= '<font face="宋体"><font color="#FF6666">'+self.角色属性B.技能栏[i].名称+'</font><br>'
                        tempstr+= self.角色属性B.技能栏[i].技能描述(self.角色属性B.武器类型)            
                    else:
                        if self.角色属性B.技能栏[i].关联技能 != ['无'] and self.角色属性B.技能栏[i].加成倍率(self.角色属性B.武器类型) != 1:
                            tempstr+='<font face="宋体"><font color="#FF6666">'+self.角色属性B.技能栏[i].名称+'</font><br>'
                            tempstr+='加成倍率：'+str(round(self.角色属性B.技能栏[i].加成倍率(self.角色属性B.武器类型)*100-100,2))+'%<br>'
                            tempstr+='关联技能：'
                            for j in self.角色属性B.技能栏[i].关联技能:
                                tempstr+=j
                                if j != self.角色属性B.技能栏[i].关联技能[-1]:
                                    tempstr+=','
                            if self.角色属性B.技能栏[i].关联技能2 != ['无']:
                                tempstr+='<br>加成倍率：'+str(round(self.角色属性B.技能栏[i].加成倍率2(self.角色属性B.武器类型)*100-100,2))+'%<br>'
                                tempstr+='关联技能：'
                                for k in self.角色属性B.技能栏[i].关联技能2:
                                    tempstr+=k
                                    if k != self.角色属性B.技能栏[i].关联技能2[-1]:
                                        tempstr+=','
                            if self.角色属性B.技能栏[i].关联技能3 != ['无']:
                                tempstr+='<br>加成倍率：'+str(round(self.角色属性B.技能栏[i].加成倍率3(self.角色属性B.武器类型)*100-100,2))+'%<br>'
                                tempstr+='关联技能：'
                                for l in self.角色属性B.技能栏[i].关联技能3:
                                    tempstr+=l
                                    if l != self.角色属性B.技能栏[i].关联技能3[-1]:
                                        tempstr+=','
                        if self.角色属性B.技能栏[i].冷却关联技能 != ['无'] and self.角色属性B.技能栏[i].CD缩减倍率(self.角色属性B.武器类型) != 1:
                            if tempstr == '':
                                tempstr+='<font face="宋体"><font color="#FF6666">'+self.角色属性B.技能栏[i].名称+'</font><br>'
                            else:
                                tempstr+='<br>'
                            tempstr+='冷却缩减：'+str(round(100 - self.角色属性B.技能栏[i].CD缩减倍率(self.角色属性B.武器类型)*100,2))+'%<br>'
                            tempstr+='冷却关联技能：'
                            for j in self.角色属性B.技能栏[i].冷却关联技能:
                                tempstr+=j
                                if j != self.角色属性B.技能栏[i].冷却关联技能[-1]:
                                    tempstr+=','
                            if self.角色属性B.技能栏[i].冷却关联技能2 != ['无']:
                                tempstr+='<br>冷却缩减：'+str(round(100 - self.角色属性B.技能栏[i].CD缩减倍率2(self.角色属性B.武器类型)*100,2))+'%<br>'
                                tempstr+='冷却关联技能：'
                                for j in self.角色属性B.技能栏[i].冷却关联技能2:
                                    tempstr+=j
                                    if j != self.角色属性B.技能栏[i].冷却关联技能2[-1]:
                                        tempstr+=','
                            if self.角色属性B.技能栏[i].冷却关联技能3 != ['无']:
                                tempstr+='<br>冷却缩减：'+str(round(100 - self.角色属性B.技能栏[i].CD缩减倍率3(self.角色属性B.武器类型)*100,2))+'%<br>'
                                tempstr+='冷却关联技能：'
                                for j in self.角色属性B.技能栏[i].冷却关联技能3:
                                    tempstr+=j
                                    if j != self.角色属性B.技能栏[i].冷却关联技能3[-1]:
                                        tempstr+=','             
                if tempstr != '':
                    tempstr += '</font>'
                    被动数据=QLabel(输出窗口)
                    被动数据.setPixmap(self.技能图片[i])
                    被动数据.setToolTip(tempstr)
                    被动数据.move(293+num*40, 500)
                    被动等级=QLabel(输出窗口)
                    被动等级.setText('Lv.'+str(实际技能等级[i]))
                    被动等级.move(293-6+num*40, 480)
                    被动等级.resize(40,28)
                    if 实际技能等级[i] != 0:
                        被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
                    else:
                        被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,0,0)}")
                    被动等级.setAlignment(Qt.AlignCenter)  
                    num+=1
        
        if self.角色属性B.远古记忆 > 0:
            被动数据=QLabel(输出窗口)
            被动数据.setPixmap((QPixmap('./ResourceFiles/img/远古记忆.png')))
            tempstr='<font face="宋体"><font color="#FF6666">'+'远古记忆'+'</font><br>'
            tempstr+='智力+'+str(self.角色属性B.远古记忆 * 15)+'</font>'
            被动数据.setToolTip(tempstr)
            被动数据.move(293+num*40, 500)
            被动等级=QLabel(输出窗口)
            被动等级.setText('Lv.'+str(self.角色属性B.远古记忆))
            被动等级.move(293-6+num*40, 480)
            被动等级.resize(40,28)
            被动等级.setAlignment(Qt.AlignCenter)
            被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")  
            num+=1

        if self.角色属性B.刀魂之卡赞 > 0:
            被动数据=QLabel(输出窗口)
            被动数据.setPixmap((QPixmap('./ResourceFiles/img/刀魂之卡赞.png')))
            tempstr='<font face="宋体"><font color="#FF6666">'+'刀魂之卡赞'+'</font><br>'
            tempstr+='力量/智力+'+str(刀魂之卡赞数据[self.角色属性B.刀魂之卡赞])+'</font>'
            被动数据.setToolTip(tempstr)
            被动数据.move(293+num*40, 500)
            被动等级=QLabel(输出窗口)
            被动等级.setText('Lv.'+str(self.角色属性B.刀魂之卡赞))
            被动等级.move(293-6+num*40, 480)
            被动等级.resize(40,28)
            被动等级.setAlignment(Qt.AlignCenter)
            被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")  
            num+=1
    
        总伤害=QLabel(输出窗口)
        总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        if 显示模式 == 1:
            总伤害.setText(self.百分比输出(总伤害数值, self.基准值[0]))
        else:
            总伤害.setText(self.格式化输出(str(int(总伤害数值))))
        总伤害.resize(250,36)
        总伤害.move(10,520)
        总伤害.setAlignment(Qt.AlignCenter) 
    
        初始x=10;初始y=31
    
        图片列表 = []
    
        for i in range(0,12):
            图片列表.append(self.装备图片[装备序号[self.排行数据[index][i]]])
    
        偏移量=187
        x坐标=[32,0,0,32,0,偏移量,偏移量+32,偏移量+32,偏移量,偏移量,偏移量+32,32]
        y坐标=[0,0,32,32,64,0,0,32,64,32,64,64]
    
        tempstr = self.装备描述计算(self.角色属性B)

        for i in range(0,12):
            装备图标=QLabel(输出窗口)
            装备图标.setMovie(图片列表[i])
            图片列表[i].start()
            装备图标.resize(26,26)
            装备图标.move(初始x+x坐标[i],初始y+y坐标[i])
            装备图标.setAlignment(Qt.AlignCenter) 
            装备 =  装备列表[装备序号[self.角色属性B.装备栏[i]]]
            if self.角色属性B.装备栏[i] == 百变怪:
                图标遮罩=QLabel(输出窗口)
                图标遮罩.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                图标遮罩.resize(26,26)
                图标遮罩.move(初始x+x坐标[i],初始y+y坐标[i])
                图标遮罩.setToolTip(tempstr[i])
            else:
                装备图标.setToolTip(tempstr[i])

        for i in range(0,12):
            装备 =  装备列表[装备序号[self.角色属性B.装备栏[i]]]
            打造状态=QLabel(输出窗口)
            if 装备.所属套装 != '智慧产物':    
                打造状态.setText('+'+str(self.角色属性B.强化等级[i]))
                if self.角色属性B.是否增幅[i]==1:
                    打造状态.setStyleSheet("QLabel{color:rgb(228,88,169);font-size:12px;font-weight:Bold}")
                else:
                    打造状态.setStyleSheet("QLabel{color:rgb(25,199,234);font-size:12px;font-weight:Bold}")
                
            else:
                打造状态.setText('+'+str(self.角色属性B.改造等级[i]))
                打造状态.setStyleSheet("QLabel{color:rgb(249,141,62);font-size:12px;font-weight:Bold;}")
            
            打造状态.move(初始x+x坐标[i]+13,初始y+y坐标[i]-8)
        
        装备 =  装备列表[装备序号[self.角色属性B.装备栏[11]]]
        if 装备.所属套装 != '智慧产物' and self.角色属性B.武器锻造等级 != 0:
            打造状态=QLabel(输出窗口)
            打造状态.setText('+'+str(self.角色属性B.武器锻造等级))
            打造状态.setStyleSheet("QLabel{color:rgb(232,104,24);font-size:12px;font-weight:Bold}")
            打造状态.move(初始x+x坐标[11]+13,初始y+y坐标[11]+20)

        输出窗口.show()  

    def 希洛克属性计算(self, 属性):
        数量 = [0] * 3
        for i in range(15):
            数量[i % 3] += self.希洛克选择状态[i]
        
        #下装属性1
        if 数量[0] == 1:
            属性.最终伤害加成(0.05)

        #戒指属性1
        if 数量[1] == 1:
            属性.百分比三攻加成(0.05)

        #辅助装备属性1
        if 数量[2] == 1:
            属性.技能攻击力加成(0.05)
        
        i = 0 #奈克斯属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.伤害增加加成(0.05) #下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.暴击伤害加成(0.05) #戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.百分比力智加成(0.05) #辅助装备

        i = 1 #暗杀者属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.伤害增加加成(0.02)
            属性.技能冷却缩减(1,45,0.2) #下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.暴击伤害加成(0.03)
            属性.技能冷却缩减(60,70,0.2) #戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.百分比力智加成(0.03)
            属性.技能冷却缩减(75,80,0.17) #辅助装备

        i = 2 #卢克西属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.技能倍率加成(50,0.17)
            属性.技能倍率加成(85,0.17)
            属性.技能倍率加成(100,0.10) #下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.技能倍率加成(50,0.17)
            属性.技能倍率加成(85,0.17)
            属性.技能倍率加成(100,0.10) #戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.技能倍率加成(50,0.17)
            属性.技能倍率加成(85,0.17)
            属性.技能倍率加成(100,0.10)#辅助装备

        i = 3 #守门将属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.进图属强 += self.守门将属强.currentIndex() * 5 + 15 #下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.进图属强 += self.守门将属强.currentIndex() * 5 + 15 #戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.进图属强 += self.守门将属强.currentIndex() * 5 + 15 #辅助装备

        i = 4 #罗德斯属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.伤害增加加成(0.04) #下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.暴击伤害加成(0.04) #戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.百分比力智加成(0.04) #辅助装备

    def 输入属性(self, 属性, x = 0):
        if self.初始属性.远古记忆 != -1:
            属性.远古记忆 = self.远古记忆.currentIndex()
        if self.初始属性.刀魂之卡赞 != -1:
            属性.刀魂之卡赞 = self.刀魂之卡赞.currentIndex()

        if self.特色选项.isChecked():
            属性.特色选项 = 1

        if self.红色宠物装备.isChecked():
            属性.红色宠物装备 = '自适应'

        if self.转甲选项.isChecked():
            属性.转甲选项 = 1
        else:
            属性.转甲选项 = 0

        for j in [self.等级调整, self.TP输入, self.次数输入, self.宠物次数]:
            for i in j:
                if i != '' and i.currentIndex() == -1:
                    i.setCurrentIndex(0)

        for i in 属性.技能栏:
            i.等级 = i.基础等级+int(self.等级调整[self.角色属性A.技能序号[i.名称]].currentText())
            if i.是否有伤害==1:
                if i.TP上限!=0:
                    i.TP等级=int(self.TP输入[self.角色属性A.技能序号[i.名称]].currentText())

        if x == 0:
            self.辟邪玉属性计算(属性)
        elif x >= 100:
            y = x - 100
            辟邪玉列表[y].当前值 = 辟邪玉列表[y].最大值
            辟邪玉列表[y].穿戴属性(属性)

        属性.时间输入 = int(self.时间输入.currentText())
        属性.次数输入.clear()
        属性.宠物次数.clear()
        属性.装备切装.clear()
        属性.技能切装.clear()
        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.是否有伤害 == 1:
                属性.次数输入.append(self.次数输入[序号].currentText())
                if self.次数输入[序号].currentIndex() != 0:
                    self.宠物次数[序号].setCurrentIndex(min(self.宠物次数[序号].currentIndex(), self.次数输入[序号].currentIndex() - 1 + i.基础释放次数))
                属性.宠物次数.append(self.宠物次数[序号].currentIndex())
                if 切装模式 == 1:
                    if self.技能切装[序号].isChecked():
                        属性.技能切装.append(1)
                    else:
                        属性.技能切装.append(0)
            else:
                属性.次数输入.append('')
                属性.宠物次数.append(0)
                属性.技能切装.append(0)
        if 切装模式 == 1:
            for i in range(12):
                if self.装备切装[i].isChecked():
                    属性.装备切装.append(self.自选装备[i].currentText())
                else:
                    属性.装备切装.append('无')

        for i in range(len(self.复选框列表)):
            if self.复选框列表[i].isChecked():
                选项设置列表[i].适用效果(属性)
        
        count = 0
        for i in 装备列表:
            if i.品质 == '神话':
                i.属性1选择 = self.神话属性选项[count * 4 + 0].currentIndex()
                i.属性2选择 = self.神话属性选项[count * 4 + 1].currentIndex()
                i.属性3选择 = self.神话属性选项[count * 4 + 2].currentIndex()
                i.属性4选择 = self.神话属性选项[count * 4 + 3].currentIndex()
                count += 1
        
        属性.攻击属性 = self.攻击属性选项.currentIndex()

        称号列表[self.称号.currentIndex()].城镇属性(属性)
        if 属性.称号触发:
            称号列表[self.称号.currentIndex()].触发属性(属性)

        宠物列表[self.宠物.currentIndex()].城镇属性(属性)
        
        for k in range(3):
            if self.护石栏[k].currentText()!= '无':
                try:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石()
                except:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石(self.护石类型选项[k].currentIndex())
                    
        属性.护石第一栏 = self.护石栏[0].currentText()
        属性.护石第二栏 = self.护石栏[1].currentText()
        属性.护石第三栏 = self.护石栏[2].currentText()
    
        for i in range(0,9):
            if self.符文[i].currentText()!='无' and self.符文效果[i].currentText() != '无':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率 *= 1 + int(j.replace('攻击','').replace('%',''))/100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD *= 1 + int(j.replace('CD','').replace('%',''))/100

        for i in range(0,12):
            属性.是否增幅[i] = self.装备打造选项[i].currentIndex()
            属性.强化等级[i] = self.装备打造选项[i + 12].currentIndex()
            属性.改造等级[i] = self.装备打造选项[i + 24].currentIndex()
        属性.武器锻造等级 = self.装备打造选项[36].currentIndex()
        属性.伤害类型 = self.装备打造选项[37].currentText()

        try:
            属性.主BUFF = float(self.BUFF输入.text()) / 100 + 1
        except: 
            QMessageBox.information(self,"错误",  "BUFF数值输入错误,已设置为默认数值") 
            self.BUFF输入.setText(str('%.1f' % ((self.角色属性A.主BUFF - 1) * 100)))
        
        if self.角色属性A.技能栏[self.三觉序号].是否有伤害 == 1 and 属性.次数输入[self.三觉序号] == '0':
            属性.技能栏[self.三觉序号].关联技能 = ['无']
        else:
            if self.觉醒选择状态 == 1:
                属性.技能栏[self.三觉序号].关联技能 = [属性.技能栏[self.一觉序号].名称]
            if self.觉醒选择状态 == 2:
                属性.技能栏[self.三觉序号].关联技能 = [属性.技能栏[self.二觉序号].名称]
    
        属性.角色熟练度 = self.装备条件选择[0].currentIndex()
        属性.技能栏空位 = self.装备条件选择[1].currentIndex()
        属性.命运的抉择 = self.装备条件选择[2].currentIndex()
        属性.天命无常 = self.装备条件选择[3].currentIndex()
        属性.悲剧的残骸 = self.装备条件选择[4].currentIndex()
        属性.先知者的预言 = self.装备条件选择[5].currentIndex()
        属性.贫瘠沙漠的遗产 = self.装备条件选择[6].currentIndex()
        属性.幸运三角 = self.装备条件选择[7].currentIndex()
        属性.擎天战甲 = self.装备条件选择[8].currentIndex()
        属性.持续伤害计算比例 = 1 - 0.01 * self.装备条件选择[9].currentIndex()
        属性.军神的隐秘遗产 = self.装备条件选择[10].currentIndex()
        属性.太极天帝剑 = self.装备条件选择[11].currentIndex()
        属性.绿色生命的面容 = self.装备条件选择[12].currentIndex()
        
        self.希洛克属性计算(属性)
        self.基础属性(属性)
    
    def 技能加成判断(self, name, 属性):
        if self.特色选项.isChecked():
            pass
        else:
            if name == 'Lv1-30(主动)Lv+1':
                属性.技能等级加成('主动',1,30,1)
                return
            if name == 'Lv1-50(主动)Lv+1':
                属性.技能等级加成('主动',1,50,1)
                return
            if name == 'Lv1-35(主动)Lv+1':
                属性.技能等级加成('主动',1,35,1)
                return
            if name == 'Lv1-30(所有)Lv+1':
                属性.技能等级加成('所有',1,30,1)
                return
            if name == 'Lv1-20(所有)Lv+1':
                属性.技能等级加成('所有',1,20,1)
                return
            if name == 'Lv20-30(所有)Lv+1':
                属性.技能等级加成('所有',20,30,1)
                return
            if name == 'Lv1-50(所有)Lv+1':
                属性.技能等级加成('所有',1,50,1)
                return
        for i in 属性.技能栏:
            if name == i.名称+'Lv+1':
                i.等级加成(1)
                return
    
    def 基础属性(self, 属性):
        if 切装模式 == 1:
            属性.切装修正.clear()
            名称 = ['力量', '智力', '物攻', '魔攻', '独立', '属强']
            num = 0
            for i in self.切装修正属性:
                try:
                    if i.text() != '':
                        属性.切装修正.append(int(i.text()))
                    else:
                        属性.切装修正.append(0)
                except:
                    QMessageBox.information(self,"错误", 名称[num] + " 切装修正输入格式错误，已重置为空")
                    i.setText('')
                    属性.切装修正.append(0)
                num += 1

        for i in range(0,16):
            for j in range(0,17):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except:
                        QMessageBox.information(self,"错误", self.行名称[j + 17 if i > 6 else j] + "：" + self.列名称[i] + "  输入格式错误，已重置为空")
                        self.属性设置输入[i][j].setText('')

        temp = []
        for j in range(0,len(self.属性设置输入[16])):
            if self.属性设置输入[16][j].text() != '':
                try:
                    temp.append(float(self.属性设置输入[16][j].text())/100)
                    if temp[-1] > 1 or temp[-1] < -0.2:
                        QMessageBox.information(self,"错误", self.修正列表名称[j] + " 输入数值超出[-20,100]，已重置为空")
                        temp[-1] = 0.0
                        self.属性设置输入[16][j].setText('')
                except:
                    temp.append(0.0)
                    QMessageBox.information(self,"错误", self.修正列表名称[j] + " 输入格式错误，已重置为空")
                    self.属性设置输入[16][j].setText('')
            else:
                temp.append(0.0)

        属性.百分比力智加成(temp[0])
        属性.百分比三攻加成(temp[1])
        属性.伤害增加加成(temp[2])
        属性.附加伤害加成(temp[3])
        属性.属性附加加成(temp[4])
        属性.暴击伤害加成(temp[5])
        属性.最终伤害加成(temp[6])
        属性.技能攻击力加成(temp[7])

        for j in range(0,17):
            if self.属性设置输入[13][j].text() != '':
                属性.力量 += float(self.属性设置输入[13][j].text())
                属性.智力 += float(self.属性设置输入[13][j].text())
            if self.属性设置输入[14][j].text() != '':
                属性.物理攻击力 += float(self.属性设置输入[14][j].text())
                属性.魔法攻击力 += float(self.属性设置输入[14][j].text())
                属性.独立攻击力 += float(self.属性设置输入[14][j].text())

        for i in [0,7]:
            for j in range(0,17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 0 and j in [1,5,10,16]:
                        属性.进图力量+=float(self.属性设置输入[i][j].text())
                    else:
                        属性.力量+=float(self.属性设置输入[i][j].text())
        for i in [1,8]:
            for j in range(0,17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 1 and j in [1,5,10,16]:
                        属性.进图智力+=float(self.属性设置输入[i][j].text())
                    else:
                        属性.智力+=float(self.属性设置输入[i][j].text())

        for i in [2,9]:
            for j in range(0,17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 2 and j in [1,5,10,16]:
                        属性.进图物理攻击力+=float(self.属性设置输入[i][j].text())
                    else:
                        属性.物理攻击力+=float(self.属性设置输入[i][j].text())

        for i in [3,10]:
            for j in range(0,17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 3 and j in [1,5,10,16]:
                        属性.进图魔法攻击力+=float(self.属性设置输入[i][j].text())
                    else:
                        属性.魔法攻击力+=float(self.属性设置输入[i][j].text())

        for i in [4,11]:
            for j in range(0,17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 4 and j in [1,5,10,16]:
                        属性.进图独立攻击力+=float(self.属性设置输入[i][j].text())
                    else:
                        属性.独立攻击力+=float(self.属性设置输入[i][j].text())

        for i in [5,12]:
            for j in range(0,17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 5 and j in [1,5,10,16]:
                        属性.进图属强+=float(self.属性设置输入[i][j].text())
                    elif i == 5 and j == 3: #3为婚房不吃辟邪玉
                        属性.所有属性强化(float(self.属性设置输入[i][j].text()))
                    else:
                        属性.所有属性强化加成(float(self.属性设置输入[i][j].text()))
                        
        #禁用红色宠物装备白字输入
        sign = -1
        if self.红色宠物装备.isChecked():
            sign = 11

        for j in range(0,17):
            if j != sign:
                if self.属性设置输入[6][j].text() != '':
                    属性.附加伤害加成(float(self.属性设置输入[6][j].text())/100)
    
        for j in range(0,17):
            if self.属性设置输入[15][j].text() != '':
                属性.最终伤害加成(float(self.属性设置输入[15][j].text())/100)
        
        for i in self.技能设置输入:
            self.技能加成判断(i.currentText(), 属性)

    def 组合计算(self, index):
        套装组合=[]
        if index <= 1:
            for a in self.有效防具套装:
                for b in self.有效首饰套装:
                    for c in self.有效特殊套装:
                        # 533
                        套装组合.append([a, a, a, a, a, b, b, b, c, c, c])
            for a in self.有效防具套装:
                for d in self.有效上链左套装:
                    for e in self.有效镯下右套装:
                        for f in self.有效环鞋指套装:
                            # 3332
                            套装组合.append([d, a, e, a, f, e, d, f, f, d, e])
                            套装组合.append([a, a, e, a, f, e, d, f, f, d, e])
                            套装组合.append([d, a, a, a, f, e, d, f, f, d, e])
                            套装组合.append([d, a, e, a, a, e, d, f, f, d, e])
        if index == 1:
            for a in self.有效防具套装:
                for b in self.有效首饰套装:
                    for c in self.有效特殊套装:
                        for d in self.有效防具套装:
                            if d != a:
                                # 2333
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
        count = 0
        if self.百变怪选项.isChecked():
            初始sign2 = '空'
        else:
            初始sign2 = '无'
        if index != 2:
            for temp in 套装组合:
                for k in [-1, 0, 5, 8]:
                    temp1 = []
                    sign = 0
                    sign2 = 初始sign2
                    for x in range(0,11):
                        品质 = '-史诗-'
                        if k == x:
                            品质= '-神话-'
                        index = 套装映射[temp[x] + 品质 + 部位列表[x]]
                        if self.装备选择状态[index] == 1:
                            sign += 1
                        else:
                            if sign2 == '空' and 装备列表[index].品质 != '神话' and 装备列表[index].所属套装 not in ['精灵使的权能', '大自然的呼吸', '能量主宰']:
                                sign += 1
                    if sign == 11:
                        count += len(self.有效武器列表)  
        if index == 2:
            count = 1     
            for i in self.有效部位列表:
                count *= len(i)                       
        return count