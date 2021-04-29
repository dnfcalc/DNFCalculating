from math import *
from PublicReference.base import *
# 2021.4.7 韩测


class 主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    数据 = []
    数据2 = []
    数据3 = []
    数据4 = []
    数据5 = []

    攻击次数5 = 0

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.数据) >= self.等级 and len(self.数据) > 0:
            等效倍率 += self.数据[self.等级] * self.攻击次数
        if len(self.数据2) >= self.等级 and len(self.数据2) > 0:
            等效倍率 += self.数据2[self.等级] * self.攻击次数2
        if len(self.数据3) >= self.等级 and len(self.数据3) > 0:
            等效倍率 += self.数据3[self.等级] * self.攻击次数3
        if len(self.数据4) >= self.等级 and len(self.数据4) > 0:
            等效倍率 += self.数据4[self.等级] * self.攻击次数4
        if len(self.数据5) >= self.等级 and len(self.数据5) > 0:
            等效倍率 += self.数据5[self.等级] * self.攻击次数5
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

# 长刀精通


class 技能0(被动技能):
    名称 = '长刀精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.95

# 暗刃战略


class 技能1(被动技能):
    名称 = '暗刃战略'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)


# 一觉被动
class 技能2(被动技能):
    名称 = 'B.G枪刃改造'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


# 二觉被动
class 技能3(被动技能):
    名称 = 'B.C精锐特训'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


# 三觉被动
class 技能4(被动技能):
    名称 = '暮光战略'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 掩护射击
class 技能5(主动技能):
    名称 = '掩护射击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据 = [int(i*1.105)for i in [0, 206, 227, 247, 268, 289, 310, 331, 351, 374, 394, 415, 436, 457, 478, 498, 519, 541, 561, 582, 602, 625, 645, 666, 688, 708, 729, 749, 771, 792, 812, 833, 855, 876, 897, 917,
                                939, 959, 980, 1001, 1022, 1043, 1063, 1084, 1106, 1126, 1147, 1167, 1190, 1210, 1231, 1252, 1273, 1294, 1314, 1335, 1357, 1377, 1398, 1418, 1441, 1462, 1482, 1503, 1524, 1545, 1566, 1586, 1608, 1628, 1649]]
    攻击次数 = 10
    # 基础 = 1847.755698
    # 成长 = 209.2273524
    CD = 6
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.105

# 捷影步


class 技能6(主动技能):
    名称 = '捷影步'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据 = [int(i*1.102) for i in [0, 370, 407, 444, 482, 519, 557, 594, 632, 670, 707, 745, 782, 820, 857, 895, 932, 969, 1006, 1044, 1083, 1120, 1158, 1195, 1232, 1269, 1309, 1346, 1383, 1420, 1458, 1495, 1532, 1571, 1608,
                                 1645, 1682, 1721, 1758, 1795, 1833, 1871, 1908, 1945, 1983, 2020, 2057, 2096, 2134, 2171, 2208, 2245, 2283, 2321, 2359, 2396, 2434, 2471, 2508, 2546, 2584, 2621, 2658, 2696, 2733, 2771, 2808, 2847, 2884, 2921, 2959]]
    攻击次数 = 5
    # 基础 = 1658.836937
    # 成长 = 187.6461134
    CD = 5
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.102

# 轮盘连射


class 技能7(主动技能):
    名称 = '轮盘连射'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    # 上挑攻击力：<data0>%
    数据 = [int(i*1.0) for i in [0, 1483, 1634, 1784, 1935, 2086, 2237, 2387, 2538, 2687, 2838, 2988, 3139, 3289, 3440, 3591, 3741, 3892, 4043, 4194, 4344, 4495, 4646, 4795, 4945, 5096, 5246, 5397, 5548, 5698, 5849, 6000, 6151, 6301,
                               6452, 6603, 6752, 6902, 7053, 7203, 7354, 7505, 7655, 7806, 7957, 8108, 8258, 8409, 8560, 8710, 8859, 9010, 9160, 9311, 9462, 9612, 9763, 9914, 10065, 10215, 10366, 10517, 10667, 10816, 10967, 11117, 11268, 11419, 11569, 11720]]
    攻击次数 = 1

    # 下劈攻击力：<data2>%
    数据2 = [int(i*1.0) for i in [0, 1887, 2080, 2271, 2463, 2654, 2846, 3037, 3229, 3421, 3613, 3803, 3995, 4187, 4379, 4570, 4762, 4953, 5145, 5336, 5529, 5719, 5911, 6103, 6295, 6486, 6677, 6869, 7061, 7252, 7444, 7636, 7827, 8018, 8211,
                                8402, 8594, 8784, 8977, 9168, 9360, 9552, 9743, 9934, 10126, 10318, 10510, 10700, 10892, 11084, 11276, 11467, 11659, 11850, 12042, 12233, 12426, 12618, 12808, 13000, 13192, 13383, 13575, 13766, 13958, 14149, 14342, 14534, 14724, 14915]]
    # 攻击次数2 = 1
    # 三觉被动变更
    # 攻击次数3 = 10
    攻击次数2 = 0

    # 射击攻击力：<data1>%
    数据3 = [int(i*1.0) for i in [0, 222, 244, 267, 289, 313, 335, 358, 380, 403, 425, 448, 470, 493, 515, 539, 560, 584, 606, 629, 651, 673, 696, 718, 742, 763, 787, 808, 832, 853, 877, 900, 922, 945, 967, 990,
                                1012, 1035, 1057, 1080, 1103, 1125, 1147, 1170, 1194, 1215, 1239, 1261, 1284, 1306, 1329, 1351, 1373, 1396, 1418, 1441, 1464, 1487, 1509, 1532, 1554, 1577, 1599, 1622, 1644, 1668, 1689, 1713, 1734, 1758]]
    # 三觉被动变更
    # 攻击次数3 = 10
    攻击次数3 = 3.72*3

    # 基础 = 1332.874675
    # 成长 = 150.5275803
    # 攻击次数 = 1

    # 基础2 = 1696.315584#下劈
    # 成长2 = 191.5866712
    # 攻击次数2 = 1

    # 基础3 = 191.5866712#射击
    # 成长3 = 22.58072454
    # 攻击次数3 = 0#10

    CD = 8
    TP成长 = 0.10
    TP上限 = 5


# 剑刃突刺
class 技能8(主动技能):
    名称 = '剑刃突刺'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2270.46039
    成长 = 258.1335954

    # 突刺攻击力：<data0>%
    数据 = [int(i*1.105) for i in [0, 255, 282, 308, 334, 359, 385, 411, 438, 464, 489, 515, 541, 568, 593, 619, 645, 671, 696, 724, 749, 775, 800, 827, 853, 879, 905, 931, 956, 982, 1009, 1035, 1061, 1087, 1112, 1140,
                                 1165, 1191, 1216, 1243, 1268, 1295, 1321, 1347, 1372, 1398, 1425, 1451, 1476, 1503, 1528, 1554, 1581, 1607, 1632, 1659, 1684, 1710, 1737, 1763, 1788, 1814, 1840, 1867, 1892, 1919, 1944, 1970, 1995, 2023]]
    攻击次数 = 4
    # 终结横斩攻击力：<data1>%
    数据2 = [int(i*1.105) for i in [0, 773, 850, 928, 1006, 1085, 1164, 1243, 1321, 1398, 1476, 1556, 1634, 1713, 1791, 1870, 1948, 2026, 2104, 2183, 2261, 2340, 2418, 2497, 2575, 2652, 2731, 2809, 2888, 2966, 3045, 3123, 3201,
                                  3279, 3358, 3436, 3515, 3593, 3672, 3750, 3828, 3906, 3985, 4063, 4142, 4220, 4299, 4378, 4455, 4533, 4611, 4690, 4769, 4848, 4926, 5003, 5081, 5161, 5239, 5318, 5396, 5475, 5553, 5631, 5709, 5788, 5866, 5945, 6023, 6102]]
    攻击次数2 = 1
    # 终结射击攻击力：<data2>%
    数据3 = [int(i*1.105) for i in [0, 247, 273, 299, 323, 349, 374, 399, 424, 449, 475, 499, 526, 549, 576, 601, 626, 651, 676, 701, 726, 752, 778, 802, 828, 852, 878, 902, 928, 954, 979, 1004, 1029, 1055, 1079, 1105,
                                  1130, 1155, 1181, 1206, 1231, 1256, 1281, 1307, 1331, 1357, 1381, 1408, 1433, 1458, 1483, 1508, 1533, 1558, 1583, 1610, 1634, 1660, 1684, 1710, 1734, 1760, 1785, 1810, 1836, 1861, 1886, 1911, 1936, 1962]]
    攻击次数3 = 3

    CD = 6
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.105

# 潜行射击


class 技能9(主动技能):
    名称 = '潜行射击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据 = [int(i*1.107) for i in [0, 201, 222, 242, 263, 283, 304, 325, 345, 364, 385, 405, 426, 446, 467, 488, 508, 529, 549, 569, 590, 610, 631, 651, 672, 693, 713, 734, 753, 774, 795, 815, 836, 856, 877, 898,
                                 918, 939, 958, 979, 1000, 1020, 1041, 1061, 1082, 1103, 1123, 1144, 1162, 1183, 1204, 1224, 1245, 1265, 1286, 1307, 1327, 1348, 1367, 1388, 1409, 1429, 1450, 1470, 1491, 1512, 1532, 1553, 1572, 1593, 1614]]
    # 十五次射击，正常模式位移距离较长，容易损失攻击次数，目前取12
    攻击次数 = 12
    # 基础 = 2709.696017 * 0.8
    # 成长 = 307.081761 * 0.8#游戏中攻速越高攻击段数越低，取本人60%-90%攻速时大致为12/15
    CD = 7
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.107

# 利刃旋斩


class 技能10(主动技能):
    名称 = '利刃旋斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41

    # 左右斩击攻击力：<data0>%
    数据 = [int(i*1.16) for i in [0, 380, 419, 457, 495, 535, 573, 611, 650, 689, 728, 765, 804, 842, 882, 919, 959, 997, 1037, 1074, 1113, 1151, 1191, 1228, 1268, 1306, 1344, 1383, 1421, 1460, 1499, 1537, 1576, 1615, 1653,
                                1692, 1730, 1769, 1808, 1846, 1885, 1924, 1962, 2001, 2039, 2078, 2117, 2155, 2194, 2233, 2271, 2310, 2348, 2387, 2424, 2464, 2501, 2542, 2579, 2619, 2656, 2696, 2733, 2773, 2810, 2851, 2888, 2928, 2965, 3004, 3042]]
    攻击次数 = 2
    # 旋转斩击攻击力：<data1>%
    数据2 = [int(i*1.16) for i in [0, 213, 234, 255, 277, 299, 321, 342, 363, 385, 407, 429, 450, 471, 493, 515, 537, 559, 580, 601, 623, 645, 667, 688, 709, 732, 753, 775, 796, 817, 840, 861, 883, 903, 926, 948,
                                 969, 992, 1012, 1034, 1056, 1078, 1100, 1120, 1141, 1162, 1185, 1207, 1228, 1249, 1270, 1293, 1314, 1336, 1357, 1379, 1401, 1422, 1445, 1466, 1487, 1509, 1531, 1553, 1573, 1595, 1618, 1639, 1661, 1681, 1703]]
    攻击次数2 = 5
    # 最终旋斩攻击力：<data2>%
    数据3 = [int(i*1.16) for i in [0, 1216, 1340, 1464, 1587, 1711, 1834, 1958, 2082, 2204, 2328, 2451, 2575, 2699, 2822, 2946, 3069, 3193, 3316, 3439, 3563, 3686, 3810, 3934, 4057, 4181, 4304, 4426, 4550, 4673, 4797, 4920, 5044, 5168,
                                 5291, 5415, 5538, 5662, 5786, 5909, 6033, 6156, 6280, 6404, 6527, 6650, 6773, 6897, 7021, 7144, 7268, 7391, 7515, 7639, 7761, 7885, 8008, 8132, 8256, 8379, 8503, 8626, 8750, 8872, 8995, 9119, 9243, 9366, 9490, 9613, 9737]]
    攻击次数3 = 1

    # 基础 = 2730.212439
    # 成长 = 308.7161807
    CD = 7
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.16

# 游弹枪袭


class 技能11(主动技能):
    名称 = '游弹枪袭'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据 = [int(i*1.104) for i in [0, 134, 148, 162, 176, 189, 203, 217, 231, 244, 258, 272, 285, 299, 313, 327, 340, 354, 368, 382, 395, 408, 423, 437, 449, 464, 478, 490, 505, 519, 532, 546, 560, 573,
                                 588, 601, 614, 629, 643, 655, 670, 683, 696, 711, 724, 738, 752, 765, 779, 794, 806, 820, 835, 848, 861, 876, 889, 902, 915, 930, 944, 956, 971, 985, 998, 1012, 1026, 1039, 1054, 1067, 1080]]
    攻击次数 = 30
    # 基础 = 3624.235294
    # 成长 = 411.4886878
    CD = 8
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.104

# 全方位射击


class 技能12(主动技能):
    名称 = '全方位射击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36

    # 周围射击攻击力：<data0>%
    数据 = [int(i*1.104) for i in [0, 282, 312, 340, 368, 398, 426, 454, 483, 512, 541, 569, 598, 627, 655, 685, 713, 742, 771, 799, 828, 856, 886, 914, 943, 972, 1001, 1029, 1058, 1087, 1115, 1144, 1173, 1202, 1229, 1260,
                                 1288, 1315, 1346, 1373, 1402, 1432, 1460, 1488, 1517, 1546, 1574, 1603, 1632, 1661, 1689, 1719, 1747, 1776, 1804, 1833, 1862, 1890, 1920, 1948, 1977, 2006, 2034, 2063, 2091, 2121, 2149, 2177, 2207, 2236, 2263]]
    攻击次数 = 15
    # 最终射击攻击力：<data1>%
    数据2 = [int(i*1.104) for i in [0, 471, 519, 567, 614, 663, 711, 758, 806, 853, 901, 951, 998, 1046, 1093, 1141, 1190, 1237, 1285, 1332, 1380, 1428, 1476, 1524, 1572, 1620, 1668, 1715, 1764, 1812, 1859, 1907, 1954, 2002, 2051,
                                  2098, 2146, 2194, 2241, 2290, 2339, 2386, 2434, 2481, 2529, 2578, 2625, 2673, 2720, 2768, 2815, 2864, 2912, 2960, 3008, 3056, 3103, 3152, 3200, 3247, 3295, 3342, 3390, 3439, 3486, 3534, 3581, 3630, 3679, 3726, 3774]]
    攻击次数2 = 6

    # 基础 = 253.6930612
    # 成长 = 28.71635054
    # 攻击次数 = 15

    # 基础2 = 423.2865306
    # 成长2 = 47.85935174
    # 攻击次数2 = 6

    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1
    ###
    # 倍率 = 1.106

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 0
            self.攻击次数 = 20
            self.数据 = [int(i*1.27 * 1.07) for i in self.数据]
            self.CD *= 0.95
        elif x == 1:
            self.攻击次数2 = 0
            self.攻击次数 = 20
            self.数据 = [int(i*1.27 * 1.16) for i in self.数据]
            # self.倍率 = self.倍率 * 1.27 * 1.16#改动位置
            self.CD *= 0.95

# 回旋飞剑


class 技能13(主动技能):
    # 暂无数组
    名称 = '回旋飞剑'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7642.573878
    成长 = 863.4943577
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    ###
    倍率 = 1.118

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)


# 枪刃乱舞
class 技能14(主动技能):
    名称 = '枪刃乱舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    # 斩击攻击力：<data0>%
    数据 = [int(i*1.121) for i in [0, 318, 350, 384, 415, 448, 481, 512, 544, 577, 610, 642, 673, 707, 739, 771, 803, 836, 868, 900, 934, 965, 997, 1030, 1062, 1095, 1126, 1159, 1192, 1223, 1257, 1289, 1321, 1353, 1385,
                                 1418, 1450, 1482, 1516, 1548, 1579, 1612, 1644, 1676, 1709, 1742, 1775, 1805, 1838, 1871, 1903, 1935, 1968, 2001, 2032, 2065, 2097, 2130, 2162, 2194, 2228, 2258, 2291, 2324, 2356, 2389, 2421, 2452, 2485, 2517, 2550]]
    攻击次数 = 10
    # 射击攻击力：<data1>%
    数据2 = [int(i*1.121) for i in [0, 219, 242, 265, 285, 309, 333, 353, 376, 399, 421, 443, 466, 488, 510, 533, 555, 577, 600, 622, 644, 667, 689, 712, 734, 755, 779, 800, 823, 846, 868, 890, 913, 935, 956, 980,
                                  1002, 1023, 1047, 1068, 1091, 1113, 1136, 1158, 1181, 1203, 1224, 1248, 1269, 1293, 1314, 1336, 1360, 1381, 1404, 1426, 1449, 1470, 1494, 1516, 1537, 1561, 1583, 1604, 1627, 1651, 1672, 1694, 1718, 1738, 1762]]
    攻击次数2 = 15
    # 最终横斩攻击力：<data2>%
    数据3 = [int(i*1.121) for i in [0, 4160, 4582, 5005, 5427, 5849, 6271, 6694, 7115, 7537, 7959, 8381, 8804, 9226, 9649, 10070, 10493, 10915, 11338, 11760, 12182, 12603, 13026, 13448, 13871, 14292, 14715, 15137, 15558, 15981, 16403, 16825, 17247, 17670, 18092,
                                  18513, 18935, 19357, 19780, 20202, 20625, 21046, 21468, 21890, 22313, 22735, 23157, 23579, 24002, 24424, 24847, 25268, 25691, 26113, 26536, 26957, 27378, 27801, 28223, 28646, 29068, 29490, 29911, 30334, 30756, 31179, 31600, 32023, 32445, 32866, 33289]]
    攻击次数3 = 1

    # 基础 = 285.9777983
    # 成长 = 32.3413506
    # 攻击次数 = 10

    # 基础2 = 197.4236818
    # 成长2 = 22.34227567
    # 攻击次数2 = 15

    # 基础3 = 3738.310823
    # 成长3 = 422.1492831
    # 攻击次数3 = 1

    ###
    # 倍率 = 1.121

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.80  # 加算
            self.数据 = [int(i*1.27) for i in self.数据]
            self.数据2 = [int(i*1.07) for i in self.数据2]
            self.数据3 = [int(i*1.07) for i in self.数据3]
            # self.攻击次数3 *= 1.27
            # self.攻击次数 *= 1.07
            # self.攻击次数2 *= 1.07
        elif x == 1:
            self.CD *= 0.80  # 加算
            self.数据 = [int(i*1.50) for i in self.数据]
            self.数据2 = [int(i*1.07) for i in self.数据2]
            self.数据3 = [int(i*1.07) for i in self.数据3]
            # self.攻击次数3 *= 1.50#改动位置
            # self.攻击次数 *= 1.07
            # self.攻击次数2 *= 1.07

# 血光斩


class 技能15(主动技能):
    名称 = '血光斩'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    # 基础 = 14496.06087
    # 成长 = 1636.743941
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    数据 = [int(i*1.105) for i in [0, 16133, 17770, 19406, 21043, 22680, 24317, 25953, 27590, 29226, 30864, 32500, 34137, 35773, 37411, 39048, 40684, 42320, 43957, 45595, 47231, 48867, 50504, 52142, 53778, 55414, 57052, 58688, 60325, 61961, 63599, 65235, 66872, 68508, 70146,
                                 71782, 73418, 75055, 76693, 78329, 79965, 81603, 83240, 84876, 86512, 88150, 89787, 91423, 93059, 94697, 96333, 97970, 99606, 101244, 102880, 104517, 106153, 107791, 109427, 111063, 112700, 114338, 115974, 117610, 119247, 120885, 122521, 124157, 125794, 127432, 129068]]

    ###
    # 倍率 = 1.105

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.数据 = [int(i*1.25) for i in self.数据]
            # self.倍率 *= 1.25#加算
        elif x == 1:
            self.数据 = [int(i*1.33) for i in self.数据]
            # self.倍率 *= 1.33#加算   改动位置


# 一觉
class 技能16(主动技能):
    名称 = '电光飞掠'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    # 基础 = 34891.02857
    # 成长 = 10539.71429
    CD = 145

    # 剑术攻击力：<data0>%
    数据 = [int(i*1.103) for i in [0, 1398, 1723, 2046, 2370, 2695, 3019, 3344, 3668, 3992, 4317, 4642, 4965, 5289, 5614, 5938, 6262, 6587, 6912, 7236, 7559, 7883, 8208, 8532, 8857, 9181, 9505, 9830, 10153, 10478, 10802, 11127, 11451, 11775, 12100, 12425,
                                 12748, 13072, 13397, 13721, 14045, 14370, 14695, 15018, 15343, 15667, 15991, 16315, 16640, 16965, 17288, 17613, 17938, 18260, 18585, 18910, 19234, 19558, 19883, 20208, 20531, 20856, 21180, 21503, 21828, 22153, 22478, 22801, 23126, 23451, 23773]]
    攻击次数 = 13
    # 射击攻击力：<data1>%
    数据2 = [int(i*1.103) for i in [0, 1703, 2098, 2494, 2889, 3284, 3680, 4075, 4470, 4866, 5261, 5656, 6051, 6447, 6842, 7237, 7633, 8027, 8422, 8818, 9213, 9608, 10004, 10399, 10794, 11190, 11585, 11980, 12376, 12771, 13166, 13562, 13957, 14351, 14747,
                                  15142, 15537, 15933, 16328, 16723, 17119, 17514, 17908, 18304, 18698, 19093, 19489, 19884, 20279, 20675, 21070, 21465, 21861, 22256, 22651, 23046, 23442, 23837, 24232, 24628, 25022, 25417, 25813, 26208, 26603, 26999, 27394, 27789, 28185, 28580, 28975]]
    攻击次数2 = 16
    # 最终射击攻击力：<data2>%
    # data2 = [0, 1703, 2098, 2494, 2889, 3284, 3680, 4075, 4470, 4866, 5261, 5656, 6051, 6447, 6842, 7237, 7633, 8027, 8422, 8818, 9213, 9608, 10004, 10399, 10794, 11190, 11585, 11980, 12376, 12771, 13166, 13562, 13957, 14351, 14747, 15142, 15537, 15933, 16328, 16723, 17119, 17514, 17908, 18304, 18698, 19093, 19489, 19884, 20279, 20675, 21070, 21465, 21861, 22256, 22651, 23046, 23442, 23837, 24232, 24628, 25022, 25417, 25813, 26208, 26603, 26999, 27394, 27789, 28185, 28580, 28975]

    ###
    # 倍率 = 1.103

# 近敌灭杀


class 技能17(主动技能):
    名称 = '近敌灭杀'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    # 刺击攻击力：<data0>%
    数据 = [int(i*1.105) for i in [0, 5885, 6482, 7080, 7676, 8273, 8871, 9468, 10066, 10662, 11259, 11857, 12454, 13051, 13648, 14245, 14843, 15440, 16036, 16633, 17230, 17828, 18425, 19022, 19619, 20216, 20814, 21410, 22008, 22605, 23202, 23800, 24395, 24993, 25590,
                                 26188, 26785, 27381, 27979, 28576, 29174, 29770, 30367, 30965, 31562, 32160, 32755, 33352, 33950, 34547, 35144, 35741, 36338, 36936, 37533, 38130, 38727, 39324, 39922, 40519, 41115, 41712, 42309, 42907, 43503, 44101, 44698, 45295, 45893, 46489, 47087]]
    # 射击攻击力：<data1>%
    数据2 = [int(i*1.105) for i in [0, 440, 486, 531, 576, 621, 664, 709, 754, 799, 844, 889, 934, 979, 1023, 1067, 1112, 1158, 1203, 1247, 1291, 1336, 1381, 1426, 1470, 1516, 1561, 1606, 1651, 1694, 1739, 1784, 1829, 1874, 1919,
                                  1964, 2009, 2053, 2097, 2142, 2188, 2233, 2278, 2321, 2366, 2411, 2456, 2500, 2546, 2591, 2636, 2681, 2724, 2769, 2814, 2859, 2904, 2949, 2994, 3039, 3083, 3127, 3172, 3218, 3263, 3308, 3351, 3396, 3441, 3486, 3530]]

    # 基础 = 5288.051613
    # 成长 = 597.1358871
    攻击次数 = 1

    # 基础2 = 396.1870968
    # 成长2 = 44.7766129
    攻击次数2 = 20

    ###
    # 倍率 = 1.105

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.数据2 = [int((1 + 0.35 * 1.2)*i) for i in self.数据2]
            # self.攻击次数2 *= (1 + 0.35 * 1.2)
        elif x == 1:
            self.CD *= 0.85
            self.数据2 = [int((1 + 0.35 * 1.58)*i) for i in self.数据2]
            # self.攻击次数2 *= (1 + 0.35 * 1.58)#改动位置

# 大回旋坠斩，护石暂不考虑跳跃
#   2020.8.13新增护石跳


class 技能18(主动技能):
    # 暂无数组
    名称 = '大回旋坠斩'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18

    基础 = (795.9230769 + 832.6695157)*1.1307
    成长 = (90.02136752 + 94.03418803)*1.1307
    攻击次数 = 10

    基础2 = 6902.951567*1.1298
    成长2 = 779.4108669*1.1298
    攻击次数2 = 1
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 += 1
            self.倍率 *= 1.16
        elif x == 1:
            self.攻击次数 += 1
            self.倍率 *= 1.23  # 改动位置

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)


# 致命焰火
class 技能19(主动技能):
    名称 = '致命焰火'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16

    # 移动射击攻击力：<data0>%
    数据 = [int(i*1.117) for i in [0, 1702, 1876, 2048, 2221, 2394, 2567, 2740, 2912, 3085, 3258, 3431, 3604, 3777, 3948, 4121, 4296, 4467, 4640, 4813, 4986, 5159, 5331, 5504, 5677, 5850, 6023, 6196, 6368, 6541, 6715, 6887, 7059, 7232, 7406,
                                 7578, 7751, 7923, 8096, 8269, 8442, 8615, 8787, 8960, 9134, 9306, 9479, 9652, 9823, 9998, 10170, 10342, 10515, 10688, 10861, 11034, 11206, 11379, 11553, 11725, 11898, 12071, 12243, 12417, 12590, 12762, 12934, 13108, 13280, 13453, 13625]]
    # 后方射击攻击力：<data2>%
    数据2 = [int(i*1.117) for i in [0, 1705, 1878, 2050, 2224, 2396, 2570, 2743, 2915, 3089, 3262, 3433, 3608, 3781, 3952, 4127, 4299, 4471, 4646, 4817, 4990, 5164, 5336, 5509, 5683, 5855, 6028, 6202, 6374, 6548, 6721, 6893, 7067, 7239, 7412,
                                  7586, 7758, 7931, 8105, 8277, 8450, 8624, 8796, 8969, 9142, 9315, 9488, 9661, 9834, 10008, 10180, 10353, 10527, 10699, 10872, 11046, 11218, 11391, 11564, 11737, 11910, 12083, 12256, 12429, 12602, 12775, 12948, 13121, 13294, 13466, 13640]]
    # 原地范围射击攻击力：<data1>%
    数据3 = [int(i*1.117) for i in [0, 2554, 2813, 3073, 3332, 3591, 3851, 4110, 4368, 4628, 4887, 5146, 5405, 5665, 5924, 6183, 6443, 6702, 6960, 7221, 7479, 7738, 7998, 8257, 8516, 8776, 9035, 9294, 9553, 9812, 10070, 10331, 10589, 10848, 11108, 11367,
                                  11626, 11885, 12145, 12404, 12662, 12923, 13181, 13440, 13700, 13959, 14218, 14478, 14737, 14996, 15256, 15515, 15773, 16034, 16292, 16551, 16811, 17070, 17329, 17588, 17847, 18106, 18365, 18625, 18883, 19142, 19402, 19661, 19920, 20180, 20439]]

    # 基础 = 1529.956522
    # 成长 = 172.7934783
    攻击次数 = 10

    # 基础2 = 1532.086957#后方
    # 成长2 = 172.923913
    攻击次数2 = 15

    # 基础3 = 2294.980237#原地
    # 成长3 = 259.215415
    攻击次数3 = 0  # 10
    CD = 40

    ###
    # 倍率 = 1.117

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础2 = self.基础3
            self.成长2 = self.成长3
            self.攻击次数2 = 10  # 猜测，否则提升过高
            self.倍率 *= 1.3
            self.CD *= 0.90


# 碧波瞬斩
class 技能20(主动技能):
    名称 = '碧波瞬斩'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    攻击次数 = 3
    # 基础 = 15133.18947
    # 成长 = 1708.524812
    CD = 50
    数据 = [int(i*1.10416) for i in [0, 16841, 18551, 20259, 21967, 23676, 25384, 27093, 28802, 30510, 32218, 33927, 35635, 37344, 39053, 40761, 42469, 44178, 45887, 47595, 49304, 51013, 52722, 54430, 56139, 57848, 59556, 61264, 62973, 64681, 66390, 68099, 69807, 71515, 73224, 74933,
                                 76641, 78350, 80058, 81766, 83476, 85185, 86894, 88602, 90310, 92019, 93727, 95436, 97145, 98853, 100561, 102270, 103979, 105687, 107396, 109104, 110812, 112521, 114230, 115940, 117648, 119356, 121065, 122773, 124482, 126191, 127899, 129607, 131316, 133025, 134733]]
    ###
    # 倍率 = 1.104

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 1
            self.数据 = [int(i*2.51*1.6) for i in self.数据]
            # self.倍率 *= 4.11#2.51*1.6
# 二觉


class 技能21(主动技能):
    名称 = '集结·暮光之翼'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    # 基础 = 81504.02778
    # 成长 = 24603.08333
    CD = 180
    # 剑术第1~4击攻击力：<data0>%
    数据 = [int(i*1.10633) for i in [0, 7958, 9803, 11648, 13494, 15339, 17184, 19030, 20876, 22721, 24567, 26412, 28256, 30103, 31948, 33793, 35639, 37484, 39329, 41175, 43021, 44866, 46712, 48557, 50401, 52248, 54093, 55938, 57784, 59629, 61474, 63320, 65166, 67011, 68857, 70702,
                                 72546, 74393, 76238, 78083, 79929, 81774, 83619, 85465, 87311, 89156, 91002, 92847, 94691, 96538, 98383, 100228, 102074, 103919, 105764, 107610, 109456, 111301, 113147, 114992, 116836, 118683, 120528, 122373, 124219, 126064, 127909, 129754, 131601, 133446, 135291]]
    攻击次数 = 4
    # 射击攻击力：<data1>%
    数据2 = [int(i*1.10633) for i in [0, 1929, 2376, 2823, 3270, 3719, 4165, 4613, 5060, 5508, 5954, 6403, 6850, 7297, 7745, 8192, 8639, 9088, 9534, 9982, 10429, 10876, 11323, 11770, 12219, 12665, 13113, 13560, 14008, 14454, 14903, 15350, 15797, 16245, 16693,
                                  17139, 17587, 18034, 18482, 18928, 19376, 19824, 20270, 20719, 21165, 21613, 22060, 22508, 22955, 23403, 23850, 24298, 24745, 25193, 25639, 26087, 26534, 26982, 27429, 27876, 28324, 28770, 29219, 29665, 30113, 30561, 31008, 31455, 31903, 32350, 32798]]
    攻击次数2 = 11
    # 最终齐射攻击力：<data2>%
    数据3 = [int(i*1.10633) for i in [0, 2122, 2613, 3106, 3597, 4091, 4582, 5074, 5566, 6059, 6551, 7042, 7535, 8026, 8520, 9011, 9503, 9995, 10488, 10980, 11471, 11964, 12455, 12949, 13440, 13932, 14424, 14917, 15409, 15900, 16393, 16884, 17378, 17869, 18361,
                                  18853, 19346, 19838, 20329, 20822, 21313, 21807, 22298, 22790, 23282, 23775, 24267, 24758, 25251, 25742, 26236, 26727, 27219, 27711, 28204, 28696, 29187, 29680, 30171, 30665, 31156, 31648, 32140, 32633, 33125, 33616, 34109, 34600, 35094, 35585, 36077]]
    攻击次数3 = 20
    # 最终齐射爆炸攻击力：<data3>%
    数据4 = [int(i*1.10633) for i in [0, 10610, 13071, 15531, 17992, 20453, 22914, 25374, 27835, 30295, 32755, 35216, 37676, 40137, 42598, 45059, 47519, 49980, 52440, 54900, 57361, 59821, 62282, 64742, 67204, 69664, 72125, 74585, 77045, 79506, 81966, 84427, 86887, 89349, 91809, 94270,
                                  96730, 99190, 101651, 104111, 106572, 109032, 111494, 113954, 116415, 118875, 121335, 123796, 126256, 128717, 131177, 133637, 136099, 138560, 141020, 143480, 145941, 148401, 150862, 153322, 155782, 158244, 160705, 163165, 165625, 168086, 170546, 173007, 175467, 177927, 180387]]
    攻击次数4 = 1

    ###
    # 倍率 = 1.107

# 95


class 技能22(主动技能):
    名称 = '燃情协战'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 1710
    成长 = 194
    攻击次数 = 10
    基础2 = 5134
    成长2 = 580
    攻击次数2 = 5
    基础3 = 42792
    成长3 = 4831
    攻击次数3 = 1

    基础4 = 2994
    成长4 = 339
    攻击次数4 = 0   # 10
    基础5 = 9272
    成长5 = 1047
    攻击次数5 = 0  # 6

    CD = 60  # 假设

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级) + self.攻击次数4 * (
                        self.基础4 + self.成长4 * self.等级) + self.攻击次数5 * (
                        self.基础5 + self.成长5 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)


# 三觉
class 技能23(主动技能):
    名称 = '暮光密令：黎明决战'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 916
    成长 = 277
    攻击次数 = 22
    基础2 = 18909
    成长2 = 5709
    攻击次数2 = 2
    基础3 = 15758
    成长3 = 4757
    攻击次数3 = 4
    基础4 = 1890
    成长4 = 571
    攻击次数4 = 16
    基础5 = 100852
    成长5 = 30446
    攻击次数5 = 1
    CD = 290  # 假设

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)+self.攻击次数4 * (
                        self.基础4 + self.成长4 * self.等级)+self.攻击次数5 * (
                        self.基础5 + self.成长5 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)


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

苍暮·暗刃一觉序号 = 0
苍暮·暗刃二觉序号 = 0
苍暮·暗刃三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        苍暮·暗刃一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        苍暮·暗刃二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        苍暮·暗刃三觉序号 = 技能序号[i.名称]

苍暮·暗刃护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        苍暮·暗刃护石选项.append(i.名称)

苍暮·暗刃符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        苍暮·暗刃符文选项.append(i.名称)


class 苍暮·暗刃角色属性(角色属性):
    实际名称 = '苍暮·暗刃'
    角色 = '枪剑士'
    职业 = '暗刃'

    武器选项 = ['长刀']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 1.85

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)


class 苍暮·暗刃(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 苍暮·暗刃角色属性()
        self.角色属性A = 苍暮·暗刃角色属性()
        self.角色属性B = 苍暮·暗刃角色属性()
        self.一觉序号 = 苍暮·暗刃一觉序号
        self.二觉序号 = 苍暮·暗刃二觉序号
        self.三觉序号 = 苍暮·暗刃三觉序号
        self.护石选项 = deepcopy(苍暮·暗刃护石选项)
        self.符文选项 = deepcopy(苍暮·暗刃符文选项)
        # QMessageBox.information(self, "提示",  "4.7日测试服数据，仅供参考")

    def 护石判断(self):
        if self.次数输入[self.角色属性A.技能序号['大回旋坠斩']].currentText() != '/CD':
            if self.次数输入[self.角色属性A.技能序号['大回旋坠斩']].currentText() != '':
                try:
                    大回旋坠斩次数 = round(
                        float(self.次数输入[self.角色属性A.技能序号['大回旋坠斩']].currentText()), 2)
                except:
                    pass
        else:
            大回旋坠斩次数 = 1

        sign = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '大回旋坠斩' and 大回旋坠斩次数 != 0:
                sign = 1
        if sign == 0:
            self.大回旋护石跳跃选项.setEnabled(False)
            self.大回旋护石跳跃选项.setStyleSheet(复选框样式)
            self.大回旋护石跳跃选项.setChecked(False)
        else:
            self.大回旋护石跳跃选项.setEnabled(True)
            self.大回旋护石跳跃选项.setStyleSheet(复选框样式)

    def 界面(self):
        super().界面()
        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(lambda state: self.护石判断())
        self.次数输入[self.角色属性A.技能序号['大回旋坠斩']].currentIndexChanged.connect(
            lambda state: self.护石判断())

        self.大回旋护石跳跃选项 = QCheckBox('大回旋护石跳跃释放', self.main_frame2)
        self.大回旋护石跳跃选项.resize(135, 20)
        self.大回旋护石跳跃选项.move(320, 420)
        self.大回旋护石跳跃选项.setStyleSheet(复选框样式)
        self.大回旋护石跳跃选项.setToolTip('跳跃释放大回旋坠斩，仅佩戴护石时生效')

        # self.轮盘连射类型选项=MyQComboBox(self.main_frame2)
        # self.轮盘连射类型选项.addItem('轮盘连射：非抓取')
        # self.轮盘连射类型选项.addItem('轮盘连射：抓取')
        # self.轮盘连射类型选项.resize(135,20)
        # self.轮盘连射类型选项.move(320,360)
        # self.轮盘连射类型选项.setToolTip('选择轮盘连射的形态')

        self.致命焰火方向选项 = MyQComboBox(self.main_frame2)
        self.致命焰火方向选项.addItem('致命焰火方向：向后')
        self.致命焰火方向选项.addItem('致命焰火方向：原地')
        self.致命焰火方向选项.resize(135, 20)
        self.致命焰火方向选项.move(320, 450)
        self.致命焰火方向选项.setToolTip('选择致命焰火的形态')

        self.战术协作方向选项 = MyQComboBox(self.main_frame2)
        self.战术协作方向选项.addItem('战术协作方向：原地')
        self.战术协作方向选项.addItem('战术协作方向：向前')
        self.战术协作方向选项.resize(135, 20)
        self.战术协作方向选项.move(320, 540)
        self.战术协作方向选项.setToolTip('选择燃情协战的形态')

        self.职业存档.append(('致命焰火方向选项', self.致命焰火方向选项, 1))
        self.职业存档.append(('战术协作方向选项', self.战术协作方向选项, 1))
        self.职业存档.append(('大回旋护石跳跃选项', self.大回旋护石跳跃选项, 0))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.大回旋护石跳跃选项.isChecked():
            属性.技能栏[属性.技能序号['大回旋坠斩']].攻击次数 = 0
            属性.技能栏[属性.技能序号['大回旋坠斩']].攻击次数2 = 3*1.07

        # if self.轮盘连射类型选项.currentIndex() == 1:
        #     属性.技能栏[属性.技能序号['轮盘连射']].攻击次数2 = 0
        #     属性.技能栏[属性.技能序号['轮盘连射']].攻击次数3 = 10

        if self.致命焰火方向选项.currentIndex() == 1:
            属性.技能栏[属性.技能序号['致命焰火']].攻击次数2 = 0
            属性.技能栏[属性.技能序号['致命焰火']].攻击次数3 = 10

        if self.战术协作方向选项.currentIndex() == 1:
            属性.技能栏[属性.技能序号['燃情协战']].攻击次数1 = 0
            属性.技能栏[属性.技能序号['燃情协战']].攻击次数2 = 0
            属性.技能栏[属性.技能序号['燃情协战']].攻击次数3 = 0
            属性.技能栏[属性.技能序号['燃情协战']].攻击次数4 = 10
            属性.技能栏[属性.技能序号['燃情协战']].攻击次数5 = 6
