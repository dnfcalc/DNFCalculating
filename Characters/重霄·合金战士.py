from PublicReference.carry.base import *
from math import *

# 等级 = 100 + 5


# class 职业主动技能(主动技能):
#     技能施放时间 = 0.0
#     脱手 = 1
#     data0 = []
#     data1 = []
#     data2 = []
#     data3 = []

#     def 等效百分比(self, 武器类型):
#         等效倍率 = 0.0
#         if len(self.data0) >= self.等级 and len(self.data0) > 0:
#             等效倍率 += self.data0[self.等级] * self.攻击次数
#         if len(self.data1) >= self.等级 and len(self.data1) > 0:
#             等效倍率 += self.data1[self.等级] * self.攻击次数1
#         if len(self.data2) >= self.等级 and len(self.data2) > 0:
#             等效倍率 += self.data2[self.等级] * self.攻击次数2
#         if len(self.data3) >= self.等级 and len(self.data3) > 0:
#             等效倍率 += self.data3[self.等级] * self.攻击次数3
#         return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率
class 技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['瞄准射击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 技能1(主动技能):
    名称 = '超频：压制'
    所在等级 = 5
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础 = 1625 - 165
    成长 = 165
    攻击次数 = 1
    # 学习诺维尔计划：涅磐后减少1秒
    CD = 6.0 - 1
    TP成长 = 0.1
    TP上限 = 7

class 技能2(主动技能):
    名称 = '烟尘弹'
    所在等级 = 10
    等级上限 = 60
    学习间隔 = 2
    基础 = 409 - 42
    成长 = 42
    攻击次数 = 6
    CD = 6
    TP成长 = 0.08
    TP上限 = 7

class 技能3(被动技能):
    名称 = '合金战士自动手枪精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.02 * self.等级, 3)

class 技能4(主动技能):
    名称 = '瞄准射击'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    基础 = 130
    成长 = 0
    攻击次数 = 7
    CD = 3
    TP成长 = 0.10
    TP上限 = 3

class 技能5(被动技能):
    名称 = '弱点扫描'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 3)

class 技能6(主动技能):
    名称 = '枪托强击'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    基础 = 4221 - 428
    成长 = 428
    CD = 8
    TP成长 = 0.1
    TP上限 = 7

class 技能7(主动技能):
    名称 = '改装榴弹'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    基础 = 3132 - 317
    成长 = 317
    CD = 6
    TP成长 = 0.1
    TP上限 = 7

class 技能8(被动技能):
    名称 = '改造烟尘弹'
    所在等级 = 25
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['烟尘弹']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.2, 3)

class 技能9(主动技能):
    名称 = '超频：重盾保卫'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    基础 = 6470 - 656
    成长 = 656
    CD = 6
    TP成长 = 0.1
    TP上限 = 7

class 技能10(主动技能):
    名称 = '磁力手雷'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    基础 = 2011 - 204
    成长 = 204
    攻击次数 = 3
    CD = 12
    TP成长 = 0.1
    TP上限 = 7

class 技能11(主动技能):
    名称 = '三连霰弹'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    基础 = 1016 - 103
    成长 = 103
    攻击次数 = 1
    基础2 = 1524 - 155
    成长2 = 155
    攻击次数2 = 1
    基础3 = 2540 - 258
    成长3 = 258
    攻击次数3 = 1
    CD = 8
    TP成长 = 0.1
    TP上限 = 7

class 技能12(主动技能):
    名称 = '爆裂飞踢'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    基础 = 3233 - 328
    成长 = 328
    攻击次数 = 1
    基础2 = 1212 - 123
    成长2 = 123
    攻击次数2 = 4
    CD = 15
    TP成长 = 0.1
    TP上限 = 7

class 技能13(主动技能):
    名称 = '超频：机械冲撞'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    # 撞击
    基础 = 4707 - 478
    成长 = 478
    攻击次数 = 1
    # 炮
    基础2 = 3138 - 318
    成长2 = 318
    攻击次数2 = 1
    CD = 13
    TP成长 = 0.1
    TP上限 = 7

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.攻击次数2 = 0
            self.攻击次数 *= 1+1.28+0.17

class 技能14(主动技能):
    名称 = '战略轰炸'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    # 榴弹
    基础 = 1647 - 167
    成长 = 167
    攻击次数 = 3
    # 手榴弹
    基础2 = 2471 - 251
    成长2 = 251
    攻击次数2 = 3
    CD = 20
    TP成长 = 0.1
    TP上限 = 7

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.攻击次数 += 2
            self.基础 *= 0.83
            self.成长 *= 0.83
            self.基础2 *= 1.14
            self.成长2 *= 1.14
            self.CD *= 0.9

class 技能15(主动技能):
    名称 = '雷达扫射'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    基础 = 1446 - 147
    成长 = 147
    攻击次数 = 15
    CD = 40
    TP成长 = 0.1
    TP上限 = 7

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.攻击次数 *= 1+0.14+0.09
            self.CD *= 0.95

class 技能16(被动技能):
    名称 = '机体复原'
    所在等级 = 48
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 3)

class 技能17(主动技能):
    名称 = '电弧能量释放'
    所在等级 = 48
    等级上限 = 1
    基础等级 = 1
    基础 = 8816 - 1406
    成长 = 1406
    攻击次数 = 1
    CD = 1

class 技能18(主动技能):
    名称 = '超频：全领域攻击'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础 = 5230
    成长 = 1577
    攻击次数 = 1
    基础2 = 2613
    成长2 = 789
    攻击次数2 = 8
    基础3 = 26138
    成长3 = 7889
    攻击次数3 = 1
    CD = 145

class 技能19(主动技能):
    名称 = '超频：电流闪踢'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    基础 = 17383 - 1764
    成长 = 1764
    CD = 25
    TP成长 = 0.1
    TP上限 = 7

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.攻击次数 *= 1+0.15+0.07
            self.CD *= 0.9

class 技能20(主动技能):
    名称 = '堡垒轰击'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    基础 = 1314 - 133
    成长 = 133
    攻击次数 = 30
    CD = 50
    TP成长 = 0.1
    TP上限 = 7

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            # 变成充能类技能
            self.基础释放次数 = 2
            self.倍率 *= 1-0.43+0.06
            self.CD *= 0.5

class 技能21(主动技能):
    名称 = 'AT-SO步行者'
    备注 = '自动射击'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 2
    基础 = 1022 - 104
    成长 = 104
    攻击次数 = 28*4
    CD = 40
    CD_min = 20

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.CD_min = 30
            # 增加持续时间
            self.攻击次数 *=30/20
            # 自爆
            self.攻击次数 += 5.6


class 技能22(被动技能):
    名称 = '躯体重塑'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 3)

class 技能23(主动技能):
    名称 = '炎神攻城炮'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    精通等级 = 30
    基础 = 67684 - 6866
    成长 = 6866
    CD = 45

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.倍率 *=1.28
            self.CD *= 0.9

class 技能24(主动技能):
    名称 = '超频：伊奎利斯-MR'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础 = 7802 - 1809
    成长 = 1809
    攻击次数 = 20
    CD = 180

class 技能25(被动技能):
    名称 = '诺维尔计划：涅磐'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 技能26(主动技能):
    名称 = '超频：音速速杀'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 10

    CD = 60

    基础 = 6349 - 644
    成长 = 644
    攻击次数 = 4

    基础2 = 38097 - 3864
    成长2 = 3864
    攻击次数2 =1

    基础3 = 63495 - 6441
    成长3 = 6441
    攻击次数3 = 1

class 技能27(主动技能):
    名称 = '超频：末世终结之战'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30

    关联技能 = ['无']

    CD = 290.0
    # 战场脉冲+落地冲击波
    基础 = 41744 - 9679
    成长 = 9679
    攻击次数 = 2

    基础2 = 5218 - 1209
    成长2 = 1209
    攻击次数2 = 12

    基础3 = 20872 - 4839
    成长3 = 4839
    攻击次数3 = 3

    基础4 = 208720 - 48398
    成长4 = 48398
    攻击次数4 = 1

    def 加成倍率(self, 武器类型):
        return 0.0

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int(
                (self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 *
                 (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 *
                 (self.基础3 + self.成长3 * self.等级) + self.攻击次数4 *
                 (self.基础4 + self.成长4 * self.等级)) *
                (1 + self.TP成长 * self.TP等级) * self.倍率)

技能列表 = []
i = 0
while i >= 0:
    try:
        tem = eval('技能'+str(i)+'()')
        tem.基础等级计算()
        技能列表.append(tem)
        i += 1
    except:
        i = -1


class 职业属性(角色属性):
    实际名称 = '重霄·合金战士'
    角色 = '神枪手(男)'
    职业 = '合金战士'

    武器选项 = ['自动手枪']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 2

    def __init__(self, 技能列表, 技能序号):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['电弧能量释放']].等级 = self.技能栏[self.技能序号['机体复原']].等级

    def 武器基础(self):
        temp = equ.get_equ_by_name(self.装备栏[11])

        self.力量 += temp.力量
        self.智力 += temp.智力
        self.物理攻击力 += temp.魔法攻击力
        self.魔法攻击力 += temp.魔法攻击力
        self.独立攻击力 += temp.独立攻击力

        if temp.所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(temp.等级, temp.品质,
                               self.强化等级[11], self.武器类型, '魔法')
            self.魔法攻击力 += 武器计算(temp.等级, temp.品质,
                               self.强化等级[11], self.武器类型, '魔法')
            self.独立攻击力 += 锻造计算(temp.等级, temp.品质, self.武器锻造等级)

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                s = self.次数输入[self.技能序号[i.名称]]
                if '/CD' in s:
                    if i.名称 == 'AT-SO步行者':
                        if self.时间输入 >= i.CD_min:
                            技能释放次数.append( self.时间输入 / max(i.等效CD(self.武器类型, self.类型),i.CD_min))
                        else:
                            技能释放次数.append( self.时间输入 / i.CD_min )
                    else:
                        技能释放次数.append(
                        int((self.时间输入 - i.演出时间) /
                            i.等效CD(self.武器类型, self.类型)) + 1 + i.基础释放次数)
                else:
                    技能释放次数.append(round(float(s), 2))
            else:
                技能释放次数.append(0)

        return self.技能释放次数解析(技能释放次数)

class 重霄·合金战士(角色窗口):
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

