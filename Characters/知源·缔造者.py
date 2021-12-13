from math import *
from PublicReference.carry.base import *


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
    data0 = [0, 11, 15, 20, 24, 29, 31, 35, 40, 44, 48, 53, 57, 61, 65, 69, 74, 78, 83, 85, 89, 94, 98, 102, 107, 110, 115, 119, 123, 128, 132, 137, 139, 143, 148, 152, 156, 160, 164, 169, 173, 177, 182, 186, 191, 193, 197, 202, 206, 210, 214, 218, 223, 227, 231, 236, 240, 242, 247, 251, 256, 260, 263, 268, 272, 277, 281, 285, 290, 294, 296]

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
    data0 = [0, 109, 148, 187, 226, 263, 302, 341, 380, 418, 457, 494, 534, 573, 611, 650, 687, 727, 765, 804, 842, 882, 920, 958, 996, 1035, 1075, 1113, 1151, 1189, 1228, 1267, 1306, 1344, 1382, 1420, 1460, 1498, 1537, 1574, 1614, 1653, 1691, 1730, 1768, 1808, 1845, 1884, 1922, 1961, 2001, 2038, 2076, 2115, 2155, 2193, 2232, 2269, 2308, 2347, 2386, 2424, 2462, 2500, 2540, 2579, 2617, 2655, 2693, 2733, 2771]

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
    data0 = [0, 78, 89, 100, 111, 124, 135, 146, 158, 169, 180, 193, 204, 215, 226, 238, 249, 260, 273, 284, 295, 307, 318, 329, 341, 353, 364, 375, 387, 398, 410, 422, 433, 444, 455, 467, 479, 490, 502, 513, 524, 536, 548, 559, 570, 582, 593, 604, 617, 628, 639, 651, 662, 673, 684, 697, 708, 719, 731, 742, 754, 766, 777, 788, 799, 811, 823, 834, 844, 856, 867]

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
    data0 = [0, 828, 950, 1071, 1191, 1313, 1433, 1555, 1675, 1797, 1917, 2038, 2160, 2281, 2401, 2523, 2643, 2764, 2885, 3007, 3127, 3247, 3368, 3489, 3611, 3731, 3853, 3973, 4094, 4214, 4337, 4457, 4578, 4699, 4821, 4941, 5063, 5183, 5304, 5424, 5547, 5667, 5788, 5909, 6030, 6150, 6273, 6393, 6514, 6634, 6754, 6877, 6997, 7118, 7239, 7360, 7480, 7603, 7723, 7844, 7964, 8086, 8207, 8328, 8449, 8570, 8690, 8813, 8933, 9054, 9174]

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
    data0 = [0, 457, 503, 550, 596, 641, 689, 735, 782, 827, 873, 921, 967, 1014, 1059, 1107, 1153, 1200, 1245, 1291, 1339, 1385, 1430, 1477, 1524, 1571, 1616, 1663, 1709, 1757, 1802, 1848, 1895, 1942, 1987, 2034, 2080, 2127, 2174, 2220, 2266, 2312, 2360, 2405, 2452, 2498, 2545, 2591, 2637, 2684, 2730, 2776, 2823, 2869, 2916, 2961, 3009, 3055, 3102, 3147, 3193, 3241, 3287, 3334, 3379, 3425, 3473, 3519, 3565, 3611, 3659]

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
    data0 = [0, 2901, 3195, 3490, 3783, 4079, 4373, 4667, 4961, 5256, 5551, 5844, 6138, 6433, 6728, 7022, 7316, 7611, 7905, 8200, 8494, 8787, 9083, 9377, 9672, 9965, 10259, 10555, 10848, 11143, 11437, 11733, 12026, 12320, 12615, 12908, 13204, 13498, 13793, 14086, 14382, 14676, 14969, 15264, 15559, 15854, 16147, 16441, 16736, 17030, 17325, 17619, 17913, 18208, 18503, 18797, 19090, 19385, 19680, 19974, 20268, 20562, 20858, 21151, 21446, 21740, 22035, 22329, 22623, 22917, 23211]

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
    data0 = [0, 375, 414, 450, 488, 527, 565, 603, 641, 680, 718, 757, 793, 832, 870, 908, 946, 985, 1023, 1060, 1099, 1137, 1174, 1212, 1251, 1289, 1327, 1365, 1404, 1442, 1480, 1517, 1555, 1593, 1631, 1670, 1708, 1746, 1784, 1823, 1861, 1898, 1936, 1975, 2013, 2050, 2089, 2127, 2166, 2203, 2241, 2279, 2317, 2355, 2394, 2432, 2470, 2508, 2547, 2585, 2621, 2660, 2698, 2736, 2774, 2813, 2851, 2890, 2927, 2965, 3003]

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
    data0 = [0, 1575, 1735, 1895, 2055, 2215, 2375, 2536, 2695, 2856, 3015, 3176, 3335, 3494, 3654, 3814, 3974, 4134, 4294, 4454, 4615, 4774, 4935, 5094, 5253, 5413, 5573, 5733, 5893, 6053, 6213, 6373, 6533, 6694, 6853, 7014, 7172, 7332, 7492, 7652, 7812, 7972, 8132, 8292, 8452, 8612, 8773, 8931, 9090, 9251, 9411, 9571, 9731, 9891, 10051, 10211, 10371, 10531, 10691, 10850, 11010, 11171, 11330, 11490, 11650, 11810, 11970, 12130, 12290, 12450, 12609]

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
    data0 = [0, 220, 255, 291, 326, 361, 397, 433, 467, 502, 537, 573, 608, 644, 679, 713, 749, 784, 819, 854, 891, 926, 960, 995, 1031, 1066, 1101, 1137, 1173, 1207, 1242, 1277, 1312, 1348, 1384, 1419, 1453, 1489, 1524, 1559, 1594, 1631, 1666, 1700, 1735, 1770, 1806, 1841, 1877, 1912, 1947, 1982, 2017, 2052, 2087, 2124, 2159, 2193, 2228, 2264, 2299, 2335, 2370, 2406, 2440, 2475, 2510, 2546, 2582, 2617, 2652]
    # 虫洞大爆炸攻击力：<data1>
    data1 = [0, 10778, 12497, 14215, 15934, 17651, 19371, 21089, 22807, 24525, 26242, 27962, 29681, 31398, 33117, 34835, 36554, 38272, 39991, 41708, 43428, 45145, 46864, 48582, 50300, 52019, 53738, 55455, 57174, 58892, 60611, 62329, 64047, 65765, 67485, 69202, 70921, 72638, 74358, 76077, 77794, 79512, 81231, 82950, 84668, 86387, 88104, 89822, 91542, 93260, 94978, 96696, 98415, 100134, 101851, 103570, 105288, 107007, 108725, 110444, 112161, 113881, 115598, 117317, 119035, 120753, 122472, 124191, 125908, 127627, 129347]

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
        int(1.0 * x) for x in [
            0, 573, 664, 754, 846, 937, 1029, 1120, 1212, 1303, 1394, 1486,
            1577, 1669, 1760, 1851, 1943, 2034, 2126, 2217, 2308, 2400, 2491,
            2581, 2673, 2764, 2856, 2947, 3039, 3130, 3221, 3313, 3404, 3496,
            3587, 3678, 3770, 3861, 3953, 4044, 4135, 4227, 4318, 4410, 4500,
            4591, 4683, 4774, 4865, 4957, 5048, 5140, 5231, 5323, 5414, 5505,
            5597, 5688, 5780, 5871, 5962, 6054, 6145, 6237, 6327, 6418, 6510,
            6601, 6692, 6784, 6875
        ]
    ]
    # 范围大小 1.2~1的倍率
    倍率 = 1.2
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
    data0 = [0, 823, 906, 990, 1074, 1156, 1240, 1324, 1407, 1491, 1575, 1658, 1742, 1824, 1908, 1992, 2075, 2159, 2243, 2327, 2409, 2493, 2576, 2660, 2744, 2827, 2911, 2995, 3077, 3161, 3245, 3328, 3412, 3496, 3579, 3663, 3745, 3829, 3913, 3996, 4080, 4164, 4247, 4331, 4414, 4497, 4581, 4665, 4748, 4832, 4916, 4998, 5082, 5165, 5249, 5333, 5417, 5500, 5584, 5666, 5750, 5834, 5917, 6001, 6085, 6168, 6252, 6335, 6418, 6502, 6586]
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
    data0 = [0, 779, 902, 1027, 1150, 1275, 1399, 1522, 1648, 1771, 1896, 2020, 2144, 2268, 2391, 2516, 2639, 2765, 2889, 3013, 3137, 3260, 3385, 3509, 3634, 3758, 3883, 4006, 4130, 4254, 4378, 4504, 4627, 4752, 4875, 4999, 5123, 5247, 5373, 5496, 5621, 5744, 5868, 5993, 6116, 6242, 6365, 6490, 6614, 6737, 6862, 6985, 7111, 7235, 7359, 7483, 7606, 7731, 7854, 7979, 8103, 8228, 8352, 8475, 8600, 8724, 8848, 8972, 9098, 9221, 9345]
    # 最后一击爆炸攻击力：<data1>
    data1 = [0, 23364, 27089, 30813, 34537, 38262, 41987, 45712, 49436, 53162, 56887, 60611, 64336, 68061, 71785, 75510, 79235, 82959, 86684, 90408, 94133, 97858, 101583, 105309, 109032, 112757, 116482, 120207, 123932, 127657, 131382, 135105, 138830, 142555, 146280, 150005, 153730, 157453, 161178, 164904, 168629, 172354, 176079, 179803, 183527, 187252, 190977, 194702, 198426, 202151, 205875, 209600, 213325, 217051, 220775, 224500, 228225, 231949, 235674, 239398, 243123, 246848, 250573, 254297, 258021, 261746, 265471, 269197, 272922, 276647, 280370]

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

    data0 = [0, 19457, 23968, 28479, 32992, 37503, 42016, 46527, 51040, 55551, 60063, 64574, 69087, 73598, 78110, 82621, 87134, 91645, 96157, 100668, 105182, 109693, 114205, 118717, 123229, 127740, 132252, 136764, 141276, 145787, 150299, 154811, 159323, 163834, 168348, 172858, 177371, 181882, 186395, 190906, 195418, 199929, 204442, 208953, 213465, 217976, 222489, 227000, 231513, 236023, 240537, 245048, 249560, 254071, 258584, 263095, 267607, 272119, 276631, 281142, 285654, 290166, 294678, 299189, 303702, 308214, 312726, 317237, 321749, 326261, 330773]
    攻击次数 = 6
    CD = 180.0
    持续秒数 = 1
    能量 = 100
    最小值 = 100
    硬直时长百分比 = 0

# class 技能17(被动技能):
#    名称 = '卓越之力'
#    所在等级 = 95
#    等级上限 = 40
#    基础等级 = 4
#
#    def 加成倍率(self, 武器类型):
#        if self.等级 == 0:
#            return 1.0
#        else:
#            return round(1.18 + 0.02 * self.等级, 5)
#
#
# class 技能18(被动技能):
#    名称 = '超卓之心'
#    所在等级 = 95
#    等级上限 = 11
#    基础等级 = 1
#
#    def 加成倍率(self, 武器类型):
#        if self.等级 == 0:
#            return 1.0
#        else:
#            return round(1.045 + 0.005 * self.等级, 5)
#
#
# class 技能19(被动技能):
#    名称 = '觉醒之抉择'
#    所在等级 = 100
#    等级上限 = 40
#    基础等级 = 2
#    关联技能 = ['无']
#
#    def 加成倍率(self, 武器类型):
#        if self.等级 == 0:
#            return 1.0
#        else:
#            return round(1.10 + 0.05 * self.等级, 5)


class 技能17(被动技能):
    名称 = '天工开物'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能18(职业主动技能):
    名称 = '创世之光'

    所在等级 = 95
    等级上限 = 60
    基础等级 = 6
    #    基础 = 84924.00
    #    成长 = 25632.0
    data0 = [0, 108124, 119092, 130060, 141030, 151998, 162969, 173937, 184907, 195875, 206846, 217814, 228782, 239752, 250720, 261691, 272659, 283630, 294597, 305568, 316536, 327507, 338475, 349442, 360413, 371381, 382352, 393320, 404290, 415258, 426229, 437197, 448164, 459135, 470103, 481074, 492042, 503012, 513980, 524951, 535919, 546887, 557857, 568825, 579796, 590764, 601735, 612702, 623673, 634641, 645609, 656580, 667547, 678518, 689486, 700457, 711424, 722395, 733363, 744331, 755302, 766269, 777240, 788208, 799179, 810147, 821117, 832085, 843053, 854024, 864992]
    攻击次数 = 1
    CD = 60.0
    持续秒数 = 3.5
    能量 = 100
    最小值 = 100
    硬直时长百分比 = 0

#	def 加成倍率(self, 武器类型):
#        return 0.0


class 技能19(职业主动技能):
    名称 = '时之终末：归烬'

    所在等级 = 100
    等级上限 = 60
    基础等级 = 2
    #    基础 = 84924.00
    #    成长 = 25632.0
    data0 = [0, 11978, 14756, 17533, 20311, 23089, 25866, 28644, 31421, 34199, 36977, 39754, 42532, 45309, 48087, 50865, 53642, 56420, 59197, 61975, 64753, 67530, 70308, 73085, 75863, 78640, 81418, 84196, 86973, 89751, 92528, 95306, 98084, 100861, 103639, 106416, 109194, 111972, 114749, 117527, 120304, 123082, 125859, 128637, 131415, 134192, 136970, 139747, 142525, 145303, 148080, 150858, 153635, 156413, 159191, 161968, 164746, 167523, 170301, 173078, 175856, 178634, 181411, 184189, 186966, 189744, 192522, 195299, 198077, 200854, 203632]
    攻击次数 = 9
    data1 = [0, 251545, 309874, 368203, 426533, 484862, 543191, 601520, 659849, 718180, 776509, 834838, 893168, 951497, 1009826, 1068155, 1126484, 1184815, 1243144, 1301473, 1359803, 1418132, 1476461, 1534790, 1593119, 1651450, 1709779, 1768108, 1826438, 1884767, 1943096, 2001425, 2059754, 2118085, 2176414, 2234743, 2293073, 2351402, 2409731, 2468060, 2526389, 2584720, 2643049, 2701378, 2759708, 2818037, 2876366, 2934695, 2993024, 3051353, 3109684, 3168013, 3226343, 3284672, 3343001, 3401330, 3459659, 3517990, 3576319, 3634648, 3692978, 3751307, 3809636, 3867965, 3926294, 3984623, 4042954, 4101283, 4159613, 4217942, 4276271]
    攻击次数1 = 1

    CD = 290
    持续秒数 = 6
    能量 = 100
    最小值 = 100
    硬直时长百分比 = 0

    def 加成倍率(self, 武器类型):
        return 0.0


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
        tem = eval('技能'+str(i)+'()')
        tem.基础等级计算()
        技能列表.append(tem)
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
    if i.所在等级 >= 1 and i.所在等级 <= 80 and i.是否有伤害 == 1:
        缔造者符文选项.append(i.名称)


class 职业属性(角色属性):
    实际名称 = '知源·缔造者'
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
                if '/CD' in self.次数输入[self.技能序号[i.名称]]:

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
                        if 余数伤害时间 < 0.03:
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

        return self.技能释放次数解析(技能释放次数)


class 知源·缔造者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
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

        self.职业存档.append(('觉醒模式', self.觉醒模式, 0))
        self.职业存档.append(('数据精算模式', self.数据精算模式, 0))

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
