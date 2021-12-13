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

class 技能0(职业主动技能):
    名称 = '下段踢'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    # 基础 = 737.65306122449
    # 成长 = 83.3469387755102
    #物理武器攻击力：<data0>%
    data0 = [0, 991, 1092, 1192, 1292, 1394, 1494, 1594, 1694, 1797, 1897, 1996, 2097, 2197, 2298, 2399, 2499, 2599, 2699, 2801, 2901, 3001, 3104, 3204, 3304, 3405, 3506, 3606, 3707, 3807, 3907, 4008, 4109, 4209, 4309, 4411, 4511, 4611, 4712, 4812, 4913, 5014, 5114, 5214, 5314, 5416, 5516, 5616, 5719, 5819, 5919, 6020, 6121, 6221, 6322, 6422, 6522, 6623, 6724, 6824, 6925, 7027, 7127, 7227, 7329, 7429, 7529, 7628, 7729, 7829, 7930]
    攻击次数 = 1
    CD = 2.0
    TP成长 = 0.08
    TP上限 = 5


class 技能1(职业主动技能):
    名称 = '碎骨'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 基础 = 3004.85
    # 成长 = 339.15
    #下段踢物理武器攻击力：<data1>%
    data0 = [0, 4058, 4468, 4879, 5290, 5703, 6114, 6527, 6937, 7349, 7760, 8172, 8583, 8995, 9406, 9819, 10230, 10641, 11053, 11464, 11875, 12288, 12699, 13111, 13521, 13933, 14345, 14757, 15168, 15581, 15990, 16403, 16814, 17226, 17638, 18049, 18460, 18872, 19283, 19696, 20106, 20518, 20930, 21341, 21752, 22165, 22575, 22988, 23399, 23811, 24222, 24633, 25044, 25457, 25868, 26281, 26692, 27101, 27513, 27926, 28337, 28750, 29160, 29573, 29983, 30394, 30807, 31218, 31629, 32041, 32452]

    攻击次数 = 1
    CD = 7
    TP成长 = 0.08
    TP上限 = 5


class 技能2(职业主动技能):
    名称 = '铁山靠'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 基础 = 2892.2
    # 成长 = 326.8
    data0 = [0, 4117, 4535, 4954, 5372, 5790, 6208, 6625, 7043, 7462, 7880, 8298, 8716, 9133, 9552, 9970, 10388, 10806, 11223, 11641, 12060, 12477, 12895, 13313, 13730, 14148, 14567, 14983, 15402, 15821, 16238, 16656, 17075, 17492, 17910, 18329, 18746, 19165, 19583, 20000, 20418, 20836, 21254, 21673, 22088, 22507, 22925, 23342, 23761, 24179, 24596, 25015, 25433, 25850, 26269, 26688, 27105, 27523, 27941, 28358, 28778, 29196, 29613, 30031, 30448, 30866, 31283, 31701, 32120, 32538, 32955]
    CD = 7
    TP成长 = 0.1
    TP上限 = 5


class 技能3(被动技能):
    名称 = '柔化肌肉'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.125 + 0.015 * self.等级, 5)


class 技能4(职业主动技能):
    名称 = '闪击快打'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 基础 = 4565.54054054054
    # 成长 = 515.459459459459
    data0 = [0, 2691, 2964, 3236, 3511, 3783, 4055, 4330, 4602, 4877, 5149, 5422, 5694, 5968, 6240, 6514, 6786, 7060, 7333, 7605, 7881, 8152, 8425, 8697, 8972, 9244, 9518, 9790, 10065, 10337, 10609, 10884, 11155, 11429, 11702, 11975, 12247, 12522, 12793, 13068, 13340, 13614, 13887, 14158, 14434, 14704, 14978, 15251, 15525, 15798, 16070, 16344, 16617, 16890, 17164, 17436, 17709, 17983, 18254, 18528, 18801, 19075, 19348, 19620, 19894, 20167, 20439, 20713, 20986, 21260, 21532]
    data1 = [0, 3741, 4121, 4501, 4882, 5258, 5639, 6017, 6398, 6777, 7158, 7536, 7915, 8295, 8675, 9056, 9434, 9815, 10194, 10574, 10951, 11332, 11710, 12091, 12470, 12851, 13231, 13611, 13990, 14369, 14749, 15127, 15508, 15886, 16267, 16645, 17025, 17405, 17785, 18164, 18544, 18924, 19304, 19684, 20063, 20442, 20820, 21200, 21581, 21960, 22340, 22719, 23098, 23478, 23858, 24237, 24617, 24997, 25377, 25758, 26134, 26515, 26893, 27274, 27653, 28034, 28413, 28794, 29171, 29552, 29931]

    攻击次数2 = 1
    CD = 12.0
    TP成长 = 0.1
    TP上限 = 5


class 技能5(职业主动技能):
    名称 = '冲膝'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 6663.62857142857
    # 成长 = 752.371428571429
    #物理攻击力：<data1>%
    data0 = [0, 8983, 9895, 10804, 11715, 12627, 13538, 14450, 15362, 16273, 17183, 18096, 19008, 19918, 20829, 21741, 22653, 23562, 24476, 25386, 26296, 27208, 28120, 29031, 29941, 30855, 31766, 32676, 33588, 34499, 35410, 36322, 37234, 38145, 39054, 39967, 40878, 41789, 42700, 43613, 44524, 45434, 46346, 47257, 48169, 49081, 49992, 50903, 51812, 52725, 53638, 54547, 55459, 56371, 57282, 58192, 59104, 60016, 60927, 61839, 62750, 63659, 64573, 65485, 66396, 67305, 68217, 69129, 70039, 70952, 71863]
    CD = 15
    TP成长 = 0.1
    TP上限 = 5


class 技能6(职业主动技能):
    名称 = '炽焰旋风腿'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 8101.2
    # 成长 = 915.8
    #旋风腿攻击力：<data1>%
    data0 = [0, 1095, 1207, 1317, 1428, 1540, 1650, 1763, 1874, 1985, 2097, 2207, 2319, 2430, 2540, 2652, 2761, 2875, 2985, 3096, 3208, 3319, 3430, 3542, 3653, 3763, 3874, 3986, 4097, 4208, 4320, 4431, 4541, 4653, 4763, 4875, 4987, 5098, 5210, 5321, 5433, 5542, 5653, 5765, 5875, 5987, 6099, 6209, 6321, 6432, 6543, 6655, 6766, 6877, 6987, 7097, 7210, 7321, 7433, 7544, 7655, 7767, 7876, 7988, 8099, 8211, 8323, 8434, 8545, 8655, 8766]
    攻击次数 = 7
    #下踢攻击力：<data2>%
    data1 = [0, 3317, 3654, 3989, 4326, 4662, 5000, 5335, 5672, 6009, 6346, 6681, 7018, 7355, 7691, 8027, 8363, 8700, 9038, 9374, 9710, 10047, 10383, 10719, 11056, 11394, 11730, 12066, 12402, 12739, 13076, 13411, 13750, 14084, 14422, 14759, 15095, 15431, 15769, 16104, 16440, 16778, 17115, 17451, 17788, 18123, 18459, 18797, 19132, 19470, 19807, 20143, 20478, 20816, 21152, 21489, 21825, 22163, 22498, 22836, 23171, 23508, 23845, 24180, 24516, 24853, 25191, 25528, 25864, 26199, 26537]
    攻击次数2 = 1

    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 +=6
            self.data0 = [int(x*0.76) for x in self.data0]
            # self.倍率 *= 1.28718046004268
        elif x == 1:
            self.攻击次数 +=6
            self.data0 = [int(x*0.86) for x in self.data0]


class 技能7(职业主动技能):
    名称 = '闪电之舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    # 基础 = 7933.9375
    # 成长 = 896.0625
    #每次攻击时的物理攻击力：<data0>%
    data0 = [0, 1316, 1451, 1584, 1717, 1852, 1984, 2119, 2253, 2385, 2519, 2655, 2787, 2920, 3054, 3188, 3320, 3455, 3589, 3721, 3856, 3990, 4122, 4257, 4389, 4523, 4658, 4792, 4923, 5059, 5192, 5326, 5459, 5592, 5727, 5861, 5993, 6127, 6261, 6395, 6528, 6661, 6796, 6930, 7062, 7196, 7331, 7464, 7597, 7731, 7865, 7999, 8132, 8266, 8398, 8534, 8667, 8799, 8934, 9068, 9200, 9335, 9469, 9601, 9736, 9869, 10002, 10137, 10269, 10403, 10538]
    #终结一击攻击力：<data1>%
    data1 = [0, 9219, 10156, 11091, 12025, 12961, 13897, 14833, 15768, 16704, 17639, 18574, 19510, 20446, 21379, 22316, 23251, 24188, 25122, 26056, 26993, 27930, 28864, 29799, 30735, 31671, 32607, 33540, 34478, 35412, 36348, 37284, 38218, 39155, 40089, 41024, 41961, 42895, 43832, 44766, 45702, 46638, 47572, 48509, 49444, 50379, 51314, 52250, 53186, 54121, 55055, 55992, 56927, 57863, 58798, 59733, 60668, 61604, 62541, 63475, 64410, 65345, 66282, 67218, 68151, 69087, 70023, 70959, 71895, 72828, 73766]

    攻击次数 = 1
    攻击次数2 = 1
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.09


class 技能8(职业主动技能):
    名称 = '瞬影连环踢'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    #飞踢攻击力：<data0>%
    data0 = [0, 20686, 22786, 24885, 26984, 29082, 31181, 33279, 35379, 37477, 39578, 41675, 43773, 45873, 47971, 50070, 52169, 54269, 56367, 58466, 60564, 62663, 64760, 66861, 68958, 71058, 73157, 75255, 77354, 79452, 81551, 83650, 85750, 87848, 89948, 92046, 94144, 96243, 98342, 100442, 102540, 104639, 106737, 108836, 110934, 113035, 115133, 117231, 119330, 121428, 123527, 125625, 127724, 129823, 131923, 134021, 136121, 138219, 140317, 142416, 144515, 146615, 148713, 150812, 152910, 155009, 157107, 159208, 161306, 163405, 165503]

    CD = 45
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.23 + 0.08


class 技能9(被动技能):
    名称 = '烈焰燃烧'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03 + 0.01 * self.等级, 5)
    # 仅作用于面板显示

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03 + 0.01 * self.等级, 5)

class 技能10(职业主动技能):
    名称 = '烈焰焚步'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    # 基础 = 31307
    # 成长 = 9452
    #再次施放后强化的技能攻击力增加量：+<data7>%
    data0 = [0, 40761, 50213, 59665, 69116, 78568, 88020, 97472, 106924, 141835, 153355, 164876, 176395, 187917, 199436, 210956, 222477, 233994, 245516, 257034, 268555, 280074, 291594, 303114, 314631, 326152, 337672, 349191, 360712, 372232, 383751, 395271, 406789, 418312, 429831, 441351, 452869, 464390, 475910, 487430, 498948, 510472, 521991, 533506, 545029, 556547, 568069, 579589, 591106, 602627, 614145, 625667, 637187, 648708, 660227, 671748, 683265, 694784, 706305, 717825, 729346, 740864, 752385, 763903, 775422, 786946, 798466, 809983, 821503, 833023, 844543]

    CD = 145
    关联技能 = ['所有']
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['烈焰焚步','双重释放','极武霸皇踢','焚火逐日拳']
    #手搓 -5% CD

    def 等效CD(self, 武器类型, 输出类型):
        if 武器类型 == '拳套':
            return round(self.CD / self.恢复 * (1-0.05), 1)

    # 被动技能攻击力加成
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.02 + 0.04 * (self.等级-1), 5)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.85


class 技能11(职业主动技能):
    名称 = '飞燕旋风'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data0 = [0, 4312, 4748, 5185, 5622, 6061, 6500, 6935, 7373, 7810, 8248, 8684, 9122, 9559, 9997, 10435, 10872, 11310, 11746, 12184, 12623, 13059, 13495, 13934, 14372, 14811, 15246, 15683, 16121, 16557, 16995, 17433, 17871, 18308, 18746, 19183, 19620, 20057, 20494, 20932, 21370, 21807, 22245, 22682, 23119, 23556, 23994, 24432, 24869, 25307, 25744, 26182, 26618, 27057, 27493, 27930, 28367, 28805, 29245, 29680, 30118, 30555, 30993, 31429, 31867, 32305, 32743, 33181, 33617, 34055, 34491]
    data1 = [0, 8870, 9772, 10672, 11571, 12472, 13374, 14273, 15171, 16072, 16971, 17873, 18773, 19672, 20573, 21473, 22373, 23272, 24172, 25072, 25973, 26874, 27773, 28674, 29573, 30473, 31373, 32273, 33173, 34074, 34975, 35874, 36773, 37674, 38575, 39474, 40374, 41273, 42175, 43076, 43976, 44874, 45775, 46676, 47576, 48475, 49375, 50275, 51176, 52076, 52975, 53875, 54777, 55676, 56576, 57476, 58376, 59276, 60177, 61076, 61976, 62878, 63777, 64677, 65577, 66475, 67377, 68277, 69177, 70077, 70978]

    攻击次数 = 2
    攻击次数2 = 1
    CD = 30
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 +=2
            self.倍率 *= 0.82
        elif x == 1:
            self.攻击次数 +=2
            self.倍率 *= 0.82 + 0.06


# 碎心修炼场实测有伤害丢失的BUG
class 技能12(职业主动技能):
    名称 = '旋风碎心踢'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    #旋转多段攻击攻击力：<data0>%
    data0 = [0, 598, 660, 720, 780, 842, 902, 964, 1024, 1085, 1146, 1207, 1267, 1329, 1389, 1449, 1511, 1571, 1633, 1693, 1754, 1814, 1875, 1935, 1996, 2057, 2117, 2179, 2239, 2301, 2361, 2422, 2483, 2544, 2604, 2665, 2726, 2787, 2848, 2908, 2970, 3030, 3092, 3152, 3212, 3274, 3334, 3395, 3456, 3517, 3577]
    #第一击攻击力：<data1>%
    data1 = [0, 8666, 9544, 10424, 11302, 12183, 13060, 13941, 14819, 15700, 16577, 17456, 18337, 19215, 20095, 20973, 21854, 22732, 23611, 24490, 25370, 26249, 27128, 28006, 28886, 29765, 30644, 31523, 32403, 33282, 34160, 35040, 35919, 36800, 37677, 38558, 39436, 40314, 41194, 42072, 42953, 43832, 44711, 45590, 46469, 47349, 48227, 49107, 49985, 50865, 51743]
    #最后一击攻击力：<data2>%
    data2 =  [0, 19642, 21635, 23627, 25620, 27614, 29607, 31599, 33590, 35584, 37576, 39570, 41563, 43556, 45547, 47541, 49534, 51526, 53519, 55512, 57505, 59496, 61491, 63483, 65475, 67468, 69461, 71453, 73446, 75440, 77432, 79424, 81419, 83409, 85403, 87395, 89389, 91381, 93375, 95368, 97359, 99352, 101344, 103339, 105331, 107324, 109316, 111308, 113301, 115293, 117288]

    攻击次数 = 4
    攻击次数2 = 1
    攻击次数3 = 1

    CD = 50
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.16
        elif x == 1:
            self.倍率 *= 1.16 + 0.08


class 技能13(被动技能):
    名称 = '烈火支配'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)


class 技能14(职业主动技能):
    名称 = '烈火强踢'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    data0 = [0, 51517, 56743, 61969, 67196, 72422, 77647, 82876, 88100, 93327, 98552, 103780, 109006, 114232, 119458, 124686, 129911, 135138, 140362, 145591, 150817, 156042, 161270, 166497, 171721, 176949, 182175, 187401, 192629, 197853, 203081, 208307, 213533, 218758, 223986, 229212, 234438, 239665, 244892, 250117, 255344, 260570, 265796, 271023, 276249, 281475, 286703, 291927, 297153, 302382, 307607, 312833, 318060, 323287, 328512, 333739, 338965, 344192, 349418, 354644, 359871, 365098, 370323, 375548, 380776, 386003, 391227, 396455, 401682, 406907, 412134]

    CD = 45
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35
            self.CD *= 0.9


class 技能15(职业主动技能):
    名称 = '烈火强拳'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    #突进拳击攻击力：<data0>%
    data0 = [0, 63496, 69937, 76380, 82819, 89261, 95703, 102148, 108586, 115029, 121471, 127912, 134354, 140794, 147236, 153678, 160121, 166562, 173003, 179445, 185888, 192326, 198770, 205213, 211653, 218095, 224536, 230978, 237420, 243861, 250304, 256743, 263186, 269630, 276068, 282512, 288953, 295395, 301836, 308278, 314720, 321162, 327602, 334045, 340485, 346927, 353369, 359813, 366253, 372695, 379135, 385577, 392018, 398461, 404901, 411343, 417787, 424228, 430670, 437110, 443552, 449993, 456435, 462878, 469319, 475760, 482203, 488644, 495085, 501526, 507968]

    CD = 55
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35

# 不适用拳套掌握CDR


class 技能16(职业主动技能):
    名称 = '极武霸皇踢'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    # 基础 = 82676.3333333337
    # 成长 = 24957.3333333333
    data0 = [0, 26170, 32237, 38306, 44375, 50443, 56510, 62580, 68647, 74716, 80785, 86852, 92921, 98989, 105058, 111126, 117194, 123264, 129331, 135401, 141467, 147538, 153604, 159675, 165742, 171810, 177879, 183947, 190015, 196084, 202152, 208221, 214289, 220357, 226426, 232494, 238561, 244631, 250698, 256768, 262836, 268905, 274972, 281041, 287109, 293178, 299245, 305315, 311382, 317452, 323518, 329589, 335656, 341724, 347794, 353861, 359931, 365998, 372066, 378135, 384203, 390272, 396340, 402410, 408477, 414546, 420612, 426683, 432750, 438819, 444887]
    data1 = [0, 32857, 40476, 48095, 55714, 63333, 70952, 78571, 86190, 93809, 101428, 109047, 116666, 124285, 131903, 139525, 147142, 154761, 162381, 170000, 177619, 185238, 192857, 200476, 208094, 215715, 223334, 230951, 238571, 246190, 253808, 261428, 269047, 276668, 284284, 291905, 299525, 307143, 314761, 322381, 330000, 337619, 345238, 352857, 360476, 368095, 375714, 383333, 390951, 398571, 406190, 413810, 421429, 429048, 436667, 444287, 451905, 459524, 467143, 474762, 482381, 490000, 497619, 505238, 512857, 520478, 528095, 535713, 543334, 550954, 558570]
    攻击次数2 = 1
    data2 = [0, 72285, 89046, 105808, 122571, 139334, 156095, 172857, 189619, 206381, 223143, 239905, 256665, 273428, 290190, 306951, 323714, 340476, 357238, 373999, 390762, 407524, 424287, 441048, 457810, 474570, 491335, 508096, 524857, 541618, 558380, 575143, 591905, 608667, 625428, 642191, 658952, 675716, 692477, 709239, 726001, 742763, 759525, 776286, 793048, 809810, 826572, 843334, 860096, 876858, 893620, 910381, 927143, 943907, 960669, 977430, 994192, 1010952, 1027717, 1044477, 1061239, 1078000, 1094762, 1111525, 1128287, 1145049, 1161810, 1178573, 1195334, 1212097, 1228859]
    攻击次数3 = 1
    CD = 180


class 技能17(被动技能):
    名称 = '千锤百炼'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能18(职业主动技能):
    名称 = '炼狱坠星腿'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    # 基础 = 79841.4
    # 成长 = 9014.6
    CD = 60
    #下劈攻击力：<data0>%
    data0 = [0, 48374, 53281, 58189, 63096, 68004, 72912, 77819, 82727, 87635, 92541, 97449, 102357, 107264, 112172, 117080, 121986, 126894, 131802, 136709, 141617, 146525, 151432, 156340, 161247, 166155, 171062, 175970, 180878, 185785, 190693, 195601, 200507, 205415, 210323, 215230, 220138, 225046, 229952, 234860, 239768, 244675, 249583, 254491, 259398, 264306, 269213, 274120, 279028, 283936, 288844, 293751, 298659, 303567, 308473, 313381, 318289, 323196, 328104, 333012, 337918, 342826, 347734, 352641, 357549, 362457, 367364, 372272, 377179, 382086, 386994]

    #冲击波攻击力：<data1>%
    data1 = [0, 58278, 64191, 70103, 76016, 81928, 87840, 93752, 99665, 105577, 111490, 117403, 123315, 129226, 135139, 141052, 146964, 152877, 158789, 164701, 170613, 176526, 182438, 188351, 194263, 200176, 206087, 212000, 217912, 223825, 229738, 235650, 241562, 247474, 253387, 259299, 265212, 271124, 277036, 282948, 288861, 294773, 300686, 306598, 312511, 318422, 324335, 330247, 336160, 342073, 347985, 353897, 359809, 365722, 371634, 377547, 383459, 389372, 395283, 401196, 407108, 413021, 418933, 424846, 430757, 436670, 442582, 448495, 454408, 460320, 466232]

    攻击次数2 = 1

# 不适用拳套掌握CDR


class 技能19(职业主动技能):
    名称 = '焚火逐日拳'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    # 基础 = 251118.333333333
    # 成长 = 75810.6666666667
    CD = 290

    #铁山靠攻击力：<data0>%
    data0 = [0, 37653, 46384, 55115, 63846, 72578, 81309, 90040, 98771, 107502, 116233, 124965, 133696, 142427, 151158, 159889, 168621, 177353, 186084, 194815, 203546, 212277, 221008, 229740, 238471, 247202, 255933, 264664, 273395, 282126, 290858, 299589, 308320, 317051, 325782, 334513, 343246, 351977, 360708, 369439, 378170, 386901, 395633, 404364, 413095, 421826, 430557, 439288, 448020, 456751, 465482, 474213, 482944, 491675, 500406, 509138, 517870, 526601, 535332, 544063, 552795, 561526, 570257, 578988, 587719, 596450, 605181, 613913, 622644, 631375, 640106]
    #正拳第1击：<data1>%
    data1 = [0, 18826, 23192, 27557, 31923, 36288, 40654, 45019, 49386, 53751, 58117, 62482, 66848, 71213, 75579, 79944, 84310, 88676, 93041, 97407, 101772, 106139, 110504, 114870, 119235, 123601, 127966, 132332, 136697, 141063, 145428, 149794, 154159, 158526, 162891, 167257, 171623, 175988, 180354, 184719, 189085, 193450, 197816, 202181, 206547, 210912, 215279, 219644, 224010, 228375, 232741, 237106, 241472, 245837, 250203, 254568, 258934, 263301, 267666, 272032, 276397, 280763, 285128, 289494, 293859, 298225, 302590, 306956, 311321, 315687, 320052]
    #正拳第2击：<data2>%
    data2 =  [0, 22591, 27830, 33069, 38307, 43546, 48786, 54024, 59263, 64502, 69740, 74979, 80217, 85456, 90695, 95933, 101172, 106412, 111650, 116889, 122127, 127366, 132605, 137843, 143082, 148321, 153559, 158798, 164036, 169276, 174515, 179753, 184992, 190231, 195469, 200708, 205946, 211185, 216425, 221663, 226902, 232141, 237379, 242618, 247857, 253095, 258334, 263572, 268811, 274051, 279289, 284528, 289767, 295005, 300244, 305482, 310721, 315960, 321198, 326438, 331677, 336915, 342154, 347392, 352631, 357870, 363108, 368347, 373586, 378824, 384064]
    #正拳第3击：<data3>%
    data3 = [0, 26357, 32469, 38580, 44692, 50804, 56915, 63028, 69140, 75252, 81363, 87475, 93587, 99699, 105810, 111923, 118035, 124147, 130258, 136370, 142482, 148593, 154705, 160817, 166930, 173041, 179153, 185265, 191377, 197488, 203600, 209712, 215825, 221936, 228048, 234160, 240272, 246383, 252495, 258607, 264718, 270830, 276943, 283055, 289166, 295278, 301390, 307502, 313613, 319725, 325838, 331950, 338061, 344173, 350285, 356396, 362508, 368620, 374732, 380843, 386956, 393068, 399180, 405291, 411403, 417515, 423627, 429738, 435851, 441963, 448074]
    #高踢攻击力：<data4>%
    data4 = [0, 56479, 69576, 82674, 95770, 108867, 121963, 135060, 148157, 161254, 174351, 187447, 200545, 213641, 226738, 239834, 252932, 266029, 279125, 292222, 305319, 318416, 331512, 344609, 357707, 370803, 383900, 396996, 410094, 423191, 436287, 449384, 462480, 475578, 488674, 501771, 514869, 527965, 541062, 554158, 567255, 580352, 593449, 606546, 619642, 632740, 645836, 658933, 672029, 685127, 698224, 711320, 724417, 737514, 750611, 763707, 776804, 789902, 802998, 816095, 829191, 842289, 855385, 868482, 881579, 894675, 907773, 920869, 933966, 947062, 960160]
    #终结攻击拳击攻击力：<data5>%
    data5 = [0, 82837, 102045, 121254, 140463, 159671, 178880, 198089, 217298, 236506, 255714, 274924, 294132, 313340, 332550, 351758, 370966, 390176, 409384, 428592, 447802, 467010, 486218, 505427, 524636, 543845, 563053, 582262, 601471, 620679, 639888, 659097, 678305, 697514, 716723, 735931, 755141, 774349, 793557, 812765, 831975, 851183, 870392, 889601, 908809, 928018, 947227, 966435, 985644, 1004853, 1024061, 1043270, 1062478, 1081687, 1100896, 1120104, 1139314, 1158522, 1177730, 1196940, 1216148, 1235356, 1254566, 1273774, 1292982, 1312191, 1331400, 1350608, 1369817, 1389026, 1408234]
    #终结攻击拳击冲击波攻击力：<data6>%
    data6 = [0, 131786, 162346, 192904, 223464, 254023, 284582, 315142, 345701, 376260, 406819, 437379, 467937, 498497, 529057, 559615, 590175, 620734, 651293, 681852, 712412, 742970, 773530, 804090, 834648, 865208, 895767, 926326, 956885, 987445, 1018003, 1048563, 1079123, 1109681, 1140241, 1170800, 1201360, 1231918, 1262478, 1293038, 1323596, 1354156, 1384715, 1415274, 1445833, 1476393, 1506951, 1537511, 1568071, 1598629, 1629189, 1659748, 1690307, 1720866, 1751426, 1781984, 1812544, 1843104, 1873662, 1904222, 1934781, 1965340, 1995899, 2026459, 2057018, 2087577, 2118137, 2148695, 2179255, 2209814, 2240373]
    攻击次数 = 1
    攻击次数2 = 1
    攻击次数3 = 1
    攻击次数4 = 1
    攻击次数5 = 1
    攻击次数6 = 1
    攻击次数7 = 1

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

class 技能20(被动技能):
    名称 = '拳套掌握'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['烈焰焚步','双重释放', '极武霸皇踢', '焚火逐日拳']
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 1.0

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if 武器类型 == '拳套':
                return 0.9
            else:
                return 1.0

class 技能21(职业主动技能):
    名称 = '双重释放'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    CD = 145
    data0 = 0
    攻击次数1 = 0
    def 等效百分比(self, 武器类型):
        return (self.data0)

class 技能22(职业主动技能):
    名称 = '肘击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # 基础 = 2892.2
    # 成长 = 326.8
    data0 = [0, 2610, 2874, 3138, 3402, 3668, 3931, 4197, 4461, 4727, 4991, 5255, 5520, 5786, 6049, 6315, 6578, 6844, 7109, 7373, 7637, 7903, 8167, 8432, 8698, 8962, 9227, 9490, 9757, 10020, 10286, 10551, 10815, 11079, 11344, 11607, 11875, 12138, 12403, 12668, 12932, 13197, 13462, 13727, 13992, 14255, 14520, 14785, 15050, 15315, 15579, 15844, 16109, 16372, 16639, 16903, 17167, 17432, 17696, 17962, 18227, 18490, 18757, 19020, 19285, 19550, 19815, 20079, 20344, 20607, 20874]

    CD = 6
    TP成长 = 0.1
    TP上限 = 5

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

归元·散打·男一觉序号 = 0
归元·散打·男二觉序号 = 0
归元·散打·男三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        归元·散打·男一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        归元·散打·男二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        归元·散打·男三觉序号 = 技能序号[i.名称]

归元·散打·男护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元·散打·男护石选项.append(i.名称)

归元·散打·男符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元·散打·男符文选项.append(i.名称)


class 归元·散打·男角色属性(角色属性):
    实际名称 = '归元·散打·男'
    角色 = '格斗家(男)'
    职业 = '散打'

    武器选项 = ['拳套', '臂铠']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 2.04

    # 额外加成
    二挡关联 = '无'

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    # 武极取整问题重写以下函数
    def 面板物理攻击力(self):
        面板物理攻击 = (self.物理攻击力 + self.进图物理攻击力)
        for i in self.技能栏:
            try:
                面板物理攻击 *= i.物理攻击力倍率(self.武器类型)
            except:
                pass
        # 武极48级被动的运算取整必须在其他物攻提升率之前
        面板物理攻击 = int(面板物理攻击) * (1 + self.百分比三攻) * (1 + self.年宠技能 *
                                                   0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        return 面板物理攻击

    def 站街物理攻击力(self):
        站街物理攻击 = self.物理攻击力
        for i in self.技能栏:
            try:
                站街物理攻击 *= i.物理攻击力倍率(self.武器类型)
            except:
                pass
        站街物理攻击 = int(站街物理攻击)
        return 站街物理攻击

    def 数据计算(self, x=0, y=-1):
        self.预处理()
        # 初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        # 整合二挡伤害
        总伤害 = 0
        for i in self.技能栏:
            if self.二挡关联 != '无':
                if (i.名称 == '瞬影连环踢' and self.二挡关联 == '二挡：瞬影连环踢') or (i.名称 == '烈火强拳' and self.二挡关联 == '二挡：烈火强拳') or (i.名称 == '炼狱坠星腿' and self.二挡关联 == '二挡：炼狱坠星腿'):
                    技能总伤害[self.技能序号[i.名称]] += 技能总伤害[self.技能序号['烈焰焚步']]
                    技能总伤害[self.技能序号['烈焰焚步']] *= 0

            if i.名称 != '烈焰焚步':
                总伤害 += 技能总伤害[self.技能序号[i.名称]]

        # 返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)


class 归元·散打·男(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 归元·散打·男角色属性()
        self.角色属性A = 归元·散打·男角色属性()
        self.角色属性B = 归元·散打·男角色属性()
        self.一觉序号 = 归元·散打·男一觉序号
        self.二觉序号 = 归元·散打·男二觉序号
        self.三觉序号 = 归元·散打·男三觉序号
        self.护石选项 = deepcopy(归元·散打·男护石选项)
        self.符文选项 = deepcopy(归元·散打·男符文选项)

    def 界面(self):
        super().界面()

        self.二挡关联选择 = MyQComboBox(self.main_frame2)
        self.二挡关联选择.addItem('二挡：瞬影连环踢')
        self.二挡关联选择.addItem('二挡：烈火强拳')
        self.二挡关联选择.addItem('二挡：炼狱坠星腿')
        self.二挡关联选择.setCurrentIndex(0)
        self.二挡关联选择.resize(150, 20)
        self.二挡关联选择.move(320, 270)

        self.职业存档.append(('二挡关联选择', self.二挡关联选择, 1))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.觉醒选择状态 == 2:
            属性.二挡关联 = self.二挡关联选择.currentText()
        else:
            属性.二挡关联 = '无'
