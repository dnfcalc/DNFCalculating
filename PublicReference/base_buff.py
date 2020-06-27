import multiprocessing
import queue
import threading
import time
import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PublicReference import logger
from PublicReference.calc_core import CalcData
from PublicReference.common import format_time
from PublicReference.minheap import MinHeap, MinHeapWithQueue
from PublicReference.producer_consumer import producer, producer_data, 工作线程数, 每个工作线程应处理的任务数, 串行搜索的层数, 批量传回的结果数
from PublicReference.装备_buff import *
from PublicReference.装备函数 import *
from PublicReference.辟邪玉_buff import *
from PublicReference.称号_buff import *
from PublicReference.宠物_buff import *
from PublicReference.选项设置_buff import *
from PublicReference.copy import *


class 技能:
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    等级 = 0
    基础等级 = 0
    是否主动 = 0
    站街生效 = 0

    def 等级加成(self, x):
        if self.等级 != 0:
            self.等级 = max(min(self.等级上限, self.等级+x), 0)

    def 结算统计(self): 
        return [0, 0, 0, 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class 被动技能(技能):
    是否主动 = 0

class 主动技能(技能):
    是否主动 = 1
    适用数值 = 0

部位列表 = ["上衣", "头肩", "下装", "腰带", "鞋", "手镯", "项链", "戒指", "耳环", "辅助装备", "魔法石", "武器"]

防具智力 = 697
防具体力 = 215
防具精神 = 0
神话上衣额外智力 = 1
神话上衣额外体力 = 1
神话上衣额外精神 = 0

class MyQComboBox(QComboBox):
    def __init__(self,窗口):
        super().__init__(窗口)
        self.setView(QListView())
        self.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(65,105,225,0.8)} QComboBox QAbstractItemView::item {height: 18px;}")

复选框样式 = "QCheckBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QCheckBox:hover{background-color:rgba(65,105,225,0.8)}"
按钮样式 = 'QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:10px} QPushButton:hover{background-color:rgba(65,105,225,0.8)}'
标签样式 = "QLabel{font-size:12px;color:white}"

堆大小上限 = 100

class 角色属性():

    职业名称 = ''

    武器选项 = []
    
    系数类型选择 = []
    
    系数类型 = ''
    防具类型 = ''
    防具精通属性 = [] 

    C力智 = 5000
    C三攻 = 2800
    排行类型 = '物理百分比'

    称号触发 = False

    智力 = 0.0
    体力 = 0.0
    精神 = 0.0
    
    #不适用系统奶加成
    进图智力 = 0.0
    进图体力 = 0.0
    进图精神 = 0.0

    百分比体精 = 0.0

    守护恩赐体精 = 0
    守护恩赐Lv = 0
    守护徽章Lv = 0
    守护徽章per = 0
    圣光十字Lv = 0

    转职被动智力 = 0
    转职被动Lv = 0
    BUFF额外增幅率 = 0

    BUFFLv = 0
    BUFF力量per = 1
    BUFF智力per = 1
    BUFF物攻per = 1
    BUFF魔攻per = 1
    BUFF独立per = 1
    一觉Lv = 0
    一觉力智 = 0
    一觉力智per = 1

    BUFF力量 = 0
    BUFF智力 = 0
    BUFF物攻 = 0
    BUFF魔攻 = 0
    BUFF独立 = 0

    一觉被动Lv = 0
    一觉被动力智 = 0
    信念光环体精 = 0

    BUFF适用面板 = 0
    
    一觉序号 = 0
    双装备模式 = 0
    切换详情 = '无'

    技能栏 = []
    技能序号 = dict()

    装备栏 = []
    套装栏 = []
    武器类型 = ''

    是否增幅 = [0] * 12
    强化等级 = [0] * 12
    改造等级 = [0] * 12
    武器锻造等级 = 0

    护石第一栏 = '无'
    护石第二栏 = '无'

    次数输入 = []

    def 系数数值站街(self):
        if self.系数类型 == '智力':
            return self.智力
        elif self.系数类型 == '体力':
            return self.体力
        elif self.系数类型 == '精神':
            return self.精神

    def 系数数值进图(self):
        if self.系数类型 == '智力':
            return self.进图智力
        elif self.系数类型 == '体力':
            return self.进图体力
        elif self.系数类型 == '精神':
            return self.进图精神

    def 穿戴装备(self, 装备, 套装):
        self.装备栏 = 装备
        self.套装栏 = 套装
        self.武器类型 = 装备列表[装备序号[self.装备栏[11]]].类型

    def 装备基础(self):
        #奶妈奶萝
        if self.系数类型 == '智力':
            self.智力 += 防具智力
            if 装备列表[装备序号[self.装备栏[0]]].品质 == '神话':
                self.智力 += 神话上衣额外智力
        #奶爸体力
        elif self.系数类型 == '体力':
            self.体力 += 防具体力
            if 装备列表[装备序号[self.装备栏[0]]].品质 == '神话':
                self.体力 += 神话上衣额外体力
        #奶爸精神
        elif self.系数类型 == '精神':
            self.精神 += 防具精神
            if 装备列表[装备序号[self.装备栏[0]]].品质 == '神话':
                self.精神 += 神话上衣额外精神
        for i in [0,1,2,3,4]:
            if 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 精通体力(100,装备列表[装备序号[self.装备栏[i]]].品质,self.强化等级[i],部位列表[i])
            else:
                x = 精通体力(100,装备列表[装备序号[self.装备栏[i]]].品质,0,部位列表[i])
            if '智力' in self.防具精通属性:
                self.智力 += x * 2
            if '体力' in self.防具精通属性:
                self.体力 += x
            if '精神' in self.防具精通属性:
                self.精神 += x * 2

        for i in [9,10]:
            if 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 左右计算(100,'史诗',self.强化等级[i])
                self.智力 += x
                self.体力 += x
                self.精神 += x

        for i in range(0,12):
            if self.是否增幅[i] and 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 增幅计算(100,装备列表[装备序号[self.装备栏[i]]].品质,self.强化等级[i])
                if '智力' in self.系数类型:
                    self.智力 += x
                if '体力' in self.系数类型:
                    self.体力 += x
                if '精神' in self.系数类型:
                    self.精神 += x
        for i in [5,6,7,8,9,10,11]:
            self.智力 += 装备列表[装备序号[self.装备栏[i]]].智力
            self.体力 += 装备列表[装备序号[self.装备栏[i]]].体力
            self.精神 += 装备列表[装备序号[self.装备栏[i]]].精神
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

    def 技能等级加成(self, 加成类型, min, max, lv):
        lv = int(lv)
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max:
                if 加成类型 == '所有':
                    i.等级加成(lv)
                else:
                    if i.是否主动 == 1:
                        i.等级加成(lv)

    def 单技能等级加成(self, 名称, lv):
        for i in self.技能栏:
            if i.名称 == 名称:
                i.等级加成(lv)

    def 提升率计算(self, 总数据):
        力量合计 = 0
        智力合计 = 0
        物攻合计 = 0
        魔攻合计 = 0
        独立合计 = 0
        for i in 总数据:
            力量合计 += i[3]
            智力合计 += i[4]
            物攻合计 += i[5]
            魔攻合计 += i[6]
            独立合计 += i[7]

        x1 = (self.C力智 + (self.C力智 - 950) * 1.35 + 7664) * self.C三攻

        if self.排行类型 == '物理百分比':
            x2  = (self.C力智 + (self.C力智 - 950) * 1.35 + 7664 + 力量合计) * (self.C三攻 + 物攻合计)
        elif self.排行类型 == '魔法百分比':
            x2  = (self.C力智 + (self.C力智 - 950) * 1.35 + 7664 + 智力合计) * (self.C三攻 + 魔攻合计)
        elif self.排行类型 == '物理固伤':
            x2  = (self.C力智 + (self.C力智 - 950) * 1.35 + 7664 + 力量合计) * (self.C三攻 + 独立合计)
        elif self.排行类型 == '魔法固伤':
            x2  = (self.C力智 + (self.C力智 - 950) * 1.35 + 7664 + 智力合计) * (self.C三攻 + 独立合计) 

        return x2 / x1 * 100

    def 适用数值计算(self):
        self.专属词条计算()
        for i in range(len(self.技能栏)):
            if  self.次数输入[i] == '1':
                self.智力 += self.技能栏[i].结算统计()[0]
                self.体力 += self.技能栏[i].结算统计()[1]
                self.精神 += self.技能栏[i].结算统计()[2]

        self.进图智力 += self.智力
        self.进图体力 += self.体力
        self.进图精神 += self.精神

        self.进图体力 *= 1 + self.百分比体精
        self.进图精神 *= 1 + self.百分比体精

        if self.系数类型 == '智力':
            self.BUFF适用面板 += self.进图智力
            for i in self.技能栏:
                if i.是否主动 == 1:
                    if i.所在等级 == 30:
                        i.适用数值 = self.BUFF适用面板
                    else:
                        i.适用数值 = self.进图智力

        elif self.系数类型 == '体力':
            self.BUFF适用面板 += self.进图体力
            for i in self.技能栏:
                if i.是否主动 == 1:
                    if i.所在等级 == 30:
                        i.适用数值 = self.BUFF适用面板
                    else:
                        i.适用数值 = self.进图体力

        elif self.系数类型 == '精神':
            self.BUFF适用面板 += self.进图精神
            for i in self.技能栏:
                if i.是否主动 == 1:
                    if i.所在等级 == 30:
                        i.适用数值 = self.BUFF适用面板
                    else:
                        i.适用数值 = self.进图精神

    #返回可能的组合列表
    def 装备替换(self, 属性):
        套装栏 = []
        for i in 属性.套装栏:
            套装栏.append(i.split('[')[0])
        if len(套装栏) < 7:
            return [deepcopy(属性)]

        匹配1 = [防具套装, 上链左套装, 上链左套装, 镯下右套装, 镯下右套装, 环鞋指套装, 环鞋指套装]
        匹配0 = [防具套装, 上链左套装, 防具套装, 镯下右套装, 防具套装, 环鞋指套装, 防具套装]

        count = []

        for i in range(7):
            if 套装栏[i] in 匹配1[i]:
                count.append(1)
            elif 套装栏[i] in 匹配0[i]:
                count.append(0)
            else:
                count.append(-9)

        sumcount = sum(count)
        if sumcount < 6:
            return [deepcopy(属性)]
        elif sumcount == 7:
            x1 = deepcopy(属性)
            x2 = deepcopy(属性)
            x3 = deepcopy(属性)
            x4 = deepcopy(属性)
            num = 0
            index = [6, 5, 7]
            for i in [x2, x3, x4]:
                i.装备栏[num * 2] = 装备列表[套装映射[装备列表[装备序号[i.装备栏[1]]].所属套装 + '-' + '史诗' + '-' + 装备列表[装备序号[i.装备栏[num * 2]]].部位]].名称
                i.套装栏[2 * num + 2] = i.套装栏[2 * num + 2].replace(装备列表[装备序号[i.装备栏[index[num]]]].所属套装, 装备列表[装备序号[i.装备栏[1]]].所属套装)
                i.切换详情 = 装备列表[装备序号[i.装备栏[num * 2]]].部位 + '：' + x1.装备栏[num * 2] + ' → ' + i.装备栏[num * 2]
                num += 1
            return [x1, x2, x3, x4]
        elif sumcount == 6:
            index = count.index(0)
            部位 = {2:6, 4:5, 6:7}
            x1 = deepcopy(属性)
            x2 = deepcopy(属性)
            x2.装备栏[index - 2] = 装备列表[套装映射[装备列表[装备序号[x2.装备栏[部位[index]]]].所属套装 + '-' + '史诗' + '-' + 装备列表[装备序号[x2.装备栏[index - 2]]].部位]].名称
            x2.套装栏[index] = x2.套装栏[index].replace(装备列表[装备序号[x2.装备栏[1]]].所属套装, 装备列表[装备序号[x2.装备栏[部位[index]]]].所属套装)
            x2.切换详情 = 装备列表[装备序号[x2.装备栏[index - 2]]].部位 + '：' + x1.装备栏[index - 2] + ' → ' + x2.装备栏[index - 2]
            return [x1, x2]

    def 数据计算(self):        
        总数据 = []
        if self.双装备模式 == 1 and self.次数输入[self.一觉序号] == '1':
            #用于计算一觉
            temp = deepcopy(self)
            
            #计算现有装备BUFF
            self.装备属性计算()
            self.适用数值计算()
            for i in range(len(self.技能栏)):
                if  self.次数输入[i] == '1':
                    总数据.append(self.技能栏[i].结算统计())
                else:
                    总数据.append([0, 0, 0, 0, 0, 0, 0, 0])

            #拷贝数据，并修改装备，返回可能的组合
            数据列表 = []
            切换列表 = []
            for 一觉计算属性 in self.装备替换(temp):
                一觉计算属性.装备属性计算()
                一觉计算属性.适用数值计算()
                数据列表.append(一觉计算属性.技能栏[self.一觉序号].结算统计()[3]) #3是力量属性  一觉力智都是相等的
                切换列表.append(一觉计算属性.切换详情)
            
            #取一觉最大值，并修改数据
            a = max(数据列表)
            总数据[self.一觉序号] = [0, 0, 0, a, a, 0, 0, 0]
            self.切换详情 = 切换列表[数据列表.index(a)]
            
        else:
            self.装备属性计算()
            self.适用数值计算()
            for i in range(len(self.技能栏)):
                if  self.次数输入[i] == '1':
                    总数据.append(self.技能栏[i].结算统计())
                else:
                    总数据.append([0, 0, 0, 0, 0, 0, 0, 0])

        return 总数据


    def 结果返回(self, x, 总数据):
        if x==0:
            return self.提升率计算(总数据)
    
        if x==1:
            return 总数据

    def BUFF计算(self, x = 0):
        总数据 = self.数据计算()
        return self.结果返回(x, 总数据)

    def 装备属性计算(self):
        self.装备基础()
        for i in self.装备栏:
            装备列表[装备序号[i]].城镇属性(self)
            装备列表[装备序号[i]].进图属性(self)
            装备列表[装备序号[i]].BUFF属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].城镇属性(self)
            套装列表[套装序号[i]].进图属性(self)
            套装列表[套装序号[i]].BUFF属性(self)

    def 专属词条计算(self):
        pass

    def 站街计算(self):
        self.专属词条计算()
        for i in self.技能栏:
            if i.站街生效 == 1:
                self.智力 += i.结算统计()[0]
                self.体力 += i.结算统计()[1]
                self.精神 += i.结算统计()[2]

    def 护石计算(self, 护石选项):
        if 护石选项 == 'buff力智增加量+2%':
            self.BUFF力量per *= 1.02
            self.BUFF智力per *= 1.02
        elif 护石选项 == 'buff力智增加量+4%':
            self.BUFF力量per *= 1.04
            self.BUFF智力per *= 1.04
        elif 护石选项 == 'buff力智增加量+6%':
            self.BUFF力量per *= 1.06
            self.BUFF智力per *= 1.06

    def BUFF面板(self):
        for i in self.技能栏:
            try:
                return i.BUFF面板()
            except:
                pass

    def 一觉面板(self):
        for i in self.技能栏:
            try:
                return i.一觉面板()
            except:
                pass

class 角色窗口(QWidget):

    def __init__(self):
        super().__init__()
        self.护石选项 = ['无','buff力智增加量+2%', 'buff力智增加量+4%', 'buff力智增加量+6%']
        self.窗口属性输入()
        self.界面()

        #创建配置文件夹
        path = './ResourceFiles/'+self.角色属性A.职业名称 + '/set'
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

    def 窗口属性输入(self):
        pass
    
    def 界面(self):
        self.setWindowTitle(self.角色属性A.职业名称 + "搭配计算器")
        self.icon = QIcon('./ResourceFiles/'+self.角色属性A.职业名称 + '/技能/BUFF.png')
        self.setWindowIcon(self.icon)
        #窗口大小
        self.setFixedSize(1120, 680)

        背景颜色 = QLabel(self)
        背景颜色.resize(self.width(),self.height())
        背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1)}")

        主背景透明度 = QGraphicsOpacityEffect()
        主背景透明度.setOpacity(0.15)
        self.主背景图片 = QPixmap('./ResourceFiles/'+self.角色属性A.职业名称 + "/bg.jpg")
        主背景 = QLabel(self)
        主背景.setPixmap(self.主背景图片)
        主背景.setGraphicsEffect(主背景透明度)

        self.技能图片 = []
        for i in self.角色属性A.技能栏:
            path = './ResourceFiles/'+self.角色属性A.职业名称 + "/技能/" + i.名称 + ".png"
            self.技能图片.append(QPixmap(path))
        
        self.输出窗口列表 = []
        self.行高 = 30 #输出窗口技能伤害标签高度
        self.排行窗口列表 = []
        
        self.装备图片 = []
        self.遮罩透明度 = []
        self.装备图片按钮 = []
        for i in 装备列表:
            self.遮罩透明度.append(QGraphicsOpacityEffect())
            self.装备图片按钮.append('')
        self.装备选择状态 = []
        for i in 装备列表:
            path = './ResourceFiles/img/装备/' + str(装备序号[i.名称]) + '.gif'
            self.装备图片.append(QMovie(path))
            self.装备选择状态.append(0)
        self.输出背景图片 = QPixmap('./ResourceFiles/'+self.角色属性A.职业名称 + "/输出背景.png")
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

        self.页面名称 = ["装备/选择/打造", "技能/符文/其它", "基础/细节/修正","神话属性修正"]
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

        # 第一个布局界面
        self.main_frame1 = QMainWindow()
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
                                        self.按钮.setToolTip(装备列表[j].名称 + '\n'+ 装备列表[j].类型 + '-' + 装备列表[j].部位)
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
        self.按钮.move(650, 30 + counter5 * 32)
        self.按钮.resize(265,28)
        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
        self.按钮.clicked.connect(lambda state, index = '无': self.套装按钮点击事件(index))
        
        counter4 = 0
        counter5 += 1
        for i in 装备列表:
            if i.部位 == '武器' and i.类型 in self.角色属性A.武器选项:
                self.图片 = QLabel(self.main_frame1)
                self.图片.setMovie(self.装备图片[装备序号[i.名称]])
                self.装备图片[装备序号[i.名称]].start()
                self.图片.resize(28, 28)
                self.图片.move(657 + 55 * counter4, 30 + counter5 * 32)
                self.按钮 = QPushButton(self.main_frame1)
                self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.按钮.resize(28, 28)
                self.按钮.setToolTip(i.名称 + '\n' + i.类型) 
                self.遮罩透明度[装备序号[i.名称]].setOpacity(0.5)
                self.按钮.setGraphicsEffect(self.遮罩透明度[装备序号[i.名称]])
                self.按钮.clicked.connect(lambda state, index = 装备序号[i.名称]: self.装备图标点击事件(index, 10))
                self.装备图片按钮[装备序号[i.名称]] = self.按钮
                self.装备图片按钮[装备序号[i.名称]].move(657 + 55 * counter4, 30 + counter5 * 32)
                counter4 += 1
                if counter4 % 5 == 0:
                    counter5 += 1
                    counter4 = 0
        
        if counter4 != 0:
            counter5 += 1
        self.按钮 = QPushButton('智慧产物', self.main_frame1)
        self.按钮.move(650, 50 + counter5 * 32)
        self.按钮.resize(265,28)
        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
        self.按钮.clicked.connect(lambda state, index = '智慧产物': self.套装按钮点击事件(index))
        
        counter4 = 0
        counter5 += 1
        for i in 装备列表:
            if i.所属套装 == '智慧产物' and i.部位 != '武器':
                self.图片 = QLabel(self.main_frame1)
                self.图片.setMovie(self.装备图片[装备序号[i.名称]])
                self.装备图片[装备序号[i.名称]].start()
                self.图片.resize(28, 28)
                self.图片.move(657 + 55 * counter4, 50 + counter5 * 32)
                self.按钮 = QPushButton(self.main_frame1)
                self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.按钮.resize(28, 28)
                self.按钮.setToolTip(i.名称 + '\n' + i.类型+ '-' + i.部位) 
                self.遮罩透明度[装备序号[i.名称]].setOpacity(0.5)
                self.按钮.setGraphicsEffect(self.遮罩透明度[装备序号[i.名称]])
                self.按钮.clicked.connect(lambda state, index = 装备序号[i.名称]: self.装备图标点击事件(index, 10))
                self.装备图片按钮[装备序号[i.名称]] = self.按钮
                self.装备图片按钮[装备序号[i.名称]].move(657 + 55 * counter4, 50 + counter5 * 32)
                counter4 += 1
                if counter4 % 5 == 0:
                    counter5 += 1
                    counter4 = 0
        
        标签 = QLabel(self.main_frame1)
        标签.move(922, 15)
        标签.setPixmap(QPixmap('./ResourceFiles/'+self.角色属性A.职业名称 + "/职业.png"))
        标签.resize(191, 523)
   
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
            for j in range(0,21):
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
            for j in range(0,21):
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
        for j in range(0,9):
            x.addItem('锻造+' + str(j))
        x.resize(110,20)
        x.move(540 , 504 + (counter - 9) * 30)
        self.装备打造选项.append(x)

        x = MyQComboBox(self.main_frame1)
        x.addItems(self.角色属性A.系数类型选择)
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

        x = QPushButton('一键增幅10',self.main_frame1)
        x.clicked.connect(lambda state: self.批量打造())
        x.move(520 , 460)
        x.resize(105, 24)
        x.setStyleSheet(按钮样式)

        self.百变怪选项 = QCheckBox('百变怪   ', self.main_frame1)
        self.百变怪选项.move(660, 613)
        self.百变怪选项.resize(80, 24)
        self.百变怪选项.setToolTip('仅在极速模式和套装模式下生效')
        self.百变怪选项.setStyleSheet(复选框样式)

        self.计算模式选择 = MyQComboBox(self.main_frame1)
        self.计算模式选择.addItems(['计算模式：极速模式', '计算模式：套装模式', '计算模式：单件模式'])
        self.计算模式选择.move(750, 613)
        self.计算模式选择.resize(235, 24)
        self.计算模式选择.setStyleSheet("MyQComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} MyQComboBox:hover{background-color:rgba(65,105,225,0.8)}")
        self.计算模式选择.setToolTip('极速模式：533和3332(散搭) (不含智慧产物)\n\n套装模式：533、3332(散搭)和3233(双防具) (不含智慧产物)\n\n单件模式：所有组合 (不含百变怪)')
        
        self.切装模式选项 = QCheckBox('一觉切1件装备', self.main_frame1)
        self.切装模式选项.move(870, 580)
        self.切装模式选项.resize(110, 24)
        self.切装模式选项.setToolTip('仅对极速模式中的3332散搭组合生效\n\n默认相同打造')
        self.切装模式选项.setStyleSheet(复选框样式)

        self.神话排名选项 = QCheckBox('神话排名模式', self.main_frame1)
        self.神话排名选项.move(990, 580)
        self.神话排名选项.resize(100, 24)
        self.神话排名选项.setToolTip('仅显示有神话的组合，且每件神话装备只会出现一次')
        self.神话排名选项.setStyleSheet(复选框样式)
        
        self.最大使用线程数 = 工作线程数
        self.线程数选择 = MyQComboBox(self.main_frame1)
        self.线程数选择.move(660, 580)
        self.线程数选择.resize(80, 24)
        for i in range(工作线程数, 0, -1):
            self.线程数选择.addItem('进程:' + str(i))

        self.计算按钮1 = QPushButton('开始计算', self.main_frame1)
        self.计算按钮1.clicked.connect(lambda state: self.计算())
        self.计算按钮1.move(990, 610)
        self.计算按钮1.resize(100, 30)
        self.计算按钮1.setStyleSheet(按钮样式)

        # 第二个布局界面
        self.main_frame2 = QMainWindow()

        #技能等级、次数输入

        self.护石第一栏 = MyQComboBox(self.main_frame2)
        self.护石第二栏 = MyQComboBox(self.main_frame2)
 
        self.等级调整 = []
        self.次数输入 = []
        
        for i in self.角色属性A.技能栏:
            self.等级调整.append(MyQComboBox(self.main_frame2))
            self.次数输入.append(MyQComboBox(self.main_frame2))

        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.所在等级 == 50 or i.所在等级 == 85:
                for j in range(0, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
            else:
                for j in range(- i.基础等级, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
            for j in range(0, 2):
                self.次数输入[序号].addItem(str(j))
        
        横坐标=30
        纵坐标=0
        横坐标偏移量=60
        纵坐标偏移量=30
        词条框宽度=48
        行高 = 20
        
        counter=0
        for i in ['契约满级','等级调整','是否适用']:
            x=QLabel(i, self.main_frame2)
            x.move(横坐标+横坐标偏移量-30+50*counter,纵坐标)
            x.setStyleSheet(标签样式)
            counter+=1
        
        纵坐标+=20
        
        for i in self.角色属性A.技能栏:
            x=QLabel(self.main_frame2)
            x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
            x.resize(28,28)
            tempstr='<font color="#FF0000"><b>'+i.名称 +i.备注 +'</b></font><br>'
            tempstr+='所在等级：<b>'+str(i.所在等级)+'</b><br>'
            tempstr+='等级上限：<b>'+str(i.等级上限)+'</b>'
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
            self.次数输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
            self.次数输入[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标)
            纵坐标+=纵坐标偏移量

        self.护石第一栏.addItems(self.护石选项)
        self.护石第二栏.addItems(self.护石选项)

       
        横坐标=430;纵坐标=20;行高=18
        x=QLabel("护石(第一栏/上)：", self.main_frame2)
        x.move(横坐标,纵坐标-5)
        x.setStyleSheet(标签样式)
        纵坐标+=21
        self.护石第一栏.move(横坐标,纵坐标)
        self.护石第一栏.resize(130, 行高)
        
        横坐标=600;纵坐标=20
        x=QLabel("护石(第二栏/下)：", self.main_frame2)
        x.move(横坐标,纵坐标-5)
        x.setStyleSheet(标签样式)
        纵坐标+=21
        self.护石第二栏.move(横坐标,纵坐标)
        self.护石第二栏.resize(130, 行高)
        
        self.辟邪玉选择 = []
        self.辟邪玉数值 = []
        for i in range(4):
            x = MyQComboBox(self.main_frame2) 
            for j in 辟邪玉列表:
                #'[' + str(j.编号) + ']' + 
                x.addItem(j.名称)
            x.resize(200,20)
            x.move(430,80 + i * 25)
            x.currentIndexChanged.connect(lambda state, index = i:self.辟邪玉数值选项更新(index))
            self.辟邪玉选择.append(x)
            y = MyQComboBox(self.main_frame2) 
            y.resize(80,20)
            y.move(650,80 + i * 25)
            self.辟邪玉数值.append(y)

        self.复选框列表 = []
        for i in 选项设置列表:
            self.复选框列表.append(QCheckBox(i.名称, self.main_frame2))

        counter=0
        for i in self.复选框列表:
            i.setStyleSheet(复选框样式)
            i.resize(125,20)
            i.move(950,10 + counter * 28)
            if counter < 1:
                i.setChecked(True)
            counter+=1

        self.排行选项 = []
        for i in range(3):
            self.排行选项.append(MyQComboBox(self.main_frame2))

        for i in [3000,3500,4000,4500,5000,5500,6000,7000,8000,10000,12000,15000,20000]:
            self.排行选项[0].addItem('C力智:' + str(i))
        self.排行选项[0].setCurrentIndex(4)

        for i in [2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600,3700,3800,3900,4000,4200,4400,4600,4800,5000]:
            self.排行选项[1].addItem('C三攻:' + str(i))
        self.排行选项[1].setCurrentIndex(8)

        for i in ['物理百分比','魔法百分比','物理固伤','魔法固伤']:
            self.排行选项[2].addItem(i)
        
        counter=0
        for i in self.排行选项:
            i.resize(100,20)
            i.move(990,520 + counter * 28)
            counter+=1


        self.计算按钮2 = QPushButton('开始计算', self.main_frame2)
        self.计算按钮2.clicked.connect(lambda state: self.计算())
        self.计算按钮2.move(990, 610)
        self.计算按钮2.resize(100, 30)
        self.计算按钮2.setStyleSheet(按钮样式)

        # 第三个布局界面
        self.main_frame3 = QMainWindow()

        self.属性设置输入 = []
        self.技能设置输入 = []

        宽度 = 43

        列名称1 = ["智力", "体力", "精神"]
        行名称1 = ["工会属性", "训练官BUFF", "戒指", "婚房", "冒险团", "晶体契约", "收集箱", "勋章", "名称装饰卡", "快捷栏纹章", "宠物装备-红",
                "  宠物装备-蓝  ", "  宠物装备-绿  ", "宠物附魔","皮肤", "站街修正", "进图修正"]
        名称 = QLabel("基础细节", self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(
            "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
        名称.resize(80, 25)
        名称.move(10, 5)

        for i in range(0, 3):
            名称 = QLabel(列名称1[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(宽度, 25)
            名称.move(95 + i * (宽度 + 5), 5)

        for j in range(0, 17):
            名称 = QLabel(行名称1[j], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(80, 25)
            名称.move(10, 35 + j * 30)

        for i in range(0, 3):
            Linelist = []
            for j in range(0, 17):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet(
                    "QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(95 + i * (宽度 + 5), 35 + j * 30)
            self.属性设置输入.append(Linelist)

        列名称2 = ["智力", "体力", "精神","徽章智","徽章体","徽章精","技能等级"]
        行名称2 = ["上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "左槽", "右槽", "耳环", "武器", "登记补正","穿戴称号", "光环", "武器装扮", "时装"]

        self.列名称 = 列名称1 + 列名称2
        self.行名称 = 行名称1 + 行名称2

        名称 = QLabel(" 附魔&徽章 ", self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(
            "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
        名称.resize(80, 25)
        名称.move(7 * 宽度, 5)
        for i in range(0, 7):
            名称 = QLabel(列名称2[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            if i == 6:
                名称.resize(150, 25)
            else:
                名称.resize(宽度, 25)
            名称.move(90 + 7 * 宽度 + i * (宽度 + 5), 5)

        for j in range(0, 17):
            名称 = QLabel(行名称2[j], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(80, 25)
            名称.move(7 * 宽度, 35 + j * 30)

        for i in range(0, 6):
            Linelist = []
            for j in range(0, 17):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet(
                    "QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(90 + 7 * 宽度 + i * (宽度 + 5), 35 + j * 30)
            self.属性设置输入.append(Linelist)

        for j in range(0, 17):
            self.技能设置输入.append(MyQComboBox(self.main_frame3))
            self.技能设置输入[j].addItem('无')
            self.技能设置输入[j].setStyleSheet(
                "MyQComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            self.技能设置输入[j].resize(150, 22)
            self.技能设置输入[j].move(90 + 7 * 宽度 + 6 * (宽度 + 5), 35 + j * 30)

        for j in [2, 3, 4]:
            self.技能设置输入[j].addItems(['Lv1-30(主动)Lv+1', 'Lv1-50(主动)Lv+1'])

        for j in [8, 9, 16]:
            for i in self.角色属性A.技能栏:
                self.技能设置输入[j].addItem(i.名称 + 'Lv+1')
        self.技能设置输入[12].addItems(['BUFFLv+1', 'BUFFLv+2','BUFFLv+3','BUFFLv+4'])
        self.技能设置输入[13].addItems(['Lv1-50(主动)Lv+1', '一觉Lv+1', '一觉Lv+2'])
        self.技能设置输入[14].addItems(['Lv1-30(所有)Lv+1', 'Lv1-50(所有)Lv+1'])

        if '智力' in self.角色属性A.系数类型选择:
            self.修正列表名称 = ['转职被动智力', 'BUFF力智%', 'BUFF三攻%', '转职被动等级', '一觉被动力智', '一觉力智%', '一觉力智']
        else:
            self.修正列表名称 = ['守护恩赐体精', 'BUFF力智%', 'BUFF三攻%', '守护恩赐等级', '信念光环体精', '一觉力智%', '一觉力智']

        Linelist = []
        for i in range(0, len(self.修正列表名称)):
            名称 = QLabel(self.修正列表名称[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(90, 25)
            名称.move(170 + 7 * 宽度 + 9 * (宽度 + 5), 35 + i * 30)
            Linelist.append(QLineEdit(self.main_frame3))
            Linelist[i].setAlignment(Qt.AlignCenter)
            Linelist[i].setStyleSheet(
                "QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            Linelist[i].resize(60, 25)
            Linelist[i].move(270 + 7 * 宽度 + 9 * (宽度 + 5), 35 + i * 30)
        self.属性设置输入.append(Linelist)

        count = 0
        self.时装选项 = []
        for i in ['头部', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']:
            名称 = QLabel(i, self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(90, 25)
            名称.move(170 + 7 * 宽度 + 9 * (宽度 + 5), 255 + count * 30)
            self.时装选项.append(MyQComboBox(self.main_frame3))
            self.时装选项[count].addItems(['高级', '节日', '稀有', '神器'])
            self.时装选项[count].resize(60, 22)
            self.时装选项[count].move(270 + 7 * 宽度 + 9 * (宽度 + 5), 255 + count * 30)
            self.时装选项[count].currentIndexChanged.connect(lambda state, index=count: self.时装选项更新(index))
            count += 1

        self.时装选项.append(MyQComboBox(self.main_frame3))
        self.时装选项[8].addItems(['高级套装[8]', '节日套装[8]', '稀有套装[8]', '神器套装[8]'])
        self.时装选项[8].resize(160, 22)
        self.时装选项[8].move(170 + 7 * 宽度 + 9 * (宽度 + 5), 260 + count * 30)
        self.时装选项[8].currentIndexChanged.connect(lambda state, index=8: self.时装选项更新(index))

        self.计算按钮3 = QPushButton('开始计算', self.main_frame3)
        self.计算按钮3.clicked.connect(lambda state: self.计算())
        self.计算按钮3.move(990, 610)
        self.计算按钮3.resize(100, 30)
        self.计算按钮3.setStyleSheet(按钮样式)


        #第四个布局
        self.main_frame4 = QMainWindow()
        
        self.神话属性选项 = []
        self.神话属性图片 = []

        for j in range(len(装备列表)):
            if 装备列表[j].品质 == '神话':
                self.神话属性图片.append(QLabel(self.main_frame4))
                self.神话属性图片[-1].setMovie(self.装备图片[j])
                self.神话属性图片[-1].setToolTip(装备列表[j].名称 + '\n'+ 装备列表[j].类型 + '-' + 装备列表[j].部位)
                self.神话属性图片[-1].resize(28, 28)
                self.神话属性图片[-1].move(-1000, -1000)
                self.装备图片[j].start()

        for i in range(4 * 35):
            self.神话属性选项.append(MyQComboBox(self.main_frame4))
            self.神话属性选项[i].resize(150, 18)
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
                                if 范围列表[j][2] == 1 and 'Lv' not in 描述列表[j]:
                                    temp += '%'
                                self.神话属性选项[count * 4 + j].addItem(temp)
                    else:
                        self.神话属性选项[count * 4 + j].addItem('无')
                count += 1

        # 把布局界面放进去
        self.stacked_layout.addWidget(self.main_frame1)
        self.stacked_layout.addWidget(self.main_frame2)
        self.stacked_layout.addWidget(self.main_frame3)
        self.stacked_layout.addWidget(self.main_frame4)

    def 时装选项更新(self, index):
        if index == 8:
            count = 0
            for i in self.时装选项:
                if count != 8:
                    i.setCurrentIndex(self.时装选项[8].currentIndex())
                count += 1
            return
        else:
            智力, 体力, 精神 = 0, 0, 0
            套装字典 = {'高级':0, '节日':0, '稀有':0, '神器':0}
            for i in range(8):
                套装字典[self.时装选项[i].currentText()] = 套装字典.get(self.时装选项[i].currentText(), 0) + 1
            #套装属性
            神器 = 套装字典['神器']
            稀有 = 套装字典['稀有'] + 神器
            if 套装字典['高级'] >= 3:
                智力 += 10; 体力 += 10; 精神 += 10
            if 稀有 >= 3 and 神器 < 3:
                智力 += 40; 体力 += 40; 精神 += 40
            if 套装字典['神器'] >= 3:
                智力 += 50; 体力 += 50; 精神 += 50
            if 套装字典['高级'] >= 8:
                智力 += 10; 体力 += 10; 精神 += 10
            if 套装字典['节日'] >= 8:
                智力 += 25; 体力 += 25; 精神 += 25
            if 稀有 >= 8 and 神器 < 8:
                智力 += 40; 体力 += 40; 精神 += 40
            if 套装字典['神器'] >= 8:
                智力 += 50; 体力 += 50; 精神 += 50
            数据 = [45, 45, 55, 65]
            智力 += 数据[self.时装选项[0].currentIndex()] #头部
            精神 += 数据[self.时装选项[0].currentIndex()] #头部
            智力 += 数据[self.时装选项[1].currentIndex()] #帽子
            精神 += 数据[self.时装选项[1].currentIndex()] #帽子
            数据 = [0, 0, 55, 65]
            体力 += 数据[self.时装选项[5].currentIndex()]  # 腰带
            数据 = [45 ,45, 55, 65]
            体力 += 数据[self.时装选项[7].currentIndex()]  # 鞋子

            数据 = [0, 20, 0, 0]
            智力 += 数据[self.时装选项[6].currentIndex()]  # 下装
            体力 += 数据[self.时装选项[6].currentIndex()]  # 下装
            精神 += 数据[self.时装选项[6].currentIndex()]  # 下装

            self.属性设置输入[3][16].setText(str(智力))
            self.属性设置输入[4][16].setText(str(体力))
            self.属性设置输入[5][16].setText(str(精神))

    def 辟邪玉数值选项更新(self, index):
        self.辟邪玉数值[index].clear()
        x = self.辟邪玉选择[index].currentIndex()
        temp = 辟邪玉列表[x].最大值
        while temp >= 辟邪玉列表[x].最小值:
            if 辟邪玉列表[x].间隔 >= 1:
                self.辟邪玉数值[index].addItem(str(int(temp)))
            else:
                self.辟邪玉数值[index].addItem(str('%.1f' % temp) + '%')
            temp -= 辟邪玉列表[x].间隔

    def 辟邪玉属性计算(self, 属性):
        for i in range(4):
            x = self.辟邪玉选择[i].currentIndex()
            if self.辟邪玉数值[i].currentIndex() >= 0:
                辟邪玉列表[x].当前值 = float(self.辟邪玉数值[i].currentText().replace('%',''))
            辟邪玉列表[x].进图属性(属性)

    def 应用的辟邪玉列表(self):
        应用的辟邪玉列表 = []
        for i in range(4):
            x = self.辟邪玉选择[i].currentIndex()
            if self.辟邪玉数值[i].currentIndex() >= 0:
                辟邪玉列表[x].当前值 = float(self.辟邪玉数值[i].currentText().replace('%', ''))
            if 辟邪玉列表[x].当前值 != 0:
                应用的辟邪玉列表.append(辟邪玉列表[x])

        return 应用的辟邪玉列表

    def 装备图标点击事件(self, index, sign):
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
            counter = 1
            for i in self.有效部位列表:
                counter *= len(i)
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

    def 批量选择(self, index):
        for i in 装备列表:
            if i.部位 != '武器':
                self.装备图标点击事件(装备序号[i.名称], index)
            else:
                if i.类型 in self.角色属性A.武器选项:
                    self.装备图标点击事件(装备序号[i.名称], index)
    
    def 批量打造(self):
        for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
            self.装备打造选项[i].setCurrentIndex(1)
            self.装备打造选项[i + 12].setCurrentIndex(10)
        for i in range(24,36):
            self.装备打造选项[i].setCurrentIndex(5)
        self.装备打造选项[36].setCurrentIndex(8)

    def 载入配置(self, path = 'set'):
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/equ3.ini', 'r', encoding='utf-8').readlines()
            self.称号.setCurrentIndex(int(setfile[0].replace('\n', '')))
            self.宠物.setCurrentIndex(int(setfile[1].replace('\n', '')))
            self.计算模式选择.setCurrentIndex(int(setfile[2].replace('\n', '')))
            # 百变怪 && 神话排名 && 一觉切装备 && 时装选项
            if int(setfile[3].replace('\n', '')):
                self.百变怪选项.setChecked(True)
            if int(setfile[4].replace('\n', '')):
                self.神话排名选项.setChecked(True)
            if int(setfile[5].replace('\n', '')):
                self.切装模式选项.setChecked(True)
            for i in range(0,len(self.时装选项)):
                self.时装选项[i].setCurrentIndex(int(setfile[i + 6].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/attr.ini', 'r', encoding='utf-8').readlines()
            for i in range(0, 10):
                for j in range(0, len(self.属性设置输入[i])):
                    self.属性设置输入[i][j].setText(setfile[i].replace('\n', '').split(',')[j])
        
            for j in range(0, 17):
                self.技能设置输入[j].setCurrentIndex(int(setfile[10].replace('\n', '').split(',')[j]))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/equ.ini', 'r', encoding='utf-8').readlines()
            for i in range(0, len(装备列表)):
                if setfile[i].replace('\n', '') == '1':
                    self.装备图标点击事件(i, 1)
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/equ1.ini', 'r', encoding='utf-8').readlines()
            for i in range(0,len(self.装备打造选项)):
                self.装备打造选项[i].setCurrentIndex(int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/equ2.ini', 'r', encoding='utf-8').readlines()
            for i in range(0,len(self.装备条件选择)):
                self.装备条件选择[i].setCurrentIndex(int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/skill1.ini', 'r', encoding='utf-8').readlines()
            num = 0
            self.护石第一栏.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石第二栏.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/skill2.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in self.角色属性A.技能栏:
                序号 = self.角色属性A.技能序号[i.名称]
                self.等级调整[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.次数输入[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/skill3.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(4):
                self.辟邪玉选择[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.辟邪玉数值[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/equ4.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(4 * 35):
                self.神话属性选项[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

    def 保存配置(self):
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/equ3.ini', 'w', encoding='utf-8')
            setfile.write(str(self.称号.currentIndex())+'\n')
            setfile.write(str(self.宠物.currentIndex())+'\n')
            setfile.write(str(self.计算模式选择.currentIndex())+'\n')
            # 百变怪 && 神话排名 && 一觉切装备 && 时装选择
            setfile.write(str(int(self.百变怪选项.isChecked())) + '\n')
            setfile.write(str(int(self.神话排名选项.isChecked())) + '\n')
            setfile.write(str(int(self.切装模式选项.isChecked())) + '\n')
            for i in range(0, len(self.时装选项)):
                setfile.write(str(self.时装选项[i].currentIndex()) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/attr.ini', 'w', encoding='utf-8')
            for i in range(0, 10):
                for j in range(0, len(self.属性设置输入[i])):
                    setfile.write(self.属性设置输入[i][j].text()+',')
                setfile.write('\n')
            for j in range(0, 17):
                setfile.write(str(self.技能设置输入[j].currentIndex())+',')
            setfile.write('\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/equ.ini', 'w', encoding='utf-8')
            for i in range(0, len(装备列表)):
                setfile.write(str(self.装备选择状态[i])+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/equ1.ini', 'w', encoding='utf-8')
            for i in range(0,len(self.装备打造选项)):
                setfile.write(str(self.装备打造选项[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/equ2.ini', 'w', encoding='utf-8')
            for i in range(0,len(self.装备条件选择)):
                setfile.write(str(self.装备条件选择[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/skill1.ini', 'w', encoding='utf-8')
            setfile.write(str(self.护石第一栏.currentIndex())+'\n')
            setfile.write(str(self.护石第二栏.currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/skill2.ini', 'w', encoding='utf-8')
            for i in self.角色属性A.技能栏:
                序号 = self.角色属性A.技能序号[i.名称]
                setfile.write(str(self.等级调整[序号].currentIndex())+'\n')
                setfile.write(str(self.次数输入[序号].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/skill3.ini', 'w', encoding='utf-8')
            for i in range(4):
                setfile.write(str(self.辟邪玉选择[i].currentIndex())+'\n')
                setfile.write(str(self.辟邪玉数值[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/equ4.ini', 'w', encoding='utf-8')
            for i in range(4 * 35):
                setfile.write(str(self.神话属性选项[i].currentIndex())+'\n')
        except:
            pass

    def 神话属性选项颜色更新(self, index):
        i = self.神话属性选项[index]
        if i.currentIndex() != 0:
            i.setStyleSheet("MyQComboBox{font-size:12px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:5px;} MyQComboBox:hover{background-color:rgba(225,5,65,0.8)} MyQComboBox QAbstractItemView::item {height: 18px;}")
        else:
            i.setStyleSheet("MyQComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} MyQComboBox:hover{background-color:rgba(65,105,225,0.8)} MyQComboBox QAbstractItemView::item {height: 18px;}")

    def click_window(self, index):
        if self.stacked_layout.currentIndex() != index:
            self.stacked_layout.setCurrentIndex(index)
        for i in self.window_btn:
            i.setStyleSheet('QToolButton{font-size:13px;color:white;background-color:rgba(70,130,200,0.8)} QToolButton:hover{background-color:rgba(40,100,235,0.8)}')
        self.window_btn[index].setStyleSheet('QToolButton{font-size:13px;color:white;background-color:rgba(200,30,30,0.8)} QToolButton:hover{background-color:rgba(235,0,0,0.8)}')

        if index == 3:
            count1 = 0
            count2 = 0
            num = 0
            for j in range(len(装备列表)):
                if 装备列表[j].品质 == '神话':
                    if self.装备选择状态[j] == 1:
                        self.神话属性图片[num].move(int(self.width() / 7 * (count1 % 7+ 0.42)), int(self.height() / 5.2 * (count2 + 0.05)))
                        for i in range(4):
                            self.神话属性选项[num * 4 + i].move(int(self.width() / 7 * (count1 % 7) + 5), int(self.height() / 5.2 * (count2 + 0.05)) + i * 22 + 32)
                        count1 += 1
                        if count1 % 7 == 0:
                            count2 += 1
                    else:
                        self.神话属性图片[num].move(-1000,-1000)
                        for i in range(4):
                            self.神话属性选项[num * 4 + i].move(-1000,-1000)
                    num += 1

    def 计算(self):
        logger.info("开始计算")
        self.保存配置()
        self.角色属性A = deepcopy(self.初始属性)
        self.输入属性(self.角色属性A)

        self.最大使用线程数 = 工作线程数 - self.线程数选择.currentIndex()

        if self.组合计算(self.计算模式选择.currentIndex()) == 0:
            QMessageBox.information(self,"错误",  "无有效组合，请更换模式或重新选择装备") 
            return

        # -------------------------------------多线程计算流程开始-------------------------------------

        startTime = time.time()
        finished = False
        producer_data.calc_index += 1
        producer_data.produced_count = 0

        def log_result_queue_info(log_func, msg, mq: MinHeapWithQueue):
            log_func("calc#{}: {}: {} remaining_qize={}, processed_result={}, speed={:.2f}/s estimated_remaining_time={}, totalWork={}".format(
                producer_data.calc_index,
                mq.name, msg, mq.minheap_queue.qsize()*批量传回的结果数, mq.processed_result_count, mq.process_results_per_second(), format_time(mq.remaining_time()*批量传回的结果数),
                producer_data.produced_count,
            ))

        def try_fetch_result(mq: MinHeapWithQueue):
            while True:
                try:
                    heap_items = mq.minheap_queue.get(block=False)
                    for heap_item in heap_items:
                        mq.minheap.add(heap_item)
                        mq.processed_result_count += 1
                        if mq.processed_result_count % 批量传回的结果数 == 0:
                            log_result_queue_info(logger.info, "try_fetch_result periodly report", mq)
                except queue.Empty as error:
                    break

        def try_fetch_result_in_background(mq: MinHeapWithQueue):
            while not finished:
                log_result_queue_info(logger.info, "try_fetch_result_in_background", mq)
                try_fetch_result(mq)
                time.sleep(0.5)

        save_top_n = 堆大小上限
        if self.神话排名选项.isChecked():
            save_top_n = 2 << 64

        mq = MinHeapWithQueue("排行", MinHeap(save_top_n), multiprocessing.Manager().Queue())

        # 异步排行线程
        fetch_result_thread = threading.Thread(target=try_fetch_result_in_background, args=(mq,), daemon=True)
        fetch_result_thread.start()

        # 异步计算搭配
        mode_index = self.计算模式选择.currentIndex()
        total_task_count = self.组合计算(self.计算模式选择.currentIndex()) # 极速模式和套装模式时
        if mode_index == 2:
            # 散件模式时
            total_task_count = 1
            for i in range(串行搜索的层数):
                total_task_count *= len(self.有效部位列表[i])

        batch_task_count = min(每个工作线程应处理的任务数 * 工作线程数, total_task_count, self.最大使用线程数)

        start_index, end_index = 0, 0
        batch_size = total_task_count // batch_task_count
        reminder = total_task_count % batch_task_count
        for i in range(batch_task_count):
            end_index = start_index + batch_size - 1
            if i < reminder:
                end_index+=1

            calc_data = CalcData()

            calc_data.是输出职业 = False

            calc_data.minheap_queue = mq.minheap_queue
            calc_data.角色属性A = deepcopy(self.角色属性A)
            calc_data.角色属性A.强化等级 = copy(self.角色属性A.强化等级)
            calc_data.角色属性A.改造等级 = copy(self.角色属性A.改造等级)
            calc_data.角色属性A.是否增幅 = copy(self.角色属性A.是否增幅)
            calc_data.角色属性A.次数输入 = copy(self.角色属性A.次数输入)
            calc_data.应用的辟邪玉列表 = copy(self.应用的辟邪玉列表())

            calc_data.mode_index = mode_index
            calc_data.start_index = start_index
            calc_data.end_index = end_index

            calc_data.装备选择状态 = copy(self.装备选择状态)
            calc_data.拥有百变怪 = self.百变怪选项.isChecked()
            calc_data.神话属性选项 = [cb.currentIndex() for cb in self.神话属性选项]

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
                for j in [0, 5, 8]:
                    if 装备列表[装备序号[tempstr[j]]].品质 == '神话' and tempstr[j] not in 神话列表:
                        神话列表.append(tempstr[j])
                        self.排行数据.append(tempstr)
                if len(神话列表) >= 35:
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

        if len(self.排行数据) == 0:
            QMessageBox.information(self,"计算错误",  "无有效组合")
            return
        if len(self.排行数据) == 1:
            self.输出界面(0)
        else:
            self.排行界面()
            
    def 排行界面(self):
        self.排行窗口列表.clear()
        滚动排行 = QMainWindow()
        self.排行窗口列表.append(滚动排行)
        滚动排行.resize(620,530)
        滚动排行.setMinimumSize(620,530)
        滚动排行.setMaximumSize(620,1030)
        滚动排行.setWindowTitle('配装排行 （点击数字可查看详情）')  
        滚动排行.setWindowIcon(self.icon)  
    
        背景颜色=QLabel(滚动排行)
        背景颜色.resize(620,1030)
        背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1.0)}")
    
        排行背景透明度=QGraphicsOpacityEffect()
        排行背景透明度.setOpacity(0.15)
        排行背景=QLabel(滚动排行)
        排行背景.move(-600,0)
        排行背景.resize(1600,1080)
        排行背景.setPixmap(self.主背景图片)
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
    
        for i in range(0,len(self.排行数据)):
            图片列表 = []
            for j in range(0,12):
                图片列表.append(self.装备图片[装备序号[self.排行数据[i][j]]])
            水平间距=[1,2,3,4,5,6.5,7.5,8.5,10,11,12,13.5]
            for j in range(0,12):
                图标=QLabel(滚动排行.topFiller)
                图标.setMovie(图片列表[j])
                图片列表[j].start()
                图标.move(int(初始x+x间隔*水平间距[j]),int(初始y+i*y间隔))
                图标.setToolTip(self.排行数据[i][j])
                if self.排行数据[i][j] == self.排行数据[i][-1]:
                    图标=QLabel(滚动排行.topFiller)
                    图标.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                    图标.resize(28,28)
                    图标.move(int(初始x+x间隔*水平间距[j]),int(初始y+i*y间隔))
                    图标.setToolTip(self.排行数据[i][j])
                
            伤害量 = str(round(self.排行数据[i][12],1)) + '%'
            if 最高伤害!=0:
                百分比=str(round(self.排行数据[i][12]/最高伤害*100,1))+'%'
            else:
                百分比=' 0.0%'
    
            if 百分比=='100.0%':
                详情按钮=QtWidgets.QPushButton(伤害量+' |'+百分比,滚动排行.topFiller)
            else:
                详情按钮=QtWidgets.QPushButton(伤害量+' | '+百分比,滚动排行.topFiller)
    
            详情按钮.clicked.connect(lambda state, index= i: self.输出界面(index))
            详情按钮.setToolTip('点击查看详情')
            详情按钮.move(int(初始x+x间隔*15),int(初始y+i*y间隔))
            详情按钮.resize(120,30)
            详情按钮.setStyleSheet(按钮样式+"QPushButton{font-size:14px}")
    
        滚动排行.scroll = QScrollArea()
        滚动排行.scroll.setStyleSheet("QScrollArea {background-color:transparent}")
        滚动排行.scroll.viewport().setStyleSheet("background-color:transparent")
        滚动排行.scroll.setWidget(滚动排行.topFiller)
        滚动排行.vbox = QVBoxLayout()
        滚动排行.vbox.addWidget(滚动排行.scroll)
        wrapper.setLayout(滚动排行.vbox)
    
        滚动排行.show()

    def 站街计算(self,装备名称,套装名称):
        C = deepcopy(self.角色属性A)
        C.穿戴装备(装备名称,套装名称)
        for i in C.装备栏:
            装备列表[装备序号[i]].城镇属性(C)
            装备列表[装备序号[i]].BUFF属性(C)
        for i in C.套装栏:
            套装列表[套装序号[i]].城镇属性(C)
            套装列表[套装序号[i]].BUFF属性(C)
        C.装备基础()
        C.站街计算()
        return C

    def 输出界面(self, index):
        装备名称 = []
        套装名称 = []
        百变怪 = self.排行数据[index][-1]
        for i in range(0, 12):
            装备名称.append(self.排行数据[index][i])
        for i in range(13,len(self.排行数据[index])-1):
            套装名称.append(self.排行数据[index][i])

        C = self.站街计算(装备名称,套装名称)

        self.角色属性B = deepcopy(self.角色属性A)
        self.角色属性B.穿戴装备(装备名称,套装名称)
        #self.角色属性B.装备属性计算()
        self.辟邪玉属性计算(self.角色属性B)
        统计详情 = self.角色属性B.BUFF计算(1)

        #最大输出界面限制
        if len(self.输出窗口列表)>=10:
            del self.输出窗口列表[0]
    
        输出窗口 = QWidget()
        self.输出窗口列表.append(输出窗口)
        输出窗口.setFixedSize(788, 564)
        输出窗口.setWindowTitle('详细数据')
        输出窗口.setWindowIcon(self.icon)  
        QLabel(输出窗口).setPixmap(self.输出背景图片)
      
        适用中的套装=QLabel(装备名称[11],输出窗口)
        适用中的套装.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")   
        适用中的套装.move(132, 138+180)
        适用中的套装.resize(132,18)
        适用中的套装.setAlignment(Qt.AlignCenter)   
    
        神话所在套装 = '无'
        for i in range(0,11):
            if 装备列表[装备序号[装备名称[i]]].品质 == '神话':
                神话所在套装 = 装备列表[装备序号[装备名称[i]]].所属套装
        for i in range(0,len(套装名称)):
            适用套装名称=QLabel(输出窗口)
            适用套装名称.setText(套装名称[i])
            适用套装名称.move(132,158+180+i*20)
            适用套装名称.resize(132,18)
            适用套装名称.setAlignment(Qt.AlignCenter)  
            if 神话所在套装 == 套装名称[i].split('[')[0]:
                适用套装名称.setStyleSheet("QLabel{font-size:12px;color:rgb(224,146,151)}")   
            else:
                适用套装名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")  
        x = self.角色属性B.BUFF面板()
        y = self.角色属性B.一觉面板()
        面板显示=[]
        for i in range(0,11):
            面板显示.append(QLabel(输出窗口))     
        面板显示[0].setText('站街：' + str(int(C.系数数值站街())))
        面板显示[1].setText('适用：' + str(int(self.角色属性B.系数数值进图())))

        面板显示[2].setText(' ' + x[0])
        面板显示[3].setText('力量：' + str(x[1]))
        面板显示[4].setText('智力：' + str(x[2]))
        面板显示[5].setText('物攻：' + str(x[3]))
        面板显示[6].setText('魔攻：' + str(x[4]))
        面板显示[7].setText('独立：' + str(x[5]))

        面板显示[8].setText(' ' + y[0])
        面板显示[9].setText('力量：' + str(y[1]))
        面板显示[10].setText('智力：' + str(y[2]))

        const = 139
        面板显示[0].move(35,const)
        面板显示[1].move(165,const)
        
        const += 36
        count = 0
        for i in  [2,3,4,5,6,7]:
            面板显示[i].move(35,const + count * 18)
            count += 1

        count = 0
        for i in  [8,9,10]:
            面板显示[i].move(165,const + count * 18)
            count += 1

        for i in range(0,len(面板显示)):
            if i != 1:
                面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            else:
                面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(150,255,30)}")
            面板显示[i].resize(100,18)
            面板显示[i].setAlignment(Qt.AlignLeft)

        tempstr=[]
        tempstr.append('BUFF力量% ：'+str(int(round(self.角色属性B.BUFF力量per * 100, 0))) + '%') 
        tempstr.append('BUFF智力% ：'+str(int(round(self.角色属性B.BUFF智力per * 100, 0))) + '%') 
        tempstr.append('BUFF物攻% ：'+str(int(round(self.角色属性B.BUFF物攻per * 100, 0))) + '%')
        tempstr.append('BUFF魔攻% ：'+str(int(round(self.角色属性B.BUFF魔攻per * 100, 0))) + '%')
        tempstr.append('BUFF独立% ：'+str(int(round(self.角色属性B.BUFF独立per * 100, 0))) + '%')
        tempstr.append('一觉力智  ：'+str(int(round(self.角色属性B.一觉力智, 0))))
        tempstr.append('一觉力智% ：'+str(int(round(self.角色属性B.一觉力智per * 100, 0))) + '%')
        tempstr.append('守护徽章% ：'+str(int(round(self.角色属性B.守护徽章per * 100, 0))) + '%')
        tempstr.append('BUFF增幅率：'+str(int(round(self.角色属性B.BUFF额外增幅率 * 100,0))) + '%') 
    
        j=318
        for i in tempstr:
            templab=QLabel(输出窗口)
            templab.setText(i)
            templab.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            templab.move(20,j)
            templab.resize(305,18)
            templab.setAlignment(Qt.AlignLeft)
            j+=18
        
        合计力量 = 0
        合计智力 = 0
        合计物攻 = 0
        合计魔攻 = 0
        合计独立 = 0
        实际技能等级=[]
        for i in self.角色属性B.技能栏:
            实际技能等级.append(i.等级)

        count = 0
        for i in range(0,len(self.角色属性B.技能栏)):
            if sum(统计详情[i]) != 0:
                count += 1
      
        self.行高 = min(int(440 / count),30)        
        j = -1
        for i in range(0,len(self.角色属性B.技能栏)):
            if sum(统计详情[i]) != 0:
                合计力量 += 统计详情[i][3]
                合计智力 += 统计详情[i][4]
                合计物攻 += 统计详情[i][5]
                合计魔攻 += 统计详情[i][6]
                合计独立 += 统计详情[i][7]

                for k in range(len(统计详情[i])):
                    if 统计详情[i][k] == 0:
                        统计详情[i][k] = ''

                j += 1
                每行详情=[]
                for k in range(0,10):
                    每行详情.append(QLabel(输出窗口))
                #图片
                每行详情[0].setPixmap(self.技能图片[i])
                每行详情[0].move(302, 50 + j * self.行高)
                每行详情[0].resize(28,min(28,self.行高 - 2)) 
                #等级
                每行详情[1].setText('Lv.'+str(实际技能等级[i]))
                每行详情[1].move(337, 50 + j * self.行高)
                每行详情[1].resize(30,min(28,self.行高)) 
                #智力
                #if self.角色属性B.技能栏[i].是否主动 == 1:
                #    每行详情[2].setText(str(int(self.角色属性B.技能栏[i].适用数值)))
                #else:
                #    每行详情[2].setText(str(0))
                每行详情[2].setText(str(统计详情[i][0]))
                每行详情[2].move(370, 50 + j * self.行高)
                每行详情[2].resize(50,min(28,self.行高))
                #体力
                每行详情[3].setText(str(统计详情[i][1]))
                每行详情[3].move(410, 50 + j * self.行高)
                每行详情[3].resize(50,min(28,self.行高)) 
                #精神
                每行详情[4].setText(str(统计详情[i][2]))
                每行详情[4].move(450, 50 + j * self.行高)
                每行详情[4].resize(50,min(28,self.行高)) 
                #力量
                每行详情[5].setText(str(统计详情[i][3]))
                每行详情[5].move(490, 50 + j * self.行高) 
                每行详情[5].resize(50,min(28,self.行高)) 
                #智力
                每行详情[6].setText(str(统计详情[i][4]))
                每行详情[6].move(530, 50 + j * self.行高)
                每行详情[6].resize(50,min(28,self.行高))
                #物攻
                每行详情[7].setText(str(统计详情[i][5]))
                每行详情[7].move(570, 50 + j * self.行高)
                每行详情[7].resize(50,min(28,self.行高))
                #魔攻
                每行详情[8].setText(str(统计详情[i][6]))
                每行详情[8].move(610, 50 + j * self.行高)
                每行详情[8].resize(50,min(28,self.行高))
                #独立
                每行详情[9].setText(str(统计详情[i][7]))
                每行详情[9].move(650, 50 + j * self.行高)
                每行详情[9].resize(50,min(28,self.行高))
     
                for l in range(1,10):
                    每行详情[l].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
                    每行详情[l].setAlignment(Qt.AlignCenter) 

        tempstr = ''
        if 合计力量 == 合计智力:
            tempstr += '力智+' + str(合计力量)
        else:
            tempstr += '力量+' + str(合计力量)
            tempstr += '，智力+' + str(合计智力)

        if 合计物攻 == 合计魔攻 and 合计魔攻 == 合计独立:
            tempstr += '，三攻+' + str(合计物攻)
        else:
            tempstr += '，物攻+' + str(合计物攻)
            tempstr += '，魔攻+' + str(合计魔攻)
            tempstr += '，独立+' + str(合计独立)
        if self.角色属性B.切换详情 != '无':
            tempstr += '<br><br>' + self.角色属性B.切换详情 
        合计=QLabel(输出窗口)
        合计.setStyleSheet("QLabel{color:rgb(104,213,237);font-size:15px}")
        合计.setText(tempstr)
        合计.resize(450,72)
        合计.move(280, 90 + j * self.行高)
        合计.setAlignment(Qt.AlignCenter) 
    
        初始x=10;初始y=31
    
        图片列表 = []
    
        for i in range(0,12):
            图片列表.append(self.装备图片[装备序号[self.排行数据[index][i]]])
    
        偏移量=187
        x坐标=[32,0,0,32,0,偏移量,偏移量+32,偏移量+32,偏移量,偏移量,偏移量+32,32]
        y坐标=[0,0,32,32,64,0,0,32,64,32,64,64]
    
        tempstr=[]
        for i in range(0,12):
            tempstr.append('')
            装备 =  装备列表[装备序号[self.角色属性B.装备栏[i]]]
            if 装备.所属套装 != '智慧产物':  
                if self.角色属性B.强化等级[i]!=0:
                    if i==8:
                        tempstr[i]+='<font color="#00A2E8">+'+str(self.角色属性B.强化等级[i])+' 强化: '
                        tempstr[i]+='三攻 + '+str(耳环计算(100,装备.品质,self.角色属性B.强化等级[i]))+'</font>'
                    if i in [9,10]:
                        tempstr[i]+='<font color="#00A2E8">+'+str(self.角色属性B.强化等级[i])+' 强化: '
                        tempstr[i]+='四维 + '+str(左右计算(100,装备.品质,self.角色属性B.强化等级[i])) +'</font>'
                    if i==11:
                        tempstr[i]+='<font color="#00A2E8">+'+str(self.角色属性B.强化等级[i])+' 强化: '
                        tempstr[i]+='物理攻击力 + '+str(武器计算(100,装备.品质,self.角色属性B.强化等级[i],装备.类型,'物理'))+'</font><br>'
                        tempstr[i]+='<font color="#00A2E8">+'+str(self.角色属性B.强化等级[i])+' 强化: '
                        tempstr[i]+='魔法攻击力 + '+str(武器计算(100,装备.品质,self.角色属性B.强化等级[i],装备.类型,'魔法'))+'</font>'

                if self.角色属性B.武器锻造等级!=0:
                    if i==11:
                        tempstr[i]+='<br><font color="#00A2E8">+'+str(self.角色属性B.武器锻造等级)+'   锻造: '
                        tempstr[i]+='独立攻击力 + '+str(锻造计算(100,装备.品质,self.角色属性B.武器锻造等级))+'</font>'

                if self.角色属性B.是否增幅[i]==1:
                    if tempstr[i] !='':
                        tempstr[i]+='<br>'
                    tempstr[i]+='<font color="#FF00FF">+'+str(self.角色属性B.强化等级[i])+' 增幅: '
                    if '体力' in self.角色属性B.系数类型:
                        tempstr[i]+='异次元体力 + '+str(增幅计算(100,装备.品质,self.角色属性B.强化等级[i]))+'</font>'
                    elif '精神' in self.角色属性B.系数类型:
                        tempstr[i]+='异次元精神 + '+str(增幅计算(100,装备.品质,self.角色属性B.强化等级[i]))+'</font>'
                    elif '智力' in self.角色属性B.系数类型:
                        tempstr[i]+='异次元智力 + '+str(增幅计算(100,装备.品质,self.角色属性B.强化等级[i]))+'</font>'

        for i in range(0,12):
            装备图标=QLabel(输出窗口)
            装备图标.setMovie(图片列表[i])
            图片列表[i].start()
            装备图标.resize(26,26)
            装备图标.move(初始x+x坐标[i],初始y+y坐标[i])
            装备图标.setAlignment(Qt.AlignCenter) 

            if self.角色属性B.装备栏[i] == 百变怪:
                图标遮罩=QLabel(输出窗口)
                图标遮罩.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                图标遮罩.resize(26,26)
                图标遮罩.move(初始x+x坐标[i],初始y+y坐标[i])
                if tempstr[i]!='':
                    图标遮罩.setToolTip('<b>'+"{:<12}".format(self.角色属性B.装备栏[i])+'<br>'+tempstr[i]+'</b>')
                else:
                    图标遮罩.setToolTip('<b>'+"{:<12}".format(self.角色属性B.装备栏[i])+'</b>')
            else:
                if tempstr[i]!='':
                    装备图标.setToolTip('<b>'+"{:<12}".format(self.角色属性B.装备栏[i])+'<br>'+tempstr[i]+'</b>')
                else:
                    装备图标.setToolTip('<b>'+"{:<12}".format(self.角色属性B.装备栏[i])+'</b>')
           
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

    def 输入属性(self, 属性):
        for i in 属性.技能栏:
            i.等级 = i.基础等级+int(self.等级调整[self.角色属性A.技能序号[i.名称]].currentText())

        属性.C力智 = int(self.排行选项[0].currentText().split(':')[1])
        属性.C三攻 = int(self.排行选项[1].currentText().split(':')[1])
        属性.排行类型 = self.排行选项[2].currentText()

        if self.切装模式选项.isChecked() and self.计算模式选择.currentIndex() == 0:
            属性.双装备模式 = 1

        count = 0
        for i in 装备列表:
            if i.品质 == '神话':
                i.属性1选择 = self.神话属性选项[count * 4 + 0].currentIndex()
                i.属性2选择 = self.神话属性选项[count * 4 + 1].currentIndex()
                i.属性3选择 = self.神话属性选项[count * 4 + 2].currentIndex()
                i.属性4选择 = self.神话属性选项[count * 4 + 3].currentIndex()
                count += 1

        for i in range(len(self.复选框列表)):
            if self.复选框列表[i].isChecked():
                选项设置列表[i].适用效果(属性)

        称号列表[self.称号.currentIndex()].城镇属性(属性)
        if 属性.称号触发:
            称号列表[self.称号.currentIndex()].触发属性(属性)

        宠物列表[self.宠物.currentIndex()].城镇属性(属性)
        
        if self.护石第一栏.currentText()!= '无':
           属性.护石第一栏 = self.护石第一栏.currentText()

        if self.护石第二栏.currentText()!= '无':
           属性.护石第二栏 = self.护石第二栏.currentText()
    
        for i in range(0,12):
            属性.是否增幅[i] = self.装备打造选项[i].currentIndex()
            属性.强化等级[i] = self.装备打造选项[i + 12].currentIndex()
            属性.改造等级[i] = self.装备打造选项[i + 24].currentIndex()
        属性.武器锻造等级 = self.装备打造选项[36].currentIndex()
        属性.系数类型 = self.装备打造选项[37].currentText()
        属性.次数输入.clear()
        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            属性.次数输入.append(self.次数输入[序号].currentText())
      
        self.基础属性(属性)
    
    def 技能加成判断(self, name, 属性):
        if name == 'Lv1-30(主动)Lv+1':
            属性.技能等级加成('主动',1,30,1)
            return
        if name == 'Lv1-50(主动)Lv+1':
            属性.技能等级加成('主动',1,50,1)
            return
        if name == 'Lv1-30(所有)Lv+1':
            属性.技能等级加成('所有',1,30,1)
            return
        if name == 'Lv1-50(所有)Lv+1':
            属性.技能等级加成('所有',1,50,1)
            return
        if name == '一觉Lv+1':
            属性.一觉Lv += 1
            return
        if name == '一觉Lv+2':
            属性.一觉Lv += 2
            return
        if name == 'BUFFLv+1':
            属性.BUFFLv += 1
            return
        if name == 'BUFFLv+2':
            属性.BUFFLv += 2
            return
        if name == 'BUFFLv+3':
            属性.BUFFLv += 3
            return
        if name == 'BUFFLv+4':
            属性.BUFFLv += 4
            return
        for i in 属性.技能栏:
            if name == i.名称+'Lv+1':
                i.等级加成(1)
                return
    
    def 基础属性(self, 属性):
        for i in range(0, 3):
            for j in range(0, 16):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except:
                        QMessageBox.information(self, "错误",
                                                self.行名称[j + 17 if i > 2 else j] + "：" + self.列名称[i] + "  输入格式错误，已重置为空")
                        self.属性设置输入[i][j].setText('')
        for i in range(3, 9):
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except:
                        QMessageBox.information(self, "错误",
                                                self.行名称[j + 17 if i > 2 else j] + "：" + self.列名称[i] + "  输入格式错误，已重置为空")
                        self.属性设置输入[i][j].setText('')

        temp = []
        for j in range(0, len(self.属性设置输入[9])):

            if self.属性设置输入[9][j].text() != '' and j in [1,2,5]:
                try:
                    temp.append(float(self.属性设置输入[9][j].text()) / 100)

                    if temp[-1] > 1 or temp[-1] < -.2:
                        QMessageBox.information(self, "错误", self.修正列表名称[j] + " 输入数值超出[-20,100]，已重置为空")
                        temp[-1] = 0.0
                        self.属性设置输入[9][j].setText('')
                except:
                    temp.append(0.0)
                    QMessageBox.information(self, "错误", self.修正列表名称[j] + " 输入格式错误，已重置为空")
                    self.属性设置输入[9][j].setText('')
            elif self.属性设置输入[9][j].text() != '' and j in [0,3,4,6]:
                try:
                    temp.append(int(self.属性设置输入[9][j].text()))
                except:
                    temp.append(0.0)
                    QMessageBox.information(self, "错误", self.修正列表名称[j] + " 输入格式错误，已重置为空")
                    self.属性设置输入[9][j].setText('')
            else:
                temp.append(0.0)
        #神话补正
        if 属性.系数类型 == '智力':
            属性.转职被动智力 += int(temp[0])
            属性.BUFF力量per *= 1 + temp[1]
            属性.BUFF智力per *= 1 + temp[1]
            属性.BUFF物攻per *= 1 + temp[2]
            属性.BUFF魔攻per *= 1 + temp[2]
            属性.BUFF独立per *= 1 + temp[2]
            属性.转职被动Lv += int(temp[3])
            属性.一觉被动力智 += int(temp[4])
            属性.一觉力智per *= 1 + temp[5]
            属性.一觉力智 += int(temp[6])
        else:
            属性.守护恩赐体精 += int(temp[0])
            属性.BUFF力量per *= 1 + temp[1]
            属性.BUFF智力per *= 1 + temp[1]
            属性.BUFF物攻per *= 1 + temp[2]
            属性.BUFF魔攻per *= 1 + temp[2]
            属性.BUFF独立per *= 1 + temp[2]
            属性.守护恩赐Lv += int(temp[3])
            属性.信念光环体精 += int(temp[4])
            属性.一觉力智per *= 1 + temp[5]
            属性.一觉力智 += int(temp[6])

        for i in [0, 3, 6]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 3 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 0 and j in [1, 9, 16]:
                        属性.进图智力 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.智力 += int(self.属性设置输入[i][j].text())
        for i in [1, 4, 7]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 4 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 1 and j in [1, 9, 16]:
                        属性.进图体力 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.体力 += int(self.属性设置输入[i][j].text())
        for i in [2, 5, 8]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 5 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 2 and j in [1, 9, 16]:
                        属性.进图精神 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.精神 += int(self.属性设置输入[i][j].text())

        for i in self.技能设置输入:
            self.技能加成判断(i.currentText(), 属性)

        属性.护石计算(属性.护石第一栏)
        属性.护石计算(属性.护石第二栏)

    def 组合计算(self, index):
        self.有效穿戴组合.clear()
        self.有效穿戴套装.clear()
        self.百变怪列表.clear()
        套装组合=[]
        套装适用=[]
        if index <= 1:
            for a in self.有效防具套装:
                for b in self.有效首饰套装:
                    for c in self.有效特殊套装:
                        # 533
                        套装组合.append([a, a, a, a, a, b, b, b, c, c, c]); 套装适用.append([a + '[2]', a + '[3]', a + '[5]', b + '[2]', b + '[3]', c + '[2]', c + '[3]'])
    
            for a in self.有效防具套装:
                for d in self.有效上链左套装:
                    for e in self.有效镯下右套装:
                        for f in self.有效环鞋指套装:
                            # 3332
                            套装组合.append([d, a, e, a, f, e, d, f, f, d, e]); 套装适用.append([a + '[2]', d + '[2]', d + '[3]', e + '[2]', e + '[3]', f + '[2]', f + '[3]'])
                            套装组合.append([a, a, e, a, f, e, d, f, f, d, e]); 套装适用.append([a + '[2]', d + '[2]', a + '[3]', e + '[2]', e + '[3]', f + '[2]', f + '[3]'])
                            套装组合.append([d, a, a, a, f, e, d, f, f, d, e]); 套装适用.append([a + '[2]', d + '[2]', d + '[3]', e + '[2]', a + '[3]', f + '[2]', f + '[3]'])
                            套装组合.append([d, a, e, a, a, e, d, f, f, d, e]); 套装适用.append([a + '[2]', d + '[2]', d + '[3]', e + '[2]', e + '[3]', f + '[2]', a + '[3]'])
    
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
                                for x in range(0,10):
                                    套装适用.append([a + '[2]', a + '[3]', d + '[2]', b + '[2]', b + '[3]', c + '[2]', c + '[3]'])
        
        count = 0
        if index != 2:
            # 极速模式与套装模式
            for temp in 套装组合:
                for k in [-1, 0, 5, 8]:
                    temp1 = []
                    sign = 0
                    if self.百变怪选项.isChecked():
                        sign2 = '空'
                    else:
                        sign2 = '无'
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
                                sign2 = 装备列表[index].名称
                        temp1.append(装备列表[index].名称)
                    if sign == 11:
                        count += len(self.有效武器列表)                         
        if index == 2:
            count = 1     
            for i in self.有效部位列表:
                count *= len(i)                       
        return count
