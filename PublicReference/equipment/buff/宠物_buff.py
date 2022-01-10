# 宠物属性部分
from PublicReference.equipment.base_item import Item

宠物列表 = [None] * 10


class 宠物9(Item):
    显示名称 = '(22)至尊·超越时空·厄俄斯/赫斯'
    名称 = "超越时空·厄俄斯/赫斯"

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 160
        属性.体力 += 160
        属性.精神 += 160
        属性.技能等级加成('所有', 1, 95, 1)

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +160<br>'
        temp += '体力 +160<br>'
        temp += '精神 +160<br>'
        temp += 'Lv1-95 技能等级+1<br>'
        return temp


class 宠物8(Item):
    显示名称 = '(22)普通·次元探险家·厄俄斯/赫斯'
    名称 = "次元探险家·厄俄斯/赫斯"

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 150
        属性.体力 += 150
        属性.精神 += 150
        属性.技能等级加成('所有', 1, 95, 1)

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +150<br>'
        temp += '体力 +150<br>'
        temp += '精神 +150<br>'
        temp += 'Lv1-95 技能等级+1<br>'
        return temp


class 宠物7(Item):
    显示名称 = '(21)至尊·火神的化身'
    名称 = "火神的化身"

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 160
        属性.体力 += 160
        属性.精神 += 160
        属性.技能等级加成('所有', 1, 80, 1)

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +160<br>'
        temp += '体力 +160<br>'
        temp += '精神 +160<br>'
        temp += 'Lv1-80 技能等级+1<br>'
        return temp


class 宠物6(Item):
    显示名称 = '(21)普通·骑士/精灵使'
    名称 = "骑士/精灵使"

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 150
        属性.体力 += 150
        属性.精神 += 150
        属性.技能等级加成('所有', 1, 80, 1)

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +150<br>'
        temp += '体力 +150<br>'
        temp += '精神 +150<br>'
        temp += 'Lv1-80 技能等级+1<br>'
        return temp


class 宠物5(Item):
    显示名称 = '(20)至尊·暴风圣女'
    名称 = "暴风圣女"

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 150
        属性.体力 += 150
        属性.精神 += 150
        属性.技能等级加成('所有', 1, 50, 1)

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +150<br>'
        temp += '体力 +150<br>'
        temp += '精神 +150<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        return temp


class 宠物4(Item):
    显示名称 = '(19)至尊·神迹·莱恩'
    名称 = '神迹·莱恩'

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 120
        属性.体力 += 120
        属性.精神 += 120
        属性.技能等级加成('所有', 1, 50, 1)

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +120<br>'
        temp += '体力 +120<br>'
        temp += '精神 +120<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        return temp


class 宠物3(Item):
    显示名称 = '(20)普通·神官'
    名称 = '神官格洛丽亚'

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 140
        属性.体力 += 140
        属性.精神 += 140
        属性.技能等级加成('所有', 1, 50, 1)

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +140<br>'
        temp += '体力 +140<br>'
        temp += '精神 +140<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        return temp


class 宠物2(Item):
    显示名称 = '(19)普通·莱恩'
    名称 = '骑士莱恩'

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 120
        属性.体力 += 120
        属性.精神 += 120
        属性.技能等级加成('所有', 1, 50, 1)

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +120<br>'
        temp += '体力 +120<br>'
        temp += '精神 +120<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        return temp


class 宠物1(Item):
    显示名称 = '(15)迷你战争领主-SSS型'
    名称 = '迷你战争领主-SSS型'

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 10
        属性.体力 += 10
        属性.精神 += 10
        属性.技能等级加成('所有', 1, 50, 2)

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +10<br>'
        temp += '体力 +10<br>'
        temp += '精神 +10<br>'
        temp += 'Lv1-50 技能等级+2<br>'
        return temp


class 宠物0(Item):
    显示名称 = '无'
    名称 = '无'

    def 城镇属性_BUFF(self, 属性):
        pass

    def 装备描述_BUFF(self, 属性):
        temp = ''
        return temp


for i in range(len(宠物列表)):
    exec('宠物列表[{}] = 宠物{}()'.format(len(宠物列表) - i - 1, i))

宠物序号 = dict()
for i in range(len(宠物列表)):
    宠物序号[宠物列表[i].名称] = i
