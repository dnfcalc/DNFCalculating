from math import *
from PublicReference.base import *

class 缔造者技能0(主动技能):
    名称 = '烈火燎原'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    基础 = 420.0 / 70
    成长 = 280.0 / 70
    能量 = 140
    最小值 = 2  
    CD = 5.0
    持续秒数 = 6.0
    TP成长 = 0.08
    TP上限 = 5
    
    def 觉醒模式(self, x):
        if x == 1:
            self.最小值=70
            self.基础 = self.基础 * 70 / 2
            self.成长 = self.成长 * 70 / 2
        
        

class 缔造者技能1(主动技能):
    名称 = '炽炎星陨'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    基础 = 119.0 / 7
    成长 = 252.0 / 7
    能量 = 140
    最小值 = 20      
    CD = 5.0
    持续秒数 = 1.0
    TP成长 = 0.08
    TP上限 = 5
    def 觉醒模式(self, x):
        if x == 1:
            self.最小值=70
            self.基础 = self.基础 * 70 / 20
            self.成长 = self.成长 * 70 / 20

class 缔造者技能2(主动技能):
    名称 = '冰霜之球'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 2960.0 / 7
    成长 = 400.0 / 7
    能量 = 140
    最小值 = 20 
    CD = 10.0
    持续秒数 = 3.0
    TP成长 = 0.08
    TP上限 = 5
    
    def 觉醒模式(self, x):
        if x == 1:
            self.最小值=70
            self.基础 = self.基础 * 70 / 20
            self.成长 = self.成长 * 70 / 20

class 缔造者技能3(主动技能):
    名称 = '冰天震地'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 2359.0 / 3
    成长 = 378.0 / 3
    能量 = 140
    最小值 = 40 
    CD = 10.0
    持续秒数 = 1.0
    TP成长 = 0.08
    TP上限 = 5
    
    def 觉醒模式(self, x):
        if x == 1:
            self.最小值=140
            self.基础 = self.基础 * 140 / 40
            self.成长 = self.成长 * 140 / 40

class 缔造者技能4(被动技能):
    名称 = '幻想之境'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1 + 0.01 * self.等级 , 5)
        else:
            return round(1.1 + 0.015 * (self.等级 - 10) , 5)

    def 独立攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 缔造者技能5(被动技能):
    名称 = '具象强化'
    所在等级 = 25
    等级上限 = 40
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.025 * self.等级, 5)

class 缔造者技能6(主动技能):
    名称 = '烈焰飓风'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4560
    成长 = 504
    能量 = 140
    最小值 = 60     
    CD = 20
    持续秒数 = 4.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.倍率 *= 1.0
        elif x == 1:
            self.CD *= 0.85
            self.倍率 *= 1.09

class 缔造者技能7(主动技能):
    名称 = '极冰护盾'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2342.0
    成长 = 261.0
    CD = 20.0
    持续秒数 = 1.0
    能量 = 140
    最小值 = 60  
    TP成长 = 0.10
    TP上限 = 5
    
    

class 缔造者技能8(主动技能):
    名称 = '超能旋风波'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 9962.0 / 35
    成长 = 1190.0 / 35
    CD = 25.0
    持续秒数 = 5.0
    能量 = 140
    最小值 = 4
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.32
    
    def 觉醒模式(self, x):
        if x == 1:
            self.最小值=46
            self.基础 = self.基础 * 46 / 4
            self.成长 = self.成长 * 46 / 4
            
class 缔造者技能9(主动技能):
    名称 = '风暴漩涡'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 9100.0 / 7
    成长 = 1015.0 / 7
    能量 = 140
    最小值 = 20
    CD = 25.0
    持续秒数 = 5.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.倍率 *= 1.22
    
    def 觉醒模式(self, x):
        if x == 1:
            self.最小值 = 70
            self.基础 = self.基础 * 70 / 20
            self.成长 = self.成长 * 70 / 20

class 缔造者技能10(被动技能):
    名称 = '洞悉'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)

class 缔造者技能11(主动技能):
    名称 = '末日虫洞'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 19
    基础 = 11434.00
    成长 = 2168.0
    CD = 45.0
    持续秒数 = 3.0
    能量 = 100
    最小值 = 100
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
        elif x == 1:
            self.倍率 *= 1.28

class 缔造者技能12(主动技能):
    名称 = '冰雪降临'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 16
    基础 = 24544.8 / 2
    成长 = 4586.4 / 2
    CD = 31.5
    持续秒数 = 3.0
    能量 = 100
    最小值 = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.最小值 = 2
            self.基础 = self.基础 / 25 * 1.28
            self.成长 = self.成长 / 25 * 1.28
            self.持续秒数 = 0.5
            # self.CD = self.CD / 25
            # self.倍率 *= 1.28
        elif x == 1:
            self.最小值 = 2
            self.基础 = self.基础 / 25 * 1.37
            self.成长 = self.成长 / 25 * 1.37
            self.持续秒数 = 0.5

class 缔造者技能13(主动技能):
    名称 = '时空链接'
    所在等级 = 70
    等级上限 = 60
    基础等级 = 18
    基础 = 49744.72 / 2
    成长 = 5709.96 / 2
    CD = 54
    持续秒数 = 5.0
    能量 = 100
    最小值 = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.32

class 缔造者技能14(被动技能):
    名称 = '创世之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 缔造者技能15(主动技能):
    名称 = '时空禁制'
    所在等级 = 80
    等级上限 = 60
    基础等级 = 9
    基础 = 35205.00
    成长 = 6797.00
    CD = 45.0
    持续秒数 = 7.0
    能量 = 100
    最小值 = 100
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.5 * 2.74

class 缔造者技能16(主动技能):
    名称 = '创世'
    备注 = '(直接爆炸)'
    所在等级 = 85
    等级上限 = 60
    基础等级 = 5
    基础 = 84924.00
    成长 = 25632.0
    CD = 180.0
    持续秒数 = 1
    能量 = 100
    最小值 = 100

class 缔造者技能17(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 缔造者技能18(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 缔造者技能19(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

class 缔造者技能20(被动技能):
    名称 = '自我觉醒'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.11

    def 独立攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.11

缔造者技能列表 = []
i = 0
while i >= 0:
    try:
        exec('缔造者技能列表.append(缔造者技能' + str(i) + '())')
        i += 1
    except:
        i = -1

缔造者技能序号 = dict()
for i in range(len(缔造者技能列表)):
    缔造者技能序号[缔造者技能列表[i].名称] = i

缔造者一觉序号 = 16
缔造者二觉序号 = 16
缔造者三觉序号 = 19

缔造者护石选项 = ['无']
for i in 缔造者技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        缔造者护石选项.append(i.名称)

缔造者符文选项 = ['无']
for i in 缔造者技能列表:
    if i.所在等级 >= 1 and i.所在等级 <= 75  and i.是否有伤害 == 1:
        缔造者符文选项.append(i.名称)


class 缔造者角色属性(角色属性):
    实际名称 = '缔造者'
    角色 = '缔造者'
    职业 = '缔造者'

    武器选项 = ['魔杖','法杖','棍棒','矛','扫把']

    类型选择 = ['魔法固伤']

    类型 = '魔法固伤'
    防具类型 = '板甲'
    防具精通属性 = ['智力']

    主BUFF = 1.66

    远古记忆 = 0
    
    数据精算模式=0
    觉醒模式=1
    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(缔造者技能列表)
        self.技能序号 = deepcopy(缔造者技能序号)

    def 技能等级加成(self, 加成类型, minLv, maxLv, lv,可变 = 0):
        lv = int(lv)

        if self.装备描述 ==1:
            if 加成类型=="所有":
                if minLv == maxLv:
                    return "Lv{} 技能等级+{}<br>".format(minLv,lv)
                else:
                    return "Lv{}-{} 技能等级+{}<br>".format(minLv,maxLv,lv)
            else:
                if minLv == maxLv:
                    return "Lv{} 主动技能等级+{}<br>".format(minLv,lv)
                else:
                    return "Lv{}-{} 主动技能等级+{}<br>".format(minLv,maxLv,lv)            
        else:  
            if self.远古记忆 > 0:
                if minLv <= 15 and maxLv >= 15:
                    self.远古记忆 = min(20, self.远古记忆 + lv)

            for i in self.技能栏:
                if i.所在等级 >= minLv and i.所在等级 <= maxLv:
                    if 加成类型 == '所有':
                        i.等级加成(lv)
            if 可变 > 0:
                self.变换词条[可变-1] = [6,2,14 + (2 if 可变 > 1 else 4), 14 + (9 if 可变 > 1 else 17)]
        return ''

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            modelchange= '觉醒模式' in dir(i)
            if modelchange and self.觉醒模式==1:
#                print('hello')
                i.觉醒模式(1)
            if i.是否有伤害 == 1:
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    
                    余数伤害时间=((int(i.能量 * (1 + (self.时间输入) / i.等效CD(self.武器类型,self.类型)))-int(int(i.能量 * (1 + (self.时间输入) / i.等效CD(self.武器类型,self.类型))) / i.最小值)*i.最小值)/i.能量)*i.等效CD(self.武器类型,self.类型)
                    余数次数=0
                    if 余数伤害时间<i.持续秒数:
                        if 余数伤害时间<0.5:
                            余数次数=-1
                        else:
                            余数次数=-1+余数伤害时间/i.持续秒数
                    else:
                        余数次数=0
                    if self.数据精算模式==1:

                        技能释放次数.append(round(int(int(i.能量 * (1 + (self.时间输入) / i.等效CD(self.武器类型,self.类型))) / i.最小值)+余数次数,2))
                    else:
                        余数次数=0
                        技能释放次数.append(round(int(int(i.能量 * (1 + (self.时间输入) / i.等效CD(self.武器类型,self.类型))) / i.最小值)+余数次数,2))
                    
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)
        return 技能释放次数
    
class 缔造者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 缔造者角色属性()
        self.角色属性A = 缔造者角色属性()
        self.角色属性B = 缔造者角色属性()
        self.一觉序号 = 缔造者一觉序号
        self.二觉序号 = 缔造者二觉序号
        self.三觉序号 = 缔造者三觉序号
        self.护石选项 = deepcopy(缔造者护石选项)
        self.符文选项 = deepcopy(缔造者符文选项)

    def 界面(self):
        super().界面()
        self.数据精算模式=QCheckBox('数据精算模式',self.main_frame2)
        self.数据精算模式.resize(100,20)
        self.数据精算模式.move(335,490)
        self.数据精算模式.setStyleSheet(复选框样式)
        self.数据精算模式.setChecked(True)
        
        self.觉醒模式=QCheckBox('觉醒模式',self.main_frame2)
        self.觉醒模式.resize(100,20)
        self.觉醒模式.move(335,520)
        self.觉醒模式.setStyleSheet(复选框样式)
        self.觉醒模式.setChecked(True)
        
    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        if self.数据精算模式.isChecked():
            属性.数据精算模式=1
        else:
            属性.数据精算模式=0
            
        if self.觉醒模式.isChecked():
            属性.觉醒模式=1
        else:
            属性.觉醒模式=0