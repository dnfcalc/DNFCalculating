from PublicReference.carry.base import *


class 技能0(被动技能):
    名称 = '机械原理'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.085+0.015*self.等级, 5)


class 技能1(主动技能):
    名称 = 'G1科罗纳'
    备注 = '(秒伤)'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data0 = [int(i*1.194) for i in [0, 555, 620, 675, 730, 785, 845, 900, 960, 1015, 1075, 1135, 1190, 1250, 1305, 1365, 1420, 1475, 1530, 1590, 1645, 1710, 1770, 1825, 1880, 1935, 1995, 2050, 2110, 2165, 2225, 2285, 2340, 2400,
                               2455, 2515, 2570, 2625, 2680, 2745, 2805, 2860, 2920, 2975, 3030, 3085, 3145, 3200, 3265, 3320, 3375, 3435, 3490, 3550, 3605, 3665, 3720, 3780, 3835, 3895, 3955, 4010, 4070, 4125, 4180, 4235, 4300, 4355, 4415, 4475, 4525]]
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return round(1, 1)

    def G系加成倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.59+0.01*self.等级, 5)

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能2(主动技能):
    名称 = 'G2旋雷者'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [int(i*1.193) for i in [0, 558, 615, 671, 728, 785, 841, 898, 954, 1011, 1067, 1124, 1181, 1237, 1294, 1350, 1407, 1464, 1520, 1577, 1634, 1690, 1747, 1804, 1860, 1917, 1973, 2030, 2087, 2143, 2200, 2256, 2313, 2370, 2426, 2483, 2540, 2596, 2653, 2709, 2766, 2823, 2879, 2936, 2992, 3049, 3106, 3162, 3219, 3275, 3332, 3389, 3445, 3502, 3559, 3615, 3672, 3728, 3785, 3842, 3898, 3955, 4011, 4068, 4125, 4181, 4238, 4295, 4351, 4408, 4464]]
    攻击次数 = 4
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return round(6, 1)

    def G系加成倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.50+0.01*self.等级, 5)

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能3(主动技能):
    名称 = '毒蛇炮'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [int(i*1.141) for i in [0, 80, 89, 98, 105, 114, 121, 130, 138, 146, 155, 163, 171, 179, 188, 196, 204, 213, 220, 228, 236, 245, 254, 261, 270, 278, 286, 294, 303, 311, 319, 328, 335, 344, 351, 360, 369, 376, 385, 393, 401, 409, 418, 426, 434, 441, 450, 459, 468, 475, 484, 491, 499, 508, 516, 525, 533, 541, 549, 558, 565, 574, 583, 590, 599, 606, 615, 623, 631, 640, 648]]
    攻击次数 = 30
    data1 = [int(i*1.0) for i in [0, 486, 535, 585, 633, 683, 732, 781, 831, 880, 929, 979, 1028, 1077, 1127, 1176, 1225, 1275, 1324, 1373, 1423, 1472, 1521, 1571, 1620, 1669, 1718, 1767, 1817, 1866, 1916, 1965, 2014, 2064, 2113,
                                2162, 2212, 2261, 2310, 2360, 2409, 2458, 2508, 2557, 2606, 2656, 2704, 2754, 2803, 2852, 2902, 2951, 3000, 3050, 3099, 3148, 3198, 3247, 3296, 3346, 3395, 3444, 3494, 3543, 3592, 3642, 3691, 3740, 3789, 3838, 3888]]
    攻击次数2 = 0
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能4(被动技能):
    名称 = '电能转换'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    # 是否加成三觉的两个技能到时候自己加
    关联技能 = ['毒蛇炮', '空战机械：狂风', '空投支援', '拦截机工厂', 'G0战争领主', 'HS12等离子体发生器', 'G4雷行者', 'GSP猎鹰科罗纳形态',
            'GSP猎鹰旋雷者形态', 'GSP猎鹰捕食者形态', '高压电磁场', '终结者：博尔特MX', '超时空光耀加农炮', 'G-X 星尘天穹', '空中射击', 'RX-78追击者', 'Ez-8自爆者']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10+0.02*self.等级, 5)


class 技能5(主动技能):
    名称 = 'G3捕食者'
    备注 = '(秒伤)'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data0 = [int(i*1.195) for i in [0, 100, 110, 120, 130, 140, 151, 161, 171, 181, 191, 201, 211, 222, 232, 242, 252, 262, 272, 283, 293, 303, 313, 323, 333, 343, 354, 364, 374, 384, 394, 404, 414, 425, 435, 445, 455, 465, 475, 485, 495, 505, 515, 525, 535, 545, 555, 566, 576, 586, 596, 606, 616, 627, 637, 647, 657, 667, 677, 687, 698, 708, 718, 728, 738, 748, 758, 769, 779, 789, 799]]
    攻击次数 = 8
    CD = 1
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return round(1, 1)

    def G系加成倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.50+0.017*self.等级, 5)

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能6(主动技能):
    名称 = 'G1磁力弹'
    所在等级 = 30
    等级上限 = 70
    基础等级 = 43
    CD = 15


# class 技能7(主动技能):
#     名称 = '自爆狂风'
#     备注 = '(自爆伤害)'
#     所在等级 = 35
#     等级上限 = 60
#     基础等级 = 36
#     data0 = [int(i*1.0) for i in [0, 2202, 2425, 2649, 2872, 3095, 3319, 3543, 3766, 3989, 4213, 4436, 4660, 4883, 5106, 5330, 5554, 5777, 6000, 6224, 6447, 6671, 6894, 7117, 7341, 7565, 7788, 8011, 8235, 8458, 8682, 8905, 9128, 9352, 9575, 9799, 10022,
#                                10245, 10469, 10693, 10915, 11139, 11363, 11586, 11810, 12033, 12256, 12480, 12704, 12926, 13150, 13374, 13597, 13821, 14044, 14267, 14491, 14715, 14937, 15161, 15385, 15608, 15831, 16055, 16278, 16502, 16725, 16948, 17172, 17395, 17619]]
#     CD = 25.5
#     TP成长 = 0.10
#     TP上限 = 5
#     是否有护石 = 1
#     演出时间 = 1.4

#     护石选项 = ['魔界', '圣痕']

#     def 装备护石(self, x):
#         if x == 0:
#             self.倍率 *= 8.79

#         elif x == 1:
#             self.倍率 *= 9.24

#     def 等效百分比(self, 武器类型):
#         return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能7(主动技能):
    名称 = '空战机械：狂风'
    # 备注 = '(机枪捣蛋模式, 秒伤)'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data0 = [int(i*1.135) for i in [0, 611, 674, 735, 797, 860, 922, 984, 1045, 1108, 1170, 1232, 1294, 1356, 1418, 1480, 1543, 1605, 1666, 1728, 1791, 1853, 1915, 1976, 2039, 2101, 2163, 2225, 2287, 2349, 2411, 2474, 2535, 2597, 2659, 2722, 2784, 2845, 2907, 2970, 3032, 3094, 3156, 3218, 3280, 3342, 3405, 3466, 3528, 3590, 3653, 3715, 3776, 3839, 3901, 3963, 4025, 4087, 4149, 4211, 4273, 4335, 4397, 4459, 4522, 4584, 4645, 4707, 4770, 4832, 4894]]
    攻击次数 = 3/3.352
    data1 = [int(i*1.135) for i in [0, 275, 303, 331, 358, 386, 415, 443, 470, 498, 526, 555, 582, 610, 638, 665, 694, 722, 750, 777, 805, 834, 861, 889, 917, 945, 973, 1001, 1029, 1057, 1085, 1113, 1141, 1168, 1196, 1225, 1253, 1280, 1308, 1336, 1364, 1392, 1420, 1448, 1475, 1504, 1532, 1560, 1587, 1615, 1644, 1671, 1699, 1727, 1755, 1783, 1811, 1839, 1866, 1895, 1923, 1951, 1978, 2006, 2035, 2063, 2090, 2118, 2146, 2174, 2202]]
    攻击次数2 = 6/3.523
    data2 = [int(i*1.135) for i in [0,2202, 2425, 2649, 2872, 3095, 3319, 3543, 3766, 3989, 4213, 4436, 4660, 4883, 5106, 5330, 5554, 5777, 6000, 6224, 6447, 6671, 6894, 7117, 7341, 7565, 7788, 8011, 8235, 8458, 8682, 8905, 9128, 9352, 9575, 9799, 10022, 10245, 10469, 10693, 10915, 11139, 11363, 11586, 11810, 12033, 12256, 12480, 12704, 12926, 13150, 13374, 13597, 13821, 14044, 14267, 14491, 14715, 14937, 15161, 15385, 15608, 15831, 16055, 16278, 16502, 16725, 16948, 17172, 17395, 17619]]
    攻击次数3 = 0
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    装备护石 = 0

    def 装备护石(self, x):
        if x == 0:
            self.装备护石 = 1
            self.演出时间 = 1.4
            self.攻击次数3 = 8.79
            self.攻击次数 = 0
            self.攻击次数2 = 0
            self.CD = 30

        elif x == 1:
            self.装备护石 = 1
            self.演出时间 = 1.4
            self.攻击次数3 = 9.24
            self.攻击次数 = 0
            self.攻击次数2 = 0
            self.CD = 30

    def 等效CD(self, 武器类型, 输出类型):
        if self.装备护石 == 1:
            return super().等效CD(武器类型, 输出类型)
        else:
            return round(1, 1)

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2+ self.data2[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能8(主动技能):
    名称 = '空投支援'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data0 = [int(i*1.177) for i in [0, 912, 1005, 1098, 1190, 1283, 1376, 1468, 1561, 1654, 1747, 1838, 1931, 2025, 2116, 2209, 2302, 2395, 2487, 2579, 2673, 2766, 2857, 2951, 3043, 3135, 3228, 3321, 3414, 3505, 3599, 3692, 3783, 3876, 3969, 4062, 4154, 4247, 4340, 4433, 4524, 4618, 4710, 4802, 4896, 4988, 5081, 5172, 5266, 5359, 5450, 5544, 5636, 5729, 5821, 5914, 6007, 6100, 6192, 6285, 6377, 6469, 6563, 6655, 6748, 6840, 6933, 7026, 7117, 7211, 7303]]
    攻击次数 = 20
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3.5

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.242
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.334
            self.CD *= 0.9

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能9(主动技能):
    名称 = '拦截机工厂'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data0 = [int(i*1.173) for i in [0, 160, 176, 193, 208, 225, 241, 258, 274, 291, 308, 324, 340, 356, 373, 389, 405, 421, 438, 454, 470, 487, 503, 520, 535, 552, 568, 585, 600, 617, 633, 650, 666, 682, 699, 715, 731, 747, 764, 780, 796, 812, 829, 846, 861, 878, 894, 911, 926, 943, 959, 976, 991, 1008, 1025, 1040, 1057, 1073, 1090, 1105, 1122, 1138, 1155, 1170, 1188, 1204, 1221, 1238, 1253, 1270, 1286]]
    攻击次数 = 110
    data1 = [int(i*1.173) for i in [0, 1205, 1327, 1450, 1572, 1695, 1817, 1940, 2062, 2184, 2306, 2428, 2550, 2672, 2794, 2918, 3041, 3163, 3285, 3407, 3529, 3651, 3774, 3896, 4019, 4141, 4263, 4385, 4508, 4631, 4753, 4875, 4997, 5120, 5242, 5364, 5486, 5609, 5731, 5853, 5975, 6098, 6220, 6343, 6466, 6588, 6710, 6832, 6954, 7076, 7198, 7321, 7444, 7566, 7689, 7811, 7933, 8055, 8177, 8300, 8422, 8544, 8667, 8789, 8911, 9033, 9156, 9279, 9401, 9523, 9644]]
    攻击次数2 = 6
    data2 =[int(i*1.173) for i in [0,21171, 23319, 25467, 27615, 29763, 31911, 34058, 36206, 38354, 40502, 42650, 44798, 46946, 49093, 51241, 53389, 55537, 57685, 59833, 61981, 64128, 66276, 68424, 70572, 72720, 74868, 77016, 79163, 81311, 83459, 85607, 87755, 89903, 92051, 94198, 96346, 98494, 100642, 102790, 104938, 107086, 109233, 111381, 113529, 115677, 117825, 119973, 122121, 124268, 126416, 128564, 130712, 132860, 135008, 137156, 139303, 141451, 143599, 145747, 147895, 150043, 152191, 154338, 156486, 158634, 160782, 162930, 165078, 167226, 155634]]
    攻击次数3 = 0
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4.9

    光反应能量模块 = 0

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(i * 1.17) for i in self.data0]
            self.data1 = [int(i * 1.17) for i in self.data1]
            self.data2 = [int(i * 1.14) for i in self.data2]
            self.攻击次数 = 120

        elif x == 1:
            self.data0 = [int(i * 1.25) for i in self.data0]
            self.data1 = [int(i * 1.25) for i in self.data1]
            self.data2 = [int(i * 1.22) for i in self.data2]
            self.攻击次数 = 120

    def 等效百分比(self, 武器类型):
        if self.光反应能量模块 == 1:
            self.攻击次数 = 0
            self.攻击次数2 = 0
            self.攻击次数3 = 1

        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能10(被动技能):
    名称 = '光反应能量模块'
    所在等级 = 45
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['拦截机工厂']
    倍率 = 1.0

    def 技能描述(self, 武器类型):
        temp = ''
        temp += '将拦截机互相连结， 生成能量散热板<br>'+ \
            '能量散热板蓄积能量并向前方发射， 然后消失'
        return temp

    def 加成倍率(self, 武器类型):
        return self.倍率


class 技能11(被动技能):
    名称 = 'G系扩张'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025+0.02*self.等级, 5)


class 技能12(主动技能):
    名称 = 'G0战争领主'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12

    data0 = [int(i*1.184) for i in [0, 539, 665, 790, 915, 1040, 1166, 1291, 1417, 1541, 1667, 1791, 1917, 2042, 2168, 2292, 2418, 2544, 2669, 2795, 2920, 3044, 3169, 3295, 3420, 3546, 3671, 3796, 3921, 4047, 4171, 4297, 4422, 4547, 4672, 4798, 4923, 5049, 5173, 5299, 5423, 5549, 5675, 5800, 5924, 6050, 6176, 6301, 6427, 6552, 6676, 6801, 6927, 7052, 7178, 7303, 7428, 7553, 7679, 7803, 7929, 8054, 8179, 8304, 8430, 8555, 8681, 8805, 8931, 9055, 9181]]
    攻击次数 = 30
    data1 = [int(i*1.184) for i in [0, 675, 832, 988, 1145, 1300, 1457, 1614, 1770, 1927, 2084, 2240, 2397, 2553, 2709, 2866, 3022, 3179, 3336, 3492, 3649, 3806, 3963, 4120, 4275, 4432, 4589, 4745, 4902, 5058, 5215, 5372, 5528, 5685, 5840, 5997, 6154, 6310, 6467, 6624, 6780, 6937, 7093, 7250, 7406, 7562, 7719, 7876, 8032, 8189, 8346, 8503, 8660, 8816, 8972, 9129, 9285, 9442, 9598, 9755, 9912, 10068, 10225, 10380, 10537, 10694, 10850, 11007, 11164, 11320, 11477]]
    攻击次数2 = 24
    data2 = [int(i*1.184) for i in [0, 2925, 3604, 4282, 4960, 5639, 6317, 6995, 7673, 8353, 9030, 9709, 10387, 11067, 11744, 12423, 13101, 13779, 14458, 15137, 15814, 16493, 17171, 17850, 18528, 19207, 19885, 20564, 21242, 21921, 22598, 23278, 23956, 24634, 25312, 25990, 26669, 27347, 28026, 28703, 29383, 30061, 30740, 31417, 32096, 32775, 33453, 34131, 34810, 35487, 36167, 36845, 37523, 38201, 38881, 39559, 40237, 40915, 41595, 42272, 42951, 43629, 44308, 44986, 45664, 46342, 47020, 47700, 48377, 49056, 49735]]
    攻击次数3 = 12
    CD = 145.0
    一觉减CD = 0
    冷却关联技能 = ['所有']
    演出时间 = 7.1

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3) * self.倍率

    def CD缩减倍率(self, 武器类型):
        return round(1 - self.一觉减CD, 3)


class 技能13(主动技能):
    名称 = 'HS12等离子体发生器'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data0 = [int(i*1.186) for i in [0, 17953, 19774, 21595, 23417, 25238, 27059, 28881, 30702, 32523, 34345, 36166, 37987, 39809, 41630, 43451, 45273, 47094, 48915, 50737, 52558, 54379, 56201, 58022, 59843, 61665, 63486, 65307, 67129, 68950, 70772, 72593, 74414, 76236, 78057, 79878, 81700, 83521, 85342, 87164, 88985, 90806, 92628, 94449, 96270, 98092, 99913, 101734, 103556, 105377]]
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.9

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.12

        elif x == 1:
            self.倍率 *= 1.21

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能14(主动技能):
    名称 = 'G4雷行者'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data0 = [int(i*1.194) for i in [0, 542, 597, 652, 706, 761, 817, 872, 927, 982, 1037, 1092, 1147, 1202, 1256, 1311, 1366, 1422, 1477, 1532, 1587, 1642, 1697, 1752, 1807, 1861, 1916, 1971, 2027, 2082, 2137, 2192, 2247, 2302, 2357, 2412, 2466, 2521, 2576, 2632, 2687, 2742, 2797, 2852, 2907, 2962, 3016, 3071, 3126, 3181, 3237, 3292, 3347, 3402, 3457, 3512, 3567, 3621, 3676, 3731, 3786, 3842, 3897, 3952, 4007, 4062, 4117, 4172, 4226, 4281, 4336]]
    攻击次数 = 48
    data1 = [int(i*1.194) for i in [0, 1117, 1231, 1344, 1458, 1570, 1685, 1798, 1912, 2024, 2138, 2252, 2365, 2478, 2592, 2705, 2819, 2932, 3046, 3158, 3273, 3386, 3499, 3612, 3726, 3840, 3953, 4066, 4180, 4293, 4407, 4520, 4634, 4746, 4861, 4974, 5087, 5200, 5315, 5427, 5541, 5654, 5768, 5881, 5995, 6108, 6221, 6334, 6449, 6562, 6675, 6788, 6903, 7015, 7129, 7242, 7356, 7469, 7583, 7696, 7809, 7923, 8037, 8149, 8263, 8376, 8491, 8603, 8717, 8830, 8943]]
    攻击次数2 = 3
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 7.3

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.12
            self.CD *= 0.9

        elif x == 1:
            self.倍率 *= 1.20
            self.CD *= 0.9

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能15(被动技能):
    名称 = 'GX主宰者'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11


    冷却关联技能 = ['所有']
    非冷却关联技能 = ['G0战争领主', '终结者：博尔特MX','G-X 星尘天穹','RX-78追击者']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 in [1, 2]:
            return round(1.08+0.02*self.等级, 5)
        if self.等级 == 3:
            return round(1.15, 5)
        if self.等级 == 4:
            return round(1.20, 5)
        if self.等级 >= 5:
            return round(1.12+0.02*self.等级, 5)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.85

class 技能16(主动技能):
    名称 = 'GSP猎鹰科罗纳形态'
    备注 = '(GSP猎鹰)'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    data0 = [int(i*1.191) for i in [0, 17356, 19117, 20878, 22638, 24399, 26160, 27921, 29682, 31442, 33203, 34964, 36725, 38486, 40246, 42007, 43768, 45529, 47290, 49051, 50811, 52572, 54333, 56094, 57855, 59615, 61376, 63137, 64898, 66659, 68419, 70180, 71941, 73702, 75463, 77223, 78984, 80745, 82506, 84267, 86027, 87788, 89549, 91310, 93071, 94831, 96592, 98353, 100114, 101875, 103636, 105396, 107157, 108918, 110679, 112440, 114200, 115961, 117722, 119483, 121244, 123004, 124765, 126526, 128287, 130048, 131808, 133569, 135330, 137091, 138852]]
    CD = 15
    基础释放次数 = 2
    演出时间 = 1.3
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35
            self.CD *= 0.9

    # def 等效CD(self, 武器类型, 输出类型):
    #     return round(self.CD, 1)

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.倍率


class 技能17(主动技能):
    名称 = 'GSP猎鹰旋雷者形态'
    备注 = '(GSP猎鹰)'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    data0 = [int(i*1.192) for i in [0, 5787, 6374, 6961, 7548, 8135, 8722, 9309, 9897, 10484, 11071, 11658, 12245, 12832, 13419, 14006, 14593, 15181, 15768, 16355, 16942, 17529, 18116, 18703, 19290, 19877, 20465, 21052, 21639, 22226, 22813, 23400, 23987, 24574, 25161, 25749, 26336, 26923, 27510, 28097, 28684, 29271, 29858, 30445, 31033, 31620, 32207, 32794, 33381, 33968, 34555, 35142, 35729, 36317, 36904, 37491, 38078, 38665, 39252, 39839, 40426, 41013, 41601, 42188, 42775, 43362, 43949, 44536, 45123, 45710, 46297]]
    攻击次数 = 3
    CD = 15
    基础释放次数 = 2
    演出时间 = 1.6
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.34
            self.CD *= 0.9

    # def 等效CD(self, 武器类型, 输出类型):
    #     return round(self.CD, 1)

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * self.倍率


class 技能18(主动技能):
    名称 = 'GSP猎鹰捕食者形态'
    备注 = '(GSP猎鹰)'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    data0 = [int(i*1.192) for i in [0, 745, 821, 897, 972, 1048, 1123, 1198, 1274, 1350, 1426, 1501, 1577, 1652, 1728, 1803, 1879, 1955, 2031, 2106, 2182, 2257, 2333, 2408, 2485, 2560, 2636, 2711, 2787, 2862, 2938, 3014, 3090, 3165, 3241, 3316, 3392, 3467, 3543, 3619, 3695, 3770, 3845, 3921, 3996, 4072, 4148, 4224, 4299, 4375, 4450, 4526, 4601, 4678, 4753, 4829, 4904, 4980, 5055, 5131, 5207, 5283, 5358, 5434, 5509, 5585, 5660, 5736, 5812, 5888, 5963]]
    攻击次数 = 25
    CD = 15
    基础释放次数 = 2
    演出时间 = 2.8

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.314
            self.CD *= 0.9

    # def 等效CD(self, 武器类型, 输出类型):
    #     return round(self.CD, 1)

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * self.倍率


class 技能19(主动技能):
    名称 = '高压电磁场'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    data0 = [int(i*1.197) for i in [0, 4041, 4451, 4861, 5270, 5680, 6091, 6501, 6910, 7321, 7730, 8141, 8550, 8960, 9371, 9780, 10190, 10600, 11010, 11421, 11830, 12240, 12650, 13060, 13471, 13879, 14290, 14701, 15110, 15520, 15930, 16340, 16751, 17159, 17570, 17980, 18390, 18800, 19209, 19620, 20030, 20440, 20850, 21259, 21670, 22081, 22489, 22900, 23309, 23720, 24130, 24539, 24950, 25359, 25769, 26180, 26589, 27000, 27409, 27819, 28230, 28639, 29050, 29458, 29869, 30280, 30689, 31099, 31508, 31919, 32330]]
    攻击次数 = 15
    CD = 50
    演出时间 = 3.5
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.30
            self.CD *= 0.9

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * self.倍率


class 技能20(主动技能):
    名称 = '终结者：博尔特MX'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5

    data0 = [int(i*1.192) for i in [0, 1877, 2312, 2748, 3183, 3619, 4054, 4489, 4924, 5360, 5796, 6231, 6666, 7101, 7537, 7972, 8408, 8842, 9278, 9714, 10149, 10585, 11019, 11455, 11890, 12326, 12762, 13196, 13632, 14067, 14503, 14938, 15374, 15809, 16244, 16680, 17115, 17551, 17986, 18421, 18856, 19292, 19728, 20163, 20598, 21033, 21469, 21904, 22340, 22774, 23210, 23646, 24081, 24517, 24951, 25387, 25822, 26258, 26694, 27128, 27564, 27999, 28435, 28870, 29305, 29740, 30176, 30612, 31047, 31482, 31917]]
    攻击次数 = 8
    data1 = [int(i*1.192) for i in [0, 4096, 5047, 5995, 6945, 7896, 8846, 9796, 10745, 11695, 12645, 13595, 14546, 15494, 16444, 17395, 18345, 19294, 20244, 21194, 22144, 23095, 24043, 24993, 25944, 26894, 27844, 28793, 29743, 30693, 31644, 32594, 33542, 34493, 35443, 36393, 37342, 38292, 39242, 40192, 41143, 42091, 43041, 43992, 44942, 45892, 46841, 47791, 48741, 49692, 50642, 51590, 52541, 53491, 54441, 55390, 56340, 57290, 58241, 59191, 60139, 61089, 62040, 62990, 63940, 64889, 65839, 66789, 67740, 68690, 69638]]
    攻击次数2 = 2
    data2 = [int(i*1.192) for i in [0, 2398, 2953, 3510, 4065, 4621, 5176, 5734, 6293, 6850, 7405, 7961, 8516, 9074, 9627, 10185, 10741, 11297, 11854, 12409, 12966, 13520, 14077, 14632, 15189, 15745, 16301, 16860, 17415, 17972, 18529, 19085, 19642, 20197, 20753, 21308, 21865, 22419, 22976, 23531, 24088, 24645, 25201, 25758, 26312, 26869, 27427, 27983, 28541, 29096, 29652, 30207, 30764, 31320, 31875, 32432, 32987, 33543, 34099, 34657, 35211, 35768, 36323, 36880, 37436, 37997, 38551, 39108, 39663, 40219, 40774]]
    攻击次数3 = 15
    data3 = [int(i*1.192) for i in [0, 2959, 3645, 4330, 5016, 5702, 6389, 7075, 7761, 8446, 9132, 9819, 10505, 11191, 11877, 12563, 13248, 13935, 14621, 15307, 15993, 16679, 17366, 18051, 18737, 19423, 20109, 20795, 21482, 22167, 22853, 23539, 24225, 24912, 25598, 26284, 26969, 27655, 28341, 29028, 29714, 30400, 31085, 31771, 32458, 33144, 33830, 34516, 35201, 35887, 36574, 37260, 37946, 38632, 39318, 40005, 40690, 41376, 42062, 42748, 43434, 44121, 44806, 45492, 46178, 46864, 47551, 48237, 48922, 49608, 50294]]
    攻击次数4 = 6
    data4 = [int(i*1.192) for i in [0, 30040, 37005, 43972, 50937, 57904, 64869, 71836, 78802, 85767, 92734, 99699, 106666, 113631, 120598, 127563, 134530, 141495, 148462, 155427, 162393, 169359, 176324, 183291, 190256, 197223, 204188, 211155, 218120, 225087, 232052, 239018, 245984, 252949, 259916, 266881, 273848, 280813, 287780, 294745, 301712, 308677, 315643, 322609, 329575, 336541, 343506, 350473, 357438, 364405, 371370, 378337, 385302, 392268, 399234, 406200, 413166, 420131, 427098, 434063, 441030, 447995, 454962, 461927, 468893, 475859, 482825, 489792, 496758, 503724, 510690]]
    攻击次数5 = 1
    data5 = [int(i*1.192) for i in [0, 230040, 37005, 43972, 50937, 57904, 64869, 71836, 78802, 85767, 92734, 99699, 106666, 113631, 120598, 127563, 134530, 141495, 148462, 155427, 162393, 169359, 176324, 183291, 190256, 197223, 204188, 211155, 218120, 225087, 232052, 239018, 245984, 252949, 259916, 266881, 273848, 280813, 287780, 294745, 301712, 308677, 315643, 322609, 329575, 336541, 343506, 350473, 357438, 364405, 371370, 378337, 385302, 392268, 399234, 406200, 413166, 420131, 427098, 434063, 441030, 447995, 454962, 461927, 468893, 475859, 482825, 489792, 496758, 503724, 510690]]
    攻击次数6 = 1
    CD = 180
    演出时间 = 7.1

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3 + self.data3[self.等级] * self.攻击次数4 + self.data4[self.等级] * self.攻击次数5 + self.data5[self.等级] * self.攻击次数6) * self.倍率


class 技能21(被动技能):
    名称 = '微型制导'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能22(主动技能):
    名称 = '超时空光耀加农炮'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 10
    演出时间 = 1.5
    基础等级 = 6
    CD = 60
    # 基础 = 6094.8
    # 成长 = 688.2
    data0 = [int(i*1.182) for i in [0,5653, 6226, 6800, 7373, 7947, 8520, 9094, 9667, 10241, 10814, 11388, 11961, 12535, 13108, 13682, 14255, 14829, 15402, 15976, 16549, 17123, 17696, 18270, 18843, 19417, 19990, 20564, 21137, 21711, 22284, 22858, 23431, 24005, 24578, 25152, 25725, 26299, 26872, 27446, 28019]]
    data1 = [int(i*1.182) for i in [0,19785, 21793, 23800, 25807, 27814, 29822, 31829, 33836, 35843, 37851, 39858, 41865, 43872, 45880, 47887, 49894, 51901, 53909, 55916, 57923, 59930, 61938, 63945, 65952, 67959, 69967, 71974, 73981, 75988, 77996, 80003, 82010, 84017, 86025, 88032, 90039, 92046, 94054, 96061, 98068]]
    攻击次数 = 6
    # 基础2 = 17777.6
    # 成长2 = 2007.4
    攻击次数2 = 4

    def 等效百分比(self, 武器类型):
       return (self.data0[self.等级]* self.攻击次数 + self.data1[self.等级]* self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能23(主动技能):
    名称 = 'G-X 星尘天穹'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = 2
    CD = 290.0
    演出时间 = 6.5
    攻击次数 = 8
    攻击次数2 = 7

    data0 = [int(i*1.184) for i in [0,16341, 20131, 23920, 27710, 31499, 35288, 39078, 42867, 46657, 50446, 54235, 58025, 61814, 65604, 69393, 73182, 76972, 80761, 84551, 88340, 92129, 95919, 99708, 103498, 107287, 111077, 114866, 118655, 122445, 126234]]
    data1 = [int(i*1.184) for i in [0,43578, 53683, 63788, 73893, 83998, 94103, 104208, 114313, 124418, 134524, 144629, 154734, 164839, 174944, 185049, 195154, 205259, 215364, 225469, 235574, 245679, 255785, 265890, 275995, 286100, 296205, 306310, 316415, 326520, 336625]]

    def 加成倍率(self, 武器类型):
        return 0.0
    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级]* self.攻击次数 + self.data1[self.等级]* self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能24(主动技能):
    名称 = '空中射击'
    备注 = '(秒伤,TP为基础精通)'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    data0 = [int(i) for i in [0, 102, 104, 106, 108, 110, 112, 114, 116,
                           118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 140]]
    攻击次数 = 1
    CD = 1
    TP成长 = 0.10
    TP上限 = 3

    def 等效CD(self, 武器类型, 输出类型):
        return round(1, 1)

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 / 0.115 * 1.6 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能25(被动技能):
    名称 = '基础精通'
    所在等级 = 1
    倍率 = 1.0
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['空中射击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 技能26(主动技能):
    名称 = 'RX-78追击者'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50

    data0 = [int(i*1.0) for i in [0, 667, 734, 802, 869, 936, 1003, 1071, 1140, 1207, 1275, 1343, 1410, 1477, 1546, 1613, 1680, 1749, 1817, 1884, 1952, 2020, 2087, 2155, 2222, 2290, 2359, 2426, 2494, 2561, 2629, 2696, 2763,
                               2831, 2898, 2967, 3035, 3102, 3169, 3237, 3305, 3372, 3440, 3509, 3576, 3643, 3712, 3779, 3846, 3915, 3982, 4049, 4117, 4186, 4253, 4320, 4389, 4456, 4523, 4590, 4658]]
    CD = 2.8
    TP成长 = 0.08
    TP上限 = 5
    演出时间 = 0.7

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能27(主动技能):
    名称 = 'Ez-8自爆者'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46

    data0 = [int(i*1.0) for i in [0, 2281, 2512, 2743, 2975, 3206, 3438, 3670, 3901, 4132, 4364, 4595, 4826, 5058, 5289, 5521, 5752, 5984, 6216, 6447, 6678, 6910, 7141, 7372, 7604, 7835, 8066, 8299, 8530, 8761, 8993, 9224,
                               9456, 9687, 9917, 10150, 10380, 10611, 10845, 11075, 11306, 11538, 11769, 12000, 12232, 12463, 12695, 12926, 13158, 13390, 13621, 13852, 14084, 14315, 14546, 14778, 15009, 15240, 15473, 15704, 15935]]
    CD = 7.5
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 0.6

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能28(主动技能):
    名称 = '机械引爆'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 5
    关联技能 = ['RX-78追击者', 'Ez-8自爆者']
    CD = 3.5
    演出时间 = 0.6
    是否有伤害 = 0

    def 加成倍率(self, 武器类型):
        if self.等级 <= 4:
            return round(1.30+0.02*self.等级, 5)
        if self.等级 >= 5:
            return round(1.40, 5)


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
    temp = i
    if i.是否有伤害 == 1 and i.是否有护石 == 1 and i.所在等级 <= 70:
        护石选项.append(i.名称)
护石选项.append('GSP猎鹰')
护石选项.append('高压电磁场')

符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 70 and i.所在等级 != 50 and i.是否有伤害 == 1:
        符文选项.append(i.名称)
符文选项.append('GSP猎鹰')
符文选项.append('高压电磁场')


class 职业角色属性(角色属性):

    实际名称 = '重霄·机械师·女'
    角色 = '神枪手(女)'
    职业 = '机械师'

    武器选项 = ['自动手枪']

    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.850

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        if self.装备检查('守护的抉择'):
            if self.护石第一栏 == 'GSP猎鹰':
                self.技能栏[self.技能序号['GSP猎鹰科罗纳形态']].CD *= 0.7
                self.技能栏[self.技能序号['GSP猎鹰科罗纳形态']].倍率 *= 1.55
                self.技能栏[self.技能序号['GSP猎鹰旋雷者形态']].CD *= 0.7
                self.技能栏[self.技能序号['GSP猎鹰旋雷者形态']].倍率 *= 1.55
                self.技能栏[self.技能序号['GSP猎鹰捕食者形态']].CD *= 0.7
                self.技能栏[self.技能序号['GSP猎鹰捕食者形态']].倍率 *= 1.55
            if self.护石第二栏 == 'GSP猎鹰':
                self.技能栏[self.技能序号['GSP猎鹰科罗纳形态']].CD *= 0.75
                self.技能栏[self.技能序号['GSP猎鹰科罗纳形态']].倍率 *= 1.45
                self.技能栏[self.技能序号['GSP猎鹰旋雷者形态']].CD *= 0.75
                self.技能栏[self.技能序号['GSP猎鹰旋雷者形态']].倍率 *= 1.45
                self.技能栏[self.技能序号['GSP猎鹰捕食者形态']].CD *= 0.75
                self.技能栏[self.技能序号['GSP猎鹰捕食者形态']].倍率 *= 1.45
        if self.技能栏[self.技能序号['光反应能量模块']].等级 != 0:
            self.技能栏[self.技能序号['拦截机工厂']].光反应能量模块 = 1
            self.技能栏[self.技能序号['拦截机工厂']].演出时间 = 1.7
            if self.装备检查('雷霆怒啸手枪'):
                self.技能栏[self.技能序号['光反应能量模块']].倍率 *= 1.2
        super().被动倍率计算()
        self.技能栏[self.技能序号['G1科罗纳']].被动倍率 *= 1+self.技能栏[self.技能序号['G2旋雷者']
                                                        ].G系加成倍率()+self.技能栏[self.技能序号['G3捕食者']].G系加成倍率()
        self.技能栏[self.技能序号['G2旋雷者']].被动倍率 *= 1+self.技能栏[self.技能序号['G1科罗纳']
                                                        ].G系加成倍率()+self.技能栏[self.技能序号['G3捕食者']].G系加成倍率()
        self.技能栏[self.技能序号['G3捕食者']].被动倍率 *= 1+self.技能栏[self.技能序号['G1科罗纳']
                                                        ].G系加成倍率()+self.技能栏[self.技能序号['G2旋雷者']].G系加成倍率()
        self.技能栏[self.技能序号['G1磁力弹']].基础 = self.技能栏[self.技能序号['G1科罗纳']].等效百分比(
            self.武器类型)*0.2*1.717*10
        self.技能栏[self.技能序号['G1磁力弹']].被动倍率 = self.技能栏[self.技能序号['G1科罗纳']].被动倍率
        self.技能栏[self.技能序号['G1磁力弹']].等级 = self.技能栏[self.技能序号['G1科罗纳']].等级

        # for i in [17, 18, 19]:
        #self.技能栏[i].等级 = self.技能栏[17].等级
        #self.技能栏[self.技能序号['GSP猎鹰捕食者形态']].等级 = self.技能栏[self.技能序号['GSP猎鹰旋雷者形态']].等级 = self.技能栏[self.技能序号['GSP猎鹰科罗纳形态']].等级


class 重霄·机械师·女(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业角色属性()
        self.角色属性A = 职业角色属性()
        self.角色属性B = 职业角色属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)

    def 护石类型选项更新(self, x):
        self.护石类型选项[x].clear()
        if self.护石栏[x].currentText() != '无':
            if self.护石栏[x].currentText() != 'GSP猎鹰':
                try:
                    self.护石类型选项[x].addItems(
                        self.初始属性.技能栏[self.初始属性.技能序号[self.护石栏[x].currentText()]].护石选项)
                except:
                    self.护石类型选项[x].addItem('魔界')
                    self.护石栏[x].setCurrentIndex(0)
            else:
                self.护石类型选项[x].addItem('圣痕')
        else:
            self.护石类型选项[x].addItem('魔界')

    def 界面(self):
        super().界面()
        self.一觉减CD开关 = QCheckBox('ฅ一觉减CD Buffღ', self.main_frame2)
        self.一觉减CD开关.setChecked(False)
        self.一觉减CD开关.resize(120, 20)
        self.一觉减CD开关.move(325, 400)
        self.一觉减CD开关.setStyleSheet(复选框样式)

        self.职业存档.append(('一觉减CD开关', self.一觉减CD开关, 0))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.一觉减CD开关.isChecked():
            属性.技能栏[属性.技能序号['G0战争领主']].一觉减CD = 0.1

    def 加载护石(self, 属性):
        for k in range(3):
            if self.护石栏[k].currentText() != '无' and self.护石栏[k].currentText() != 'GSP猎鹰':
                try:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石()
                except:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石(
                        self.护石类型选项[k].currentIndex())
            elif self.护石栏[k].currentText() == 'GSP猎鹰':
                属性.技能栏[self.角色属性A.技能序号['GSP猎鹰科罗纳形态']].装备护石(0)
                属性.技能栏[self.角色属性A.技能序号['GSP猎鹰旋雷者形态']].装备护石(0)
                属性.技能栏[self.角色属性A.技能序号['GSP猎鹰捕食者形态']].装备护石(0)

        属性.护石第一栏 = self.护石栏[0].currentText()
        属性.护石第二栏 = self.护石栏[1].currentText()
        属性.护石第三栏 = self.护石栏[2].currentText()

        if self.复选框列表[7].isChecked():
            if 属性.技能栏[self.角色属性A.技能序号['空战机械：狂风']].装备护石 == 1:
                属性.技能栏[self.角色属性A.技能序号['空战机械：狂风']].CD *= 0.80

        for i in range(9):
            if self.符文[i].currentText() != '无' and self.符文效果[i].currentText() != '无' and self.符文[i].currentText() != 'GSP猎鹰':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率 *= 1 + int(
                            j.replace('攻击', '').replace('%', '')) / 100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD *= 1 + int(
                            j.replace('CD', '').replace('%', '')) / 100
            elif self.符文[i].currentText() == 'GSP猎鹰':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号['GSP猎鹰捕食者形态']].倍率 *= 1 + \
                            int(j.replace('攻击', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['GSP猎鹰旋雷者形态']].倍率 *= 1 + \
                            int(j.replace('攻击', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['GSP猎鹰科罗纳形态']].倍率 *= 1 + \
                            int(j.replace('攻击', '').replace('%', '')) / 100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号['GSP猎鹰捕食者形态']].CD *= 1 + \
                            int(j.replace('CD', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['GSP猎鹰旋雷者形态']].CD *= 1 + \
                            int(j.replace('CD', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['GSP猎鹰科罗纳形态']].CD *= 1 + \
                            int(j.replace('CD', '').replace('%', '')) / 100
