from PublicReference.equipment.描述 import *
from PublicReference.equipment.base_item import Item
# 称号属性部分

称号列表 = [None] * 7


class 称号6(Item):
    显示名称 = '(21)骑士之誓(Lv15-35 所有技能Lv+1)'
    名称 = '骑士之誓'

    def 城镇属性_BUFF(self, 属性):
        四维固定加成(属性, 80)
        属性.技能等级加成('所有', 15, 35, 1)

    def 装备描述_BUFF(self, 属性):
        temp = 四维固定加成(属性, 80)
        temp += 'Lv15-35 技能等级 +1<br>'
        return temp


class 称号5(Item):
    显示名称 = '(20)权御九界(Lv15-35 主动技能Lv+1)'
    名称 = '权御九界'

    def 城镇属性_BUFF(self, 属性):
        四维固定加成(属性, 80)
        属性.技能等级加成('主动', 15, 35, 1)

    def 装备描述_BUFF(self, 属性):
        temp = 四维固定加成(属性, 80)
        temp += 'Lv15-35 主动技能等级 +1<br>'
        return temp


class 称号4(Item):
    显示名称 = '(20)无畏战斗者(LV15-20 所有技能Lv+1)'
    名称 = '无畏战斗者'

    def 城镇属性_BUFF(self, 属性):
        四维固定加成(属性, 80)
        属性.技能等级加成('所有', 15, 20, 1)

    def 装备描述_BUFF(self, 属性):
        temp = 四维固定加成(属性, 80)
        temp += 'Lv15-20 技能等级 +1<br>'
        return temp


class 称号3(Item):
    显示名称 = '(20)无畏战争者(Lv20-25 所有技能Lv+1)'
    名称 = '无畏战争者'

    def 城镇属性_BUFF(self, 属性):
        四维固定加成(属性, 80)
        属性.技能等级加成('所有', 20, 25, 1)

    def 装备描述_BUFF(self, 属性):
        temp = 四维固定加成(属性, 80)
        temp += 'Lv20-25 技能等级 +1<br>'
        return temp


class 称号2(Item):
    显示名称 = '(20)无畏死亡者(LV25-30 所有技能Lv+1)'
    名称 = '无畏死亡者'

    def 城镇属性_BUFF(self, 属性):
        四维固定加成(属性, 80)
        属性.技能等级加成('所有', 25, 30, 1)

    def 装备描述_BUFF(self, 属性):
        temp = 四维固定加成(属性, 80)
        temp += 'Lv25-30 技能等级 +1<br>'
        return temp


class 称号1(Item):
    显示名称 = '(20)无畏牺牲者(Lv30-35 所有技能Lv+1)'
    名称 = '无畏牺牲者'

    def 城镇属性_BUFF(self, 属性):
        四维固定加成(属性, 80)
        属性.技能等级加成('所有', 30, 35, 1)

    def 装备描述_BUFF(self, 属性):
        temp = 四维固定加成(属性, 80)
        temp += 'Lv30-35 技能等级 +1<br>'
        return temp


class 称号0(Item):
    pass


for i in range(len(称号列表)):
    exec('称号列表[{}] = 称号{}()'.format(len(称号列表) - i - 1, i))

称号序号 = dict()
for i in range(len(称号列表)):
    称号序号[称号列表[i].名称] = i
