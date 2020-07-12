from PublicReference.base import *

class 黑暗武士主动技能(主动技能):
    类型 = '物理'
    计算CD = 0
    def 等效CD(self, 武器类型):
        if self.计算CD != 0:
            return round(self.计算CD, 1)
        if self.类型 == '物理':
            if 武器类型 == '短剑':
                return round(self.CD / self.恢复 * 1.00, 1)
            if 武器类型 == '太刀':
                return round(self.CD / self.恢复 * 0.95, 1)
            if 武器类型 == '钝器':
                return round(self.CD / self.恢复 * 1.05, 1)
            if 武器类型 == '巨剑':
                return round(self.CD / self.恢复 * 1.10, 1)
            if 武器类型 == '光剑':
                return round(self.CD / self.恢复 * 0.90, 1)
        else:
            if 武器类型 == '短剑':
                return round(self.CD / self.恢复 * 1.05, 1)
            else:
                return round(self.CD / self.恢复 * 1.00, 1)

class 黑暗武士技能0(黑暗武士主动技能):
    名称 = '挑击'
    类型 = '物理'
    所在等级 = 1
    等级上限 = 20
    基础等级 = 10
    基础 = 88.9
    成长 = 11.1
    CD = 2.0
    TP成长 = 0.08
    TP上限 = 5

class 黑暗武士技能1(黑暗武士主动技能):
    名称 = '暗影斩'
    类型 = '魔法'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    基础 = 577.673
    成长 = 65.327
    CD = 3.1
    TP成长 = 0.1
    TP上限 = 5

class 黑暗武士技能2(黑暗武士主动技能):
    名称 = '黑暗十字斩'
    类型 = '物理'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 125.776
    成长 = 14.224
    攻击次数 = 2
    基础2 = 552.490
    成长2 = 52.531
    攻击次数2 = 1
    CD = 3.0
    TP成长 = 0.08
    TP上限 = 5

class 黑暗武士技能3(黑暗武士主动技能):
    名称 = '暗影·波动剑'
    类型 = '魔法'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 628.98
    成长 = 71.020
    CD = 3.1
    TP成长 = 0.08
    TP上限 = 5


class 黑暗武士技能4(黑暗武士主动技能):
    名称 = '滑斩'
    类型 = '物理'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    基础 = 749.347
    成长 = 84.653
    CD = 3.0

class 黑暗武士技能5(黑暗武士主动技能):
    名称 = '跃斩'
    类型 = '物理'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    基础 = 749.347
    成长 = 84.653
    CD = 3.0
    # 钝器冲击波
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            if 武器类型 != '钝器':
                return self.基础 + self.成长 * self.等级
            else:
                return (self.基础 + self.成长 * self.等级) + (442.269 + 52.531 * self.等级)

class 黑暗武士技能6(黑暗武士主动技能):
    名称 = '跃地斩'
    类型 = '物理'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 320.429
    成长 = 34.571
    攻击次数 = 4
    CD = 4.0
    TP成长 = 0.08
    TP上限 = 5

class 黑暗武士技能7(黑暗武士主动技能):
    名称 = '冥光斩'
    类型 = '魔法'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 435.787
    成长 = 49.213
    攻击次数 = 2
    CD = 10.5
    TP成长 = 0.10
    TP上限 = 5

class 黑暗武士技能8(黑暗武士主动技能):
    名称 = '瞬影斩'
    类型 = '物理'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 1299.2
    成长 = 146.8
    攻击次数 = 2
    CD = 5

class 黑暗武士技能9(黑暗武士主动技能):
    名称 = '暗月斩'
    类型 = '魔法'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 395.347
    成长 = 44.653
    基础2 = 427.633
    成长2 = 48.367
    攻击次数2 = 1
    CD = 4.2
    TP成长 = 0.08
    TP上限 = 5

class 黑暗武士技能10(黑暗武士主动技能):
    名称 = '暗影三击剑'
    类型 = '魔法'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 1822.806
    成长 = 346.194
    CD = 8.4

class 黑暗武士技能11(黑暗武士主动技能):
    名称 = '暗劲爆发'
    类型 = '物理'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 46
    基础 = 353.044
    成长 = 39.956
    基础2 = 389.933
    成长2 = 44.067
    攻击次数2 = 8
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 5


class 黑暗武士技能12(黑暗武士主动技能):
    名称 = '邪影·波动剑'
    类型 = '魔法'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 100.0
    成长 = 0
    基础2 = 709.810
    成长2 = 80.190
    攻击次数2 = 3
    基础3 = 141.905
    成长3 = 16.095
    攻击次数3 = 4
    CD = 7.0

class 黑暗武士技能13(黑暗武士主动技能):
    名称 = '突刺'
    类型 = '物理'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 160.745 * 3
    成长 = 18.255 * 3
    CD = 3
    # 太/光加成
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            if 武器类型 == '钝器' or '太刀':
                return (112.213 + 12.787 * self.等级) * 5
            else:
                return self.基础 + self.成长 * self.等级

class 黑暗武士技能14(黑暗武士主动技能):
    名称 = '暗影鞭'
    类型 = '魔法'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 29
    基础 = 635.357
    成长 = 120.643
    基础2 = 1483.5
    成长2 = 281.5
    攻击次数2 = 1
    CD = 8.4
    TP成长 = 0.10
    TP上限 = 5

class 黑暗武士技能15(黑暗武士主动技能):
    名称 = '灭魂封魔斩'
    类型 = '物理'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3785.525 * 1.24
    成长 = 427.275 * 1.24
    CD = 30

class 黑暗武士技能16(黑暗武士主动技能):
    名称 = '冥魂珠'
    类型 = '魔法'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 293.811
    成长 = 33.189
    攻击次数 = 13
    基础2 = 668.514
    成长2 = 75.486
    攻击次数2 = 1
    CD = 10.5
    TP成长 = 0.1
    TP上限 = 5


class 黑暗武士技能17(黑暗武士主动技能):
    名称 = '暗影升龙击'
    类型 = '物理'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 3480.027
    成长 = 392.973
    CD = 10

class 黑暗武士技能18(黑暗武士主动技能):
    名称 = '冥魂之陨'
    类型 = '魔法'
    所在等级 = 35
    等级上限 = 60
    基础等级 =36
    基础 = 258.686
    成长 = 29.314
    攻击次数 = 24
    CD = 21
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.14
        self.成长 *= 1.14
        self.CD *= 0.9

class 黑暗武士技能19(黑暗武士主动技能):
    名称 = '破魂之刃'
    类型 = '物理'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6441.4
    成长 = 727.6
    CD = 15
    TP成长 = 0.1
    TP上限 = 5

class 黑暗武士技能20(黑暗武士主动技能):
    名称 = '凝魂波动阵'
    类型 = '魔法'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 1875.171
    成长 = 211.829
    基础2 = 622.629
    成长2 = 70.371
    攻击次数2 = 7
    CD = 21
    TP成长 = 0.1
    TP上限 = 5

class 黑暗武士技能21(黑暗武士主动技能):
    名称 = '破魂斩'
    类型 = '物理'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 5072.219
    成长 = 572.781
    CD = 15
    TP成长 = 0.12
    TP上限 = 5

class 黑暗武士技能22(黑暗武士主动技能):
    名称 = '冥炎破空斩'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 2910.344
    成长 = 328.656
    攻击次数 = 2
    基础2 = 3495.281
    成长2 = 394.719
    攻击次数2 = 2
    基础3 = 116.813
    成长3 = 13.188
    攻击次数3 = 8
    CD = 47.2
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础2 *= 1.34
        self.成长2 *= 1.34
        self.基础3 *= 2.67 * 8
        self.成长3 *= 2.67 * 8
        self.攻击次数3 = 1

class 黑暗武士技能23(黑暗武士主动技能):
    名称 = '禁魂斩'
    类型 = '魔法'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 6510.781 * 1.1
    成长 = 735.219 * 1.1
    CD = 21
    TP成长 = 0
    TP上限 = 5


class 黑暗武士技能24(黑暗武士主动技能):
    名称 = '魔狱裂魂斩'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 338.733
    成长 = 38.267
    基础2 = 2372.067
    成长2 = 267.933
    攻击次数2 = 1
    基础3 = 1662.3
    成长3 = 187.7
    攻击次数3 = 6
    CD = 40
    TP成长 = 0.10
    TP上限 = 5

class 黑暗武士技能25(黑暗武士主动技能):
    名称 = '黑暗明王阵'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 1761.267
    成长 = 198.733
    攻击次数 = 4
    基础2 = 4085.4
    成长2 = 461.6
    攻击次数2 = 1
    CD = 47.2
    TP成长 = 0.10
    TP上限 = 5

class 黑暗武士技能26(黑暗武士主动技能):
    名称 = '魔影剑舞'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 647.033
    成长 = 72.967
    攻击次数 = 13
    基础2 = 1549.9
    成长2 = 175.1
    攻击次数2 = 3
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 0.5
        self.成长 *= 0.5
        self.基础2 = self.基础2 * 0.19 + self.基础2 * 1.30 + self.基础2 * 0.91 * 6 + self.基础2 * 0.96
        self.成长2 = self.成长2 * 0.19 + self.成长2 * 1.30 + self.成长2 * 0.91 * 6 + self.成长2 * 0.96
        self.攻击次数2 = 1

class 黑暗武士技能27(黑暗武士主动技能):
    名称 = '幽魂剑'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 19
    基础 = 173.056
    成长 = 32.944
    攻击次数 = 33
    基础2 = 5728.444
    成长2 = 1086.556
    攻击次数2 = 1
    CD = 45

class 黑暗武士技能28(黑暗武士主动技能):
    名称 = '暗炎冥魂波'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 16
    基础 = 2697.333
    成长 = 511.667
    攻击次数 = 5
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.21
        self.成长 *= 1.21
        self.CD *= 0.9

class 黑暗武士技能29(黑暗武士主动技能):
    名称 = '斩龙破'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 1561.647
    成长 = 176.353
    基础2 = 1561.647
    成长2 = 176.353
    攻击次数2 = 1
    基础3 = 14233.059
    成长3 = 1606.941
    攻击次数3 = 1
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.攻击次数 = 0
        self.攻击次数2 = 0
        self.基础3 *= 0.27
        self.成长3 *= 0.27
        self.攻击次数3 = 6
        self.CD *= 0.9

class 黑暗武士技能30(黑暗武士主动技能):
    名称 = '邪影升龙斩'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 39162.333
    成长 = 4421.667
    CD = 50

class 黑暗武士技能31(黑暗武士主动技能):
    名称 = '超时空碎裂'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 1793
    成长 = 542
    攻击次数 = 19
    基础2 = 34095
    成长2 = 10292
    攻击次数2 = 1
    CD = 180

class 黑暗武士技能32(被动技能):
    名称 = '暗·短剑精通'
    所在等级 = 15
    等级上限 = 40
    基础等级 = 30
    关联技能2 = ['所有']
    #物理攻击
    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '短剑':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.015, 5)

    #魔法攻击
    def 加成倍率2(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '短剑':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.0129, 5)

    #物理攻击力面板
    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '短剑':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.015, 5)

    #魔法攻击力面板
    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '短剑':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.0129, 5)

class 黑暗武士技能33(被动技能):
    名称 = '暗·太刀精通'
    所在等级 = 15
    等级上限 = 40
    基础等级 = 30
    关联技能2 = ['所有']
    # 物理攻击
    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '太刀':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.013, 5)

    # 魔法攻击
    def 加成倍率2(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '太刀':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.012, 5)

    # 物理攻击力面板
    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '太刀':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.013, 5)

    # 魔法攻击力面板
    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '太刀':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.012, 5)

class 黑暗武士技能34(被动技能):
    名称 = '暗·巨剑精通'
    所在等级 = 15
    等级上限 = 40
    基础等级 = 30
    关联技能2 = ['所有']
    # 物理攻击
    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '巨剑':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.012, 5)

    # 魔法攻击
    def 加成倍率2(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '巨剑':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.012, 5)

    # 物理攻击力面板
    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '巨剑':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.012, 5)

    # 魔法攻击力面板
    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '巨剑':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.012, 5)

class 黑暗武士技能35(被动技能):
    名称 = '暗·钝器精通'
    所在等级 = 15
    等级上限 = 40
    基础等级 = 30
    关联技能2 = ['所有']
    # 物理攻击
    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '钝器':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.012, 5)

    # 魔法攻击
    def 加成倍率2(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '钝器':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.012, 5)

    # 物理攻击力面板
    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '钝器':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.012, 5)

    # 魔法攻击力面板
    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '钝器':
            return 1.0
        else:
            return round(1.00 + self.等级 * 0.012, 5)

class 黑暗武士技能36(被动技能):
    名称 = '暗·光剑精通'
    所在等级 = 15
    等级上限 = 40
    基础等级 = 30
    关联技能2 = ['所有']
    # 物理攻击
    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '光剑':
            return 1.0
        else:
            return round(1.02 + self.等级 * 0.013, 5)

    # 魔法攻击
    def 加成倍率2(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '光剑':
            return 1.0
        else:
            return round(1.02 + self.等级 * 0.013, 5)

    # 物理攻击力面板
    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '光剑':
            return 1.0
        else:
            return round(1.02 + self.等级 * 0.013, 5)

    # 魔法攻击力面板
    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '光剑':
            return 1.0
        else:
            return round(1.02 + self.等级 * 0.013, 5)

class 黑暗武士技能37(被动技能):
    名称 = '时间停滞'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 <= 15:
            return round(1.045 + 0.01 * self.等级, 5)
        else:
            return round(0.97 + 0.015 * self.等级, 5)

class 黑暗武士技能38(被动技能):
    名称 = '次元融合'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['无']
    def 力智倍率(self):
        return round(1 + 0.02 * self.等级, 5)
        #每级2%力智

class 黑暗武士技能39(被动技能):
    名称 = '自我觉醒'
    所在等级 = 75
    等级上限 = 1
    基础等级 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.01 + 0.1 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.01 + self.等级 * 0.1, 5)

    # 魔法攻击力面板
    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.01 + self.等级 * 0.1, 5)

class 黑暗武士技能40(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 黑暗武士技能41(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 黑暗武士技能42(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['超时空碎裂']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

class 黑暗武士技能43(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['挑击']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

黑暗武士技能列表 = []
i = 0
while i >= 0:
    try:
        exec('黑暗武士技能列表.append(黑暗武士技能'+str(i)+'())')
        i += 1
    except:
        i = -1

黑暗武士技能序号 = dict()
for i in range(len(黑暗武士技能列表)):
    黑暗武士技能序号[黑暗武士技能列表[i].名称] = i


黑暗武士二觉序号 = 0
黑暗武士三觉序号 = 0
for i in 黑暗武士技能列表:
    if i.所在等级 == 85:
        黑暗武士二觉序号 = 黑暗武士技能序号[i.名称]
    if i.所在等级 == 100:
        黑暗武士三觉序号 = 黑暗武士技能序号[i.名称]

黑暗武士护石选项 = ['无']
for i in 黑暗武士技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        黑暗武士护石选项.append(i.名称)

黑暗武士符文选项 = ['无']
for i in 黑暗武士技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        黑暗武士符文选项.append(i.名称)

class 黑暗武士角色属性(角色属性):

    职业名称 = '黑暗武士'

    武器选项 = ['光剑','太刀','巨剑','短剑','钝器']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['物理百分比','魔法百分比']
    
    #默认
    伤害类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量','智力']

    主BUFF = 1.54
   
    #基础属性(含唤醒)
    基础力量 = 906.0
    基础智力 = 844.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    远古记忆 = 0
    
    #计算CD
    排列技能 = ['无', '无', '无', '无', '无'] * 6

    def __init__(self):
        self.技能栏= deepcopy(黑暗武士技能列表)
        self.技能序号= deepcopy(黑暗武士技能序号)

    def 被动倍率计算(self):
        for i in ['暗·太刀精通','暗·短剑精通','暗·巨剑精通','暗·光剑精通','暗·钝器精通']:
            if self.武器类型 not in i:
                self.技能栏[self.技能序号[i]].关联技能 = ['无']

        for i in self.技能栏:
            if i.关联技能 != ['无']:
                if i.关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            # 分物理魔法 调用武器精通的加成倍率
                            if i.名称 in ['暗·太刀精通','暗·短剑精通','暗·巨剑精通','暗·光剑精通','暗·钝器精通']:
                                if j.类型 == '物理':
                                    j.被动倍率 *= i.加成倍率(self.武器类型)
                                else:
                                    j.被动倍率 *= i.加成倍率2(self.武器类型)
                            else:
                                j.被动倍率 *= i.加成倍率(self.武器类型)
                else :
                    for k in i.关联技能:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率(self.武器类型)

    def 伤害指数计算(self):
        
        防御 = max(防御输入 - self.固定减防, 0) * (1 - self.百分比减防)
        基准倍率 = 1.5 * self.主BUFF * (1 - 防御 / (防御+ 20000))

        self.火属性强化 += int((self.火属性强化 - 22) * self.百分比属强)
        self.冰属性强化 += int((self.冰属性强化 - 22) * self.百分比属强)
        self.光属性强化 += int((self.光属性强化 - 22) * self.百分比属强)
        self.暗属性强化 += int((self.暗属性强化 - 22) * self.百分比属强)

        if self.攻击属性 == 0:
            属性倍率=1.05+0.0045*max(self.火属性强化 - 火抗输入,self.冰属性强化 - 冰抗输入,self.光属性强化 - 光抗输入,self.暗属性强化 - 暗抗输入)
        elif self.攻击属性 == 1:
            属性倍率=1.05+0.0045*(self.火属性强化 - 火抗输入)
        elif self.攻击属性 == 2:
            属性倍率=1.05+0.0045*(self.冰属性强化 - 冰抗输入)
        elif self.攻击属性 == 3:
            属性倍率=1.05+0.0045*(self.光属性强化 - 光抗输入)
        elif self.攻击属性 == 4:
            属性倍率=1.05+0.0045*(self.暗属性强化 - 暗抗输入)

        if self.红色宠物装备 == '自适应':
            self.宠物装备判断(属性倍率)

        面板1 = int((self.面板力量()/250+1) * (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻))
        面板2 = int((self.面板智力()/250+1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻))

        增伤倍率=1+self.伤害增加
        增伤倍率*=1+self.暴击伤害
        增伤倍率*=1+self.最终伤害
        增伤倍率*=self.技能攻击力
        增伤倍率*=1+self.持续伤害*(1-0.1*self.持续伤害计算比例)
        增伤倍率*=1+self.附加伤害+self.属性附加*属性倍率
        self.伤害指数1=面板1*属性倍率*增伤倍率*基准倍率/100
        self.伤害指数2=面板2*属性倍率*增伤倍率*基准倍率/100

    def CD倍率计算(self):
        super().CD倍率计算()
        for i in self.排列技能:
            count = 0
            总CD = 0
            for j in i:
                if j != '无':
                    count += 1
                    总CD += self.技能栏[self.技能序号[j]].等效CD(self.武器类型)
            if count != 0:
                计算CD = 总CD / count * 1.2
                for j in i:
                    if j != '无':
                        self.技能栏[self.技能序号[j]].计算CD = 计算CD

    def 伤害计算(self, x = 0):
        
        self.所有属性强化(self.进图属强)
        # Will添加
        self.CD倍率计算()
        self.加算冷却计算()

        self.被动倍率计算()
        self.伤害指数计算()

        技能释放次数=[]
        技能单次伤害=[]
        技能总伤害=[]
    
        #技能单次伤害计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                # 分物理魔法 乘伤害指数
                if i.类型 == '物理':
                    技能单次伤害.append(i.等效百分比(self.武器类型)*self.伤害指数1*i.被动倍率)
                else:
                    技能单次伤害.append(i.等效百分比(self.武器类型)*self.伤害指数2*i.被动倍率)
            else:
                技能单次伤害.append(0)
      
        #技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                if self.次数输入[self.技能序号[i.名称]] =='/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型) + 1 +i.基础释放次数))
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)
    
        #单技能伤害合计
    
        for i in self.技能栏:
            if i.是否有伤害==1 and 技能释放次数[self.技能序号[i.名称]] != 0:
                技能总伤害.append(技能单次伤害[self.技能序号[i.名称]]*技能释放次数[self.技能序号[i.名称]]*(1+self.白兔子技能*0.20+self.年宠技能*0.10*self.宠物次数[self.技能序号[i.名称]]/技能释放次数[self.技能序号[i.名称]]+self.斗神之吼秘药*0.12))
            else:
                技能总伤害.append(0)
    
        总伤害=0
        for i in self.技能栏:
            总伤害+=技能总伤害[self.技能序号[i.名称]]
        
        if x==0:
            return 总伤害
    
        if x==1:
            详细数据=[]
            for i in range(0,len(self.技能栏)):
                详细数据.append(技能释放次数[i])
                详细数据.append(技能总伤害[i])
                if 技能释放次数[i]!=0:
                    详细数据.append(技能总伤害[i]/技能释放次数[i])
                else:
                    详细数据.append(0)
                if 总伤害!=0:
                    详细数据.append(技能总伤害[i]/总伤害*100)
                else:
                    详细数据.append(0)
            return 详细数据

    def 站街力量(self):
        return int(max(self.力量, self.智力) * self.技能栏[self.技能序号['次元融合']].力智倍率())

    def 站街智力(self):
        return self.站街力量()

    def 面板力量(self):
        if self.系统奶 == False:
            return int(int((self.力量 + self.进图力量)) * (1 + self.百分比力智) * self.技能栏[self.技能序号['次元融合']].力智倍率())
        else:
            return int(int((self.力量 + int((self.力量 - self.基础力量) * 1.35 + 7664) +self.进图力量)) * (1 + self.百分比力智) * self.技能栏[self.技能序号['次元融合']].力智倍率())

    def 面板智力(self):
        return self.面板力量()

class 黑暗武士(角色窗口):

    def 窗口属性输入(self):
        self.初始属性 = 黑暗武士角色属性()
        self.角色属性A = 黑暗武士角色属性()
        self.角色属性B = 黑暗武士角色属性()
        self.一觉序号 = 黑暗武士二觉序号
        self.二觉序号 = 黑暗武士二觉序号
        self.三觉序号 = 黑暗武士三觉序号
        self.护石选项 = deepcopy(黑暗武士护石选项)
        self.符文选项 = deepcopy(黑暗武士符文选项)

    def 界面(self):
        super().界面()

        for i in [self.觉醒选择, self.一觉图片, self.二觉图片, self.一觉遮罩, self.二觉遮罩]:
            i.move(-1000, -1000)

        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.所在等级 == 50:
                self.等级调整[序号].clear()
                for j in range(- i.基础等级, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
        
        初始x = 310; 初始y = 640
        self.技能排列=QLabel(self.main_frame2)
        self.技能排列.setPixmap(QPixmap('./ResourceFiles/'+self.角色属性A.职业名称 + "/技能/skill.png"))
        self.技能排列.resize(242, 293)
        self.技能排列.move(初始x, 初始y)

        技能名称 = ['无']
        for i in self.初始属性.技能栏:
            if i.是否主动 == 1:
                技能名称.append(i.名称)

        self.技能排列 = []
        self.排列图片 = []
        for i in range(6):
            temp = []
            temp2 = []
            for j in range(6):
                temp.append(MyQComboBox(self.main_frame2))
                temp[j].resize(100, 22)
                temp[j].addItems(技能名称)
                temp[j].currentIndexChanged.connect(lambda state, x = i, y = j:self.排列图片更改(x, y))
                if i == 0:
                    temp[j].move(310 + 110 * j, 440 + 28 * i)
                else:
                    temp[j].move(310 + 110 * j, 450 + 28 * i)
                temp2.append(QLabel(self.main_frame2))
                temp2[j].resize(26, 26)
                temp2[j].setAlignment(Qt.AlignCenter) 
                if i == 0:
                    temp2[j].move(初始x + 10 + 39 * j, 初始y + 24 + 44 * i)
                else:
                    temp2[j].move(初始x + 10 + 39 * j, 初始y + 39 + 44 * i)
            self.技能排列.append(temp)
            self.排列图片.append(temp2)

        self.清空排列按钮 = QPushButton('清空排列', self.main_frame2)
        self.清空排列按钮.clicked.connect(lambda state: self.清空排列())
        self.清空排列按钮.move(850, 660)
        self.清空排列按钮.resize(100, 30)
        self.清空排列按钮.setStyleSheet(按钮样式)

        self.护甲精通选择=MyQComboBox(self.main_frame2)
        self.护甲精通选择.addItem('轻甲')
        self.护甲精通选择.addItem('布甲')
        self.护甲精通选择.addItem('重甲')
        self.护甲精通选择.addItem('板甲')
        self.护甲精通选择.resize(120,20)
        self.护甲精通选择.move(720,665)

    def 清空排列(self):

        box = QMessageBox(QMessageBox.Warning, "提示", "是否清空排列？")
        box.setWindowIcon(self.icon)
        yes = box.addButton(self.tr("确定"), QMessageBox.YesRole)
        no = box.addButton(self.tr("取消"), QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton() == yes:
            for i in self.技能排列:
                for j in i:
                    j.setCurrentIndex(0)
        
    def 排列图片更改(self, x, y):
        技能字典 = {}
        for i in self.技能排列:
            for j in i:
                if j.currentText() != '无':
                    技能字典[j.currentText()] = 技能字典.get(j.currentText(), 0) + 1

        if self.技能排列[x][y].currentText() != '无':
            self.排列图片[x][y].setPixmap(self.技能图片[self.角色属性A.技能序号[self.技能排列[x][y].currentText()]])
            if 技能字典[self.技能排列[x][y].currentText()] > 1:
                self.技能排列[x][y].setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(225,5,65,0.8)} QComboBox QAbstractItemView::item {height: 18px;}")
            else:
                self.技能排列[x][y].setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(65,105,225,0.8)} QComboBox QAbstractItemView::item {height: 18px;}")
        else:
            self.排列图片[x][y].setPixmap(QPixmap('无'))
            self.技能排列[x][y].setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(65,105,225,0.8)} QComboBox QAbstractItemView::item {height: 18px;}")
    
    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性)

        排列倍率 = [2.0, 1.0, 1.3, 1.5, 1.8, 2.0]

        for i in range(6):
            for j in range(6):
                if self.技能排列[i][j].currentText() != '无':
                    属性.技能栏[属性.技能序号[self.技能排列[i][j].currentText()]].倍率 *= 排列倍率[i]

        排列技能 = []
        for j in range(6):
            temp = []
            for i in range(1, 6):
                temp.append(self.技能排列[i][j].currentText())
            排列技能.append(temp)
            
        属性.排列技能 = deepcopy(排列技能)

        for i in self.初始属性.技能栏:
            if i.是否主动 == 1 and i.所在等级 >= 40:
                if 属性.伤害类型 == '物理百分比':
                    i.类型 = '物理'
                else:
                    i.类型 = '魔法'

        #防具类型 = '轻甲'

        属性.护甲精通 = self.护甲精通选择.currentIndex()
        if 属性.护甲精通 == 0:
            属性.防具类型 = '轻甲'
            属性.防具精通属性 = ['力量']
        if 属性.护甲精通 == 1:
            属性.防具类型 = '布甲'
            属性.防具精通属性 = ['智力']
        if 属性.护甲精通 == 2:
            属性.防具类型 = '重甲'
            属性.防具精通属性 = ['力量']
        if 属性.护甲精通 == 3:
            属性.防具类型 = '板甲'
            属性.防具精通属性 = ['智力']

    def 载入配置(self, path = 'set'):
        super().载入配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/skill4.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(6):
                for j in range(6):
                    self.技能排列[i][j].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1

            self.护甲精通选择.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

    def 保存配置(self, path = 'set'):
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.职业名称 + '/' + path + '/skill4.ini', 'w', encoding='utf-8')
            for i in range(6):
                for j in range(6):
                    setfile.write(str(self.技能排列[i][j].currentIndex())+'\n')
            setfile.write(str(self.护甲精通选择.currentIndex())+'\n')
        except:
            pass


