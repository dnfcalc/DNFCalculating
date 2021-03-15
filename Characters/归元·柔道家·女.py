from math import *
from PublicReference.base import *

class 归元·柔道家·女技能0(主动技能):
    名称 = '背摔'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 1386.43 * 1.092
    成长 = 156.57 * 1.092
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5

class 归元·柔道家·女技能1(主动技能):
    名称 = '抛投'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 3164.50 * 1.077
    成长 = 357.47 * 1.077
    CD = 8.5
    TP成长 = 0.1
    TP上限 = 5

class 归元·柔道家·女技能2(被动技能):
    名称 = '摔技强化'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1 + 0.01 * self.等级, 5)
            else:
                return round(1.1 + 0.02 * (self.等级 - 10), 5)

class 归元·柔道家·女技能3(主动技能):
    名称 = '折颈'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 41
    基础 = 3430.65
    成长 = 387.38
    CD = 7.7
    TP成长 = 0.1
    TP上限 = 5

class 归元·柔道家·女技能4(主动技能):
    名称 = '野蛮冲撞'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4091.91 * 1.05
    成长 = 462.08 * 1.05
    CD = 8.0
    TP成长 = 0.1
    TP上限 = 5

class 归元·柔道家·女技能5(被动技能):
    名称 = '强力抱摔'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 归元·柔道家·女技能6(主动技能):
    名称 = '霹雳肘击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5348.07 * 1.05
    成长 = 603.95 * 1.05
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5

class 归元·柔道家·女技能7(主动技能):
    名称 = '空绞锤'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 3787.39 * 1.078
    成长 = 436.65 * 1.078
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5

class 归元·柔道家·女技能8(主动技能):
    名称 = '霹雳冲击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 2559.92
    成长 = 289.04
    基础2 = 5835.91
    成长2 = 659.11
    攻击次数2 = 1
    倍率 =  1.103
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

class 归元·柔道家·女技能9(主动技能):
    名称 = '螺旋彗星落'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8630.10 * 1.078
    成长 = 974.93 * 1.078
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
            self.CD *= 0.88 
        elif x == 1:
            self.倍率 *= 1.29
            self.CD *= 0.88
    #附加效果：攻击力+8%更变至攻击力+17%

class 归元·柔道家·女技能10(主动技能):
    名称 = '地狱摇篮（抓轰炮）'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 13623.29 * 1.078
    成长 = 1539.26 * 1.078
    CD = 30.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.32
            self.CD *= 0.9
    #附加效果：最后一击攻击力+30%更变至最后一击攻击力+59% ; [抓轰炮]攻击力 +10%更变至[抓轰炮]攻击力 +19%
        
class 归元·柔道家·女技能11(主动技能):
    名称 = '裂石破天'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 15889.25 * 1.10
    成长 = 1794.98 * 1.10
    CD = 45
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.31
   #最后一击冲击波攻击力+17%更变至最后一击冲击波攻击力+28% ; [随机应变]冲击波攻击力增加量+13%更变至[随机应变]冲击波攻击力增加量+21%

class 归元·柔道家·女技能12(被动技能):
    名称 = '抓取奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.015 * self.等级, 5)

class 归元·柔道家·女技能13(主动技能):
    名称 = '末日风暴'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 1340.79
    成长 = 406.02
    基础2 = 20945.11
    成长2 = 6317.08
    攻击次数2 = 1
    倍率 = 1.107
    CD = 140.0

class 归元·柔道家·女技能14(主动技能):
    名称 = '空绞连锤（抓轰炮）'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 1170.88
    成长 = 132.08
    基础2 = 14058.93
    成长2 = 1588.06
    攻击次数2 = 1
    倍率 = 1.132
    CD = 30.0
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.12
        elif x == 1:
            self.倍率 *= 1.21
    #攻击力 +12%更变至攻击力  +21%

class 归元·柔道家·女技能15(被动技能):
    名称 = '极手奥义'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 归元·柔道家·女技能16(主动技能):
    名称 = '死亡摇篮'
    所在等级 = 70
    等级上限 = 60
    基础等级 = 18
    基础 = 25524.88 * 1.10
    成长 = 2883.51 * 1.10
    CD = 50
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.31

class 归元·柔道家·女技能17(主动技能):
    名称 = '末日摇篮'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 7654.70
    成长 = 864.27
    基础2 = 30620.97
    成长2 = 3457.06
    攻击次数2 = 1
    倍率 = 1.1
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3225
            self.CD *=0.9
    #攻击力+15% ；生成总攻击力15%伤害的旋风（多段，15次攻击，每次1%）

class 归元·柔道家·女技能18(主动技能):
    名称 = '风暴之舞'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 5308.98
    成长 = 600.99
    攻击次数 = 6
    基础2 = 14760.91
    成长2 = 1665.05
    攻击次数2 = 1
    倍率 = 1.1
    CD = 45.0 
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 0.56
            self.成长 *= 0.56
            self.攻击次数 = 13
            self.倍率 *= 1.19 
    #多段攻击力减少44% ；次数+7；攻击力+19%

class 归元·柔道家·女技能19(主动技能):
    名称 = '苍宇彗星落'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 8601.87
    成长 = 2598.03
    基础2 = 77442.63
    成长2 = 23385.07
    攻击次数2 = 1
    倍率 = 1.1
    CD = 180

class 归元·柔道家·女技能20(被动技能):
    名称 = '光芒之翼'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 归元·柔道家·女技能21(主动技能):
    名称 = '送葬舞步'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 6
    基础 = 94820.66208
    成长 = 10706.22299
    CD = 60.0

class 归元·柔道家·女技能22(主动技能):
    名称 = '女皇时代辉煌舞台'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']
    基础 = 266199.5202
    成长 = 80363.47518
    CD = 290
    def 加成倍率(self, 武器类型):
        return 0


归元·柔道家·女技能列表 = []
i = 0
while i >= 0:
    try:
        exec('归元·柔道家·女技能列表.append(归元·柔道家·女技能'+str(i)+'())')
        i += 1
    except:
        i = -1

归元·柔道家·女技能序号 = dict()
for i in range(len(归元·柔道家·女技能列表)):
    归元·柔道家·女技能序号[归元·柔道家·女技能列表[i].名称] = i

归元·柔道家·女一觉序号 = 0
归元·柔道家·女二觉序号 = 0
归元·柔道家·女三觉序号 = 0
for i in 归元·柔道家·女技能列表:
    if i.所在等级 == 50:
        归元·柔道家·女一觉序号 = 归元·柔道家·女技能序号[i.名称]
    if i.所在等级 == 85:
        归元·柔道家·女二觉序号 = 归元·柔道家·女技能序号[i.名称]
    if i.所在等级 == 100:
        归元·柔道家·女三觉序号 = 归元·柔道家·女技能序号[i.名称]

归元·柔道家·女护石选项 = ['无']
for i in 归元·柔道家·女技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元·柔道家·女护石选项.append(i.名称)

归元·柔道家·女符文选项 = ['无']
for i in 归元·柔道家·女技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元·柔道家·女符文选项.append(i.名称)

class 归元·柔道家·女角色属性(角色属性):

    实际名称 = '归元·柔道家·女'
    角色 = '格斗家(女)'
    职业 = '柔道家'

    武器选项 = ['手套','臂铠','东方棍','爪']
    
    类型选择 = ['物理固伤']
    
    类型 = '物理固伤'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 2.07
   
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(归元·柔道家·女技能列表)
        self.技能序号= deepcopy(归元·柔道家·女技能序号)

class 归元·柔道家·女(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 归元·柔道家·女角色属性()
        self.角色属性A = 归元·柔道家·女角色属性()
        self.角色属性B = 归元·柔道家·女角色属性()
        self.一觉序号 = 归元·柔道家·女一觉序号
        self.二觉序号 = 归元·柔道家·女二觉序号
        self.三觉序号 = 归元·柔道家·女三觉序号
        self.护石选项 = deepcopy(归元·柔道家·女护石选项)
        self.符文选项 = deepcopy(归元·柔道家·女符文选项)

    def 界面(self):
        super().界面()

        self.死亡风暴次数选择=MyQComboBox(self.main_frame2)
        for i in range(1, 14):
            self.死亡风暴次数选择.addItem('末日风暴：' + str(i) + '段')
        self.死亡风暴次数选择.setCurrentIndex(12)
        self.死亡风暴次数选择.resize(120,20)
        self.死亡风暴次数选择.move(325,390)   

    def 载入配置(self, path='set'):
        super().载入配置(path)
        try:
           setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'r',encoding='utf-8').readlines()
           self.死亡风暴次数选择.setCurrentIndex(int(setfile[0].replace('\n', '')))
        except:
            pass

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'w', encoding='utf-8')
            setfile.write(str(self.死亡风暴次数选择.currentIndex())+'\n')
        except:
            pass

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        属性.技能栏[属性.技能序号['末日风暴']].攻击次数 *= self.死亡风暴次数选择.currentIndex() + 1
