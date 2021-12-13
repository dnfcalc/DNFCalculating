from math import *
from PublicReference.carry.base import *

# 技能后的倍率是魔化后的倍率


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
    魔化 = 1.0

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
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.魔化

class 技能0(职业主动技能):
    名称 = '恶魔之手'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    data0 = [int(x*1.2) for x in [0, 426, 469, 512, 555, 599, 642, 685, 728, 772, 815, 858, 901, 945, 988, 1031, 1074, 1117, 1161, 1204, 1247, 1290,
           1334, 1377, 1420, 1463, 1507, 1550, 1593, 1636, 1680, 1723, 1766, 1809, 1852, 1896, 1939, 1982, 2025, 2069, 2112,
           2155, 2198, 2242, 2285, 2328, 2371, 2415, 2458, 2501, 2544, 2587, 2631, 2674, 2717, 2760, 2804, 2847, 2890, 2933,
           2977, 3020, 3063, 3106, 3150, 3193, 3236, 3279, 3322, 3366, 3409]]
    data1 = [int(x*1.2) for x in [0, 852, 938, 1025, 1111, 1198, 1284, 1371, 1457, 1544, 1630, 1717, 1803, 1890, 1976, 2062, 2149, 2235, 2322, 2408,
           2495, 2581, 2668, 2754, 2841, 2927, 3014, 3100, 3187, 3273, 3360, 3446, 3532, 3619, 3705, 3792, 3878, 3965, 4051,
           4138, 4224, 4311, 4397, 4484, 4570, 4657, 4743, 4830, 4916, 5002, 5089, 5175, 5262, 5348, 5435, 5521, 5608, 5694,
           5781, 5867, 5954, 6040, 6127, 6213, 6300, 6386, 6472, 6559, 6645, 6732, 6818]]
    攻击次数2 = 1
    魔化 = 2.24  # 魔化
    CD = 6 * 1.6
    TP成长 = 0.08
    TP上限 = 5

class 技能1(职业主动技能):
    名称 = '死亡切割'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    data0 = [int(x*1.2) for x in [0, 221, 243, 265, 288, 310, 333, 355, 378, 400, 422, 445, 467, 490, 512, 535, 557, 579, 602, 624, 647, 669, 692, 714, 736, 759, 781, 804, 826, 849, 871, 893, 916, 938, 961, 983, 1006, 1028, 1050, 1073, 1095, 1118, 1140, 1163, 1185, 1207, 1230, 1252, 1275, 1297, 1320, 1342, 1364, 1387, 1409, 1432, 1454, 1477, 1499, 1521, 1544, 1566, 1589, 1611, 1634, 1656, 1678, 1701, 1723, 1746, 1768]]
    攻击次数 = 6
    魔化 = 2.25  # 魔化
    CD = 5 * 1.6
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能2(被动技能):
    名称 = '镰刀精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class 技能3(职业主动技能):
    名称 = '裂地锤'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data0 = [int(x*1.101) for x in [0, 441, 487, 532, 577, 620, 668, 714, 759, 805, 852, 896, 943, 986, 1034, 1079, 1124, 1170, 1216, 1260, 1307, 1351,
           1397, 1444, 1488, 1534, 1582, 1625, 1670, 1716, 1761, 1809, 1852, 1899, 1942, 1990, 2036, 2081, 2127, 2174, 2218,
           2265, 2308, 2354, 2401, 2444, 2492, 2538, 2582, 2629, 2673, 2719, 2765, 2810, 2855, 2902, 2947, 2992, 3038, 3083,
           3128, 3176, 3221, 3266, 3312, 3357, 3402, 3448, 3494, 3539, 3585]]
    攻击次数 = 8  # 最高8hit 三觉优化
    CD = 5 * 1.55
    TP成长 = 0.10
    TP上限 = 5


class 技能4(被动技能):
    名称 = '恶魔诅咒'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['不朽战吼', '地狱之门', '厄运之轮', '恶魔之拳', '恶魔之手', '恶魔之握', '复仇之刺', '黑暗权能',
            '回旋飞镰', '毁灭强击', '裂地锤', '末日浩劫', '死亡切割', '永堕：混沌弑神', '审判', '极恶洪流', '末日福音：毁灭之翼']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.03 * self.等级, 5)


class 技能5(职业主动技能):
    名称 = '回旋飞镰'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [int(x*1.131) for x in [0, 674, 733, 794, 861, 942, 995, 1056, 1131, 1190, 1251, 1311, 1385, 1446, 1507, 1574, 1634, 1694, 1768, 1829, 1903, 1964, 2031, 2091, 2150, 2211, 2286, 2353, 2414, 2481, 2540, 2601, 2668, 2729, 2804, 2863, 2932, 2990, 3051, 3119, 3179, 3260, 3320, 3388, 3447, 3508, 3575, 3636, 3697, 3764, 3838, 3898, 3965, 4026, 4093, 4154, 4214, 4282, 4341, 4415, 4475, 4543, 4603, 4671, 4731, 4797, 4858, 4933, 4993, 5060, 5121]]
    攻击次数 = 1
    data1 = [int(x*1.131) for x in [0, 396, 438, 480, 520, 558, 601, 643, 681, 723, 765, 807, 846, 888, 930, 970, 1012, 1054, 1093, 1135, 1174, 1216, 1256, 1298, 1340, 1382, 1421, 1461, 1503, 1544, 1584, 1626, 1667, 1708, 1748, 1789, 1830, 1872, 1914, 1954, 1996, 2034, 2076, 2116, 2158, 2200, 2240, 2282, 2324, 2364, 2402, 2444, 2485, 2527, 2567, 2609, 2651, 2691, 2733, 2772, 2814, 2854, 2896, 2937, 2978, 3019, 3061, 3100, 3142, 3182, 3224]]
    攻击次数2 = 6  # 最高6hit
    魔化 = 1.9 # 魔化
    CD = 10 * 1.5
    TP成长 = 0.10
    TP上限 = 5

class 技能6(职业主动技能):
    名称 = '复仇之刺'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data0 = [int(x*1.213) for x in [0, 2795, 3079, 3362, 3646, 3930, 4213, 4497, 4780, 5064, 5348, 5631, 5915, 6198, 6482, 6766, 7049, 7333, 7616, 7900, 8184, 8467, 8751, 9034, 9318, 9602, 9885, 10169, 10453, 10736, 11020, 11303, 11587, 11871, 12154, 12438, 12721, 13005, 13289, 13572, 13856, 14139, 14423, 14707, 14990, 15274, 15558, 15841, 16125, 16408, 16692, 16976, 17259, 17543, 17826, 18110, 18394, 18677, 18961, 19244, 19528, 19812, 20095, 20379, 20662, 20946, 21230, 21513, 21797, 22081, 22364]]
    data1 = [int(x*1.213) for x in [0, 4072, 4484, 4897, 5312, 5724, 6137, 6550, 6963, 7375, 7789, 8203, 8616, 9029, 9441, 9855, 10267, 10680, 11095, 11507, 11921, 12333, 12746, 13160, 13573, 13986, 14400, 14812, 15225, 15638, 16051, 16467, 16879, 17291, 17705, 18117, 18529, 18943, 19358, 19771, 20184, 20595, 21010, 21421, 21836, 22250, 22662, 23074, 23489, 23900, 24313, 24729, 25141, 25555, 25967, 26380, 26793, 27206, 27620, 28033, 28446, 28858, 29272, 29684, 30096, 30512, 30924, 31338, 31750, 32163, 32577]]
    攻击次数2 = 1
    CD = 10 * 1.6
    TP成长 = 0.10
    TP上限 = 5


class 技能7(职业主动技能):
    名称 = '厄运之轮'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 36
    data0 = [int(x*1.25) for x in [0, 685, 754, 824, 894, 963, 1033, 1102, 1172, 1241, 1311, 1380, 1450, 1519, 1589, 1658, 1728, 1797, 1867, 1937, 2006, 2076, 2145, 2215, 2284, 2354, 2423, 2493, 2562, 2632, 2701, 2771, 2841, 2910, 2980, 3049, 3119, 3188, 3258, 3327, 3397, 3466, 3536, 3605, 3675, 3744, 3814, 3884, 3953, 4023, 4092, 4162, 4231, 4301, 4370, 4440, 4509, 4579, 4648, 4718, 4787, 4857, 4927, 4996, 5066, 5135, 5205, 5274, 5344, 5413, 5483]]
    攻击次数 = 6
    魔化 = 2.34
    CD = 16 * 1.5
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.25
        elif x == 1:
            self.倍率 *= 1.34


class 技能8(职业主动技能):
    名称 = '恶魔之拳'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data0 = [int(x*1.24) for x in [0, 186, 205, 224, 243, 262, 281, 300, 319, 338, 357, 376, 395, 413, 432, 451, 470, 489, 508, 527, 546, 565, 584, 603, 622, 641, 660, 679, 698, 717, 735, 754, 773, 792, 811, 830, 849, 868, 887, 906, 925, 944, 963, 982, 1001, 1020, 1038, 1057, 1076, 1095, 1114, 1133, 1152, 1171, 1190, 1209, 1228, 1247, 1266, 1285, 1304, 1323, 1342, 1360, 1379, 1398, 1417, 1436, 1455, 1474, 1493]]
    攻击次数 = 10
    data1 = [int(x*1.24) for x in [0, 7217, 7950, 8682, 9414, 10146, 10879, 11611, 12343, 13075, 13807, 14540, 15272, 16004, 16736, 17469, 18201, 18933, 19665, 20398, 21130, 21862, 22594, 23327, 24059, 24791, 25523, 26256, 26988, 27720, 28452, 29185, 29917, 30649, 31381, 32114, 32846, 33578, 34310, 35042, 35775, 36507, 37239, 37971, 38704, 39436, 40168, 40900, 41633, 42365, 43097, 43829, 44562, 45294, 46026, 46758, 47491, 48223, 48955, 49687, 50420, 51152, 51884, 52616, 53349, 54081, 54813, 55545, 56277, 57010, 57742]]
    攻击次数2 = 1
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(x*1.1) for x in self.data0]
            self.data1 = [int(x*1.25) for x in self.data1]
            self.CD *= 0.85
        elif x == 1:
            self.data0 = [int(x*1.1) for x in self.data0]
            self.data1 = [int(x*1.37) for x in self.data1]
            self.CD *= 0.85


class 技能9(职业主动技能):
    名称 = '恶魔之握'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data0 = [int(x*1.25) for x in [0, 505, 557, 609, 660, 711, 763, 814, 866, 916, 968, 1020, 1071, 1123, 1173, 1225, 1277, 1328, 1379, 1431, 1482, 1534, 1584, 1636, 1688, 1739, 1790, 1842, 1893, 1945, 1995, 2047, 2099, 2150, 2201, 2252, 2304, 2356, 2406, 2458, 2510, 2561, 2613, 2663, 2715, 2767, 2818, 2869, 2920, 2972, 3024, 3074, 3126, 3178, 3229, 3280, 3331, 3383, 3435, 3485, 3537, 3589, 3640, 3691, 3742, 3794, 3846, 3896, 3948, 3999, 4051]]
    攻击次数 = 2
    data1 = [int(x*1.25) for x in [0, 10881, 11984, 13088, 14193, 15296, 16400, 17503, 18607, 19712, 20815, 21919, 23023, 24126, 25231, 26335, 27438, 28542, 29646, 30750, 31854, 32958, 34061, 35165, 36270, 37373, 38477, 39581, 40685, 41789, 42893, 43996, 45100, 46205, 47308, 48412, 49516, 50619, 51724, 52828, 53931, 55035, 56140, 57243, 58347, 59450, 60554, 61659, 62762, 63866, 64970, 66073, 67178, 68282, 69385, 70489, 71593, 72697, 73801, 74905, 76008, 77112, 78217, 79320, 80424, 81528, 82631, 83736, 84840, 85943, 87047]]
    攻击次数2 = 1
    CD = 30
    TP成长 = 0.10
    TP上限 = 5

class 技能10(职业主动技能):
    名称 = '黑暗权能'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 31
    data0 = [int(x*1.102) for x in [0, 625, 688, 752, 815, 878, 942, 1006, 1068, 1132, 1196, 1259, 1323, 1385, 1449, 1513, 1577, 1640, 1703, 1766, 1830, 1894, 1956, 2020, 2084, 2147, 2211, 2274, 2337, 2401, 2465, 2527, 2591, 2655, 2718, 2782, 2844, 2908, 2972, 3036, 3099, 3162, 3225, 3289, 3353, 3415, 3479, 3543, 3606, 3670, 3733, 3796, 3860, 3924, 3987, 4050, 4114, 4177, 4241, 4303, 4367, 4431, 4495, 4558, 4621, 4684, 4748, 4812, 4876, 4938, 5002]]
    data1 = [int(x*1.102) for x in [0, 371, 408, 446, 484, 522, 559, 597, 635, 673, 709, 747, 785, 823, 860, 898, 936, 974, 1011, 1049, 1087, 1125, 1161, 1199, 1237, 1275, 1312, 1350, 1388, 1426, 1463, 1501, 1539, 1575, 1613, 1651, 1689, 1726, 1764, 1802, 1840, 1877, 1915, 1953, 1991, 2027, 2065, 2103, 2141, 2178, 2216, 2254, 2292, 2329, 2367, 2405, 2443, 2479, 2517, 2555, 2593, 2630, 2668, 2706, 2744, 2781, 2819, 2857, 2895, 2931, 2969]]
    data2 = [int(x*1.102) for x in [0, 5884, 6480, 7078, 7673, 8271, 8868, 9466, 10062, 10658, 11255, 11852, 12450, 13046, 13644, 14239, 14837, 15434, 16030, 16628, 17224, 17821, 18418, 19016, 19612, 20210, 20805, 21402, 22000, 22596, 23194, 23790, 24387, 24984, 25582, 26178, 26774, 27371, 27968, 28566, 29162, 29759, 30356, 30953, 31550, 32146, 32743, 33340, 33937, 34534, 35132, 35727, 36325, 36922, 37518, 38116, 38711, 39309, 39906, 40503, 41100, 41698, 42293, 42891, 43488, 44084, 44682, 45277, 45875, 46472, 47069]]
    攻击次数 = 1
    攻击次数2 = 32
    攻击次数3 = 1
    CD = 40
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 42
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数2 = 42 * 1.09
            self.CD *= 0.9


class 技能11(职业主动技能):
    名称 = '魔化：末日审判者'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    data0 = [int(x*1.15) for x in [0, 822, 943, 1063, 1183, 1303, 1425, 1546, 1665, 1787, 1906, 2028, 2148, 2268, 2388, 2510, 2628, 2749, 2870, 2989, 3109, 3230, 3351, 3470, 3591, 3710, 3831, 3951, 4072, 4192, 4312, 4432, 4553, 4673, 4793, 4914, 5034, 5153, 5274, 5395, 5513]]
    攻击次数 = 2
    data1 = [int(x*1.15) for x in [0, 983, 1145, 1307, 1469, 1630, 1792, 1954, 2115, 2280, 2440, 2602, 2765, 2926, 3088, 3249, 3410, 3572, 3735, 3897, 4057, 4219, 4381, 4543, 4704, 4865, 5027, 5188, 5351, 5513, 5673, 5836, 5997, 6159, 6321, 6481, 6644, 6806, 6967, 7130, 7291]]
    攻击次数2 = 2
    data2 = [int(x*1.15) for x in [0, 1503, 1800, 2097, 2393, 2688, 2986, 3281, 3577, 3876, 4173, 4468, 4765, 5061, 5357, 5654, 5950, 6245, 6543, 6839, 7135, 7431, 7728, 8024, 8319, 8616, 8912, 9209, 9505, 9801, 10097, 10395, 10689, 10985, 11283, 11578, 11873, 12171, 12467, 12765, 13059]]
    攻击次数3 = 2
    data3 = [int(x*1.15) for x in [0, 1603, 1926, 2249, 2571, 2891, 3215, 3536, 3859, 4183, 4506, 4826, 5150, 5473, 5795, 6117, 6439, 6760, 7083, 7405, 7727, 8048, 8372, 8694, 9015, 9338, 9660, 9981, 10305, 10626, 10947, 11271, 11591, 11914, 12238, 12558, 12880, 13203, 13524, 13847, 14169]]
    攻击次数4 = 2

    # 审判关联数据
    sp_data0 = [int(x*1.193) for x in [0, 8805, 10847, 12890, 14931, 16973, 19015, 21057, 23099, 25141, 27183, 29225, 31266, 33308, 35350, 37392, 39434, 41476, 43518, 45560, 47601, 49643, 51685, 53727, 55769, 57811, 59853, 61895, 63936, 65978, 68021, 70063, 72105, 74147, 76189, 78231, 80272, 82314, 84356, 86398, 88440]]
    sp_data1 = [int(x*1.193) for x in [0, 25062, 30874, 36685, 42497, 48308, 54120, 59931, 65743, 71555, 77367, 83178, 88990, 94801, 100612, 106424, 112236, 118048, 123859, 129671, 135483, 141293, 147105, 152917, 158729, 164540, 170352, 176164, 181976, 187786, 193598, 199410, 205221, 211033, 216845, 222657, 228468, 234279, 240091, 245902, 251714]]

    CD = 1

    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.15


class 技能12(主动技能):
    名称 = '审判'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    data0 = 0
    data1 = 0
    攻击次数2 = 1
    魔化 = 1.1 # 魔化
    CD = 145

    def 等效百分比(self, 武器类型):
        return (self.data0 + self.data1) * self.倍率 * self.魔化


class 技能13(被动技能):
    名称 = '恶魔唤醒'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['不朽战吼', '地狱之门', '厄运之轮', '恶魔之拳', '恶魔之手', '恶魔之握', '复仇之刺', '黑暗权能',
            '回旋飞镰', '毁灭强击', '裂地锤', '末日浩劫', '死亡切割', '永堕：混沌弑神', '极恶洪流', '末日福音：毁灭之翼']
    关联技能2 = ['魔化：末日审判者']
    关联技能3 = ['审判']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.015 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.01 * self.等级, 5)

    def 加成倍率3(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class 技能14(职业主动技能):
    名称 = '地狱之门'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data0 = [int(x*1.181) for x in [0, 1467, 1614, 1763, 1911, 2060, 2210, 2357, 2506, 2656, 2803, 2952, 3102, 3249, 3399, 3546, 3695, 3845, 3992, 4142, 4291, 4438, 4588, 4737, 4884, 5034, 5182, 5331, 5480, 5629, 5777, 5926, 6075, 6223, 6373, 6521, 6669, 6816, 6967, 7115, 7263, 7413, 7562, 7709, 7860, 8008, 8155, 8306, 8453, 8601, 8752, 8899, 9047, 9198, 9345, 9494, 9643, 9792, 9940, 10087, 10238, 10386, 10533, 10684, 10832, 10979, 11130, 11278, 11425, 11576, 11723]]
    攻击次数 = 8
    倍率 = 1.5  # 魔化
    CD = 30
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 9
            self.CD *= 0.88
        elif x == 1:
            self.倍率 *= 1.08
            self.攻击次数 = 9
            self.CD *= 0.88


class 技能15(职业主动技能):
    名称 = '末日浩劫'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data0 = [int(x*1.219) for x in [0, 20616, 22708, 24800, 26891, 28983, 31075, 33165, 35257, 37349, 39440, 41532, 43624, 45716, 47807, 49898, 51990, 54081, 56173, 58265, 60356, 62448, 64540, 66631, 68722, 70814, 72906, 74997, 77089, 79181, 81271, 83363, 85455, 87546, 89638, 91730, 93822, 95913, 98004, 100096, 102187, 104279, 106371, 108462, 110554, 112646, 114737, 116828, 118920, 121012, 123103, 125195, 127287, 129377, 131469, 133561, 135653, 137744, 139836, 141928, 144019, 146110, 148202, 150293, 152385, 154477, 156569, 158660, 160752, 162843, 164934]]
    倍率 = 1.35   # 魔化
    CD = 50
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.08*1.1
        elif x == 1:
            self.倍率 *= 1.08*1.18


class 技能16(职业主动技能):
    名称 = '不朽战吼'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    data0 = [int(x*1.23) for x in [0, 7700, 8482, 9263, 10044, 10826, 11608, 12388, 13170, 13951, 14733, 15515, 16295, 17077, 17858, 18640, 19421, 20201, 20983, 21763, 22545, 23327, 24108, 24890, 25670, 26452, 27234, 28015, 28796, 29577, 30359, 31140, 31920, 32702, 33483, 34264, 35045, 35827, 36609, 37389, 38171, 38952, 39734, 40514, 41296, 42078, 42859, 43641, 44420, 45202, 45984, 46764, 47546, 48327, 49109, 49891, 50671, 51453, 52235, 53016, 53797, 54578, 55360, 56141, 56921, 57703, 58484, 59266, 60047, 60828, 61610]]
    攻击次数 = 5
    data1 = [int(x*1.23) for x in [0, 2752, 3033, 3312, 3588, 3868, 4148, 4426, 4707, 4986, 5266, 5546, 5824, 6103, 6381, 6662, 6941, 7220, 7501, 7778, 8057, 8338, 8616, 8895, 9176, 9453, 9732, 10012, 10291, 10571, 10850, 11130, 11409, 11687, 11967, 12245, 12524, 12805, 13083, 13361, 13641, 13921, 14200, 14480, 14760, 15038, 15317, 15598, 15876, 16154, 16434, 16714, 16992, 17273, 17552, 17829, 18110, 18388, 18667, 18947, 19227, 19507, 19784, 20064, 20343, 20621, 20902, 21181, 21460, 21741, 22018]]
    攻击次数2 = 2
    CD = 40

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.29
        self.CD *= 0.86


class 技能17(被动技能):
    名称 = '原罪之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)


class 技能18(职业主动技能):
    名称 = '毁灭强击'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    data0 = [int(x*1.231) for x in [0, 5066, 5580, 6094, 6609, 7123, 7636, 8150, 8664, 9179, 9692, 10206, 10720, 11235, 11749, 12262, 12776, 13291, 13805, 14318, 14832, 15346, 15861, 16375, 16888, 17402, 17917, 18431, 18945, 19458, 19973, 20487, 21001, 21514, 22028, 22543, 23057, 23571, 24084, 24599, 25113, 25627, 26140, 26655, 27169, 27683, 28197, 28710, 29225, 29739, 30253, 30768, 31281, 31795, 32309, 32823, 33337, 33851, 34365, 34879, 35394, 35907, 36421, 36935, 37450, 37964, 38477, 38991, 39505, 40020, 40533]]
    攻击次数 = 1
    data1 = [int(x*1.231) for x in [0, 23644, 26042, 28441, 30840, 33237, 35637, 38036, 40435, 42834, 45232, 47631, 50030, 52429, 54827, 57226, 59625, 62024, 64422, 66820, 69220, 71619, 74016, 76416, 78815, 81214, 83612, 86011, 88410, 90809, 93206, 95606, 98005, 100403, 102803, 105201, 107599, 109999, 112398, 114795, 117195, 119594, 121991, 124391, 126789, 129189, 131588, 133985, 136385, 138784, 141181, 143581, 145980, 148378, 150778, 153175, 155574, 157974, 160372, 162770, 165170, 167568, 169967, 172366, 174764, 177164, 179562, 181960, 184360, 186758, 189157]]
    攻击次数2 = 1
    data2 = [int(x*1.231) for x in [0, 1012, 1116, 1219, 1321, 1424, 1526, 1629, 1733, 1836, 1938, 2041, 2143, 2246, 2350, 2452, 2555, 2658, 2760, 2863, 2966, 3069, 3172, 3275, 3377, 3480, 3582, 3686, 3789, 3891, 3994, 4097, 4199, 4302, 4406, 4508, 4611, 4714, 4816, 4919, 5023, 5125, 5228, 5330, 5433, 5536, 5639, 5742, 5845, 5947, 6050, 6153, 6255, 6359, 6462, 6564, 6667, 6769, 6872, 6976, 7078, 7181, 7284, 7386, 7489, 7593, 7695, 7798, 7901, 8003, 8106]]
    攻击次数3 = 10  # 最低5
    魔化 = 1.35 # 魔化
    CD = 45.0

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.35


class 技能19(职业主动技能):
    名称 = '永堕：混沌弑神'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    data0 = [int(x*1.15) for x in [0, 4013, 4944, 5875, 6805, 7736, 8667, 9597, 10528, 11459, 12389, 13320, 14251, 15181, 16112, 17043, 17974, 18904, 19835, 20766, 21696, 22627, 23558, 24488, 25419, 26350, 27280, 28211, 29142, 30073, 31003, 31934, 32865, 33795, 34726, 35657, 36587, 37518, 38449, 39380, 40310, 41241, 42172, 43102, 44033, 44964, 45894, 46825, 47756, 48686, 49617, 50548, 51479, 52409, 53340, 54271, 55201, 56132, 57063, 57993, 58924, 59855, 60786, 61716, 62647, 63578, 64508, 65439, 66370, 67300, 68231]]
    攻击次数 = 0
    data1 = [int(x*1.15) for x in [0, 2876, 3543, 4210, 4877, 5544, 6211, 6878, 7545, 8212, 8879, 9546, 10213, 10880, 11547, 12214, 12881, 13548, 14215, 14882, 15549, 16216, 16883, 17550, 18217, 18884, 19551, 20218, 20885, 21552, 22219, 22886, 23553, 24220, 24887, 25554, 26221, 26888, 27555, 28222, 28889, 29556, 30223, 30890, 31557, 32224, 32891, 33558, 34225, 34892, 35559, 36226, 36893, 37560, 38227, 38894, 39561, 40228, 40895, 41562, 42229, 42896, 43563, 44230, 44897, 45564, 46231, 46898, 47565, 48232, 48899]]
    攻击次数2 = 12
    data2 = [int(x*1.15) for x in [0, 7224, 8899, 10575, 12250, 13925, 15600, 17276, 18951, 20626, 22301, 23977, 25652, 27327, 29002, 30678, 32353, 34028, 35703, 37379, 39054, 40729, 42404, 44080, 45755, 47430, 49105, 50781, 52456, 54131, 55806, 57482, 59157, 60832, 62507, 64183, 65858, 67533, 69208, 70884, 72559, 74234, 75909, 77585, 79260, 80935, 82610, 84286, 85961, 87636, 89311, 90987, 92662, 94337, 96012, 97688, 99363, 101038, 102713, 104389, 106064, 107739, 109414, 111090, 112765, 114440, 116115, 117791, 119466, 121141, 122816]]
    攻击次数3 = 1
    data3 = [int(x*1.15) for x in [0, 17258, 21260, 25262, 29264, 33266, 37268, 41270, 45272, 49274, 53276, 57278, 61280, 65282, 69284, 73286, 77288, 81290, 85292, 89294, 93296, 97298, 101300, 105302, 109304, 113306, 117308, 121310, 125312, 129314, 133316, 137318, 141320, 145322, 149324, 153326, 157328, 161330, 165332, 169334, 173336, 177338, 181340, 185342, 189344, 193346, 197348, 201350, 205352, 209354, 213355, 217357, 221359, 225361, 229363, 233365, 237367, 241369, 245371, 249373, 253375, 257377, 261379, 265381, 269383, 273385, 277387, 281389, 285391, 289393, 293395]]
    攻击次数4 = 2
    魔化 = 1.35 # 魔化
    CD = 180.0

    def 等效百分比(self, 武器类型):
        # 按X或Z
        self.data3 = [int(x*1.35) for x in self.data3]
        return super().等效百分比(武器类型)


class 技能20(被动技能):
    名称 = '光之影'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能21(职业主动技能):
    名称 = '极恶洪流'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    data0 = [int(x*1.21) for x in [0, 8416, 9269, 10123, 10977, 11830, 12684, 13538, 14392, 15246, 16099, 16953, 17807, 18661, 19515, 20368, 21222, 22076, 22930, 23783, 24637, 25491, 26345, 27198, 28052, 28906, 29760, 30614, 31467, 32321, 33175, 34029, 34883, 35736, 36590, 37444, 38298, 39151, 40005, 40859, 41713, 42567, 43420, 44274, 45128, 45982, 46836, 47689, 48543, 49397, 50250, 51105, 51958, 52812, 53666, 54519, 55373, 56227, 57081, 57935, 58788, 59642, 60496, 61350, 62204, 63057, 63911, 64765, 65618, 66473, 67326]]
    攻击次数 = 3
    data1 = [int(x*1.21) for x in [0, 37871, 41713, 45554, 49397, 53239, 57081, 60923, 64765, 68607, 72449, 76291, 80133, 83975, 87817, 91659, 95501, 99343, 103185, 107027, 110869, 114711, 118553, 122395, 126237, 130079, 133921, 137763, 141605, 145448, 149289, 153131, 156973, 160816, 164657, 168499, 172341, 176183, 180025, 183867, 187710, 191551, 195393, 199235, 203078, 206919, 210761, 214603, 218446, 222287, 226129, 229972, 233814, 237655, 241497, 245340, 249182, 253023, 256865, 260708, 264550, 268391, 272234, 276076, 279917, 283759, 287602, 291444, 295285, 299127, 302970]]
    攻击次数2 = 1
    攻击次数 = 3
    攻击次数2 = 1
    CD = 60.0
    魔化 = 1.3

    def 等效百分比(self, 武器类型):
        # [长按技能键时] 攻击力增加率 20%
        self.倍率 *= 1.2
        return super().等效百分比(武器类型)


class 技能22(职业主动技能):
    名称 = '末日福音：毁灭之翼'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 = [int(x*1.246) for x in [0, 49219, 60632, 72046, 83459, 94872, 106285, 117699, 129112, 140525, 151938, 163352, 174765, 186178, 197591, 209005, 220418, 231831, 243244, 254658, 266071, 277484, 288897, 300311, 311724, 323137, 334550, 345964, 357377, 368790, 380203, 391617, 403030, 414443, 425856, 437270, 448683, 460096, 471509, 482923, 494336, 505749, 517162, 528576, 539989, 551402, 562816, 574229, 585642, 597055, 608469, 619882, 631295, 642708, 654122, 665535, 676948, 688361, 699775, 711188, 722601, 734014, 745428, 756841, 768254, 779667, 791081, 802494, 813907, 825320, 836734]]
    攻击次数 = 1
    data1 = [int(x*1.246) for x in [0, 24609, 30316, 36023, 41729, 47436, 53142, 58849, 64556, 70262, 75969, 81676, 87382, 93089, 98795, 104502, 110209, 115915, 121622, 127329, 133035, 138742, 144448, 150155, 155862, 161568, 167275, 172982, 178688, 184395, 190101, 195808, 201515, 207221, 212928, 218635, 224341, 230048, 235754, 241461, 247168, 252874, 258581, 264288, 269994, 275701, 281408, 287114, 292821, 298527, 304234, 309941, 315647, 321354, 327061, 332767, 338474, 344180, 349887, 355594, 361300, 367007, 372714, 378420, 384127, 389833, 395540, 401247, 406953, 412660, 418367]]
    攻击次数2 = 1
    data2 = [int(x*1.246) for x in [0, 61524, 75791, 90057, 104324, 118590, 132857, 147123, 161390, 175657, 189923, 204190, 218456, 232723, 246989, 261256, 275523, 289789, 304056, 318322, 332589, 346855, 361122, 375388, 389655, 403922, 418188, 432455, 446721, 460988, 475254, 489521, 503788, 518054, 532321, 546587, 560854, 575120, 589387, 603654, 617920, 632187, 646453, 660720, 674986, 689253, 703519, 717786, 732053, 746319, 760586, 774852, 789119, 803385, 817652, 831919, 846185, 860452, 874718, 888985, 903251, 917518, 931785, 946051, 960318, 974584, 988851, 1003117, 1017384, 1031650, 1045917]]
    攻击次数3 = 1
    data3 = [int(x*1.246) for x in [0, 110744, 136424, 162103, 187783, 213463, 239143, 264823, 290502, 316182, 341862, 367542, 393222, 418902, 444581, 470261, 495941, 521621, 547301, 572980, 598660, 624340, 650020, 675700, 701379, 727059, 752739, 778419, 804099, 829779, 855458, 881138, 906818, 932498, 958178, 983857, 1009537, 1035217, 1060897, 1086577, 1112257, 1137936, 1163616, 1189296, 1214976, 1240656, 1266335, 1292015, 1317695, 1343375, 1369055, 1394735, 1420414, 1446094, 1471774, 1497454, 1523134, 1548813, 1574493, 1600173, 1625853, 1651533, 1677213, 1702892, 1728572, 1754252, 1779932, 1805612, 1831291, 1856971, 1882651]]
    攻击次数4 = 1

    CD = 290.0
    魔化 = 1.4

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

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

神启·复仇者一觉序号 = 12
神启·复仇者二觉序号 = 19
神启·复仇者三觉序号 = 22

神启·复仇者护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        神启·复仇者护石选项.append(i.名称)

神启·复仇者符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        神启·复仇者符文选项.append(i.名称)


class 神启·复仇者角色属性(角色属性):

    实际名称 = '神启·复仇者'
    角色 = '圣职者(男)'
    职业 = '复仇者'

    武器选项 = ['镰刀']

    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '重甲'
    防具精通属性 = ['智力']

    主BUFF = 1.90

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        一觉 = self.技能栏[self.技能序号['魔化：末日审判者']]
        self.技能栏[self.技能序号['审判']].data0 = 一觉.sp_data0[一觉.等级]
        self.技能栏[self.技能序号['审判']].data1 = 一觉.sp_data1[一觉.等级]


class 神启·复仇者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 神启·复仇者角色属性()
        self.角色属性A = 神启·复仇者角色属性()
        self.角色属性B = 神启·复仇者角色属性()
        self.一觉序号 = 神启·复仇者一觉序号
        self.二觉序号 = 神启·复仇者二觉序号
        self.三觉序号 = 神启·复仇者三觉序号
        self.护石选项 = deepcopy(神启·复仇者护石选项)
        self.符文选项 = deepcopy(神启·复仇者符文选项)
