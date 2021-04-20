from math import *
from PublicReference.base import *


class 职业主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    data0 = []
    data1 = []
    data2 = []
    data3 = []

    攻击次数 = 1
    攻击次数1 = 0
    攻击次数2 = 0
    攻击次数3 = 0

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.data0) >= self.等级 and len(self.data0) > 0:
            等效倍率 += self.data0[self.等级] * self.攻击次数
        if len(self.data1) >= self.等级 and len(self.data1) > 0:
            等效倍率 += self.data1[self.等级] * self.攻击次数1
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.攻击次数2
        if len(self.data3) >= self.等级 and len(self.data3) > 0:
            等效倍率 += self.data3[self.等级] * self.攻击次数3
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能0(职业主动技能):
    名称 = '烈火燎原'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    data0 = [
        0, 10, 14, 18, 22, 26, 28, 32, 36, 40, 44, 48, 52, 55, 59, 63, 67, 71,
        75, 77, 81, 85, 89, 93, 97, 100, 104, 108, 112, 116, 120, 124, 126,
        130, 134, 138, 142, 145, 149, 153, 157, 161, 165, 169, 173, 175, 179,
        183, 187, 191, 194, 198, 202, 206, 210, 214, 218, 220, 224, 228, 232,
        236, 239, 243, 247, 251, 255, 259, 263, 267, 269
    ]
    攻击次数 = 1
    能量 = 140
    最小值 = 2
    CD = 5.0
    持续秒数 = 6.0
    TP成长 = 0.08
    TP上限 = 5
    硬直时长百分比 = 0

    def 觉醒模式(self, x):
        if x == 1:
            觉醒后能量消耗 = 70
            self.data0 = [int(x * 觉醒后能量消耗 / self.最小值) for x in self.data0]
            self.最小值 = 觉醒后能量消耗
            # self.基础 = self.基础 * 70 / 2
            # self.成长 = self.成长 * 70 / 2


class 技能1(职业主动技能):
    名称 = '炽炎星陨'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    data0 = [
        0, 99, 134, 170, 205, 239, 274, 310, 345, 380, 415, 449, 485, 520, 555,
        590, 624, 660, 695, 730, 765, 801, 836, 870, 905, 940, 976, 1011, 1045,
        1080, 1115, 1151, 1186, 1221, 1255, 1290, 1326, 1361, 1396, 1430, 1466,
        1501, 1536, 1571, 1606, 1642, 1676, 1711, 1746, 1781, 1817, 1851, 1886,
        1921, 1957, 1992, 2027, 2061, 2096, 2132, 2167, 2202, 2236, 2271, 2307,
        2342, 2377, 2411, 2446, 2482, 2517
    ]
    攻击次数 = 1
    能量 = 140
    最小值 = 20
    CD = 5.0
    持续秒数 = 1.0
    TP成长 = 0.08
    TP上限 = 5
    硬直时长百分比 = 0

    def 觉醒模式(self, x):
        if x == 1:
            觉醒后能量消耗 = 70
            self.data0 = [int(x * 觉醒后能量消耗 / self.最小值) for x in self.data0]
            self.最小值 = 觉醒后能量消耗


class 技能2(职业主动技能):
    名称 = '冰霜之球'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    data0 = [
        0, 70, 80, 90, 100, 111, 121, 131, 142, 152, 162, 173, 183, 193, 203,
        214, 224, 234, 245, 255, 265, 276, 286, 296, 306, 317, 327, 337, 348,
        358, 368, 379, 389, 399, 409, 420, 430, 440, 451, 461, 471, 482, 492,
        502, 512, 523, 533, 543, 554, 564, 574, 585, 595, 605, 615, 626, 636,
        646, 657, 667, 677, 688, 698, 708, 718, 729, 739, 749, 758, 769, 779
    ]
    攻击次数 = 6
    # 能量消耗值：20
    能量 = 140
    最小值 = 20
    CD = 10.0
    持续秒数 = 3.0
    TP成长 = 0.08
    TP上限 = 5
    硬直时长百分比 = 0

    def 觉醒模式(self, x):
        if x == 1:
            觉醒后能量消耗 = 70
            self.data0 = [int(x * 觉醒后能量消耗 / self.最小值) for x in self.data0]
            self.最小值 = 觉醒后能量消耗


class 技能3(职业主动技能):
    名称 = '冰天震地'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    # 冰盘攻击力：<data0>
    data0 = [
        0, 745, 854, 963, 1071, 1181, 1289, 1398, 1506, 1616, 1724, 1833, 1942,
        2051, 2159, 2269, 2377, 2486, 2594, 2704, 2812, 2920, 3029, 3138, 3247,
        3355, 3465, 3573, 3682, 3790, 3900, 4008, 4117, 4226, 4335, 4443, 4553,
        4661, 4770, 4878, 4988, 5096, 5205, 5314, 5423, 5531, 5641, 5749, 5858,
        5966, 6074, 6184, 6292, 6401, 6510, 6619, 6727, 6837, 6945, 7054, 7162,
        7272, 7380, 7489, 7598, 7707, 7815, 7925, 8033, 8142, 8250
    ]
    攻击次数 = 1
    # 能量消耗值：40
    能量 = 140
    最小值 = 40
    CD = 10.0
    持续秒数 = 1.0
    TP成长 = 0.08
    TP上限 = 5
    硬直时长百分比 = 0

    def 觉醒模式(self, x):
        if x == 1:
            觉醒后能量消耗 = 140
            self.data0 = [int(x * 觉醒后能量消耗 / self.最小值) for x in self.data0]
            self.最小值 = 觉醒后能量消耗


class 技能4(被动技能):
    名称 = '幻想之境'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1 + 0.01 * self.等级, 5)
        else:
            return round(1.1 + 0.015 * (self.等级 - 10), 5)

    def 独立攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class 技能5(被动技能):
    名称 = '具象强化'
    所在等级 = 25
    等级上限 = 40
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.025 * self.等级, 5)


class 技能6(职业主动技能):
    名称 = '烈焰飓风'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 烈焰飓风攻击力：<data0>
    data0 = [
        0, 415, 457, 500, 542, 583, 626, 668, 711, 752, 794, 837, 879, 922,
        963, 1006, 1048, 1091, 1132, 1174, 1217, 1259, 1300, 1343, 1385, 1428,
        1469, 1512, 1554, 1597, 1638, 1680, 1723, 1765, 1806, 1849, 1891, 1934,
        1976, 2018, 2060, 2102, 2145, 2186, 2229, 2271, 2314, 2355, 2397, 2440,
        2482, 2524, 2566, 2608, 2651, 2692, 2735, 2777, 2820, 2861, 2903, 2946,
        2988, 3031, 3072, 3114, 3157, 3199, 3241, 3283, 3326
    ]
    攻击次数 = 12
    # 烈焰飓风持续时间：3秒
    # 能量消耗值：60
    能量 = 140
    最小值 = 60
    CD = 20
    持续秒数 = 4.0
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0.05
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.倍率 *= 1.0
        elif x == 1:
            self.CD *= 0.85
            self.倍率 *= 1.09


class 技能7(职业主动技能):
    名称 = '极冰护盾'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data0 = [
        0, 2579, 2840, 3102, 3363, 3626, 3887, 4148, 4410, 4672, 4934, 5195,
        5456, 5718, 5980, 6242, 6503, 6765, 7027, 7289, 7550, 7811, 8074, 8335,
        8597, 8858, 9119, 9382, 9643, 9905, 10166, 10429, 10690, 10951, 11213,
        11474, 11737, 11998, 12260, 12521, 12784, 13045, 13306, 13568, 13830,
        14092, 14353, 14614, 14876, 15138, 15400, 15661, 15923, 16185, 16447,
        16708, 16969, 17231, 17493, 17755, 18016, 18277, 18540, 18801, 19063,
        19324, 19587, 19848, 20109, 20371, 20632
    ]
    攻击次数 = 1

    CD = 20.0
    持续秒数 = 1.0
    能量 = 140
    最小值 = 60
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0.1


class 技能8(职业主动技能):
    名称 = '超能旋风波'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data0 = [
        0, 341, 376, 409, 444, 479, 514, 548, 583, 618, 653, 688, 721, 756,
        791, 825, 860, 895, 930, 964, 999, 1034, 1067, 1102, 1137, 1172, 1206,
        1241, 1276, 1311, 1345, 1379, 1414, 1448, 1483, 1518, 1553, 1587, 1622,
        1657, 1692, 1725, 1760, 1795, 1830, 1864, 1899, 1934, 1969, 2003, 2037,
        2072, 2106, 2141, 2176, 2211, 2245, 2280, 2315, 2350, 2383, 2418, 2453,
        2487, 2522, 2557, 2592, 2627, 2661, 2695, 2730
    ]
    攻击次数 = 1
    CD = 25.0
    持续秒数 = 5.0
    能量 = 140
    最小值 = 4
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.32

    def 觉醒模式(self, x):
        if x == 1:
            觉醒后能量消耗 = 46
            self.data0 = [int(x * 觉醒后能量消耗 / self.最小值) for x in self.data0]
            self.最小值 = 觉醒后能量消耗


class 技能9(职业主动技能):
    名称 = '风暴漩涡'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data0 = [
        0, 1432, 1577, 1723, 1868, 2014, 2159, 2305, 2450, 2596, 2741, 2887,
        3032, 3176, 3322, 3467, 3613, 3758, 3904, 4049, 4195, 4340, 4486, 4631,
        4775, 4921, 5066, 5212, 5357, 5503, 5648, 5794, 5939, 6085, 6230, 6376,
        6520, 6665, 6811, 6956, 7102, 7247, 7393, 7538, 7684, 7829, 7975, 8119,
        8264, 8410, 8555, 8701, 8846, 8992, 9137, 9283, 9428, 9574, 9719, 9864,
        10009, 10155, 10300, 10445, 10591, 10736, 10882, 11027, 11173, 11318,
        11463
    ]
    攻击次数 = 1

    能量 = 140
    最小值 = 20
    CD = 25.0
    持续秒数 = 5.0
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.倍率 *= 1.22

    def 觉醒模式(self, x):
        if x == 1:
            觉醒后能量消耗 = 70
            self.data0 = [int(x * 觉醒后能量消耗 / self.最小值) for x in self.data0]
            self.最小值 = 觉醒后能量消耗


class 技能10(被动技能):
    名称 = '洞悉'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class 技能11(职业主动技能):
    名称 = '末日虫洞'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 19
    # 行星碎片攻击力：<data0>
    data0 = [
        0, 200, 232, 264, 296, 328, 361, 393, 424, 456, 488, 520, 552, 585,
        617, 648, 680, 712, 744, 776, 809, 841, 872, 904, 936, 968, 1000, 1033,
        1065, 1096, 1128, 1160, 1192, 1224, 1257, 1289, 1320, 1352, 1384, 1416,
        1448, 1481, 1513, 1544, 1576, 1608, 1640, 1672, 1705, 1737, 1768, 1800,
        1832, 1864, 1896, 1929, 1961, 1992, 2024, 2056, 2088, 2121, 2153, 2185,
        2216, 2248, 2280, 2312, 2345, 2377, 2409
    ]
    # 虫洞大爆炸攻击力：<data1>
    data1 = [
        0, 9789, 11351, 12911, 14472, 16032, 17594, 19154, 20715, 22275, 23835,
        25397, 26958, 28518, 30079, 31639, 33201, 34761, 36322, 37882, 39444,
        41004, 42565, 44125, 45686, 47247, 48808, 50368, 51929, 53490, 55051,
        56611, 58172, 59732, 61294, 62854, 64415, 65975, 67537, 69098, 70658,
        72218, 73779, 75341, 76901, 78462, 80022, 81582, 83144, 84705, 86265,
        87826, 89387, 90948, 92508, 94069, 95629, 97191, 98751, 100312, 101872,
        103434, 104994, 106555, 108115, 109676, 111237, 112798, 114358, 115919,
        117481
    ]

    攻击次数 = 19
    攻击次数1 = 1

    CD = 45.0
    持续秒数 = 3.0
    能量 = 100
    最小值 = 100
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
        elif x == 1:
            self.倍率 *= 1.28


class 技能12(职业主动技能):
    名称 = '冰雪降临'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 16
    data0 = [
        int(1.2 * x) for x in [
            0, 573, 664, 754, 846, 937, 1029, 1120, 1212, 1303, 1394, 1486,
            1577, 1669, 1760, 1851, 1943, 2034, 2126, 2217, 2308, 2400, 2491,
            2581, 2673, 2764, 2856, 2947, 3039, 3130, 3221, 3313, 3404, 3496,
            3587, 3678, 3770, 3861, 3953, 4044, 4135, 4227, 4318, 4410, 4500,
            4591, 4683, 4774, 4865, 4957, 5048, 5140, 5231, 5323, 5414, 5505,
            5597, 5688, 5780, 5871, 5962, 6054, 6145, 6237, 6327, 6418, 6510,
            6601, 6692, 6784, 6875
        ]
    ]
    攻击次数 = 21
    CD = 31.5
    持续秒数 = 3.0
    能量 = 100
    最小值 = 50
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            能量消耗 = 2
            self.data0 = [int(x * 能量消耗 / self.最小值) for x in self.data0]
            self.最小值 = 能量消耗
            self.倍率 *= 1.28
            self.持续秒数 = 0.5
            self.硬直时长百分比 = 0.15
        elif x == 1:
            能量消耗 = 2
            self.data0 = [int(x * 能量消耗 / self.最小值) for x in self.data0]
            self.最小值 = 能量消耗
            self.倍率 *= 1.37
            self.持续秒数 = 0.5
            self.硬直时长百分比 = 0.15


class 技能13(职业主动技能):
    名称 = '时空链接'
    所在等级 = 70
    等级上限 = 60
    基础等级 = 18
    data0 = [
        0, 823, 906, 990, 1074, 1156, 1240, 1324, 1407, 1491, 1575, 1658, 1742,
        1824, 1908, 1992, 2075, 2159, 2243, 2327, 2409, 2493, 2576, 2660, 2744,
        2827, 2911, 2995, 3077, 3161, 3245, 3328, 3412, 3496, 3579, 3663, 3745,
        3829, 3913, 3996, 4080, 4164, 4247, 4331, 4414, 4497, 4581, 4665, 4748,
        4832, 4916, 4998, 5082, 5165, 5249, 5333, 5417, 5500, 5584, 5666, 5750,
        5834, 5917, 6001, 6085, 6168, 6252, 6335, 6418, 6502, 6586
    ]
    攻击次数 = 34
    CD = 54
    持续秒数 = 5.0
    能量 = 100
    最小值 = 50
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0.05
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24

        elif x == 1:
            self.倍率 *= 1.32


class 技能14(被动技能):
    名称 = '创世之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能15(职业主动技能):
    名称 = '时空禁制'
    所在等级 = 80
    等级上限 = 60
    基础等级 = 9
    # 多段攻击力：<data0>
    data0 = [
        0, 706, 818, 931, 1043, 1156, 1268, 1380, 1494, 1606, 1719, 1831, 1944,
        2056, 2168, 2281, 2393, 2507, 2619, 2732, 2844, 2956, 3069, 3181, 3295,
        3407, 3520, 3632, 3744, 3857, 3969, 4083, 4195, 4308, 4420, 4532, 4645,
        4757, 4871, 4983, 5096, 5208, 5320, 5433, 5545, 5659, 5771, 5884, 5996,
        6108, 6221, 6333, 6447, 6559, 6672, 6784, 6896, 7009, 7121, 7234, 7346,
        7460, 7572, 7684, 7797, 7909, 8022, 8134, 8248, 8360, 8472
    ]
    # 最后一击爆炸攻击力：<data1>
    data1 = [
        0, 21182, 24559, 27936, 31312, 34689, 38066, 41443, 44820, 48198,
        51575, 54951, 58328, 61705, 65082, 68459, 71836, 75212, 78589, 81966,
        85343, 88720, 92097, 95475, 98850, 102228, 105605, 108982, 112359,
        115736, 119113, 122489, 125866, 129243, 132620, 135997, 139374, 142750,
        146127, 149505, 152882, 156259, 159636, 163013, 166389, 169766, 173143,
        176520, 179897, 183274, 186650, 190027, 193404, 196782, 200159, 203536,
        206913, 210289, 213666, 217043, 220420, 223797, 227174, 230550, 233927,
        237304, 240681, 244059, 247436, 250813, 254189
    ]
    攻击次数 = 30
    攻击次数1 = 1

    CD = 45.0
    持续秒数 = 7.0
    能量 = 100
    最小值 = 100
    硬直时长百分比 = 0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.5 * 2.74


class 技能16(职业主动技能):
    名称 = '创世'
    备注 = '(直接爆炸)'
    所在等级 = 85
    等级上限 = 60
    基础等级 = 5
    #    基础 = 84924.00
    #    成长 = 25632.0
    data0 = [
        0, 18425, 22697, 26969, 31242, 35514, 39788, 44060, 48333, 52605,
        56878, 61150, 65423, 69695, 73968, 78240, 82513, 86785, 91058, 95330,
        99604, 103876, 108149, 112421, 116694, 120966, 125239, 129511, 133784,
        138056, 142329, 146601, 150874, 155146, 159420, 163691, 167965, 172237,
        176510, 180782, 185055, 189327, 193600, 197872, 202145, 206417, 210690,
        214962, 219236, 223507, 227781, 232053, 236326, 240598, 244871, 249143,
        253416, 257688, 261961, 266233, 270506, 274778, 279051, 283323, 287597,
        291869, 296142, 300414, 304687, 308959, 313232
    ]
    攻击次数 = 6
    CD = 180.0
    持续秒数 = 1
    能量 = 100
    最小值 = 100
    硬直时长百分比 = 0


class 技能17(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能18(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class 技能19(被动技能):
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


class 技能20(被动技能):
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


技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能' + str(i) + '())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

缔造者一觉序号 = 16
缔造者二觉序号 = 16
缔造者三觉序号 = 19

缔造者护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        缔造者护石选项.append(i.名称)

缔造者符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 1 and i.所在等级 <= 75 and i.是否有伤害 == 1:
        缔造者符文选项.append(i.名称)


class 缔造者角色属性(角色属性):
    实际名称 = '缔造者'
    角色 = '缔造者'
    职业 = '缔造者'

    武器选项 = ['魔杖', '法杖', '棍棒', '矛', '扫把']

    类型选择 = ['魔法固伤']

    类型 = '魔法固伤'
    防具类型 = '板甲'
    防具精通属性 = ['智力']

    主BUFF = 1.66

    远古记忆 = 0

    数据精算模式 = 0
    觉醒模式 = 1

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 技能等级加成(self, 加成类型, minLv, maxLv, lv, 可变=0):
        lv = int(lv)

        if self.装备描述 == 1:
            if 加成类型 == "所有":
                if minLv == maxLv:
                    return "Lv{} 技能等级+{}<br>".format(minLv, lv)
                else:
                    return "Lv{}-{} 技能等级+{}<br>".format(minLv, maxLv, lv)
            else:
                if minLv == maxLv:
                    return "Lv{} 主动技能等级+{}<br>".format(minLv, lv)
                else:
                    return "Lv{}-{} 主动技能等级+{}<br>".format(minLv, maxLv, lv)
        else:
            if self.远古记忆 > 0:
                if minLv <= 15 and maxLv >= 15:
                    self.远古记忆 = min(20, self.远古记忆 + lv)

            for i in self.技能栏:
                if i.所在等级 >= minLv and i.所在等级 <= maxLv:
                    if 加成类型 == '所有':
                        i.等级加成(lv)
            if 可变 > 0:
                self.变换词条[可变 - 1] = [
                    6, 2, 14 + (2 if 可变 > 1 else 4), 14 + (9 if 可变 > 1 else 17)
                ]
        return ''

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            modelchange = '觉醒模式' in dir(i)
            if modelchange and self.觉醒模式 == 1:
                #                print('hello')
                i.觉醒模式(1)
            if i.是否有伤害 == 1:
                if self.次数输入[self.技能序号[i.名称]] == '/CD':

                    余数伤害时间 = (
                        (int(i.能量 *
                             (1 +
                              (self.时间输入 *
                               (1 - i.硬直时长百分比)) / i.等效CD(self.武器类型, self.类型)))
                         - int(
                             int(i.能量 *
                                 (1 +
                                  (self.时间输入) / i.等效CD(self.武器类型, self.类型))) /
                             i.最小值) * i.最小值) / i.能量) * i.等效CD(
                                 self.武器类型, self.类型)
                    余数次数 = 0
                    if 余数伤害时间 < i.持续秒数:
                        if 余数伤害时间 < 0.5:
                            余数次数 = -1
                        else:
                            余数次数 = -1 + 余数伤害时间 / i.持续秒数
                    else:
                        余数次数 = 0
                    if self.数据精算模式 == 1 and self.时间输入 != 1:

                        技能释放次数.append(
                            round(
                                int(
                                    int(i.能量 *
                                        (1 + (self.时间输入 * (1 - i.硬直时长百分比)) /
                                         i.等效CD(self.武器类型, self.类型))) / i.最小值)
                                + 余数次数, 2))
                    else:
                        余数次数 = 0
                        技能释放次数.append(
                            round(
                                int(
                                    int(i.能量 *
                                        (1 + (self.时间输入 * (1 - i.硬直时长百分比)) /
                                         i.等效CD(self.武器类型, self.类型))) / i.最小值)
                                + 余数次数, 2))

                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(round(float(self.次数输入[self.技能序号[i.名称]]), 2))
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
        self.数据精算模式 = QCheckBox('数据精算模式', self.main_frame2)
        self.数据精算模式.resize(100, 20)
        self.数据精算模式.move(335, 490)
        self.数据精算模式.setStyleSheet(复选框样式)
        self.数据精算模式.setChecked(True)

        self.觉醒模式 = QCheckBox('觉醒模式', self.main_frame2)
        self.觉醒模式.resize(100, 20)
        self.觉醒模式.move(335, 520)
        self.觉醒模式.setStyleSheet(复选框样式)
        self.觉醒模式.setChecked(True)

    def 载入配置(self, path='set'):
        super().载入配置(path)
        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/skill5.ini',
                           'r',
                           encoding='utf-8').readlines()
            self.数据精算模式.setChecked(True if int(setfile[0].replace('\n', '')) ==
                                   1 else False)
            self.觉醒模式.setChecked(True if int(setfile[1].replace('\n', '')) ==
                                 1 else False)
        except:
            pass

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/skill5.ini',
                           'w',
                           encoding='utf-8')
            setfile.write('1\n' if self.数据精算模式.isChecked() else '0\n')
            setfile.write('1\n' if self.觉醒模式.isChecked() else '0\n')
        except:
            pass

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.数据精算模式.isChecked():
            属性.数据精算模式 = 1
        else:
            属性.数据精算模式 = 0

        if self.觉醒模式.isChecked():
            属性.觉醒模式 = 1
        else:
            属性.觉醒模式 = 0
