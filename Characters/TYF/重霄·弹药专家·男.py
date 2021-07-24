from math import *
from PublicReference.base import *


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
            等效倍率 += self.data1[self.等级] * self.攻击次数2
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.攻击次数3
        if len(self.data3) >= self.等级 and len(self.data3) > 0:
            等效倍率 += self.data3[self.等级] * self.攻击次数4
        if len(self.data4) >= self.等级 and len(self.data4) > 0:
            等效倍率 += self.data4[self.等级] * self.攻击次数5
        if len(self.data5) >= self.等级 and len(self.data5) > 0:
            等效倍率 += self.data5[self.等级] * self.攻击次数6
        if len(self.data6) >= self.等级 and len(self.data6) > 0:
            等效倍率 += self.data6[self.等级] * self.攻击次数7
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

    # 弹药技能不受武器CD惩罚
    def 等效CD(self, 武器类型, 输出类型):
        return round(self.CD / self.恢复, 1)


class 技能0(被动技能):
    名称 = '弹夹改装'
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
    冷却关联技能 = ['交叉射击', 'M18阔剑地雷', 'C4飞弹', 'G18冰冻手雷', 'G35感电手雷', 'G61重力手雷',
              'G38ARG智能手雷', '爆裂弹', '聚合弹', '重火力支援', '镭射狙击', '凝固汽油弹', '轻火力速射']

    def 加成倍率(self, 武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def 物理攻击力倍率(self, 武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def 魔法攻击力倍率(self, 武器类型):
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


class 技能3(职业主动技能):
    名称 = 'M18阔剑地雷'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    # 基础 = 641.63
    # 成长 = 72.4
    data0 = [int(i*1.1213) for i in [0, 714, 786, 859, 931, 1003, 1076, 1148, 1221, 1293, 1365, 1438, 1510, 1583, 1655, 1728, 1800, 1872, 1945, 2017, 2090, 2162, 2235, 2307, 2379, 2452, 2524, 2597, 2669, 2742, 2814, 2886, 2959, 3031, 3104, 3176, 3248, 3321, 3393, 3466, 3538, 3611, 3683, 3755, 3828, 3900, 3973, 4045, 4118, 4190, 4262, 4335, 4407, 4480, 4552, 4624, 4697, 4769, 4842, 4914, 4987, 5059, 5131, 5204, 5276, 5349, 5421, 5494, 5566, 5638, 5711]]
    攻击次数 = 3
    CD = 6.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能4(职业主动技能):
    名称 = 'G35感电手雷'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [int(i*1.1514) for i in [0,540,595,650,705,760,814,869,924,979,1034,1089,1144,1198,1253,1308,1363,1418,1473,1527,1582,1637,1692,1747,1802,1856,1911,1966,2021,2076,2131,2185,2240,2295,2350,2405,2460,2515,2569,2624,2679,2734,2789,2844,2898,2953,3008,3063,3118,3173,3227,3282,3337,3392,3447,3502,3557,3611,3666,3721,3776]]
    data1 = [int(i*1.00) for i in [0, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
           14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
           14, 14, 14, 14, 14, 14, 14]]
    攻击次数2 = 18

    CD = 3.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    脱手 = 0
    技能施放时间 = 0


    def 等效CD(self, 武器类型, 输出类型):
        # 经过测试,手雷恢复速度无法享受技能冷却恢复加成
        return round(self.CD, 1)

class 技能5(职业主动技能):
    名称 = '交叉射击'
    脱手 = 0
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [int(i*1.3727) for i in [0, 1417, 1561, 1704, 1848, 1992, 2136, 2279, 2423, 2567, 2711, 2854, 2998, 3142, 3286, 3429, 3573, 3717, 3861, 4004, 4148, 4292, 4436, 4579, 4723, 4867, 5011, 5154, 5298, 5442, 5586, 5729, 5873, 6017, 6161, 6304, 6448, 6592, 6736, 6879, 7023, 7167, 7311, 7454, 7598, 7742, 7886, 8029, 8173, 8317, 8461, 8604, 8748, 8892, 9036, 9179, 9323, 9467, 9611, 9754, 9898, 10042, 10186, 10329, 10473, 10617, 10761, 10904, 11048, 11192, 11336]]
    攻击次数 = 3
    技能施放时间 = 0.3
    CD = 10.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能6(职业主动技能):
    名称 = '爆裂弹'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    # 基础 = 622.125
    # 成长 = 105.525
    data0 = [int(i*1.1601) for i in [0, 662, 768, 873, 978, 1084, 1189, 1294, 1400, 1506, 1611, 1717, 1822, 1927, 2033, 2138, 2244, 2350, 2455, 2561, 2666]]
    CD = 5.0


class 技能7(职业主动技能):
    名称 = 'G18冰冻手雷'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data0 = [int(i*1.1567) for i in [0, 675, 744, 812, 881, 949, 1018, 1086, 1155, 1223, 1292, 1360, 1429, 1497, 1566, 1634, 1703, 1772, 1840, 1909, 1977, 2046, 2114, 2183, 2251, 2320, 2388, 2457, 2525, 2594, 2662, 2731, 2799, 2868, 2936, 3005, 3073, 3142, 3210, 3279, 3347, 3416, 3485, 3553, 3622, 3690, 3759, 3827, 3896, 3964, 4033, 4101, 4170, 4238, 4307, 4375, 4444, 4512, 4581, 4649, 4718, 4786, 4855, 4923, 4992, 5060, 5129, 5197, 5266, 5335, 5403]]
    CD = 4.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能8(职业主动技能):
    名称 = '聚合弹'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 8206.58
    # 成长 = 926.53341
    data0 = [int(i*1.1847) for i in [0, 9129, 10056, 10982, 11908, 12834, 13760, 14687, 15613, 16539, 17465, 18392, 19318, 20244, 21170, 22096, 23023, 23949, 24875, 25801, 26728, 27654, 28580, 29506, 30432, 31359, 32285, 33211, 34137, 35064, 35990, 36916, 37842, 38768, 39695, 40621, 41547, 42473, 43399, 44326, 45252, 46178, 47104, 48031, 48957, 49883, 50809, 51735, 52662, 53588, 54514, 55440, 56367, 57293, 58219, 59145, 60071, 60998, 61924, 62850, 63776, 64703, 65629, 66555, 67481, 68407, 69334, 70260, 71186, 72112, 73038]]
    CD = 18.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 技能9(职业主动技能):
    名称 = 'C4飞弹'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 7122.49875
    # 成长 = 804.25125
    data0 = [int(i*1.1598) for i in [0, 7927, 8732, 9536, 10340, 11144, 11949, 12753, 13557, 14361, 15166, 15970, 16774, 17579, 18383, 19187, 19991, 20796, 21600, 22404, 23208, 24013, 24817, 25621, 26426, 27230, 28034, 28838, 29643, 30447, 31251, 32055, 32860, 33664, 34468, 35272, 36077, 36881, 37685, 38490, 39294, 40098, 40902, 41707, 42511, 43315, 44119, 44924, 45728, 46532, 47337, 48141, 48945, 49749, 50554, 51358, 52162, 52966, 53771, 54575, 55379, 56183, 56988, 57792, 58596, 59401, 60205, 61009, 61813, 62618, 63422]]
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.32


class 技能10(职业主动技能):
    名称 = '凝固汽油弹'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data0 = [int(i*1.1825) for i in [0, 9850, 10849, 11848, 12848, 13847, 14846, 15846, 16845, 17844, 18844, 19843, 20842, 21841, 22841, 23840, 24839, 25839, 26838, 27837, 28837, 29836, 30835, 31835, 32834, 33833, 34832, 35832, 36831, 37830, 38830, 39829, 40828, 41828, 42827, 43826, 44826, 45825, 46824, 47823, 48823, 49822, 50821, 51821, 52820, 53819, 54819, 55818, 56817, 57817, 58816, 59815, 60814, 61814, 62813, 63812, 64812, 65811, 66810, 67810, 68809, 69808, 70807, 71807, 72806, 73805, 74805, 75804, 76803, 77803, 78802]]
    data1 = [int(i*1.00) for i in [0, 53, 58, 64, 69, 74, 80, 85, 91, 96, 101, 107, 112, 118, 123, 128, 134, 139, 145, 150, 155, 161, 166, 172, 177, 182, 188, 193, 199, 204, 209, 215, 220, 226, 231, 236, 242, 247, 253, 258, 263, 269, 274, 280, 285, 290, 296, 301, 307, 312, 317, 323, 328, 334, 339, 344, 350, 355, 361, 366, 371, 377, 382, 388, 393, 398, 404, 409, 415, 420, 425]]
    攻击次数2 = 15
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [x * 1.31 for x in self.data0]
            self.攻击次数2 = 0
            self.CD *= 0.94
        elif x == 1:
            self.data0 = [x * 1.40 for x in self.data0]
            self.攻击次数2 = 0
            self.CD *= 0.94


class 技能11(职业主动技能):
    名称 = '镭射狙击'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data0 = [int(i*1.1693) for i in [0, 3360, 3701, 4042, 4383, 4724, 5065, 5406, 5747, 6088, 6429, 6770, 7110, 7451, 7792, 8133, 8474, 8815, 9156, 9497, 9838, 10179, 10520, 10861, 11202, 11542, 11883, 12224, 12565, 12906, 13247, 13588, 13929, 14270, 14611, 14952, 15293, 15633, 15974, 16315, 16656, 16997, 17338, 17679, 18020, 18361, 18702, 19043, 19384, 19724, 20065, 20406, 20747, 21088, 21429, 21770, 22111, 22452, 22793, 23134, 23475, 23815, 24156, 24497, 24838, 25179, 25520, 25861, 26202, 26543, 26884]]
    攻击次数 = 5
    CD = 45.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.28
            # self.倍率 *= 1.18
        elif x == 1:
            self.倍率 *= 1.36


class 技能12(被动技能):
    名称 = '弹药主宰'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['所有']
    关联技能2 = ['爆裂弹']

    def 加成倍率(self, 武器类型):
        return 1.105 + self.等级 * 0.015 if self.等级 > 0 else 1

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.3


class 技能13(职业主动技能):
    名称 = '黑玫瑰特种战队'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    data0 = [int(i*1.2545) for i in [0, 1789, 2204, 2619, 3034, 3448, 3863, 4278, 4693, 5108, 5523, 5938, 6353, 6768, 7183, 7598, 8013, 8427, 8842, 9257, 9672, 10087, 10502, 10917, 11332, 11747, 12162, 12577, 12991, 13406, 13821, 14236, 14651, 15066, 15481, 15896, 16311, 16726, 17141, 17556, 17970, 18385, 18800, 19215, 19630, 20045, 20460, 20875, 21290, 21705, 22120, 22535, 22949, 23364, 23779, 24194, 24609, 25024, 25439, 25854, 26269, 26684, 27099, 27513, 27928, 28343, 28758, 29173, 29588, 30003, 30418]]
    # 基础 = 1373.97702
    # 成长 = 415.33411
    攻击次数 = 16
    # 基础2 = 242.389
    # 成长2 = 73.91189
    data1 = [int(i*1.2542) for i in [0, 318, 391, 465, 539, 613, 686, 760, 834, 908, 981, 1055, 1129, 1203, 1277, 1350, 1424, 1498, 1572, 1645, 1719, 1793, 1867, 1940, 2014, 2088, 2162, 2235, 2309, 2383, 2457, 2530, 2604, 2678, 2752, 2826, 2899, 2973, 3047, 3121, 3194, 3268, 3342, 3416, 3489, 3563, 3637, 3711, 3784, 3858, 3932, 4006, 4079, 4153, 4227, 4301, 4375, 4448, 4522, 4596, 4670, 4743, 4817, 4891, 4965, 5038, 5112, 5186, 5260, 5333, 5407]]
    # 攻击次数2 = 90 10hit左右无法打到
    攻击次数2 = 80
    CD = 145.0


class 技能14(职业主动技能):
    名称 = 'G61重力手雷'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data0 = [int(i*1.177) for i in [0, 6265, 6901, 7536, 8172, 8808, 9443, 10079, 10715, 11350, 11986, 12622, 13257, 13893, 14529, 15164, 15800, 16436, 17071, 17707, 18342, 18978, 19614, 20249, 20885, 21521, 22156, 22792, 23428, 24063, 24699, 25335, 25970, 26606, 27241, 27877, 28513, 29148, 29784, 30420, 31055, 31691, 32327, 32962, 33598, 34234, 34869, 35505, 36141, 36776, 37412, 38047, 38683, 39319, 39954, 40590, 41226, 41861, 42497, 43133, 43768, 44404, 45040, 45675, 46311, 46947, 47582, 48218, 48853, 49489, 50125]]
    data1 = [int(i*1.1766) for i in [0, 208, 230, 251, 272, 293, 314, 335, 357, 378, 399, 420, 441, 463, 484, 505, 526, 547, 569, 590, 611, 632, 653, 674, 696, 717, 738, 759, 780, 802, 823, 844, 865, 886, 908, 929, 950, 971, 992, 1014, 1035, 1056, 1077, 1098, 1119, 1141, 1162, 1183, 1204, 1225, 1247, 1268, 1289, 1310, 1331, 1353, 1374, 1395, 1416, 1437, 1458, 1480, 1501, 1522, 1543, 1564, 1586, 1607, 1628, 1649, 1670]]
    攻击次数 = 1
    攻击次数2 = 29
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(x*1.83) for x in self.data0]
            self.技能施放时间 = 1.5
            self.攻击次数2 = 15
            # self.倍率 *= 1.18
        elif x == 1:
            self.data0 = [int(x*2.01) for x in self.data0]
            self.技能施放时间 = 1.5
            self.攻击次数2 = 15


class 技能15(职业主动技能):
    名称 = '轻火力速射'
    脱手 = 0
    技能施放时间 = 1
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data0 = [int(i*1.1814) for i in [0, 1229, 1353, 1478, 1602, 1727, 1852, 1976, 2101, 2226, 2350, 2475, 2599, 2724, 2849, 2973, 3098, 3223, 3347, 3472, 3597, 3721, 3846, 3970, 4095, 4220, 4344, 4469, 4594, 4718, 4843, 4968, 5092, 5217, 5341, 5466, 5591, 5715, 5840, 5965, 6089, 6214, 6339, 6463, 6588, 6712, 6837, 6962, 7086, 7211, 7336, 7460, 7585, 7710, 7834, 7959, 8083, 8208, 8333, 8457, 8582, 8707, 8831, 8956, 9080, 9205, 9330, 9454, 9579, 9704, 9828]]
    攻击次数 = 17
    CD = 30.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础2 = self.基础*0.22
            self.成长2 = self.成长*0.22
            self.技能施放时间 = 2
            self.攻击次数2 = 17
            self.CD *= 0.95
            # self.倍率 *= 1.18
        elif x == 1:
            self.基础2 = self.基础*0.36
            self.成长2 = self.成长*0.36
            self.技能施放时间 = 2
            self.攻击次数2 = 17
            self.CD *= 0.95


class 技能16(被动技能):
    名称 = '战地功勋'
    所在等级 = 75
    等级上限 = 30
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 3)


class 技能17(职业主动技能):
    名称 = '重火力支援'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    data0 = [int(i*1.187) for i in [0, 5169, 5693, 6217, 6742, 7266, 7790, 8315, 8839, 9363, 9888, 10412, 10936, 11461, 11985, 12509, 13034, 13558, 14083, 14607, 15131, 15656, 16180, 16704, 17229, 17753, 18277, 18802, 19326, 19850, 20375, 20899, 21423, 21948, 22472, 22996, 23521, 24045, 24569, 25094, 25618, 26143, 26667, 27191, 27716, 28240, 28764, 29289, 29813, 30337, 30862, 31386, 31910, 32435, 32959, 33483, 34008, 34532, 35056, 35581, 36105, 36630, 37154, 37678, 38203, 38727, 39251, 39776, 40300, 40824, 41349]]
    攻击次数 = 10
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self,x):
        if x ==0:
            self.倍率 *= 1.35


class 技能18(职业主动技能):
    名称 = 'G38ARG智能手雷'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 基础 = 13127.83*1.127
    # 成长 = 1482.17*1.127
    data0 = [int(i*1.1534) for i in [0, 16468, 18139, 19809, 21480, 23151, 24821, 26492, 28163, 29833, 31504, 33175, 34846, 36516, 38187, 39858, 41528, 43199, 44870, 46541, 48211, 49882, 51553, 53223, 54894, 56565, 58235, 59906, 61577, 63248, 64918, 66589, 68260, 69930, 71601, 73272, 74942, 76613, 78284, 79955, 81625, 83296, 84967, 86637, 88308, 89979, 91649, 93320, 94991, 96662, 98332, 100003, 101674, 103344, 105015, 106686, 108357, 110027, 111698, 113369, 115039, 116710, 118381, 120051, 121722, 123393, 125064, 126734, 128405, 130076, 131746]]
    攻击次数 = 1
    # 基础2 = 3063.17*1.127
    # 成长2 = 345.83*1.127
    data1 = [int(i*1.1534) for i in [0, 3842, 4232, 4622, 5012, 5401, 5791, 6181, 6571, 6961, 7351, 7740, 8130, 8520, 8910, 9300, 9690, 10079, 10469, 10859, 11249, 11639, 12029, 12418, 12808, 13198, 13588, 13978, 14368, 14757, 15147, 15537, 15927, 16317, 16707, 17096, 17486, 17876, 18266, 18656, 19046, 19435, 19825, 20215, 20605, 20995, 21384, 21774, 22164, 22554, 22944, 23334, 23723, 24113, 24503, 24893, 25283, 25673, 26062, 26452, 26842, 27232, 27622, 28012, 28401, 28791, 29181, 29571, 29961, 30351, 30740]]
    攻击次数2 = 10
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self,x):
        if x==0:
            self.data0 = [int(i*4.22) for i in self.data0]
            self.攻击次数2 = 0


class 技能19(职业主动技能):
    名称 = '超新星核爆'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    data0 = [int(i*1.24) for i in [0, 71384, 87937, 104490, 121043, 137596, 154149, 170702, 187254, 203807, 220360, 236913, 253466, 270019, 286572, 303125, 319678, 336231, 352784, 369337, 385889, 402442, 418995, 435548, 452101, 468654, 485207, 501760, 518313, 534866, 551419, 567972, 584525, 601077, 617630, 634183, 650736, 667289, 683842, 700395, 716948, 733501, 750054, 766607, 783160, 799713, 816265, 832818, 849371, 865924, 882477, 899030, 915583, 932136, 948689, 965242, 981795, 998348, 1014900, 1031453, 1048006, 1064559, 1081112, 1097665, 1114218, 1130771, 1147324, 1163877, 1180430, 1196983, 1213536]]
    data1 = [int(i*1.24) for i in [0, 2039, 2512, 2985, 3458, 3931, 4404, 4877, 5350, 5823, 6296, 6768, 7241, 7714, 8187, 8660, 9133, 9606, 10079, 10552, 11025, 11498, 11971, 12444, 12917, 13390, 13863, 14336, 14808, 15281, 15754, 16227, 16700, 17173, 17646, 18119, 18592, 19065, 19538, 20011, 20484, 20957, 21430, 21903, 22376, 22848, 23321, 23794, 24267, 24740, 25213, 25686, 26159, 26632, 27105, 27578, 28051, 28524, 28997, 29470, 29943, 30415, 30888, 31361, 31834, 32307, 32780, 33253, 33726, 34199, 34672]]
    攻击次数 = 1
    攻击次数2 = 15
    脱手 = 0
    技能施放时间 = 1
    CD = 180.0


class 技能20(被动技能):
    名称 = '赤诚之心'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    关联技能 = ['所有']
    关联技能2 = ['交叉射击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.16

class 技能21(职业主动技能):
    名称 = '皇鹰特战队'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    data0 = [int(i*1.1295) for i in [0, 2206, 2430, 2654, 2878, 3102, 3326, 3550, 3774, 3998, 4222, 4445, 4669, 4893, 5117, 5341, 5565, 5789, 6013, 6237, 6460, 6684, 6908, 7132, 7356, 7580, 7804, 8028, 8252, 8476, 8699, 8923, 9147, 9371, 9595, 9819, 10043, 10267, 10491, 10715, 10938, 11162, 11386, 11610, 11834, 12058, 12282, 12506, 12730, 12953, 13177, 13401, 13625, 13849, 14073, 14297, 14521, 14745, 14969, 15192, 15416, 15640, 15864, 16088, 16312, 16536, 16760, 16984, 17207, 17431, 17655]]
    攻击次数 = 16
    data1 = [int(i*1.1295) for i in [0, 55174, 60771, 66369, 71966, 77563, 83161, 88758, 94356, 99953, 105550, 111148, 116745, 122343, 127940, 133537, 139135, 144732, 150330, 155927, 161524, 167122, 172719, 178316, 183914, 189511, 195109, 200706, 206303, 211901, 217498, 223096, 228693, 234290, 239888, 245485, 251083, 256680, 262277, 267875, 273472, 279070, 284667, 290264, 295862, 301459, 307057, 312654, 318251, 323849, 329446, 335044, 340641, 346238, 351836, 357433, 363030, 368628, 374225, 379823, 385420, 391017, 396615, 402212, 407810, 413407, 419004, 424602, 430199, 435797, 441394]]
    攻击次数2 = 1
    data2 = [int(i*1.1295) for i in [0, 8276, 9115, 9955, 10794, 11634, 12474, 13313, 14153, 14993, 15832, 16672, 17511, 18351, 19191, 20030, 20870, 21709, 22549, 23389, 24228, 25068, 25907, 26747, 27587, 28426, 29266, 30105, 30945, 31785, 32624, 33464, 34304, 35143, 35983, 36822, 37662, 38502, 39341, 40181, 41020, 41860, 42700, 43539, 44379, 45218, 46058, 46898, 47737, 48577, 49416, 50256, 51096, 51935, 52775, 53615, 54454, 55294, 56133, 56973, 57813, 58652, 59492, 60331, 61171, 62011, 62850, 63690, 64529, 65369, 66209]]
    攻击次数3 = 4
    # 基础 = 113194.2
    # 成长 = 12179.8
    CD = 60.0
    脱手 = 0
    技能施放时间 = 0.2


class 技能22(职业主动技能):
    名称 = '赤魂风暴狙击'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 = [int(i*1.1928) for i in [0, 3509, 4323, 5137, 5951, 6765, 7579, 8393, 9207, 10020, 10834, 11648, 12462, 13276, 14090, 14904, 15718, 16532, 17345, 18159, 18973, 19787, 20601, 21415, 22229, 23043, 23857, 24670, 25484, 26298, 27112, 27926, 28740, 29554, 30368, 31182, 31995, 32809, 33623, 34437, 35251, 36065, 36879, 37693, 38507, 39320, 40134, 40948, 41762, 42576, 43390, 44204, 45018, 45832, 46645, 47459, 48273, 49087, 49901, 50715, 51529, 52343, 53157, 53970, 54784, 55598, 56412, 57226, 58040, 58854, 59668]]
    攻击次数 = 12
    data1 = [int(i*1.1928) for i in [0, 147415, 181598, 215781, 249965, 284148, 318331, 352515, 386698, 420881, 455064, 489248, 523431, 557614, 591797, 625981, 660164, 694347, 728531, 762714, 796897, 831080, 865264, 899447, 933630, 967813, 1001997, 1036180, 1070363, 1104547, 1138730, 1172913, 1207096, 1241280, 1275463, 1309646, 1343829, 1378013, 1412196, 1446379, 1480563, 1514746, 1548929, 1583112, 1617296, 1651479, 1685662, 1719845, 1754029, 1788212, 1822395, 1856579, 1890762, 1924945, 1959128, 1993312, 2027495, 2061678, 2095861, 2130045, 2164228, 2198411, 2232595, 2266778, 2300961, 2335144, 2369328, 2403511, 2437694, 2471878, 2506061]]
    攻击次数2 = 1
    data2 = [int(i*1.1928) for i in [0, 52648, 64856, 77064, 89273, 101481, 113689, 125898, 138106, 150314, 162523, 174731, 186939, 199148, 211356, 223564, 235773, 247981, 260189, 272397, 284606, 296814, 309022, 321231, 333439, 345647, 357856, 370064, 382272, 394481, 406689, 418897, 431106, 443314, 455522, 467730, 479939, 492147, 504355, 516564, 528772, 540980, 553189, 565397, 577605, 589814, 602022, 614230, 626439, 638647, 650855, 663063, 675272, 687480, 699688, 711897, 724105, 736313, 748522, 760730, 772938, 785147, 797355, 809563, 821772, 833980, 846188, 858396, 870605, 882813, 895021]]
    攻击次数3 = 4
    data3 = [int(i*1.1928) for i in [0, 2807, 3459, 4110, 4761, 5412, 6063, 6714, 7365, 8016, 8667, 9319, 9970, 10621, 11272, 11923, 12574, 13225, 13876, 14527, 15179, 15830, 16481, 17132, 17783, 18434, 19085, 19736, 20387, 21038, 21690, 22341, 22992, 23643, 24294, 24945, 25596, 26247, 26898, 27550, 28201, 28852, 29503, 30154, 30805, 31456, 32107, 32758, 33410, 34061, 34712, 35363, 36014, 36665, 37316, 37967, 38618, 39270, 39921, 40572, 41223, 41874, 42525, 43176, 43827, 44478, 45130, 45781, 46432, 47083, 47734]]
    攻击次数4 = 3
    data4 = [int(i*1.1928) for i in [0, 12635, 15565, 18495, 21425, 24355, 27285, 30215, 33145, 36075, 39005, 41935, 44865, 47795, 50725, 53655, 56585, 59515, 62445, 65375, 68305, 71235, 74165, 77095, 80025, 82955, 85885, 88815, 91745, 94675, 97605, 100535, 103465, 106395, 109325, 112255, 115185, 118115, 121045, 123975, 126905, 129835, 132765, 135695, 138625, 141555, 144485, 147415, 150345, 153275, 156205, 159135, 162065, 164995, 167925, 170855, 173785, 176715, 179645, 182575, 185505, 188435, 191365, 194295, 197225, 200155, 203085, 206015, 208945, 211875, 214805]]
    攻击次数5 = 1
    CD = 290.0
    脱手 = 0
    技能施放时间 = 6.3
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

class 技能23(被动技能):
    名称 = '弹药改良'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['所有']
    关联技能2 = ['所有']
    #技能加成描述 = ''
    #加成数值 = 1.0

    def 加成倍率(self, 武器类型):
        if (self.等级 < 10):
            return 1.0
        else:
            return round(1.23 + 0.01 * (self.等级-10), 3)

    #自定义描述 = 1

    def 技能描述(self, 武器类型):
        return self.技能加成描述

    def 加成倍率2(self, 武器类型):
        return 1.1

技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能'+str(i)+'())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

重霄·弹药专家·男一觉序号 = 0
重霄·弹药专家·男二觉序号 = 0
重霄·弹药专家·男三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        重霄·弹药专家·男一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        重霄·弹药专家·男二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        重霄·弹药专家·男三觉序号 = 技能序号[i.名称]

重霄·弹药专家·男护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        重霄·弹药专家·男护石选项.append(i.名称)

重霄·弹药专家·男符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1 and i.名称 != '爆裂弹':
        重霄·弹药专家·男符文选项.append(i.名称)


class 重霄·弹药专家·男角色属性(角色属性):

    实际名称 = '重霄·弹药专家·男'
    角色 = '神枪手(男)'
    职业 = '弹药专家'

    武器选项 = ['手弩', '步枪']

    类型选择 = ['魔法百分比', '物理百分比']

    类型 = '魔法百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['智力', '力量']

    超负荷属性 = 0

    主BUFF = 1.84

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 技能释放次数计算(self):
        技能释放次数 = []
        技能消耗时间 = 0.0
        爆裂弹间隔 = 0.115
        每轮射击次数 = 0.5 * \
            (16 + floor(0.5 * (min(self.技能栏[self.技能序号['弹夹改装']].等级, 20)-10)))

        if (self.武器类型 != '手弩'):
            爆裂弹间隔 = 0.14
            每轮射击次数 = 0.5 * \
                (9 + floor(0.5 * (min(self.技能栏[self.技能序号['弹夹改装']].等级, 20)-9)))

        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if i.名称 == '爆裂弹':
                    技能释放次数.append(0)
                else:
                    if '/CD' in self.次数输入[self.技能序号[i.名称]]:
                        技能释放次数.append(
                            int((self.时间输入) / (i.等效CD(self.武器类型, self.类型)+i.技能施放时间) + 1 + i.基础释放次数))
                        if i.脱手 == 1:
                            技能消耗时间 += int((self.时间输入) / (i.等效CD(self.武器类型,
                                          self.类型) + i.技能施放时间) + 1 + i.基础释放次数) * 0.2
                        else:
                            技能消耗时间 += int((self.时间输入) / (i.等效CD(self.武器类型,
                                          self.类型) + i.技能施放时间) + 1 + i.基础释放次数) * i.技能施放时间
                    elif self.次数输入[self.技能序号[i.名称]] != '0':
                        技能释放次数.append(
                            round(float(self.次数输入[self.技能序号[i.名称]]), 2))
                    else:
                        技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        if '/CD' in self.次数输入[self.技能序号['爆裂弹']]:
            每轮射击时间 = 每轮射击次数 * 爆裂弹间隔
            射击轮次 = int((self.时间输入-技能消耗时间)/每轮射击时间)
            技能释放次数[self.技能序号['爆裂弹']] = int(floor((self.时间输入-技能消耗时间-射击轮次*0.2)/爆裂弹间隔))
        else:
            if self.次数输入[self.技能序号['爆裂弹']] != '0':
                技能释放次数[self.技能序号['爆裂弹']] = round(
                    self.次数输入[self.技能序号['爆裂弹']], 2)*每轮射击次数
            else:
                技能释放次数[self.技能序号['爆裂弹']] = 0
                
        return self.技能释放次数解析(技能释放次数)

    def 伤害指数计算(self):
        super().伤害指数计算()

    #def 预处理(self):
    #    if self.超负荷属性 == 0:
    #        self.技能栏[self.技能序号['弹药改良']].加成数值 = 1.1
    #        self.技能栏[self.技能序号['弹药改良']].自定义描述 = 0
    #    if self.超负荷属性 == 1:
    #        self.技能栏[self.技能序号['弹药改良']].技能加成描述 = '火属性强化增加：36'
    #        self.火属性强化 += 36
    #    if self.超负荷属性 == 2:
    #        self.技能栏[self.技能序号['弹药改良']].技能加成描述 = '冰属性强化增加：36'
    #        self.冰属性强化 += 36
    #    if self.超负荷属性 == 3:
    #        self.技能栏[self.技能序号['弹药改良']].技能加成描述 = '光属性强化增加：36'
    #        self.光属性强化 += 36
    #    super().预处理()


class 重霄·弹药专家·男(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 重霄·弹药专家·男角色属性()
        self.角色属性A = 重霄·弹药专家·男角色属性()
        self.角色属性B = 重霄·弹药专家·男角色属性()
        self.一觉序号 = 重霄·弹药专家·男一觉序号
        self.二觉序号 = 重霄·弹药专家·男二觉序号
        self.三觉序号 = 重霄·弹药专家·男三觉序号
        self.护石选项 = deepcopy(重霄·弹药专家·男护石选项)
        self.符文选项 = deepcopy(重霄·弹药专家·男符文选项)

    #def 输入属性(self, 属性, x=0):
    #    super().输入属性(属性, x)
      #  属性.超负荷属性 = self.超负荷属性选择.currentIndex()


    #def 界面2(self):
    #    super().界面2()

    #    self.超负荷属性选择 = MyQComboBox(self.main_frame2)
    #    self.超负荷属性选择.addItems(['超负荷装填：无', '超负荷装填：火', '超负荷装填：冰', '超负荷装填：光'])
    #    self.超负荷属性选择.resize(120, 20)
    #    self.超负荷属性选择.move(325, 420)