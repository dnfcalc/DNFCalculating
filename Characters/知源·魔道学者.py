﻿from math import *
from PublicReference.carry.base import *


class 技能0(主动技能):
    名称 = '变异苍蝇拍'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [int(i*75606/11.83/5722*1.085) for i in  [0, 5722, 6301, 6884, 7464, 8045, 8625, 9206, 9785, 10367, 10947, 11529, 12109, 12690, 13270, 13852, 14431, 15010, 15591, 16173, 16754, 17333, 17915, 18495, 19076, 19656, 20238, 20818, 21400, 21978, 22559, 23140, 23721, 24301, 24883, 25463, 26043, 26623, 27204, 27784, 28364, 28947, 29526, 30107, 30688, 31268, 31848, 32430, 33011, 33591, 34172, 34753, 35332, 35912, 36493, 37073, 37655, 38235, 38816, 39396, 39978, 40557, 41139, 41720, 42301, 42880, 43461, 44041, 44622, 45202, 45784]]
    CD = 6.4
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 0.1

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能1(被动技能):
    名称 = '亲和法米利尔'
    所在等级 = 15
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 5)


class 技能2(主动技能):
    名称 = '改良舒露露'
    备注 = '大成功'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # 大成功
    data0 = [int(i*17949/2.51/6419*1.085) for i in  [0, 6419, 7070, 7721, 8373, 9023, 9675, 10326, 10977, 11630, 12281, 12931, 13583, 14234, 14886, 15536, 16187, 16839, 17490, 18142, 18793, 19444, 20095, 20746, 21397, 22048, 22699, 23352, 24003, 24654, 25306, 25957, 26609, 27259, 27909, 28561,29212, 29864, 30515, 31166, 31819, 32470, 33122, 33773, 34421, 35074, 35725, 36376, 37028, 37679, 38331, 38982, 39633, 40286, 40937, 41586, 42237, 42888, 43541, 44192, 44843, 45495, 46146, 46798, 47449, 48099, 48750, 49401, 50053, 50704, 51355]]
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能3(主动技能):
    名称 = '熔岩药瓶失败'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 26
    data0 = [int(i*94167/11.83/6927*1.085) for i in  [0, 6927, 8031, 9137, 10242, 11346, 12451, 13555, 14659, 15764, 16868, 17973, 19078, 20182, 21289, 22393, 23496, 24601, 25705, 26810, 27915, 29020, 30126, 31230, 32332, 33436, 34541, 35648, 36752, 37857, 38961, 40064, 41169, 42274, 43379, 44484,45589, 46694, 47798, 48902, 50006, 51111, 52216, 53320, 54425, 55530, 56635, 57738, 58843, 59948, 61053, 62157, 63262, 64366, 65471, 66575, 67679, 68784, 69889, 70994, 72099, 73203, 74308, 75411, 76516, 77621, 78725, 79830, 80934, 82040, 83143]]
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能24(主动技能):
    名称 = '熔岩药瓶成功'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 26
    data1 = [int(i*24417/11.83/1884*1.085) for i in  [0, 1884, 2187, 2488, 2785, 3083, 3383, 3687, 3988, 4290, 4590, 4889, 5191, 5492, 5792, 6094, 6393, 6691, 6992, 7294, 7594, 7895, 8198, 8498, 8798, 9101, 9399, 9698, 9998, 10301, 10601, 10902, 11204, 11502, 11803, 12106, 12406, 12704, 13002, 13307, 13605, 13906, 14208, 14508, 14809, 15112, 15412, 15715, 16008, 16311, 16612, 16912, 17215, 17515, 17813, 18116, 18416, 18718, 19020, 19317, 19616, 19916, 20218, 20520, 20823, 21123, 21422, 21725, 22026, 22324, 22623]]
    攻击次数2 = 6
    data2 = [int(i*1.0*1218/11.83/103*1.085) for i in  [0, 103, 120, 135, 152, 169, 184, 201, 218, 234, 250, 267, 284, 300, 316, 333, 349, 364, 382, 398, 415, 430, 446, 464, 481, 497, 512, 529, 546, 561, 578, 594, 611, 627, 644, 660, 677, 693, 709, 726, 742, 758, 775, 792, 807, 824, 841, 857, 873, 890, 906, 922, 939, 955, 972, 988, 1005, 1021, 1038, 1054, 1070, 1087, 1104, 1119, 1136, 1153, 1169, 1185, 1202, 1218, 1233]]
    攻击次数3 = 10

    # 灼烧
    data3 = [int(i*1.0*1.085) for i in  [0, 12, 14, 16, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 73, 75, 77, 79, 81,
           83, 85, 87, 89, 91, 93, 95, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 144]]
    攻击次数4 = 10
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3 + self.data3[self.等级] * self.攻击次数4) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能4(主动技能):
    名称 = '魔道酸雨云'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 26
    data1 = [int(i*2591/11.83/194*1.085) for i in [0, 194, 224, 254, 286, 316, 346, 377, 408, 438, 469, 501, 531, 562, 593, 625, 655, 686, 717, 747, 777, 807, 840, 869, 900, 931, 964, 992, 1024, 1054, 1085, 1116, 1148, 1178, 1209, 1239, 1270, 1299, 1331, 1363, 1393, 1423, 1455, 1487, 1517, 1547, 1579, 1608, 1639, 1671, 1700, 1732, 1762, 1792, 1822, 1854, 1886, 1917, 1946, 1978, 2010, 2040, 2070, 2102, 2131, 2162, 2192, 2225, 2253, 2286, 2315]]
    攻击次数2 = 36
    # 大成功闪电部分未加强
    data2 = [int(i*11759/11.83/994*1.085) for i in [0, 994, 1153, 1310, 1471, 1631, 1787, 1947, 2105, 2263, 2423, 2579, 2740, 2900, 3058, 3217, 3375, 3534, 3692, 3851, 4009, 4166, 4325, 4486, 4646, 4801, 4962, 5121, 5278, 5439, 5595, 5756, 5915, 6073, 6232, 6389, 6547, 6708, 6867, 7024, 7182, 7341, 7503, 7661, 7817, 7977, 8134, 8293, 8451, 8610, 8769, 8931, 9089, 9246, 9405, 9566, 9724, 9881, 10040, 10197, 10355, 10518, 10676, 10835, 10992, 11150, 11311, 11467, 11624, 11785, 11946]]
    攻击次数3 = 6
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能5(主动技能):
    名称 = '电鳗碰撞机'
    备注 = '大成功'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data1 = [int(i*1.0*1.085) for i in [0, 870, 959, 1048, 1136, 1226, 1314, 1402, 1490, 1578, 1666, 1756, 1844, 1933, 2020, 2109, 2196, 2287, 2374, 2463, 2552, 2640, 2728, 2815, 2906, 2994, 3082, 3170, 3259, 3346, 3436, 3524, 3613, 3700, 3790, 3878, 3966, 4055, 4144, 4232, 4319, 4409, 4496, 4586, 4673, 4763, 4850, 4939, 5027, 5116, 5204, 5293, 5382, 5470, 5558, 5646, 5736, 5823, 5912, 6000, 6089, 6176, 6266, 6354, 6443, 6531, 6620, 6708, 6795, 6886, 6974]]
    攻击次数2 = 14
    data2 = [int(i*1.0*1.085) for i in [0, 1370, 1509, 1648, 1787, 1928, 2067, 2205, 2345, 2484, 2623, 2762, 2901, 3040, 3179, 3318, 3457, 3596, 3736, 3874, 4013, 4153, 4292, 4430, 4569, 4709, 4849, 4988, 5127, 5266, 5405, 5545, 5683, 5822, 5961, 6099, 6238, 6378, 6518, 6657, 6795, 6935, 7074, 7213, 7352, 7491, 7630, 7770, 7910, 8047, 8186, 8326, 8464, 8603, 8743, 8882, 9020, 9160, 9300, 9439, 9578, 9717, 9856, 9995, 10135, 10273, 10412, 10552, 10691, 10831, 10971]]
    攻击次数3 = 1
    # 感电
    data3 = [int(i*1.0*1.085) for i in [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15, 16, 16, 16, 17,
           17, 18, 18, 18, 19, 19, 20, 20, 20, 21, 21, 22, 22, 22, 23, 23, 24, 24, 25, 25, 25, 26, 26, 27, 27, 27, 28, 28, 29, 29, 29, 30, 30, 31, 31, 31]]
    攻击次数4 = 5
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4.8

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3 + self.data3[self.等级] * self.攻击次数4) * (1 + self.TP成长 * self.TP等级) * self.倍率
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27

        elif x == 1:
            self.倍率 *= 1.36


class 技能6(主动技能):
    名称 = '反重力装置'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    # 大成功
    data0 = [int(i*161550/11.83/12258*1.085) for i in [0, 12258, 13502, 14745, 15989, 17233, 18475, 19719, 20963, 22207, 23451, 24694, 25937, 27181, 28424, 29668, 30912, 32155, 33399, 34642, 35886, 37130, 38373, 39617, 40861, 42105, 43347, 44591, 45834, 47078, 48322, 49566, 50810, 52052, 53296, 54540, 55784, 57027, 58271, 59515, 60757, 62001, 63245, 64489, 65733, 66977, 68221, 69463, 70707, 71950, 73194, 74438, 75681, 76925, 78168, 79412, 80656, 81900, 83143, 84387, 85631, 86873, 88117, 89360, 90604, 91848, 93092, 94336, 95579, 96822, 98066]]
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.1

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能7(主动技能):
    名称 = '暴炎加热炉失败'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data0 = [int(i*11948/11.83/918*1.085) for i in [0, 918, 1010, 1105, 1198, 1291, 1384, 1478, 1571, 1665, 1758, 1851, 1943, 2036, 2130, 2222, 2316, 2409, 2504, 2596, 2689, 2782, 2875, 2969, 3062, 3156, 3248, 3342, 3435, 3528, 3622, 3715, 3807, 3900, 3994, 4087, 4179, 4273, 4366, 4461, 4553, 4647, 4739, 4833, 4927, 5020, 5113, 5205, 5299, 5393, 5487, 5579, 5673, 5764, 5858, 5951, 6044, 6138, 6230, 6325, 6418, 6511, 6604, 6696, 6790, 6884, 6977, 7070, 7164, 7256, 7351]]
    攻击次数 = 13
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 2.0

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2768

        elif x == 1:
            self.倍率 *= 1.3655


class 技能8(主动技能):
    名称 = '冰霜钻孔车失败'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data1 = [int(i*1.0*1.085) for i in [0, 922, 1016, 1109, 1203, 1297, 1391, 1483, 1577, 1672, 1765, 1858, 1952, 2046, 2140, 2233, 2327, 2421, 2514, 2608, 2702, 2795, 2889, 2983, 3076, 3170, 3264, 3358, 3451, 3544, 3639, 3733, 3825, 3919, 4013, 4106, 4199, 4293, 4387, 4481, 4573, 4668, 4762, 4855, 4948, 5042, 5137, 5230, 5323, 5417, 5511, 5604, 5699, 5792, 5885, 5979, 6073, 6167, 6260, 6354, 6448, 6541, 6635, 6729, 6823, 6915, 7009, 7103, 7198, 7289, 7383]]
    攻击次数2 = 9
    data2 = [int(i*1.0*1.085) for i in [0, 8306, 9150, 9992, 10836, 11677, 12521, 13363, 14207, 15050, 15891, 16735, 17578, 18420, 19263, 20107, 20947, 21791, 22634, 23477, 24320, 25162, 26005, 26848, 27691, 28533, 29377, 30219, 31061, 31904, 32748, 33591, 34433, 35276, 36118, 36961, 37804, 38647, 39489, 40332, 41175, 42018, 42862, 43704, 44546, 45389, 46233, 47074, 47918, 48762, 49602, 50445, 51289, 52132, 52974, 53817, 54659, 55503, 56345, 57188, 58032, 58874, 59715, 60559, 61403, 62244, 63087, 63930, 64773, 65615, 66459]]
    攻击次数3 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 2.0

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24

        elif x == 1:
            self.倍率 *= 1.32


class 技能9(主动技能):
    名称 = '超级苍蝇拍'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data0 = [int(i*1.0*1.085) for i in [0, 27391, 30171, 32948, 35726, 38504, 41284, 44063, 46842, 49621, 52400, 55178, 57958, 60737, 63516, 66294, 69074, 71852, 74631, 77411, 80190, 82968, 85748, 88525, 91304, 94082, 96862, 99640, 102419, 105199, 107978, 110756, 113535, 116314, 119093, 121872, 124652, 127430, 130209, 132988, 135767, 138546, 141322, 144100, 146880, 149658, 152438, 155217, 157996, 160774, 163554, 166332, 169111, 171890, 174669, 177448, 180226, 183007, 185785, 188564, 191343, 194122, 196899, 199678, 202458, 205236, 208015, 210794, 213574, 216352, 219130]]
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.1

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.15
            self.CD *= 0.9

        elif x == 1:
            self.倍率 *= 1.24
            self.CD *= 0.9


class 技能10(被动技能):
    名称 = '成功预感'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1 + round(16 + 1.5 * (self.等级 - 16), 1) / 100


class 技能11(主动技能):
    名称 = '技艺融合'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    data1 = [int(i*1.13*1.085) for i in [0, 1704, 2100, 2496, 2893, 3287, 3684, 4079, 4475, 4870, 5266, 5660, 6058, 6452, 6849, 7243, 7639, 8033, 8430, 8825, 9221, 9617, 10012, 10408, 10804, 11198, 11595, 11991, 12384, 12782, 13177, 13571, 13966, 14364, 14757, 15154, 15550, 15944, 16341, 16737, 17131, 17528, 17923, 18320, 18715, 19111, 19504, 19902, 20296, 20691, 21088, 21483, 21878, 22275, 22670, 23065, 23461, 23857, 24251, 24648, 25042, 25438, 25836, 26229, 26626, 27021, 27417, 27811, 28208, 28603, 28999]]
    攻击次数2 = 22
    data2 = [int(i*1.13*1.085) for i in [0, 46315, 57054, 67795, 78534, 89273, 100014, 110754, 121494, 132233, 142972, 153713, 164453, 175191, 185933, 196672, 207412, 218151, 228891, 239631, 250370, 261112, 271851, 282590, 293331, 304069, 314810, 325549, 336288, 347031, 357770, 368509, 379248, 389988, 400728, 411467, 422209, 432948, 443687, 454427, 465167, 475906, 486646, 497387, 508127, 518866, 529605, 540344, 551086, 561825, 572566, 583305, 594044, 604785, 615525, 626264, 637003, 647743, 658485, 669224, 679964, 690702, 701442, 712182, 722921, 733664, 744403, 755141, 765881, 776621, 787361]]
    攻击次数3 = 1
    CD = 145.0

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3 * 1.1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能12(主动技能):
    名称 = '光电兔'
    备注 = '大成功'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data1 = [int(i*124475/11.83/9439*1.085) for i in [0, 9439, 10397, 11355, 12312, 13270, 14227, 15186, 16142, 17100, 18058, 19016, 19974, 20931, 21889, 22847, 23805, 24762, 25719, 26677, 27635, 28593, 29550, 30507, 31466, 32423, 33381, 34338, 35296, 36254, 37212, 38169, 39126, 40085, 41042, 42001, 42957, 43914, 44873, 45830, 46788, 47745, 48704, 49661, 50620, 51576, 52534, 53492, 54449, 55407, 56364, 57323, 58280, 59239, 60195, 61153, 62111, 63068, 64025, 64983, 65941, 66899, 67857, 68814, 69772, 70730, 71688, 72644, 73602, 74560, 75518]]
    攻击次数2 = 4
    data2 = [int(i*81071/11.83/5524*1.085) for i in [0, 5524, 6085, 6645, 7205, 7766, 8327, 8887, 9447, 10008, 10568, 11128, 11689, 12250, 12810, 13370, 13931, 14491, 15051, 15612, 16173, 16733, 17293, 17854, 18414, 18975, 19535, 20097, 20656, 21216, 21778, 22338, 22899, 23458, 24020, 24580, 25140, 25701, 26261, 26822, 27383, 27943, 28503, 29063, 29624, 30184, 30745, 31306, 31866, 32426, 32986, 33547, 34107, 34668, 35229, 35789, 36349, 36909, 37470, 38030, 38591, 39153, 39712, 40272, 40832, 41394, 41954, 42514, 43076, 43636, 44196]]
    攻击次数3 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 4
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.15

        elif x == 1:
            self.倍率 *= 1.23


class 技能13(主动技能):
    名称 = '雪人刨冰'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16

    data1 = [int(i*1.131*1.085) for i in [0, 2102, 2314, 2527, 2740, 2954, 3168, 3381, 3594, 3806, 4021, 4234, 4446, 4660, 4874, 5086, 5301, 5513, 5728, 5938, 6153, 6368, 6579, 6796, 7007, 7220, 7435, 7647, 7861, 8074, 8287, 8500, 8714, 8928, 9140, 9354, 9566, 9779, 9994, 10207, 10419, 10633, 10846, 11060, 11272, 11486, 11699, 11912, 12125, 12339, 12553]]
    攻击次数2 = 18

    data2 = [int(i*1.131*1.085) for i in [0, 1295, 1427, 1560, 1690, 1822, 1952, 2083, 2218, 2349, 2480, 2610, 2742, 2873, 3006, 3137, 3269, 3399, 3531, 3662, 3796, 3927, 4058, 4189, 4320, 4453, 4584, 4716, 4847, 4980, 5111, 5243, 5374, 5504, 5637, 5767, 5899, 6030, 6163, 6295, 6426, 6556, 6688, 6818, 6952, 7084, 7214, 7345, 7476, 7608, 7739]]
    攻击次数3 = 13

    data3 = [int(i*1.131*1.085) for i in [0, 17828, 19634, 21443, 23252, 25059, 26869, 28677, 30486, 32294, 34103, 35911, 37719, 39526, 41336, 43143, 44954, 46762, 48572, 50379, 52187, 53998, 55805, 57613, 59424, 61229, 63038, 64848, 66656, 68464, 70273, 72080, 73889, 75697, 77507, 79313, 81123, 82932, 84740, 86548, 88358, 90165, 91975, 93783, 95591, 97402, 99210, 101017, 102826, 104633, 106443]]
    攻击次数4 = 1

    CD = 40.0
    演出时间 = 4

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3 + self.data3[self.等级] * self.攻击次数4) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.3


class 技能14(被动技能):
    名称 = '贤者之石'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['魔道酸雨云', '电鳗碰撞机', '反重力装置', '熔岩药瓶成功']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能15(被动技能):
    名称 = '魔道学助手'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['变异苍蝇拍', '超级苍蝇拍', '改良舒露露', '技艺融合', '超级棒棒糖',
            '光电兔', '雪人刨冰', '乌洛波洛斯之环', '糖果大作战精怪乐园', '糖果大作战捣蛋杰克']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)


class 技能16(被动技能):
    名称 = '魔道学助手+苦涩棒棒糖'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['冰霜钻孔车失败', '暴炎加热炉失败', '熔岩药瓶失败']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.88 + 0.02 * self.等级, 5)


class 技能17(主动技能):
    名称 = '超级棒棒糖'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    data1 = [int(i*1.141*1.085) for i in [0, 51736, 56983, 62233, 67479, 72729, 77977, 83227, 88475, 93725, 98971, 104221, 109469, 114718, 119966, 125215, 130462, 135715, 140960, 146210, 151458, 156707, 161954, 167204, 172452, 177701, 182950, 188198, 193446, 198695, 203942, 209192, 214440, 219690, 224939, 230188, 235433, 240683, 245931, 251181, 256430, 261679, 266925, 272174, 277422, 282673, 287920, 293169, 298418, 303666, 308916, 314163, 319413, 324660, 329909, 335157, 340408, 345655, 350905, 356151, 361399, 366649, 371898, 377147, 382396, 387643, 392891, 398141, 403389, 408637, 413887]]
    攻击次数2 = 1
    data2 = [int(i*1.141*1.085) for i in [0, 33077, 36433, 39788, 43144, 46499, 49856, 53211, 56565, 59921, 63277, 66632, 69989, 73342, 76700, 80053, 83410, 86765, 90121, 93480, 96834, 100190, 103546, 106902, 110255, 113614, 116967, 120323, 123678, 127034, 130388, 133745, 137099, 140457, 143810, 147167, 150523, 153878, 157235, 160590, 163948, 167301, 170658, 174014, 177369, 180724, 184081, 187436, 190792, 194147, 197503, 200858, 204213, 207570, 210925, 214279, 217636, 220992, 224348, 227704, 231058, 234416, 237770, 241128, 244482, 247839, 251193, 254549, 257905, 261262, 264615]]
    攻击次数3 = 1
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.32
        self.CD *= 0.9

    CD = 45.0
    演出时间 = 0.5


class 技能18(主动技能):
    名称 = '乌洛波洛斯之环'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    data1 = [int(i*1.14*1.085) for i in [0, 2868, 3533, 4198, 4864, 5529, 6194, 6861, 7525, 8190, 8855, 9521, 10186, 10851, 11515, 12182, 12846, 13510, 14178, 14842, 15508, 16173, 16838, 17503, 18168, 18833, 19499, 20164, 20829, 21496, 22160, 22825, 23490, 24156, 24821, 25485, 26152, 26817, 27482, 28146, 28813, 29478, 30143, 30807, 31474, 32138, 32803, 33468, 34133, 34799, 35463, 36130, 36796, 37460, 38127, 38791, 39455, 40121, 40785, 41452, 42117, 42780, 43449, 44113, 44778, 45443, 46106, 46774, 47438, 48103, 48769]]
    攻击次数2 = 21
    data2 = [int(i*1.14*1.085) for i in [0, 2332, 2872, 3412, 3954, 4493, 5033, 5575, 6115, 6655, 7197, 7736, 8276, 8818, 9360, 9900, 10440, 10982, 11522, 12061, 12603, 13144, 13683, 14224, 14766, 15307, 15847, 16387, 16929, 17468, 18009, 18550, 19089, 19630, 20172, 20713, 21253, 21794, 22334, 22875, 23415, 23956, 24498, 25037, 25576, 26118, 26659, 27200, 27741, 28282, 28822, 29362, 29903, 30443, 30984, 31526, 32065, 32604, 33146, 33688, 34228, 34769, 35310, 35851, 36389, 36930, 37472, 38012, 38552, 39093, 39636]]
    攻击次数3 = 20
    data3 = [int(i*1.14*1.085) for i in [0, 72646, 89494, 106340, 123187, 140032, 156877, 173722, 190569, 207415, 224262, 241107, 257953, 274800, 291646, 308492, 325338, 342185, 359029, 375876, 392721, 409568, 426412, 443259, 460105, 476951, 493797, 510644, 527490, 544335, 561180, 578027, 594872, 611719, 628565, 645411, 662256, 679103, 695949, 712796, 729641, 746487, 763333, 780179, 797024, 813871, 830716, 847563, 864409, 881255, 898100, 914947, 931793, 948637, 965483, 982331, 999177, 1016022, 1032868, 1049714, 1066560, 1083406, 1100254, 1117099, 1133944, 1150790, 1167637, 1184483, 1201328, 1218174, 1235021]]
    攻击次数4 = 1

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数2 + self.data2[self.等级] * self.攻击次数3+self.data3[self.等级] * self.攻击次数4) * self.倍率

    CD = 180.0


class 技能19(主动技能):
    名称 = '魔法秀'
    所在等级 = 20
    等级上限 = 15
    基础等级 = 10
    是否有伤害 = 0
    冷却关联技能 = ['改良舒露露', '熔岩药瓶失败', '魔道酸雨云', '电鳗碰撞机', '暴炎加热炉失败',
              '冰霜钻孔车失败', '反重力装置', '熔岩药瓶成功', '光电兔', '雪人刨冰', '糖果大作战捣蛋杰克']

    魔法秀数值 = [0, 22, 43, 65, 86, 108, 130, 151, 173, 194, 216,
             238, 259, 281, 302, 324, 346, 367, 389, 410, 432]

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.001*self.魔法秀数值[self.等级], 3)


class 技能20(被动技能):
    名称 = '粉红糖果'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能21(主动技能):
    名称 = '糖果大作战捣蛋杰克'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    data0 = [int(i*1.131*1.085) for i in [0, 5463, 6017, 6571, 7125, 7680, 8233, 8788, 9342, 9897, 10450, 11005, 11559, 12113, 12667, 13222, 13776, 14330, 14885, 15439, 15993, 16547, 17102, 17655, 18210, 18764, 19319, 19872, 20427, 20981, 21535, 22089, 22644, 23198, 23752, 24306, 24861, 25414, 25969, 26524, 27078, 27632, 28186, 28741, 29294, 29849, 30403, 30958, 31511, 32066, 32620]]
    攻击次数 = 25
    # 基础 = 4909
    # 成长 = 554
    CD = 60.0

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * self.倍率


class 技能22(主动技能):
    名称 = '糖果大作战精怪乐园'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 = [int(i*1.141*1.085) for i in [0, 12317, 15173, 18029, 20886, 23742, 26597, 29454, 32310, 35167, 38022, 40879, 43735, 46591, 49447, 52303, 55160, 58016, 60872, 63728, 66584, 69441, 72296, 75153, 78009, 80865, 83721, 86577, 89434, 92290, 95146, 98002, 100858, 103715, 106570, 109427, 112283, 115140, 117995, 120851, 123708, 126564, 129421, 132276, 135132, 137989, 140845, 143701, 146557, 149414, 152270]]
    攻击次数 = 8
    # 基础 = 9461
    # 成长 = 2856
    # 攻击次数 = 8
    data2 = [int(i*1.141*1.085) for i in [0, 73904, 91040, 108178, 125314, 142452, 159588, 176726, 193862, 211000, 228136, 245274, 262411, 279548, 296686, 313822, 330960, 348096, 365234, 382370, 399508, 416644, 433782, 450918, 468056, 485193, 502330, 519468, 536604, 553742, 570878, 588016, 605152, 622290, 639426, 656564, 673700, 690838, 707975, 725112, 742249, 759386, 776524, 793660, 810798, 827934, 845072, 862208, 879346, 896482, 913620]]
    # 基础2 = 56768
    # 成长2 = 17136
    攻击次数3 = 1
    data3 = [int(i*1.141*1.085) for i in [0, 80062, 98627, 117192, 135757, 154323, 172888, 191453, 210018, 228583, 247148, 265713, 284278, 302844, 321409, 339974, 358539, 377105, 395670, 414234, 432800, 451365, 469930, 488495, 507061, 525626, 544191, 562756, 581321, 599887, 618452, 637016, 655582, 674147, 692712, 711277, 729843, 748408, 766973, 785538, 804103, 822669, 841233, 859798, 878364, 896929, 915494, 934059, 952625, 971190, 989755]]
    # 基础3 = 61497
    # 成长3 = 18565
    攻击次数4 = 4
    CD = 290.0
    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data2[self.等级] * self.攻击次数3+self.data3[self.等级] * self.攻击次数4) * self.倍率

    def 加成倍率(self, 武器类型):
        return 0.0


class 技能23(被动技能):
    名称 = '幸运棒棒糖'
    所在等级 = 25
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.07 + 0.01 * self.等级, 5)


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

知源·魔道学者一觉序号 = 0
知源·魔道学者二觉序号 = 0
知源·魔道学者三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        知源·魔道学者一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        知源·魔道学者二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        知源·魔道学者三觉序号 = 技能序号[i.名称]

知源·魔道学者护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        知源·魔道学者护石选项.append(i.名称)

知源·魔道学者符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        知源·魔道学者符文选项.append(i.名称)


class 知源·魔道学者角色属性(角色属性):

    实际名称 = '知源·魔道学者'
    角色 = '魔法师(女)'
    职业 = '魔道学者'

    武器选项 = ['魔杖', '法杖', '棍棒', '矛', '扫把']

    类型选择 = ['魔法固伤']

    类型 = '魔法固伤'
    防具类型 = '皮甲'
    防具精通属性 = ['智力']

    主BUFF = 1.92

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)


class 知源·魔道学者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 知源·魔道学者角色属性()
        self.角色属性A = 知源·魔道学者角色属性()
        self.角色属性B = 知源·魔道学者角色属性()
        self.一觉序号 = 知源·魔道学者一觉序号
        self.二觉序号 = 知源·魔道学者二觉序号
        self.三觉序号 = 知源·魔道学者三觉序号
        self.护石选项 = deepcopy(知源·魔道学者护石选项)
        self.符文选项 = deepcopy(知源·魔道学者符文选项)
