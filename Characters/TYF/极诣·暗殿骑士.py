from PublicReference.base import *

# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '太刀':
#             return round(self.CD / self.恢复 * 1, 1)
#         if 武器类型 == '短剑':
#             return round(self.CD / self.恢复 * 1.05, 1)
#         if 武器类型 == '钝器':
#             return round(self.CD / self.恢复 * 1, 1)
#         if 武器类型 == '巨剑':
#             return round(self.CD / self.恢复 * 1, 1)


class 技能0(主动技能):
    名称 = '暗影之矛'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    data0 = [int(i*1.20) for i in [0, 300, 331, 361, 391, 422, 453, 483, 514, 545, 574, 605, 636, 666, 697, 727, 758, 788, 819, 850, 879, 910, 941, 971, 1002, 1033, 1062, 1093, 1124, 1155, 1185, 1215, 1246, 1276, 1307, 1338, 1367,
           1398, 1429, 1460, 1490, 1521, 1551, 1581, 1612, 1643, 1672, 1703, 1734, 1765, 1795, 1826, 1857, 1886, 1917, 1948, 1978, 2009, 2039, 2069, 2100, 2131, 2162, 2191, 2222, 2253, 2283, 2314, 2345, 2374, 2405]]
    攻击次数 = 8
    CD = 5.0
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能1(被动技能):
    名称 = '乌希尔的诅咒'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.10 + 0.02 * self.等级, 5)


class 技能2(主动技能):
    名称 = '暗影缠袭'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data0 = [int(i*1.20) for i in [0, 85, 94, 103, 111, 120, 129, 138, 145, 155, 164, 173, 180, 189, 198, 206, 215, 224, 233, 241, 250, 259, 268, 276, 285, 294, 303, 310, 319, 328, 337, 345, 354, 363, 372,
           380, 389, 398, 407, 415, 424, 433, 442, 449, 458, 467, 476, 484, 493, 502, 511, 519, 528, 537, 546, 554, 563, 572, 581, 588, 597, 606, 615, 623, 632, 641, 650, 658, 667, 676, 685]]
    攻击次数 = 0  # 抓取不了建筑
    data1 = [int(i*1.20) for i in [0, 828, 912, 995, 1079, 1163, 1248, 1331, 1415, 1499, 1584, 1667, 1751, 1835, 1920, 2003, 2087, 2171, 2256, 2339, 2423, 2507, 2592, 2675, 2759, 2843, 2926, 3011, 3095, 3179, 3263, 3348, 3431, 3515, 3599, 3684,
           3767, 3851, 3935, 4020, 4103, 4187, 4271, 4354, 4439, 4523, 4607, 4690, 4775, 4859, 4943, 5026, 5111, 5195, 5279, 5362, 5447, 5531, 5615, 5698, 5782, 5867, 5951, 6035, 6118, 6203, 6287, 6371, 6454, 6539, 6623]]
    攻击次数2 = 4  # 受站位影响
    CD = 7.0
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能3(主动技能):
    名称 = '暗影漩涡'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data0 = [int(i*1.20) for i in [0, 1365, 1504, 1642, 1781, 1918, 2057, 2195, 2334, 2473, 2611, 2750, 2888, 3027, 3166, 3304, 3443, 3581, 3720, 3857, 3996, 4135, 4273, 4412, 4550, 4689, 4828, 4966, 5105, 5243, 5382, 5520, 5659, 5798, 5935, 6074,
           6212, 6351, 6490, 6628, 6767, 6905, 7044, 7182, 7321, 7460, 7598, 7737, 7874, 8013, 8152, 8290, 8429, 8567, 8706, 8844, 8983, 9122, 9260, 9399, 9537, 9676, 9815, 9952, 10091, 10229, 10368, 10506, 10645, 10784, 10922]]
    data1 = [int(i*1.20) for i in [0, 273, 300, 328, 355, 384, 411, 439, 466, 494, 521, 550, 577, 605, 632, 660, 688, 716, 743, 771, 798, 827, 854, 882, 909, 937, 964, 993, 1020, 1048, 1075, 1103, 1130, 1159, 1186, 1214, 1241, 1269,
           1297, 1325, 1353, 1380, 1409, 1436, 1464, 1491, 1519, 1546, 1575, 1602, 1630, 1657, 1685, 1712, 1741, 1768, 1796, 1823, 1851, 1878, 1907, 1934, 1962, 1989, 2018, 2045, 2073, 2100, 2128, 2155, 2184]]
    攻击次数2 = 6
    CD = 6.0
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能4(被动技能):
    名称 = '汲魂之力'
    所在等级 = 25
    等级上限 = 30
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.10 + 0.02 * self.等级, 5)


class 技能5(主动技能):
    名称 = '暗影禁锢'
    所在等级 = 25
    等级上限 = 70
    基础等级 = 41
    data0 = [int(i*1.20) for i in [0, 3879, 4272, 4666, 5060, 5453, 5847, 6241, 6633, 7027, 7421, 7814, 8208, 8602, 8994, 9388, 9782, 10175, 10569, 10963, 11356, 11750, 12144, 12536, 12930, 13324, 13717, 14111, 14505, 14898, 15292, 15686, 16080, 16472, 16866, 17260, 17653,
           18047, 18441, 18834, 19228, 19622, 20014, 20408, 20802, 21195, 21589, 21983, 22375, 22769, 23163, 23556, 23950, 24344, 24737, 25131, 25525, 25917, 26311, 26705, 27098, 27492, 27886, 28279, 28673, 29067, 29459, 29853, 30247, 30640, 31034]]
    data1 = [int(i*1.20) for i in [0, 2585, 2848, 3111, 3373, 3635, 3897, 4160, 4423, 4684, 4947, 5209, 5472, 5735, 5996, 6259, 6521, 6784, 7046, 7308, 7571, 7833, 8096, 8357, 8620, 8882, 9145, 9408, 9669, 9932, 10194, 10457, 10720, 10981, 11244, 11506, 11769,
           12030, 12293, 12556, 12818, 13081, 13342, 13605, 13868, 14130, 14392, 14654, 14917, 15180, 15442, 15704, 15966, 16229, 16492, 16754, 17016, 17278, 17541, 17804, 18065, 18328, 18590, 18853, 19116, 19377, 19640, 19902, 20165, 20426, 20689]]
    CD = 12
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] + self.data1[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能6(主动技能):
    名称 = '灵魂摄取'
    所在等级 = 30
    等级上限 = 70
    基础等级 = 41
    data0 = [int(i*1.20) for i in [0, 501, 551, 603, 653, 704, 754, 806, 856, 908, 958, 1009, 1060, 1111, 1161, 1213, 1263, 1315, 1365, 1416, 1466, 1518, 1568, 1620, 1670, 1721, 1772, 1823, 1873, 1925, 1975, 2027, 2077, 2128, 2178, 2230,
           2280, 2332, 2382, 2433, 2484, 2535, 2585, 2637, 2687, 2739, 2789, 2840, 2890, 2942, 2992, 3044, 3094, 3145, 3196, 3247, 3297, 3349, 3399, 3451, 3501, 3552, 3602, 3654, 3704, 3756, 3806, 3857, 3908, 3958, 4009]]
    攻击次数 = 10
    CD = 8
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能7(主动技能):
    名称 = '释魂飞弹'
    所在等级 = 30
    等级上限 = 70
    基础等级 = 26
    data0 = [int(i*1.24) for i in [0, 599, 694, 791, 886, 981, 1076, 1172, 1268, 1363, 1459, 1554, 1651, 1746, 1841, 1936, 2032, 2128, 2224, 2319, 2414, 2511, 2606, 2701, 2796, 2892, 2988, 3084, 3179, 3274, 3371, 3466, 3561, 3657, 3753, 3848,
           3944, 4039, 4134, 4231, 4326, 4421, 4517, 4613, 4708, 4804, 4899, 4994, 5091, 5186, 5281, 5377, 5473, 5568, 5664, 5759, 5854, 5951, 6046, 6141, 6237, 6333, 6428, 6524, 6619, 6714, 6811, 6906, 7001, 7097, 7193]]
    攻击次数 = 4
    CD = 5
    TP成长 = 0.14
    TP上限 = 3

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            if self.TP等级 >= 1:
                return (self.data0[self.等级] * self.攻击次数 * 2) * (0.72 + self.TP成长 * self.TP等级) * self.倍率
            else:
                return (self.data0[self.等级] * self.攻击次数 * 2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能8(主动技能):
    名称 = '魅影暗魂斩'
    所在等级 = 30
    等级上限 = 70
    基础等级 = 38
    data0 = [int(i*1.20) for i in [0, 1444, 1591, 1738, 1885, 2030, 2177, 2324, 2471, 2618, 2765, 2912, 3058, 3205, 3352, 3499, 3645, 3792, 3939, 4085, 4232, 4379, 4526, 4673, 4820, 4965, 5112, 5258, 5404, 5551, 5697, 5844, 5991, 6138, 6285, 6432,
           6579, 6724, 6871, 7018, 7165, 7312, 7459, 7604, 7751, 7898, 8045, 8192, 8339, 8486, 8632, 8779, 8925, 9072, 9219, 9366, 9513, 9659, 9804, 9951, 10098, 10244, 10391, 10538, 10684, 10831, 10978, 11125, 11271, 11418, 11565]]
    data1 = [int(i*1.20) for i in [0, 1543, 1699, 1855, 2012, 2168, 2324, 2480, 2638, 2794, 2950, 3107, 3263, 3419, 3575, 3732, 3888, 4044, 4202, 4359, 4515, 4673, 4829, 4985, 5142, 5298, 5454, 5610, 5767, 5923, 6079, 6237, 6393, 6549, 6705, 6862, 7020,
           7177, 7333, 7489, 7646, 7802, 7958, 8114, 8272, 8428, 8584, 8741, 8897, 9053, 9209, 9366, 9522, 9681, 9837, 9993, 10149, 10307, 10463, 10619, 10776, 10932, 11088, 11244, 11401, 11557, 11713, 11871, 12027, 12183, 12342]]
    攻击次数 = 1
    攻击次数2 = 4
    CD = 11.0
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能9(主动技能):
    名称 = '魔镜幻影阵'
    所在等级 = 35
    等级上限 = 70
    基础等级 = 36
    基础 = 9239.657
    成长 = 1043.343
    # 生成攻击力
    data0 = [int(i*1.20) for i in [0, 791, 870, 951, 1031, 1111, 1192, 1272, 1352, 1433, 1513, 1593, 1674, 1754, 1833, 1915, 1994, 2074, 2155, 2235, 2315, 2396, 2476, 2556, 2637, 2717, 2796, 2878, 2957, 3037, 3118, 3198, 3278, 3359, 3439, 3519,
           3600, 3680, 3760, 3841, 3920, 4000, 4081, 4161, 4241, 4322, 4402, 4482, 4563, 4643, 4723, 4804, 4883, 4963, 5044, 5124, 5204, 5285, 5365, 5445, 5526, 5606, 5686, 5767, 5847, 5926, 6007, 6087, 6167, 6248, 6328]]
    # 幻镜攻击力
    data1 = [int(i*1.20) for i in [0, 791, 872, 951, 1031, 1112, 1192, 1272, 1353, 1433, 1513, 1594, 1674, 1754, 1835, 1915, 1994, 2075, 2155, 2236, 2316, 2396, 2477, 2557, 2637, 2718, 2798, 2878, 2959, 3039, 3118, 3199, 3279, 3360, 3440, 3520,
           3601, 3681, 3761, 3842, 3922, 4002, 4083, 4162, 4242, 4323, 4403, 4484, 4564, 4644, 4725, 4805, 4885, 4966, 5046, 5126, 5207, 5286, 5366, 5447, 5527, 5608, 5688, 5768, 5849, 5929, 6009, 6090, 6170, 6250, 6331]]
    攻击次数2 = 12
    CD = 15.0
    倍率 = 1
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.21
        elif x == 1:
            self.倍率 *= 1.30

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>魔镜低鸣</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[魔镜幻影阵]<br>"
            temp += "防护罩持续时间内移动速度 +10%<br>"
            temp += "镜阵攻击力 +14%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "防护罩持续时间内移动速度 +5%<br>"
            temp += "镜阵攻击力 +7%"
        elif x == 1:
            temp = "<font color='#FF00FF'>魔镜低鸣</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[魔镜幻影阵]<br>"
            temp += "防护罩持续时间内移动速度 +10%<br>"
            temp += "镜阵攻击力 +14%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "防护罩持续时间内移动速度 +5%<br>"
            temp += "镜阵攻击力 +16%"
        return temp

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能10(主动技能):
    名称 = '释魂狂怒'
    所在等级 = 35
    等级上限 = 70
    基础等级 = 36
    data0 = [int(i*1.24) for i in [0, 14715, 16207, 17701, 19193, 20686, 22178, 23672, 25164, 26658, 28150, 29643, 31136, 32629, 34121, 35615, 37107, 38601, 40093, 41586, 43078, 44572, 46064, 47558, 49050, 50543, 52036, 53529, 55021, 56515, 58007, 59501, 60993, 62486, 63978, 65472,
           66964, 68458, 69950, 71443, 72936, 74429, 75921, 77415, 78907, 80401, 81893, 83386, 84878, 86372, 87865, 89358, 90851, 92343, 93837, 95329, 96823, 98315, 99808, 101301, 102794, 104286, 105780, 107272, 108765, 110258, 111751, 113243, 114737, 116229, 117723]]
    CD = 15
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能11(主动技能):
    名称 = '暗影囚杀'
    所在等级 = 40
    等级上限 = 70
    基础等级 = 33
    data0 = [int(i*1.20) for i in [0, 313, 345, 377, 409, 440, 473, 505, 537, 568, 600, 632, 664, 695, 727, 760, 792, 823, 855, 887, 919, 950, 982, 1015, 1047, 1078, 1110, 1142, 1174, 1205, 1237, 1269, 1302, 1333, 1365, 1397, 1429,
           1460, 1492, 1524, 1557, 1587, 1620, 1652, 1684, 1715, 1747, 1779, 1810, 1842, 1875, 1907, 1938, 1970, 2002, 2034, 2065, 2097, 2130, 2162, 2193, 2225, 2257, 2289, 2320, 2352, 2384, 2417, 2448, 2480, 2512]]
    攻击次数 = 14
    data1 = [int(i*1.20) for i in [0, 9525, 10492, 11457, 12424, 13391, 14357, 15324, 16289, 17256, 18223, 19189, 20156, 21121, 22088, 23055, 24021, 24988, 25953, 26920, 27887, 28853, 29820, 30785, 31752, 32719, 33685, 34652, 35617, 36584, 37551, 38517, 39484, 40449, 41416,
           42383, 43349, 44316, 45281, 46248, 47215, 48181, 49148, 50113, 51080, 52046, 53013, 53980, 54945, 55912, 56878, 57845, 58812, 59777, 60744, 61710, 62677, 63644, 64609, 65576, 66542, 67509, 68476, 69441, 70408, 71374, 72341, 73308, 74273, 75240, 76206]]
    攻击次数2 = 1
    # 护石
    data2 = [int(x*1.0) for x in data0]
    攻击次数3 = 0
    护石黑暗气息 = 0
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 5
            self.攻击次数2 *= 1.52
            self.攻击次数3 = 4
            self.护石黑暗气息 = 1.32
        elif x == 1:
            self.攻击次数 = 5
            self.攻击次数2 *= 1.52
            self.攻击次数3 = 4
            self.护石黑暗气息 = 2.31

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>暗影囚狱</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[暗影囚杀]<br>"
            temp += "斩击多段攻击次数 -9次<br>"
            temp += "最后一击强制控制敌人1.5秒<br>"
            temp += "最后一击攻击力 +52%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "最后一击控制结束时， 黑暗气息爆炸并造成多段伤害<br>"
            temp += "- 黑暗气息的攻击力为多段攻击力的132%<br>"
            temp += "- 多段攻击次数 : 4<br>"
            temp += "斩击多段攻击速度 +20%"
        elif x == 1:
            temp = "<font color='#FF00FF'>暗影囚狱</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[暗影囚杀]<br>"
            temp += "斩击多段攻击次数 -9次<br>"
            temp += "最后一击强制控制敌人1.5秒<br>"
            temp += "最后一击攻击力 +52%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "最后一击控制结束时， 黑暗气息爆炸并造成多段伤害<br>"
            temp += "- 黑暗气息的攻击力为多段攻击力的231%<br>"
            temp += "- 多段攻击次数 : 4<br>"
            temp += "斩击多段攻击速度 +20%"
        return temp

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3 * self.护石黑暗气息) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能12(主动技能):
    名称 = '暗影盛宴'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data0 = [int(i*1.00) for i in [0, 1786, 1967, 2149, 2330, 2512, 2692, 2874, 3055, 3237, 3418, 3599, 3780, 3962, 4143, 4323, 4505, 4687, 4868, 5050, 5230, 5411, 5593, 5774, 5956, 6136, 6318, 6499, 6681, 6862, 7043, 7224, 7406, 7587, 7769, 7949, 8131,
           8312, 8494, 8675, 8855, 9037, 9219, 9400, 9582, 9762, 9943, 10125, 10306, 10488, 10668, 10850, 11031, 11213, 11394, 11575, 11756, 11938, 12119, 12299, 12481, 12663, 12844, 13026, 13206, 13387, 13569, 13751, 13932, 14112, 14294]]
    攻击次数 = 15
    # 护石数据
    data1 = [int(x*1.0) for x in data0]
    攻击次数2 = 0
    CD = 40
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = (2.25 + 5.19) * 0.5
            self.CD *= 0.84
        elif x == 1:
            self.攻击次数2 = (2.25 + 7.59) * 0.5
            self.CD *= 0.84

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>暗影聚合</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[暗影盛宴]<br>"
            temp += "发射剑气后， 生成并发射暗影球<br>"
            temp += "- 暗影球攻击力为爆炸攻击力的225%<br>"
            temp += "冷却时间 -16%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "剑气爆炸攻击次数 +100%<br>"
            temp += "多段攻击间隔 -50%<br>"
            temp += "剑气爆炸攻击力 -50%<br>"
            temp += "暗影球攻击力比率 +519%"
        elif x == 1:
            temp = "<font color='#FF00FF'>暗影聚合</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[暗影盛宴]<br>"
            temp += "发射剑气后， 生成并发射暗影球<br>"
            temp += "- 暗影球攻击力为爆炸攻击力的225%<br>"
            temp += "冷却时间 -16%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "剑气爆炸攻击次数 +100%<br>"
            temp += "多段攻击间隔 -50%<br>"
            temp += "剑气爆炸攻击力 -50%<br>"
            temp += "暗影球攻击力比率 +759%"
        return temp

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能13(被动技能):
    名称 = '灵魂傀儡'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.055 + 0.015 * self.等级, 5)


class 技能14(主动技能):
    名称 = '末日杀戮'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 48299.2 * 1.1
    成长 = 14582 * 1.1
    # 刺击魔法攻击
    data0 = [int(i*1.20) for i in [0, 886, 1091, 1297, 1501, 1707, 1913, 2118, 2324, 2529, 2735, 2941, 3145, 3351, 3556, 3762, 3968, 4173, 4379, 4584, 4790, 4996, 5200, 5406, 5611, 5817, 6022, 6228, 6434, 6638, 6844, 7049, 7255, 7461, 7666, 7872, 8076,
           8282, 8488, 8693, 8899, 9104, 9310, 9515, 9721, 9927, 10131, 10337, 10542, 10748, 10954, 11159, 11365, 11569, 11775, 11981, 12186, 12392, 12597, 12803, 13009, 13214, 13420, 13624, 13830, 14035, 14241, 14447, 14652, 14858, 15062]]
    攻击次数 = 1
    # 魅影连击
    data1 = [int(i*1.20) for i in [0, 1778, 2190, 2602, 3015, 3427, 3839, 4251, 4665, 5077, 5489, 5902, 6314, 6726, 7138, 7551, 7963, 8375, 8787, 9200, 9612, 10024, 10438, 10850, 11262, 11674, 12087, 12499, 12911, 13324, 13736, 14148, 14560, 14974, 15386, 15798, 16211,
           16623, 17035, 17447, 17860, 18272, 18684, 19096, 19509, 19921, 20333, 20747, 21159, 21571, 21983, 22396, 22808, 23220, 23633, 24045, 24457, 24869, 25283, 25695, 26107, 26520, 26932, 27344, 27756, 28169, 28581, 28993, 29405, 29819, 30231]]
    攻击次数2 = 5
    # 最终一击
    data2 = [int(i*1.20) for i in [0, 7554, 9306, 11057, 12809, 14560, 16313, 18065, 19816, 21568, 23319, 25071, 26822, 28575, 30327, 32078, 33830, 35581, 37334, 39086, 40837, 42589, 44340, 46093, 47844, 49596, 51348, 53099, 54851, 56602, 58355, 60107, 61858, 63610, 65361, 67114, 68865,
           70617, 72369, 74120, 75872, 77623, 79376, 81128, 82879, 84631, 86382, 88135, 89887, 91638, 93390, 95141, 96893, 98644, 100397, 102149, 103900, 105652, 107403, 109156, 110908, 112659, 114411, 116162, 117914, 119665, 121418, 123170, 124921, 126673, 128424]]
    攻击次数3 = 5
    # 爆炸
    data3 = [int(i*1.20) for i in [0, 15338, 18895, 22451, 26009, 29565, 33122, 36678, 40236, 43792, 47349, 50906, 54463, 58020, 61576, 65133, 68689, 72247, 75803, 79360, 82918, 86474, 90031, 93587, 97144, 100701, 104258, 107814, 111371, 114929, 118485, 122042, 125598, 129156, 132712, 136269, 139825,
           143382, 146939, 150496, 154053, 157609, 161167, 164723, 168280, 171836, 175394, 178950, 182507, 186064, 189620, 193178, 196734, 200291, 203847, 207405, 210961, 214518, 218075, 221632, 225189, 228745, 232302, 235858, 239416, 242972, 246529, 250087, 253643, 257200, 260756]]
    攻击次数4 = 1
    CD = 145.0
    倍率 = 1.1

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3 + self.data3[self.等级] * self.攻击次数4) * self.倍率


class 技能15(主动技能):
    名称 = '魔影轰杀'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data0 = [int(i*1.32) for i in [0, 5453, 6006, 6560, 7113, 7666, 8219, 8773, 9327, 9879, 10433, 10986, 11539, 12092, 12646, 13199, 13752, 14305, 14859, 15413, 15965, 16519, 17072, 17626, 18178, 18732, 19285, 19838, 20391, 20945, 21499, 22051, 22605, 23158, 23712, 24264,
           24818, 25371, 25925, 26477, 27031, 27585, 28137, 28691, 29244, 29798, 30350, 30904, 31457, 32011, 32563, 33117, 33671, 34223, 34777, 35330, 35884, 36436, 36990, 37544, 38097, 38649, 39203, 39757, 40310, 40863, 41416, 41970, 42522, 43076, 43630]]
    攻击次数 = 4
    CD = 30.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    倍率 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.14
        elif x == 1:
            self.倍率 *= 1.22

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>暗影随行</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[魔影轰杀]<br>"
            temp += "魔影由追踪敌人变更为环绕在自身周围<br>"
            temp += "- 再次按技能键时发射魔影技能<br>"
            temp += "- 持续时间10秒 (持续时间结束时自动发射)<br>"
            temp += "- 爆炸次数 -3次<br>"
            temp += "- 魔影攻击力为爆炸攻击力的1%<br>"
            temp += "爆炸攻击力 +5%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "追踪范围 +200px<br>"
            temp += "爆炸攻击力 +9%"
        elif x == 1:
            temp = "<font color='#FF00FF'>暗影随行</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[魔影轰杀]<br>"
            temp += "魔影由追踪敌人变更为环绕在自身周围<br>"
            temp += "- 再次按技能键时发射魔影技能<br>"
            temp += "- 持续时间10秒 (持续时间结束时自动发射)<br>"
            temp += "- 爆炸次数 -3次<br>"
            temp += "- 魔影攻击力为爆炸攻击力的1%<br>"
            temp += "爆炸攻击力 +5%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "追踪范围 +200px<br>"
            temp += "爆炸攻击力 +17%"
        return temp

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能16(主动技能):
    名称 = '死亡献祭'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data0 = [int(i*1.20) for i in [0, 1660, 1827, 1996, 2164, 2333, 2500, 2669, 2838, 3006, 3174, 3342, 3511, 3680, 3848, 4016, 4184, 4353, 4522, 4689, 4858, 5026, 5195, 5362, 5531, 5700, 5868, 6037, 6204, 6373, 6542, 6710, 6878, 7046, 7215, 7384, 7552,
           7720, 7889, 8057, 8226, 8393, 8562, 8731, 8899, 9067, 9235, 9404, 9573, 9741, 9909, 10077, 10246, 10415, 10582, 10751, 10919, 11088, 11255, 11424, 11593, 11761, 11930, 12097, 12266, 12435, 12603, 12771, 12939, 13108, 13277]]
    攻击次数 = 11
    data1 = [int(i*1.20) for i in [0, 19001, 20928, 22856, 24783, 26710, 28639, 30567, 32494, 34421, 36349, 38277, 40205, 42132, 44060, 45987, 47916, 49843, 51770, 53698, 55625, 57554, 59481, 61409, 63336, 65263, 67191, 69119, 71047, 72974, 74902, 76829, 78758, 80685, 82612, 84540, 86467,
           88396, 90323, 92251, 94178, 96105, 98034, 99962, 101889, 103816, 105744, 107672, 109600, 111527, 113455, 115382, 117311, 119238, 121165, 123093, 125020, 126949, 128876, 130804, 132731, 134658, 136587, 138514, 140442, 142369, 144297, 146225, 148153, 150080, 152007]]
    攻击次数2 = 1
    CD = 50.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 *= 1.31
        elif x == 1:
            self.攻击次数2 *= 1.46

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>无上祭品</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[死亡献祭]<br>"
            temp += "在前方召唤幻影， 替代自身生成魔法阵<br>"
            temp += "增加以幻影为中心吸附敌人的功能<br>"
            temp += "[死亡献祭]爆炸攻击力 +27%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "幻影生成魔法阵时， 可以移动<br>"
            temp += "[死亡献祭]爆炸攻击力 +4%"
        elif x == 1:
            temp = "<font color='#FF00FF'>无上祭品</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[死亡献祭]<br>"
            temp += "在前方召唤幻影， 替代自身生成魔法阵<br>"
            temp += "增加以幻影为中心吸附敌人的功能<br>"
            temp += "[死亡献祭]爆炸攻击力 +27%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "幻影生成魔法阵时， 可以移动<br>"
            temp += "[死亡献祭]爆炸攻击力 +19%"
        return temp

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能17(主动技能):
    名称 = '天罚死光'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据 = [int(i*1.32) for i in [0, 52556, 57887, 63219, 68550, 73882, 79215, 84546, 89878, 95209, 100541, 105872, 111205, 116537, 121868, 127200, 132531, 137864, 143196, 148527, 153859, 159190, 164522, 169855, 175186, 180518, 185849, 191181, 196514, 201845, 207177, 212508, 217840, 223171, 228504, 233836,
          239167, 244499, 249830, 255163, 260495, 265826, 271158, 276489, 281821, 287154, 292485, 297817, 303148, 308480, 313813, 319144, 324476, 329807, 335139, 340470, 345803, 351135, 356466, 361798, 367129, 372461, 377794, 383125, 388457, 393788, 399120, 404453, 409784, 415116, 420447]]
    CD = 40.0
    # 蓄力倍率
    倍率 = 1.1
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1 + 0.03 * 1.96 * 4

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.倍率


class 技能18(被动技能):
    名称 = '薄暮'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['暗影之矛', '暗影缠袭', '灵魂摄取', '魅影暗魂斩', '暗影禁锢', '暗影漩涡', '魔镜幻影阵', '暗影囚杀', '末日杀戮',
            '魔影轰杀', '死亡献祭', '暗影盛宴', '天罚死光', '天罚之剑', '神罚·灭世裁决', '暗影绽放：死亡荆棘', '冥王降临：净土救赎']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.24 + 0.02 * self.等级, 5)


class 技能19(主动技能):
    名称 = '天罚之剑'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    data0 = [int(i*1.11) for i in [0, 17407, 19172, 20939, 22705, 24470, 26237, 28002, 29768, 31535, 33300, 35066, 36833, 38598, 40364, 42130, 43896, 45662, 47428, 49194, 50959, 52726, 54492, 56257, 58024, 59790, 61555, 63322, 65087, 66853, 68620, 70385, 72152, 73917, 75683, 77450, 79215,
           80981, 82748, 84513, 86279, 88044, 89811, 91577, 93342, 95109, 96874, 98641, 100407, 102172, 103939, 105705, 107470, 109237, 111002, 112768, 114535, 116300, 118066, 119831, 121598, 123364, 125130, 126896, 128662, 130428, 132194, 133959, 135726, 137492, 139257]]
    data1 = [int(i*1.11) for i in [0, 45626, 50256, 54885, 59513, 64142, 68772, 73400, 78029, 82658, 87287, 91916, 96544, 101173, 105802, 110431, 115060, 119689, 124317, 128947, 133576, 138204, 142833, 147463, 152091, 156720, 161348, 165978, 170607, 175235, 179864, 184494, 189122, 193751, 198379, 203009,
           207638, 212266, 216895, 221525, 226153, 230782, 235410, 240040, 244669, 249297, 253926, 258556, 263184, 267813, 272441, 277070, 281700, 286328, 290957, 295586, 300215, 304844, 309473, 314101, 318731, 323359, 327988, 332617, 337246, 341875, 346504, 351132, 355762, 360391, 365019]]
    CD = 45
    倍率 = 1.1
    # 护石倍率
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.33

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] + self.data1[self.等级]) * self.倍率


class 技能20(主动技能):
    名称 = '神罚·灭世裁决'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    data0 = [int(i*1.25) for i in [0, 9891, 12184, 14477, 16771, 19064, 21358, 23651, 25944, 28239, 30532, 32825, 35119, 37412, 39705, 42000, 44293, 46587, 48880, 51173, 53467, 55760, 58053, 60348, 62641, 64935, 67228, 69521, 71815, 74109, 76402, 78696, 80989, 83283, 85576, 87869, 90164, 92457,
           94750, 97044, 99337, 101631, 103924, 106217, 108512, 110805, 113098, 115392, 117685, 119978, 122273, 124566, 126860, 129153, 131446, 133740, 136033, 138326, 140621, 142914, 145208, 147501, 149794, 152089, 154382, 156675, 158969, 161262, 163556, 165849, 168142]]
    攻击次数 = 7
    data1 = [int(i*1.25) for i in [0, 69235, 85289, 101344, 117398, 133453, 149508, 165562, 181617, 197671, 213726, 229781, 245835, 261890, 277944, 293999, 310054, 326108, 342163, 358217, 374272, 390328, 406381, 422436, 438490, 454545, 470601, 486654, 502710, 518763, 534818, 550874, 566927, 582983, 599036, 615092,
           631147, 647201, 663256, 679309, 695365, 711418, 727474, 743529, 759583, 775638, 791691, 807747, 823802, 839856, 855911, 871965, 888020, 904075, 920129, 936184, 952238, 968293, 984348, 1000402, 1016457, 1032511, 1048566, 1064621, 1080675, 1096730, 1112784, 1128839, 1144894, 1160948, 1177003]]
    CD = 180.0
    倍率 = 1.1

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级]) * self.倍率


class 技能21(被动技能):
    名称 = '以身载灵'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.18 + 0.02 * self.等级, 5)


class 技能22(主动技能):
    名称 = '暗影绽放：死亡荆棘'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    data0 = [int(i*1.13) for i in [0, 38764, 42693, 46623, 50553, 54483, 58413, 62343, 66273, 70203, 74133, 78063, 81993, 85923, 89853, 93783, 97713, 101643, 105573, 109502, 113432, 117362, 121292, 125222, 129152, 133082, 137012, 140942, 144872, 148802, 152732, 156662, 160592, 164522, 168452, 172382,
           176312, 180241, 184171, 188101, 192031, 195961, 199891, 203821, 207751, 211681, 215611, 219541, 223471, 227401, 231331, 235261, 239191, 243121, 247050, 250980, 254910, 258840, 262770, 266700, 270630, 274560, 278490, 282420, 286350, 290280, 294210, 298140, 302070, 306000, 309930]]
    data1 = [int(i*1.13) for i in [0, 90448, 99618, 108788, 117958, 127128, 136298, 145467, 154637, 163807, 172977, 182147, 191317, 200487, 209656, 218826, 227996, 237166, 246336, 255506, 264676, 273846, 283015, 292185, 301355, 310525, 319695, 328865, 338035, 347204, 356374, 365544, 374714, 383884, 393054, 402224,
           411394, 420563, 429733, 438903, 448073, 457243, 466413, 475583, 484752, 493922, 503092, 512262, 521432, 530602, 539772, 548941, 558111, 567281, 576451, 585621, 594791, 603961, 613131, 622300, 631470, 640640, 649810, 658980, 668150, 677320, 686489, 695659, 704829, 713999, 723169]]
    CD = 60.0

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] + self.data1[self.等级]) * self.倍率


class 技能23(主动技能):
    名称 = '冥王降临：净土救赎'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 = [int(i*1.20) for i in [0, 11941, 14710, 17479, 20248, 23017, 25786, 28555, 31324, 34093, 36862, 39631, 42400, 45169, 47938, 50707, 53476, 56245, 59014, 61783, 64552, 67321, 70090, 72859, 75628, 78397, 81166, 83935, 86704, 89473, 92242, 95011, 97780, 100549, 103317, 106087, 108856,
           111624, 114393, 117162, 119931, 122700, 125469, 128238, 131007, 133776, 136545, 139314, 142083, 144852, 147621, 150390, 153159, 155928, 158697, 161466, 164235, 167004, 169773, 172542, 175311, 178080, 180849, 183618, 186387, 189156, 191925, 194694, 197463, 200232, 203001]]
    攻击次数 = 10
    data1 = [int(i*1.20) for i in [0, 278627, 343238, 407846, 472456, 537066, 601674, 666285, 730895, 795503, 860113, 924723, 989331, 1053942, 1118552, 1183162, 1247770, 1312381, 1376991, 1441599, 1506209, 1570819, 1635427, 1700038, 1764648, 1829256, 1893866, 1958476, 2023084, 2087695, 2152305, 2216913, 2281523, 2346134, 2410742, 2475352,
           2539962, 2604570, 2669180, 2733791, 2798399, 2863009, 2927619, 2992227, 3056838, 3121448, 3186058, 3250666, 3315276, 3379887, 3444495, 3509105, 3573715, 3638323, 3702934, 3767544, 3832152, 3896762, 3961372, 4025980, 4090591, 4155201, 4219809, 4284419, 4349030, 4413638, 4478248, 4542858, 4607466, 4672076, 4736687]]
    CD = 290.0
    关联技能 = ['无']

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级]) * self.倍率

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

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

极诣·暗殿骑士一觉序号 = 0
极诣·暗殿骑士二觉序号 = 0
极诣·暗殿骑士三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        极诣·暗殿骑士一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        极诣·暗殿骑士二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        极诣·暗殿骑士三觉序号 = 技能序号[i.名称]

极诣·暗殿骑士护石选项 = [
    '无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣·暗殿骑士护石选项.append(i.名称)

极诣·暗殿骑士符文选项 = [
    '无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        极诣·暗殿骑士符文选项.append(i.名称)


class 极诣·暗殿骑士角色属性(角色属性):
    实际名称 = '极诣·暗殿骑士'
    角色 = '鬼剑士(女)'
    职业 = '暗殿骑士'

    武器选项 = ['太刀', '短剑', '巨剑', '钝器']

    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '板甲'
    防具精通属性 = ['智力']

    主BUFF = 1.65

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)


class 极诣·暗殿骑士(角色窗口):

    def 窗口属性输入(self):
        self.初始属性 = 极诣·暗殿骑士角色属性()
        self.角色属性A = 极诣·暗殿骑士角色属性()
        self.角色属性B = 极诣·暗殿骑士角色属性()
        self.一觉序号 = 极诣·暗殿骑士一觉序号
        self.二觉序号 = 极诣·暗殿骑士二觉序号
        self.三觉序号 = 极诣·暗殿骑士三觉序号
        self.护石选项 = deepcopy(极诣·暗殿骑士护石选项)
        self.符文选项 = deepcopy(极诣·暗殿骑士符文选项)
