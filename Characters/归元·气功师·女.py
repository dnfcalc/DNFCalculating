from math import *
from PublicReference.base import *


# 武器手套
# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '手套':
#             return round(self.CD / self.恢复 * 1.05, 1)


# 蓄念炮
class 归元·气功师·女技能0(被动技能):
    名称 = '蓄念炮'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    # 基础 = 226
    # 成长 = 5
    关联技能 = ['念气波蓄念炮']

    def 加成倍率(self, 武器类型):
        return round(2.26 + 0.05 * self.等级, 5)


# 分身
class 归元·气功师·女技能1(主动技能):
    名称 = '分身'
    所在等级 = 5
    等级上限 = 20
    基础等级 = 10
    基础个数 = 0
    是否有伤害 = 0
    TP上限 = 0
    关联技能 = ['幻影爆碎']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return round(self.基础个数 + self.等级, 5)


# 一觉被动
class 归元·气功师·女技能2(被动技能):
    名称 = '乱舞千叶花'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.15 + 0.01 * self.等级, 5)

# 二觉被动


class 归元·气功师·女技能3(被动技能):
    名称 = '心之念意'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.03 * self.等级, 5)


# 念气归元
class 归元·气功师·女技能4(被动技能):
    名称 = '念气归元'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 分身0.01 最后被动倍率=幻爆百分比*100
class 归元·气功师·女技能5(主动技能):
    名称 = '幻影爆碎'
    是否主动 = 0
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 386.6
    成长 = 43.8
    CD = 12
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.基础 + self.成长 * self.等级, 5)

    # def 等效CD(self, 武器类型):
    #     if 武器类型 == '手套':
    #         return round(self.CD * 1.05, 1)


# 念气波
class 归元·气功师·女技能6(主动技能):
    名称 = '念气波'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 593
    成长 = 66.8
    CD = 1
    TP成长 = 0.08
    TP上限 = 5


# 念气波蓄念炮
class 归元·气功师·女技能7(主动技能):
    名称 = '念气波蓄念炮'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 593
    成长 = 66.8
    CD = 3
    TP成长 = 0.08
    TP上限 = 5


# 念气环绕
class 归元·气功师·女技能8(主动技能):
    名称 = '念气环绕'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    基础 = 322
    成长 = 36.5
    CD = 0.5
    TP成长 = 0.10
    TP上限 = 5
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03 + 0.02 * self.等级, 3)

# 念兽龙虎啸


class 归元·气功师·女技能9(主动技能):
    名称 = '念兽龙虎啸'
    所在等级 = 40
    等级上限 = 30
    基础等级 = 20
    基础 = 732
    成长 = 0
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 <= 19:
            return round(1.03 + 0.01 * self.等级, 5)
        else:
            return round(0.84 + 0.02 * self.等级, 5)


class 归元·气功师·女技能10(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['念兽龙虎啸']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

# 气玉弹


class 归元·气功师·女技能11(主动技能):
    名称 = '气玉弹'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2876.5
    成长 = 323.5
    CD = 8
    TP成长 = 0.08
    TP上限 = 5

# 狮子吼


class 归元·气功师·女技能12(主动技能):
    名称 = '狮子吼'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 5659.1
    成长 = 638.9
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27
        elif x == 1:
            self.倍率 *= 1.27 + 0.09


# 螺旋念气场
class 归元·气功师·女技能13(主动技能):
    名称 = '螺旋念气场'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 9336.7
    成长 = 1051.3
    # 实际CD为20秒
    演出时间 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.13
        elif x == 1:
            self.倍率 *= 1.13 + 0.09


# 念兽雷龙出海
class 归元·气功师·女技能14(主动技能):
    名称 = '念兽雷龙出海'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 20572
    成长 = 2361
    攻击次数 = 1
    # 秒C
    基础2 = 15427
    成长2 = 1770.5
    攻击次数2 = 0

    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.13
        elif x == 1:
            self.倍率 *= 1.13 + 0.09


# 一觉
class 归元·气功师·女技能15(主动技能):
    名称 = '千莲怒放'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 34236
    成长 = 10337
    CD = 145


# 奔雷掌
class 归元·气功师·女技能16(主动技能):
    名称 = '奔雷掌'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 14808.2
    成长 = 1671.8
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20006759886
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.28807255611
            self.CD *= 0.90

# 狂狮怒吼


class 归元·气功师·女技能17(主动技能):
    名称 = '狂狮怒吼'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 17450.5
    成长 = 1969.5
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.188
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.254
            self.CD *= 0.90

# 奇袭幻影


class 归元·气功师·女技能18(主动技能):
    名称 = '奇袭幻影'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 38967.3
    成长 = 4400.7
    CD = 40
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.33


# 聚能念气炮
class 归元·气功师·女技能19(主动技能):
    名称 = '聚能念气炮'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 47986.6
    成长 = 5418.3
    CD = 45
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.26


# 二觉
class 归元·气功师·女技能20(主动技能):
    名称 = '念帝旋天破'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 91535
    成长 = 27634
    CD = 180

# 天雷分身步


class 归元·气功师·女技能21(主动技能):
    名称 = '天雷分身步'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    # 🐎测试9hit,游戏写的10hit
    基础 = 71859.4
    成长 = 8113.6
    倍率 = 1.10  # 加强
    CD = 60.0

# 三觉


class 归元·气功师·女技能22(主动技能):
    名称 = '念印幻流破'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 229668
    成长 = 69341
    倍率 = 1.08  # 加强
    CD = 290.0
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0


归元·气功师·女技能列表 = []
i = 0
while i >= 0:
    try:
        exec('归元·气功师·女技能列表.append(归元·气功师·女技能' + str(i) + '())')
        i += 1
    except:
        i = -1

归元·气功师·女技能序号 = dict()
for i in range(len(归元·气功师·女技能列表)):
    归元·气功师·女技能序号[归元·气功师·女技能列表[i].名称] = i

归元·气功师·女一觉序号 = 0
归元·气功师·女二觉序号 = 0
归元·气功师·女三觉序号 = 0
for i in 归元·气功师·女技能列表:
    if i.所在等级 == 50:
        归元·气功师·女一觉序号 = 归元·气功师·女技能序号[i.名称]
    if i.所在等级 == 85:
        归元·气功师·女二觉序号 = 归元·气功师·女技能序号[i.名称]
    if i.所在等级 == 100:
        归元·气功师·女三觉序号 = 归元·气功师·女技能序号[i.名称]

归元·气功师·女护石选项 = ['无']
for i in 归元·气功师·女技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元·气功师·女护石选项.append(i.名称)

归元·气功师·女符文选项 = ['无']
for i in 归元·气功师·女技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元·气功师·女符文选项.append(i.名称)


class 归元·气功师·女角色属性(角色属性):
    实际名称 = '归元·气功师·女'
    角色 = '格斗家(女)'
    职业 = '气功师'

    武器选项 = ['手套']

    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.57
    BUFF属强 = 86

    远古记忆 = 0

    # 1 秒C
    雷龙开关 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(归元·气功师·女技能列表)
        self.技能序号 = deepcopy(归元·气功师·女技能序号)

    def 被动倍率计算(self):
        self.技能栏[self.技能序号['分身']].基础个数 = self.技能栏[self.技能序号['幻影爆碎']].TP等级

        self.技能栏[self.技能序号['念兽雷龙出海']].攻击次数 = (1 - self.雷龙开关)
        self.技能栏[self.技能序号['念兽雷龙出海']].攻击次数2 = self.雷龙开关

        if self.装备检查('拥抱晨曦之温暖') or self.装备检查('融化黑暗之温暖'):
            self.技能栏[self.技能序号['幻影爆碎']].恢复 -= 0.3

        super().被动倍率计算()

    def 伤害指数计算(self):
        self.光属性强化 += self.BUFF属强
        super().伤害指数计算()


class 归元·气功师·女(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 归元·气功师·女角色属性()
        self.角色属性A = 归元·气功师·女角色属性()
        self.角色属性B = 归元·气功师·女角色属性()
        self.一觉序号 = 归元·气功师·女一觉序号
        self.二觉序号 = 归元·气功师·女二觉序号
        self.三觉序号 = 归元·气功师·女三觉序号
        self.护石选项 = deepcopy(归元·气功师·女护石选项)
        self.符文选项 = deepcopy(归元·气功师·女符文选项)

    def 界面(self):
        super().界面()

        self.BUFF.move(self.BUFF.x() - 18, self.BUFF.y())
        self.BUFF输入.move(self.BUFF输入.x() - 20, self.BUFF输入.y())
        self.BUFF输入.resize(40, 25)

        self.BUFF输入2 = QLineEdit(self.main_frame2)
        self.BUFF输入2.setText(str(self.初始属性.BUFF属强))
        self.BUFF输入2.resize(40, 25)
        self.BUFF输入2.move(self.BUFF输入.x() + 45, self.BUFF输入.y())
        self.BUFF输入2.setStyleSheet(输入框样式)
        self.BUFF输入2.setAlignment(Qt.AlignCenter)

        self.雷龙开关 = QCheckBox('雷龙出海秒C', self.main_frame2)
        self.雷龙开关.resize(100, 20)
        self.雷龙开关.move(335, 440)
        self.雷龙开关.setStyleSheet(复选框样式)
        self.雷龙开关.setChecked(True)

    def 载入配置(self, path='set'):
        super().载入配置(path)
        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' +
                           path + '/skill5.ini', 'r', encoding='utf-8').readlines()
            self.BUFF输入2.setText(str(setfile[0].replace('\n', '')))
            self.雷龙开关.setChecked(True if int(
                setfile[1].replace('\n', '')) == 1 else False)

        except:
            pass

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 +
                           '/' + path + '/skill5.ini', 'w', encoding='utf-8')
            setfile.write(self.BUFF输入2.text()+'\n')
            setfile.write('1\n' if self.雷龙开关.isChecked() else '0\n')
        except:
            pass

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        try:
            self.BUFF光强 = int(self.BUFF输入2.text())
        except:
            self.BUFF光强 = self.初始属性.BUFF属强

        属性.BUFF属强 = self.BUFF光强

        if self.雷龙开关.isChecked():
            属性.雷龙开关 = 1
