from PublicReference.装备 import *
from PublicReference.装备函数 import *
from PublicReference.辟邪玉 import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import copy
import heapq
import ctypes

class 技能:
    名称 = ''
    所在等级 = 0
    等级上限 = 0
    等级 = 0
    基础等级 = 0

    def 等级加成(self, x):
        if self.等级 != 0:
            self.等级 = max(min(self.等级上限, self.等级+x), 0)

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
    # Will添加
    CD倍率 = 1.0
    TP成长 = 0.0
    TP上限 = 0
    TP等级 = 0
    是否主动 = 1
    是否有伤害 = 1
    恢复 = 1.0
    倍率 = 1.0
    被动倍率 = 1.0
    基础释放次数 = 0
    是否有护石 = 0
    关联技能 = ['无']
    关联技能2 = ['无']
    关联技能3 = ['无']
    # Will添加
    冷却关联技能 = ['无']
    冷却关联技能2 = ['无']
    冷却关联技能3 = ['无']


    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)
    def 等效CD(self, 武器类型):
        # Will修改
        return round(self.CD * self.CD倍率 / self.恢复, 1)

class 被动技能(技能):
    是否主动 = 0
    是否有伤害 = 0
    关联技能 = ['所有']
    # Will添加
    关联技能2 = ['无']
    关联技能3 = ['无']

    冷却关联技能 = ['无']
    冷却关联技能2 = ['无']
    冷却关联技能3 = ['无']

符文效果选项 = ['无', '攻击+5%,CD+3%', 'CD-4%', '攻击+3%', '攻击-3%,CD-6%', '攻击+3%,CD+2%', 'CD-3%', '攻击+2%', '攻击-2%,CD-4%']

部位列表 = ["上衣", "头肩", "下装", "腰带", "鞋", "手镯", "项链", "戒指", "耳环", "辅助装备", "魔法石", "武器"]

防具力量 = {'布甲':500, '皮甲':697,'轻甲':732,'重甲':715,'板甲':697}
防具智力 = {'布甲':732, '皮甲':697,'轻甲':655,'重甲':655,'板甲':697}
神话上衣额外力量 = {'布甲':0, '皮甲':1,'轻甲':2,'重甲':1,'板甲':1}
神话上衣额外智力 = {'布甲':2, '皮甲':1,'轻甲':1,'重甲':1,'板甲':1}

下拉框样式 = "QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px} QComboBox:hover{background-color:rgba(65,105,225,0.8)}"
复选框样式 = "QCheckBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QCheckBox:hover{background-color:rgba(65,105,225,0.8)}"
按钮样式 = 'QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:10px} QPushButton:hover{background-color:rgba(65,105,225,0.8)}'
标签样式 = "QLabel{font-size:12px;color:white}"

堆大小上限 = 100
最大组合数计算上限 = 301440

class 角色属性():

    职业名称 = ''

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

    #基础属性(含唤醒)
    基础力量 = 0.0
    基础智力 = 0.0
    
    #适用系统奶加成
    力量 = 0.0
    智力 = 0.0
    
    #不适用系统奶加成
    进图力量 = 0.0
    进图智力 = 0.0
    进图物理攻击力 = 0
    进图魔法攻击力 = 0
    进图独立攻击力 = 0
    进图属强 = 0

    #人物基础 + 唤醒 + 防具精通
    物理攻击力 = 0.0
    魔法攻击力 = 0.0
    独立攻击力 = 0.0
    火属性强化 = 0
    冰属性强化 = 0
    光属性强化 = 0
    暗属性强化 = 0
    百分比力智 = 0.0
    百分比三攻 = 0.0
    伤害增加 = 0.0
    附加伤害 = 0.0
    属性附加 = 0.0
    暴击伤害 = 0.0
    最终伤害 = 0.0
    技能攻击力 = 1.0
    持续伤害 = 0.0
    加算冷却缩减 = 0.0

    攻击速度 = 0.00
    移动速度 = 0.00
    释放速度 = 0.00
    命中率 = 0.0
    回避率 = 0.0
    物理暴击率 = 0.00
    魔法暴击率 = 0.00

    技能栏 = []
    技能序号 = dict()

    装备栏 = []
    套装栏 = []
    武器类型 = ''

    是否增幅 = [0] * 12
    强化等级 = [0] * 12
    改造等级 = [0] * 12
    武器锻造等级 = 0

    时间输入 = 0
    次数输入 = []
    宠物次数 = []
    
    #0英雄 1传说
    角色熟练度 = 0
    #0 1 2 3 4 5 6
    技能栏空位 = 0
    #0数学期望 1黄字+35% 2爆伤+35% 3白字+35% 4终伤+35% 5三攻+35%
    命运的抉择 = 0
    #0数学期望 123456
    天命无常 = 0
    #0数学期望 1 HP高于70% 2 HP在70~30% 3 HP低于30%
    悲剧的残骸 = 0
    #0数学期望 1 5%属性附加 2 10%技能攻击力 3 15%技能攻击力
    先知者的预言 = 0
    #0无霸体状态 1 霸体状态 2 无伤状态 
    贫瘠沙漠的遗产 = 0
    #0数学期望 1 7效果 2 77效果 3 777效果
    幸运三角 = 0
    #0过充电状态 1过负荷状态
    擎天战甲 = 0
    #0 100%  1 90%  2 80%  3 70%  4 60%  5 50%  6 40%  7 30%  8 20%  9 10%  10 0%
    持续伤害计算比例 = 0
    #0 120+ 1 120-100 2 100-80 3 80-60 4 60-40 5 40-
    军神的隐秘遗产 = 0
    #0太极天帝剑：阳  1太极天帝剑：阴  
    太极天帝剑 = 0
    #0绿色生命的面容：无  1绿色生命的面容：阴暗面
    绿色生命的面容 = 0

    护石第一栏 = '无'
    护石第二栏 = '无'

    def 穿戴装备(self, 装备, 套装):
        self.装备栏 = 装备
        self.套装栏 = 套装
        self.武器类型 = 装备列表[装备序号[self.装备栏[11]]].类型

    def 装备基础(self):
        self.力量 += 防具力量[self.防具类型]
        self.智力 += 防具智力[self.防具类型]
        if 装备列表[装备序号[self.装备栏[0]]].品质 == '神话':
            self.力量 += 神话上衣额外力量[self.防具类型]
            self.智力 += 神话上衣额外智力[self.防具类型]

        for i in [0,1,2,3,4]:
            if 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 精通计算(100,装备列表[装备序号[self.装备栏[i]]].品质,self.强化等级[i],部位列表[i])
            else:
                x = 精通计算(100,装备列表[装备序号[self.装备栏[i]]].品质,0,部位列表[i])
            if '力量' in self.防具精通属性:
                self.力量 += x
            if '智力' in self.防具精通属性:
                self.智力 += x
  

        for i in [9,10]:
            if 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 左右计算(100,'史诗',self.强化等级[i])
                self.力量 += x
                self.智力 += x

        for i in range(0,12):
            if self.是否增幅[i] and 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 增幅计算(100,装备列表[装备序号[self.装备栏[i]]].品质,self.强化等级[i])
                if '物理' in self.伤害类型:
                    self.力量 += x
                if '魔法' in self.伤害类型:
                    self.智力 += x

        if 装备列表[装备序号[self.装备栏[11]]].所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(100,'史诗',self.强化等级[11],self.武器类型,'物理')
            self.魔法攻击力 += 武器计算(100,'史诗',self.强化等级[11],self.武器类型,'魔法')
            self.独立攻击力 += 锻造计算(100,'史诗',self.武器锻造等级)
        
        if 装备列表[装备序号[self.装备栏[8]]].所属套装 != '智慧产物':
            x = 耳环计算(100,装备列表[装备序号[self.装备栏[8]]].品质,self.强化等级[8])
            self.物理攻击力 += x
            self.魔法攻击力 += x
            self.独立攻击力 += x

        for i in [5,6,7,8,9,10,11]:
            self.力量 += 装备列表[装备序号[self.装备栏[i]]].力量
            self.智力 += 装备列表[装备序号[self.装备栏[i]]].智力
            self.物理攻击力 += 装备列表[装备序号[self.装备栏[i]]].物理攻击力
            self.魔法攻击力 += 装备列表[装备序号[self.装备栏[i]]].魔法攻击力
            self.独立攻击力 += 装备列表[装备序号[self.装备栏[i]]].独立攻击力

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

    def 技能等级加成(self, 加成类型, min, max, lv):
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max:
                if 加成类型 == '所有':
                    i.等级加成(lv)
                else:
                    if i.是否主动 == 1:
                        i.等级加成(lv)
        if (min <= 20 and max >= 20) and 加成类型 == '所有':
            self.物理暴击率 += lv * 0.01

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
                    i.倍率 *= (1 + x)

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

    def 面板物理攻击力(self):
        面板物理攻击 = (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻) * (1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        for i in self.技能栏:
            try : 
                面板物理攻击 *= i.物理攻击力倍率(self.武器类型)
            except : 
                pass
        return round(面板物理攻击,3) * (self.面板力量() / 250 + 1) 

    def 面板魔法攻击力(self):
        面板魔法攻击 = (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻) * (1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        for i in self.技能栏:
            try : 
                面板魔法攻击 *= i.魔法攻击力倍率(self.武器类型)
            except : 
                pass
        return round(面板魔法攻击,3) * (self.面板智力() / 250 + 1) 

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
        return round(面板独立攻击,3)

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
                            j.CD倍率 *= i.CD缩减倍率(self.武器类型)
                else:
                    for k in i.冷却关联技能:
                        self.技能栏[self.技能序号[k]].CD倍率 *= i.CD缩减倍率(self.武器类型)
            if i.冷却关联技能2 !=['无']:
                if i.冷却关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD倍率 *= i.CD缩减倍率2(self.武器类型)
                else:
                    for k in i.冷却关联技能2:
                        self.技能栏[self.技能序号[k]].CD倍率2 *= i.CD缩减倍率2(self.武器类型)
            if i.冷却关联技能3 !=['无']:
                if i.冷却关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD倍率 *= i.CD缩减倍率3(self.武器类型)
                else:
                    for k in i.冷却关联技能3:
                        self.技能栏[self.技能序号[k]].CD倍率 *= i.CD缩减倍率3(self.武器类型)

    def 被动倍率计算(self):
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

    def 伤害指数计算(self):
        基准倍率 = 1.5 * self.主BUFF * (1 - 443215 / (443215 + 20000))

        if self.伤害类型 == '物理百分比':
            面板 = (self.面板力量()/250+1) * (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻)
        if self.伤害类型 == '魔法百分比':
            面板 = (self.面板智力()/250+1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻)
        if self.伤害类型 == '物理固伤':
            面板 = (self.面板力量()/250+1) * (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻)
        if self.伤害类型 == '魔法固伤':
            面板 = (self.面板智力()/250+1) * (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻)

        属性倍率=1.05+0.0045*max(self.火属性强化,self.冰属性强化,self.光属性强化,self.暗属性强化)
        增伤倍率=1+self.伤害增加
        增伤倍率*=1+self.暴击伤害
        增伤倍率*=1+self.最终伤害
        增伤倍率*=self.技能攻击力
        增伤倍率*=1+self.持续伤害*(1-0.1*self.持续伤害计算比例)
        增伤倍率*=1+self.附加伤害+self.属性附加*属性倍率
        self.伤害指数=面板*属性倍率*增伤倍率*基准倍率/100

    def 伤害计算(self, x = 0):
        
        self.所有属性强化(self.进图属强)
        # Will添加
        self.CD倍率计算()
        self.加算冷却计算()

        self.被动倍率计算()
        self.伤害指数计算()

        技能释放次数=[]
        技能单次伤害=[]
        技能总伤害=[]
    
        #技能单次伤害计算
        for i in self.技能栏:
            if i.是否主动==1:
                技能单次伤害.append(i.等效百分比(self.武器类型)*self.伤害指数*i.被动倍率)
            else:
                技能单次伤害.append(0)
      
        #技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                if self.次数输入[self.技能序号[i.名称]] =='/CD':
                    技能释放次数.append(int(self.时间输入/i.等效CD(self.武器类型) + 1 +i.基础释放次数))
                else:
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]])+i.基础释放次数)
            else:
                技能释放次数.append(0)
    
        #单技能伤害合计
    
        for i in self.技能栏:
            if i.是否主动==1 and 技能释放次数[self.技能序号[i.名称]] != 0:
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

    def 站街物理攻击力(self):
        站街物理攻击 = self.物理攻击力
        for i in self.技能栏:
            try : 
                站街物理攻击 *= i.物理攻击力倍率(self.武器类型)
            except : 
                pass
        return round(站街物理攻击, 3) * (self.站街力量() / 250 + 1)

    def 站街魔法攻击力(self):
        站街魔法攻击 =  self.魔法攻击力
        for i in self.技能栏:
            try : 
                站街魔法攻击 *= i.魔法攻击力倍率(self.武器类型)
            except : 
                pass
        return round(站街魔法攻击,3) * (self.站街智力() / 250 + 1)

    def 站街独立攻击力(self):
        站街独立攻击 = self.独立攻击力
        for i in self.技能栏:
            try : 
                站街独立攻击 *= i.独立攻击力倍率(self.武器类型)
            except : 
                pass
        return round(站街独立攻击, 3)
    
    def 装备属性计算(self):
        self.装备基础()

        for i in self.装备栏:
            装备列表[装备序号[i]].城镇属性(self)
            装备列表[装备序号[i]].进图属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].城镇属性(self)
            套装列表[套装序号[i]].进图属性(self)

class 角色窗口(QWidget):
    
    def __init__(self):
        super().__init__()
        self.窗口属性输入()
        self.界面()
        self.载入配置()

    def 关闭窗口(self):
        self.close()
        self.排行窗口列表.clear()

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
        主背景透明度.setOpacity(0.25)
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
        self.装备条件选择 = []
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

        self.页面名称 = ["装备选择", "其它设置", "基础属性"]
        self.页面数量 = len(self.页面名称)
        self.btn_group = QButtonGroup(self.frame_tool)
        for i in range(0, self.页面数量):
            self.window_btn = QToolButton(self.frame_tool)
            self.window_btn.setText(self.页面名称[i])
            self.window_btn.resize(int(self.width() / self.页面数量), 24)
            self.window_btn.move(self.window_btn.width() * i, 0)
            self.window_btn.setStyleSheet('QToolButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);} QToolButton:hover{background-color:rgba(65,105,225,0.8)}')
            self.window_btn.clicked.connect(lambda state, index = i: self.click_window(index))
            self.btn_group.addButton(self.window_btn, i)

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
                            for j in range(0,len(装备列表)):
                                if 装备列表[j].所属套装 == i.名称 and 装备列表[j].品质 == 品质:
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
        
        标签 = QLabel('装备条件设置', self.main_frame1)
        标签.move(940, 5)
        标签.resize(170,20)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        self.装备条件选择.clear()
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['角色熟练度：英雄', '角色熟练度：传说'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['技能栏空位：0', '技能栏空位：1', '技能栏空位：2', '技能栏空位：3', '技能栏空位：4', '技能栏空位：5', '技能栏空位：6'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['命运的抉择：数学期望', '命运的抉择：黄字+35%', '命运的抉择：爆伤+35%', '命运的抉择：白字+35%', '命运的抉择：终伤+35%', '命运的抉择：三攻+35%'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['骰子：数学期望', '骰子：1点', '骰子：2点', '骰子：3点', '骰子：4点', '骰子：5点', '骰子：6点'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['悲剧的残骸：数学期望', '悲剧的残骸：HP高于70%', '悲剧的残骸：HP70-30%', '悲剧的残骸：HP低于30%'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['先知者预言：数学期望', '先知者预言：属白+5%', '先知者预言：技攻+10%', '先知者预言：技攻+15%'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['贫瘠沙漠的遗产：无', '贫瘠沙漠的遗产：霸体', '贫瘠沙漠的遗产：无伤'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['幸运三角：数学期望', '幸运三角：7效果', '幸运三角：77效果', '幸运三角：777效果'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['擎天战甲：过充电状态', '擎天战甲：过负荷状态'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['持续伤害适用：100%', '持续伤害适用：90%', '持续伤害适用：80%', '持续伤害适用：70%', '持续伤害适用：60%', '持续伤害适用：50%', '持续伤害适用：40%', '持续伤害适用：30%', '持续伤害适用：20%', '持续伤害适用：10%', '持续伤害适用：0%'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['军神的隐秘遗产：120%以上', '军神的隐秘遗产：120-100%', '军神的隐秘遗产：100-80%', '军神的隐秘遗产：80-60%', '军神的隐秘遗产：60-40%', '军神的隐秘遗产：40%以下'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['太极天帝剑：阳', '太极天帝剑：阴'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['绿色生命的面容：无', '绿色生命的面容：阴暗面'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['希洛克融合：无','希洛克：奈克斯(伤害增幅)', '希洛克：暗杀者(冷却缩减)', '希洛克：卢克西(觉醒增幅)', '希洛克：罗德斯(霸体抗性)', '希洛克：守门将(45属强)', '希洛克：守门将(90属强)', '希洛克：守门将(135属强)'])
        for i in range(0, len(self.装备条件选择)):
            self.装备条件选择[i].resize(170, 20)
            self.装备条件选择[i].setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QComboBox:hover{background-color:rgba(65,105,225,0.8)}")
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
            x = QComboBox(self.main_frame1)
            x.addItems(['强化','增幅'])
            x.resize(55,20)
            x.setStyleSheet(下拉框样式)
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
            x = QComboBox(self.main_frame1)
            for j in range(0,21):
                x.addItem(str(j))
            x.resize(50,20)
            x.setStyleSheet(下拉框样式)
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
            x = QComboBox(self.main_frame1)
            for j in range(0,21):
                x.addItem('改造+' + str(j))
            x.resize(75,20)
            x.setStyleSheet(下拉框样式)
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

        x = QComboBox(self.main_frame1)
        for j in range(0,9):
            x.addItem('锻造+' + str(j))
        x.resize(110,20)
        x.move(540 , 504 + (counter - 9) * 30)
        x.setStyleSheet(下拉框样式)
        self.装备打造选项.append(x)

        x = QComboBox(self.main_frame1)
        x.addItems(self.角色属性A.伤害类型选择)
        x.resize(110,20)
        x.move(540 , 504 + (counter - 8) * 30)
        x.setStyleSheet(下拉框样式)
        self.装备打造选项.append(x)

        self.称号 = QComboBox(self.main_frame1)
        self.称号.addItems(['(2020)伟大的意志', '(2019)神选之英杰', '(2020)使徒降临', '(2019)超越极限者', '(2018)神之试炼', '(2015)哥特绮梦'])
        
        self.宠物 = QComboBox(self.main_frame1)
        self.宠物.addItems(['(2020)至尊', '(2019)至尊·进化', '(2020)普通', '(2019)普通'])

        x = QLabel('称号&宠物选择：', self.main_frame1)
        x.resize(130,20)
        x.move(360 , 400)
        x.setAlignment(Qt.AlignCenter)
        x.setStyleSheet(标签样式)
        
        counter = 0
        for x in [self.称号, self.宠物]:
            x.resize(130,20)
            x.move(360 , 430 + counter * 30)
            x.setStyleSheet(下拉框样式)  
            counter += 1    

        x = QPushButton('一键全选', self.main_frame1)
        x.clicked.connect(lambda state, index = 1: self.批量选择(index))
        x.move(505 , 400)
        x.resize(115, 24)
        x.setStyleSheet(按钮样式)

        x = QPushButton('一键清空',self.main_frame1)
        x.clicked.connect(lambda state, index = 0: self.批量选择(index))
        x.move(505 , 430)
        x.resize(115, 24)
        x.setStyleSheet(按钮样式)

        x = QPushButton('一键10/12/8/5',self.main_frame1)
        x.clicked.connect(lambda state: self.批量打造())
        x.move(505 , 460)
        x.resize(115, 24)
        x.setStyleSheet(按钮样式)

        self.百变怪选项 = QCheckBox('百变怪   ', self.main_frame1)
        self.百变怪选项.move(660, 613)
        self.百变怪选项.resize(80, 24)
        self.百变怪选项.setToolTip('仅在极速模式和套装模式下生效')
        self.百变怪选项.setStyleSheet(复选框样式)

        self.计算模式选择 = QComboBox(self.main_frame1)
        self.计算模式选择.addItems(['计算模式：极速模式', '计算模式：套装模式', '计算模式：单件模式'])
        self.计算模式选择.move(750, 613)
        self.计算模式选择.resize(235, 24)
        self.计算模式选择.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QComboBox:hover{background-color:rgba(65,105,225,0.8)}")
        self.计算模式选择.setToolTip('极速模式：533和3332(散搭) (不含智慧产物)\n\n套装模式：533、3332(散搭)和3233(双防具) (不含智慧产物)\n\n单件模式：所有组合 (不含百变怪)')

        self.神话排名选项 = QCheckBox('神话排名模式', self.main_frame1)
        self.神话排名选项.move(880, 580)
        self.神话排名选项.resize(100, 24)
        self.神话排名选项.setToolTip('仅显示有神话的组合，且每件神话装备只会出现一次')
        self.神话排名选项.setStyleSheet(复选框样式)

        self.显示选项 = QCheckBox('亿为单位显示', self.main_frame1)
        self.显示选项.move(990, 580)
        self.显示选项.resize(100, 24)
        self.显示选项.setStyleSheet(复选框样式)

        self.计算按钮1 = QPushButton('开始计算', self.main_frame1)
        self.计算按钮1.clicked.connect(lambda state: self.计算())
        self.计算按钮1.move(990, 610)
        self.计算按钮1.resize(100, 30)
        self.计算按钮1.setStyleSheet(按钮样式)

        # 第二个布局界面
        self.main_frame2 = QMainWindow()

        #技能等级、TP、次数输入、宠物次数
        self.BUFF输入 = QLineEdit(self.main_frame2)
        self.时间输入 = QComboBox(self.main_frame2)
        self.护石第一栏 = QComboBox(self.main_frame2)
        self.护石第二栏 = QComboBox(self.main_frame2)
        self.符文 = []
        self.符文效果 = []

        self.觉醒选择状态 = 2
        
        self.等级调整 = []
        self.TP输入 = []
        self.次数输入 = []
        self.宠物次数 = []
        
        for i in self.角色属性A.技能栏:
            i.等级 = i.基础等级
            self.等级调整.append(QComboBox(self.main_frame2))
            if i.是否有伤害 == 1 and i.TP上限 != 0:
                self.TP输入.append(QComboBox(self.main_frame2))
            else:
                self.TP输入.append('')
            if i.是否有伤害 == 1:
                self.次数输入.append(QComboBox(self.main_frame2))
                self.宠物次数.append(QComboBox(self.main_frame2))
            else:
                self.次数输入.append('')
                self.宠物次数.append('')
        
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
                tempstr='<font color="#FF0000"><b>'+i.名称+'</b></font><br>'
                tempstr+='所在等级：<b>'+str(i.所在等级)+'</b><br>'
                tempstr+='等级上限：<b>'+str(i.等级上限)+'</b>'
                if i.是否主动==1:
                    tempstr+='<br>百分比：<b>'+str(int(i.等效百分比(self.角色属性A.武器类型)))+'%</b>'
                    if i.TP上限 !=0:
                        tempstr+='<br>TP成长：<b>'+str(int(i.TP成长*100))+'%</b>'
                        tempstr+='<br>TP上限：<b>'+str(i.TP上限)+'</b>'
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
                self.等级调整[self.角色属性A.技能序号[i.名称]].setStyleSheet(下拉框样式)
                横坐标-=80
                纵坐标+=纵坐标偏移量
        
        横坐标=横坐标+80+50
        纵坐标=30
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                if i.是否主动==1:
                    if i.TP上限!=0:
                        self.TP输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                        self.TP输入[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标)
                        self.TP输入[self.角色属性A.技能序号[i.名称]].setStyleSheet(下拉框样式)
                纵坐标+=纵坐标偏移量
        
        横坐标=横坐标+50
        纵坐标=30
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                if i.是否主动==1:
                    self.次数输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                    self.次数输入[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标)
                    self.次数输入[self.角色属性A.技能序号[i.名称]].setStyleSheet(下拉框样式)
                    self.宠物次数[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                    self.宠物次数[self.角色属性A.技能序号[i.名称]].move(横坐标+50,纵坐标)
                    self.宠物次数[self.角色属性A.技能序号[i.名称]].setStyleSheet(下拉框样式)
                纵坐标+=纵坐标偏移量

        横坐标=横坐标+120
        纵坐标=20
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 0:
                x=QLabel(self.main_frame2)
                x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
                x.resize(28,28)
                tempstr='<font color="#FF0000"><b>'+i.名称+'</b></font><br>'
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
                self.等级调整[self.角色属性A.技能序号[i.名称]].setStyleSheet(下拉框样式)
                横坐标-=80
                纵坐标+=纵坐标偏移量
        
        x=横坐标+20;y=纵坐标+60
        self.觉醒选择=QLabel(self.main_frame2)
        self.觉醒选择.setPixmap(QPixmap('./ResourceFiles/'+self.角色属性A.职业名称 + "/技能/觉醒选择.png"))
        self.觉醒选择.resize(120,100)
        self.觉醒选择.move(x,y-20)
        
        self.BUFF=QLabel(self.main_frame2)
        self.BUFF.setPixmap(QPixmap('./ResourceFiles/'+self.角色属性A.职业名称 + "/技能/BUFF.png"))
        self.BUFF.resize(28,28)
        self.BUFF.move(x-2,y-40)
        self.BUFF.setToolTip( '最高值参考：' + str('%.1f' % ((self.角色属性A.主BUFF - 1) * 100)))
        
        self.BUFF输入.setText(str((self.角色属性A.主BUFF - 1) * 100))
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

        self.护石第一栏.addItems(self.护石选项)
        self.护石第二栏.addItems(self.护石选项)

        for i in range(0,6):
            self.符文.append(QComboBox(self.main_frame2))
            self.符文[i].addItems(self.符文选项)
            self.符文效果.append(QComboBox(self.main_frame2))
            self.符文效果[i].addItems(符文效果选项)
        
        横坐标=480;纵坐标=20;行高=18
        x=QLabel("护石(第一栏/上)：", self.main_frame2)
        x.move(横坐标,纵坐标-5)
        x.setStyleSheet(标签样式)
        纵坐标+=21
        self.护石第一栏.move(横坐标,纵坐标)
        self.护石第一栏.resize(130, 行高)
        self.护石第一栏.setStyleSheet(下拉框样式)
        纵坐标+=25
        for i in range(0,3):
            tempstr='符文'+str(i+1)+'选择: '
            x=QLabel(tempstr, self.main_frame2)
            x.move(横坐标,纵坐标-5)
            x.setStyleSheet(标签样式)
            纵坐标+=21
            self.符文[i].move(横坐标,纵坐标)
            self.符文[i].resize(130, 行高)
            self.符文[i].setStyleSheet(下拉框样式)
            纵坐标+=21
            self.符文效果[i].move(横坐标,纵坐标)
            self.符文效果[i].resize(130,行高)
            self.符文效果[i].setStyleSheet(下拉框样式)
            纵坐标+=25
        
        横坐标=650;纵坐标=20
        x=QLabel("护石(第二栏/下)：", self.main_frame2)
        x.move(横坐标,纵坐标-5)
        x.setStyleSheet(标签样式)
        纵坐标+=21
        self.护石第二栏.move(横坐标,纵坐标)
        self.护石第二栏.resize(130, 行高)
        self.护石第二栏.setStyleSheet(下拉框样式)
        纵坐标+=25
        for i in range(3,6):
            tempstr='符文'+str(i+1)+'选择: '
            x=QLabel(tempstr, self.main_frame2)
            x.move(横坐标,纵坐标-5)
            x.setStyleSheet(标签样式)
            纵坐标+=21
            self.符文[i].move(横坐标,纵坐标)
            self.符文[i].resize(130, 行高)
            self.符文[i].setStyleSheet(下拉框样式)
            纵坐标+=21
            self.符文效果[i].move(横坐标,纵坐标)
            self.符文效果[i].resize(130,行高)
            self.符文效果[i].setStyleSheet(下拉框样式)
            纵坐标+=25

        self.辟邪玉选择 = []
        self.辟邪玉数值 = []
        for i in range(4):
            x = QComboBox(self.main_frame2) 
            for j in 辟邪玉列表:
                x.addItem('[' + str(j.编号) + ']' + j.名称)
            x.resize(200,20)
            x.setStyleSheet(下拉框样式)
            x.move(480,300 + i * 25)
            x.currentIndexChanged.connect(lambda state, index = i:self.辟邪玉数值选项更新(index))
            self.辟邪玉选择.append(x)
            y = QComboBox(self.main_frame2) 
            y.resize(80,20)
            y.setStyleSheet(下拉框样式)
            y.move(700,300 + i * 25)
            self.辟邪玉数值.append(y)


        self.复选框列表 = []
        self.复选框列表.append(QCheckBox('顶级力量灵药     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('顶级智力灵药     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('斗神之吼秘药     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('赛丽亚的特调酷饮 ', self.main_frame2))
        self.复选框列表.append(QCheckBox('魔界战力释放秘药 ', self.main_frame2))
        self.复选框列表.append(QCheckBox('宠物次数适用(10%)', self.main_frame2))
        self.复选框列表.append(QCheckBox('称号效果触发     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('精神刺激灵药     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('虚祖皇家能量秘药 ', self.main_frame2))
        self.复选框列表.append(QCheckBox('黄金羊毛         ', self.main_frame2))
        self.复选框列表.append(QCheckBox('白兔子(20%全程)  ', self.main_frame2))
        self.复选框列表.append(QCheckBox('雷米迪亚蛋糕     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('系统奶BUFF      ', self.main_frame2))

        counter=0
        for i in self.复选框列表:
            i.setStyleSheet(复选框样式)
            i.resize(125,20)
            i.move(970,10 + counter * 28)
            if counter < 7 and counter > 1:
                i.setChecked(True)
            counter+=1
        if '物理' in self.角色属性A.伤害类型:
            self.复选框列表[0].setChecked(True)
        if '魔法' in self.角色属性A.伤害类型:
            self.复选框列表[1].setChecked(True)

        x=QLabel("时间输入：", self.main_frame2)
        x.move(850, 618)
        x.resize(70, 20)
        x.setStyleSheet(标签样式)
        self.时间输入.addItems(['1', '10', '15', '20', '25', '30', '60'])
        self.时间输入.move(920, 617)
        self.时间输入.resize(50, 20)
        self.时间输入.setStyleSheet(下拉框样式)

        self.计算按钮2 = QPushButton('开始计算', self.main_frame2)
        self.计算按钮2.clicked.connect(lambda state: self.计算())
        self.计算按钮2.move(990, 610)
        self.计算按钮2.resize(100, 30)
        self.计算按钮2.setStyleSheet(按钮样式)

        # 第三个布局界面
        self.main_frame3 = QMainWindow()

        名称列表 = ["上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "耳环", "辅助装备", "魔法石", "武器", "称号", "宠物", "宠物装备","光环", "武器装扮", "皮肤", "时装", "勋章", "快捷栏装备"]
        
        self.属性设置输入 = []
        self.技能设置输入 = []

        宽度 = 43
        
        列名称1 = ["力量", "智力", "物攻", "魔攻", "独立", "属强", "白字"]
        行名称1 = ["工会属性", "训练官BUFF", "戒指", "婚房", "冒险团", "晶体契约", "收集箱", "勋章", "名称装饰卡", "副武器/盾牌", "快捷栏纹章", "  宠物装备-红  ", "  宠物装备-蓝  ", "  宠物装备-绿  ", "宠物附魔", "站街修正", "进图修正"]
        名称 = QLabel("基础细节",self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
        名称.resize(80, 25)
        名称.move(10,5)
       
        for i in range(0, 7):
            名称 = QLabel(列名称1[i],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(宽度, 25)
            名称.move(95 + i*(宽度 + 5), 5)
    
        for j in range(0, 17):
            名称 = QLabel(行名称1[j],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(80, 25)
            名称.move(10, 35 + j*30)
    
        for i in range(0, 7):
            Linelist = []
            for j in range(0, 17):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(95 + i*(宽度 + 5), 35 + j*30)
            self.属性设置输入.append(Linelist)
    
        列名称2 = ["力量", "智力", "物攻", "魔攻", "独立", "属强", "徽章力", "徽章智", "终伤", "技能"]
        行名称2 = ["上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "左槽", "右槽", "耳环", "武器", "称号", "光环", "武器装扮", "皮肤", "时装"]

        self.列名称 = 列名称1 + 列名称2
        self.行名称 = 行名称1 + 行名称2

        名称 = QLabel(" 附魔&徽章 ",self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
        名称.resize(80, 25)
        名称.move(140+7*宽度,5)
        for i in range(0, 10):
            名称 = QLabel(列名称2[i],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            if i == 9:
                名称.resize(150, 25)
            else:
                名称.resize(宽度, 25)
            名称.move(225+7*宽度 + i*(宽度 + 5), 5)
    
        for j in range(0, 17):
            名称 = QLabel(行名称2[j],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(80, 25)
            名称.move(140+7*宽度, 35 + j*30)
    
        for i in range(0, 9):
            Linelist = []
            for j in range(0, 17):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(225+7*宽度 + i*(宽度 + 5), 35 + j*30)
            self.属性设置输入.append(Linelist)
    
        for j in range(0, 17):
            self.技能设置输入.append(QComboBox(self.main_frame3))
            self.技能设置输入[j].addItem('无')
            self.技能设置输入[j].setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            self.技能设置输入[j].resize(150, 22)
            self.技能设置输入[j].move(225+7*宽度 + 9*(宽度 + 5), 35 + j*30)
    
        for j in [2, 3, 4]:
            self.技能设置输入[j].addItems(['Lv1-30(主动)Lv+1', 'Lv1-50(主动)Lv+1'])
    
        for j in [8, 9, 16]:
            for i in self.角色属性A.技能栏:
                self.技能设置输入[j].addItem(i.名称+'Lv+1')
        self.技能设置输入[12].addItem('Lv1-50(主动)Lv+1')
        self.技能设置输入[13].addItems(['Lv1-30(所有)Lv+1', 'Lv1-50(所有)Lv+1'])

        self.修正列表名称 = ['力智%', '三攻%', '黄字', '白字', '属白', '爆伤', '终伤', '技攻']
        
        Linelist = []
        for i in range(0, len(self.修正列表名称)):
            名称 = QLabel(self.修正列表名称[i],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(60, 25)
            名称.move(250 + i*65, 570)
            Linelist.append(QLineEdit(self.main_frame3))
            Linelist[i].setAlignment(Qt.AlignCenter)
            Linelist[i].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            Linelist[i].resize(60, 22)
            Linelist[i].move(250 + i*65, 610)
        self.属性设置输入.append(Linelist)

        self.计算按钮3 = QPushButton('开始计算', self.main_frame3)
        self.计算按钮3.clicked.connect(lambda state: self.计算())
        self.计算按钮3.move(990, 610)
        self.计算按钮3.resize(100, 30)
        self.计算按钮3.setStyleSheet(按钮样式)

        # 把布局界面放进去
        self.stacked_layout.addWidget(self.main_frame1)
        self.stacked_layout.addWidget(self.main_frame2)
        self.stacked_layout.addWidget(self.main_frame3)

    def 辟邪玉数值选项更新(self, index):
        self.辟邪玉数值[index].clear()
        x = self.辟邪玉选择[index].currentIndex()
        temp = 辟邪玉列表[x].最小值
        while temp <= 辟邪玉列表[x].最大值:
            self.辟邪玉数值[index].addItem(str('%.1f' % temp))
            temp += 辟邪玉列表[x].间隔

    def 辟邪玉属性计算(self, 属性):
        for i in range(4):
            x = self.辟邪玉选择[i].currentIndex()
            if self.辟邪玉数值[i].currentIndex() >= 0:
                辟邪玉列表[x].当前值 = float(self.辟邪玉数值[i].currentText())
            if 辟邪玉列表[x].间隔 == 1:
                辟邪玉列表[x].当前值 = int(辟邪玉列表[x].当前值)
            辟邪玉列表[x].进图属性(属性)

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
        for i in 装备列表:
            if i.部位 != '武器':
                self.装备图标点击事件(装备序号[i.名称], index)
            else:
                if i.类型 in self.角色属性A.武器选项:
                    self.装备图标点击事件(装备序号[i.名称], index)
    
    def 批量打造(self):
        for i in [0,1,2,3,4,5,6,7,9,10]:
            self.装备打造选项[i].setCurrentIndex(1)
            self.装备打造选项[i + 12].setCurrentIndex(10)
        self.装备打造选项[8].setCurrentIndex(0)
        self.装备打造选项[8 + 12].setCurrentIndex(12)
        if '百分比' in self.装备打造选项[37].currentText():
            self.装备打造选项[11].setCurrentIndex(0)
            self.装备打造选项[11 + 12].setCurrentIndex(12)
        if '固伤' in self.装备打造选项[37].currentText():
            self.装备打造选项[11].setCurrentIndex(1)
            self.装备打造选项[11 + 12].setCurrentIndex(10)
        for i in range(24,36):
            self.装备打造选项[i].setCurrentIndex(5)
        self.装备打造选项[36].setCurrentIndex(8)

    def 载入配置(self):
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/attr.ini', 'r', encoding='utf-8').readlines()
            for i in range(0, 17):
                for j in range(0, len(self.属性设置输入[i])):
                    self.属性设置输入[i][j].setText(setfile[i].replace('\n', '').split(',')[j])
        
            for j in range(0, 17):
                self.技能设置输入[j].setCurrentIndex(int(setfile[17].replace('\n', '').split(',')[j]))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/equ.ini', 'r', encoding='utf-8').readlines()
            for i in range(0, len(装备列表)):
                if setfile[i].replace('\n', '') == '1':
                    self.装备图标点击事件(i, 1)
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/equ1.ini', 'r', encoding='utf-8').readlines()
            for i in range(0,len(self.装备打造选项)):
                self.装备打造选项[i].setCurrentIndex(int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/equ2.ini', 'r', encoding='utf-8').readlines()
            for i in range(0,len(self.装备条件选择)):
                self.装备条件选择[i].setCurrentIndex(int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/equ3.ini', 'r', encoding='utf-8').readlines()
            self.称号.setCurrentIndex(int(setfile[0].replace('\n', '')))
            self.宠物.setCurrentIndex(int(setfile[1].replace('\n', '')))
            self.计算模式选择.setCurrentIndex(int(setfile[2].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/skill1.ini', 'r', encoding='utf-8').readlines()
            num = 0
            self.BUFF输入.setText(setfile[num].replace('\n', '')); num += 1
            self.时间输入.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石第一栏.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石第二栏.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            for i in range(0,6):
                self.符文[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.符文效果[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.强化觉醒选择(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/skill2.ini', 'r', encoding='utf-8').readlines()
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
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/skill3.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(4):
                self.辟邪玉选择[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.辟邪玉数值[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

    def 保存配置(self):
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/attr.ini', 'w', encoding='utf-8')
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
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/equ3.ini', 'w', encoding='utf-8')
            setfile.write(str(self.称号.currentIndex())+'\n')
            setfile.write(str(self.宠物.currentIndex())+'\n')
            setfile.write(str(self.计算模式选择.currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/skill1.ini', 'w', encoding='utf-8')
            setfile.write(self.BUFF输入.text()+'\n')
            setfile.write(str(self.时间输入.currentIndex())+'\n')
            setfile.write(str(self.护石第一栏.currentIndex())+'\n')
            setfile.write(str(self.护石第二栏.currentIndex())+'\n')
            for i in range(0,6):
                setfile.write(str(self.符文[i].currentIndex())+'\n')
                setfile.write(str(self.符文效果[i].currentIndex())+'\n')
            setfile.write(str(self.觉醒选择状态)+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/skill2.ini', 'w', encoding='utf-8')
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
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/set/skill3.ini', 'w', encoding='utf-8')
            for i in range(4):
                setfile.write(str(self.辟邪玉选择[i].currentIndex())+'\n')
                setfile.write(str(self.辟邪玉数值[i].currentIndex())+'\n')
        except:
            pass

    def click_window(self, index):
        if self.stacked_layout.currentIndex() != index:
            self.stacked_layout.setCurrentIndex(index)

    def 计算(self):
        self.保存配置()
        if self.组合生成(self.计算模式选择.currentIndex()) == 0:
            QMessageBox.information(self,"错误",  "计算量过大，请更换模式或重新选择装备")
            return
        if len(self.有效穿戴组合) == 0:
            QMessageBox.information(self,"错误",  "无有效组合，请更换模式或重新选择装备")
            return
        
        self.角色属性A = copy.deepcopy(self.初始属性)
        self.角色属性A.技能栏 = copy.deepcopy(self.初始属性.技能栏)
        self.输入属性(self.角色属性A)
        self.伤害列表 = []
        heapq.heapify(self.伤害列表)
        heapSize = 0
        minDamage = -1
        
        if self.神话排名选项.isChecked():
            for i in range(0, len(self.有效穿戴组合)):
                self.角色属性B = copy.deepcopy(self.角色属性A)
                self.角色属性B.技能栏 = copy.deepcopy(self.角色属性A.技能栏)
                self.角色属性B.穿戴装备(self.有效穿戴组合[i], self.有效穿戴套装[i])
                self.角色属性B.装备属性计算()
                self.辟邪玉属性计算(self.角色属性B)
                damage = self.角色属性B.伤害计算()
                if (heapSize > 0):
                    minDamage = self.伤害列表[0][0]
                heapq.heappush(self.伤害列表, [damage] + self.角色属性B.装备栏 + [damage] + self.角色属性B.套装栏 + [self.百变怪列表[i]])
                heapSize = heapSize + 1
    
            self.排行数据.clear()
            self.伤害列表 = heapq.nlargest(heapSize, self.伤害列表)
            神话列表 = []
            for i in range(heapSize):
                tempstr = self.伤害列表[i][1:]
                for j in [0,5,8]:
                    if 装备列表[装备序号[tempstr[j]]].品质=='神话' and tempstr[j] not in 神话列表:
                        神话列表.append(tempstr[j])
                        self.排行数据.append(tempstr)
                if len(神话列表) >= 35:
                    break
        else:
            for i in range(0, len(self.有效穿戴组合)):
                self.角色属性B = copy.deepcopy(self.角色属性A)
                self.角色属性B.技能栏 = copy.deepcopy(self.角色属性A.技能栏)
                self.角色属性B.穿戴装备(self.有效穿戴组合[i], self.有效穿戴套装[i])
                self.角色属性B.装备属性计算()
                self.辟邪玉属性计算(self.角色属性B)
                damage = self.角色属性B.伤害计算()
                if (heapSize > 0):
                    minDamage = self.伤害列表[0][0]
                if heapSize >= 堆大小上限:
                    if damage >= minDamage:
                        heapq.heappushpop(self.伤害列表, [damage] + self.角色属性B.装备栏 + [damage] + self.角色属性B.套装栏 + [self.百变怪列表[i]])
                else:
                    heapq.heappush(self.伤害列表, [damage] + self.角色属性B.装备栏 + [damage] + self.角色属性B.套装栏 + [self.百变怪列表[i]])
                    heapSize = heapSize + 1
    
            self.排行数据.clear()
            self.伤害列表 = heapq.nlargest(heapSize, self.伤害列表)

            for i in range(min(heapSize,堆大小上限)):
                self.排行数据.append(self.伤害列表[i][1:])

                
        if len(self.排行数据) == 0:
            QMessageBox.information(self,"错误",  "请确认有勾选含神话装备的组合")
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
        滚动排行.setWindowTitle('配装排行 （点击伤害数字可查看详情）')  
        滚动排行.setWindowIcon(self.icon)  
    
        背景颜色=QLabel(滚动排行)
        背景颜色.resize(620,1030)
        背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1.0)}")
    
        排行背景透明度=QGraphicsOpacityEffect()
        排行背景透明度.setOpacity(0.5)
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

    def 格式化输出(self, 数字文本):
        if self.显示选项.isChecked():
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
        C = copy.deepcopy(self.角色属性A)
        C.技能栏 = copy.deepcopy(self.角色属性A.技能栏)
        C.穿戴装备(装备名称,套装名称)
        for i in C.装备栏:
            装备列表[装备序号[i]].城镇属性(C)
        for i in C.套装栏:
            套装列表[套装序号[i]].城镇属性(C)
        C.装备基础()

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

        self.角色属性B = copy.deepcopy(self.角色属性A)
        self.角色属性B.技能栏 = copy.deepcopy(self.角色属性A.技能栏)
        self.角色属性B.穿戴装备(装备名称,套装名称)
        self.角色属性B.装备属性计算()
        self.辟邪玉属性计算(self.角色属性B)
        统计详情 = self.角色属性B.伤害计算(1)

        #最大输出界面限制
        if len(self.输出窗口列表)>=10:
            del self.输出窗口列表[0]
    
        输出窗口 = QWidget()
        self.输出窗口列表.append(输出窗口)
        输出窗口.setFixedSize(788, 564)
        输出窗口.setWindowTitle('详细数据')
        输出窗口.setWindowIcon(self.icon)  
        QLabel(输出窗口).setPixmap(self.输出背景图片)
      
        excel=[]
        for i in range(0,len(self.角色属性B.技能栏)):
            excel.append(统计详情[i*4+1])
        excel.sort()

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
    
        面板显示=[]
        for i in range(0,17):
            面板显示.append(QLabel(输出窗口))        
    
        面板显示[0].setText(str(int(self.角色属性B.面板力量())))
        面板显示[1].setText(str(int(self.角色属性B.面板物理攻击力())))
        面板显示[2].setText(str(int(self.角色属性B.面板智力())))
        面板显示[3].setText(str(int(self.角色属性B.面板魔法攻击力())))
        
        面板显示[5].setText(str(int(self.角色属性B.火属性强化)))
        面板显示[6].setText(str(int(self.角色属性B.冰属性强化)))
        面板显示[7].setText(str(int(self.角色属性B.光属性强化)))
        面板显示[8].setText(str(int(self.角色属性B.暗属性强化)))
        
        tempstr = '<font color="#FFFFFF">'+str(int(C.站街独立攻击力()))+'</font>   '
        tempstr += '<font color="#96FF32">'+str(int(self.角色属性B.面板独立攻击力()))+'</font>'
        面板显示[4].setText(tempstr)

        面板显示[9].setText(str(int(C.站街力量())))
        面板显示[10].setText(str(int(C.站街物理攻击力())))
        面板显示[11].setText(str(int(C.站街智力())))
        面板显示[12].setText(str(int(C.站街魔法攻击力())))
        
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
    
        tempstr=[]
        tempstr.append('力智：'+str(int(round(self.角色属性B.百分比力智*100,0)))+'%') 
        tempstr.append('三攻：'+str(int(round(self.角色属性B.百分比三攻*100,0)))+'%') 
        tempstr.append('黄字：'+str(int(round(self.角色属性B.伤害增加*100,0)))+'%')
        tempstr.append('白字：'+str(int(round(self.角色属性B.附加伤害*100,0)))+'%')
        tempstr.append('属白：'+str(int(round(self.角色属性B.属性附加*100,0)))+'%')
        tempstr.append('爆伤：'+str(int(round(self.角色属性B.暴击伤害*100,0)))+'%')
        tempstr.append('终伤：'+str(int(round(self.角色属性B.最终伤害*100,0)))+'%')
        tempstr.append('技攻：'+str(int(round(self.角色属性B.技能攻击力*100-100,0)))+'%')
        tempstr.append('持续：'+str(int(round(self.角色属性B.持续伤害*100,0)))+'%') 
        
        j=318
        for i in tempstr:
            templab=QLabel(输出窗口)
            templab.setText(i)
            templab.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            templab.move(20,j)
            templab.resize(305,18)
            templab.setAlignment(Qt.AlignLeft)
            j+=18
    
        实际技能等级=[]
        技能等效CD=[]
        for i in self.角色属性B.技能栏:
            实际技能等级.append(i.等级)
            if i.是否主动==1:
                技能等效CD.append(i.等效CD(self.角色属性B.武器类型))
            else:
                技能等效CD.append(0)
    
        总伤害数值=0
    
        for i in range(0,len(self.角色属性B.技能栏)):
            j=len(self.角色属性B.技能栏)-1-excel.index(统计详情[i*4+1])
            if 统计详情[i*4] != 0:
                每行详情=[]
                for k in range(0,7):
                    每行详情.append(QLabel(输出窗口))
                #图片
                每行详情[0].setPixmap(self.技能图片[i])
                每行详情[0].resize(28,min(28,self.行高 - 2)) 
                tempstr='<font color="#FF0000"><b>'+self.角色属性B.技能栏[i].名称+'</b></font><br>'
                tempstr+='百分比：<b>'+str(int(self.角色属性B.技能栏[i].等效百分比(self.角色属性B.武器类型) / self.角色属性B.技能栏[i].倍率))+'%</b><br>'
                tempstr+='被动倍率：<b>'+str(round(self.角色属性B.技能栏[i].被动倍率*100,1))+'%</b><br>'
                if self.角色属性B.技能栏[i].倍率!=0:
                    tempstr+='其它倍率：<b>'+str(round(self.角色属性B.技能栏[i].倍率*100,1))+'%</b><br>'
                tempstr+='CD显示：<b>'+str(round(self.角色属性B.技能栏[i].CD,2))+'s</b><br>'
                tempstr+='CD恢复：<b>'+str(round(self.角色属性B.技能栏[i].恢复*100,1))+'%</b>'
                每行详情[0].setToolTip(tempstr)
    
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
                总伤害数值+=int(统计详情[i*4+1])
                每行详情[4].setText(self.格式化输出(str(int(统计详情[i*4+1]))))
                每行详情[4].move(448, 50 + j * self.行高)
                每行详情[4].resize(108,min(28,self.行高)) 
                #平均伤害
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
            if self.角色属性B.技能栏[i].关联技能 != ['无']:
                被动数据=QLabel(输出窗口)
                被动数据.setPixmap(self.技能图片[i])
                tempstr='<font color="#FF0000"><b>'+self.角色属性B.技能栏[i].名称+'</b></font><br>'
                tempstr+='加成倍率：<b>'+str(round(self.角色属性B.技能栏[i].加成倍率(self.角色属性B.武器类型)*100-100,2))+'%</b><br>'
                tempstr+='关联技能：<b>'
                for j in self.角色属性B.技能栏[i].关联技能:
                    tempstr+=j
                    if j != self.角色属性B.技能栏[i].关联技能[-1]:
                        tempstr+=','
                tempstr+='</b>'
                # Will添加
                if self.角色属性B.技能栏[i].关联技能2 != ['无']:
                    tempstr+='<br>加成倍率：<b>'+str(round(self.角色属性B.技能栏[i].加成倍率2(self.角色属性B.武器类型)*100-100,2))+'%</b><br>'
                    tempstr+='关联技能：<b>'
                    for k in self.角色属性B.技能栏[i].关联技能2:
                        tempstr+=k
                        if k != self.角色属性B.技能栏[i].关联技能2[-1]:
                            tempstr+=','
                    tempstr+='</b>'
                if self.角色属性B.技能栏[i].关联技能3 != ['无']:
                    tempstr+='<br>加成倍率：<b>'+str(round(self.角色属性B.技能栏[i].加成倍率3(self.角色属性B.武器类型)*100-100,2))+'%</b><br>'
                    tempstr+='关联技能：<b>'
                    for l in self.角色属性B.技能栏[i].关联技能3:
                        tempstr+=l
                        if l != self.角色属性B.技能栏[i].关联技能3[-1]:
                            tempstr+=','
                    tempstr+='</b>'
                被动数据.setToolTip(tempstr)
                被动数据.move(300+num*40, 500)
                被动等级=QLabel(输出窗口)
                被动等级.setText('Lv.'+str(实际技能等级[i]))
                被动等级.move(300-6+num*40, 480)
                被动等级.resize(40,28)
                if 实际技能等级[i] != 0:
                    被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
                else:
                    被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,0,0)}")
                被动等级.setAlignment(Qt.AlignCenter)  
                num+=1
    
        总伤害=QLabel(输出窗口)
        总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        总伤害.setText(self.格式化输出(str(总伤害数值)))
        总伤害.resize(250,36)
        总伤害.move(10,517)
        总伤害.setAlignment(Qt.AlignCenter) 
    
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
                    if '物理' in self.角色属性B.伤害类型:
                        tempstr[i]+='异次元力量 + '+str(增幅计算(100,装备.品质,self.角色属性B.强化等级[i]))+'</font>'
                    else:
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
            if i.是否主动==1:
                if i.TP上限!=0:
                    i.TP等级=int(self.TP输入[self.角色属性A.技能序号[i.名称]].currentText())
        if self.复选框列表[0].isChecked():
            属性.进图力量+=175
        if self.复选框列表[1].isChecked():
            属性.进图智力+=175
        if self.复选框列表[2].isChecked():
            属性.斗神之吼秘药 = True
        if self.复选框列表[3].isChecked():
            属性.进图属强 += 5
        if self.复选框列表[4].isChecked():
            属性.进图力量+=150
            属性.进图智力+=150
        if self.复选框列表[5].isChecked():
            属性.年宠技能 = True
        if self.复选框列表[7].isChecked():
            属性.技能冷却缩减(1,100,0.20)
        if self.复选框列表[8].isChecked():
            属性.进图力量+=100
            属性.进图智力+=100
            属性.进图属强 += 5
        if self.复选框列表[9].isChecked():
            属性.进图力量+=60
            属性.进图智力+=60
        if self.复选框列表[10].isChecked():
            属性.白兔子技能 = True
        if self.复选框列表[11].isChecked():
            属性.百分比力智+=0.20
        if self.复选框列表[12].isChecked():
            属性.系统奶 = True
        if self.称号.currentText() == '(2020)伟大的意志':
            属性.力量 += 90
            属性.智力 += 90
            属性.物理攻击力 += 65
            属性.魔法攻击力 += 65
            属性.独立攻击力 += 65
            属性.所有属性强化(20)
            属性.暴击伤害 += 0.18
            属性.百分比力智 += 0.04
            if self.复选框列表[6].isChecked():
                属性.进图力量+=35
                属性.进图智力+=35
        if self.称号.currentText() == '(2019)神选之英杰':
            属性.力量 += 75
            属性.智力 += 75
            属性.物理攻击力 += 45
            属性.魔法攻击力 += 45
            属性.独立攻击力 += 65
            属性.所有属性强化(20)
            属性.暴击伤害 += 0.18
            属性.物理暴击率+=0.15
            属性.攻击速度+=0.04
            属性.移动速度+=0.04
            if self.复选框列表[6].isChecked():
                属性.进图力量+=35
                属性.进图智力+=35
        if self.称号.currentText() == '(2020)使徒降临':
            属性.力量 += 80
            属性.智力 += 80
            属性.物理攻击力 += 60
            属性.魔法攻击力 += 60
            属性.独立攻击力 += 60
            属性.所有属性强化(15)
            属性.附加伤害 += 0.12
            属性.百分比力智 += 0.03
            if self.复选框列表[6].isChecked():
                属性.进图力量+=35
                属性.进图智力+=35
        if self.称号.currentText() == '(2018)神之试炼':
            属性.力量 += 55
            属性.智力 += 55
            属性.所有属性强化(15)
            属性.暴击伤害 += 0.15
            if self.复选框列表[6].isChecked():
                属性.进图属强 += 10
        if self.称号.currentText() == '(2019)超越极限者':
            属性.力量 += 60
            属性.智力 += 60
            属性.所有属性强化(15)
            属性.暴击伤害 += 0.15
            if self.复选框列表[6].isChecked():
                属性.进图属强 += 10
        if self.称号.currentText() == '(2015)哥特绮梦':
            属性.力量 += 30
            属性.智力 += 30
            属性.物理攻击力 += 70
            属性.魔法攻击力 += 70
            属性.独立攻击力 += 90
            属性.加算冷却缩减 += 0.10
        if self.宠物.currentText() == '(2020)至尊':
            属性.力量 += 150
            属性.智力 += 150
            属性.所有属性强化(24)
            属性.附加伤害 += 0.15
            属性.技能等级加成('所有',1,50,1)
            属性.加算冷却缩减 += 0.05
            属性.最终伤害 += 0.05
            属性.百分比力智 += 0.12
        if self.宠物.currentText() == '(2019)至尊·进化':
            属性.力量 += 120
            属性.智力 += 120
            属性.所有属性强化(24)
            属性.附加伤害 += 0.15
            属性.技能等级加成('所有',1,50,1)
            属性.加算冷却缩减 += 0.05
            属性.最终伤害 += 0.05
            属性.百分比力智 += 0.08
        if self.宠物.currentText() == '(2020)普通':
            属性.力量 += 140
            属性.智力 += 140
            属性.所有属性强化(24)
            属性.附加伤害 += 0.12
            属性.技能等级加成('所有',1,50,1)
            属性.加算冷却缩减 += 0.05
            属性.百分比力智 += 0.10

        if self.宠物.currentText() == '(2019)普通':
            属性.力量 += 120
            属性.智力 += 120
            属性.所有属性强化(24)
            属性.附加伤害 += 0.12
            属性.技能等级加成('所有',1,50,1)
            属性.加算冷却缩减 += 0.05

    
        if self.护石第一栏.currentText()!= '无':
            属性.技能栏[self.角色属性A.技能序号[self.护石第一栏.currentText()]].装备护石()
            属性.护石第一栏 = self.护石第一栏.currentText()
    
        if self.护石第二栏.currentText()!= '无':
            属性.技能栏[self.角色属性A.技能序号[self.护石第二栏.currentText()]].装备护石()
            属性.护石第二栏 = self.护石第二栏.currentText()
    
        for i in range(0,6):
            if self.符文[i].currentText()!='无':
                if self.符文效果[i].currentText()=='攻击+5%,CD+3%':
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率*=1.05
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD*=1.03
                if self.符文效果[i].currentText()=='CD-4%':
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD*=0.96
                if self.符文效果[i].currentText()=='攻击+3%':
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率*=1.03
                if self.符文效果[i].currentText()=='攻击-3%,CD-6%':
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率*=0.97
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD*=0.94
                if self.符文效果[i].currentText()=='攻击+3%,CD+2%':
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率*=1.03
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD*=1.02
                if self.符文效果[i].currentText()=='CD-3%':
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD*=0.97
                if self.符文效果[i].currentText()=='攻击+2%':
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率*=1.02
                if self.符文效果[i].currentText()=='攻击-2%,CD-4%':
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率*=0.98
                    属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD*=0.96

        for i in range(0,12):
            属性.是否增幅[i] = self.装备打造选项[i].currentIndex()
            属性.强化等级[i] = self.装备打造选项[i + 12].currentIndex()
            属性.改造等级[i] = self.装备打造选项[i + 24].currentIndex()
        属性.武器锻造等级 = self.装备打造选项[36].currentIndex()
        属性.伤害类型 = self.装备打造选项[37].currentText()

        try:
            属性.主BUFF = float(self.BUFF输入.text()) / 100 + 1
        except: 
            QMessageBox.information(主窗口,"错误",  "BUFF数值输入错误,已设置为默认数值") 
            self.BUFF输入.setText(str((self.角色属性A.主BUFF - 1) * 100))
    
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
        属性.持续伤害计算比例 = self.装备条件选择[9].currentIndex()
        属性.军神的隐秘遗产 = self.装备条件选择[10].currentIndex()
        属性.太极天帝剑 = self.装备条件选择[11].currentIndex()
        属性.绿色生命的面容 = self.装备条件选择[12].currentIndex()
        if self.装备条件选择[13].currentIndex() != 0:
            属性.最终伤害+=0.05
            属性.百分比三攻+=0.05
            属性.技能攻击力*=1.05
        if self.装备条件选择[13].currentIndex() == 1:
            属性.暴击伤害+=0.05
            属性.百分比力智+=0.05
            属性.伤害增加+=0.05
        if self.装备条件选择[13].currentIndex() == 2:
            属性.暴击伤害+=0.03
            属性.百分比力智+=0.03
            属性.伤害增加+=0.02

            属性.技能冷却缩减(1,45,0.2)
            属性.技能冷却缩减(60,70,0.2)
            属性.技能冷却缩减(75,80,0.17)
        if self.装备条件选择[13].currentIndex() == 3:
            属性.技能倍率加成(50,0.17)
            属性.技能倍率加成(85,0.17)
            属性.技能倍率加成(100,0.10)

            属性.技能倍率加成(50,0.17)
            属性.技能倍率加成(85,0.17)
            属性.技能倍率加成(100,0.10)

            属性.技能倍率加成(50,0.17)
            属性.技能倍率加成(85,0.17)
            属性.技能倍率加成(100,0.10)
        if self.装备条件选择[13].currentIndex() == 4:
            属性.暴击伤害+=0.04
            属性.百分比力智+=0.04
            属性.伤害增加+=0.04
        if self.装备条件选择[13].currentIndex() == 5:
            属性.所有属性强化(45)
        if self.装备条件选择[13].currentIndex() == 6:
            属性.所有属性强化(90)
        if self.装备条件选择[13].currentIndex() == 7:
            属性.所有属性强化(135)

        属性.时间输入 = int(self.时间输入.currentText())
        属性.次数输入.clear()
        属性.宠物次数.clear()
        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.是否有伤害 == 1:
                属性.次数输入.append(self.次数输入[序号].currentText())
                if self.次数输入[序号].currentIndex() != 0:
                    self.宠物次数[序号].setCurrentIndex(min(self.宠物次数[序号].currentIndex(), self.次数输入[序号].currentIndex() - 1 + i.基础释放次数))
                属性.宠物次数.append(self.宠物次数[序号].currentIndex())
            else:
                属性.次数输入.append('')
                属性.宠物次数.append(0)

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
        for i in 属性.技能栏:
            if name == i.名称+'Lv+1':
                i.等级加成(1)
                return
    
    def 基础属性(self, 属性):
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

        属性.百分比力智 += temp[0]
        属性.百分比三攻 += temp[1]
        属性.伤害增加 += temp[2]
        属性.附加伤害 += temp[3]
        属性.属性附加 += temp[4]
        属性.暴击伤害 += temp[5]
        属性.最终伤害 += temp[6]
        属性.技能攻击力 *= 1 + temp[7]

        for i in [0,7,13]:
            for j in range(0,17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 0 and j in [1,5,10,16]:
                        属性.进图力量+=float(self.属性设置输入[i][j].text())
                    else:
                        属性.力量+=float(self.属性设置输入[i][j].text())
        for i in [1,8,14]:
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
                    else:
                        属性.所有属性强化(float(self.属性设置输入[i][j].text()))
    
        for j in range(0,17):
            if self.属性设置输入[6][j].text() != '':
                属性.附加伤害+=float(self.属性设置输入[6][j].text())/100
    
        for j in range(0,17):
            if self.属性设置输入[15][j].text() != '':
                属性.最终伤害+=float(self.属性设置输入[15][j].text())/100
    
        for i in self.技能设置输入:
            self.技能加成判断(i.currentText(), 属性)

    def 组合生成(self, index):
        self.有效穿戴组合.clear()
        self.有效穿戴套装.clear()
        self.百变怪列表.clear()
        套装组合=[]
        套装适用=[]
        if index <= 1:
            for a in self.有效防具套装:
                for b in self.有效首饰套装:
                    for c in self.有效特殊套装:
                        套装组合.append([a, a, a, a, a, b, b, b, c, c, c]); 套装适用.append([a + '[2]', a + '[3]', a + '[5]', b + '[2]', b + '[3]', c + '[2]', c + '[3]'])
    
            for a in self.有效防具套装:
                for d in self.有效上链左套装:
                    for e in self.有效镯下右套装:
                        for f in self.有效环鞋指套装:
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
    
        if index != 2:
            count = -1
            count2 = 0
            for temp in 套装组合:
                count += 1
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
                        for i in self.有效武器列表:
                            self.有效穿戴组合.append(temp1 + [i])
                            self.有效穿戴套装.append(套装适用[count])
                            self.百变怪列表.append(sign2)
                            count2 += 1
                            if count2 > 最大组合数计算上限:
                                return 0
                                                                
        else:
            count = 0
            for a1 in self.有效部位列表[0]:
                for a2 in self.有效部位列表[1]:
                    for a3 in self.有效部位列表[2]:
                        for a4 in self.有效部位列表[3]:
                            for a5 in self.有效部位列表[4]:
                                for a6 in self.有效部位列表[5]:
                                    for a7 in self.有效部位列表[6]:
                                        for a8 in self.有效部位列表[7]:
                                            for a9 in self.有效部位列表[8]:
                                                for a10 in self.有效部位列表[9]:
                                                    for a11 in self.有效部位列表[10]:
                                                        for a12 in self.有效部位列表[11]:
                                                            temp = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
                                                            神话数量 = 0
                                                            for i in temp:
                                                                if 装备列表[装备序号[i]].品质 == '神话':
                                                                    神话数量 += 1
                                                            if 神话数量 <= 1:
                                                                件数统计 = [0] * len(所有套装列表)
                                                                for i in temp:
                                                                    所属套装名称 = 装备列表[装备序号[i]].所属套装
                                                                    if 所属套装名称 != '无' and 所属套装名称 != '智慧产物':
                                                                        件数统计[所有套装列表.index(所属套装名称)] += 1
                                                                temp2 = []
                                                                for i in range(0,len(件数统计)):
                                                                    if 件数统计[i] >= 2:
                                                                        temp2.append(所有套装列表[i] + '[2]')
                                                                    if 件数统计[i] >= 3:
                                                                        temp2.append(所有套装列表[i] + '[3]')
                                                                    if 件数统计[i] >= 5:
                                                                        temp2.append(所有套装列表[i] + '[5]')    
                                                                self.有效穿戴组合.append(temp)
                                                                self.有效穿戴套装.append(temp2)
                                                                self.百变怪列表.append('空')
                                                                count += 1
                                                                if count > 最大组合数计算上限:
                                                                    return 0
        return 1
