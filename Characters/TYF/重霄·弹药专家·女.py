from PublicReference.base import *
from math import *

等级 = 100 + 5


with open(os.path.join(skillDataPath,"CurrentVersion","重霄·弹药专家·女.json"), encoding='utf-8') as fp:
  skill_info = json.load(fp)
fp.close()


class 职业主动技能(主动技能):

    技能施放时间 = 0.0
    脱手 = 1

    data0 = []
    data1 = []
    data2 = []
    data3 = []

    hit0 = 1
    hit1 = 0
    hit2 = 0
    hit3 = 0

    power0 = 1
    power1 = 1
    power2 = 1
    power3 = 1



    def __init__(self,skillName):
        self.名称 = skillName
        self.CD = skill_info[skillName]["CD"]
        self.所在等级 = skill_info[skillName]["所在等级"]
        self.等级上限 = skill_info[skillName]["等级上限"]
        self.学习间隔 = skill_info[skillName]["学习间隔"]
        self.等级精通 = skill_info[skillName]["等级精通"]
        self.基础等级 = min(int((等级 - self.所在等级) / self.学习间隔), self.等级精通) + 1
        for i in range(len(skill_info[skillName]["attackInfo"])):
            exec('self.data'+str(i)+'=skill_info[skillName]["attackInfo"]['+str(i)+']["data"]')
            exec('self.hit'+ str(i)+'=skill_info[skillName]["attackInfo"]['+str(i)+']["hit"]')
            exec('self.power'+ str(i)+'=skill_info[skillName]["attackInfo"]['+str(i)+']["power"]')

        super().__init__()

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.data0) >= self.等级 and len(self.data0) > 0:
            等效倍率 += self.data0[self.等级] * self.hit0 * self.power0
        if len(self.data1) >= self.等级 and len(self.data1) > 0:
            等效倍率 += self.data1[self.等级] * self.hit1 * self.power1
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.hit2 * self.power2
        if len(self.data3) >= self.等级 and len(self.data3) > 0:
            等效倍率 += self.data3[self.等级] * self.hit3 * self.power3
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能0(被动技能):
    名称 = '单兵推进器'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['交叉射击', '聚合弹', '凝固汽油弹', '轻火力速射']
    关联技能2 = ['爆裂弹']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (10 + self.等级) / 100, 3)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (2 * self.等级) / 100, 3)


class 技能1(被动技能):
    名称 = '兵器研究'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['EMP磁爆', '决战之日', '终解·制空霸权']

    def 加成倍率(self, 武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def 独立攻击力倍率(self, 武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.01 * self.等级, 3)


class 技能2(被动技能):
    名称 = '手雷精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['G35感电手雷', 'G18冰冻手雷']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.1 * self.等级, 3)


class 技能3(被动技能):
    名称 = '弹药改良'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['所有']
    技能加成描述 = ''
    加成数值 = 1.0

    def 加成倍率(self, 武器类型):
        return self.加成数值

    自定义描述 = 1

    def 技能描述(self, 武器类型):
        return self.技能加成描述


class 技能4(职业主动技能):
    def __init__(self):
        super().__init__('M18阔剑地雷')
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能5(职业主动技能):
    def __init__(self):
        super().__init__('G35感电手雷')
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    基础释放次数 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if (self.等级 < 18):
            return 1.0
        else:
            return round(1 + 0.01 * (self.等级 - 18), 3)

    def 等效CD(self, 武器类型, 输出类型):
        # 经过测试,手雷恢复速度无法享受技能冷却恢复加成
        return round(self.CD, 1)


class 技能6(职业主动技能):
    def __init__(self):
        super().__init__('交叉射击')
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能7(职业主动技能):
    def __init__(self):
        super().__init__('爆裂弹')

class 技能8(职业主动技能):
    def __init__(self):
        super().__init__('G18冰冻手雷')

    基础释放次数 = 3
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        # 经过测试,手雷恢复速度无法享受技能冷却恢复加成
        return round(self.CD, 1)


class 技能9(职业主动技能):
    def __init__(self):
        super().__init__('聚合弹')

    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能10(职业主动技能):
    def __init__(self):
        super().__init__('C4飞弹')
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.data0 = [i * 1.16 for i in self.data0]
        elif 类型 == 1:
            self.data0 = [i * 1.25 for i in self.data0]


class 技能11(职业主动技能):
    def __init__(self):
        super().__init__('凝固汽油弹')

    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.data0 = [x * 1.31 for x in self.data0]
            self.hit1 = 0
            self.CD *= 0.94
        elif 类型 == 1:
            self.data0 = [x * 1.40 for x in self.data0]
            self.hit1 = 0
            self.CD *= 0.94


class 技能12(职业主动技能):
    def __init__(self):
        super().__init__('镭射狙击')

    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.data0 = [x * 0.26 for x in self.data0]
            self.hit0 = 24
            self.技能施放时间 = 3.0
        elif 类型 == 1:
            self.data0 = [x * 0.28 for x in self.data0]
            self.hit0 = 24
            self.技能施放时间 = 3.0


class 技能13(被动技能):
    名称 = '弹药强化'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        return 1.105 + self.等级 * 0.015 if self.等级 > 0 else 1


class 技能14(职业主动技能):
    def __init__(self):
        super().__init__('EMP磁爆')
    名称 = 'EMP磁爆'


class 技能15(职业主动技能):
    def __init__(self):
        super().__init__('G61重力地雷')

    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    技能施放时间 = 3
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.data0 = [x * 2.16 for x in self.data0]
            self.技能施放时间 = 0.5
            self.hit1 = 5
        elif 类型 == 1:
            self.data0 = [x * 2.34 for x in self.data0]
            self.技能施放时间 = 0.5
            self.hit1 = 5


class 技能16(职业主动技能):
    def __init__(self):
        super().__init__('轻火力速射')
    脱手 = 0

    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    技能施放时间 = 1
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.data1 = [x * 0.6 for x in self.data0]
            self.技能施放时间 = 1.5
            self.hit1 = 6
            self.CD *= 0.95
        elif 类型 == 1:
            self.data1 = [x * 0.82 for x in self.data0]
            self.技能施放时间 = 1.5
            self.hit1 = 6
            self.CD *= 0.95


class 技能17(被动技能):
    名称 = '制空掌握'
    所在等级 = 75
    等级上限 = 30
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 3)


class 技能18(职业主动技能):
    def __init__(self):
        super().__init__('开火')

    脱手 = 0
    技能施放时间 = 1
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.data0 = [x * 1.35 for x in self.data0]


class 技能19(职业主动技能):
    def __init__(self):
        super().__init__('G96热压手雷')

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.data0 = [x * 1.29 for x in self.data0]
            self.CD *= 0.9


class 技能20(职业主动技能):
    def __init__(self):
        super().__init__('决战之日')
    技能施放时间 = 5


class 技能21(被动技能):
    名称 = '单兵推进器-02X'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能22(职业主动技能):
    def __init__(self):
        super().__init__('空袭战略')
    持续时间 = 6


class 技能23(职业主动技能):
    def __init__(self):
        super().__init__('终解·制空霸权')

    关联技能 = ['无']
    脱手 = 0
    技能施放时间 = 6.8

    def 加成倍率(self, 武器类型):
        return 0.0


技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能' + str(i) + '())')
        i += 1
    except:
        i = -1


class 职业属性(角色属性):
    实际名称 = '重霄·弹药专家·女'
    角色 = '神枪手(女)'
    职业 = '弹药专家'

    武器选项 = ['手弩', '步枪']

    类型选择 = ['魔法固伤', '物理固伤']

    类型 = '魔法固伤'
    防具类型 = '皮甲'
    防具精通属性 = ['智力', '力量']

    超负荷属性 = 0

    主BUFF = 1.84

    远古记忆 = 0

    打桩模式 = 0

    补给输出形态选择 = 0

    # 守门人四属强 = [0,0,0,0]

    def __init__(self, 技能列表, 技能序号):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 技能释放次数计算(self):
        技能释放次数 = []
        技能消耗时间 = 0.0
        爆裂弹间隔 = 0.115
        每轮空射次数 = 12 + floor(0.5 * min(self.技能栏[self.技能序号['单兵推进器']].等级, 20))
        每轮时间 = 爆裂弹间隔 * 每轮空射次数 + 1.05
        # 最大不脱手时间 = 0.0

        反应时间 = 0.0
        释放时间系数 = 0.0
        起落地时间 = 0.0
        CD延迟 = 0.0

        if(self.打桩模式 == 0):
            反应时间 = 1.5
            释放时间系数 = 1.0
            起落地时间 = 1.5
            CD延迟 = 0.0

        elif(self.打桩模式 == 1):
            反应时间 = 0.0
            释放时间系数 = 0.0
            起落地时间 = 1.0
            CD延迟 = 0.0

        elif(self.打桩模式 == 2):
            反应时间 = 3.0
            释放时间系数 = 2.0
            起落地时间 = 3.0
            CD延迟 = 2.0

        if (self.武器类型 != '手弩'):
            爆裂弹间隔 = 0.14
            每轮空射次数 = 4 + floor(0.5 * min(self.技能栏[self.技能序号['单兵推进器']].等级, 20))
            每轮时间 = 爆裂弹间隔 * 每轮空射次数 + 起落地时间

        爆裂弹位置 = self.技能序号['爆裂弹']

        最大不脱手时间 = 0
        for i in self.技能栏:
            if i.是否有伤害 == 1 and i.脱手 != 1 and i.技能施放时间 > 最大不脱手时间 and self.次数输入[self.技能序号[i.名称]]:
                最大不脱手时间 = i.技能施放时间 + 0.5
        # print(最大不脱手时间)

        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if i.名称 == '爆裂弹':
                    技能释放次数.append(0)
                else:
                    if self.次数输入[self.技能序号[i.名称]] == '/CD':
                        # 根据技能CD及最大不脱手时间得到技能空转的时间
                        最终CD = i.等效CD(self.武器类型, self.类型)
                        空转时间 = 0
                        if 最终CD < 最大不脱手时间:
                            空转时间 = 最大不脱手时间 - 最终CD
                        # 计算不脱手时间
                        # 技能无法释放次数 = int(最大不脱手时间/(i.等效CD(self.武器类型,self.类型)))
                        # print(技能无法释放次数)
                        # print(最大不脱手时间)
                        # print(int((self.时间输入 - 反应时间-最大不脱手时间) / (i.等效CD(self.武器类型,self.类型) + i.技能施放时间*释放时间系数 + CD延迟) + 1 + i.基础释放次数))
                        # print(技能无法释放次数)
                        技能次数 = max(0, int((self.时间输入 - 反应时间 - 空转时间) /
                                   (最终CD + i.技能施放时间*释放时间系数 + CD延迟) + 1 + i.基础释放次数))
                        技能释放次数.append(技能次数)
                        # 技能释放次数.append(int((self.时间输入 - 反应时间) / (i.等效CD(self.武器类型) + i.技能施放时间*释放时间系数 + CD延迟) + 1 + i.基础释放次数))
                        if i.脱手 == 1:
                            技能消耗时间 += 技能次数 * 0.12 * 释放时间系数
                        else:
                            技能消耗时间 += 技能次数 * i.技能施放时间*释放时间系数
                    elif self.次数输入[self.技能序号[i.名称]] != '0':
                        技能释放次数.append(
                            round(float(self.次数输入[self.技能序号[i.名称]]), 2))
                        if i.脱手 == 1:
                            技能消耗时间 += int(self.次数输入[self.技能序号[i.名称]]
                                          ) * 0.12 * 释放时间系数
                        else:
                            技能消耗时间 += int(self.次数输入[self.技能序号[i.名称]]
                                          ) * i.技能施放时间 * 释放时间系数
                    else:
                        技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        # 填补补给占用时间，补给期间选择丢雷暂时不考虑空射
        # 追加补给选择丢雷对子弹的输出时间的影响
        # 技能消耗时间 += self.技能栏[self.技能序号['空袭战略']].持续时间() if self.补给输出形态选择 == 0 else 0
        # print(补给占用时间)
        if self.次数输入[self.技能序号['爆裂弹']] == '/CD':
            技能释放次数[爆裂弹位置] = max(
                int(floor((self.时间输入 - 技能消耗时间) / 每轮时间) * 每轮空射次数), 0)
            技能释放次数[爆裂弹位置] += max(floor((self.时间输入 - 技能消耗时间 - 每轮时间 *
                                 floor((self.时间输入 - 技能消耗时间) / 每轮时间) - 起落地时间/2) / 爆裂弹间隔), 0)
        else:
            技能释放次数[爆裂弹位置] = int(self.次数输入[self.技能序号['爆裂弹']] * 每轮空射次数)
        return 技能释放次数

    def 预处理(self):
        if self.超负荷属性 == 0:
            self.技能栏[self.技能序号['弹药改良']].加成数值 = 1.1
            self.技能栏[self.技能序号['弹药改良']].自定义描述 = 0
        if self.超负荷属性 == 1:
            self.技能栏[self.技能序号['弹药改良']].技能加成描述 = '火属性强化增加：36'
            self.火属性强化 += 36
        if self.超负荷属性 == 2:
            self.技能栏[self.技能序号['弹药改良']].技能加成描述 = '冰属性强化增加：36'
            self.冰属性强化 += 36
        if self.超负荷属性 == 3:
            self.技能栏[self.技能序号['弹药改良']].技能加成描述 = '光属性强化增加：36'
            self.光属性强化 += 36
        super().预处理()


class 重霄·弹药专家·女(角色窗口):
    def 窗口属性输入(self):
        技能序号 = dict()
        for i in range(len(技能列表)):
            技能序号[技能列表[i].名称] = i

        一觉序号 = 0
        二觉序号 = 0
        三觉序号 = 0

        for i in 技能列表:
            if i.所在等级 == 50:
                一觉序号 = 技能序号[i.名称]
            if i.所在等级 == 85:
                二觉序号 = 技能序号[i.名称]
            if i.所在等级 == 100:
                三觉序号 = 技能序号[i.名称]

        护石选项 = ['无']
        for i in 技能列表:
            if i.是否有伤害 == 1 and i.是否有护石 == 1:
                护石选项.append(i.名称)

        符文选项 = ['无']
        for i in 技能列表:
            if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1 and i.名称 != '爆裂弹':
                符文选项.append(i.名称)
        self.初始属性 = 职业属性(技能列表, 技能序号)
        self.角色属性A = 职业属性(技能列表, 技能序号)
        self.角色属性B = 职业属性(技能列表, 技能序号)
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)

    def 界面2(self):
        super().界面2()

        self.超负荷属性选择 = MyQComboBox(self.main_frame2)
        self.超负荷属性选择.addItems(['超负荷装填：无', '超负荷装填：火', '超负荷装填：冰', '超负荷装填：光'])
        self.超负荷属性选择.resize(120, 20)
        self.超负荷属性选择.move(325, 420)

        # self.补给输出形态选择=MyQComboBox(self.main_frame2)
        # self.补给输出形态选择.addItems(['输出丢雷','爆发丢技能'])
        # self.补给输出形态选择.resize(120,20)
        # self.补给输出形态选择.move(325,450)

        self.打桩模式 = MyQComboBox(self.main_frame2)
        y = QLabel("打桩模式：", self.main_frame2)
        y.move(500, self.height() - 63)
        y.resize(70, 20)
        y.setStyleSheet(标签样式)
        self.打桩模式.addItems(['常规打桩', '桩逼模式', '手残模式'])
        self.打桩模式.move(570, self.height() - 63)
        self.打桩模式.resize(80, 20)

        self.职业存档.append(('超负荷属性选择', self.超负荷属性选择, 1))
        self.职业存档.append(('打桩模式', self.打桩模式, 1))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        属性.打桩模式 = self.打桩模式.currentIndex()
        属性.超负荷属性 = self.超负荷属性选择.currentIndex()
        # 属性.补给输出形态选择 = self.补给输出形态选择.currentIndex()
