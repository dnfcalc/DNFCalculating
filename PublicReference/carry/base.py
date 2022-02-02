from PublicReference.equipment.equ_list import *
from PublicReference.equipment.称号 import *
from PublicReference.equipment.宠物 import *
from PublicReference.equipment.辟邪玉 import *
from PublicReference.equipment.武器融合 import *
from PublicReference.equipment.冒险家名望 import *
from PublicReference.choise.选项设置 import *
from PublicReference.choise.细节选项 import *
from PublicReference.common import *
from PublicReference.utils.uniqueCode import get_mac_address
import operator

from PublicReference.utils.common import format_range, to_percent

等级 = 100


class 技能:
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    等级 = 0
    基础等级 = 0
    等级溢出 = 0
    自定义描述 = 0
    学习间隔 = 1
    等级精通 = 60
    基础等级 = 0

    关联技能 = ['无']
    关联技能2 = ['无']
    关联技能3 = ['无']
    非关联技能 = ['无']
    非关联技能2 = ['无']
    非关联技能3 = ['无']
    冷却关联技能 = ['无']
    冷却关联技能2 = ['无']
    冷却关联技能3 = ['无']
    非冷却关联技能 = ['无']
    非冷却关联技能2 = ['无']
    非冷却关联技能3 = ['无']

    版本 = 装备版本

    def 等级加成(self, x):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                if self.基础等级 != self.等级上限 and self.关联技能 != ['无']:
                    self.等级溢出 = 1
            else:
                self.等级 += x

    def 基础等级计算(self):
        pass


class 主动技能(技能):
    # 只扩展了技能的三条属性，第一条技能hit默认1,2、3条hit默认为0，需要手动赋值
    # 如果需要继续扩展，可以在各自职业类内继承后自行扩展，同时需要重写下等效百分比函数
    # 固伤在填写基础及成长的时候需要注意，技能面板/独立得到的成长及数值需要*100
    基础 = 0.0
    成长 = 0.0
    攻击次数 = 1.0
    基础2 = 0.0
    成长2 = 0.0
    攻击次数2 = 0.0
    基础3 = 0.0
    成长3 = 0.0
    攻击次数3 = 0.0
    CD = 0.0
    TP成长 = 0.0
    TP上限 = 0
    TP等级 = 0
    是否主动 = 1
    是否有伤害 = 1
    恢复 = 1.0
    倍率 = 1.0
    被动倍率 = 1.0
    基础释放次数 = 0
    演出时间 = 0
    是否有护石 = 0
    护石选项 = ['魔界']

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int(
                (self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 *
                 (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 *
                 (self.基础3 + self.成长3 * self.等级)) *
                (1 + self.TP成长 * self.TP等级) * self.倍率)

    def 等效CD(self, 武器类型, 输出类型):
        return round(self.CD / self.恢复 * 武器冷却惩罚(武器类型, 输出类型, self.版本), 1)

    def 基础等级计算(self):
        if self.基础等级 == 0:
            # 契约等级+5
            self.基础等级 = min(int((等级 + 5 - self.所在等级) / self.学习间隔 + 1),
                            self.等级精通)


class 被动技能(技能):
    是否主动 = 0
    是否有伤害 = 0
    关联技能 = ['所有']

    def 基础等级计算(self):
        if self.基础等级 == 0:
            # 契约等级+5
            self.基础等级 = min(int((等级 + 5 - self.所在等级) / self.学习间隔 + 1),
                            self.等级精通)


符文效果选项 = [
    '无',
    trans('{攻击}+5%,CD+3%'), 'CD-4%',
    trans('{攻击}+3%'),
    trans('{攻击}-3%,CD-6%'),
    trans('{攻击}+3%,CD+2%'), 'CD-3%',
    trans('{攻击}+2%'),
    trans('{攻击}-2%,CD-4%'),
    trans('{攻击}+2%,CD+1%'), 'CD-2%',
    trans('{攻击}+1%'),
    trans('{攻击}-1%,CD-3%'),
    trans('{攻击}+6%,CD+4%'), 'CD-5%',
    trans('{攻击}+4%'),
    trans('{攻击}-4%,CD-7%')
]

刀魂之卡赞数据 = [
    0, 31, 40, 48, 58, 67, 79, 90, 103, 116, 131, 145, 161, 178, 194, 212, 230,
    250, 270, 292, 313
]


class 角色属性(属性):
    # region 属性变量
    职业分类 = '输出'
    主BUFF = 1.0
    系统奶系数 = 0
    系统奶基数 = 0
    年宠技能 = False
    白兔子技能 = False
    斗神之吼秘药 = False
    称号触发 = False

    屏蔽三觉 = False

    超卓之心等级 = 1
    觉醒之抉择技能 = ''

    物理攻击力 = 65
    魔法攻击力 = 65
    独立攻击力 = 1045
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13

    进图物理攻击力 = 0
    进图魔法攻击力 = 0
    进图独立攻击力 = 0
    进图属强 = 0

    # 红阵，远古记忆 -1表示没有该技能
    远古记忆 = -1
    刀魂之卡赞 = -1

    百分比力智 = 0.0
    百分比三攻 = 0.0
    伤害增加 = 0.0
    黄字 = 0.0  # 冲突属性
    附加伤害 = 0.0
    属性附加 = 0.0
    暴击伤害 = 0.0
    暴伤 = 0.0  # 冲突属性
    最终伤害 = 0.0
    技能攻击力 = 1.0
    技能攻击力累加 = 0.0
    # 技能攻击力显示 = 1.0
    持续伤害 = 0.0
    加算冷却缩减 = 0.0
    百分比减防 = 0.0
    固定减防 = 0
    词条提升率 = [0] * 6
    词条选择 = []

    # 队友增幅系数
    队友增幅系数 = 1.0

    防御输入 = 0
    火抗输入 = 0
    冰抗输入 = 0
    光抗输入 = 0
    暗抗输入 = 0

    攻击速度 = 0.00
    移动速度 = 0.00
    施放速度 = 0.00
    命中率 = 0.0
    回避率 = 0.0
    物理暴击率 = 0.00
    魔法暴击率 = 0.00

    自适应选项 = [0] * 2
    自适应描述 = ['无'] * 2

    时间输入 = 0
    次数输入 = []
    宠物次数 = []
    技能切装 = []
    装备切装 = []
    开启切装 = 0
    切装修正 = []

    转甲选项 = 0

    希洛克武器词条 = 0
    武器词条触发 = 0

    # 0英雄 1传说
    角色熟练度 = 0
    # 0 1 2 3 4 5 6
    技能栏空位 = 6
    # 0数学期望 1黄字+35% 2暴伤+35% 3白字+35% 4终伤+35% 5三攻+35%
    命运的抉择 = 0
    # 0数学期望 123456
    天命无常 = 0
    # 0数学期望 1 HP高于70% 2 HP在70~30% 3 HP低于30%
    悲剧的残骸 = 0
    # 0数学期望 1 5%属性附加 2 10%技能攻击力 3 15%技能攻击力
    先知者的预言 = 0
    # 0无霸体状态 1 霸体状态 2 无伤状态
    贫瘠沙漠的遗产 = 1
    # 0数学期望 1 7效果 2 77效果 3 777效果
    幸运三角 = 0
    # 0过充电状态 1过负荷状态
    擎天战甲 = 0
    # 0.00~1.00
    持续伤害计算比例 = 0
    # 0 120+ 1 120-100 2 100-80 3 80-60 4 60-40 5 40-
    军神的隐秘遗产 = 0
    # 0太极天帝剑：阳  1太极天帝剑：阴
    太极天帝剑 = 0
    # 0绿色生命的面容：无  1绿色生命的面容：阴暗面
    绿色生命的面容 = 1
    # 0噙毒手套：中毒  1噙毒手套：未中毒
    噙毒手套 = 0

    攻击属性 = 0
    产物升级 = 0

    # 是否为图内状态
    状态 = 0
    # 是否为输出装备描述
    装备描述 = 0

    # 辟邪玉属性
    附加伤害增加增幅 = 1.0
    属性附加伤害增加增幅 = 1.0
    技能伤害增加增幅 = 1.0
    暴击伤害增加增幅 = 1.0
    伤害增加增幅 = 1.0
    最终伤害增加增幅 = 1.0
    力量智力增加增幅 = 1.0
    物理魔法攻击力增加增幅 = 1.0
    所有属性强化增加 = 1.0

    # 0武器，1首饰，2特殊，3防具
    变换词条 = [
        # 原词条类型，原词条数值，可洗最小值，可洗最大值，择优不考虑觉醒
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    计算自适应 = 1
    # 计算自适应方式 = 0
    输出提升率 = 0

    def getskillinfo(self):
        return self.技能栏

    # endregion

    # region 词条属性
    def 附加伤害加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans('{附加伤害} +$value<br>', value=to_percent(x))
        else:
            self.附加伤害 += self.附加伤害增加增幅 * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.变换词条[可变 - 1] = [
                    3,
                    round(x * 100),
                    round(x * 100) + (2 if 可变 > 1 else 4),
                    round(x * 100) + (8 if 可变 > 1 else 16)
                ]
        return ''

    def 三攻固定加成(self, x=0, y=0, z=0):
        if self.装备描述 == 1:
            return trans('{物攻/魔攻/独立} +$value<br>', value=x)
        else:
            if y == 0 or z == 0:
                y = x
                z = x
            self.物理攻击力 += x
            self.魔法攻击力 += y
            self.独立攻击力 += z
        return ''

    def 力智固定加成(self, x=0, y=0):
        if self.装备描述 == 1:
            return trans('{力量、智力} +$value<br>', value=x)
        else:
            if y == 0:
                y = x
            self.力量 += x
            self.智力 += y
        return ''

    def 持续伤害加成(self, x):
        if self.装备描述 == 1:
            return trans('{持续伤害} +$value<br>', value=to_percent(x))
        else:
            self.持续伤害 += x
        return ''

    def 属性附加加成(self, x):
        if self.装备描述 == 1:
            return trans('{属性附加伤害} +$value<br>', value=to_percent(x))
        else:
            self.属性附加 += self.属性附加伤害增加增幅 * x
        return ''

    def 技能攻击力加成(self, x, 辟邪玉加成=1,适用累加=1):
        if self.装备描述 == 1:
            return trans('{技能攻击力} +$value<br>', value=to_percent(x))
        if 适用累加 == 0:
            self.技能攻击力 *= 1 + self.技能伤害增加增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.技能攻击力累加 += x
            if self.技能攻击力累加 <= 2:
                self.技能攻击力 *= 1 + self.技能伤害增加增幅 * x if 辟邪玉加成 == 1 else x
            else:
                self.技能攻击力 *= 1 + (self.技能伤害增加增幅*(2+x-self.技能攻击力累加)+self.技能攻击力累加-2) if self.技能攻击力累加 - x < 2  or 辟邪玉加成 == 1 else x
        return ''

    def 暴击伤害加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans('{暴击伤害} +$value<br>', value=to_percent(x))
        else:
            self.暴击伤害 += self.暴击伤害增加增幅 * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.变换词条[可变 - 1] = [
                    4,
                    round(x * 100),
                    round(x * 100) + (2 if 可变 > 1 else 4),
                    round(x * 100) + (8 if 可变 > 1 else 16)
                ]
        return ''

    def 伤害增加加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans('{伤害增加} +$value<br>', value=to_percent(x))
        else:
            self.伤害增加 += self.伤害增加增幅 * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.变换词条[可变 - 1] = [
                    2,
                    round(x * 100),
                    round(x * 100) + (2 if 可变 > 1 else 4),
                    round(x * 100) + (8 if 可变 > 1 else 16)
                ]
        return ''

    def 最终伤害加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans('{最终伤害} +$value<br>', value=to_percent(x))
        else:
            self.最终伤害 += self.最终伤害增加增幅 * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.变换词条[可变 - 1] = [
                    5,
                    round(x * 100),
                    round(x * 100) + (2 if 可变 > 1 else 4),
                    round(x * 100) + (8 if 可变 > 1 else 16)
                ]
        return ''

    def 百分比力智加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans('{力量、智力} +$value<br>', value=to_percent(x))
        else:
            self.百分比力智 += self.力量智力增加增幅 * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.变换词条[可变 - 1] = [
                    0,
                    round(x * 100),
                    round(x * 100) + (2 if 可变 > 1 else 4),
                    round(x * 100) + (8 if 可变 > 1 else 16)
                ]
        return ''

    def 百分比三攻加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans('{物攻、魔攻、独立} +$value<br>', value=to_percent(x))
        else:
            self.百分比三攻 += self.物理魔法攻击力增加增幅 * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.变换词条[可变 - 1] = [
                    1,
                    round(x * 100),
                    round(x * 100) + (2 if 可变 > 1 else 4),
                    round(x * 100) + (8 if 可变 > 1 else 16)
                ]
        return ''

    def 火属性强化加成(self, x, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans("{火属性强化} +$value<br>", value=x)
        else:
            if self.状态 == 0:
                self.火属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
            else:
                self.火属性强化 += int(self.所有属性强化增加 * x)
        return ''

    def 冰属性强化加成(self, x, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans("{冰属性强化} +$value<br>", value=x)
        else:
            if self.状态 == 0:
                self.冰属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
            else:
                self.冰属性强化 += int(self.所有属性强化增加 * x)
        return ''

    def 光属性强化加成(self, x, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans("{光属性强化} +$value<br>", value=x)
        else:
            if self.状态 == 0:
                self.光属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
            else:
                self.光属性强化 += int(self.所有属性强化增加 * x)
        return ''

    def 暗属性强化加成(self, x, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans("{暗属性强化} +$value<br>", value=x)
        else:
            if self.状态 == 0:
                self.暗属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
            else:
                self.暗属性强化 += int(self.所有属性强化增加 * x)
        return ''

    def 所有属性强化加成(self, x, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans("{所有属性强化} +$value<br>", value=x)
        else:
            if self.状态 == 0:
                temp = self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
            else:
                temp = int(self.所有属性强化增加 * x)
            self.所有属性强化(temp)
        return ''

    def 攻击速度增加(self, x):
        if self.装备描述 == 1:
            return trans("{攻击速度} +$value<br>", value=to_percent(x, 2))
        else:
            self.攻击速度 += x
        return ''

    def 移动速度增加(self, x):
        if self.装备描述 == 1:
            return trans("{移动速度} +$value<br>", value=to_percent(x, 2))
        else:
            self.移动速度 += x
        return ''

    def 施放速度增加(self, x):
        if self.装备描述 == 1:
            return trans("{释放速度} +$value<br>", value=to_percent(x, 2))
        else:
            self.施放速度 += x
        return ''

    def 命中率增加(self, x):
        if self.装备描述 == 1:
            return trans("{命中率} +$value<br>", value=to_percent(x, 1))
        else:
            self.命中率 += x
        return ''

    def 物理暴击率增加(self, x):
        if self.装备描述 == 1:
            return trans("{物理暴击率} +$value<br>", value=to_percent(x))
        else:
            self.物理暴击率 += x
        return ''

    def 魔法暴击率增加(self, x):
        if self.装备描述 == 1:
            return trans("{魔法暴击率} +$value<br>", value=to_percent(x))
        else:
            self.魔法暴击率 += x
        return ''

    def 技能等级加成(self, 加成类型, minLv, maxLv, lv, 可变=0):
        lv = int(lv)
        if self.装备描述 == 1:
            label = trans('技能等级' if 加成类型 == '所有' else '主动技能等级')
            if minLv == maxLv:
                return ("Lv{} {}+{}<br>").format(minLv, label, lv)
            return ("Lv{}-{} {}+{}<br>").format(minLv, maxLv, label, lv)
        else:
            if self.远古记忆 > 0:
                if minLv <= 15 and maxLv >= 15:
                    self.远古记忆 = min(20, self.远古记忆 + lv)

            if self.刀魂之卡赞 > 0:
                if minLv <= 5 and maxLv >= 5:
                    self.刀魂之卡赞 = min(20, self.刀魂之卡赞 + lv)

            for i in self.技能栏:
                if i.所在等级 >= minLv and i.所在等级 <= maxLv:
                    if 加成类型 == '所有':
                        i.等级加成(lv)
                    else:
                        if i.是否主动 == 1:
                            i.等级加成(lv)
            if 可变 > 0:
                self.变换词条[可变 - 1] = [
                    6, 2, 14 + (2 if 可变 > 1 else 4), 14 + (8 if 可变 > 1 else 16)
                ]
        return ''

    def 武器装扮等级加成(self, Lv, lv):
        lv = int(lv)
        for i in self.技能栏:
            if i.所在等级 == Lv and i.是否主动 == 1 and i.名称 not in [
                    "念兽龙虎啸", "风雷啸", "圣灵符文", "神圣之光"
            ]:
                i.等级加成(lv)

    def 技能冷却缩减(self, min, max, x):
        if self.装备描述 == 1:
            label = trans('技能')
            if min == max:
                return ("Lv{} {}CD -{}<br>").format(min, label, to_percent(x))
            else:
                return ("Lv{}-{} {}CD -{}<br>").format(min, max, label,
                                                       to_percent(x))
        else:
            for i in self.技能栏:
                if i.所在等级 >= min and i.所在等级 <= max:
                    if i.是否有伤害 == 1:
                        i.CD *= (1 - x)
        return ''

    def 技能恢复加成(self, min, max, x):
        if self.装备描述 == 1:
            label = trans('技能恢复')
            if min == max:
                return "Lv{} {}+{}%<br>".format(min, label, round(x * 100))
            else:
                return "Lv{}-{} {}+{}%<br>".format(min, max, label,
                                                   round(x * 100))
        else:
            for i in self.技能栏:
                if i.所在等级 >= min and i.所在等级 <= max:
                    if i.是否有伤害 == 1:
                        i.恢复 += x
        return ''

    def 进图属强加成(self, x, 辟邪玉加成=1):
        if self.装备描述 == 1:
            return trans('{进图属性强化} +$value<br>', value=x)
        else:
            self.进图属强 += int(self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x)
        return ''

    def 技能倍率加成(self, lv, x):
        if self.装备描述 == 1:
            return trans("Lv$level {技能攻击力} +$value<br>",
                         level=lv,
                         value=to_percent(x))
        else:
            for i in self.技能栏:
                if i.所在等级 == lv:
                    if i.是否有伤害 == 1:
                        i.倍率 *= (1 + x * self.技能伤害增加增幅)
        return ''

    def 单技能修改(self, 名称, 倍率, CD):
        if self.装备描述 == 1:
            tem = ""
            if 倍率 != 1:
                tem += trans("[{$name}]{攻击力} +$value<br>",
                             name=名称,
                             value=to_percent(倍率 - 1))
            if CD != 1:
                tem += trans("[{$name}]{CD} +$value<br>",
                             name=名称,
                             value=to_percent(CD - 1))
            return tem
        else:
            for i in self.技能栏:
                if i.是否有伤害 == 1:
                    if i.名称 == 名称:
                        i.倍率 *= 倍率
                        i.CD *= CD
        return ''

    def 所有属性强化(self, x):
        self.火属性强化 += x
        self.冰属性强化 += x
        self.光属性强化 += x
        self.暗属性强化 += x

    # endregion

    # region 面板计算
    def 防具精通计算(self, i):
        temp = equ.get_equ_by_name(self.装备栏[i])
        if temp.等级 == 100:
            if temp.所属套装 != '智慧产物':
                return 精通计算(temp.等级, temp.品质, self.强化等级[i], 部位列表[i])
            else:
                return 精通计算(temp.等级, temp.品质, self.改造等级[i], 部位列表[i])
        elif temp.等级 > 85:
            计算等级 = temp.等级
            if temp.所属套装 == '兵法之神':
                if self.装备检查('过往时光的轮回'):
                    计算等级 = 100
            return 精通计算(计算等级, temp.品质, self.强化等级[i], 部位列表[i])
        else:
            计算等级 = temp.等级
            if temp.所属套装 == '战术之王的御敌':
                if self.装备检查('战术之王的战术指挥棒'):
                    计算等级 = 100
            elif temp.所属套装 == '魔战无双':
                if self.装备检查('聚魔漩涡'):
                    计算等级 = 100
            x = 精通计算(计算等级, temp.品质, self.强化等级[i], 部位列表[i])
            if self.转甲选项 == 1:
                return round(x, 2)
            else:
                return round(0.4 * x, 2)

    def 站街力量(self):
        return int(self.力量)

    def 站街智力(self):
        return int(self.智力)

    def 面板力量(self):
        return (self.力量 + int((self.力量 - self.基础力量) * self.系统奶系数 + self.系统奶基数)
                + self.进图力量) * (1 + self.百分比力智)

    def 面板智力(self):
        return (self.智力 + int((self.智力 - self.基础智力) * self.系统奶系数 + self.系统奶基数)
                + self.进图智力) * (1 + self.百分比力智)

    def 站街物理攻击力倍率(self):
        站街物理攻击倍率 = 1.0
        for i in self.技能栏:
            try:
                站街物理攻击倍率 *= i.物理攻击力倍率(self.武器类型)
            except:
                pass
        return 站街物理攻击倍率

    def 站街魔法攻击力倍率(self):
        站街魔法攻击倍率 = 1.0
        for i in self.技能栏:
            try:
                站街魔法攻击倍率 *= i.魔法攻击力倍率(self.武器类型)
            except:
                pass
        return 站街魔法攻击倍率

    def 站街独立攻击力倍率(self):
        站街独立攻击倍率 = 1.0
        for i in self.技能栏:
            try:
                站街独立攻击倍率 *= i.独立攻击力倍率(self.武器类型)
            except:
                pass
        return 站街独立攻击倍率

    def 站街物理攻击力(self):
        return self.物理攻击力 * self.站街物理攻击力倍率()

    def 站街魔法攻击力(self):
        return self.魔法攻击力 * self.站街魔法攻击力倍率()

    def 站街独立攻击力(self):
        return self.独立攻击力 * self.站街独立攻击力倍率()

    def 面板物理攻击力(self):
        面板物理攻击 = (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻) * (
            1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        for i in self.技能栏:
            try:
                面板物理攻击 *= i.物理攻击力倍率进图(self.武器类型)
            except:
                pass
        return 面板物理攻击 * self.站街物理攻击力倍率()

    def 面板魔法攻击力(self):
        面板魔法攻击 = (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻) * (
            1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        for i in self.技能栏:
            try:
                面板魔法攻击 *= i.魔法攻击力倍率进图(self.武器类型)
            except:
                pass
        return 面板魔法攻击 * self.站街魔法攻击力倍率()

    def 面板独立攻击力(self):
        面板独立攻击 = (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻)
        for i in self.技能栏:
            try:
                面板独立攻击 *= i.独立攻击力倍率进图(self.武器类型)
            except:
                pass
        return 面板独立攻击 * self.站街独立攻击力倍率()

    def 面板系数计算(self):
        if self.类型 == '物理百分比':
            return int((self.面板力量() / 250 + 1) * (self.物理攻击力 + self.进图物理攻击力) *
                       (1 + self.百分比三攻))
        elif self.类型 == '魔法百分比':
            return int((self.面板智力() / 250 + 1) * (self.魔法攻击力 + self.进图魔法攻击力) *
                       (1 + self.百分比三攻))
        elif self.类型 == '物理固伤':
            return int((self.面板力量() / 250 + 1) * (self.独立攻击力 + self.进图独立攻击力) *
                       (1 + self.百分比三攻))
        elif self.类型 == '魔法固伤':
            return int((self.面板智力() / 250 + 1) * (self.独立攻击力 + self.进图独立攻击力) *
                       (1 + self.百分比三攻))

    def 力智计算(self):
        return max(self.面板力量(), self.面板智力())

    # endregion

    # region 输出计算
    def 加算冷却计算(self):
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                i.CD *= (1 - self.加算冷却缩减)

    def CD倍率计算(self):
        for i in self.技能栏:
            if i.冷却关联技能 != ['无']:
                if i.冷却关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率(self.武器类型)
                else:
                    for k in i.冷却关联技能:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率(self.武器类型)
            if i.非冷却关联技能 != ['无']:
                if i.非冷却关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD /= i.CD缩减倍率(self.武器类型)
                else:
                    for k in i.非冷却关联技能:
                        self.技能栏[self.技能序号[k]].CD /= i.CD缩减倍率(self.武器类型)
            if i.冷却关联技能2 != ['无']:
                if i.冷却关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率2(self.武器类型)
                else:
                    for k in i.冷却关联技能2:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率2(self.武器类型)
            if i.非冷却关联技能2 != ['无']:
                if i.非冷却关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD /= i.CD缩减倍率2(self.武器类型)
                else:
                    for k in i.非冷却关联技能2:
                        self.技能栏[self.技能序号[k]].CD /= i.CD缩减倍率2(self.武器类型)
            if i.冷却关联技能3 != ['无']:
                if i.冷却关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率3(self.武器类型)
                else:
                    for k in i.冷却关联技能3:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率3(self.武器类型)
            if i.非冷却关联技能3 != ['无']:
                if i.非冷却关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD /= i.CD缩减倍率3(self.武器类型)
                else:
                    for k in i.非冷却关联技能3:
                        self.技能栏[self.技能序号[k]].CD /= i.CD缩减倍率3(self.武器类型)

    def 被动倍率计算(self):
        if self.远古记忆 > 0:
            self.进图智力 += self.远古记忆 * 15
        if self.刀魂之卡赞 > 0:
            self.进图力量 += 刀魂之卡赞数据[self.刀魂之卡赞]
            self.进图智力 += 刀魂之卡赞数据[self.刀魂之卡赞]
        for i in self.技能栏:
            i.被动倍率 = 1
        for i in self.技能栏:
            if i.关联技能 != ['无']:
                if i.关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率(self.武器类型)
                else:
                    for k in i.关联技能:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率(self.武器类型)
            if i.非关联技能 != ['无']:
                if i.非关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 /= i.加成倍率(self.武器类型)
                else:
                    for k in i.非关联技能:
                        self.技能栏[self.技能序号[k]].被动倍率 /= i.加成倍率(self.武器类型)

            if i.关联技能2 != ['无']:
                if i.关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率2(self.武器类型)
                else:
                    for k in i.关联技能2:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率2(self.武器类型)

            if i.非关联技能2 != ['无']:
                if i.非关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 /= i.加成倍率2(self.武器类型)
                else:
                    for k in i.非关联技能2:
                        self.技能栏[self.技能序号[k]].被动倍率 /= i.加成倍率2(self.武器类型)

            if i.关联技能3 != ['无']:
                if i.关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率3(self.武器类型)
                else:
                    for k in i.关联技能3:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率3(self.武器类型)

            if i.非关联技能3 != ['无']:
                if i.非关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 /= i.加成倍率3(self.武器类型)
                else:
                    for k in i.非关联技能3:
                        self.技能栏[self.技能序号[k]].被动倍率 /= i.加成倍率3(self.武器类型)

    def 属性倍率计算(self):
        # 火、冰、光、暗
        self.属性倍率组 = []
        self.属性倍率组.append(1.05 + 0.0045 * int(self.火属性强化 - self.火抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.冰属性强化 - self.冰抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.光属性强化 - self.光抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.暗属性强化 - self.暗抗输入))
        if self.攻击属性 == 0:
            self.属性倍率 = max(self.属性倍率组)
        elif self.攻击属性 == 1:
            self.属性倍率 = self.属性倍率组[0]
        elif self.攻击属性 == 2:
            self.属性倍率 = self.属性倍率组[1]
        elif self.攻击属性 == 3:
            self.属性倍率 = self.属性倍率组[2]
        elif self.攻击属性 == 4:
            self.属性倍率 = self.属性倍率组[3]

    def 伤害指数计算(self):

        防御 = max(self.防御输入 - self.固定减防, 0) * (1 - self.百分比减防)
        基准倍率 = 1.5 * self.主BUFF * (1 - 防御 / (防御 + 200 * 等级))

        # 避免出现浮点数取整BUG
        self.伤害增加 += 0.00000001

        self.属性倍率计算()

        # if sum(self.自适应选项) != 0:
        if self.计算自适应 == 1:
            self.自适应计算()

        # self.希洛克武器提升()

        面板 = self.面板系数计算()

        增伤倍率 = 1 + int(self.伤害增加 * 100) / 100
        增伤倍率 *= 1 + self.暴击伤害
        增伤倍率 *= 1 + self.最终伤害
        增伤倍率 *= self.技能攻击力
        增伤倍率 *= 1 + self.持续伤害 * self.持续伤害计算比例
        增伤倍率 *= 1 + self.附加伤害 + self.属性附加 * self.属性倍率

        self.伤害指数 = 面板 * self.属性倍率 * 增伤倍率 * 基准倍率 / 100 * self.队友增幅系数

        # 7.8日,伤害数据压缩
        self.伤害指数 /= 1000

    def 伤害计算(self, x=0):
        if 切装模式 == 1 and self.切装判断():
            temp = self.装备替换()
            A = temp[0].数据计算(1, 1)  # 身上装备计算
            B = temp[1].数据计算(1, 0)  # 切装装备计算
            self.预处理()
            for i in range(len(self.技能栏)):
                self.技能栏[i] = deepcopy(temp[self.技能切装[i]].技能栏[i])
            C = []
            总伤害 = 0
            for i in range(len(A)):
                C.append(A[i] if (self.技能切装[int(i / 4)] == 0) else B[i])
                if i % 4 == 1:
                    总伤害 += C[i]
            if x == 0:
                return 总伤害
            else:
                for i in range(int(len(A) / 4)):
                    if 总伤害 != 0:
                        C[i * 4 + 3] = C[i * 4 + 1] / 总伤害 * 100
                    else:
                        C[i * 4 + 3] = 0
                return C
        else:
            self.技能切装 = [0] * len(self.技能栏)
            # if self.计算自适应 == 1:
            #     self.择优拷贝 = deepcopy(self)
            #     self.择优拷贝.计算自适应 = 0
            return self.数据计算(x)

    def 技能释放次数解析(self, 技能释放次数):
        for i in range(len(self.技能栏)):
            if '/CD' in self.次数输入[i]:
                技能释放次数[i] = eval(self.次数输入[i].replace('/CD', str(技能释放次数[i])))
            if type(self.宠物次数[i]) == type('str'):
                self.宠物次数[i] = eval(self.宠物次数[i].replace(
                    'num', str(技能释放次数[i])))
        return 技能释放次数

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                s = self.次数输入[self.技能序号[i.名称]]
                if '/CD' in s:
                    技能释放次数.append(
                        int((self.时间输入 - i.演出时间) /
                            i.等效CD(self.武器类型, self.类型)) + 1 + i.基础释放次数)
                else:
                    技能释放次数.append(round(float(s), 2))
            else:
                技能释放次数.append(0)

        return self.技能释放次数解析(技能释放次数)

    def 技能单次伤害计算(self, y):
        # y切装标记
        技能单次伤害 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1 and self.技能切装[self.技能序号[i.名称]] != y:
                技能单次伤害.append(i.等效百分比(self.武器类型) * self.伤害指数 * i.被动倍率)
            else:
                技能单次伤害.append(0)
        return 技能单次伤害

    def 技能总伤害计算(self, a, b):
        # a次数 b单次伤害
        技能总伤害 = []
        for i in self.技能栏:
            index = self.技能序号[i.名称]
            if i.是否有伤害 == 1 and a[index] != 0:
                技能总伤害.append(a[index] * b[index] * (
                    1 + self.白兔子技能 * 0.20 + self.年宠技能 * 0.10 *
                    self.宠物次数[index] / a[index]  # 宠物技能占比 = 宠物次数 / 释放次数
                    + self.斗神之吼秘药 * 0.12))
            else:
                技能总伤害.append(0)
        return 技能总伤害

    def 数据返回(self, x, a, b):
        # a次数  b伤害
        总伤害 = sum(b)
        if x == 0:
            # 伤害数据，用于排序
            return 总伤害
        elif x == 1:
            # 详细数据，用于展示  四个数据一组
            # 0次数 1总伤害 2平均伤害 3占比
            data = []
            for i in range(len(self.技能栏)):
                data.append(a[i])
                data.append(b[i])
                if a[i] != 0:
                    data.append(b[i] / a[i])
                else:
                    data.append(b[i])
                if 总伤害 != 0:
                    data.append(b[i] / 总伤害 * 100)
                else:
                    data.append(0)
            return data

    def 数据计算(self, x=0, y=-1):
        self.预处理()
        # 初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        # 返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)

    def 装备词条计算(self):
        # 初始化 以防和自选冲突
        self.变换词条 = [
            # 原词条类型，原词条数值，可洗最小值，可洗最大值，择优不考虑觉醒
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        if 调试开关 == 0:
            for i in range(12):
                temp = equ.get_equ_by_name(self.装备栏[i])
                temp.城镇属性(self)
                temp.变换属性(self)
                if temp.所属套装 == '智慧产物' and self.产物升级 == 1:
                    temp.产物升级(self)
                # 添加可洗属性

            for i in self.套装栏:
                equ.get_suit_by_name(i).城镇属性(self)
            # print(self.变换词条)
            # 进图触发属强向下取整
            self.状态 = 1
            for i in range(12):
                equ.get_equ_by_name(self.装备栏[i]).进图属性(self)

            for i in self.套装栏:
                equ.get_suit_by_name(i).进图属性(self)
            self.状态 = 0
        self.黑鸦词条扣除()
        # print(self.黑鸦词条)
        # 冲突属性计算
        self.伤害增加加成(self.黄字)
        self.暴击伤害加成(self.暴伤)

    def 预处理(self):
        self.装备属性计算()
        self.三觉屏蔽1()
        self.所有属性强化(self.进图属强)
        self.CD倍率计算()
        self.加算冷却计算()
        self.被动倍率计算()
        self.三觉屏蔽2()
        self.伤害指数计算()

    def 装备属性计算(self):
        self.装备基础()
        self.装备词条计算()

    def 其它属性计算(self):
        for i in range(12):
            equ.get_equ_by_name(self.装备栏[i]).其它属性(self)

        for i in self.套装栏:
            equ.get_suit_by_name(i).其它属性(self)

    # endregion

    # region 择优相关
    def 词条提示上下限计算(self, 词条范围, 词条数值):
        词条提升率 = [[0, 0]] * 6

        if 0 in 词条范围:
            # 百分比力智
            最高提升 = 0
            x = self.面板系数计算()
            self.百分比力智加成(词条数值[0])
            最高提升 = round(self.面板系数计算() / x - 1, 8)
            self.百分比力智加成(-词条数值[0])

            最低提升 = 0
            self.百分比力智加成(self.择优极限[0] - 词条数值[0])
            x = self.面板系数计算()
            self.百分比力智加成(词条数值[0])
            最低提升 = round(self.面板系数计算() / x - 1, 8)
            self.百分比力智加成(-self.择优极限[0])

            词条提升率[0] = [最低提升, 最高提升]

        if 1 in 词条范围:
            最高提升 = 0
            x = 1 + self.百分比三攻
            self.百分比三攻加成(词条数值[1])
            最高提升 = round((1 + self.百分比三攻) / x - 1, 8)
            self.百分比三攻加成(-词条数值[1])

            最低提升 = 0
            self.百分比三攻加成(self.择优极限[1] - 词条数值[1])
            x = 1 + self.百分比三攻
            self.百分比三攻加成(词条数值[1])
            最低提升 = round((1 + self.百分比三攻) / x - 1, 8)
            self.百分比三攻加成(-self.择优极限[1])

            词条提升率[1] = [最低提升, 最高提升]

        if 2 in 词条范围:
            最高提升 = 0
            x = 1 + int(self.伤害增加 * 100) / 100
            self.伤害增加加成(词条数值[2])
            最高提升 = round((1 + int(self.伤害增加 * 100) / 100) / x - 1, 8)
            self.伤害增加加成(-词条数值[2])

            最低提升 = 0
            self.伤害增加加成(self.择优极限[2] - 词条数值[2])
            x = 1 + int(self.伤害增加 * 100) / 100
            self.伤害增加加成(词条数值[2])
            最低提升 = round((1 + int(self.伤害增加 * 100) / 100) / x - 1, 8)
            self.伤害增加加成(-self.择优极限[2])

            词条提升率[2] = [最低提升, 最高提升]

        if 3 in 词条范围:
            最高提升 = 0
            x = 1 + self.附加伤害 + self.属性附加 * self.属性倍率
            self.附加伤害加成(词条数值[3])
            最高提升 = round((1 + self.附加伤害 + self.属性附加 * self.属性倍率) / x - 1, 8)
            self.附加伤害加成(-词条数值[3])

            最低提升 = 0
            self.附加伤害加成(self.择优极限[3] - 词条数值[3])
            x = 1 + self.附加伤害 + self.属性附加 * self.属性倍率
            self.附加伤害加成(词条数值[3])
            最低提升 = round((1 + self.附加伤害 + self.属性附加 * self.属性倍率) / x - 1, 8)
            self.附加伤害加成(-self.择优极限[3])

            词条提升率[3] = [最低提升, 最高提升]

        if 4 in 词条范围:
            最高提升 = 0
            x = 1 + self.暴击伤害
            self.暴击伤害加成(词条数值[4])
            最高提升 = round((1 + self.暴击伤害) / x - 1, 8)
            self.暴击伤害加成(-词条数值[4])

            最低提升 = 0
            self.暴击伤害加成(self.择优极限[4] - 词条数值[4])
            x = 1 + self.暴击伤害
            self.暴击伤害加成(词条数值[4])
            最低提升 = round((1 + self.暴击伤害) / x - 1, 8)
            self.暴击伤害加成(-self.择优极限[4])

            词条提升率[4] = [最低提升, 最高提升]

        if 5 in 词条范围:
            最高提升 = 0
            x = 1 + self.最终伤害
            self.最终伤害加成(词条数值[5])
            最高提升 = round((1 + self.最终伤害) / x - 1, 8)
            self.最终伤害加成(-词条数值[5])

            最低提升 = 0
            self.最终伤害加成(self.择优极限[5] - 词条数值[5])
            x = 1 + self.最终伤害
            self.最终伤害加成(词条数值[5])
            最低提升 = round((1 + self.最终伤害) / x - 1, 8)
            self.最终伤害加成(-self.择优极限[5])

            词条提升率[5] = [最低提升, 最高提升]

        return 词条提升率

    def 词条修改(self, x):
        self.百分比力智加成(x)
        self.百分比三攻加成(x)
        self.伤害增加加成(x)
        self.附加伤害加成(x)
        self.暴击伤害加成(x)
        self.最终伤害加成(x)

    def 基础提升率计算(self):
        词条基数 = [
            250 + self.力智计算(),
            1 + self.百分比三攻,
            100 * (1 + self.伤害增加),
            1 + self.附加伤害 + self.属性附加 * self.属性倍率,
            1 + self.暴击伤害,
            1 + self.最终伤害,
        ]
        self.词条修改(0.01)
        词条提升后数值 = [
            250 + self.力智计算(),
            1 + self.百分比三攻,
            100 * (1 + self.伤害增加),
            1 + self.附加伤害 + self.属性附加 * self.属性倍率,
            1 + self.暴击伤害,
            1 + self.最终伤害,
        ]
        self.词条修改(-0.01)

        return [词条基数, 词条提升后数值]

    def 词条提升率计算(self, 词条范围, 词条数值, y=0):

        词条提升率 = [0] * 6

        if 0 in 词条范围:
            # 百分比力智
            x = self.面板系数计算()
            self.百分比力智加成(词条数值[0])
            词条提升率[0] = round(self.面板系数计算() / x - 1, 8)
            self.百分比力智加成(-词条数值[0])

        if 1 in 词条范围:
            # 百分比三攻
            x = 1 + self.百分比三攻
            self.百分比三攻加成(词条数值[1])
            词条提升率[1] = round((1 + self.百分比三攻) / x - 1, 8)
            self.百分比三攻加成(-词条数值[1])

        if 2 in 词条范围:
            # 伤害增加
            x = 1 + int(self.伤害增加 * 100) / 100
            self.伤害增加加成(词条数值[2])
            词条提升率[2] = round((1 + int(self.伤害增加 * 100) / 100) / x - 1, 8)
            self.伤害增加加成(-词条数值[2])

        if 3 in 词条范围:
            # 附加伤害
            x = 1 + self.附加伤害 + self.属性附加 * self.属性倍率
            self.附加伤害加成(词条数值[3])
            词条提升率[3] = round((1 + self.附加伤害 + self.属性附加 * self.属性倍率) / x - 1,
                             8)
            self.附加伤害加成(-词条数值[3])

        if 4 in 词条范围:
            # 暴击伤害
            x = 1 + self.暴击伤害
            self.暴击伤害加成(词条数值[4])
            词条提升率[4] = round((1 + self.暴击伤害) / x - 1, 8)
            self.暴击伤害加成(-词条数值[4])

        if 5 in 词条范围:
            # 最终伤害
            x = 1 + self.最终伤害
            self.最终伤害加成(词条数值[5])
            词条提升率[5] = round((1 + self.最终伤害) / x - 1, 8)
            self.最终伤害加成(-词条数值[5])

        if y == 1:
            self.词条提升率 = copy(词条提升率)

        # for k in range(6):
        #     if 词条提升率[k] == max(词条提升率):
        #         词条属性列表[k].加成属性(self, 词条数值[k])
        #         return k
        tem = []
        最小词条 = 0
        for k in range(6):
            if 词条提升率[k] == max(词条提升率):
                # 词条属性列表[k].加成属性(self, 词条数值[k])
                tem.append(k)
        待排序提升率 = []
        for i in tem:
            待排序提升率.append([i, self.择优极限[i]])
        待排序提升率.sort(key=lambda x: round(x[1], 2), reverse=False)
        self.择优极限 = [round(self.择优极限[i] - 词条数值[i], 3) for i in range(6)]
        最小词条 = 待排序提升率[0][0]
        词条属性列表[最小词条].加成属性(self, 词条数值[最小词条])
        return 最小词条

    def 自适应计算(self, x=0):
        # print(self.计算自适应方式)
        if self.黑鸦武器择优模式 == 0:
            self.择优词条 = [[round(self.变换词条[0][3] / 100, 2)] * 6,
                         [round(self.变换词条[1][3] / 100, 2)] * 6,
                         [round(self.变换词条[2][3] / 100, 2)] * 6,
                         [round(self.变换词条[3][3] / 100, 2)] * 6, [0.1] * 6,
                         [0.05] * 6, [0.08, 0.08, 0.07, 0.08, 0, 0.08],
                         [0, 0.05, 0.05, 0, 0.05, 0]]
        else:
            self.择优词条 = [[round(0.16, 2)] * 6,
                         [round(self.变换词条[1][3] / 100, 2)] * 6,
                         [round(self.变换词条[2][3] / 100, 2)] * 6,
                         [round(self.变换词条[3][3] / 100, 2)] * 6, [0.1] * 6,
                         [0.05] * 6, [0.08, 0.08, 0.07, 0.08, 0, 0.08],
                         [0, 0.05, 0.05, 0, 0.05, 0]]
        self.是否择优 = self.词条是否择优()
        self.择优结果 = [[0, 0]] * len(self.择优词条)
        # print(self.择优词条)
        # self.是否择优 = self.词条是否择优()
        # print(self.是否择优)
        # print(self.计算自适应方式)
        # if self.计算自适应方式 == 0:
        #     self.贪心自适应()
        # else:
        # self.全局自适应()
        if self.输出提升率 != 0:
            self.择优提升率计算()
        else:
            try:
                self.全局自适应()
            except Exception as error:
                logger.error(error)
                self.贪心自适应()
        for i in range(len(self.择优结果)):
            # 词条属性列表[self.择优结果[i][0]].加成属性(self,self.择优结果[i][1])
            if i < 4:
                self.黑鸦词条[i].append("")
                if self.择优结果[i][1] != 0:
                    self.黑鸦词条[i][4] = (
                        trans("觉醒Lv+2 ")
                        if i == 0 and self.择优结果[i][1] == 0.16 else '') + trans(
                            黑鸦武器属性列表[self.择优结果[i][0]].描述) + '+' + str(
                                round(self.择优结果[i][1] * 100)) + '%'
            if i == 4:
                if self.是否择优[i] == 0:
                    self.词条提升率 = [0] * 6
                else:
                    self.词条选择.clear()
                    self.词条选择.append(self.择优结果[i][0])
            if i == 5:
                if self.是否择优[i] != 0:
                    self.词条选择.append(self.择优结果[i][0])
            if i == 6:
                self.自适应描述[0] = '{}%{}'.format(
                    int(self.择优结果[i][1] * 100),
                    trans(词条属性列表[self.择优结果[i][0]].描述))
            if i == 7:
                self.自适应描述[1] = '{}%{}'.format(
                    int(self.择优结果[i][1] * 100),
                    trans(词条属性列表[self.择优结果[i][0]].描述))

    def 计算择优范围(self, d):
        index = []
        for i in range(6):
            if d[i] != 0:
                index.append(i)
        if len(index) == 0:
            index.append(0)
        return index

    def 择优提升率计算(self):

        up = self.基础提升率计算()

        data_array = [[0 for i in range(6)] for i in range(8)]

        for i in range(8):
            for j in range(6):
                data_array[i][j] = self.择优词条[i][j] * (
                    up[1][j] - up[0][j]) * self.是否择优[i] * 100
        try:
            self.全局自适应()
        except:
            self.贪心自适应()
        k = [up[0][0], up[0][1], up[0][2], up[0][3], up[0][4], up[0][5]]
        k[self.择优结果[0][0]] += data_array[0][self.择优结果[0][0]]
        k[self.择优结果[1][0]] += data_array[1][self.择优结果[1][0]]
        k[self.择优结果[2][0]] += data_array[2][self.择优结果[2][0]]
        k[self.择优结果[3][0]] += data_array[3][self.择优结果[3][0]]
        k[self.择优结果[4][0]] += data_array[4][self.择优结果[4][0]]
        k[self.择优结果[5][0]] += data_array[5][self.择优结果[5][0]]
        k[self.择优结果[6][0]] += data_array[6][self.择优结果[6][0]]
        k[self.择优结果[7][0]] += data_array[7][self.择优结果[7][0]]
        max_data = k[0] * k[1] * int(k[2]) * k[3] * k[4] * k[5]

        rangelist = [self.计算择优范围(i) for i in data_array]

        path = './详细数据'
        if not os.path.exists(path):
            os.makedirs(path)
        result_path = os.path.join(
            path, '{}-{}.csv'.format(self.实际名称,
                                     time.strftime('%m-%d-%H-%M-%S')))
        wf = open(result_path, 'w', encoding='gbk')
        wf.write('黑鸦武器,黑鸦戒指,黑鸦左槽,黑鸦下装,残香10%,残香5%,宠物装备,光环,系数,伤害\n')
        increase_counter(ga_category="carry详细功能使用", name="输出择优数据")
        for a1 in rangelist[0]:
            for a2 in rangelist[1]:
                for a3 in rangelist[2]:
                    for a4 in rangelist[3]:
                        for a5 in rangelist[4]:
                            for a6 in rangelist[5]:
                                for a7 in rangelist[6]:
                                    for a8 in rangelist[7]:
                                        k = [
                                            up[0][0], up[0][1], up[0][2],
                                            up[0][3], up[0][4], up[0][5]
                                        ]
                                        k[a1] += data_array[0][a1]
                                        k[a2] += data_array[1][a2]
                                        k[a3] += data_array[2][a3]
                                        k[a4] += data_array[3][a4]
                                        k[a5] += data_array[4][a5]
                                        k[a6] += data_array[5][a6]
                                        k[a7] += data_array[6][a7]
                                        k[a8] += data_array[7][a8]
                                        rate = k[0] * k[1] * int(
                                            k[2]
                                        ) * k[3] * k[4] * k[5] / max_data
                                        damage = int(rate * self.输出提升率)
                                        wf.write(
                                            '{},{},{},{},{},{},{},{},{:.8},{}\n'
                                            .format(
                                                '无' if len(rangelist[0]) == 1
                                                else 词条属性列表[a1].描述,
                                                '无' if len(rangelist[1]) == 1
                                                else 词条属性列表[a2].描述,
                                                '无' if len(rangelist[2]) == 1
                                                else 词条属性列表[a3].描述,
                                                '无' if len(rangelist[3]) == 1
                                                else 词条属性列表[a4].描述,
                                                '无' if len(rangelist[4]) == 1
                                                else 词条属性列表[a5].描述,
                                                '无' if len(rangelist[5]) == 1
                                                else 词条属性列表[a6].描述,
                                                '无' if len(rangelist[6]) == 1
                                                else 词条属性列表[a7].描述,
                                                '无' if len(rangelist[7]) == 1
                                                else 词条属性列表[a8].描述, rate,
                                                damage))
        os.startfile(result_path)

    def 全局自适应(self):
        x = 6
        y = 8
        data_array = ((ctypes.c_double * x) * (y + 1))()  # 提升值数组
        index = (ctypes.c_int * y)()  # 索引

        up = self.基础提升率计算()

        # 第一行为词条基础
        for j in range(x):
            data_array[0][j] = up[0][j]

        # 后续8行为可选词条
        for i in range(y):
            for j in range(x):
                data_array[i + 1][j] = self.择优词条[i][j] * (
                    up[1][j] - up[0][j]) * self.是否择优[i] * 100

        preferred.cal_index(data_array, byref(index))

        for i in range(y):
            if self.是否择优[i] != 0:
                self.择优结果[i] = [index[i], self.择优词条[i][index[i]]]
                词条属性列表[self.择优结果[i][0]].加成属性(self, self.择优结果[i][1])

    def 贪心自适应(self):
        # self.全局自适应()
        # return
        # self.择优词条 = [
        #     [round(self.变换词条[0][3]/100,2)]*6,
        #     [round(self.变换词条[1][3]/100,2)]*6,
        #     [round(self.变换词条[2][3]/100,2)]*6,
        #     [round(self.变换词条[3][3]/100,2)]*6,
        #     [0.1]*6,
        #     [0.05]*6,
        #     [0.07,0,0.07,0.08,0,0,0],
        #     [0,0.05,0.05,0,0.05,0,0]
        # ]
        self.择优范围 = []
        for item in self.择优词条:
            词条数值 = item
            计算范围 = []
            for i in range(6):
                if 词条数值[i] != 0:
                    计算范围.append(i)
            self.择优范围.append(计算范围)
        贪心排序 = []
        自由择优 = []
        条件择优 = []
        条件择优结果 = []
        count = 1
        self.择优极限 = [0] * 6
        for i in range(len(self.择优词条)):
            if self.是否择优[i] == 1:
                词条数目 = len(list(filter(lambda x: x != 0, self.择优词条[i])))
                贪心排序.append([count, max(self.择优词条[i]), 词条数目])
                self.择优极限 = [
                    round(self.择优极限[j] + self.择优词条[i][j], 3) for j in range(6)
                ]
                if 词条数目 == 6:
                    自由择优.append(count)
                else:
                    条件择优.append(count)
                # 说明存在非全部择优的情况
            count += 1

        # 贪心排序 = [
        #     [1,round(self.变换词条[0][3]/100,2),6],
        #     [2,round(self.变换词条[1][3]/100,2),6],
        #     [3,round(self.变换词条[2][3]/100,2),6],
        #     [4,round(self.变换词条[3][3]/100,2),6],
        #     [5,0.1,6],
        #     [6,0.05,6],
        #     [7,0.08,3],
        #     [8,0.05,3]
        # ]
        贪心排序.sort(key=lambda x: round(x[1], 2), reverse=True)
        贪心排序.sort(key=lambda x: int(x[2]), reverse=True)

        # print(self.择优词条)
        # print(条件择优)
        # self.自适应1 = 0
        # self.自适应2 = 0
        # if self.自适应选项[0] !=0:
        #     self.自适应1 = 1
        # if self.自适应选项[1] !=0:
        #     self.自适应2 = 1

        # self.择优极限 = [0]*6
        # for item in 贪心排序:
        #     self.择优极限累计(item[0])
        # print(self.择优极限)

        for item in 贪心排序:
            条件择优结果 = []
            # 每次择优完计算非完全择优的每一个最高最低收益
            for temp in 条件择优:
                if self.是否择优[temp - 1] == 1:
                    词条数值 = self.择优词条[temp - 1]
                    上下限 = self.词条提示上下限计算(self.择优范围[temp - 1], 词条数值)
                    下限提升最高 = max([上下限[i][0] for i in range(len(上下限))])
                    index = 0
                    # tem = []
                    待排序提升率 = []
                    for i in range(6):
                        if 上下限[i][0] == 下限提升最高:
                            # tem.append(i)
                            待排序提升率.append([i, self.择优极限[i]])
                    待排序提升率.sort(key=lambda x: round(x[1], 2), reverse=False)
                    index = 待排序提升率[0][0]
                    del 上下限[index]
                    if 下限提升最高 >= max([上下限[i][1] for i in range(len(上下限))]):
                        self.是否择优[temp - 1] = 0
                        词条属性列表[index].加成属性(self, 词条数值[index])
                        # 条件择优结果.append('{}%{}'.format(int(词条数值[index] * 100), 词条属性列表[index].描述))
                        self.择优极限 = [
                            round(self.择优极限[i] - 词条数值[i], 3) for i in range(6)
                        ]
                        self.择优结果[temp - 1] = [index, 词条数值[index]]
                    # else:
                    #     条件择优结果.append('')
                # else:
                #     条件择优结果.append('')
            # for i in range(len(条件择优)):
            #     if 条件择优结果[i]!='':
            #         self.自适应描述[i]= 条件择优结果[i]
            self.择优计算(item[0])

    def 择优计算(self, index):
        for i in range(1, 5):
            if index == i and self.是否择优[index - 1] != 0:
                词条数值 = self.择优词条[index - 1]
                res = self.词条提升率计算(self.择优范围[index - 1], 词条数值)
                self.择优结果[index - 1] = [res, 词条数值[res]]
                # self.黑鸦词条[i-1].append("")
                # self.黑鸦词条[i-1][4] = 黑鸦武器属性列表[res].描述 +'+' +str(self.变换词条[i-1][3])+'%'
                # print(self.黑鸦词条)
                return
        # 残香词条1-10%
        if index == 5:
            if self.是否择优[index - 1] != 0:
                # self.词条选择.clear()
                词条数值 = self.择优词条[index - 1]
                res = self.词条提升率计算(self.择优范围[index - 1], 词条数值, 1)
                self.择优结果[index - 1] = [res, 词条数值[res]]
                # self.词条选择.append(res)
                # print(self.词条选择)
            return
        # 残香词条2
        if index == 6:
            if self.是否择优[index - 1] != 0:
                词条数值 = self.择优词条[index - 1]
                res = self.词条提升率计算(self.择优范围[index - 1], self.择优词条[index - 1])
                self.择优结果[index - 1] = [res, 词条数值[res]]
                # self.词条选择.append(self.词条提升率计算(self.择优范围[index-1], self.择优词条[index-1]))
            return
        # 宠物红色装备词条
        if index == 7:
            if self.是否择优[index - 1] != 0:  # 宠物
                词条数值 = self.择优词条[index - 1]
                res = self.词条提升率计算(self.择优范围[index - 1], 词条数值)
                self.择优结果[index - 1] = [res, 词条数值[res]]
                # self.自适应描述[0] = '{}%{}'.format(int(词条数值[res] * 100), 词条属性列表[res].描述)
                self.是否择优[index - 1] = 0
            return
        # 光环词条
        if index == 8:
            if self.是否择优[index - 1] != 0:  # 光环
                词条数值 = self.择优词条[index - 1]
                res = self.词条提升率计算(self.择优范围[index - 1], 词条数值)
                self.择优结果[index - 1] = [res, 词条数值[res]]
                # self.自适应描述[1] = '{}%{}'.format(5, 词条属性列表[res].描述)
                self.是否择优[index - 1] = 0
            return

    def 词条是否择优(self):
        temp = [0] * 8
        for i in range(4):
            if self.黑鸦词条[i][0] == 1 and self.变换词条[i][1] != 0:
                temp[i] = 1
        # 残香词条1-10%
        if self.希洛克武器词条 != 0:
            temp[4] = 1
        if self.希洛克武器词条 == 1 and self.武器词条触发 == 1:
            temp[5] = 1
        if self.自适应选项[0] != 0:
            temp[6] = 1
        if self.自适应选项[1] != 0:
            temp[7] = 1
        return temp

    def 自适应输出(self):
        temp = ''
        if self.自适应选项[0] != 0:  # 宠物
            temp += trans('{宠物}:$value', value=self.自适应描述[0])
        if self.自适应选项[1] != 0:  # 光环
            if temp != '':
                temp += '|'
            temp += trans('{光环}:$value', value=self.自适应描述[1])
        return temp

    def 黑鸦词条扣除(self):
        for i in range(4):
            self.黑鸦词条[i].append("")
            if self.黑鸦词条[i][0] != 0 and self.变换词条[i][1] != 0:
                self.黑鸦词条变更(self.变换词条[i], -1)
                if self.黑鸦词条[i][0] == 2 and self.变换词条[i][1]:
                    temp = [
                        self.黑鸦词条[i][1],
                        (14 if self.变换词条[i][0] == 6 else self.变换词条[i][1]) +
                        self.黑鸦词条[i][2], 0, 0
                    ]
                    self.黑鸦词条变更(temp, 1)
                    self.黑鸦词条[i][4] = 黑鸦武器属性列表[temp[0]].描述 + '+' + str(
                        (14 if self.变换词条[i][0] == 6 else self.变换词条[i][1]) +
                        self.黑鸦词条[i][2]) + ('' if temp[0] == 6 else '%')
                if self.黑鸦词条[i][0] == 3 and self.变换词条[i][1]:
                    self.黑鸦词条[i][4] = ""
                    temp = [6, 2, 0, 0]
                    self.黑鸦词条变更([6, 2, 0, 0])
                    self.黑鸦词条[i][4] += 黑鸦武器属性列表[temp[0]].描述 + '+' + '2'
                    self.黑鸦词条[i][4] += '<br>'
                    temp = [self.黑鸦词条[i][1], self.黑鸦词条[i][2], 0, 0]
                    self.黑鸦词条变更(temp, 1)
                    self.黑鸦词条[i][4] += 黑鸦武器属性列表[temp[0]].描述 + '+' + str(
                        self.黑鸦词条[i][2]) + '%'
        if self.黑鸦词条[0][0] == 1 and self.黑鸦武器择优模式 == 1 and self.变换词条[0][1] != 0:
            self.技能等级加成('所有', 50, 50, 2)
            self.技能等级加成('所有', 85, 85, 2)
            self.技能等级加成('所有', 100, 100, 2)

    def 黑鸦词条变更(self, 变换词条, 增减=1):
        # print(变换词条)
        if 变换词条[0] == 6:
            黑鸦武器属性列表[变换词条[0]].加成属性(self, 增减 * 变换词条[1])
        else:
            黑鸦武器属性列表[变换词条[0]].加成属性(self, 增减 * 变换词条[1] / 100)

    # endregion

    # region 功能函数
    def 装备检查(self, 装备名称):
        for i in self.装备栏:
            if i == 装备名称:
                return True
        return False

    def 切装判断(self):
        for i in self.装备切装:
            if i != '无':
                return True
        return False

    def 装备替换(self):
        Q = deepcopy(self)
        P = deepcopy(self)

        temp = list(P.装备栏)

        for i in range(12):
            if P.装备切装[i] != '无':
                temp[i] = P.装备切装[i]

        P.装备栏 = tuple(temp)

        P.适用套装计算()

        P.武器类型 = equ.get_equ_by_name(P.装备栏[11]).类型
        P.力量 += P.切装修正[0]
        P.智力 += P.切装修正[1]
        P.物理攻击力 += P.切装修正[2]
        P.魔法攻击力 += P.切装修正[3]
        P.独立攻击力 += P.切装修正[4]
        P.所有属性强化加成(P.切装修正[5])

        return [Q, P]

    def 三觉屏蔽1(self):
        if self.屏蔽三觉 == True:
            for i in self.技能栏:
                if i.所在等级 >= 95:
                    if i.所在等级 == 95 and i.是否主动 == 0:
                        self.超卓之心等级 = i.等级 - 3
                    else:
                        i.倍率 = 0

    def 三觉屏蔽2(self):
        if self.屏蔽三觉 == True:
            temp = None
            for j in self.技能栏:
                if j.是否有伤害 == 1:
                    j.被动倍率 *= 1.045 + 0.005 * self.超卓之心等级
                if j.所在等级 == 100:
                    temp = j
            self.技能栏[self.技能序号[self.觉醒之抉择技能]].被动倍率 *= 1.1 + 0.05 * temp.等级

    # endregion


class 角色窗口(窗口):
    def __init__(self):
        super().__init__()

    # region 界面分页
    def 界面(self):
        count = 0
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                count += 1
        self.窗口高度 = max(55 + 30 * count, 680)
        self.setFixedSize(1120, 680)
        self.输出背景图片 = QPixmap(trans('./ResourceFiles/img/输出背景.png'))
        self.职业存档 = []
        super().界面()

    def 界面1(self):
        super().界面1()
        # increase_counter(ga_category="carry界面", name="界面/选择/打造")

        for i in 称号列表:
            self.称号.addItem(trans(i.显示名称), i.名称)

        for i in 宠物列表:
            self.宠物.addItem(trans(i.显示名称), i.名称)

        标签 = QLabel(trans('装备条件设置'), self.main_frame1)
        标签.move(940, 5)
        标签.resize(170, 20)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        self.装备条件选择.clear()
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['角色熟练度：英雄', '角色熟练度：传说'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        for i in range(0, 7):
            self.装备条件选择[-1].addItem(trans('{技能栏空位}：$value', value=i))
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(
            trans([
                '命运的抉择：数学期望', '命运的抉择：黄字+10%', '命运的抉择：暴伤+10%', '命运的抉择：终伤+10%',
                '命运的抉择：三攻+10%', '命运的抉择：技攻+10%'
            ]))
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(
            trans([
                '骰子：数学期望', '骰子：1点', '骰子：2点', '骰子：3点', '骰子：4点', '骰子：5点', '骰子：6点'
            ]))
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(
            trans([
                '悲剧的残骸：数学期望', '悲剧的残骸：HP高于70%', '悲剧的残骸：HP70-30%',
                '悲剧的残骸：HP低于30%'
            ]))
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(
            trans(
                ['先知者预言：数学期望', '先知者预言：属白+5%', '先知者预言：技攻+10%', '先知者预言：技攻+15%']))
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(
            trans(['贫瘠沙漠的遗产：无', '贫瘠沙漠的遗产：霸体', '贫瘠沙漠的遗产：无伤']))
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(
            trans(['幸运三角：数学期望', '幸运三角：7效果', '幸运三角：77效果', '幸运三角：777效果']))
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['擎天战甲：过充电状态', '擎天战甲：过负荷状态'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        for i in range(101):
            self.装备条件选择[-1].addItem(trans('{持续伤害适用}$value%', value=100 - i))
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(
            trans([
                '军神的隐秘遗产：120%以上', '军神的隐秘遗产：120-100%', '军神的隐秘遗产：100-80%',
                '军神的隐秘遗产：80-60%', '军神的隐秘遗产：60-40%', '军神的隐秘遗产：40%以下'
            ]))
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['太极天帝剑：阳', '太极天帝剑：阴'])
        self.装备条件选择.append(MyQComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['{噙毒手套}：中毒', '{噙毒手套}：未中毒'])
        # self.装备条件选择.append(MyQComboBox(self.main_frame1))
        # self.装备条件选择[-1].addItems(['绿色生命的面容：无', '绿色生命的面容：阴暗面'])
        for i in range(len(self.装备条件选择)):
            self.装备条件选择[i].resize(170, 20)
            self.装备条件选择[i].move(940, 30 + 28 * i)

        self.百变怪选项 = QCheckBox(trans('百变怪'), self.main_frame1)
        self.百变怪选项.move(660, 613)
        self.百变怪选项.resize(80, 24)
        self.百变怪选项.setToolTip('<font size="3" face="宋体">{}</font>'.format(
            trans("仅在极速模式和套装模式下生效")))
        self.百变怪选项.setStyleSheet(复选框样式)

        self.计算模式选择 = MyQComboBox(self.main_frame1)
        self.计算模式选择.addItems(['计算模式：极速模式', '计算模式：套装模式', '计算模式：单件模式'])
        self.计算模式选择.move(750, 613)
        self.计算模式选择.resize(235, 24)
        self.计算模式选择.setStyleSheet(下拉框样式)
        self.计算模式选择.setToolTip('<font size="3" face="宋体">{}</font>'.format(
            trans(
                '极速模式：533和3332(散搭) (不含智慧产物)<br><br>套装模式：533、3332(散搭)和3233(双防具) (不含智慧产物)<br><br>单件模式：所有组合 (不含百变怪)'
            )))

        self.最大使用线程数 = thread_num

        # 一键修正按钮添加
        一键站街修正名称 = trans(['站街力智', '站街三攻', '站街属强'])
        for i in range(len(一键站街修正名称)):
            名称 = QLabel(一键站街修正名称[i], self.main_frame1)
            名称.setAlignment(Qt.AlignCenter)
            名称.move(940 + i * 57, 394)
            名称.resize(52, 25)
            名称.setStyleSheet(标签样式)
            self.一键站街设置输入.append(QLineEdit(self.main_frame1))
            self.一键站街设置输入[i].setAlignment(Qt.AlignCenter)
            self.一键站街设置输入[i].setStyleSheet(输入框样式)
            self.一键站街设置输入[i].resize(52, 22)
            self.一键站街设置输入[i].move(940 + i * 57, 424)

        一键修正按钮 = QPushButton(trans('一键修正面板细节'), self.main_frame1)
        一键修正按钮.clicked.connect(lambda state: self.一键修正(0))
        一键修正按钮.move(940, 450)
        一键修正按钮.resize(166, 25)
        一键修正按钮.setStyleSheet(按钮样式)

        # self.单套择优方式选项 = MyQComboBox(self.main_frame1)
        # self.单套择优方式选项.move(940, 30 + 28 * 12)
        # self.单套择优方式选项.resize(170,20)
        # self.单套择优方式选项.addItem('单套择优方式：局部择优')
        # self.单套择优方式选项.addItem('单套择优方式：全局择优')
        # self.单套择优方式选项.setToolTip('排行榜及自选采用局部择优方式\n该选项仅适用于查看详情\n局部择优与全局择优大多数情况下一致\n少数情况下会有0.1%不到的差距')

        x = 1006
        y = 485
        宽度 = 100
        高度 = 20
        间隔 = 4
        self.红色宠物装备 = QCheckBox(trans('宠物装备择优'), self.main_frame1)
        self.红色宠物装备.move(x, y)
        self.红色宠物装备.resize(宽度, 高度)
        self.红色宠物装备.setStyleSheet(复选框样式)
        self.红色宠物装备.setToolTip('<font size="3" face="宋体">{}</font>'.format(
            trans('7%黄字,8%力智,8%白字,8%三攻取最高值')))
        self.红色宠物装备.stateChanged.connect(lambda state: self.下拉框禁用(
            self.红色宠物装备, self.细节选项输入[0][11], 下拉框样式_detail))

        self.光环自适应 = QCheckBox(trans('光环词条择优'), self.main_frame1)
        self.光环自适应.move(x, y + (高度 + 间隔) * 1)
        self.光环自适应.resize(宽度, 高度)
        self.光环自适应.setStyleSheet(复选框样式)
        self.光环自适应.setToolTip('<font size="3" face="宋体">{}</font>'.format(
            trans('5%黄字，5%暴伤，5%三攻取最高值')))
        self.光环自适应.stateChanged.connect(lambda state: self.下拉框禁用(
            self.光环自适应, self.细节选项输入[1][13], 下拉框样式_detail))

        self.禁用存档 = QCheckBox(trans('禁用自动存档'), self.main_frame1)
        self.禁用存档.move(x, y + (高度 + 间隔) * 2)
        self.禁用存档.resize(宽度, 高度)
        self.禁用存档.setStyleSheet(复选框样式)

        self.神话排名选项 = QCheckBox(trans('神话排名模式'), self.main_frame1)
        self.神话排名选项.move(x, y + (高度 + 间隔) * 3)
        self.神话排名选项.resize(宽度, 高度)
        self.神话排名选项.setToolTip('<font size="3" face="宋体">{}</font>'.format(
            trans('仅显示有神话的组合，且每件神话装备只会出现一次')))
        self.神话排名选项.setStyleSheet(复选框样式)

        self.显示选项 = QCheckBox(trans('亿为单位显示'), self.main_frame1)
        self.显示选项.move(x, y + (高度 + 间隔) * 4)
        self.显示选项.resize(宽度, 高度)
        self.显示选项.setStyleSheet(复选框样式)

        x = 910
        y = 485
        宽度 = 90
        高度 = 20
        间隔 = 4
        重置按钮 = QPushButton(trans('全局重置'), self.main_frame1)
        重置按钮.clicked.connect(lambda state: self.全局重置())
        重置按钮.move(x, y)
        重置按钮.resize(宽度, 高度)
        重置按钮.setStyleSheet(按钮样式)

        self.线程数选择 = MyQComboBox(self.main_frame1)
        self.线程数选择.move(x, y + (高度 + 间隔) * 1)
        self.线程数选择.resize(宽度, 高度)
        for i in range(thread_num, 0, -1):
            self.线程数选择.addItem(trans('{进程}:$value', value=i))
        if thread_num > 1:
            self.线程数选择.setCurrentIndex(1)

        self.存档选择 = MyQComboBox(self.main_frame1)
        self.存档选择.move(x, y + (高度 + 间隔) * 2)
        self.存档选择.resize(宽度, 高度)
        self.存档选择.currentIndexChanged.connect(lambda state: self.存档更换())

        self.智慧产物限制 = MyQComboBox(self.main_frame1)
        self.智慧产物限制.move(x, y + (高度 + 间隔) * 3)
        self.智慧产物限制.resize(宽度, 高度)
        for i in range(1, 12):
            self.智慧产物限制.addItem(trans('改造≤$件').format(i))
        self.智慧产物限制.setCurrentIndex(2)
        self.智慧产物限制.setToolTip('<font size="3" face="宋体">{}</font>'.format(
            trans('不计智慧产物武器以及轮回SS')))

        self.攻击属性选项 = MyQComboBox(self.main_frame1)
        self.攻击属性选项.move(x, y + (高度 + 间隔) * 4)
        self.攻击属性选项.resize(宽度, 高度)
        self.攻击属性选项.addItems(format_range('攻击属性:{}',
                                          ['全', '火', '冰', '光', '暗']))

    def 界面2(self):
        # 第二个布局界面
        # increase_counter(ga_category="carry界面", name="技能/符文/药剂")
        # 技能等级、TP、次数输入、宠物次数
        self.BUFF输入 = QLineEdit(self.main_frame2)
        self.时间输入 = MyQComboBox(self.main_frame2)

        self.护石栏 = []
        for i in range(3):
            self.护石栏.append(MyQComboBox(self.main_frame2))
        self.符文 = []
        self.符文效果 = []

        self.觉醒选择状态 = 2

        self.等级调整 = []
        self.TP输入 = []
        self.次数输入 = []
        self.宠物次数 = []
        self.奶量buff输入 = []

        if 切装模式 == 1:
            self.技能切装 = []

        count = 0
        for i in self.角色属性A.技能栏:
            i.等级 = i.基础等级
            self.等级调整.append(MyQComboBox(self.main_frame2))
            self.等级调整[count].currentIndexChanged.connect(
                lambda state, index=count: self.等级调整标注(index))
            count += 1
            if i.是否有伤害 == 1 and i.TP上限 != 0:
                self.TP输入.append(MyQComboBox(self.main_frame2))
            else:
                self.TP输入.append('')
            if i.是否有伤害 == 1:
                self.次数输入.append(MyQComboBox(self.main_frame2))
                self.宠物次数.append(MyQComboBox(self.main_frame2))
                if 切装模式 == 1:
                    temp = QCheckBox(self.main_frame2)
                    temp.setStyleSheet(复选框样式)
                    # temp.setStyleSheet("QCheckBox:{background-color:transparent}")
                    self.技能切装.append(temp)
            else:
                self.次数输入.append('')
                self.宠物次数.append('')
                if 切装模式 == 1:
                    self.技能切装.append('')

        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.所在等级 == 50 or i.所在等级 == 85:
                for j in range(i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
            else:
                for j in range(-i.基础等级, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))

            if i.是否有伤害 == 1 and i.TP上限 != 0:
                for j in range(i.TP上限 + 1):
                    self.TP输入[序号].addItem(str(j))

            if i.是否有伤害 == 1:
                self.次数输入[序号].setMaxVisibleItems(15)
                self.次数输入[序号].addItem('/CD')
                self.宠物次数[序号].setMaxVisibleItems(15)
                for j in range(11):
                    self.次数输入[序号].addItem(str(j))
                    self.宠物次数[序号].addItem(str(j))
                self.次数输入[序号].addItem('填写')
                self.次数输入[序号].activated.connect(
                    lambda state, index=序号: self.次数输入填写(index))
                self.宠物次数[序号].addItem('填写')
                self.宠物次数[序号].activated.connect(
                    lambda state, index=序号: self.宠物次数填写(index))

        # 三觉强化选择
        self.一觉遮罩透明度 = QGraphicsOpacityEffect()
        self.一觉遮罩透明度.setOpacity(0.5)
        self.二觉遮罩透明度 = QGraphicsOpacityEffect()
        self.二觉遮罩透明度.setOpacity(0.0)

        横坐标 = 10
        纵坐标 = 0
        横坐标偏移量 = 60
        纵坐标偏移量 = 30
        词条框宽度 = 48
        行高 = 20

        counter = 0
        for i in trans(["契约满级", "等级调整", "TP等级", "释放次数", "宠物次数"]):
            x = QLabel(i, self.main_frame2)
            x.move(横坐标 + 横坐标偏移量 - 30 + 50 * counter, 纵坐标 + 5)
            x.setStyleSheet(标签样式)
            counter += 1

        纵坐标 += 20

        skill_sort = self.技能列表显示排序(self.角色属性A.技能栏)

        for i in skill_sort:
            if i.是否有伤害 == 1:
                x = QLabel(self.main_frame2)
                x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
                x.resize(28, 28)
                tempstr = trans(
                    '<font face="宋体"><font color="#FF6666">{$name}<br>',
                    name=i.名称)
                if i.备注 is not None and i.备注 != '':
                    tempstr += trans('{$value}</font><br>', value=i.备注)
                else:
                    tempstr += '</font>'
                tempstr += trans('{所在等级}：$level<br>', level=i.所在等级)
                tempstr += trans('{等级上限}：$limit', limit=i.等级上限)
                if i.是否主动 == 1:
                    tempstr += trans('<br>{百分比}：$value%',
                                     value=int(i.等效百分比(self.角色属性A.武器类型)))
                    if i.TP上限 != 0:
                        tempstr += trans('<br>{TP成长}：$value',
                                         value=to_percent(i.TP成长))
                        tempstr += trans('<br>{TP上限}：$value', value=i.TP上限)
                tempstr += '</font>'
                x.setToolTip(tempstr)
                x.move(横坐标, 纵坐标 + 7)
                横坐标 += 40
                x = QLabel('Lv' + str(i.基础等级), self.main_frame2)
                x.resize(40, 28)
                x.move(横坐标, 纵坐标 + 7)
                x.setStyleSheet(标签样式)
                横坐标 += 40
                self.等级调整[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                self.等级调整[self.角色属性A.技能序号[i.名称]].move(横坐标, 纵坐标 + 10)
                横坐标 -= 80
                纵坐标 += 纵坐标偏移量

        横坐标 = 横坐标 + 80 + 50
        纵坐标 = 30

        for i in skill_sort:
            if i.是否有伤害 == 1:
                if i.TP上限 != 0:
                    self.TP输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                    self.TP输入[self.角色属性A.技能序号[i.名称]].move(横坐标, 纵坐标)
                纵坐标 += 纵坐标偏移量

        横坐标 = 横坐标 + 50
        纵坐标 = 30

        for i in skill_sort:
            if i.是否有伤害 == 1:
                self.次数输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                self.次数输入[self.角色属性A.技能序号[i.名称]].move(横坐标, 纵坐标)
                self.宠物次数[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                self.宠物次数[self.角色属性A.技能序号[i.名称]].move(横坐标 + 50, 纵坐标)
                if 切装模式 == 1:
                    self.技能切装[self.角色属性A.技能序号[i.名称]].move(
                        横坐标 + 55 + 词条框宽度, 纵坐标 + 5)
                纵坐标 += 纵坐标偏移量

        横坐标 = 横坐标 + 130
        纵坐标 = 20

        for i in skill_sort:
            if i.是否有伤害 == 0:
                x = QLabel(self.main_frame2)
                x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
                x.resize(28, 28)
                tempstr = trans(
                    '<font face="宋体"><font color="#FF6666">{$name}<br>',
                    name=i.名称)
                if i.备注 is not None and i.备注 != '':
                    tempstr += trans('{$value}</font><br>', value=i.备注)
                else:
                    tempstr += '</font>'
                tempstr += trans('{所在等级}：$level<br>', level=i.所在等级)
                tempstr += trans('{等级上限}：$limit', limit=i.等级上限)
                tempstr += '</font>'
                x.setToolTip(tempstr)
                x.move(横坐标, 纵坐标 + 7)
                横坐标 += 40
                x = QLabel('Lv' + str(i.基础等级), self.main_frame2)
                x.resize(40, 28)
                x.move(横坐标, 纵坐标 + 7)
                x.setStyleSheet(标签样式)
                横坐标 += 40
                self.等级调整[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                self.等级调整[self.角色属性A.技能序号[i.名称]].move(横坐标, 纵坐标 + 10)
                横坐标 -= 80
                纵坐标 += 纵坐标偏移量

        x = 横坐标 + 20
        y = 纵坐标 + 60
        self.觉醒选择 = QLabel(self.main_frame2)
        self.觉醒选择.setPixmap(QPixmap('./ResourceFiles/img/觉醒选择.png'))
        self.觉醒选择.resize(120, 100)
        self.觉醒选择.move(x, y - 20)

        self.BUFF = QLabel(self.main_frame2)
        self.BUFF.setPixmap(
            QPixmap('./ResourceFiles/' + self.角色属性A.实际名称 + "/技能/BUFF.png"))
        self.BUFF.resize(28, 28)
        self.BUFF.move(x - 2, y - 40)
        self.BUFF.setToolTip(
            trans('<font size="3" face="宋体">{最高值参考}：$value</font>',
                  value=to_percent(self.角色属性A.主BUFF - 1)))

        self.BUFF输入.setText(str('%.1f' % ((self.角色属性A.主BUFF - 1) * 100)))
        self.BUFF输入.resize(50, 25)
        self.BUFF输入.move(x + 38, y - 38)
        self.BUFF输入.setStyleSheet(输入框样式)
        self.BUFF输入.setAlignment(Qt.AlignCenter)

        self.一觉图片 = QLabel(self.main_frame2)
        self.一觉图片.setPixmap(self.技能图片[self.一觉序号])
        self.一觉图片.resize(28, 28)
        self.一觉图片.move(x + 7, y + 8)
        self.二觉图片 = QLabel(self.main_frame2)
        self.二觉图片.setPixmap(self.技能图片[self.二觉序号])
        self.二觉图片.resize(28, 28)
        self.二觉图片.move(x + 52, y + 8)
        self.一觉遮罩 = QPushButton(self.main_frame2)
        self.一觉遮罩.resize(38, 50)
        self.一觉遮罩.move(x + 2, y + 5)
        self.一觉遮罩.setStyleSheet(
            "QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}"
        )
        self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
        self.一觉遮罩.clicked.connect(lambda state, index=1: self.强化觉醒选择(index))
        self.二觉遮罩 = QPushButton(self.main_frame2)
        self.二觉遮罩.resize(38, 50)
        self.二觉遮罩.move(x + 47, y + 5)
        self.二觉遮罩.setStyleSheet(
            "QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}"
        )
        self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)
        self.二觉遮罩.clicked.connect(lambda state, index=2: self.强化觉醒选择(index))

        for i in range(3):
            self.护石栏[i].addItems(self.护石选项)
        self.护石类型选项 = []

        for i in range(9):
            self.符文.append(MyQComboBox(self.main_frame2))
            self.符文[i].addItems(self.符文选项)
            self.符文效果.append(MyQComboBox(self.main_frame2))
            self.符文效果[i].addItems(符文效果选项)

        横坐标 = 480
        纵坐标 = 20
        行高 = 18
        x = QLabel(trans("{护石}Ⅰ"), self.main_frame2)
        x.move(横坐标, 纵坐标)
        x.setStyleSheet(标签样式)
        y = MyQComboBox(self.main_frame2)
        y.move(横坐标 + 65, 纵坐标)
        y.resize(65, 行高)
        self.护石类型选项.append(y)
        纵坐标 += 21
        self.护石栏[0].move(横坐标, 纵坐标)
        self.护石栏[0].resize(130, 行高)
        self.护石栏[0].currentIndexChanged.connect(
            lambda state, index=0: self.护石类型选项更新(index))
        纵坐标 += 25
        for i in range(3):
            tempstr = trans("{符文}$value{选择}：", value=i + 1)
            x = QLabel(tempstr, self.main_frame2)
            x.move(横坐标, 纵坐标)
            x.setStyleSheet(标签样式)
            纵坐标 += 21
            self.符文[i].move(横坐标, 纵坐标)
            self.符文[i].resize(130, 行高)
            self.符文[i].activated.connect(
                lambda state, index=i: self.符文技能更改(index))
            纵坐标 += 21
            self.符文效果[i].move(横坐标, 纵坐标)
            self.符文效果[i].resize(130, 行高)
            self.符文效果[i].activated.connect(
                lambda state, index=i: self.符文效果更改(index))
            纵坐标 += 25

        横坐标 = 650
        纵坐标 = 20
        x = QLabel(trans("{护石}Ⅱ"), self.main_frame2)
        x.move(横坐标, 纵坐标)
        x.setStyleSheet(标签样式)
        y = MyQComboBox(self.main_frame2)
        y.move(横坐标 + 65, 纵坐标)
        y.resize(65, 行高)
        self.护石类型选项.append(y)
        纵坐标 += 21
        self.护石栏[1].move(横坐标, 纵坐标)
        self.护石栏[1].resize(130, 行高)
        self.护石栏[1].currentIndexChanged.connect(
            lambda state, index=1: self.护石类型选项更新(index))
        纵坐标 += 25
        for i in range(3, 6):
            tempstr = trans("{符文}$value{选择}：", value=i + 1)
            x = QLabel(tempstr, self.main_frame2)
            x.move(横坐标, 纵坐标)
            x.setStyleSheet(标签样式)
            纵坐标 += 21
            self.符文[i].move(横坐标, 纵坐标)
            self.符文[i].resize(130, 行高)
            纵坐标 += 21
            self.符文效果[i].move(横坐标, 纵坐标)
            self.符文效果[i].resize(130, 行高)
            纵坐标 += 25

        横坐标 = 820
        纵坐标 = 20
        x = QLabel(trans("{护石}Ⅲ"), self.main_frame2)
        x.move(横坐标, 纵坐标)
        x.setStyleSheet(标签样式)
        y = MyQComboBox(self.main_frame2)
        y.move(横坐标 + 65, 纵坐标)
        y.resize(65, 行高)
        self.护石类型选项.append(y)
        纵坐标 += 21
        self.护石栏[2].move(横坐标, 纵坐标)
        self.护石栏[2].resize(130, 行高)
        self.护石栏[2].currentIndexChanged.connect(
            lambda state, index=2: self.护石类型选项更新(index))
        纵坐标 += 25
        for i in range(6, 9):
            tempstr = trans("{符文}$value{选择}：", value=i + 1)
            x = QLabel(tempstr, self.main_frame2)
            x.move(横坐标, 纵坐标)
            x.setStyleSheet(标签样式)
            纵坐标 += 21
            self.符文[i].move(横坐标, 纵坐标)
            self.符文[i].resize(130, 行高)
            纵坐标 += 21
            self.符文效果[i].move(横坐标, 纵坐标)
            self.符文效果[i].resize(130, 行高)
            纵坐标 += 25

        for i in range(3):
            self.护石类型选项[i].addItem('魔界')
            self.护石类型选项[i].addItem('圣痕')
            self.护石类型选项[i].currentIndexChanged.connect(
                lambda state, index=i: self.护石描述更新(index))

        self.复选框列表 = []
        self.复选框列表list = []

        for i in 选项设置列表:
            if (觉醒开关 == 0 or "·" not in self.初始属性.实际名称) and i.名称 == '屏蔽三觉':
                continue
            self.复选框列表.append(QCheckBox(trans(i.名称), self.main_frame2))
            self.复选框列表list.append(i.名称)

        奶量buff力智label = QLabel(trans("奶量buff力智"), self.main_frame2)
        奶量buff力智label.setStyleSheet(标签样式)
        奶量buff力智label.setAlignment(Qt.AlignCenter)

        偏移 = (35 if self.初始属性.远古记忆 != -1 else 0) + (35 if self.初始属性.刀魂之卡赞 != -1
                                                    else 0) + 35
        奶量buff力智label.move(970, 24 + counter * 80 + 10 + 偏移)
        奶量buff力智输入框 = QLineEdit(self.main_frame2)
        奶量buff力智输入框.setStyleSheet(文本框样式黄)
        奶量buff力智输入框.move(1050, 21 + counter * 80 + 10 + 偏移)
        奶量buff力智输入框.resize(50, 20)
        self.奶量buff输入.append(奶量buff力智输入框)

        奶量buff三攻label = QLabel(trans("奶量buff三攻"), self.main_frame2)
        奶量buff三攻label.setStyleSheet(标签样式)
        奶量buff三攻label.setAlignment(Qt.AlignCenter)
        奶量buff三攻label.move(970, 24 + counter * 80 + 40 + 偏移)
        奶量buff三攻输入框 = QLineEdit(self.main_frame2)
        奶量buff三攻输入框.setStyleSheet(文本框样式黄)
        奶量buff三攻输入框.move(1050, 15 + counter * 80 + 45 + 偏移)
        奶量buff三攻输入框.resize(50, 20)
        self.奶量buff输入.append(奶量buff三攻输入框)

        counter = 0

        for i in self.复选框列表:
            i.setStyleSheet(复选框样式)
            i.resize(125, 20)
            i.move(980, 10 + counter * 24)
            if counter < 7 and 调试开关 == 0:
                i.setChecked(True)
            counter += 1

        sign = 0
        if self.初始属性.远古记忆 != -1:
            i = QLabel(self.main_frame2)
            i.setPixmap(QPixmap('./ResourceFiles/img/远古记忆.png'))
            i.resize(28, 28)
            i.move(1000, 15 + counter * 24)
            self.远古记忆 = MyQComboBox(self.main_frame2)
            self.远古记忆.currentIndexChanged.connect(
                lambda state, index=100: self.等级调整标注(index))
            for i in range(12):
                self.远古记忆.addItem(str(i))
            self.远古记忆.resize(50, 20)
            self.远古记忆.move(1035, 19 + counter * 24)
            sign = 30

        if self.初始属性.刀魂之卡赞 != -1:
            i = QLabel(self.main_frame2)
            i.setPixmap(QPixmap('./ResourceFiles/img/刀魂之卡赞.png'))
            i.resize(28, 28)
            i.move(1000, 15 + sign + counter * 24)
            self.刀魂之卡赞 = MyQComboBox(self.main_frame2)
            self.刀魂之卡赞.currentIndexChanged.connect(
                lambda state, index=200: self.等级调整标注(index))
            for i in range(12):
                self.刀魂之卡赞.addItem(str(i))
            self.刀魂之卡赞.resize(50, 20)
            self.刀魂之卡赞.move(1035, 19 + sign + counter * 24)

        x = QLabel(trans("{攻击目标}："), self.main_frame2)
        x.move(660, self.height() - 62)
        x.resize(70, 20)
        x.setStyleSheet(标签样式)
        self.攻击目标 = MyQComboBox(self.main_frame2)
        for i in 攻击目标:
            self.攻击目标.addItem(i[0])
        self.攻击目标.move(730, self.height() - 63)
        self.攻击目标.resize(110, 20)
        x = QLabel(trans("{时间输入}："), self.main_frame2)
        x.move(850, self.height() - 62)
        x.resize(70, 20)
        x.setStyleSheet(标签样式)
        self.时间输入.addItems(
            ['1', '10', '15', '20', '25', '30', '45', '50', '60'])
        self.时间输入.setEditable(True)
        self.时间输入.move(920, self.height() - 63)
        self.时间输入.resize(50, 20)

        self.技能存档选择 = MyQComboBox(self.main_frame2)
        self.技能存档选择.move(990, self.height() - 105)
        self.技能存档选择.resize(110, 20)
        self.技能存档选择.currentIndexChanged.connect(lambda state: self.技能存档更换())

        self.计算按钮2 = QPushButton(trans('开始计算'), self.main_frame2)
        self.计算按钮2.clicked.connect(lambda state: self.计算())
        self.计算按钮2.move(990, self.height() - 70)
        self.计算按钮2.resize(110, 30)
        self.计算按钮2.setStyleSheet(按钮样式)

    def 界面3(self):
        # increase_counter(ga_category="carry界面", name="基础/细节/修正")
        # 第三个布局界面
        self.属性设置输入 = []
        self.细节选项输入 = []

        self.列名称 = []
        self.行名称 = []

        名称 = QLabel(trans(表头名称1), self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(标签样式)
        名称.resize(80, 25)
        名称.move(10, 文本框间隔)

        m = -1
        for i in 列名称1:
            m += 1
            名称 = QLabel(trans(i), self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            if i == "选项":
                名称.resize(文本框宽度 * 2 + 5, 25)
            else:
                名称.resize(文本框宽度, 25)
            名称.move(95 + m * (文本框宽度 + 5), 文本框间隔)
            self.列名称.append(i)

        n = -1
        for j in 行名称1.keys():
            n += 1
            名称 = QLabel(trans(j), self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            if 行名称1[j] == 1:
                名称.setStyleSheet(标签样式_2)
            else:
                名称.setStyleSheet(标签样式)
            名称.resize(80, 25)
            名称.move(10, 文本框间隔 + 30 + n * 30)
            self.行名称.append(j)

        m = -1
        for i in 列名称1:
            m += 1
            templist = []
            n = -1
            for j in 行名称1.keys():
                n += 1
                if i == "选项":
                    templist.append(MyQComboBox(self.main_frame3))
                    templist[n].resize(文本框宽度 * 2 + 5, 22)
                    templist[n].setStyleSheet(下拉框样式_detail)
                    if 行1选项[j][0] != -1:
                        templist[n].addItem('无')
                        for s_id in 行1选项[j]:
                            templist[n].addItem(细节选项列表[s_id].描述)
                    else:
                        templist[n].setDisabled(True)
                else:
                    templist.append(QLineEdit(self.main_frame3))
                    if 行名称1[j] == 1:
                        templist[n].setStyleSheet(文本框样式黄)
                    else:
                        templist[n].setStyleSheet(文本框样式白)
                    templist[n].resize(文本框宽度, 22)
                    templist[n].setAlignment(Qt.AlignCenter)
                templist[n].move(95 + m * (文本框宽度 + 5), 文本框间隔 + 30 + n * 30 + 2)
            if i == "选项":
                self.细节选项输入.append(templist)
            else:
                self.属性设置输入.append(templist)

        名称 = QLabel(trans(表头名称2), self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(标签样式)
        名称.resize(80, 25)
        名称.move(160 + (len(列名称1) + 1) * 文本框宽度, 文本框间隔)

        m = -1
        for i in 列名称2:
            m += 1
            名称 = QLabel(trans(i), self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            if i == "技能":
                名称.resize(155, 25)
            elif i == "选项":
                名称.resize(文本框宽度 * 2 + 5, 25)
            else:
                名称.resize(文本框宽度, 25)
            名称.move(245 + (len(列名称1) + 1) * 文本框宽度 + m * (文本框宽度 + 5), 文本框间隔)
            self.列名称.append(trans(i))
            if i == "选项":
                m += 1

        n = -1
        for j in 行名称2.keys():
            n += 1
            名称 = QLabel(trans(j), self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            if 行名称2[j] == 1:
                名称.setStyleSheet(标签样式_2)
            else:
                名称.setStyleSheet(标签样式)
            名称.resize(80, 25)
            名称.move(160 + (len(列名称1) + 1) * 文本框宽度, 文本框间隔 + 30 + n * 30)
            self.行名称.append(trans(j))
        count = len(self.细节选项输入)
        m = -1
        for i in 列名称2:
            m += 1
            templist = []
            n = -1
            for j in 行名称2.keys():
                n += 1
                if i == "选项":
                    templist.append(MyQComboBox(self.main_frame3))
                    templist[n].resize(文本框宽度 * 2 + 5, 22)
                    templist[n].setStyleSheet(下拉框样式_detail)
                    if 行2选项[j][0] != -1:
                        templist[n].addItem('无')
                        templist[n].setPlaceholderText("增伤词条选择")
                        templist[n].currentIndexChanged.connect(
                            lambda state, index=templist[n]: self.细节增伤选项颜色更新(
                                index))
                        for s_id in 行2选项[j]:
                            templist[n].addItem(细节选项列表[s_id].描述)
                    else:
                        templist[n].setDisabled(True)
                elif i == "技能":
                    templist.append(MyQComboBox(self.main_frame3))
                    templist[n].resize(155, 22)
                    templist[n].setStyleSheet(下拉框样式_detail)
                    cur = 行2技能[j][0]
                    if cur == -1:
                        templist[n].setDisabled(True)
                        pass
                    elif cur in [100, 999]:
                        templist[n].addItem('无')
                        if cur == 999:
                            skills = [
                                i.名称 for i in self.角色属性A.技能栏 if i.所在等级 <= 85
                            ]
                        else:
                            skills = [
                                i.名称 for i in self.角色属性A.技能栏
                                if i.所在等级 <= 70 and i.所在等级 not in [48, 50]
                            ]
                            if self.角色属性A.实际名称 == '极诣·黑暗武士':
                                skills.append('幽魂剑')
                            if self.角色属性A.实际名称 == '知源·缔造者':
                                skills.append('末日虫洞')

                        for skill_name in skills:
                            templist[n].addItem(
                                trans('{$name}Lv+1', name=skill_name),
                                skill_name + "Lv+1")
                    else:
                        templist[n].addItem('无')
                        for s_id in 行2技能[j]:
                            templist[n].addItem(细节选项列表[s_id].描述)
                else:
                    templist.append(QLineEdit(self.main_frame3))
                    if 行名称2[j] == 1:
                        templist[n].setStyleSheet(文本框样式黄)
                    else:
                        templist[n].setStyleSheet(文本框样式白)
                    templist[n].resize(文本框宽度, 22)
                    templist[n].setAlignment(Qt.AlignCenter)
                templist[n].move(
                    245 + (len(列名称1) + 1) * 文本框宽度 + m * (文本框宽度 + 5),
                    文本框间隔 + 30 + n * 30 + 2)
            if i in ["选项", "技能"]:
                self.细节选项输入.append(templist)
                m += 1
            else:
                self.属性设置输入.append(templist)

        self.修正列表名称 = [
            trans('力智') + '%',
            trans('三攻') + '%',
            trans('黄字'),
            trans('白字'),
            trans('属白'),
            trans('暴伤'),
            trans('终伤'),
            trans('技攻')
        ]

        距离 = 30
        templist = []

        for i in range(len(self.修正列表名称)):
            名称 = QLabel(self.修正列表名称[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(50, 25)
            名称.move(距离 + i * 55, 570)
            templist.append(QLineEdit(self.main_frame3))
            templist[i].setAlignment(Qt.AlignCenter)
            templist[i].setStyleSheet(文本框样式白)
            templist[i].resize(50, 22)
            templist[i].move(距离 + i * 55, 610)
        self.属性设置输入.append(templist)

        count = 0
        self.时装选项 = []
        for i in ['头部', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']:
            名称 = QLabel(trans(i), self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(50, 25)
            名称.move(520 + count * 55, 570)
            self.时装选项.append(MyQComboBox(self.main_frame3))
            self.时装选项[count].setStyleSheet(下拉框样式_detail)
            self.时装选项[count].addItems(['高级', '节日', '稀有', '神器'])
            self.时装选项[count].resize(50, 22)
            self.时装选项[count].move(520 + count * 55, 610)
            self.时装选项[count].currentIndexChanged.connect(
                lambda state, index=count: self.时装选项更新(index))
            count += 1

        self.时装选项.append(MyQComboBox(self.main_frame3))
        self.时装选项[8].setStyleSheet(下拉框样式_detail)
        self.时装选项[8].addItems([
            trans('高级套装') + '[8]',
            trans('节日套装') + '[8]',
            trans('稀有套装') + '[8]',
            trans('神器套装') + '[8]'
        ])
        self.时装选项[8].resize(100, 22)
        self.时装选项[8].move(990, 570)
        self.时装选项[8].currentIndexChanged.connect(
            lambda state, index=8: self.时装选项更新(index))

        self.计算按钮3 = QPushButton(trans('开始计算'), self.main_frame3)
        self.计算按钮3.clicked.connect(lambda state: self.计算())
        self.计算按钮3.move(990, 610)
        self.计算按钮3.resize(110, 30)
        self.计算按钮3.setStyleSheet(按钮样式)

    def 界面5(self):
        # increase_counter(ga_category="carry界面", name="自选装备计算")
        # 第五个布局
        标签 = QLabel(trans('单件选择'), self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(240, 25)
        标签.move(70, 20)

        标签 = QLabel(trans('锁定'), self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(70, 25)
        标签.move(10, 20)

        self.图片显示 = []

        count = 0
        self.自选装备 = []
        self.自选装备结果 = []
        if 切装模式 == 1:
            self.装备切装 = []
            self.切装修正属性 = []
        self.装备锁定 = []
        for i in 部位列表:
            锁定选择 = QCheckBox(trans(i), self.main_frame5)
            锁定选择.setStyleSheet(复选框样式)
            锁定选择.resize(70, 22)
            锁定选择.move(10, 50 + 30 * count)
            self.装备锁定.append(锁定选择)

            combo = MyQComboBox(self.main_frame5)

            combo.resize(220, 22)
            combo.move(90, 50 + 30 * count)
            combo.currentIndexChanged.connect(
                lambda state, index=count: self.自选装备更改(index))
            if 切装模式 == 1:
                temp = QCheckBox(self.main_frame5)
                temp.setStyleSheet(复选框样式)
                self.装备切装.append(temp)
                self.装备切装[count].move(320, 55 + 30 * count)
            for j in equ.get_equ_list():
                if j.部位 == i:
                    if i == '武器':
                        if j.类型 in self.角色属性A.武器选项:
                            combo.addItem(j.名称)
                    else:
                        combo.addItem(j.名称)
            self.自选装备.append(combo)
            count += 1

        if 切装模式 == 1:
            num = 0
            for i in trans(['力量', '智力', '物攻', '魔攻', '独立', '属强']):
                标签 = QLabel(i, self.main_frame5)
                标签.setAlignment(Qt.AlignCenter)
                标签.setStyleSheet(标签样式)
                标签.resize(45, 25)
                标签.move(30 + 50 * num, 60 + 30 * count)
                self.切装修正属性.append(QLineEdit(self.main_frame5))
                self.切装修正属性[num].setAlignment(Qt.AlignCenter)
                self.切装修正属性[num].setStyleSheet(输入框样式)
                self.切装修正属性[num].resize(45, 22)
                self.切装修正属性[num].move(30 + 50 * num, 85 + 30 * count)
                num += 1

        self.计算标识 = 1

        横坐标 = 355
        标签 = QLabel(trans('批量选择'), self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(160, 25)
        标签.move(横坐标, 20)

        套装类型 = ['防具', '首饰', '特殊', '上链左', '镯下右', '环鞋指']
        count = 0
        self.自选套装 = []
        for i in 套装类型:
            套装名称 = []
            combo = MyQComboBox(self.main_frame5)
            for j in equ.get_suit_list():
                if j.名称 not in 套装名称 and j.类型 == i:
                    套装名称.append(j.名称)
                    combo.addItem(j.名称)
            combo.resize(160, 22)
            combo.move(横坐标, 50 + 30 * count)
            combo.activated.connect(
                lambda state, index=count: self.自选套装更改(index))
            self.自选套装.append(combo)
            count += 1

        self.神话部位选项 = MyQComboBox(self.main_frame5)
        self.神话部位选项.addItems(['神话部位：无', '神话部位：上衣', '神话部位：手镯', '神话部位：耳环'])
        self.神话部位选项.resize(160, 22)
        self.神话部位选项.move(横坐标, 50 + 30 * count)
        self.神话部位选项.activated.connect(lambda state: self.神话部位更改())

        count += 1
        self.改造套装 = MyQComboBox(self.main_frame5)
        for n in equ.get_equ_list():
            try:
                self.改造套装.addItem(n.关联套装)
            except:
                pass
        self.改造套装.resize(160, 22)
        self.改造套装.move(横坐标, 50 + 30 * count)
        self.改造套装.activated.connect(lambda state: self.改造套装更改())

        count += 1
        self.转甲选项 = QCheckBox(trans('85SS转甲'), self.main_frame5)
        self.转甲选项.resize(80, 22)
        self.转甲选项.move(横坐标 + 40, 50 + 30 * count)
        self.转甲选项.setChecked(True)
        self.转甲选项.setStyleSheet(复选框样式)
        self.转甲选项.stateChanged.connect(lambda state: self.自选计算(1))

        count += 1
        # 一键修正按钮添加
        一键站街修正名称 = trans(['站街力智', '站街三攻', '站街属强'])
        for i in range(len(一键站街修正名称)):
            名称 = QLabel(一键站街修正名称[i], self.main_frame5)
            名称.setAlignment(Qt.AlignCenter)
            名称.move(横坐标 - 5 + i * 57, 50 + 30 * count)
            名称.resize(52, 25)
            名称.setStyleSheet(标签样式)
            self.一键站街设置输入.append(QLineEdit(self.main_frame5))
            self.一键站街设置输入[i + 3].setAlignment(Qt.AlignCenter)
            self.一键站街设置输入[i + 3].setStyleSheet(输入框样式)
            self.一键站街设置输入[i + 3].resize(52, 22)
            self.一键站街设置输入[i + 3].move(横坐标 - 5 + i * 57, 80 + 30 * count)

        count += 2
        一键修正按钮 = QPushButton(trans('一键修正面板细节'), self.main_frame5)
        一键修正按钮.clicked.connect(lambda state: self.一键修正(1))
        一键修正按钮.move(横坐标 - 5, 50 + 30 * count)
        一键修正按钮.resize(165, 25)
        一键修正按钮.setStyleSheet(按钮样式)

        标签 = QLabel(trans('辟邪玉提升率(理论值仅供参考)'), self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(200, 25)
        标签.move(525, 20)

        self.辟邪玉提升率1 = []
        self.辟邪玉提升率2 = []
        count = 0
        for i in 辟邪玉列表:
            if i.名称 != '无':
                if i.最大值 != 1:
                    temp = trans(i.名称) + '+' + str(i.最大值) + '%'
                else:
                    temp = trans(i.名称) + '+' + str(i.最大值)
                self.辟邪玉提升率1.append(QLabel(temp, self.main_frame5))
                self.辟邪玉提升率1[count].setAlignment(Qt.AlignCenter)
                self.辟邪玉提升率1[count].setStyleSheet(标签样式)
                self.辟邪玉提升率1[count].resize(180, 25)
                self.辟邪玉提升率1[count].move(520, 50 + 30 * count)
                self.辟邪玉提升率2.append(QLabel('0.00%', self.main_frame5))
                self.辟邪玉提升率2[count].setAlignment(Qt.AlignCenter)
                self.辟邪玉提升率2[count].setStyleSheet(标签样式)
                self.辟邪玉提升率2[count].resize(60, 25)
                self.辟邪玉提升率2[count].move(710, 50 + 30 * count)
                count += 1

        初始x = 805
        初始y = 20
        图片显示 = QLabel(self.main_frame5)
        图片显示.setPixmap(self.输出背景图片)
        图片显示.setAlignment(Qt.AlignTop)
        图片显示.resize(268, 546)
        图片显示.move(初始x, 初始y + 11)
        人物 = QLabel(self.main_frame5)
        图片 = QPixmap('./ResourceFiles/' + self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(初始x + 90 + int(45 - 图片.width() / 2), 初始y + 40)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)

        偏移量 = 187
        x坐标 = [
            32, 0, 0, 32, 0, 偏移量, 偏移量 + 32, 偏移量 + 32, 偏移量, 偏移量, 偏移量 + 32, 32
        ]
        y坐标 = [0, 0, 32, 32, 64, 0, 0, 32, 64, 32, 64, 64]

        for i in range(12):
            self.图片显示.append(QLabel(self.main_frame5))
            self.图片显示[i].setMovie(
                equ.get_img_by_name(self.自选装备[i].currentData()))
            self.图片显示[i].resize(26, 26)
            self.图片显示[i].move(初始x + 10 + x坐标[i], 初始y + 31 + y坐标[i])
            self.图片显示[i].setAlignment(Qt.AlignCenter)

        self.面板显示 = []
        for i in range(18):
            self.面板显示.append(QLabel(self.main_frame5))

        self.面板布局设置(self.面板显示, 1)

        self.词条显示 = []
        for i in range(12):
            self.词条显示.append(QLabel(self.main_frame5))

        j = 312 + 初始y
        for i in self.词条显示:
            i.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            i.move(5 + 初始x, j)
            i.resize(180, 17)
            i.setAlignment(Qt.AlignLeft)
            j += 17

        self.总伤害 = QLabel(self.main_frame5)
        self.总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        self.总伤害.resize(250, 36)
        self.总伤害.move(10 + 初始x, 520 + 初始y)
        self.总伤害.setAlignment(Qt.AlignCenter)

        self.套装名称显示 = []
        for i in range(13):
            self.套装名称显示.append(QLabel(self.main_frame5))
            self.套装名称显示[i].move(114 + 初始x, 128 + 180 + 17 * i + 初始y)
            self.套装名称显示[i].resize(150, 18)
            self.套装名称显示[i].setAlignment(Qt.AlignCenter)

        self.打造显示 = []
        for i in range(13):
            self.打造显示.append(QLabel(self.main_frame5))
            self.打造显示[i].move(-100, -100)

        自选计算按钮 = QPushButton(trans('查看详情'), self.main_frame5)
        自选计算按钮.clicked.connect(lambda state: self.自选计算())
        自选计算按钮.move(995, 610)
        自选计算按钮.resize(80, 28)
        自选计算按钮.setStyleSheet(按钮样式)

        self.基准值 = []

        设置基准值 = QPushButton(trans('设为基准'), self.main_frame5)
        设置基准值.clicked.connect(lambda state: self.基准值设置())
        设置基准值.move(900, 610)
        设置基准值.resize(80, 28)
        设置基准值.setStyleSheet(按钮样式)

        清空基准值 = QPushButton(trans('清空基准'), self.main_frame5)
        清空基准值.clicked.connect(lambda state: self.基准值设置(1))
        清空基准值.move(805, 610)
        清空基准值.resize(80, 28)
        清空基准值.setStyleSheet(按钮样式)

        self.对比格式 = QCheckBox(trans('数值对比'), self.main_frame5)
        self.对比格式.stateChanged.connect(lambda state: self.自选计算(1))
        self.对比格式.move(615, 612)
        self.对比格式.resize(70, 24)
        self.对比格式.setStyleSheet(复选框样式)
        if 多语言开关 == 0:
            名望设置 = QPushButton(trans('名望细节'), self.main_frame5)
            名望设置.clicked.connect(lambda _: self.名望设置())
            名望设置.move(710, 610)
            名望设置.resize(80, 28)
            名望设置.setStyleSheet(按钮样式)

    def 名望设置(self):
        increase_counter(ga_category="carry详细功能使用", name="名望")

        def createClient():
            store.set("/fame/temp/property", self)
            # 设置图标和背景 临时做法
            store.const("/app/window/icon", self.icon)
            store.const("/app/window/background_image", self.主背景图片)
            store.watch("/fame/event/changed", lambda _, : self.自选计算(1))
            client = 名望窗口()
            client.初始化()
            return client

        DefaultDialogRegister.showDialog("base_fame({})".format(type(self)),
                                         createClient, self)

    def 自选装备更改(self, index=0):
        try:
            self.图片显示[index].setMovie(
                equ.get_img_by_name(self.自选装备[index].currentData()))
        except:
            pass

        if self.初始属性.职业分类 == '输出':
            if self.当前页面 == 5 and self.计算标识 == 1:
                self.自选计算(1)
        else:
            if self.当前页面 == 4 and self.计算标识 == 1:
                self.自选计算(1)

    def 自选套装更改(self, index):
        self.计算标识 = 0
        name = self.自选套装[index].currentData()
        for i in range(11):
            if self.装备锁定[i].isChecked():
                continue
            x = -1
            for j in equ.get_equ_list():
                if j.部位 == 部位列表[i]:
                    x += 1
                    if j.所属套装2 == name:
                        self.自选装备[i].setCurrentIndex(x)
                        break
                    elif j.所属套装 == name and j.品质 != '神话':
                        self.自选装备[i].setCurrentIndex(x)
                        break
        self.计算标识 = 1
        self.自选计算(1)

    def 界面6(self):
        # increase_counter(ga_category="carry界面", name="辟邪玉/希洛克/黑鸦/奥兹玛")
        横坐标 = 10
        纵坐标 = 0

        标签 = QLabel(trans('辟邪玉计算 （鼠标悬停查看算法）'), self.main_frame6)
        标签.setStyleSheet(标签样式 + 'QLabel{font-size:13px;}')
        标签.resize(290, 20)
        标签.move(横坐标 + 10, 纵坐标)
        标签.setAlignment(Qt.AlignCenter)

        temp = '<font face="宋体">{}<br><br>'.format(
            trans('假定基础伤害为100，词条1=50%，词条2=50%：'))
        temp += trans('5%黄字增幅，佩戴前：200，佩戴后：205<br>')
        temp += trans('暴伤终伤白字属白力智三攻同上，黄字向下取整<br>')
        temp += trans('技攻辟邪玉加成等级技攻(歧路腰类)<br>不加成具体技能技攻(歧路鞋类)<br><br>')
        temp += trans(
            '3%技攻增幅，佩戴前：100*1.5*1.5=225<br>佩戴后：100*1.515*1.515=229.5225<br><br>'
        )
        # temp += '附加、最终、百分力智增幅：宠物相关词条不享受加成<br>'
        temp += trans('属强增幅：唤醒(13)婚房(8)药剂和技能属强不享受加成<br>')
        temp += trans('进图触发属强单独计算向下取整<br><br>')
        temp += '<font color="#B99460">{}</font></font>'.format(
            trans(
                '属白增幅分对应属性，计算器未作区分<br>双属性附加(星之海)需手动计算并在第三页修正<br><br>计算方式仅供参考，请以实际游戏为准！'
            ))

        标签.setToolTip(temp)

        self.辟邪玉选择 = []
        self.辟邪玉数值 = []
        for i in range(4):
            x = MyQComboBox(self.main_frame6)
            for j in 辟邪玉列表:
                x.addItem(j.名称)
            x.resize(200, 20)
            x.move(横坐标, 纵坐标 + (i + 1) * 25)
            x.currentIndexChanged.connect(
                lambda state, index=i: self.辟邪玉数值选项更新(index))
            self.辟邪玉选择.append(x)
            y = MyQComboBox(self.main_frame6)
            y.resize(80, 20)
            y.move(横坐标 + 220, 纵坐标 + (i + 1) * 25)
            self.辟邪玉数值.append(y)

        标签 = QLabel(trans('黑鸦遴选词条'), self.main_frame6)
        标签.setStyleSheet(标签样式 + 'QLabel{font-size:13px;}')
        标签.resize(300, 20)
        标签.move(横坐标 + 10, 纵坐标 + 330 - 20)
        标签.setAlignment(Qt.AlignCenter)

        名称 = trans(['武　　器', '戒　　指', '辅助装备', '下　　装'])

        self.黑鸦词条 = []
        for i in range(4):
            x = QLabel(名称[i], self.main_frame6)
            x.setStyleSheet(标签样式 +
                            'QLabel{font-size:13px;};text-align: justify;')
            # x.setStyleSheet('text-align: justify')
            x.resize(55, 20)
            x.move(横坐标, 纵坐标 - 145 + (i + 20) * 25 - 20)
            tem = []
            tem.append(MyQComboBox(self.main_frame6))
            tem[-1].setStyleSheet(下拉框样式)
            if i == 0:
                tem[0].addItems(['无', '计算最高', '自选数值', '自选数值-觉醒'])
                tem[0].resize(91, 20)
                tem[0].move(横坐标 + 60, 纵坐标 - 20 + 25 * (i + 15) - 20)
                tem[0].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦词条更新(index))
            else:
                tem[0].addItems(['无', '计算最高', '自选数值'])
                tem[0].resize(91, 20)
                tem[0].move(横坐标 + 60, 纵坐标 - 20 + 25 * (i + 15) - 20)
                tem[0].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦词条更新(index))
            tem.append(MyQComboBox(self.main_frame6))
            tem[-1].setStyleSheet(下拉框样式)
            tem[1].resize(70, 20)
            tem[1].move(横坐标 + 161, 纵坐标 - 20 + 25 * (i + 15) - 20)
            # if i > 0:
            for item in 词条属性列表:
                tem[1].addItem(item.描述)
            # else:
            #     for item in 黑鸦武器属性列表:
            #         tem[1].addItem(item.描述)
            #         tem[1].currentIndexChanged.connect(lambda state:self.黑鸦武器词条更新())
            # tem[1].currentIndexChanged.connect(lambda state: self.希洛克武器词条更新())
            tem.append(MyQComboBox(self.main_frame6))
            tem[-1].setStyleSheet(下拉框样式)
            tem[2].resize(60, 20)
            tem[2].move(横坐标 + 241, 纵坐标 - 20 + 25 * (i + 15) - 20)
            if i > 0:
                for item in range(1, 5):
                    tem[2].addItem("+" + str(item * 2) + '%')
            else:
                for item in range(1, 5):
                    tem[2].addItem("+" + str(item * 4) + '%')
            self.黑鸦词条.append(tem)
            self.黑鸦词条更新(i)
            # tem[1].currentIndexChanged.connect(lambda state: self.希洛克武器词条更新())

        self.武器择优模式 = MyQComboBox(self.main_frame6)
        self.武器择优模式.addItems(['武器默认择优词条', '武器默认择优觉醒'])
        self.武器择优模式.resize(151, 20)
        self.武器择优模式.move(横坐标, 纵坐标 - 20 + 25 * (4 + 15) - 20)
        # self.武器择优模式.setStyleSheet(复选框样式)
        # self.武器择优模式.setChecked(False)

        self.守门人全属强 = QCheckBox(trans('  守门人全属强\n  自动补正'), self.main_frame6)
        self.守门人全属强.resize(120, 30)
        self.守门人全属强.move(横坐标 + 181, 纵坐标 + 291 - 15)
        self.守门人全属强.setStyleSheet(复选框样式)
        self.守门人全属强.setChecked(False)
        self.守门人全属强.setEnabled(False)
        self.守门人全属强.setStyleSheet(复选框样式)
        self.守门人全属强.setToolTip(
            trans("<font size='3' face='宋体'>计算时自动替换细节页的附魔勋章为全属强方案<br>") +
            trans('自带单属强职业不可使用<br>') + trans('守门人属强：全属强+30*3<br>') + trans(
                '武器：全属强+13（若原附魔为龙珠时不替换）<br>首饰：全属强+28*3(25*3站街修正属强自行-9)<br>') +
            trans('辅助装备：全属强+12<br>魔法石：全属强+30<br>勋章：全属强+7<br>宠物附魔：三攻+60</font>')
        )

        self.智慧产物升级 = QCheckBox(trans('智慧产物升级'), self.main_frame6)
        self.智慧产物升级.resize(140, 20)
        self.智慧产物升级.move(横坐标 + 161, 纵坐标 - 19 + 25 * (4 + 15) - 20)
        self.智慧产物升级.setStyleSheet(复选框样式)
        self.智慧产物升级.setChecked(False)

        横坐标 = 横坐标 + 320
        纵坐标 = 0

        标签 = QLabel(trans('希洛克相关'), self.main_frame6)
        标签.setStyleSheet(标签样式 + 'QLabel{font-size:13px;}')
        标签.resize(300, 20)
        标签.move(横坐标 - 310, 纵坐标 + 135 - 10)
        标签.setAlignment(Qt.AlignCenter)

        名称 = trans(['奈克斯', '暗杀者', '卢克西', '守门人', '洛多斯'])
        self.希洛克套装按钮 = []
        self.希洛克单件按钮 = []
        self.希洛克遮罩透明度 = []
        self.希洛克装备图标 = []
        self.希洛克选择状态 = [0] * 15
        count = 0
        for i in 名称:
            self.希洛克套装按钮.append(QPushButton(i, self.main_frame6))
            self.希洛克套装按钮[count].setStyleSheet(按钮样式)
            self.希洛克套装按钮[count].resize(50, 22)
            self.希洛克套装按钮[count].move(横坐标 - 320,
                                     纵坐标 + 160 + 3 + count * 32 - 10)
            self.希洛克套装按钮[count].clicked.connect(
                lambda state, index=(count + 1) * 100: self.希洛克选择(index))
            for j in range(3):
                序号 = count * 3 + j
                图片 = QLabel(self.main_frame6)
                图片.setPixmap(
                    QPixmap('./ResourceFiles/img/希洛克/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标 - 260 + j * 30, 纵坐标 + 160 + count * 32 - 10)
                self.希洛克装备图标.append(图片)
                self.希洛克遮罩透明度.append(QGraphicsOpacityEffect())
                self.希洛克遮罩透明度[序号].setOpacity(0.5)
                self.希洛克单件按钮.append(QPushButton(self.main_frame6))
                self.希洛克单件按钮[序号].setStyleSheet(
                    "background-color: rgb(0, 0, 0)")
                self.希洛克单件按钮[序号].resize(28, 28)
                self.希洛克单件按钮[序号].move(横坐标 - 260 + j * 30,
                                      纵坐标 + 160 + count * 32 - 10)
                self.希洛克单件按钮[序号].setGraphicsEffect(self.希洛克遮罩透明度[序号])
                self.希洛克单件按钮[序号].clicked.connect(
                    lambda state, index=序号: self.希洛克选择(index))
            count += 1

        self.守门人属强 = MyQComboBox(self.main_frame6)
        for i in range(7):
            self.守门人属强.addItem(trans('{守门人属强}：$value', value=15 + i * 5))
        self.守门人属强.resize(120, 20)
        self.守门人属强.setCurrentIndex(3)
        self.守门人属强.move(横坐标 - 139, 纵坐标 + 93 + 3 + count * 32 - 10)
        self.守门人属强.activated.connect(
            lambda state, index=序号: self.守门人属强选项(index))

        self.希洛克武器词条 = []
        count += 1
        self.希洛克武器词条.append(MyQComboBox(self.main_frame6))
        self.希洛克武器词条[0].addItems(['武器词条：无', '自适应最高值', '自选词条数值'])
        self.希洛克武器词条[0].resize(120, 20)
        self.希洛克武器词条[0].move(横坐标 - 139, 纵坐标 - 32 + count * 32 - 10)
        self.希洛克武器词条[0].currentIndexChanged.connect(
            lambda state: self.希洛克武器词条更新())

        for i in range(1, 3):
            count += 1
            self.希洛克武器词条.append(MyQComboBox(self.main_frame6))
            self.希洛克武器词条[-1].setStyleSheet(下拉框样式)
            for k in 词条属性列表:
                self.希洛克武器词条[i].addItem(k.描述)
            self.希洛克武器词条[i].resize(72, 20)
            self.希洛克武器词条[i].move(横坐标 - 139, 纵坐标 - 32 + count * 32 - 10)

        count -= 2
        for i in range(3, 5):
            count += 1
            self.希洛克武器词条.append(MyQComboBox(self.main_frame6))
            self.希洛克武器词条[-1].setStyleSheet(下拉框样式)
            for k in [3, 4, 5]:
                self.希洛克武器词条[i].addItem(str(k * (5 - i)) + '%')
            self.希洛克武器词条[i].resize(43, 20)
            self.希洛克武器词条[i].move(横坐标 - 62, 纵坐标 - 32 + count * 32 - 10)

        for i in range(1, 5):
            self.希洛克武器词条[-1].setStyleSheet(下拉框样式)
            self.希洛克武器词条[i].setEnabled(False)
            # self.希洛克武器词条[i].setStyleSheet(下拉框样式)

        纵向偏移 = 335
        标签 = QLabel(trans('奥兹玛相关'), self.main_frame6)
        标签.setStyleSheet(标签样式 + 'QLabel{font-size:13px;}')
        标签.resize(300, 20)
        标签.move(横坐标 - 310 - 5, 纵坐标 + 135 - 10 + 纵向偏移)
        标签.setAlignment(Qt.AlignCenter)

        名称 = trans(['阿斯特罗斯', '贝利亚斯', '雷德梅恩', '罗什巴赫', '泰玛特'])
        self.奥兹玛套装按钮 = []
        self.奥兹玛单件按钮 = []
        self.奥兹玛遮罩透明度 = []
        self.奥兹玛装备图标 = []
        self.奥兹玛选择状态 = [0] * 25
        count = 0
        for i in 名称:
            self.奥兹玛套装按钮.append(QPushButton(i, self.main_frame6))
            self.奥兹玛套装按钮[count].setStyleSheet(按钮样式)
            self.奥兹玛套装按钮[count].resize(75, 22)
            self.奥兹玛套装按钮[count].move(横坐标 - 320 - 5,
                                     纵坐标 + 160 + 3 + count * 32 - 10 + 纵向偏移)
            self.奥兹玛套装按钮[count].clicked.connect(
                lambda state, index=(count + 1) * 100: self.奥兹玛选择(index))
            for j in range(5):
                序号 = count * 5 + j
                图片 = QLabel(self.main_frame6)
                图片.setPixmap(
                    QPixmap('./ResourceFiles/img/奥兹玛/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标 - 260 + j * 30 + 20 - 5,
                        纵坐标 + 160 + count * 32 - 10 + 纵向偏移)
                self.奥兹玛装备图标.append(图片)
                self.奥兹玛遮罩透明度.append(QGraphicsOpacityEffect())
                self.奥兹玛遮罩透明度[序号].setOpacity(0.5)
                self.奥兹玛单件按钮.append(QPushButton(self.main_frame6))
                self.奥兹玛单件按钮[序号].setStyleSheet(
                    "background-color: rgb(0, 0, 0)")
                self.奥兹玛单件按钮[序号].resize(28, 28)
                self.奥兹玛单件按钮[序号].move(横坐标 - 260 + j * 30 + 20 - 5,
                                      纵坐标 + 160 + count * 32 - 10 + 纵向偏移)
                self.奥兹玛单件按钮[序号].setGraphicsEffect(self.奥兹玛遮罩透明度[序号])
                self.奥兹玛单件按钮[序号].clicked.connect(
                    lambda state, index=序号: self.奥兹玛选择(index))
            count += 1

        self.阿斯特罗斯选项 = []
        for i in range(5):
            self.阿斯特罗斯选项.append(MyQComboBox(self.main_frame6))
            self.阿斯特罗斯选项[i].addItem('70.75.80')
            self.阿斯特罗斯选项[i].addItem('40.45.60')
            self.阿斯特罗斯选项[i].addItem('20.25.35')
            self.阿斯特罗斯选项[i].resize(60 + 15, 20)
            self.阿斯特罗斯选项[i].setCurrentIndex(0)
            self.阿斯特罗斯选项[i].move(横坐标 - 139 + 60 - 15,
                                 纵坐标 + 160 + 3 - 10 + 纵向偏移 + i * 32)
        self.阿斯特罗斯选项显示(0)

        self.计算按钮3 = QPushButton(trans('开始计算'), self.main_frame6)
        self.计算按钮3.clicked.connect(lambda state: self.计算())
        self.计算按钮3.move(990, self.height() - 70)
        self.计算按钮3.resize(110, 30)
        self.计算按钮3.setStyleSheet(按钮样式)

    # endregion

    # region 界面函数
    # 第二页
    def 输出时间变化(self):
        输出时间变化提示 = QMessageBox(QMessageBox.Question, "提示",
                               "切换输出时间请检查技能次数是否为/CD,否则计算结果不发生变化")
        输出时间变化提示.setWindowIcon(self.icon)
        输出时间变化提示.exec_()
        pass

    def 技能列表显示排序(self, skill):
        temp = deepcopy(skill)
        temp.sort(key=operator.attrgetter('所在等级'))
        return temp

    def 次数输入填写(self, x):
        if self.次数输入[x].currentIndex() == 12:
            self.次数输入[x].setEditable(True)
            self.次数输入[x].clearEditText()
            self.次数输入[x].setStyleSheet(下拉框样式)
        elif self.次数输入[x].currentIndex() == 13:
            temp = self.次数输入[x].currentText()
            self.次数输入[x].removeItem(13)
            self.次数输入[x].setCurrentIndex(12)
            self.次数输入[x].setEditable(True)
            self.次数输入[x].clearEditText()
            self.次数输入[x].setStyleSheet(下拉框样式)
            self.次数输入[x].setCurrentText(temp)
        else:
            self.次数输入[x].setEditable(False)

    def 宠物次数填写(self, x):
        if self.宠物次数[x].currentIndex() == 11:
            self.宠物次数[x].setEditable(True)
            self.宠物次数[x].clearEditText()
            self.宠物次数[x].setStyleSheet(下拉框样式)
        elif self.宠物次数[x].currentIndex() == 12:
            temp = self.宠物次数[x].currentText()
            self.宠物次数[x].removeItem(12)
            self.宠物次数[x].setCurrentIndex(11)
            self.宠物次数[x].setEditable(True)
            self.宠物次数[x].clearEditText()
            self.宠物次数[x].setStyleSheet(下拉框样式)
            self.宠物次数[x].setCurrentText(temp)
        else:
            self.宠物次数[x].setEditable(False)

    def 护石描述更新(self, x):
        try:
            self.护石栏[x].setToolTip('<font face="宋体">' + self.初始属性.技能栏[
                self.初始属性.技能序号[self.护石选项[self.护石栏[x].currentIndex()]]].护石描述(
                    self.护石类型选项[x].currentIndex()) + '</font></font>')
        except:
            self.护石栏[x].setToolTip('<font face="宋体">暂缺</font>')

    def 护石类型选项更新(self, x):
        self.护石类型选项[x].clear()
        if self.护石栏[x].currentData() != '无':
            try:
                self.护石类型选项[x].addItems(
                    trans(self.初始属性.技能栏[self.初始属性.技能序号[self.护石选项[
                        self.护石栏[x].currentIndex()]]].护石选项))
                self.护石类型选项[x].setCurrentIndex(
                    len(self.初始属性.技能栏[self.初始属性.技能序号[self.护石选项[
                        self.护石栏[x].currentIndex()]]].护石选项) - 1)
            except:
                self.护石类型选项[x].addItem('魔界')
                self.护石类型选项[x].addItem('圣痕')
                self.护石栏[x].setCurrentIndex(0)
        else:
            self.护石类型选项[x].addItem('魔界')
            self.护石类型选项[x].addItem('圣痕')

    def 符文技能更改(self, i):
        if i == 0:
            for i in range(1, 9):
                self.符文[i].setCurrentIndex(self.符文[0].currentIndex())
        else:
            self.符文[i + 3].setCurrentIndex(self.符文[i].currentIndex())
            self.符文[i + 6].setCurrentIndex(self.符文[i].currentIndex())

    def 符文效果更改(self, i):
        self.符文效果[i + 3].setCurrentIndex(self.符文效果[i].currentIndex())
        self.符文效果[i + 6].setCurrentIndex(self.符文效果[i].currentIndex())

    def 等级调整标注(self, index):
        警告 = "技能等级调整指调整<font color='#FF0000'>学习等级</font>(非实际等级)<br>一般用于修正天空下装技能，一二觉时装切装<br>其余等级加成会自动计算，请勿手动调整"
        if index < 100:
            try:
                x = int(self.等级调整[index].currentText())
            except:
                x = 1
            if x > 0:
                self.等级调整[index].setStyleSheet(下拉框样式_warn)
            if x > 1:
                QMessageBox.information(self, "警告", 警告)
            if x < 0:
                self.等级调整[index].setStyleSheet(下拉框样式_down)
            if x == 0:
                self.等级调整[index].setStyleSheet(下拉框样式)
        elif index == 100:
            try:
                x = int(self.远古记忆.currentText())
            except:
                x = 11
            if x == 11:
                self.远古记忆.setStyleSheet(下拉框样式_warn)
            if x < 10:
                self.远古记忆.setStyleSheet(下拉框样式_down)
            if x == 10:
                self.远古记忆.setStyleSheet(下拉框样式)
        elif index == 200:
            try:
                x = int(self.刀魂之卡赞.currentText())
            except:
                x = 11
            if x == 11:
                self.刀魂之卡赞.setStyleSheet(下拉框样式_warn)
            if x < 10:
                self.刀魂之卡赞.setStyleSheet(下拉框样式_down)
            if x == 10:
                self.刀魂之卡赞.setStyleSheet(下拉框样式)

    def 加载护石(self, 属性):
        for k in range(3):
            if self.护石栏[k].currentData() != '无':
                try:
                    属性.技能栏[self.角色属性A.技能序号[self.护石选项[
                        self.护石栏[k].currentIndex()]]].装备护石()
                except:
                    属性.技能栏[self.角色属性A.技能序号[self.护石选项[
                        self.护石栏[k].currentIndex()]]].装备护石(
                            self.护石类型选项[k].currentIndex())

        属性.护石第一栏 = self.护石选项[self.护石栏[0].currentIndex()]
        属性.护石第二栏 = self.护石选项[self.护石栏[1].currentIndex()]
        属性.护石第三栏 = self.护石选项[self.护石栏[2].currentIndex()]

        for i in range(9):
            if self.符文[i].currentData() != '无' and self.符文效果[i].currentData(
            ) != '无':
                for j in self.符文效果[i].currentData().split(','):
                    if trans('攻击') in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文选项[
                            self.符文[i].currentIndex()]]].倍率 *= 1 + int(
                                j.replace(trans('攻击'), '').replace('%',
                                                                   '')) / 100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文选项[
                            self.符文[i].currentIndex()]]].CD *= 1 + int(
                                j.replace('CD', '').replace('%', '')) / 100

    # 第三页
    def 细节增伤选项颜色更新(self, index):
        if index.currentIndex() <= 0:
            index.setStyleSheet(下拉框样式_warn)
        else:
            index.setStyleSheet(下拉框样式_detail)
        pass

    # 第五页
    def 阿斯特罗斯选项显示(self, n):
        for i in range(5):
            if i < n:
                self.阿斯特罗斯选项[i].setEnabled(True)
            else:
                self.阿斯特罗斯选项[i].setEnabled(False)

    def 守门人属强选项(self, x):
        if self.守门人属强.currentIndex() != 3:
            self.守门人全属强.setEnabled(False)
            self.守门人全属强.setChecked(False)
            self.守门人全属强.setStyleSheet(复选框样式)
        else:
            number = sum(self.希洛克选择状态[9:11])
            if self.角色属性A.职业 not in ('冰结师', '鬼泣', '死灵术士', '气功师', '忍者', '暗枪士'):
                if number == 3:
                    self.守门人全属强.setEnabled(True)
                    self.守门人全属强.setChecked(True)
                    self.守门人全属强.setStyleSheet(复选框样式)

    def 希洛克武器词条更新(self):
        if self.希洛克武器词条[0].currentIndex() != 2:
            for i in range(1, 5):
                self.希洛克武器词条[i].setEnabled(False)
        else:
            for i in range(1, 5):
                self.希洛克武器词条[i].setEnabled(True)

    def 黑鸦词条更新(self, index):
        if self.黑鸦词条[index][0].currentIndex() < 2:
            for i in range(1, 3):
                self.黑鸦词条[index][i].setEnabled(False)
        else:
            for i in range(1, 3):
                self.黑鸦词条[index][i].setEnabled(True)

    def 时装选项更新(self, index):
        if index == 8:
            count = 0
            for i in self.时装选项:
                if count != 8:
                    i.setCurrentIndex(self.时装选项[8].currentIndex())
                count += 1
            return
        else:
            力量, 智力, 属强 = 0, 0, 0
            套装字典 = {'高级': 0, '节日': 0, '稀有': 0, '神器': 0}
            for i in range(8):
                套装字典[self.时装选项[i].currentData()] = 套装字典.get(
                    self.时装选项[i].currentData(), 0) + 1
            # 套装属性
            神器 = 套装字典['神器']
            稀有 = 套装字典['稀有'] + 神器
            if 套装字典['高级'] >= 3:
                力量 += 10
                智力 += 10
            if 稀有 >= 3 and 神器 < 3:
                力量 += 40
                智力 += 40
            if 套装字典['神器'] >= 3:
                力量 += 50
                智力 += 50
            if 套装字典['高级'] >= 8:
                力量 += 10
                智力 += 10
            if 套装字典['节日'] >= 8:
                力量 += 25
                智力 += 25
            if 稀有 >= 8 and 神器 < 8:
                力量 += 40
                智力 += 40
                属强 += 6
            if 套装字典['神器'] >= 8:
                力量 += 50
                智力 += 50
                属强 += 10
            数据 = [45, 45, 55, 65]
            智力 += 数据[self.时装选项[0].currentIndex()]  # 头部
            智力 += 数据[self.时装选项[1].currentIndex()]  # 帽子
            力量 += 数据[self.时装选项[7].currentIndex()]  # 鞋子
            数据 = [45, 45, 55, 65]
            力量 += 数据[self.时装选项[5].currentIndex()]  # 腰带
            数据 = [0, 6, 0, 0]
            属强 += 数据[self.时装选项[4].currentIndex()]  # 上衣

            数据 = [0, 20, 0, 0]
            智力 += 数据[self.时装选项[6].currentIndex()]  # 下装
            力量 += 数据[self.时装选项[6].currentIndex()]  # 下装

            self.属性设置输入[6][16].setText(str(max(力量, 智力)))
            self.属性设置输入[8][16].setText(str(属强 if 属强 != 0 else ''))

    # 通用
    def 下拉框禁用(self, a, b, c=下拉框样式):
        if a.isChecked():
            b.setStyleSheet(c)
            b.setEnabled(False)
        else:
            b.setStyleSheet(c)
            b.setEnabled(True)

    # endregion

    # region 计算相关

    def 奥兹玛选择(self, index, x=0):
        super().奥兹玛选择(index, x)
        self.阿斯特罗斯选项显示(sum(self.奥兹玛选择状态[0:5]))

    def 希洛克属性计算(self, 属性, x=0):
        # 0表示计算属性 1表示计算描述
        return 希洛克.希洛克属性_输出(属性, self.希洛克选择状态, self.守门人属强.currentIndex(), x)

    def 奥兹玛属性计算(self, 属性, x=0):
        # 0表示计算属性 1表示计算描述
        阿斯特罗斯选项 = []
        for i in range(sum(self.奥兹玛选择状态[:5])):
            阿斯特罗斯选项.append(self.阿斯特罗斯选项[i].currentIndex())
        return 奥兹玛.奥兹玛属性_输出(属性, self.奥兹玛选择状态, 阿斯特罗斯选项, x)

    def 自选计算(self, x=0):
        if x == 0:
            self.保存配置(self.存档位置)
            self.关闭排行窗口()
            self.排行数据.clear()

        self.角色属性A = deepcopy(self.初始属性)
        if x == 0:
            self.输入属性(self.角色属性A)
        else:
            self.输入属性(self.角色属性A, 1)
        if self.是否计算 != 1:
            self.click_window(1)
            return
        装备 = []
        for index in range(len(self.自选装备)):
            装备.append(self.自选装备[index].currentData())

        temp = deepcopy(self.初始属性)
        temp.穿戴装备计算套装(装备)
        套装 = temp.套装栏

        if x != 0:
            伤害列表 = []
            for i in range(len(辟邪玉列表)):
                temp = deepcopy(self.初始属性)
                self.输入属性(temp, 100 + i)
                temp.穿戴装备(装备, 套装)
                伤害列表.append(temp.伤害计算(0))

            提升率 = []
            for i in range(1, len(伤害列表)):
                if 伤害列表[0] != 0:
                    提升率.append(伤害列表[i] / 伤害列表[0] - 1)
                else:
                    提升率.append(0)

            提升率排序 = copy(提升率)
            提升率排序.sort(reverse=True)

            for i in range(len(提升率)):
                temp = str('%.2f' % (提升率[i] * 100)) + '%'
                self.辟邪玉提升率2[i].setText(temp)
                x = 提升率排序.index(提升率[i]) / len(提升率) * 10 - 2
                y = 1 / (1 + math.exp(-x))
                if SkinVersion == 'None':
                    颜色 = (0, 0, 0)
                else:
                    颜色 = (int(255 - 80 * y), int(245 - 100 * y),
                          int(0 + 150 * y))
                self.辟邪玉提升率1[i].setStyleSheet(
                    'QLabel{font-size:12px;color:rgb' + str(颜色) + '}')
                self.辟邪玉提升率2[i].setStyleSheet(
                    'QLabel{font-size:12px;color:rgb' + str(颜色) + '}')

            self.角色属性A = deepcopy(self.初始属性)
            self.输入属性(self.角色属性A)
            C = self.站街计算(装备, 套装)
            B = deepcopy(self.角色属性A)
            B.穿戴装备(装备, 套装)
            B.其它属性计算()
            总伤害数值 = B.伤害计算(0)

            if len(self.基准值) != 0:
                self.总伤害.setText(self.百分比输出(总伤害数值, self.基准值[0]))
            else:
                self.总伤害.setText(self.格式化输出(str(int(总伤害数值))))

            tempstr = self.装备描述计算(B)
            图片列表 = self.获取装备图片(装备)
            for i in range(12):
                self.图片显示[i].setToolTip(tempstr[i])
                self.图片显示[i].setMovie(图片列表[i])

            self.面板显示设置(self.面板显示, B, C)
            self.打造显示设置(self.打造显示, B, 1)

            词条数值 = self.词条显示计算(B)
            词条解释 = self.词条显示计算(B, 1)
            for i in range(0, len(词条数值)):
                if i == 5 and B.技能攻击力累加 > 2:
                    self.词条显示[i].setStyleSheet(
                        "QLabel{font-size:12px;color:red}")
                self.词条显示[i].setText(词条数值[i])
                self.词条显示[i].setToolTip('<font color="#B99460">' + 词条解释[i] +
                                        '</font>')

            for i in self.套装名称显示:
                i.setText('')

            self.套装显示设置(self.套装名称显示, B)

            # 更新人物名望(角色属性=B, 人物设置=self)

        if x == 0:
            self.排行数据.append(装备 + [0] + 套装 + ['无'])
            self.输出界面(0)

    def 站街计算(self, 装备名称, 套装名称):
        C = deepcopy(self.角色属性A)
        C.穿戴装备(装备名称, 套装名称)
        if 调试开关 == 0:
            for i in C.装备栏:
                equ.get_equ_by_name(i).城镇属性(C)
            for i in C.套装栏:
                equ.get_suit_by_name(i).城镇属性(C)
            C.装备基础()
        C.被动倍率计算()

        return C

    # endregion

    # region 读档存档
    def 载入旧版json(self, path='set', page=[0, 1, 2, 3, 4, 5]):
        filepath = './ResourceFiles/{}/{}'.format(self.角色属性A.实际名称, path)

        if 0 in page:
            # 第一页(装备/选择/打造)
            try:
                filename = 'page_1.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                try:
                    store.set("/{type}/data/title", set_data['称号'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/pet", set_data['称号'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/compute_mode", set_data['计算模式'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set('/{type}/data/ditto_checked', set_data["百变怪"])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/pet_equip_adaptive",
                              set_data['宠物装备择优'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/aura_adaptive", set_data['光环词条择优'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/myth_top_checked",
                              set_data['神话排名勾选'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/damage_unit", set_data['亿为单位显示'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/thread_count", set_data['线程数量'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/attack_elemental",
                              set_data['攻击属性'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/remodel_limit", set_data['改造数量'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/equip_checked", set_data['装备勾选'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/equip_forges", set_data['装备打造'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/equip_conditions",
                              set_data['装备条件'])
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 1 in page:
            # 第二页(技能/符文/药剂)
            try:
                filename = 'page_2.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                try:
                    store.set("/{type}/data/buff_input", set_data['BUFF输入'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/time_input", set_data['时间输入'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/awakening_binding",
                              set_data['觉醒选择'])
                except Exception as error:
                    logger.error(error)
                try:
                    if '远古记忆' in set_data:
                        store.set("/{type}/data/ancient_memory",
                                  set_data['远古记忆'])
                except Exception as error:
                    logger.error(error)
                try:
                    if '刀魂之卡赞' in set_data:
                        store.set("/{type}/data/kazan", set_data['刀魂之卡赞'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/talismans", set_data['护石栏'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/talisman_types", set_data['护石类型'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/runes_skills", set_data['符文技能'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/runes_effects", set_data['符文效果'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/consumables", set_data['药剂勾选'])
                except Exception as error:
                    logger.error(error)
                try:
                    skills = {}
                    技能选项 = set_data['技能选项']
                    for key in 技能选项.keys():
                        技能 = 技能选项[key]
                        skill = {'level': 技能['等级'], 'count': 技能['次数']}
                        if 'TP' in 技能:
                            skill['tp'] = 技能['TP']
                        if '宠物' in 技能:
                            skill['pet'] = 技能['宠物']
                        if '切装' in 技能:
                            skill['switch'] = 技能['切装']
                        skills[key] = skill
                    store.set("/{type}/data/skill", skills)
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 2 in page:
            # 第三页(基础/细节/修正)
            try:
                filename = 'page_3.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()

                try:
                    store.set("/{type}/data/avatar", set_data['时装选项'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/detail_values", set_data['细节数值'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/detail_options", set_data['细节选项'])
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 3 in page:
            # 第四页(神话属性修正)
            try:
                filename = 'page_4.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                try:
                    store.set("/{type}/data/myth_properties",
                              set_data['神话属性修正'])
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 4 in page:
            # 第五页(辟邪玉/希洛克/黑鸦/奥兹玛)
            try:
                filename = 'page_5.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()

                try:
                    store.set("/{type}/data/remodel_upgrade",
                              set_data['智慧产物升级'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/weapon_adaptive_mode",
                              set_data['武器择优模式'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/nameless_elemental_value",
                              set_data['守门人属强'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/jude_effects", set_data['辟邪玉效果'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/jude_values", set_data['辟邪玉数值'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/astaroth_options",
                              set_data['阿斯特罗斯选项'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set('/{type}/data/black_purgatory', set_data['黑鸦选择'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set('/{type}/data/siroco', set_data['希洛克选择'])
                except Exception as error:
                    logger.error(error)
                try:
                    store.set('/{type}/data/ozma', set_data['奥兹玛选择'])
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 5 in page:
            # 第六页(自选装备计算)
            try:
                filename = 'page_6.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()

                try:
                    store.set("/{type}/data/self_select/equips",
                              [set_data['自选装备']])
                    store.set("/{type}/data/self_select/column_index", 0)
                except Exception as error:
                    logger.error(error)
                try:
                    store.set("/{type}/data/self_select/locked",
                              set_data['装备锁定'])
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        # 职业存档
        try:
            filename = 'char.json'
            set_data = {}
            with open(os.path.join(filepath, filename),
                      encoding='utf-8') as fp:
                set_data = json.load(fp)
            fp.close()
            store.set("/{type}/data/character_sets", set_data)
        except Exception as error:
            logger.error(error)
        pass

    def 载入json(self, path='set', page=[0, 1, 2, 3, 4, 5]):
        filepath = './ResourceFiles/{}/{}'.format(self.角色属性A.实际名称, path)
        filename = os.path.join(filepath, "store.json")

        if os.path.exists(filename):
            try:
                set_data = {}
                with open(filename, encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                store.imports(set_data)
            except Exception as error:
                logger.error(error)
        else:
            self.载入旧版json(path, page)

        if 0 in page:
            # 第一页(装备/选择/打造)
            try:
                try:
                    self.称号.setCurrentIndex(store.get("/{type}/data/title", 0))
                except Exception as error:
                    logger.error(error)
                try:
                    self.宠物.setCurrentIndex(store.get("/{type}/data/pet", 0))
                except Exception as error:
                    logger.error(error)
                try:
                    self.计算模式选择.setCurrentIndex(
                        store.get("/{type}/data/compute_mode", 0))
                except Exception as error:
                    logger.error(error)
                try:
                    self.百变怪选项.setChecked(
                        store.get("/{type}/data/ditto_checked", False))
                except Exception as error:
                    logger.error(error)
                try:
                    self.红色宠物装备.setChecked(
                        store.get("/{type}/data/pet_equip_adaptive", True))
                except Exception as error:
                    logger.error(error)
                try:
                    self.光环自适应.setChecked(
                        store.get("/{type}/data/aura_adaptive", True))
                except Exception as error:
                    logger.error(error)
                try:
                    self.神话排名选项.setChecked(
                        store.get("/{type}/data/myth_top_checked", True))
                except Exception as error:
                    logger.error(error)
                try:
                    self.显示选项.setChecked(
                        store.get("/{type}/data/damage_unit", True))
                except Exception as error:
                    logger.error(error)
                try:
                    self.线程数选择.setCurrentIndex(
                        store.get("/{type}/data/thread_count"))
                except Exception as error:
                    logger.error(error)
                try:
                    self.攻击属性选项.setCurrentIndex(
                        store.get("/{type}/data/attack_elemental"))
                except Exception as error:
                    logger.error(error)
                try:
                    self.智慧产物限制.setCurrentIndex(
                        store.get("/{type}/data/remodel_limit"))
                except Exception as error:
                    logger.error(error)
                try:
                    self.批量选择(0)
                    num = 0
                    data = store.get("/{type}/data/equip_checked")
                    for i in data:
                        if i == 1:
                            self.装备图标点击事件(num, 1)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = store.get("/{type}/data/equip_forges")
                    for i in data:
                        self.装备打造选项[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = store.get("/{type}/data/equip_conditions")
                    for i in data:
                        self.装备条件选择[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 1 in page:
            # 第二页(技能/符文/药剂)
            try:
                try:
                    self.BUFF输入.setText(store.get("/{type}/data/buff_input"))
                except Exception as error:
                    logger.error(error)
                try:
                    时间 = store.get("/{type}/data/time_input", '25')
                    if int(时间) < 10:
                        self.时间输入.setCurrentIndex(int(时间))
                    else:
                        self.时间输入.setCurrentText(str(时间))
                except Exception as error:
                    logger.error(error)
                try:
                    self.强化觉醒选择(store.get("/{type}/data/awakening_binding"))
                except Exception as error:
                    logger.error(error)
                try:
                    if self.初始属性.远古记忆 != -1:
                        self.远古记忆.setCurrentIndex(
                            store.get("/{type}/data/ancient_memory"))
                except Exception as error:
                    logger.error(error)
                try:
                    if self.初始属性.刀魂之卡赞 != -1:
                        self.刀魂之卡赞.setCurrentIndex(
                            store.get("/{type}/data/kazan"))
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = store.get("/{type}/data/talismans")
                    for i in data:
                        self.护石栏[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = store.get("/{type}/data/talisman_types")
                    for i in data:
                        self.护石类型选项[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = store.get("/{type}/data/runes_skills")
                    for i in data:
                        self.符文[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = store.get("/{type}/data/runes_effects")
                    for i in data:
                        self.符文效果[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = store.get("/{type}/data/consumables")
                    for i in data:
                        self.复选框列表[num].setChecked(i)
                        num += 1
                except Exception as error:
                    logger.error(error)

                try:
                    skills = store.get("/{type}/data/skill")
                    for i in skills:
                        try:
                            序号 = self.角色属性A.技能序号[i]
                            self.设置技能选项(序号, skills[i])
                        except Exception as error:
                            logger.error(error)
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 2 in page:
            # 第三页(基础/细节/修正)
            try:
                try:
                    num = 0
                    data = store.get("/{type}/data/avatar")
                    for i in data:
                        self.时装选项[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/detail_values")
                    x = 0
                    for i in data:
                        y = 0
                        for j in i:
                            self.属性设置输入[x][y].setText(j)
                            y += 1
                        x += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/detail_options")
                    x = 0
                    for i in data:
                        y = 0
                        for j in i:
                            self.细节选项输入[x][y].setCurrentIndex(j)
                            y += 1
                        x += 1
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 3 in page:
            # 第四页(神话属性修正)
            try:
                data = store.get("/{type}/data/myth_properties")
                num = 0
                for i in data:
                    self.神话属性选项[num].setCurrentIndex(i)
                    num += 1
            except Exception as error:
                logger.error(error)

        if 4 in page:
            # 第五页(辟邪玉/希洛克/黑鸦/奥兹玛)
            try:
                try:
                    self.智慧产物升级.setChecked(
                        store.get("/{type}/data/remodel_upgrade"))
                except Exception as error:
                    logger.error(error)
                try:
                    self.武器择优模式.setCurrentIndex(
                        store.get("/{type}/data/weapon_adaptive_mode"))
                except Exception as error:
                    logger.error(error)
                try:
                    self.守门人属强.setCurrentIndex(
                        store.get("/{type}/data/nameless_elemental_value"))
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/weapon_fusion", [0] * 5)
                    num = 0
                    for i in data:
                        self.希洛克武器词条[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/jude_effects")
                    num = 0
                    for i in data:
                        self.辟邪玉选择[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/jude_values")
                    num = 0
                    for i in data:
                        self.辟邪玉数值[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/astaroth_options", [])
                    num = 0
                    for i in data:
                        self.阿斯特罗斯选项[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/black_purgatory")
                    x = 0
                    for i in data:
                        y = 0
                        for j in i:
                            self.黑鸦词条[x][y].setCurrentIndex(j)
                            y += 1
                        x += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/siroco", [])
                    self.希洛克选择(0, 1)
                    num = 0
                    for i in data:
                        if i == 1:
                            self.希洛克选择(num)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/ozma", [])
                    self.奥兹玛选择(0, 1)
                    num = 0
                    for i in data:
                        if i == 1:
                            self.奥兹玛选择(num)
                        num += 1
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 5 in page:
            # 第六页(自选装备计算)
            try:
                try:
                    data = store.get("/{type}/data/self_select/equips", [[]])
                    column_index = store.get(
                        "/{type}/data/self_select/column_index", 0)
                    data = data[column_index]
                    num = 0
                    for i in data:
                        self.自选装备[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/self_select/locked")
                    num = 0
                    for i in data:
                        self.装备锁定[num].setChecked(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        # 职业存档
        try:
            data = store.get("/{type}/data/character_set", [])
            for i in self.职业存档:
                try:
                    key = i[0]
                    if key not in data:
                        continue
                    # 复选框
                    if i[2] == 0:
                        i[1].setChecked(data[key])
                    # 下拉框
                    elif i[2] == 1:
                        i[1].setCurrentIndex(data[key])
                    # 文本框
                    elif i[2] == 2:
                        i[1].setText(data[key])
                except Exception as error:
                    logger.error(error)
        except Exception as error:
            logger.error(error)

    def 载入配置(self, path='set'):
        filepath = './ResourceFiles/{}/{}/'.format(self.角色属性A.实际名称, path)
        if os.path.exists(os.path.join(
                filepath, "page_1.json")) or os.path.exists(
                    os.path.join(filepath, "store.json")):
            self.载入json(path)
            return
        else:
            # 如果不存在任何存档则载入重置存档
            self.载入json(path='reset')

    def isIntSeriously(self, number):
        result = False
        try:
            n = float(number)
            # 判断是否是整数并且是否小于10
            if n.is_integer() and str(number).count('.') == 0 and n <= 10:
                result = True
        except:
            pass
        return result

    def 设置技能选项(self, 序号, info):
        try:
            self.等级调整[序号].setCurrentIndex(info['level'])
        except:
            pass
        try:
            self.TP输入[序号].setCurrentIndex(info['tp'])
        except:
            pass

        try:
            if info['count'] == '/CD':
                self.次数输入[序号].setCurrentIndex(0)
            elif self.isIntSeriously(info['count']):
                self.次数输入[序号].setCurrentIndex(int(info['count']) + 1)
            else:
                self.次数输入[序号].setCurrentIndex(12)
                self.次数输入[序号].setEditable(True)
                self.次数输入[序号].clearEditText()
                self.次数输入[序号].setCurrentText(info['count'])
                self.次数输入[序号].setStyleSheet(下拉框样式)
        except:
            pass

        try:
            if self.isIntSeriously(info['pet']):
                self.宠物次数[序号].setCurrentIndex(int(info['pet']))
            else:
                self.宠物次数[序号].setCurrentIndex(11)
                self.宠物次数[序号].setEditable(True)
                self.宠物次数[序号].clearEditText()
                self.宠物次数[序号].setCurrentText(info['pet'])
                self.宠物次数[序号].setStyleSheet(下拉框样式)
        except:
            pass

        if 切装模式 == 1:
            try:
                self.技能切装[序号].setChecked(info['switch'])
            except:
                pass

    def 获取技能选项(self, 序号):
        info = {}
        try:
            info['level'] = self.等级调整[序号].currentIndex()
        except:
            info['level'] = 0
        try:
            info['tp'] = self.TP输入[序号].currentIndex()
        except:
            info['tp'] = 0

        try:
            info['count'] = self.次数输入[序号].currentText()
        except:
            info['count'] = '0'

        try:
            info['pet'] = self.宠物次数[序号].currentText()
        except:
            info['pet'] = '0'

        if 切装模式 == 1:
            try:
                info['switch'] = self.技能切装[序号].isChecked()
            except:
                info['switch'] = False
        return info

    def exports_store(self, page=[0, 1, 2, 3, 4, 5]):
        if 0 in page:
            # 第一页(装备/选择/打造)
            try:
                store.set("/{type}/data/title", self.称号.currentIndex())
                store.set("/{type}/data/pet", self.宠物.currentIndex())
                store.set("/{type}/memory/title", self.称号.currentData())
                store.set('/{type}/memory/pet', self.宠物.currentData())
                store.set("/{type}/data/compute_mode",
                          self.计算模式选择.currentIndex())
                store.set("/{type}/data/ditto_checked", self.百变怪选项.isChecked())
                store.set("/{type}/data/pet_equip_adaptive",
                          self.红色宠物装备.isChecked())
                store.set("/{type}/data/aura_adaptive", self.光环自适应.isChecked())
                store.set("/{type}/data/myth_top_checked",
                          self.神话排名选项.isChecked())
                store.set("/{type}/data/damage_unit", self.显示选项.isChecked())
                store.set("/{type}/data/thread_count",
                          self.线程数选择.currentIndex())
                store.set("/{type}/data/attack_elemental",
                          self.攻击属性选项.currentIndex())
                store.set("/{type}/data/remodel_limit",
                          self.智慧产物限制.currentIndex())
                store.set("/{type}/data/equip_checked", self.装备选择状态)
                store.set("/{type}/data/equip_forges",
                          [i.currentIndex() for i in self.装备打造选项])
                store.set("/{type}/data/equip_conditions",
                          [i.currentIndex() for i in self.装备条件选择])
            except Exception as error:
                logger.error(error)

        if 1 in page:
            # 第二页(技能/符文/药剂)
            try:
                store.set("/{type}/data/buff_input", self.BUFF输入.text())
                store.set("/{type}/data/time_input", self.时间输入.currentText())

                store.set("/{type}/data/awakening_binding", self.觉醒选择状态)

                if self.初始属性.远古记忆 != -1:
                    store.set("/{type}/data/ancient_memory",
                              self.远古记忆.currentIndex())
                if self.初始属性.刀魂之卡赞 != -1:
                    store.set("/{type}/data/kazan", self.刀魂之卡赞.currentIndex())
                store.set("/{type}/data/talismans",
                          [i.currentIndex() for i in self.护石栏])
                store.set("/{type}/data/talisman_types",
                          [i.currentIndex() for i in self.护石类型选项])
                store.set("/{type}/memory/talisman_types",
                          [i.currentData() for i in self.护石类型选项])
                store.set("/{type}/data/runes_skills",
                          [i.currentIndex() for i in self.符文])
                store.set("/{type}/data/runes_effects",
                          [i.currentIndex() for i in self.符文效果])
                store.set("/{type}/data/consumables",
                          [i.isChecked() for i in self.复选框列表])

                skills = {}
                for i in self.角色属性A.技能栏:
                    序号 = self.角色属性A.技能序号[i.名称]
                    skill = self.获取技能选项(序号)
                    skills[i.名称] = skill
                store.set("/{type}/data/skill", skills)
            except Exception as error:
                logger.error(error)

        if 2 in page:
            # 第三页(基础/细节/修正)
            try:
                store.set("/{type}/data/avatar",
                          [i.currentIndex() for i in self.时装选项])
                store.set("/{type}/data/detail_values",
                          [[j.text() for j in i] for i in self.属性设置输入])
                store.set("/{type}/data/detail_options",
                          [[j.currentIndex() for j in i] for i in self.细节选项输入])
            except Exception as error:
                logger.error(error)

        if 3 in page:
            # 第四页(神话属性修正)
            try:
                store.set("/{type}/data/myth_properties",
                          [i.currentIndex() for i in self.神话属性选项])
            except Exception as error:
                logger.error(error)
            try:
                store.set("/{type}/data/remodel_properties",
                          [i.currentIndex() for i in self.改造产物选项])
            except Exception as error:
                logger.error(error)
        if 4 in page:
            # 第五页(辟邪玉/希洛克/黑鸦)
            try:
                store.set("/{type}/data/remodel_upgrade",
                          self.智慧产物升级.isChecked())
                store.set("/{type}/data/weapon_adaptive_mode",
                          self.武器择优模式.currentIndex())
                store.set("/{type}/data/nameless_elemental_value",
                          self.守门人属强.currentIndex())
                store.set("/{type}/data/weapon_fusion",
                          [i.currentIndex() for i in self.希洛克武器词条])
                store.set("/{type}/data/jude_effects",
                          [i.currentIndex() for i in self.辟邪玉选择])
                store.set("/{type}/data/jude_values",
                          [i.currentIndex() for i in self.辟邪玉数值])
                store.set("/{type}/data/astaroth_options",
                          [i.currentIndex() for i in self.阿斯特罗斯选项])
                store.set('/{type}/data/black_purgatory',
                          [[j.currentIndex() for j in i] for i in self.黑鸦词条])
                store.set('/{type}/data/siroco', self.希洛克选择状态)
                store.set('/{type}/data/ozma', self.奥兹玛选择状态)
            except Exception as error:
                logger.error(error)

        if 5 in page:
            # 第六页(自选装备计算)
            try:
                data = store.get("/{type}/data/self_select/equips", [])
                column_index = 0
                length = len(self.自选装备)
                while column_index >= len(data):
                    data.append([0] * length)

                data[column_index] = [i.currentIndex() for i in self.自选装备]
                store.set("/{type}/data/self_select/equips", data)

                store.set("/{type}/memory/equips",
                          [i.currentData() for i in self.自选装备])

                store.set("/{type}/data/self_select/equips", data)

                store.set('/{type}/data/self_select/column_index',
                          column_index)
                store.set("/{type}/data/self_select/locked",
                          [i.isChecked() for i in self.装备锁定])
            except Exception as error:
                logger.error(error)
        # 职业存档
        try:
            set_data = {}
            for i in self.职业存档:
                # 复选框
                if i[2] == 0:
                    set_data[i[0]] = i[1].isChecked()
                # 下拉框
                elif i[2] == 1:
                    set_data[i[0]] = i[1].currentIndex()
                # 文本框
                elif i[2] == 2:
                    set_data[i[0]] = i[1].text()
            store.set("/{type}/data/character_set", set_data)
        except Exception as error:
            logger.error(error)

    def 保存json(self, path='set', page=[0, 1, 2, 3, 4, 5], store=None):
        if store is None:
            from PublicReference.utils.storex import store
        self.exports_store(page)
        try:
            filepath = './ResourceFiles/{}/{}/store.json'.format(
                self.角色属性A.实际名称, path)
            set_data = store.exports(
                lambda i: str.startswith(i, "/carry/data"))
            with open(filepath, "w", encoding='utf-8') as fp:
                json.dump(set_data, fp, ensure_ascii=False, indent=4)
            fp.close()
        except Exception as error:
            logger.error(error)

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        if self.技能存档位置 != '全局存档':
            self.保存json(path=self.技能存档位置, store=Store())
        self.保存json(path)

    # endregion

    # region 一键修正
    def 一键修正(self, x=0):
        increase_counter(ga_category="carry详细功能使用", name="一键修正")
        if x == 0:
            if self.组合计算(2) == 0:
                QMessageBox.information(self, "错误", "请勾选齐全身上穿戴的装备")
                return
            if self.组合计算(2) > 1:
                QMessageBox.information(self, "错误", "请勿勾选身上未穿戴的装备")
                return
        self.修正套装计算(x)
        self.角色属性B = deepcopy(self.初始属性)
        self.角色属性B.技能栏 = deepcopy(self.初始属性.技能栏)
        self.输入属性(self.角色属性B)
        self.角色属性B.穿戴装备计算套装(self.有效穿戴组合[0])
        for i in self.角色属性B.装备栏:
            equ.get_equ_by_name(i).城镇属性(self.角色属性B)
        for i in self.角色属性B.套装栏:
            equ.get_suit_by_name(i).城镇属性(self.角色属性B)
        self.角色属性B.装备基础()
        self.角色属性B.被动倍率计算()
        self.面板修正(self.角色属性B.类型, x * 3)

    def 面板修正(self, 类型, x):
        数据 = []
        原始数据 = []
        名称 = ['力智', '三攻', '属强']
        for i in range(3):
            try:
                if self.一键站街设置输入[i + x].text() != '':
                    数据.append(int(self.一键站街设置输入[i + x].text()))
                else:
                    数据.append(0)
            except:
                QMessageBox.information(self, "错误", 名称[i] + "输入格式错误，已重置为空")
                self.一键站街设置输入[i + x].setText('')
                数据.append(0)

        if sum(数据) == 0:
            return

        if 数据[0] != 0 and 数据[1] == 0:
            QMessageBox.information(self, "错误", "请输入三攻")
            return

        for i in range(5):
            if self.属性设置输入[i][15].text() != '':
                原始数据.append(int(self.属性设置输入[i][15].text()))
            else:
                原始数据.append(0)
        if 数据[1] != 0:
            if 类型 == '物理百分比':
                self.物理百分比修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街力量()),
                             数据[1], 原始数据[0], 原始数据[2])
            elif 类型 == '魔法百分比':
                self.魔法百分比修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街智力()),
                             数据[1], 原始数据[1], 原始数据[3])
            elif 类型 == '物理固伤':
                self.物理固伤修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街力量()),
                            数据[1], 原始数据[0], 原始数据[4])
            elif 类型 == '魔法固伤':
                self.魔法固伤修正(数据[0] if 数据[0] != 0 else int(self.角色属性B.站街智力()),
                            数据[1], 原始数据[1], 原始数据[4])

        if 数据[2] != 0:
            self.属强修正(数据[2])
        self.click_window(2)
        QMessageBox.information(
            self, "自动修正计算完毕", "仅对站街修正进行了修改，使面板与输入一致<br>请自行核对其它页面 非力智三攻属强 条目")

    def 力量一键修正(self, 输入力智, 修正力量2):
        修正前力量 = self.角色属性B.力量
        if self.初始属性.实际名称 == '黑暗武士':
            self.角色属性B.力量 = 输入力智 / self.角色属性B.技能栏[
                self.角色属性B.技能序号['次元融合']].力智倍率()
            修正力量 = int(输入力智 / self.角色属性B.技能栏[self.角色属性B.技能序号['次元融合']].力智倍率() +
                       1) - int(修正前力量)
        else:
            self.角色属性B.力量 = 输入力智
            修正力量 = 输入力智 - int(修正前力量)
        self.属性设置输入[0][15].setText(str(int(修正力量 + 修正力量2)))

    def 智力一键修正(self, 输入力智, 修正智力2):
        修正前智力 = self.角色属性B.智力
        if self.初始属性.实际名称 == '黑暗武士':
            self.角色属性B.智力 = 输入力智 / self.角色属性B.技能栏[
                self.角色属性B.技能序号['次元融合']].力智倍率()
            修正智力 = int(输入力智 / self.角色属性B.技能栏[self.角色属性B.技能序号['次元融合']].力智倍率() +
                       1) - int(修正前智力)
        else:
            self.角色属性B.智力 = 输入力智
            修正智力 = 输入力智 - int(修正前智力)
        self.属性设置输入[1][15].setText(str(int(修正智力 + 修正智力2)))

    def 物攻一键修正(self, 输入力智, 输入三攻, 修正物理攻击力2):
        修正前物理攻击力 = self.角色属性B.物理攻击力
        站街物理攻击倍率 = self.角色属性B.站街物理攻击力倍率()
        j = round(输入三攻 / 站街物理攻击倍率, 0)
        站街实际三攻 = int(j)
        for k in range(int(j) - 2, int(j) + 3):
            self.角色属性B.物理攻击力 = float(k)
            验证物理攻击力1 = int(self.角色属性B.站街物理攻击力())
            self.角色属性B.物理攻击力 = float(k + 1)
            验证物理攻击力2 = int(self.角色属性B.站街物理攻击力())
            if 验证物理攻击力1 <= 输入三攻 and 验证物理攻击力2 > 输入三攻:
                站街实际三攻 = float(k)
        修正物理攻击力 = 站街实际三攻 - 修正前物理攻击力
        self.属性设置输入[2][15].setText(str(int(修正物理攻击力 + 修正物理攻击力2)))

    def 魔攻一键修正(self, 输入力智, 输入三攻, 修正魔法攻击力2):
        修正前魔法攻击力 = self.角色属性B.魔法攻击力
        站街魔法攻击倍率 = self.角色属性B.站街魔法攻击力倍率()
        j = round(输入三攻 / 站街魔法攻击倍率, 0)
        站街实际三攻 = int(j)
        for k in range(int(j) - 2, int(j) + 3):
            self.角色属性B.魔法攻击力 = float(k)
            验证魔法攻击力1 = int(self.角色属性B.站街魔法攻击力())
            self.角色属性B.魔法攻击力 = float(k + 1)
            验证魔法攻击力2 = int(self.角色属性B.站街魔法攻击力())
            if 验证魔法攻击力1 <= 输入三攻 and 验证魔法攻击力2 > 输入三攻:
                站街实际三攻 = float(k)
        修正魔法攻击力 = 站街实际三攻 - 修正前魔法攻击力
        self.属性设置输入[3][15].setText(str(int(修正魔法攻击力 + 修正魔法攻击力2)))

    def 独立一键修正(self, 输入力智, 输入三攻, 修正独立攻击力2):
        修正前独立攻击力 = self.角色属性B.独立攻击力
        站街独立攻击倍率 = self.角色属性B.站街独立攻击力倍率()
        j = round(输入三攻 / 站街独立攻击倍率, 0)
        站街实际三攻 = int(j)
        for k in range(int(j) - 2, int(j) + 3):
            self.角色属性B.独立攻击力 = float(k)
            验证独立攻击力1 = int(self.角色属性B.站街独立攻击力())
            self.角色属性B.独立攻击力 = float(k + 1)
            验证独立攻击力2 = int(self.角色属性B.站街独立攻击力())
            if 验证独立攻击力1 <= 输入三攻 and 验证独立攻击力2 > 输入三攻:
                站街实际三攻 = float(k)
        修正独立攻击力 = 站街实际三攻 - 修正前独立攻击力
        self.属性设置输入[4][15].setText(str(int(修正独立攻击力 + 修正独立攻击力2)))

    def 物理百分比修正(self, 输入力智, 输入三攻, 修正力量2, 修正物理攻击力2):
        self.力量一键修正(输入力智, 修正力量2)
        self.物攻一键修正(输入力智, 输入三攻, 修正物理攻击力2)

    def 魔法百分比修正(self, 输入力智, 输入三攻, 修正智力2, 修正魔法攻击力2):
        self.智力一键修正(输入力智, 修正智力2)
        self.魔攻一键修正(输入力智, 输入三攻, 修正魔法攻击力2)

    def 物理固伤修正(self, 输入力智, 输入三攻, 修正力量2, 修正独立攻击力2):
        self.力量一键修正(输入力智, 修正力量2)
        self.独立一键修正(输入力智, 输入三攻, 修正独立攻击力2)

    def 魔法固伤修正(self, 输入力智, 输入三攻, 修正智力2, 修正独立攻击力2):
        self.智力一键修正(输入力智, 修正智力2)
        self.独立一键修正(输入力智, 输入三攻, 修正独立攻击力2)

    def 属强修正(self, 输入属强):
        try:
            站街火强 = self.角色属性B.火属性强化加成() + self.角色属性B.火属性强化
        except:
            站街火强 = self.角色属性B.火属性强化
        try:
            站街冰强 = self.角色属性B.冰属性强化加成() + self.角色属性B.冰属性强化
        except:
            站街冰强 = self.角色属性B.冰属性强化
        try:
            站街光强 = self.角色属性B.光属性强化加成() + self.角色属性B.光属性强化
        except:
            站街光强 = self.角色属性B.光属性强化
        try:
            站街暗强 = self.角色属性B.暗属性强化加成() + self.角色属性B.暗属性强化
        except:
            站街暗强 = self.角色属性B.暗属性强化

        if self.属性设置输入[5][15].text() != '':
            修改前 = float(self.属性设置输入[5][15].text())
        else:
            修改前 = 0

        修正前属强 = int(max(站街火强, 站街冰强, 站街光强, 站街暗强))

        for k in range(-2, 3):
            temp = int((输入属强 + k - 修正前属强) / self.角色属性B.所有属性强化增加)
            y = 修正前属强 + temp * self.角色属性B.所有属性强化增加
            if int(y) == 输入属强:
                break

        修改后 = temp + 修改前
        self.属性设置输入[5][15].setText(str(int(修改后)))

    # endregion

    # region 输出界面
    def 词条显示计算(self, 属性, x=0):

        属白换算 = 属性.属性倍率 * 属性.属性附加

        tempstr = []
        # temp = '<font color="{}">'.format(self.辟邪玉显示())
        if x == 0:
            label = "{}：{}"

            tempstr.append(label.format(trans("黄字"), to_percent(属性.伤害增加,
                                                                1)))  # 0
            tempstr.append(label.format(trans("暴伤"), to_percent(属性.暴击伤害,
                                                                1)))  # 1
            tempstr.append(label.format(trans("白字"), to_percent(属性.附加伤害,
                                                                1)))  # 2
            tempstr.append(label.format(trans("属白"), to_percent(属性.属性附加,
                                                                1)))  # 3

            tempstr.append(label.format(trans("终伤"), to_percent(属性.最终伤害,
                                                                1)))  # 4

            tempstr.append(
                label.format(trans("技攻"), to_percent(属性.技能攻击力 - 1, 1)))  # 5

            tempstr.append(label.format(trans("三攻"), to_percent(属性.百分比三攻,
                                                                1)))  # 6

            tempstr.append(label.format(trans("力智"), to_percent(属性.百分比力智,
                                                                1)))  # 7

            tempstr.append(label.format(trans('持续'), to_percent(属性.持续伤害,
                                                                1)))  # 8
            tempstr.append(label.format(trans("攻速"), to_percent(属性.攻击速度,
                                                                1)))  # 9
            tempstr.append(label.format(trans("施放"), to_percent(属性.施放速度,
                                                                1)))  # 10
            tempstr.append(label.format(trans('移速'), to_percent(属性.移动速度,
                                                                1)))  # 11
            if 属白换算 != 0:
                tempstr[2] += '|{}'.format(to_percent(属白换算 + 属性.附加伤害, 1))
                tempstr[3] += '|{}'.format(to_percent(属白换算, 1))
        else:
            label = "{} +{}"
            tempstr.append(
                trans('攻击时,额外增加$的伤害增加量').format(to_percent(属性.伤害增加, 1)))  # 0
            tempstr.append(
                trans('暴击时,额外增加$的伤害增加量').format(to_percent(属性.暴击伤害, 1)))  # 1
            tempstr.append(trans('攻击时,附加$的伤害').format(to_percent(属性.附加伤害,
                                                                 1)))  # 2
            tempstr.append(
                trans('攻击时,附加$的属性伤害').format(to_percent(属性.属性附加, 1)))  # 3

            tempstr.append(label.format(trans("最终伤害"), to_percent(属性.最终伤害,
                                                                  1)))  # 4

            tempstr.append(
                label.format(trans("技能攻击力"), to_percent(属性.技能攻击力 - 1, 1)))  # 5

            tempstr.append(
                label.format(trans("物理、魔法、独立攻击力"), to_percent(属性.百分比三攻,
                                                              1)))  # 6

            tempstr.append(
                label.format(trans("力量、智力"), to_percent(属性.百分比力智, 1)))  # 7

            tempstr.append(
                trans('发生持续伤害X秒,伤害量为对敌人增加造成伤害的$').format(to_percent(
                    属性.持续伤害, 1)))  # 8
            tempstr.append(label.format(trans("攻击速度"), to_percent(属性.攻击速度,
                                                                  1)))  # 9
            tempstr.append(label.format(trans("施放速度"), to_percent(属性.施放速度,
                                                                  1)))  # 10
            tempstr.append(label.format(trans("移动速度"), to_percent(属性.移动速度,
                                                                  1)))  # 11

        # 为防止部分**对显示造成误解，暂不在词条后显示加成
        # date = {2:属性.附加伤害增加增幅,
        #         3:属性.属性附加伤害增加增幅,
        #         5:属性.技能伤害增加增幅,
        #         1:属性.暴击伤害增加增幅,
        #         0:属性.伤害增加增幅,
        #         4:属性.最终伤害增加增幅,
        #         7:属性.力量智力增加增幅,
        #         6:属性.物理魔法攻击力增加增幅}

        # for i in date.keys():
        #     if date[i] != 1.0:
        #         x = date[i] - 1
        #         y = ' +{}%' if x > 0 else ' {}%'
        #         if i in [2, 3] and '|' in tempstr[i]:
        #             y = y.replace(' ', '')
        #         tempstr[i] += temp + '{}</font>'.format(y.format(round(x * 100, 1)))
        return tempstr

    def 面板布局设置(self, 面板显示, x=0):

        初始x = 0
        const = 128 + 19

        # self.main_frame5
        if x == 1:
            初始x += 805
            const += 31

        count = 0

        # 站街力量 站街物攻 进图力量 进图物攻
        for i in [0, 1, 4, 5, 6]:
            面板显示[i].move(20 + 初始x, const + count * 18)
            count += 1
        count = 0

        # 站街力量 站街物攻 进图力量 进图物攻
        # for i in [9, 10, 0, 1]:
        #     面板显示[i].move(20 + 初始x, const + count * 18)
        #     count += 1
        # count = 0

        # 站街智力 站街魔攻 进图智力 进图魔攻
        for i in [2, 3]:
            面板显示[i].move(150 + 初始x, const + count * 18)
            count += 1
        # 独立
        # 面板显示[4].move(150 + 初始x, const + count * 18)
        count = 6

        面板显示[7].move(20 + 初始x, const + 6 * 18)
        面板显示[8].move(150 + 初始x, const + 6 * 18)
        面板显示[9].move(20 + 初始x, const + 7 * 18 - 5)
        面板显示[10].move(150 + 初始x, const + 7 * 18 - 5)

        # 进图属强
        for i in range(len(面板显示) - 1):
            面板显示[i].resize(100, 18)
            面板显示[i].setAlignment(Qt.AlignRight)
            if i in [7, 8, 9, 10]:
                面板显示[i].setAlignment(Qt.AlignCenter)
            if i == 4:
                面板显示[i].resize(155, 18)
        面板显示[5].resize(230, 18)
        面板显示[6].resize(230, 18)
        面板显示[11].resize(230, 18)
        面板显示[11].move(20 + 初始x, const + 5 * 18)
        面板显示[11].setAlignment(Qt.AlignLeft)
        # 面板显示[7].resize(100, 72)
        # 面板显示[7].move(175 + 初始x, const + count * 18 - 75)
        # 面板显示[7].setAlignment(Qt.AlignCenter)
        # 面板显示[7].setStyleSheet('QLabel{font-size:12px}')

    def 面板显示设置(self, 显示, 进图, 站街):

        显示[0].setText(
            '<font color="#FFFFFF">{} </font><font color="#96FF32">{}</font>'.
            format(str(int(站街.站街力量())), str(int(进图.面板力量()))))
        显示[0].setStyleSheet("QLabel{font-size:12px;}")
        显示[1].setText(
            '<font color="#FFFFFF">{} </font><font color="#96FF32">{}</font>'.
            format(str(int(站街.站街物理攻击力())), str(int(进图.面板物理攻击力()))))
        显示[1].setStyleSheet("QLabel{font-size:12px;}")
        显示[2].setText(
            '<font color="#FFFFFF">{} </font><font color="#96FF32">{}</font>'.
            format(str(int(站街.站街智力())), str(int(进图.面板智力()))))
        显示[2].setStyleSheet("QLabel{font-size:12px;}")
        显示[3].setText(
            '<font color="#FFFFFF">{} </font><font color="#96FF32">{}</font>'.
            format(str(int(站街.站街魔法攻击力())), str(int(进图.面板魔法攻击力()))))
        显示[3].setStyleSheet("QLabel{font-size:12px;}")
        显示[4].setText(
            '<font color="#FFFFFF">{} </font><font color="#96FF32">{} </font><font style='
            'color:rgb(114,114,114)'
            '">{}</font>'.format(str(int(站街.站街独立攻击力())),
                                 str(int(进图.面板独立攻击力())),
                                 get_mac_address()[0:8]))
        显示[4].setStyleSheet("QLabel{font-size:12px;}")
        显示[5].setText(
            ('<font color="#FFFFFF">' + trans('火') + '({})' + trans('冰') +
             '({})' + trans('光') + '({})' + trans('暗') + '({})</font>').format(
                 int(站街.火属性强化), int(站街.冰属性强化), int(站街.光属性强化), int(站街.暗属性强化)))
        显示[5].setStyleSheet("QLabel{font-size:12px;}")
        显示[6].setText(
            ('<font color="#96FF32">' + trans('火') + '({})' + trans('冰') +
             '({})' + trans('光') + '({})' + trans('暗') + '({})</font>').format(
                 int(进图.火属性强化), int(进图.冰属性强化), int(进图.光属性强化), int(进图.暗属性强化)))
        显示[6].setStyleSheet("QLabel{font-size:12px;}")
        辟邪玉词条 = self.辟邪玉显示(1)
        for i in range(len(辟邪玉词条)):
            显示[7 + i].setText(辟邪玉词条[i])
            显示[7 + i].setStyleSheet("QLabel{font-size:12px;}")

        显示[11].setText("<font style='color:rgb(20,20,20)'>{}</font>".format(
            get_mac_address()[0:8]))
        显示[11].setStyleSheet("QLabel{font-size:15px;}")

        # 显示[0].setText(str(int(进图.面板力量())))
        # 显示[1].setText(str(int(进图.面板物理攻击力())))
        # 显示[2].setText(str(int(进图.面板智力())))
        # 显示[3].setText(str(int(进图.面板魔法攻击力())))

        # # 独立攻击力
        # tempstr = '<font color="#FFFFFF">{}</font>   '.format(int(
        #     站街.站街独立攻击力()))
        # tempstr += '<font color="#96FF32">{}</font>'.format(int(进图.面板独立攻击力()))
        # 显示[4].setText(tempstr)

        # # 属性强化
        # tempstr = ''
        # # if 进图.所有属性强化增加 != 1.0:
        # #     x = 进图.所有属性强化增加 - 1
        # #     y = ' +{}%' if x > 0 else ' {}%'
        # #     tempstr += '<font color="{}">{}</font>'.format(self.辟邪玉显示(), y.format(round(x * 100, 1)))
        # 显示[5].setText('{}{}'.format(int(进图.火属性强化), tempstr))
        # 显示[6].setText('{}{}'.format(int(进图.冰属性强化), tempstr))
        # 显示[7].setText('{}{}'.format(int(进图.光属性强化), tempstr))
        # 显示[8].setText('{}{}'.format(int(进图.暗属性强化), tempstr))
        # 显示[9].setText(str(int(站街.站街力量())))
        # 显示[10].setText(str(int(站街.站街物理攻击力())))
        # 显示[11].setText(str(int(站街.站街智力())))
        # 显示[12].setText(str(int(站街.站街魔法攻击力())))
        # 显示[13].setText(str(int(站街.火属性强化)))
        # 显示[14].setText(str(int(站街.冰属性强化)))
        # 显示[15].setText(str(int(站街.光属性强化)))
        # 显示[16].setText(str(int(站街.暗属性强化)))
        # 显示[17].setText(self.辟邪玉显示(1))

    def 辟邪玉显示(self, x=0):
        temp = ''
        num = 0
        list = []
        for i in range(4):
            k = self.辟邪玉选择[i].currentIndex()
            if k > 0:
                list.append('{} {}'.format(
                    trans(辟邪玉列表[k].简称), '' if self.辟邪玉数值[i].currentText()
                    == '+0' else self.辟邪玉数值[i].currentText()))
                num += 1
        辟邪玉颜色 = 颜色[{4: '史诗', 3: '传说', 2: '神器', 1: '稀有'}.get(num, '稀有')]
        if x == 0:
            return 辟邪玉颜色
        else:
            if num == 0:
                return ''
            else:
                for i in range(num):
                    list[i] = '<font color="{}">{}</font>'.format(
                        辟邪玉颜色, list[i])
                return list

    def 套装显示设置(self, 显示, 属性):
        count = 0

        显示[count].setText(trans(self.称号.currentData()))
        显示[count].setStyleSheet(
            "QLabel{font-size:12px;color:rgb(255,255,255)}")
        显示[count].setToolTip(self.称号描述())
        count += 1

        显示[count].setText(trans(self.宠物.currentData()))
        显示[count].setStyleSheet(
            "QLabel{font-size:12px;color:rgb(255,255,255)}")
        显示[count].setToolTip(self.宠物描述())
        count += 1

        神话所在套装 = []
        for i in range(11):
            temp = equ.get_equ_by_name(属性.装备栏[i])
            if temp.品质 == '神话':
                神话所在套装.append(temp.所属套装)

        # 套装属性合并
        套装 = []
        套装件数 = []
        套装属性 = []
        套装名称 = 属性.套装栏
        for i in range(len(套装名称)):
            temp = 套装名称[i].split('[')[0]
            if temp not in 套装:
                套装.append(temp)
                套装件数.append([])
                套装属性.append('')
            if len(套装名称[i].split('[')) > 1:
                件数 = 套装名称[i].split('[')[1].split(']')[0]
                套装件数[套装.index(temp)].append(件数)
                套装属性[套装.index(
                    temp
                )] += '<font size="3" face="宋体"><font color="#78FF1E">' + 套装名称[
                    i] + '</font><br>' + equ.get_suit_by_name(套装名称[i]).装备描述(
                        self.角色属性B)[:-4] + '</font><br>'

        # 自适应属性
        if sum(self.角色属性A.自适应选项) != 0:
            套装.append(self.角色属性A.自适应输出())
            套装件数.append([])
            套装属性.append('')
        tempstr = ''
        武器词条属性 = trans(['力智', '三攻', '黄字', '白字', '暴伤', '终伤'])
        if self.希洛克武器词条[0].currentIndex() == 1:
            tempstr += trans("{残香}：$value+10%",
                             value=武器词条属性[self.角色属性A.词条选择[0]])
            if sum(self.希洛克选择状态) == 3:
                tempstr += "|{}+5%".format(武器词条属性[self.角色属性A.词条选择[1]])
            套装.append(tempstr)
            套装件数.append([])
            套装属性.append('')

        # 显示套装
        for i in range(len(套装)):
            if len(套装件数[i]) > 0:
                显示[count].setText(trans(套装[i]) + '[' + str(max(套装件数[i])) + ']')
            else:
                显示[count].setText(trans(套装[i]))
            if 套装[i] in 神话所在套装:
                显示[count].setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(226,150,146)}")
            else:
                显示[count].setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(255,255,255)}")
            显示[count].setToolTip(套装属性[i][:-4])
            count += 1

        try:
            # 显示黑鸦词条
            黑鸦部位 = trans(['武器', '戒指', '辅助装备', '下装'])
            for i in range(4):
                if 属性.黑鸦词条[i][4] != '':
                    显示[count].setText(黑鸦部位[i] + ':' +
                                      属性.黑鸦词条[i][4].replace('<br>', ' '))
                    显示[count].setStyleSheet(
                        "QLabel{font-size:12px;color:rgb(255,255,255)}")
                    count += 1
        except Exception as error:
            logger.error(error)
            pass

    def 打造显示设置(self, 显示, 属性, x=0):
        初始x = 10
        初始y = 31
        pox_y2 = 11

        # self.main_frame5
        if x == 1:
            初始x += 805
            初始y += 20 + pox_y2

        偏移量 = 187
        x坐标 = [
            32, 0, 0, 32, 0, 偏移量, 偏移量 + 32, 偏移量 + 32, 偏移量, 偏移量, 偏移量 + 32, 32
        ]
        y坐标 = [0, 0, 32, 32, 64, 0, 0, 32, 64, 32, 64, 64]

        temp = []
        for i in range(12):
            装备 = equ.get_equ_by_name(属性.装备栏[i])
            打造状态 = 显示[i]
            if 装备.所属套装 != '智慧产物':
                打造状态.setText('+' + str(属性.强化等级[i]))
                if 属性.是否增幅[i] == 1:
                    打造状态.setStyleSheet(
                        "QLabel{color:rgb(228,88,169);font-size:12px;font-weight:Bold}"
                    )
                    temp.append('增幅+{} {}'.format(属性.强化等级[i], 装备.名称))
                else:
                    打造状态.setStyleSheet(
                        "QLabel{color:rgb(25,199,234);font-size:12px;font-weight:Bold}"
                    )
                    temp.append('强化+{} {}'.format(属性.强化等级[i], 装备.名称))

            else:
                打造状态.setText('+' + str(属性.改造等级[i]))
                打造状态.setStyleSheet(
                    "QLabel{color:rgb(249,141,62);font-size:12px;font-weight:Bold;}"
                )
                temp.append('改造+{} {}'.format(属性.改造等级[i], 装备.名称))

            打造状态.move(初始x + x坐标[i] + 13, 初始y + y坐标[i] - 8 - pox_y2)
            打造状态.resize(21, 10)

        装备 = equ.get_equ_by_name(属性.装备栏[11])
        if 装备.所属套装 != '智慧产物' and 属性.武器锻造等级 != 0:
            打造状态 = 显示[12]
            打造状态.setText('+' + str(属性.武器锻造等级))
            打造状态.setStyleSheet(
                "QLabel{color:rgb(232,104,24);font-size:12px;font-weight:Bold}"
            )
            打造状态.move(初始x + x坐标[11] + 13, 初始y + y坐标[11] + 20 - pox_y2)
            temp[11] += '(锻造+{})'.format(属性.武器锻造等级)
            打造状态.resize(21, 10)
        return temp

    def 格式化输出(self, 数字文本, x=0):
        if x == 1:
            返回值 = str('%.2f' % round(int(数字文本) / 100000000, 2))
        elif self.显示选项.isChecked():
            返回值 = str('%.2f' % round(int(数字文本) / 100000000, 2)) + '亿'
        else:
            返回值 = ''
            for i in range(len(数字文本)):
                if len(数字文本) % 3 == 2 and i % 3 == 2:
                    返回值 += ','
                if len(数字文本) % 3 == 1 and i % 3 == 1:
                    返回值 += ','
                if len(数字文本) % 3 == 0 and i % 3 == 0:
                    if i != 0:
                        返回值 += ','
                返回值 += str(数字文本[i])
        return 返回值

    def 称号描述(self):
        temp = '<font size="3" face="宋体">'
        temp += '<font color="#78FF1E">' + \
            trans(self.称号.currentData()) + '</font><br>'
        temp += 称号列表[self.称号.currentIndex()].装备描述(self.角色属性B)[:-4]
        temp += '</font>'
        return temp

    def 宠物描述(self):
        temp = '<font size="3" face="宋体">'
        temp += '<font color="#78FF1E">' + self.宠物.currentText(
        ) + '</font><br>'
        temp += 宠物列表[self.宠物.currentIndex()].装备描述(self.角色属性B)[:-4]
        temp += '</font>'
        return temp

    def 装备描述计算(self, 属性):
        tempstr = []
        数量 = sum(self.希洛克选择状态)

        武器词条属性 = ['力智', '三攻', '黄字', '白字', '暴伤', '终伤']
        希洛克 = self.希洛克属性计算(属性, 1)
        奥兹玛 = self.奥兹玛属性计算(属性, 1)

        for i in range(12):
            装备 = equ.get_equ_by_name(属性.装备栏[i])
            # 名称
            tempstr.append(
                trans(
                    '<font size="3" face="宋体"><font color="$color">{$name}</font>',
                    color=颜色[装备.品质],
                    name=装备.名称))
            # 等级 品质 类型 部位
            tempstr[i] += trans('<br>Lv$level {$rarity} {$type}({$part})',
                                level=装备.等级,
                                rarity=装备.品质,
                                type=装备.类型,
                                part=装备.部位)
            # 套装
            if 装备.所属套装 != '无':
                if 装备.所属套装 != '智慧产物':
                    y = 装备.所属套装
                else:
                    y = 装备.所属套装2
            else:
                y = ''
            if y != '':
                tempstr[i] += trans(
                    '<br><font color="#78FF1E">{$value} {套装}</font>', value=y)

            # 精通描述
            if i < 5:
                x = 属性.防具精通计算(i)
                y = trans('<br>{精通}:')
                for n in 属性.防具精通属性:
                    y += trans(n) + ' '
                tempstr[i] += y + '+' + str(x)

            # 打造描述
            if 装备.所属套装 != '智慧产物':
                # 强化描述
                if 属性.强化等级[i] != 0:
                    if i == 8:
                        tempstr[i] += trans(
                            '<br><font color="#68D5ED">+$value {强化}：',
                            value=属性.强化等级[i])
                        tempstr[i] += trans('{三攻} + $value</font>',
                                            value=耳环计算(装备.等级, 装备.品质,
                                                       属性.强化等级[i]))
                    if i in [9, 10]:
                        tempstr[i] += trans(
                            '<br><font color="#68D5ED">+$value {强化}：',
                            value=属性.强化等级[i])
                        tempstr[i] += trans('{四维} + $value</font>',
                                            value=左右计算(装备.等级, 装备.品质,
                                                       属性.强化等级[i]))
                    if i == 11:
                        tempstr[i] += trans(
                            '<br><font color="#68D5ED">+$value {强化}：',
                            value=属性.强化等级[i])
                        tempstr[i] += trans('{物理攻击力} + $value</font>',
                                            value=武器计算(装备.等级, 装备.品质,
                                                       属性.强化等级[i], 装备.类型,
                                                       '物理'))
                        tempstr[i] += trans(
                            '<br><font color="#68D5ED">+$value {强化}：',
                            value=属性.强化等级[i])
                        tempstr[i] += trans('{魔法攻击力} + $value</font>',
                                            value=武器计算(装备.等级, 装备.品质,
                                                       属性.强化等级[i], 装备.类型,
                                                       '魔法'))
                # 锻造描述
                if i == 11 and 属性.武器锻造等级 != 0:
                    tempstr[i] += trans(
                        '<br><font color="#B36BFF">+$value  {锻造}  ',
                        value=属性.武器锻造等级)
                    tempstr[i] += trans('{独立攻击力} + $value</font>',
                                        value=锻造计算(装备.等级, 装备.品质, 属性.武器锻造等级))

                # 增幅描述
                if 属性.是否增幅[i] == 1:
                    if tempstr[i] != '':
                        tempstr[i] += '<br>'

                    value = 增幅计算(装备.等级, 装备.品质, 属性.强化等级[i], 属性.增幅版本)
                    tempstr[i] += trans("<font color='#FF00FF'>+$value {增幅}：",
                                        value=属性.强化等级[i])
                    if '物理' in 属性.类型 or '力量' in 属性.类型:
                        tempstr[i] += trans('异次元力量')
                    else:
                        tempstr[i] += trans('异次元智力')
                    tempstr[i] += ' +{}</font>'.format(value)

            # 遴选描述
            if tempstr[i] != '':
                tempstr[i] += '<br>'
            if i == 2 and 属性.黑鸦词条[3][0] != 0 and 属性.变换词条[3][1] != 0:
                tempstr[i] += 装备.装备描述_变换属性(属性)[:-4] + "<br>"
                tempstr[i] += 属性.黑鸦词条[3][4]
                # 下装
            elif i == 7 and 属性.黑鸦词条[1][0] != 0 and 属性.变换词条[1][1] != 0:
                tempstr[i] += 装备.装备描述_变换属性(属性)[:-4] + "<br>"
                tempstr[i] += 属性.黑鸦词条[1][4]
                # 戒指
            elif i == 9 and 属性.黑鸦词条[2][0] != 0 and 属性.变换词条[2][1] != 0:
                tempstr[i] += 装备.装备描述_变换属性(属性)[:-4] + "<br>"
                tempstr[i] += 属性.黑鸦词条[2][4]
                # 辅助
            elif i == 11 and 属性.黑鸦词条[0][0] != 0 and 属性.变换词条[0][1] != 0:
                tempstr[i] += 装备.装备描述_变换属性(属性)[:-4] + "<br>"
                tempstr[i] += 属性.黑鸦词条[0][4]
                # 武器
            else:
                tempstr[i] += 装备.装备描述(属性)[:-4]

            # 希洛克描述
            if i in [2, 7, 9]:
                if 希洛克[i] != '':
                    tempstr[i] += trans(
                        '<br><font color="#00A2E8">{希洛克融合属性}：</font><br>')
                    tempstr[i] += 希洛克[i]

            # 奥兹玛描述
            if i in [1, 3, 4, 6, 10]:
                if 奥兹玛[i] != '':
                    tempstr[i] += trans(
                        '<br><font color="#00A2E8">{奥兹玛融合属性}：</font><br>')
                    tempstr[i] += 奥兹玛[i]

            # 希洛克武器描述
            if self.希洛克武器词条[0].currentIndex() > 0 and i == 11:
                tempstr[i] += trans(
                    '<br><font color="#00A2E8">{希洛克融合属性}：</font><br>')
                if self.希洛克武器词条[0].currentIndex() == 1:
                    tempstr[i] += trans("{属性1}：{$value} +10%<br>",
                                        value=武器词条属性[属性.词条选择[0]])
                    if 数量 == 3:
                        tempstr[i] += trans("{属性2}：{$value} +5%<br>",
                                            value=武器词条属性[属性.词条选择[1]])
                else:
                    tempstr[i] += trans(
                        "{属性1}：{$a} +$b%<br>",
                        a=武器词条属性[self.希洛克武器词条[1].currentIndex()],
                        b=(self.希洛克武器词条[3].currentIndex() + 3) * 2)
                    if 数量 == 3:
                        tempstr[i] += trans(
                            "{属性2}：{$a} +$b%<br>",
                            a=武器词条属性[self.希洛克武器词条[2].currentIndex()],
                            b=(self.希洛克武器词条[4].currentIndex() + 3) * 1)
            if tempstr[i].endswith('<br>'):
                tempstr[i] = tempstr[i][:-4]
            tempstr[i] += '</font>'
        return tempstr

    def 百分比输出(self, A, B):
        if B == 0:
            return self.格式化输出(str(int(A)))
        temp1 = A - B
        temp2 = round((A / B - 1) * 100, 2)
        if self.对比格式.isChecked():
            if temp1 == 0:
                return '<font face="宋体">无变化</font>'
            elif temp1 > 0:
                return '<font face="宋体" color= "#96FF1E">+' + self.格式化输出(
                    str(int(temp1)), 1) + ' (' + str(
                        '%.2f' % abs(temp2)) + '%)</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + self.格式化输出(
                    str(int(temp1)), 1) + ' (' + str(
                        '%.2f' % abs(temp2)) + '%)</font>'
        else:
            if temp2 == 0:
                return '<font face="宋体">无变化</font>'
            elif temp2 > 0:
                return '<font face="宋体" color= "#96FF1E">+' + str(
                    '%.2f' % temp2) + '%</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + str(
                    '%.2f' % temp2) + '%</font>'

    def 被动技能描述(self, i):
        tempstr = ''
        if self.角色属性B.技能栏[i].所在等级 != 100 or self.角色属性B.技能栏[i].是否主动 == 0:
            if self.角色属性B.技能栏[i].等级 > 0:
                if self.角色属性B.技能栏[i].自定义描述 == 1:
                    tempstr += '<font face="宋体"><font color="#FF6666">' + trans(
                        self.角色属性B.技能栏[i].名称) + '</font><br>'
                    tempstr += self.角色属性B.技能栏[i].技能描述(self.角色属性B.武器类型)
                else:
                    不适用于title = trans('<font color=gray>({不适用于}：')
                    if self.角色属性B.技能栏[i].关联技能 != [
                            '无'
                    ] and self.角色属性B.技能栏[i].加成倍率(self.角色属性B.武器类型) != 1:
                        加成倍率key = '{加成倍率}：$value<br>'
                        关联技能title = trans('{关联技能}：')
                        tempstr += trans(
                            '<font face="宋体"><font color="#FF6666">{$value}</font><br>',
                            value=self.角色属性B.技能栏[i].名称)
                        tempstr += trans(
                            加成倍率key,
                            value=to_percent(
                                self.角色属性B.技能栏[i].加成倍率(self.角色属性B.武器类型) - 1,
                                2))
                        tempstr += 关联技能title
                        for j in self.角色属性B.技能栏[i].关联技能:
                            tempstr += trans(j)
                            if j != self.角色属性B.技能栏[i].关联技能[-1]:
                                tempstr += ','
                        if self.角色属性B.技能栏[i].非关联技能 != ['无']:
                            tempstr += 不适用于title
                            for j in self.角色属性B.技能栏[i].非关联技能:
                                tempstr += trans(j)
                                if j != self.角色属性B.技能栏[i].非关联技能[-1]:
                                    tempstr += ','
                            tempstr += ')</font>'
                        if self.角色属性B.技能栏[i].关联技能2 != ['无']:
                            tempstr += "<br>" + trans(
                                加成倍率key,
                                value=to_percent(
                                    self.角色属性B.技能栏[i].加成倍率2(self.角色属性B.武器类型) -
                                    1, 2))
                            tempstr += 关联技能title
                            for k in self.角色属性B.技能栏[i].关联技能2:
                                tempstr += trans(k)
                                if k != self.角色属性B.技能栏[i].关联技能2[-1]:
                                    tempstr += ','
                        if self.角色属性B.技能栏[i].非关联技能2 != ['无']:
                            tempstr += 不适用于title
                            for j in self.角色属性B.技能栏[i].非关联技能2:
                                tempstr += trans(j)
                                if j != self.角色属性B.技能栏[i].非关联技能2[-1]:
                                    tempstr += ','
                            tempstr += ')</font>'
                        if self.角色属性B.技能栏[i].关联技能3 != ['无']:
                            tempstr += "<br>" + trans(
                                加成倍率key,
                                value=to_percent(
                                    self.角色属性B.技能栏[i].加成倍率3(self.角色属性B.武器类型) -
                                    1, 2))
                            tempstr += 关联技能title
                            for l in self.角色属性B.技能栏[i].关联技能3:
                                tempstr += trans(l)
                                if l != self.角色属性B.技能栏[i].关联技能3[-1]:
                                    tempstr += ','
                        if self.角色属性B.技能栏[i].非关联技能3 != ['无']:
                            tempstr += 不适用于title
                            for j in self.角色属性B.技能栏[i].非关联技能3:
                                tempstr += trans(j)
                                if j != self.角色属性B.技能栏[i].非关联技能3[-1]:
                                    tempstr += ','
                            tempstr += ')</font>'
                    if self.角色属性B.技能栏[i].冷却关联技能 != [
                            '无'
                    ] and self.角色属性B.技能栏[i].CD缩减倍率(self.角色属性B.武器类型) != 1:
                        冷却关联title = trans('{冷却关联技能}：')
                        冷却缩减key = "{冷却缩减}：$value<br>"
                        if tempstr == '':
                            tempstr += trans(
                                '<font face="宋体"><font color="#FF6666">{$value}</font><br>',
                                value=self.角色属性B.技能栏[i].名称)
                        else:
                            tempstr += '<br>'
                        tempstr += trans(
                            冷却缩减key,
                            value=to_percent(
                                1 - self.角色属性B.技能栏[i].CD缩减倍率(self.角色属性B.武器类型),
                                2))
                        tempstr += 冷却关联title
                        for j in self.角色属性B.技能栏[i].冷却关联技能:
                            tempstr += trans(j)
                            if j != self.角色属性B.技能栏[i].冷却关联技能[-1]:
                                tempstr += ','
                        if self.角色属性B.技能栏[i].非冷却关联技能 != ['无']:
                            tempstr += 不适用于title
                            for j in self.角色属性B.技能栏[i].非冷却关联技能:
                                tempstr += trans(j)
                                if j != self.角色属性B.技能栏[i].非冷却关联技能[-1]:
                                    tempstr += ','
                            tempstr += ')</font>'
                        if self.角色属性B.技能栏[i].冷却关联技能2 != ['无']:
                            tempstr += trans(
                                冷却缩减key,
                                value=to_percent(
                                    1 -
                                    self.角色属性B.技能栏[i].CD缩减倍率2(self.角色属性B.武器类型),
                                    2))
                            tempstr += 冷却关联title
                            for j in self.角色属性B.技能栏[i].冷却关联技能2:
                                tempstr += trans(j)
                                if j != self.角色属性B.技能栏[i].冷却关联技能2[-1]:
                                    tempstr += ','
                        if self.角色属性B.技能栏[i].非冷却关联技能2 != ['无']:
                            tempstr += 不适用于title
                            for j in self.角色属性B.技能栏[i].非冷却关联技能2:
                                tempstr += trans(j)
                                if j != self.角色属性B.技能栏[i].非冷却关联技能2[-1]:
                                    tempstr += ','
                            tempstr += ')</font>'
                        if self.角色属性B.技能栏[i].冷却关联技能3 != ['无']:
                            tempstr += trans(
                                冷却缩减key,
                                value=to_percent(
                                    1 -
                                    self.角色属性B.技能栏[i].CD缩减倍率3(self.角色属性B.武器类型),
                                    2))
                            tempstr += 冷却关联title
                            for j in self.角色属性B.技能栏[i].冷却关联技能3:
                                tempstr += trans(j)
                                if j != self.角色属性B.技能栏[i].冷却关联技能3[-1]:
                                    tempstr += ','
                        if self.角色属性B.技能栏[i].非冷却关联技能3 != ['无']:
                            tempstr += 不适用于title
                            for j in self.角色属性B.技能栏[i].非冷却关联技能3:
                                tempstr += trans(j)
                                if j != self.角色属性B.技能栏[i].非冷却关联技能3[-1]:
                                    tempstr += ','
                            tempstr += ')</font>'
        return tempstr

    def 输出界面(self, index, name=''):
        # 调试模式下 index为-1
        flag = 1
        if index < 0:
            flag = 0
            index = 0
            武器名称 = ''
            for i in equ.get_equ_list():
                if i.类型 == self.角色属性A.武器选项[0]:
                    武器名称 = i.名称
                    break
            #调试模式默认图标显示
            self.排行数据.append([
                '撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂',
                '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的心之所念', '军神的遗书', '军神的庇护宝石',
                武器名称, 0, '噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]',
                '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]', '无'
            ])

        pdata = {}
        装备名称 = self.排行数据[index][0:12]
        套装名称 = self.排行数据[index][13:-1]
        百变怪 = self.排行数据[index][-1]

        self.角色属性B = deepcopy(self.角色属性A)
        self.角色属性B.穿戴装备(装备名称, 套装名称)

        #C为站街属性
        C = self.站街计算(装备名称, 套装名称)
        if flag == 1:
            self.角色属性B.其它属性计算()

        词条提升率计算 = deepcopy(self.角色属性B)
        统计详情 = self.角色属性B.伤害计算(1)
        # self.角色属性B.计算自适应方式 = 0

        # 最大输出界面限制
        if len(self.输出窗口列表) >= 10:
            del self.输出窗口列表[0]

        输出窗口 = QWidget()
        输出窗口.setStyleSheet('''QToolTip {
           background-color: black;
           color: white;
           border: 0px
           }
           QLabel {
               font-size:12px;
            }''')

        输出窗口.setFixedSize(788, 546)
        pox_y = 18
        pox_y2 = 11
        temp = ''
        if name == '':
            temp += trans('详细数据') + ' 仅供参考 带节奏死个🐎' + ' ' + get_mac_address()
            # if self.角色属性A.计算自适应方式 == 1:
            #     temp+= ' - 全局择优'
            # else:
            #     temp+= ' - 局部择优'
        else:
            temp += name
        # temp += "装备版本："+self.角色属性A.版本 + " 增幅版本：" + self.角色属性A.增幅版本

        输出窗口.setWindowTitle(temp)
        输出窗口.setWindowIcon(self.icon)
        QLabel(输出窗口).setPixmap(self.输出背景图片)
        人物 = QLabel(输出窗口)
        图片 = QPixmap('./ResourceFiles/' + self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(90 + int(45 - 图片.width() / 2), 40 - pox_y2)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)

        excel = []
        for i in range(len(self.角色属性B.技能栏)):
            excel.append(统计详情[i * 4 + 1])
        excel.sort()

        面板显示 = []
        for i in range(18):
            面板显示.append(QLabel(输出窗口))

        self.面板布局设置(面板显示)

        self.面板显示设置(面板显示, self.角色属性B, C)

        j = 312
        pdata['词条'] = self.词条显示计算(self.角色属性B)
        词条解释 = self.词条显示计算(self.角色属性B, 1)
        for i in range(0, len(pdata['词条'])):
            templab = QLabel(输出窗口)
            templab.setText(pdata['词条'][i])
            if i == 5 and self.角色属性B.技能攻击力累加 > 2:
                templab.setStyleSheet(
                    "QLabel{font-size:12px;color:red}")
            else:
                templab.setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(104,213,237)}")
            templab.move(7, j - pox_y2)
            templab.resize(180, 17)
            templab.setAlignment(Qt.AlignLeft)
            templab.setToolTip('<font color="#B99460">' + 词条解释[i] + '</font>')
            j += 17

        位置 = 308
        间隔 = 17

        套装名称显示 = []
        for i in range(16):
            套装名称显示.append(QLabel(输出窗口))
            套装名称显示[i].move(114, 位置 - pox_y2 + 间隔 * i)
            套装名称显示[i].resize(150, 18)
            套装名称显示[i].setAlignment(Qt.AlignCenter)
            套装名称显示[i].setText('')

        self.套装显示设置(套装名称显示, self.角色属性B)

        实际技能等级 = []
        技能等效CD = []
        for i in self.角色属性B.技能栏:
            实际技能等级.append(i.等级)
            if i.是否有伤害 == 1:
                技能等效CD.append(i.等效CD(self.角色属性B.武器类型, self.角色属性B.类型))
            else:
                技能等效CD.append(0)

        总伤害数值 = 0

        count = 0
        for i in range(len(self.角色属性B.技能栏)):
            if 统计详情[i * 4 + 1] != 0:
                count += 1

        self.行高 = 32

        伤害列表 = []
        for i in range(len(self.角色属性B.技能栏)):
            伤害列表.append(统计详情[i * 4 + 1])
            总伤害数值 += 统计详情[i * 4 + 1]
        伤害列表.sort(reverse=True)
        try:
            self.exports_store()
            更新人物名望()
            # TODO: 重新布局
            总名望 = store.get("/fame/temp_result")
            名望详情 = store.get("/fame/temp_result/detail")
            if 总名望 > 0:
                dmi = ((总伤害数值 / 1e8) / pow((总名望 / (1e4) - 0.5), 3))
                templabel = QLabel(输出窗口)
                templabel.setText("{} ({})".format(总名望, round(dmi, 2)))
                templabel.setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(255,255,255)}")
                templabel.move(130, 110)
                templabel.resize(100, 42)
                templabel.setToolTip(
                    '系数计算公式:dmi = ((总伤害数值 / 1e8) / pow((总名望 / (1e4) - 0.5), 3))<br>'
                    + str(名望详情))

        except Exception as e:
            logger.error(e)
        if len(self.基准值) != 0:
            显示模式 = 1
        else:
            显示模式 = 0

        main = 技能详情(输出窗口, self, 统计详情, excel, 实际技能等级, 技能等效CD, 显示模式, count)
        pdata['技能'] = main.data
        main.setGeometry(277, 36 - pox_y, 498, 455)

        # region 被动详情
        num = 0
        for i in range(len(self.角色属性B.技能栏)):
            # Will修改
            tempstr = self.被动技能描述(i)
            if tempstr != '':
                tempstr += '</font>'
                被动数据 = QLabel(输出窗口)
                被动数据.setPixmap(self.技能图片[i])
                被动数据.setToolTip(tempstr)
                被动数据.move(293 + num * 40, 500 - pox_y)
                被动等级 = QLabel(输出窗口)
                被动等级.setText('Lv.' + str(实际技能等级[i]))
                被动等级.move(293 - 6 + num * 40, 480 - pox_y)
                被动等级.resize(40, 28)
                if 实际技能等级[i] != 0:
                    被动等级.setStyleSheet(
                        "QLabel{font-size:12px;color:rgb(255,255,255)}")
                else:
                    被动等级.setStyleSheet(
                        "QLabel{font-size:12px;color:rgb(255,0,0)}")
                被动等级.setAlignment(Qt.AlignCenter)
                num += 1

        if self.角色属性B.远古记忆 > 0:
            被动数据 = QLabel(输出窗口)
            被动数据.setPixmap((QPixmap('./ResourceFiles/img/远古记忆.png')))
            tempstr = trans(
                '<font face="宋体"><font color="#FF6666">{远古记忆}</font><br>{智力}+$value</font>',
                value=self.角色属性B.远古记忆 * 15)
            被动数据.setToolTip(tempstr)
            被动数据.move(293 + num * 40, 500 - pox_y)
            被动等级 = QLabel(输出窗口)
            被动等级.setText('Lv.' + str(self.角色属性B.远古记忆))
            被动等级.move(293 - 6 + num * 40, 480 - pox_y)
            被动等级.resize(40, 28)
            被动等级.setAlignment(Qt.AlignCenter)
            被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            num += 1

        if self.角色属性B.刀魂之卡赞 > 0:
            被动数据 = QLabel(输出窗口)
            被动数据.setPixmap((QPixmap('./ResourceFiles/img/刀魂之卡赞.png')))
            tempstr = trans(
                '<font face="宋体"><font color="#FF6666">{刀魂之卡赞}</font><br>{力量、智力}+$value</font>',
                value=刀魂之卡赞数据[self.角色属性B.刀魂之卡赞])
            被动数据.setToolTip(tempstr)
            被动数据.move(293 + num * 40, 500 - pox_y)
            被动等级 = QLabel(输出窗口)
            被动等级.setText('Lv.' + str(self.角色属性B.刀魂之卡赞))
            被动等级.move(293 - 6 + num * 40, 480 - pox_y)
            被动等级.resize(40, 28)
            被动等级.setAlignment(Qt.AlignCenter)
            被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            num += 1
        # endregion

        总伤害 = QLabel(输出窗口)
        总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        if 显示模式 == 1:
            总伤害.setText(self.百分比输出(总伤害数值, self.基准值[0]))
        else:
            总伤害.setText(self.格式化输出(str(int(总伤害数值))))
        总伤害.resize(250, 36)
        总伤害.move(10, 520 - pox_y2)
        总伤害.setAlignment(Qt.AlignCenter)

        初始x = 10
        初始y = 31

        图片列表 = self.获取装备图片(self.排行数据[index])

        偏移量 = 187
        x坐标 = [
            32, 0, 0, 32, 0, 偏移量, 偏移量 + 32, 偏移量 + 32, 偏移量, 偏移量, 偏移量 + 32, 32
        ]
        y坐标 = [0, 0, 32, 32, 64, 0, 0, 32, 64, 32, 64, 64]

        tempstr = self.装备描述计算(self.角色属性B)

        for i in range(12):
            装备图标 = QLabel(输出窗口)
            装备图标.setMovie(图片列表[i])
            装备图标.resize(26, 26)
            装备图标.move(初始x + x坐标[i], 初始y + y坐标[i] - pox_y2)
            装备图标.setAlignment(Qt.AlignCenter)
            if self.角色属性B.装备栏[i] == 百变怪:
                图标遮罩 = QLabel(输出窗口)
                图标遮罩.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                图标遮罩.resize(26, 26)
                图标遮罩.move(初始x + x坐标[i], 初始y + y坐标[i] - pox_y2)
                图标遮罩.setToolTip(tempstr[i])
            else:
                装备图标.setToolTip(tempstr[i])

        打造显示 = []
        for i in range(13):
            打造显示.append(QLabel(输出窗口))
            打造显示[i].move(-100, -100)

        temp = self.打造显示设置(打造显示, self.角色属性B)

        pdata['名称'] = self.角色属性A.实际名称
        pdata['装备'] = temp

        if 多语言开关 == 0:
            label = QLabel(输出窗口)
            label.setText(get_mac_address())
            label.setStyleSheet(
                f'QLabel{{font-size:15px;{make_watermark_qt_color_string(watermark_surrounding_backgroud_color_detail)};font-weight:bolder}}'
            )
            label.move(290, 540 - pox_y)
            butten = QtWidgets.QPushButton(trans('输出技能数据'), 输出窗口)
            butten.clicked.connect(
                lambda state, d=deepcopy(pdata): self.输出数据(d))
            butten.move(676, 540 - pox_y)
            butten.setStyleSheet(按钮样式)
            butten.resize(90, 21)
            词条提升率计算.输出提升率 = 总伤害数值
            butten = QtWidgets.QPushButton(trans('输出择优数据'), 输出窗口)
            butten.clicked.connect(lambda state: 词条提升率计算.伤害计算(0))
            butten.move(575, 540 - pox_y)
            butten.setStyleSheet(按钮样式)
            butten.resize(90, 21)

        输出显示 = MainWindow(输出窗口)
        self.输出窗口列表.append(输出显示)
        输出显示.show()

    def 输出数据(self, d):
        try:
            increase_counter(ga_category="carry详细功能使用", name="输出技能数据")
            path = './详细数据'
            if not os.path.exists(path):
                os.makedirs(path)

            count = max(len(d['装备']), len(d['词条']), len(d['技能']))
            rows = []
            for i in range(count):
                t = d['词条'][i].split('：') if i < len(d['词条']) else []
                rows.append([
                    (str(d['装备'][i]) if i < len(d['装备']) else ''),
                    (str(t[0][-2] + t[0][-1]) if i < len(d['词条']) else ''),
                    (str(t[1]) if i < len(d['词条']) else ''),
                    '',
                    (str(d['技能'][i][0]) if i < len(d['技能']) else ''),
                    (str(d['技能'][i][1]) if i < len(d['技能']) else ''),
                    (str(d['技能'][i][2]) if i < len(d['技能']) else ''),
                    (str(d['技能'][i][3]) if i < len(d['技能']) else ''),
                    (str(d['技能'][i][4]) if i < len(d['技能']) else ''),
                    (str(d['技能'][i][5]) if i < len(d['技能']) else ''),
                    (str(d['技能'][i][6]) if i < len(d['技能']) else ''),
                    (str(d['技能'][i][7]) if i < len(d['技能']) else ''),
                ])
            result_path = os.path.join(
                path, '{}-{}.csv'.format(d['名称'],
                                         time.strftime('%m-%d-%H-%M-%S')))
            result = open(result_path, 'w', encoding='gbk')
            result.write(
                "装备,词条类型,词条数值,,技能名称,技能等级,技能CD,技能次数,总伤害,平均伤害,伤害占比,技能倍率\n")
            for row in rows:
                result.write(','.join(row) + '\n')
            result.close()
            os.startfile(result_path)
        except Exception as error:
            pass

    # endregion

    # region 输入属性
    def 输入属性(self, 属性, x=0):

        i = self.攻击目标.currentIndex()
        属性.防御输入 = 攻击目标[i][1]
        属性.火抗输入 = 攻击目标[i][2]
        属性.冰抗输入 = 攻击目标[i][3]
        属性.光抗输入 = 攻击目标[i][4]
        属性.暗抗输入 = 攻击目标[i][5]

        if self.初始属性.远古记忆 != -1:
            属性.远古记忆 = self.远古记忆.currentIndex()
        if self.初始属性.刀魂之卡赞 != -1:
            属性.刀魂之卡赞 = self.刀魂之卡赞.currentIndex()

        属性.自适应选项 = copy([(1 if self.红色宠物装备.isChecked() else 0),
                         (1 if self.光环自适应.isChecked() else 0)])
        # 属性.计算自适应方式 = self.单套择优方式选项.currentIndex()

        if self.转甲选项.isChecked():
            属性.转甲选项 = 1
        else:
            属性.转甲选项 = 0

        for j in [self.等级调整, self.TP输入, self.次数输入, self.宠物次数]:
            for i in j:
                if i != '' and i.currentIndex() == -1:
                    i.setCurrentIndex(0)

        for i in 属性.技能栏:
            i.等级 = i.基础等级 + int(self.等级调整[self.角色属性A.技能序号[i.名称]].currentData())
            if i.是否有伤害 == 1:
                if i.TP上限 != 0:
                    i.TP等级 = int(
                        self.TP输入[self.角色属性A.技能序号[i.名称]].currentData())

        if x == 0:
            self.辟邪玉属性计算(属性)
        elif x >= 100:
            y = x - 100
            辟邪玉列表[y].当前值 = 辟邪玉列表[y].最大值
            辟邪玉列表[y].穿戴属性(属性)

        if sum(self.希洛克选择状态) == 3:
            属性.武器词条触发 = 1

        if self.希洛克武器词条[0].currentIndex() == 1:
            属性.希洛克武器词条 = 1
        elif self.希洛克武器词条[0].currentIndex() == 2:
            词条属性列表[self.希洛克武器词条[1].currentIndex()].加成属性(
                属性, (self.希洛克武器词条[3].currentIndex() + 3) * 0.02)
            if 属性.武器词条触发 == 1:
                词条属性列表[self.希洛克武器词条[2].currentIndex()].加成属性(
                    属性, (self.希洛克武器词条[4].currentIndex() + 3) * 0.01)
        try:
            属性.时间输入 = int(float(self.时间输入.currentText()))
        except:
            属性.时间输入 = 25
        属性.次数输入.clear()
        属性.宠物次数.clear()
        属性.装备切装.clear()
        属性.技能切装.clear()
        self.是否计算 = 1
        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.是否有伤害 == 1:
                s = self.次数输入[序号].currentText()
                s = s.replace('，', ',').replace('（', '(').replace('）', ')')
                try:
                    if eval(s.replace('/CD', '1')) >= 0:
                        属性.次数输入.append(s)
                except Exception as e:
                    logger.error(e)
                    QMessageBox.information(self, "错误",
                                            "“{}”技能次数输入错误，请重新输入".format(i.名称))
                    self.是否计算 = 0
                    break

                s = self.宠物次数[序号].currentText().replace('，', ',').replace(
                    '（', '(').replace('）', ')')
                try:
                    if eval(s.replace('num', '1')) >= 0:
                        属性.宠物次数.append(s)
                except:
                    QMessageBox.information(self, "错误",
                                            "“{}”宠物次数输入错误，请重新输入".format(i.名称))
                    self.是否计算 = 0
                    break

                if 切装模式 == 1:
                    if self.技能切装[序号].isChecked():
                        属性.技能切装.append(1)
                    else:
                        属性.技能切装.append(0)
            else:
                属性.次数输入.append('0')
                属性.宠物次数.append('0')
                属性.技能切装.append(0)
        if 切装模式 == 1:
            for i in range(12):
                if self.装备切装[i].isChecked():
                    属性.装备切装.append(self.自选装备[i].currentData())
                else:
                    属性.装备切装.append('无')

        for i in range(len(self.复选框列表)):
            if self.复选框列表[i].isChecked():
                选项设置列表[选项设置序号[self.复选框列表list[i]]].适用效果(属性)

        count = 0
        count2 = 0
        for i in equ.get_equ_list():
            if i.品质 == '神话':
                i.属性1选择 = self.神话属性选项[count * 4 + 0].currentIndex()
                i.属性2选择 = self.神话属性选项[count * 4 + 1].currentIndex()
                i.属性3选择 = self.神话属性选项[count * 4 + 2].currentIndex()
                i.属性4选择 = self.神话属性选项[count * 4 + 3].currentIndex()
                count += 1
            if i.所属套装 == '智慧产物':
                i.属性1选择 = self.改造产物选项[count2 * 4 + 0].currentIndex()
                i.属性2选择 = self.改造产物选项[count2 * 4 + 1].currentIndex()
                i.属性3选择 = self.改造产物选项[count2 * 4 + 2].currentIndex()
                i.属性4选择 = self.改造产物选项[count2 * 4 + 3].currentIndex()
                count2 += 1

        属性.攻击属性 = self.攻击属性选项.currentIndex()

        称号列表[self.称号.currentIndex()].城镇属性(属性)
        if 属性.称号触发:
            称号列表[self.称号.currentIndex()].触发属性(属性)

        宠物列表[self.宠物.currentIndex()].城镇属性(属性)

        self.加载护石(属性)

        for i in range(12):
            属性.是否增幅[i] = self.装备打造选项[i].currentIndex()
            属性.强化等级[i] = self.装备打造选项[i + 12].currentIndex()
            属性.改造等级[i] = self.装备打造选项[i + 24].currentIndex()
        属性.武器锻造等级 = self.装备打造选项[36].currentIndex()
        属性.类型 = self.装备打造选项[37].currentData()

        try:
            属性.主BUFF = float(self.BUFF输入.text()) / 100 + 1
        except:
            QMessageBox.information(self, "错误", "BUFF数值输入错误,已设置为默认数值")
            self.BUFF输入.setText(str('%.1f' % ((self.角色属性A.主BUFF - 1) * 100)))

        try:
            if self.觉醒选择状态 == 1:
                属性.觉醒之抉择技能 = 属性.技能栏[self.一觉序号].名称
            elif self.觉醒选择状态 == 2:
                属性.觉醒之抉择技能 = 属性.技能栏[self.二觉序号].名称
            if self.角色属性A.屏蔽三觉 == True:
                属性.技能栏[self.三觉序号].关联技能 = ['无']
            else:
                if self.角色属性A.技能栏[self.三觉序号].是否有伤害 == 1 and str(
                        属性.次数输入[self.三觉序号]) == '0':
                    属性.技能栏[self.三觉序号].关联技能 = ['无']
                else:
                    属性.技能栏[self.三觉序号].关联技能 = [属性.觉醒之抉择技能]
        except:
            pass

        属性.角色熟练度 = self.装备条件选择[0].currentIndex()
        属性.技能栏空位 = self.装备条件选择[1].currentIndex()
        属性.命运的抉择 = self.装备条件选择[2].currentIndex()
        属性.天命无常 = self.装备条件选择[3].currentIndex()
        属性.悲剧的残骸 = self.装备条件选择[4].currentIndex()
        属性.先知者的预言 = self.装备条件选择[5].currentIndex()
        属性.贫瘠沙漠的遗产 = self.装备条件选择[6].currentIndex()
        属性.幸运三角 = self.装备条件选择[7].currentIndex()
        属性.擎天战甲 = self.装备条件选择[8].currentIndex()
        属性.持续伤害计算比例 = 1 - 0.01 * self.装备条件选择[9].currentIndex()
        属性.军神的隐秘遗产 = self.装备条件选择[10].currentIndex()
        属性.太极天帝剑 = self.装备条件选择[11].currentIndex()
        属性.噙毒手套 = self.装备条件选择[12].currentIndex()
        # 属性.绿色生命的面容 = self.装备条件选择[12].currentIndex()
        属性.产物升级 = 1 if self.智慧产物升级.isChecked() else 0
        属性.黑鸦武器择优模式 = self.武器择优模式.currentIndex()
        属性.黑鸦词条 = []
        for i in range(4):
            temp = [
                self.黑鸦词条[i][0].currentIndex(), self.黑鸦词条[i][1].currentIndex(),
                ((2 if i > 0 else 4)) * (self.黑鸦词条[i][2].currentIndex() + 1), 0
            ]
            属性.黑鸦词条.append(temp)
        self.希洛克属性计算(属性)
        self.奥兹玛属性计算(属性)
        self.基础属性(属性)

    def 基础属性(self, 属性):
        if 切装模式 == 1:
            属性.切装修正.clear()
            名称 = ['力量', '智力', '物攻', '魔攻', '独立', '属强']
            num = 0
            for i in self.切装修正属性:
                try:
                    if i.text() != '':
                        属性.切装修正.append(int(i.text()))
                    else:
                        属性.切装修正.append(0)
                except:
                    QMessageBox.information(self, "错误",
                                            名称[num] + " 切装修正输入格式错误，已重置为空")
                    i.setText('')
                    属性.切装修正.append(0)
                num += 1

        for i in range(len(self.列名称) - 3):
            for j in range(len(行名称1)):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except:
                        QMessageBox.information(
                            self, "错误",
                            self.行名称[(j + len(行名称1)) if i >= len(列名称1) else j]
                            + "：" + self.列名称[i] + "  输入格式错误，已重置为空")
                        self.属性设置输入[i][j].setText('')

        temp = []
        num = len(self.列名称) - 3
        for j in range(len(self.属性设置输入[num])):
            if self.属性设置输入[num][j].text() != '':
                try:
                    temp.append(float(self.属性设置输入[num][j].text()) / 100)
                    if temp[-1] > 1 or temp[-1] < -0.2:
                        QMessageBox.information(
                            self, "错误",
                            self.修正列表名称[j] + " 输入数值超出[-20,100]，已重置为空")
                        temp[-1] = 0.0
                        self.属性设置输入[num][j].setText('')
                except:
                    temp.append(0.0)
                    QMessageBox.information(self, "错误",
                                            self.修正列表名称[j] + " 输入格式错误，已重置为空")
                    self.属性设置输入[num][j].setText('')
            else:
                temp.append(0.0)

        属性.百分比力智加成(temp[0])
        属性.百分比三攻加成(temp[1])
        属性.伤害增加加成(temp[2])
        属性.附加伤害加成(temp[3])
        属性.属性附加加成(temp[4])
        属性.暴击伤害加成(temp[5])
        属性.最终伤害加成(temp[6])
        属性.技能攻击力加成(temp[7])

        for i in [0, 6, 9]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 0 and j in [1, 5, 10, 16]:
                        属性.进图力量 += float(self.属性设置输入[i][j].text())
                    else:
                        属性.力量 += float(self.属性设置输入[i][j].text())
        for i in [1, 6, 9]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 1 and j in [1, 5, 10, 16]:
                        属性.进图智力 += float(self.属性设置输入[i][j].text())
                    else:
                        属性.智力 += float(self.属性设置输入[i][j].text())

        for i in [2, 7, 10]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 2 and j in [1, 5, 10, 16]:
                        属性.进图物理攻击力 += float(self.属性设置输入[i][j].text())
                    else:
                        属性.物理攻击力 += float(self.属性设置输入[i][j].text())

        for i in [3, 7, 10]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 3 and j in [1, 5, 10, 16]:
                        属性.进图魔法攻击力 += float(self.属性设置输入[i][j].text())
                    else:
                        属性.魔法攻击力 += float(self.属性设置输入[i][j].text())

        for i in [4, 7, 10]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 4 and j in [1, 5, 10, 16]:
                        属性.进图独立攻击力 += float(self.属性设置输入[i][j].text())
                    else:
                        属性.独立攻击力 += float(self.属性设置输入[i][j].text())

        for i in [5, 8]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 5 and j in [1, 5, 10, 16]:
                        属性.进图属强 += float(self.属性设置输入[i][j].text())
                    elif i == 5 and j == 3:  # 3为婚房不吃辟邪玉
                        属性.所有属性强化(float(self.属性设置输入[i][j].text()))
                    else:
                        属性.所有属性强化加成(float(self.属性设置输入[i][j].text()))

        for i in self.细节选项输入:
            for j in i:
                if j.isEnabled():
                    if j.currentData() not in ['', '无']:
                        try:
                            细节选项列表[细节选项序号[j.currentData()]].效果(属性)
                        except:
                            for k in 属性.技能栏:
                                if j.currentData() == k.名称 + 'Lv+1':
                                    k.等级加成(1)
                                    break

        if self.奶量buff输入[0].text() not in ['', '无']:
            # print(属性.力量)
            属性.进图力量 += int(self.奶量buff输入[0].text())
            属性.进图智力 += int(self.奶量buff输入[0].text())
            # print(属性.力量)

        if self.奶量buff输入[1].text() not in ['', '无']:
            属性.进图物理攻击力 += int(self.奶量buff输入[1].text())
            属性.进图魔法攻击力 += int(self.奶量buff输入[1].text())
            属性.进图独立攻击力 += int(self.奶量buff输入[1].text())

        # 守门人全属强方案
        if self.守门人全属强.isChecked():
            if self.属性设置输入[0][14].text() != '':
                属性.力量 -= float(self.属性设置输入[0][14].text())
            if self.属性设置输入[1][14].text() != '':
                属性.智力 -= float(self.属性设置输入[1][14].text())
            if self.属性设置输入[2][14].text() != '':
                属性.物理攻击力 -= float(self.属性设置输入[2][14].text())
            if self.属性设置输入[3][14].text() != '':
                属性.魔法攻击力 -= float(self.属性设置输入[3][14].text())
            if self.属性设置输入[4][14].text() != '':
                属性.独立攻击力 -= float(self.属性设置输入[4][14].text())
            if self.属性设置输入[5][7].text() != '':
                属性.所有属性强化加成(-(float(self.属性设置输入[5][7].text())))
            if self.属性设置输入[5][14].text() != '':
                属性.所有属性强化加成(-(float(self.属性设置输入[5][14].text())))

            for j in range(5, 10):
                if self.属性设置输入[6][j].text() != '':
                    属性.力量 -= float(self.属性设置输入[6][j].text())
                    属性.智力 -= float(self.属性设置输入[6][j].text())
                if self.属性设置输入[7][j].text() != '':
                    属性.物理攻击力 -= float(self.属性设置输入[7][j].text())
                    属性.魔法攻击力 -= float(self.属性设置输入[7][j].text())
                    属性.独立攻击力 -= float(self.属性设置输入[7][j].text())
                if self.属性设置输入[8][j].text() != '':
                    属性.所有属性强化加成(-(float(self.属性设置输入[8][j].text())))

            属性.物理攻击力 += 60
            属性.魔法攻击力 += 60
            属性.独立攻击力 += 60
            属性.所有属性强化加成(int(28 * 3 + 12 + 30 + 7))

            # 龙珠时附魔不替换
            if self.属性设置输入[7][11].text() == '' or self.属性设置输入[8][11].text(
            ) == '':
                if self.属性设置输入[6][11].text() != '':
                    属性.力量 -= float(self.属性设置输入[6][11].text())
                    属性.智力 -= float(self.属性设置输入[6][11].text())
                if self.属性设置输入[7][11].text() != '':
                    属性.物理攻击力 -= float(self.属性设置输入[7][11].text())
                    属性.魔法攻击力 -= float(self.属性设置输入[7][11].text())
                    属性.独立攻击力 -= float(self.属性设置输入[7][11].text())
                if self.属性设置输入[8][11].text() != '':
                    属性.所有属性强化加成(-(float(self.属性设置输入[8][11].text())))
                # 武器全属强为13
                属性.所有属性强化加成(int(13))

    # endregion
