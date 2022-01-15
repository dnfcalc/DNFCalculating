from PublicReference.carry.base import *


class 职业主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    data0 = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []

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
        if len(self.data4) >= self.等级 and len(self.data4) > 0:
            等效倍率 += self.data4[self.等级] * self.攻击次数4
        if len(self.data5) >= self.等级 and len(self.data5) > 0:
            等效倍率 += self.data5[self.等级] * self.攻击次数5
        if len(self.data6) >= self.等级 and len(self.data6) > 0:
            等效倍率 += self.data6[self.等级] * self.攻击次数6
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能0(职业主动技能):
    名称 = '别过来！'
    所在等级 = 5
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50

    data0 = [int(i*1.22)for i in [0, 2441, 2688, 2936, 3184, 3431, 3679, 3927, 4174, 4422, 4670, 4917, 5165, 5413, 5661, 5908, 6156, 6404, 6651, 6899, 7147, 7394, 7642, 7890, 8137, 8385, 8633, 8880, 9128, 9376, 9623, 9871, 10119, 10366, 10614, 10862,
                                  11109, 11357, 11605, 11852, 12100, 12348, 12595, 12843, 13091, 13338, 13586, 13834, 14081, 14329, 14577, 14824, 15072, 15320, 15567, 15815, 16063, 16310, 16558, 16806, 17053, 17301, 17549, 17796, 18044, 18292, 18539, 18787, 19035, 19282, 19530]]
    攻击次数 = 3
    CD = 6
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能1(职业主动技能):
    名称 = '玫瑰藤蔓'
    所在等级 = 10
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    # 与站位相关，站位可能导致只能打一半
    data0 = [int(i*1.22)for i in [0, 533, 586, 640, 695, 748, 803, 857, 911, 965, 1019, 1074, 1127, 1181, 1236, 1289, 1344, 1398, 1451, 1506, 1560, 1615, 1668, 1722, 1777, 1830, 1885, 1939, 1992,
                                  2047, 2101, 2155, 2209, 2263, 2317, 2371, 2426, 2479, 2533, 2588, 2641, 2696, 2750, 2803, 2858, 2912, 2967, 3020, 3074, 3129, 3182, 3237, 3291, 3344, 3399, 3453, 3507, 3561, 3615, 3669, 3723]]
    攻击次数 = 4
    data1 = [int(i*1.072)for i in [0, 79, 87, 95, 103, 111, 119, 127, 135, 143, 151, 159, 167, 175, 183, 191, 199, 207, 215, 222, 230, 238, 246, 254, 262, 270, 278, 286,
                                   294, 302, 310, 318, 326, 334, 342, 350, 358, 367, 375, 383, 391, 399, 407, 415, 423, 431, 439, 447, 455, 463, 471, 479, 487, 495, 503, 511, 519, 527, 535, 543, 551]]
    攻击次数1 = 4
    CD = 5
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能2(职业主动技能):
    名称 = '疯狂乱抓'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    data0 = [int(i*1.22)for i in [0, 792, 873, 952, 1033, 1114, 1194, 1274, 1354, 1435, 1516, 1595, 1676, 1757, 1837, 1918, 1997, 2078, 2159, 2239, 2319, 2399, 2480, 2561, 2640, 2721, 2802, 2882, 2963, 3042, 3123, 3204,
                                  3284, 3364, 3444, 3525, 3606, 3686, 3766, 3847, 3927, 4008, 4087, 4168, 4249, 4329, 4409, 4489, 4570, 4651, 4731, 4811, 4892, 4972, 5053, 5132, 5213, 5294, 5374, 5455, 5534, 5615, 5696, 5776, 5856, 5937, 6017]]
    攻击次数 = 2
    CD = 4
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能3(被动技能):
    名称 = '人偶操纵者'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 3
    等级上限 = 50
    自定义描述 = 1

    智力 = [0, 69, 73, 77, 81, 85, 90, 95, 100, 106, 112, 118, 124, 130, 137, 144, 152, 160, 168, 176, 184, 193, 202, 212, 221, 231, 241, 252, 262, 273, 284,
          296, 308, 320, 332, 344, 358, 371, 384, 398, 412, 426, 440, 456, 470, 486, 502, 518, 534, 550, 567, 581, 597, 613, 629, 645, 660, 676, 692, 708, 724]

    额外智力 = 0

    def 加成倍率(self, 武器类型):
        return 1.0

    def 加成智力(self):
        return self.智力[self.等级] + self.额外智力

    def 技能描述(self, 武器类型):
        return "智力增加量："+str(self.加成智力())


class 技能4(被动技能):
    名称 = '邪恶的好奇心'
    所在等级 = 20
    等级上限 = 20
    学习间隔 = 20
    等级上限 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + self.等级*0.15, 3)


class 技能5(被动技能):
    名称 = '小魔女的偏爱'
    所在等级 = 20
    等级上限 = 1
    学习间隔 = 3
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['疯狂乱抓', '疯熊火箭拳', '疯熊守护', '疯疯熊坠击', '变大吧！疯疯熊', '哇咔咔！', '咆哮吧！疯疯熊']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1, 3)


class 技能6(职业主动技能):
    名称 = '疯熊火箭拳'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    data0 = [int(i*1.054)for i in [0, 3058, 3369, 3680, 3989, 4300, 4610, 4921, 5230, 5541, 5852, 6162, 6472, 6782, 7093, 7404, 7713, 8024, 8334, 8645, 8954, 9265, 9576, 9886, 10196, 10506, 10817, 11128, 11437, 11748, 12058, 12369, 12678, 12989, 13300, 13610,
                                   13920, 14230, 14541, 14852, 15161, 15472, 15782, 16093, 16403, 16713, 17024, 17334, 17644, 17955, 18265, 18576, 18885, 19196, 19507, 19817, 20127, 20437, 20748, 21058, 21368, 21679, 21989, 22300, 22609, 22920, 23231, 23541, 23851, 24161, 24472]]
    攻击次数 = 1
    CD = 6
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能7(职业主动技能):
    名称 = '蔷薇藤鞭'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    data0 = [int(i*1.054)for i in [0, 2290, 2655, 3019, 3384, 3749, 4115, 4480, 4845, 5210, 5575, 5940, 6305, 6670, 7035, 7401, 7766, 8131, 8496, 8861, 9226, 9591, 9956, 10321, 10687, 11052, 11417, 11782, 12147, 12512,
                                   12877, 13242, 13607, 13973, 14338, 14703, 15068, 15433, 15798, 16163, 16528, 16893, 17259, 17624, 17989, 18354, 18719, 19084, 19449, 19813, 20178, 20543, 20909, 21274, 21639, 22004, 22369, 22734, 23099, 23464, 23829]]
    攻击次数 = 2
    CD = 10
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能8(职业主动技能):
    名称 = '火热的爱意'
    所在等级 = 25
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    data0 = [int(i*1.211)for i in [0, 985, 1142, 1299, 1456, 1613, 1771, 1928, 2085, 2242, 2399, 2556, 2713, 2870, 3027, 3184, 3341, 3498, 3655,
                                   3813, 3970, 4127, 4284, 4441, 4598, 4755, 4912, 5069, 5226, 5383, 5540, 5698, 5855, 6012, 6169, 6326, 6483, 6640, 6797, 6954, 7111]]
    攻击次数 = 3
    CD = 10
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能9(职业主动技能):
    名称 = '疯熊守护'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    data0 = [int(i*1.251)for i in [0, 4286, 4722, 5157, 5592, 6026, 6461, 6897, 7332, 7766, 8201, 8636, 9072, 9506, 9941, 10376, 10812, 11246, 11681, 12116, 12550, 12986, 13421, 13856, 14290, 14725, 15161, 15596, 16030, 16465,
                                   16900, 17336, 17770, 18205, 18640, 19075, 19510, 19945, 20380, 20815, 21250, 21685, 22120, 22555, 22989, 23425, 23860, 24295, 24729, 25164, 25600, 26035, 26469, 26904, 27339, 27775, 28209, 28644, 29079, 29513, 29949]]
    攻击次数 = 5
    CD = 10
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能10(职业主动技能):
    名称 = '疯疯熊坠击'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    data0 = [int(i*1.123)for i in [0, 7479, 8237, 8996, 9755, 10514, 11272, 12031, 12790, 13548, 14308, 15066, 15826, 16584, 17342, 18102, 18860, 19619, 20378, 21136, 21895, 22654, 23413, 24171, 24931, 25689, 26447, 27207, 27965, 28725, 29483, 30241, 31001, 31759,
                                   32518, 33277, 34036, 34794, 35553, 36312, 37070, 37830, 38588, 39346, 40106, 40864, 41624, 42382, 43140, 43900, 44658, 45417, 46176, 46935, 47693, 48452, 49211, 49969, 50729, 51487, 52245, 53005, 53763, 54522, 55281, 56040, 56799, 57557, 58316, 59075, 59834]]
    攻击次数 = 1
    CD = 15
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.倍率 *= 1.40


class 技能11(职业主动技能):
    名称 = '蔷薇囚狱'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    data0 = [int(i*1.251)for i in [0, 674, 742, 811, 879, 948, 1016, 1085, 1153, 1221, 1290, 1358, 1427, 1495, 1563, 1632, 1700, 1769, 1837, 1906, 1974, 2042, 2111, 2179, 2248, 2316, 2385, 2453, 2521,
                                   2590, 2658, 2727, 2795, 2864, 2932, 3000, 3069, 3137, 3206, 3274, 3343, 3411, 3479, 3548, 3616, 3685, 3753, 3822, 3890, 3958, 4027, 4095, 4164, 4232, 4300, 4369, 4437, 4506, 4574, 4643, 4711]]
    攻击次数 = 6
    data1 = [int(i*1.251)for i in [0, 5058, 5571, 6084, 6598, 7111, 7624, 8137, 8650, 9164, 9677, 10190, 10703, 11216, 11729, 12243, 12756, 13269, 13782, 14295, 14809, 15322, 15835, 16348, 16861, 17374, 17888, 18401, 18914, 19427,
                                   19940, 20454, 20967, 21480, 21993, 22506, 23019, 23533, 24046, 24559, 25072, 25585, 26099, 26612, 27125, 27638, 28151, 28665, 29178, 29691, 30204, 30717, 31230, 31744, 32257, 32770, 33283, 33796, 34310, 34823, 35336]]

    攻击次数1 = 1
    data2 = [int(i*1.251)for i in [0, 91, 101, 110, 119, 129, 138, 147, 157, 166, 175, 185, 194, 203, 213, 222, 231, 241, 250, 259, 269, 278, 287, 297, 306, 315, 325, 334,
                                   343, 353, 362, 371, 381, 390, 399, 409, 418, 427, 437, 446, 455, 465, 474, 483, 493, 502, 511, 521, 530, 539, 549, 558, 567, 577, 586, 595, 605, 614, 623, 633, 642]]
    攻击次数2 = 6+1
    CD = 20
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能12(职业主动技能):
    名称 = '死命召唤'
    所在等级 = 40
    等级上限 = 11
    学习间隔 = 2
    等级精通 = 1
    data0 = [int(i*1.119)for i in [0, 12483, 14473, 16463, 18453, 20443, 22433, 24423, 26413, 28404, 30394, 32384, 34374, 36364, 38354, 40344, 42334, 44324, 46314, 48304, 50295, 52285, 54275, 56265, 58255, 60245, 62235, 64225, 66215, 68205, 70195, 72186, 74176, 76166, 78156, 80146,
                                   82136, 84126, 86116, 88106, 90096, 92086, 94077, 96067, 98057, 100047, 102037, 104027, 106017, 108007, 109997, 111987, 113977, 115968, 117958, 119948, 121938, 123928, 125918, 127908, 129898, 131888, 133878, 135868, 137859, 139849, 141839, 143829, 145819, 147809, 149799]]
    攻击次数 = 1
    CD = 7
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.倍率 *= 1.16


class 技能13(职业主动技能):
    名称 = '林中小屋'
    所在等级 = 45
    等级上限 = 11
    学习间隔 = 2
    等级精通 = 1
    data0 = [int(i*1.0)for i in [0, 1493, 1645, 1796, 1948, 2100, 2251, 2403, 2554, 2706, 2857, 3009, 3160, 3312, 3464, 3615, 3767, 3918, 4070, 4221, 4373, 4524, 4676, 4828, 4979, 5131, 5282, 5434, 5585, 5737, 5888, 6040, 6192, 6343, 6495,
                                 6646, 6798, 6949, 7101, 7252, 7404, 7556, 7707, 7859, 8010, 8162, 8313, 8465, 8616, 8768, 8920, 9071, 9223, 9374, 9526, 9677, 9829, 9980, 10132, 10284, 10435, 10587, 10738, 10890, 11041, 11193, 11344, 11496, 11648, 11799, 11951]]
    攻击次数 = 4
    CD = 1


class 技能14(职业主动技能):
    名称 = '变大吧！疯疯熊'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    data0 = [int(i*1.241)for i in [0, 2107, 2321, 2535, 2749, 2963, 3177, 3390, 3604, 3818, 4032, 4246, 4460, 4673, 4887, 5101, 5315, 5529, 5743, 5956, 6170, 6384, 6598, 6812, 7026, 7239, 7453, 7667, 7881, 8095, 8309, 8522, 8736, 8950, 9164, 9378,
                                   9592, 9805, 10019, 10233, 10447, 10661, 10875, 11088, 11302, 11516, 11730, 11944, 12158, 12372, 12585, 12799, 13013, 13227, 13441, 13655, 13868, 14082, 14296, 14510, 14724, 14938, 15151, 15365, 15579, 15793, 16007, 16221, 16434, 16648, 16862]]
    攻击次数 = 6
    data1 = [int(i*1.241)for i in [0, 8431, 9286, 10141, 10997, 11852, 12708, 13563, 14418, 15274, 16129, 16984, 17840, 18695, 19550, 20406, 21261, 22116, 22972, 23827, 24682, 25538, 26393, 27248, 28104, 28959, 29814, 30670, 31525, 32381, 33236, 34091, 34947, 35802,
                                   36657, 37513, 38368, 39223, 40079, 40934, 41789, 42645, 43500, 44355, 45211, 46066, 46921, 47777, 48632, 49488, 50343, 51198, 52054, 52909, 53764, 54620, 55475, 56330, 57186, 58041, 58896, 59752, 60607, 61462, 62318, 63173, 64028, 64884, 65739, 66594, 67450]]
    攻击次数1 = 1
    CD = 45
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.倍率 *= 1.25


class 技能15(被动技能):
    名称 = '少女的爱'
    所在等级 = 48
    等级上限 = 40
    学习间隔 = 3
    等级上限 = 30
    自定义描述 = 1
    智力 = [0, 14, 37, 59, 82, 104, 127, 149, 172, 194, 217, 239, 262, 284, 307, 329, 352, 374, 397, 419, 442,
          464, 487, 509, 532, 554, 577, 599, 622, 644, 667, 689, 712, 734, 757, 779, 802, 824, 847, 869, 892]

    额外智力 = 0

    def 加成倍率(self, 武器类型):
        return 1.0

    def 加成智力(self):
        return self.智力[self.等级] + self.额外智力

    def 技能描述(self, 武器类型):
        return "智力增加量："+str(self.加成智力())


class 技能16(职业主动技能):
    名称 = '开幕！人偶剧场'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    data0 = [int(i*1.251)for i in [0, 54948, 67690, 80431, 93173, 105914, 118657, 131399, 144141, 156882, 169624, 182366, 195107, 207849, 220590, 233332, 246074, 258815, 271557,
                                   284299, 297040, 309782, 322525, 335267, 348008, 360750, 373491, 386233, 398975, 411716, 424458, 437200, 449941, 462683, 475425, 488166, 500908, 513650, 526392, 539134, 551876]]
    攻击次数 = 1
    CD = 170


class 技能17(职业主动技能):
    名称 = '人偶戏法'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    data0 = [int(i*1.25)for i in [0, 1256, 1383, 1511, 1638, 1765, 1893, 2021, 2148, 2275, 2402, 2531, 2658, 2785, 2913, 3040, 3167, 3295, 3423,
                                  3550, 3677, 3804, 3932, 4060, 4187, 4315, 4442, 4569, 4697, 4825, 4952, 5079, 5206, 5334, 5462, 5589, 5716, 5844, 5971, 6099, 6227]]
    攻击次数 = 4
    data1 = [int(i*1.25)for i in [0, 5024, 5534, 6044, 6553, 7064, 7574, 8084, 8593, 9103, 9613, 10123, 10632, 11142, 11652, 12161, 12671, 13182, 13692, 14201,
                                  14711, 15221, 15730, 16240, 16750, 17260, 17769, 18279, 18789, 19298, 19809, 20319, 20829, 21338, 21848, 22358, 22868, 23377, 23887, 24397, 24906]]
    攻击次数1 = 1
    CD = 45
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.data1 = [int(i*2.24) for i in self.data1]


class 技能18(职业主动技能):
    名称 = '哇咔咔！'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    data0 = [int(i*1.251)for i in [0, 2770, 3051, 3332, 3612, 3894, 4175, 4456, 4737, 5018, 5299, 5580, 5862, 6142, 6423, 6704, 6985, 7266, 7548, 7829,
                                   8110, 8391, 8671, 8952, 9233, 9515, 9796, 10077, 10358, 10639, 10920, 11200, 11482, 11763, 12044, 12325, 12606, 12887, 13168, 13450, 13731]]
    攻击次数 = 10
    CD = 40
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.倍率 *= 1.22


class 技能19(职业主动技能):
    名称 = '苦痛庭院'
    所在等级 = 75
    等级上限 = 30
    学习间隔 = 2
    等级精通 = 40
    data0 = [int(i*1.25)for i in [0, 2512, 2767, 3022, 3277, 3531, 3786, 4042, 4297, 4552, 4807, 5061, 5316, 5571, 5826, 6081,
                                  6336, 6590, 6846, 7101, 7356, 7611, 7866, 8120, 8375, 8630, 8885, 9140, 9395, 9649, 9905, 10160, 10415, 10670, 10925]]
    攻击次数 = 9
    data1 = [int(i*1.25)for i in [0, 558, 615, 671, 727, 784, 841, 898, 955, 1012, 1067, 1124, 1181, 1238, 1294, 1351,
                                  1408, 1464, 1521, 1577, 1634, 1691, 1748, 1804, 1860, 1917, 1974, 2031, 2088, 2144, 2200, 2257, 2314, 2371, 2427]]
    攻击次数1 = 10
    data2 = [int(i*1.25)for i in [0, 22614, 24909, 27203, 29498, 31791, 34085, 36380, 38674, 40968, 43262, 45557, 47851, 50146, 52439, 54734,
                                  57028, 59323, 61616, 63911, 66205, 68500, 70794, 73088, 75382, 77677, 79971, 82266, 84559, 86853, 89148, 91442, 93736, 96030, 98325]]
    攻击次数2 = 1
    CD = 40

    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.倍率 *= 1.28
            self.CD *= 0.9


class 技能20(被动技能):
    名称 = '冥月绽放'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    额外智力 = 0
    自定义描述 = 1
    智力 = [0, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330,
          340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540]

    额外智力 = 0

    def 加成倍率(self, 武器类型):
        return round(1.22+0.02*self.等级, 3)

    def 加成智力(self):
        return self.智力[self.等级] + self.额外智力

    def 技能描述(self, 武器类型):
        return '''智力增加量：{}<br>
            技能攻击力加成：{}%<br>
            属性抗性减少量：20*3
        '''.format(str(self.加成智力()), str(22+2*self.等级))


class 技能21(职业主动技能):
    名称 = '咆哮吧！疯疯熊'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    data0 = [int(i*1.25)for i in [0, 2094, 2306, 2519, 2731, 2944, 3156, 3369, 3581, 3794, 4006, 4219, 4431, 4644, 4856, 5069, 5281, 5494, 5706, 5919, 6131, 6344, 6556, 6769, 6981, 7193, 7406, 7618, 7831, 8043, 8256, 8468, 8681, 8893, 9106, 9318,
                                  9531, 9743, 9956, 10168, 10381, 10593, 10806, 11018, 11231, 11443, 11656, 11868, 12081, 12293, 12505, 12718, 12930, 13143, 13355, 13568, 13780, 13993, 14205, 14418, 14630, 14843, 15055, 15268, 15480, 15693, 15905, 16118, 16330, 16543, 16755]]
    攻击次数 = 24
    CD = 45

    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.倍率 *= 1.12*1.25


class 技能22(职业主动技能):
    名称 = '欢迎光临人偶之森'
    所在等级 = 85
    等级上限 = 60
    学习间隔 = 5
    等级精通 = 50
    data0 = [int(i*1.251)for i in [0, 6681, 8230, 9780, 11329, 12878, 14428, 15977, 17526, 19075, 20625, 22174, 23723, 25273, 26822, 28371, 29921, 31470, 33019, 34568, 36118, 37667, 39216, 40766, 42315, 43864, 45414, 46963, 48512, 50061, 51611, 53160, 54709, 56259, 57808,
                                   59357, 60907, 62456, 64005, 65554, 67104, 68653, 70202, 71752, 73301, 74850, 76400, 77949, 79498, 81047, 82597, 84146, 85695, 87245, 88794, 90343, 91892, 93442, 94991, 96540, 98090, 99639, 101188, 102738, 104287, 105836, 107385, 108935, 110484, 112033, 113583]]
    攻击次数 = 7
    data1 = [int(i*1.251)for i in [0, 23385, 28807, 34230, 39652, 45075, 50497, 55920, 61342, 66765, 72187, 77610, 83033, 88455, 93878, 99300, 104723, 110145, 115568, 120990, 126413, 131835, 137258, 142681, 148103, 153526, 158948, 164371, 169793, 175216, 180638, 186061, 191483, 196906, 202329,
                                   207751, 213174, 218596, 224019, 229441, 234864, 240286, 245709, 251131, 256554, 261976, 267399, 272822, 278244, 283667, 289089, 294512, 299934, 305357, 310779, 316202, 321624, 327047, 332470, 337892, 343315, 348737, 354160, 359582, 365005, 370427, 375850, 381272, 386695, 392118, 397540]]
    攻击次数1 = 2
    data2 = [int(i*1.251)for i in [0, 62359, 76819, 91279, 105739, 120199, 134660, 149119, 163579, 178040, 192500, 206960, 221420, 235880, 250340, 264801, 279260, 293720, 308181, 322641, 337102, 351561, 366021, 380482, 394942, 409402, 423862, 438322, 452782, 467243, 481702, 496162, 510623, 525083, 539543,
                                   554003, 568463, 582923, 597384, 611843, 626303, 640764, 655224, 669684, 684144, 698604, 713064, 727525, 741984, 756444, 770905, 785365, 799825, 814285, 828745, 843205, 857666, 872126, 886585, 901046, 915506, 929967, 944426, 958886, 973347, 987807, 1002267, 1016727, 1031187, 1045647, 1060108]]
    攻击次数2 = 1
    CD = 180


class 技能23(被动技能):
    名称 = '不祥的微笑'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    自定义描述 = 1
    额外智力 = 0

    智力 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340,
          350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

    def 加成智力(self):
        return self.智力[self.等级] + self.额外智力

    def 技能描述(self, 武器类型):

        return '''智力增加量：{}<br>
            技能攻击力加成：{}%
        '''.format(str(self.加成智力()), str(18+2*self.等级))


class 技能24(职业主动技能):
    名称 = '挚爱囚笼'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    data0 = [int(i*1.251)for i in [0, 12271, 13516, 14760, 16005, 17250, 18495, 19740, 20985, 22230, 23475, 24720, 25965, 27209, 28454, 29699,
                                   30944, 32189, 33434, 34679, 35924, 37169, 38414, 39658, 40903, 42148, 43393, 44638, 45883, 47128, 48373, 49618, 50863, 52107, 53352]]
    攻击次数 = 3
    data1 = [int(i*1.251)for i in [0, 4772, 5256, 5740, 6224, 6708, 7192, 7676, 8161, 8645, 9129, 9613, 10097, 10581, 11065, 11549, 12034,
                                   12518, 13002, 13486, 13970, 14454, 14938, 15422, 15907, 16391, 16875, 17359, 17843, 18327, 18811, 19295, 19780, 20264, 20748]]
    攻击次数1 = 6
    data2 = [int(i*1.251)for i in [0, 8180, 9010, 9840, 10670, 11500, 12330, 13160, 13990, 14820, 15650, 16480, 17310, 18139, 18969, 19799,
                                   20629, 21459, 22289, 23119, 23949, 24779, 25609, 26439, 27269, 28099, 28929, 29759, 30588, 31418, 32248, 33078, 33908, 34738, 35568]]
    攻击次数2 = 2
    CD = 60


class 技能25(职业主动技能):
    名称 = '终幕！人偶剧场'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    data0 = [int(i*1.251)for i in [0, 4577, 5638, 6700, 7761, 8822, 9883, 10946, 12007, 13068, 14129, 15190, 16252, 17314, 18375, 19436, 20498, 21559, 22620, 23682, 24743, 25805, 26866, 27927, 28988, 30050, 31112, 32173, 33234, 34295, 35357, 36419, 37480, 38541,
                                   39602, 40664, 41725, 42787, 43848, 44909, 45971, 47032, 48094, 49155, 50217, 51278, 52339, 53400, 54462, 55524, 56585, 57646, 58707, 59769, 60831, 61892, 62953, 64014, 65076, 66137, 67199, 68260, 69321, 70383, 71444, 72505, 73567, 74629, 75690, 76751, 77812]]
    攻击次数 = 8
    data1 = [int(i*1.251)for i in [0, 18308, 22554, 26799, 31045, 35291, 39536, 43782, 48028, 52272, 56518, 60764, 65009, 69255, 73501, 77746, 81992, 86237, 90483, 94728, 98974, 103220, 107465, 111711, 115956, 120201, 124447, 128693, 132938, 137184, 141430, 145675, 149920, 154166, 158411,
                                   162657, 166903, 171148, 175394, 179639, 183885, 188130, 192376, 196622, 200867, 205113, 209359, 213603, 217849, 222095, 226340, 230586, 234832, 239077, 243322, 247568, 251813, 256059, 260305, 264550, 268796, 273042, 277287, 281532, 285778, 290024, 294269, 298515, 302761, 307005, 311251]]
    攻击次数1 = 3
    data2 = [int(i*1.251)for i in [0, 274633, 338316, 402000, 465683, 529366, 593049, 656732, 720416, 784099, 847782, 911465, 975148, 1038832, 1102515, 1166199, 1229882, 1293565, 1357249, 1420932, 1484615, 1548298, 1611981, 1675665, 1739348, 1803031, 1866714, 1930397, 1994081, 2057764, 2121447, 2185130, 2248813, 2312497, 2376180,
                                   2439863, 2503546, 2567230, 2630913, 2694596, 2758279, 2821962, 2885646, 2949329, 3013012, 3076695, 3140378, 3204062, 3267745, 3331428, 3395111, 3458794, 3522478, 3586161, 3649844, 3713527, 3777210, 3840894, 3904577, 3968260, 4031943, 4095627, 4159310, 4222993, 4286676, 4350359, 4414043, 4477726, 4541409, 4605092, 4668775]]
    攻击次数2 = 1
    CD = 290
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0


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

    实际名称 = '战斗·知源·小魔女'
    角色 = '魔法师(女)'
    职业 = '小魔女'

    武器选项 = ['扫把']
    类型选择 = ['魔法固伤']

    类型 = '魔法固伤'

    防具类型 = '板甲'
    防具精通属性 = ['智力']

    主BUFF = 1.7

    def __init__(self, 技能列表, 技能序号):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.智力 += self.技能栏[self.技能序号['人偶操纵者']].加成智力()
        self.进图智力 += self.技能栏[self.技能序号['少女的爱']].加成智力()
        self.智力 += self.技能栏[self.技能序号['冥月绽放']].加成智力()
        self.火抗输入 -= 60
        self.光抗输入 -= 60
        self.冰抗输入 -= 60
        self.暗抗输入 -= 60


class 战斗·知源·小魔女(角色窗口):
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
