﻿from PublicReference.base import *

# class 职业主动技能(职业主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '矛':
#             return round(self.CD / self.恢复 * 1.05, 1)

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

class 技能0(被动技能):
    名称 = '鲜血融合'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 物理攻击力倍率进图(self, 武器类型):
        if self.等级<= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 *self.等级 , 5)
    def 加成倍率(self, 武器类型):
        if self.等级<= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 *self.等级 , 5)

class 技能1(被动技能):
    名称 = '血之共鸣'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)

class 技能2(被动技能):
    名称 = '血狱之力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

class 技能3(被动技能):
    名称 = '鲜血之殇'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 技能4(被动技能):
    名称 = '血源之眼'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 技能5(职业主动技能):
    名称 = '血蝠之袭'
    所在等级= 15
    等级上限 =60
    基础等级 =46
    #基础 = 3072.95454545
    #成长 = 347.62237762
    CD = 5
    TP成长 = 0.10
    TP上限 = 5
    data0 = [ int(i*1.0) for i in [0, 228, 251, 275, 297, 321, 344, 367, 390, 414, 436, 460, 483, 506, 529, 553, 575, 599, 622, 645, 668, 692, 715, 738, 761, 785, 807, 831, 854, 877, 900, 924, 946, 970, 993, 1016, 1039, 1063, 1085, 1109, 1132, 1155, 1178, 1202, 1225, 1248, 1271, 1295, 1317, 1341, 1364, 1387, 1410, 1434, 1456, 1480, 1503, 1526, 1549, 1573, 1595, 1619, 1642, 1665, 1688, 1712, 1735, 1758, 1781, 1805, 1827]]
    攻击次数 = 15

class 技能6(职业主动技能):
    名称 = '血翼突击'
    所在等级= 15
    等级上限 =60
    基础等级 =46
    #基础 = 2329.84763635444
    #成长 = 263.1339020924
    data0 = [ int(i*1.0*1.124) for i in [0, 2307, 2541, 2775, 3009, 3244, 3477, 3712, 3945, 4180, 4414, 4648, 4882, 5116, 5350, 5585, 5818, 6053, 6286, 6521, 6755, 6989, 7223, 7457, 7691, 7925, 8159, 8394, 8627, 8862, 9096, 9330, 9565, 9798, 10033, 10266, 10501, 10735, 10969, 11203, 11437, 11671, 11905, 12139, 12374, 12607, 12842, 13075, 13310, 13544, 13778, 14012, 14246, 14480, 14715, 14948, 15183, 15416, 15651, 15885, 16119, 16353, 16587, 16821, 17055, 17289, 17524, 17757, 17992, 18225, 18460]]
    CD = 5
    TP成长 = 0.10
    TP上限 = 5

class 技能7(职业主动技能):
    名称 = '鲜血长枪'
    所在等级= 20
    等级上限 =60
    基础等级 =43
    #基础 = 2993.1012727272
    #成长 = 337.716727272
    data0 = [ int(i*1.0*1.123) for i in [0, 1483, 1633, 1784, 1934, 2085, 2235, 2385, 2535, 2686, 2836, 2987, 3137, 3288, 3438, 3589, 3739, 3890, 4040, 4191, 4341, 4492, 4642, 4793, 4943, 5094, 5244, 5395, 5545, 5695, 5845, 5996, 6146, 6297, 6447, 6598, 6748, 6899, 7049, 7200, 7350, 7501, 7651, 7802, 7952, 8103, 8253, 8404, 8554, 8705, 8855, 9005, 9155, 9306, 9456, 9607, 9757, 9908, 10058, 10209, 10359, 10510, 10660, 10811, 10961, 11112, 11262, 11413, 11563, 11714, 11864]]
    攻击次数 = 2
    CD = 6
    TP成长 = 0.10
    TP上限 = 5

class 技能8(职业主动技能):
    名称 = '血蝠之舞'
    所在等级 =25
    等级上限 =60
    基础等级 =41
    #基础 = 3293.18181818
    #成长 = 372.58741259
    data0 = [ int(i*1.0) for i in [0, 122, 135, 147, 159, 172, 185, 196, 209, 222, 234, 246, 259, 271, 284, 296, 308, 321, 334, 345, 358, 371, 383, 395, 408, 420, 433, 445, 457, 470, 483, 495, 507, 520, 532, 545, 557, 569, 582, 595, 606, 619, 632, 644, 656, 669, 681, 694, 706, 718, 731, 744, 755, 768, 781, 793, 805, 818, 830, 843, 855, 867, 880, 893, 905, 917, 930, 942, 955, 967, 979]]
    攻击次数 = 30
    CD = 6
    TP成长 = 0.10
    TP上限 = 5

class 技能9(职业主动技能):
    名称 = '血腥狩猎'
    所在等级 =25
    等级上限 =60
    基础等级 =41
    #基础 = 4179
    #成长 = 472.5
    data0 = [ int(i*1.05) for i in [0, 886, 976, 1066, 1156, 1246, 1336, 1426, 1516, 1606, 1696, 1786, 1876, 1966, 2056, 2146, 2236, 2326, 2416, 2506, 2596, 2686, 2776, 2866, 2956, 3046, 3136, 3226, 3316, 3406, 3496, 3586, 3676, 3766, 3856, 3946, 4036, 4126, 4216, 4306, 4396, 4486, 4576, 4666, 4756, 4846, 4936, 5026, 5116, 5206, 5296, 5386, 5476, 5566, 5656, 5746, 5836, 5926, 6016, 6106, 6196, 6286, 6376, 6466, 6556, 6646, 6736, 6826, 6916, 7006, 7096]]
    攻击次数 = 5
    CD = 8
    TP成长 = 0.10
    TP上限 = 5


class 技能10(职业主动技能):
    名称 = '狱血之犬'
    所在等级= 30
    等级上限 =60
    基础等级 =38
    #基础 = 4162.87878788
    #成长 = 470.76223776
    #咬住敌人时物理攻击力：<data0>%
    data0 = [ int(i*1.0) for i in [0, 331, 365, 398, 432, 465, 499, 533, 566, 600, 634, 667, 701, 735, 768, 802, 835, 869, 902, 935, 969, 1003, 1036, 1070, 1104, 1137, 1171, 1205, 1238, 1272, 1305, 1339, 1373, 1406, 1440, 1474, 1507, 1541, 1575, 1608, 1642, 1675, 1709, 1743, 1776, 1810, 1844, 1877, 1911, 1945, 1978, 2012, 2045, 2079, 2113, 2145, 2179, 2213, 2246, 2280, 2314, 2347, 2381, 2415, 2448, 2482, 2515, 2549, 2583, 2616, 2650]]
    #撕咬多段攻击物理攻击力：<data1>%
    data1 = [ int(i*1.0) for i in [0, 331, 365, 398, 432, 465, 499, 533, 566, 600, 634, 667, 701, 735, 768, 802, 835, 869, 902, 935, 969, 1003, 1036, 1070, 1104, 1137, 1171, 1205, 1238, 1272, 1305, 1339, 1373, 1406, 1440, 1474, 1507, 1541, 1575, 1608, 1642, 1675, 1709, 1743, 1776, 1810, 1844, 1877, 1911, 1945, 1978, 2012, 2045, 2079, 2113, 2145, 2179, 2213, 2246, 2280, 2314, 2347, 2381, 2415, 2448, 2482, 2515, 2549, 2583, 2616, 2650]]
    攻击次数2 = 13
    CD = 10
    TP成长 = 0.10
    TP上限 = 5

class 技能11(职业主动技能):
    名称 = '狱血之牙'
    所在等级= 30
    等级上限 =60
    基础等级 =38
    #基础 = 5281.5666666
    #成长 = 596.353846154
    data0 = [ int(i*1.1) for i in [0, 5344, 5885, 6428, 6970, 7512, 8055, 8596, 9138, 9681, 10223, 10765, 11307, 11849, 12392, 12934, 13475, 14018, 14560, 15102, 15645, 16186, 16729, 17271, 17813, 18355, 18897, 19439, 19982, 20524, 21065, 21608, 22150, 22693, 23235, 23776, 24319, 24861, 25403, 25945, 26487, 27029, 27572, 28114, 28656, 29198, 29740, 30283, 30825, 31366, 31909, 32451, 32993, 33535, 34077, 34620, 35162, 35704, 36246, 36788, 37330, 37873, 38415, 38956, 39499, 40041, 40584, 41125, 41667, 42210, 42752]]
    CD = 12
    TP成长 = 0.10
    TP上限 = 5
    额外倍率 = 0
    触发概率 = 0
    def 等效百分比(self, 武器类型):
        return (1 + self.额外倍率 * self.触发概率) * super().等效百分比(武器类型)

class 技能12(职业主动技能):
    名称 = '血腥炼狱'
    所在等级= 35
    等级上限 =60
    基础等级 =36
    #基础 = 9392.703939
    #成长 = 1061.7061888
    data0 = [ int(i*1.123) for i in [0, 931, 1025, 1120, 1215, 1309, 1404, 1498, 1593, 1687, 1782, 1876, 1971, 2065, 2160, 2255, 2349, 2444, 2538, 2633, 2727, 2822, 2916, 3011, 3105, 3200, 3295, 3389, 3484, 3578, 3673, 3767, 3861, 3955, 4050, 4145, 4239, 4334, 4428, 4523, 4617, 4712, 4806, 4901, 4995, 5090, 5185, 5279, 5374, 5468, 5563, 5657, 5752, 5846, 5941, 6035, 6130, 6225, 6319, 6414, 6508, 6603, 6697, 6792, 6886, 6981, 7075, 7169, 7264, 7358, 7453]]
    攻击次数 = 10
    CD =18
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2
            # self.基础 *= 1.2
            # self.成长 *= 1.2
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.29
            # self.基础 *= 1.29
            # self.成长 *= 1.29
            self.CD *= 0.9

class 技能13(职业主动技能):
    名称 = '噬魂囚笼'
    所在等级= 40
    等级上限 =60
    基础等级 =33
    #hit数存疑，测试为30，写的31
    #基础 = 12175.36181818/31*30
    #成长 = 1333.46433566/31*30
    data0 = [ int(i*1.123) for i in [0, 389, 429, 468, 508, 547, 587, 626, 666, 705, 745, 785, 825, 864, 904, 943, 983, 1022, 1062, 1101, 1141, 1180, 1220, 1259, 1299, 1338, 1378, 1417, 1457, 1496, 1536, 1575, 1615, 1655, 1695, 1734, 1774, 1813, 1853, 1892, 1932, 1971, 2011, 2050, 2090, 2129, 2169, 2208, 2248, 2287, 2327, 2366, 2406, 2445, 2485, 2525, 2565, 2604, 2644, 2683, 2723, 2762, 2802, 2841, 2881, 2920, 2960, 2999, 3039, 3078, 3118]]
    攻击次数 = 30
    CD =20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2
            # self.基础 *= 1.2
            # self.成长 *= 1.2
            self.CD *= 0.82
        elif x == 1:
            self.倍率 *= 1.29
            # self.基础 *= 1.29
            # self.成长 *= 1.29
            self.CD *= 0.82

class 技能14(职业主动技能):
    名称 = '狱血之噬'
    所在等级= 45
    等级上限 =60
    基础等级 =31
    #基础 = 23208.8198030
    #成长 = 2620.41055594
    #吸血物理攻击力：<data0>%
    data0 = [ int(i*1.123) for i in [0, 23000, 25334, 27667, 30000, 32334, 34667, 37001, 39334, 41667, 44001, 46335, 48667, 51001, 53335, 55668, 58001, 60335, 62668, 65002, 67335, 69668, 72002, 74335, 76668, 79002, 81335, 83669, 86002, 88335, 90669, 93003, 95335, 97669, 100003, 102336, 104669, 107003, 109336, 111670, 114003, 116336, 118670, 121003, 123336, 125670, 128004, 130336, 132670, 135004, 137337, 139670, 142004, 144337, 146671, 149004, 151337, 153671, 156005, 158337, 160671, 163005, 165338, 167671, 170005, 172338, 174672, 177005, 179338, 181672, 184005]]
    CD =40
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2
            # self.基础 *= 1.2
            # self.成长 *= 1.2
        elif x == 1:
            self.倍率 *= 1.28
            # self.基础 *= 1.28
            # self.成长 *= 1.28

class 技能15(职业主动技能):
    名称 = '伯爵之歌'
    所在等级= 50
    等级上限 =60
    基础等级 =12
    # 基础 = 46649
    # 成长 = 14081
    #多段物理攻击力：<data0>%
    data0 = [ int(i*1.0) for i in [0, 3036, 3740, 4445, 5148, 5853, 6556, 7261, 7965, 8668, 9373, 10076, 10781, 11485, 12189, 12893, 13597, 14301, 15005, 15709, 16414, 17117, 17822, 18525, 19230, 19934, 20638, 21342, 22046, 22750, 23455, 24158, 24863, 25566, 26271, 26975, 27679, 28383, 29087, 29791, 30495, 105760, 107882, 110002, 112124, 114245, 116367, 118488, 120609, 122731, 124852, 126973, 129094, 131216, 133337, 135458, 137579, 139701, 141822, 143943, 146064, 148186, 150307, 152428, 154550, 156671, 158793, 160913, 163035, 165156, 167278]]
    攻击次数 = 14
    #最终一击物理攻击力：<data1>%
    data1 = [ int(i*1.0) for i in [0, 18218, 22443, 26667, 30892, 35116, 39341, 43565, 47790, 52014, 56238, 60463, 64687, 68912, 73136, 77361, 81585, 85810, 90035, 94259, 98484, 102708, 106933, 111157, 115382, 119606, 123831, 128055, 132280, 136505, 140729, 144954, 149178, 153403, 157627, 161852, 166076, 170301, 174525, 178750, 182975, 105760, 107882, 110002, 112124, 114245, 116367, 118488, 120609, 122731, 124852, 126973, 129094, 131216, 133337, 135458, 137579, 139701, 141822, 143943, 146064, 148186, 150307, 152428, 154550, 156671, 158793, 160913, 163035, 165156, 167278]]
    攻击次数2 = 1
    CD = 145

class 技能16(职业主动技能):
    名称 = '魔仆召唤：狱犬'
    所在等级= 60
    等级上限 =40
    基础等级 =23
    #基础 = 18037.9022727225
    #成长 = 2037.774650352
    #多段物理攻击力：<data0>%
    data0 = [ int(i*1.05) for i in [0, 911, 1003, 1095, 1187, 1280, 1373, 1465, 1557, 1650, 1742, 1835, 1927, 2019, 2112, 2205, 2296, 2389, 2482, 2574, 2666, 2759, 2851, 2944, 3036, 3128, 3221, 3313, 3405, 3498, 3590, 3683, 3775, 3867, 3960, 4053, 4145, 4237, 4330, 4422, 4515]]
    攻击次数 = 21
    CD =25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.13
            # self.基础 *= 1.13
            # self.成长 *= 1.13
            self.CD *= 0.8
        elif x == 1:
            self.倍率 *= 1.22
            # self.基础 *= 1.22
            # self.成长 *= 1.22
            self.CD *= 0.8

class 技能17(职业主动技能):
    名称 = '血翼绽放'
    所在等级= 70
    等级上限 =40
    基础等级 =18
    #基础 = 25260.95
    #成长 = 2852.003846153
    #蝙蝠群冲击波攻击力：<data0>%
    data0 = [ int(i*1.1) for i in [0, 10223, 11260, 12297, 13334, 14371, 15408, 16445, 17483, 18520, 19556, 20594, 21631, 22668, 23705, 24743, 25780, 26816, 27854, 28891, 29928, 30965, 32003, 33039, 34076, 35114, 36151, 37188, 38225, 39262, 40299, 41336, 42374, 43411, 44448, 45485, 46522, 47559, 48596, 49634, 50671]]
    #血气之翼物理攻击力：<data1>%
    data1 = [ int(i*1.1) for i in [0, 15335, 16890, 18445, 20001, 21557, 23113, 24668, 26224, 27780, 29335, 30891, 32446, 34003, 35558, 37114, 38670, 40225, 41781, 43336, 44893, 46448, 48004, 49559, 51115, 52671, 54226, 55782, 57338, 58894, 60449, 62005, 63561, 65116, 66672, 68227, 69784, 71339, 72895, 74450, 76006]]
    攻击次数2 = 1
    CD =50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.25
            # self.基础 *= 1.25
            # self.成长 *= 1.25
        elif x == 1:
            self.倍率 *= 1.33
            # self.基础 *= 1.33
            # self.成长 *= 1.33

class 技能18(职业主动技能):
    名称 = '地狱冥犬'
    所在等级= 75
    等级上限 =40
    基础等级 =16
    #基础 = 30218.85
    #成长 = 5734.946153849
    #撕咬攻击力：<data0>%
    data0 = [ int(i*1.1) for i in [0, 817, 947, 1078, 1208, 1337, 1469, 1599, 1729, 1860, 1990, 2120, 2251, 2381, 2510, 2642, 2772, 2902, 3033, 3162, 3294, 3424, 3554, 3685, 3815, 3945, 4075, 4205, 4335, 4467, 4596, 4726, 4857, 4987, 5117, 5248, 5378, 5508, 5640, 5769, 5899]]
    攻击次数 = 20
    #冲向地面攻击力：<data1>%
    data1 = [ int(i*1.1) for i in [0, 16349, 18955, 21562, 24169, 26775, 29382, 31989, 34595, 37202, 39808, 42414, 45020, 47627, 50234, 52840, 55447, 58054, 60660, 63267, 65874, 68479, 71085, 73692, 76298, 78905, 81512, 84118, 86725, 89332, 91938, 94545, 97151, 99756, 102364, 104970, 107576, 110184, 112790, 115396, 118004]]
    攻击次数2 = 1
    CD =30
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.29
            # self.基础 *= 1.29
            # self.成长 *= 1.29
            self.CD *= 0.9

class 技能19(职业主动技能):
    名称 = '死亡之握'
    所在等级= 80
    等级上限 =40
    基础等级 =13
    #基础 = 60756.9115151488
    #成长 = 6859.7572027936
    data0 = [ int(i*1.12) for i in [0, 60372, 66497, 72622, 78746, 84871, 90996, 97121, 103245, 109370, 115495, 121620, 127745, 133869, 139994, 146119, 152244, 158368, 164493, 170618, 176743, 182867, 188992, 195116, 201242, 207366, 213491, 219615, 225741, 231865, 237990, 244115, 250240, 256365, 262489, 268614, 274738, 280864, 286988, 293113, 299237]]
    CD =50
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.34
            # self.基础 *= 1.34
            # self.成长 *= 1.34

class 技能20(职业主动技能):
    名称 = '血界彼岸'
    所在等级= 85
    等级上限 =40
    基础等级 =5
    #基础 = 108898.72
    #成长 = 32796.96
    #多段攻击力：<data0>%
    data0 = [ int(i*1.12) for i in [0, 1832, 2256, 2681, 3106, 3531, 3955, 4380, 4805, 5230, 5655, 6080, 6505, 6929, 7354, 7779, 8204, 8628, 9054, 9478, 9903, 10327, 10753, 11177, 11602, 12027, 12452, 12876, 13301, 13726, 14151, 14575, 15001, 15425, 15850, 16275, 16700, 17125, 17549, 17975, 18399]]
    攻击次数 = 35
    #最终一击攻击力：<data1>%
    data1 = [ int(i*1.12) for i in [0, 62287, 76730, 91174, 105617, 120061, 134504, 148947, 163391, 177835, 192278, 206721, 221165, 235608, 250052, 264495, 278938, 293382, 307825, 322269, 336712, 351155, 365599, 380043, 394485, 408929, 423373, 437816, 452260, 466703, 481146, 495590, 510034, 524477, 538920, 553364, 567807, 582251, 596694, 611137, 625581]]
    攻击次数2 = 1
    CD = 180

class 技能21(主动技能):
    名称 = '血翼蔽空'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 104283.2
    成长 = 11773.8
    CD = 60.0

class 技能22(主动技能):
    名称 = '血域帷幕·陨灭'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 31035.0050128261
    成长 = 9368.99498717389
    攻击次数 = 1
    基础2 = 3103.1256775528
    成长2 = 936.8743224472
    攻击次数2 = 20
    基础3 = 217248.082151946
    成长3 = 65583.9178480538
    攻击次数3 = 1
    CD = 290.0

    def 加成倍率(self, 武器类型):
        return 0.0

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

知源·血法师一觉序号 = 0
知源·血法师二觉序号 = 0
知源·血法师三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        知源·血法师一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        知源·血法师二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        知源·血法师三觉序号 = 技能序号[i.名称]

知源·血法师护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        知源·血法师护石选项.append(i.名称)

知源·血法师符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        知源·血法师符文选项.append(i.名称)

class 知源·血法师角色属性(角色属性):

    实际名称 = '知源·血法师'
    角色 = '魔法师(男)'
    职业 = '血法师'

    武器选项 = ['矛']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    狱血之牙触发概率 = 0

    主BUFF = 1.97

    def 被动倍率计算(self):
        if 装备列表[装备序号[self.装备栏[11]]].名称 == '歼灵灭魂矛':
            self.技能栏[self.技能序号['狱血之牙']].触发概率 = self.狱血之牙触发概率
        super().被动倍率计算()

    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(技能列表)
        self.技能序号= deepcopy(技能序号)

class 知源·血法师(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 知源·血法师角色属性()
        self.角色属性A = 知源·血法师角色属性()
        self.角色属性B = 知源·血法师角色属性()
        self.一觉序号 = 知源·血法师一觉序号
        self.二觉序号 = 知源·血法师二觉序号
        self.三觉序号 = 知源·血法师三觉序号
        self.护石选项 = deepcopy(知源·血法师护石选项)
        self.符文选项 = deepcopy(知源·血法师符文选项)

    def 界面(self):
        super().界面()
        self.狱血之牙概率=MyQComboBox(self.main_frame2)
        self.狱血之牙概率.resize(130,20)
        self.狱血之牙概率.move(320,450)
        for i in range(11):
            self.狱血之牙概率.addItem('歼灵灭魂矛：' + str(i * 10) + '%')
        self.狱血之牙概率.setCurrentIndex(1)

    def 载入配置(self, path='set'):
        super().载入配置(path)
        try:
           setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'r',encoding='utf-8').readlines()
           self.狱血之牙概率.setCurrentIndex(int(setfile[0].replace('\n', '')))
        except:
            pass

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'w', encoding='utf-8')
            setfile.write(str(self.狱血之牙概率.currentIndex())+'\n')

        except:
            pass

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        属性.狱血之牙触发概率 = round(self.狱血之牙概率.currentIndex() / 10, 2)
