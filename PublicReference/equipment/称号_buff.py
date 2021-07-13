# 称号属性部分

称号列表 = [None] * 7


class 称号6():
    名称 = '(21)五一·LV15-35(所有)'

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 80
        属性.体力 += 80
        属性.精神 += 80
        属性.技能等级加成('所有', 15, 35, 1)

    def 触发属性(self, 属性):
        pass

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +80<br>'
        temp += '体力 +80<br>'
        temp += '精神 +80<br>'
        temp += 'Lv15-35 技能等级 +1<br>'
        return temp


class 称号5():
    名称 = '(20)五一·LV15-35(主动)'

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 80
        属性.体力 += 80
        属性.精神 += 80
        属性.技能等级加成('主动', 15, 35, 1)

    def 触发属性(self, 属性):
        pass

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +80<br>'
        temp += '体力 +80<br>'
        temp += '精神 +80<br>'
        temp += 'Lv15-35 主动技能等级 +1<br>'
        return temp


class 称号4():
    名称 = '(20)五一·LV15-20'

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 80
        属性.体力 += 80
        属性.精神 += 80
        属性.技能等级加成('所有', 15, 20, 1)

    def 触发属性(self, 属性):
        pass

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +80<br>'
        temp += '体力 +80<br>'
        temp += '精神 +80<br>'
        temp += 'Lv15-20 技能等级 +1<br>'
        return temp


class 称号3():
    名称 = '(20)五一·LV20-25'

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 80
        属性.体力 += 80
        属性.精神 += 80
        属性.技能等级加成('所有', 20, 25, 1)

    def 触发属性(self, 属性):
        pass

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +80<br>'
        temp += '体力 +80<br>'
        temp += '精神 +80<br>'
        temp += 'Lv20-25 技能等级 +1<br>'
        return temp


class 称号2():
    名称 = '(20)五一·LV25-30'

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 80
        属性.体力 += 80
        属性.精神 += 80
        属性.技能等级加成('所有', 25, 30, 1)

    def 触发属性(self, 属性):
        pass

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +80<br>'
        temp += '体力 +80<br>'
        temp += '精神 +80<br>'
        temp += 'Lv25-30 技能等级 +1<br>'
        return temp


class 称号1():
    名称 = '(20)五一·LV30-35'

    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 80
        属性.体力 += 80
        属性.精神 += 80
        属性.技能等级加成('所有', 30, 35, 1)

    def 触发属性(self, 属性):
        pass

    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +80<br>'
        temp += '体力 +80<br>'
        temp += '精神 +80<br>'
        temp += 'Lv30-35 技能等级 +1<br>'
        return temp


class 称号0():
    名称 = '无'

    def 城镇属性_BUFF(self, 属性):
        pass

    def 触发属性(self, 属性):
        pass

    def 装备描述_BUFF(self, 属性):
        temp = ''
        return temp


for i in range(len(称号列表)):
    exec('称号列表[{}] = 称号{}()'.format(len(称号列表) - i - 1, i))

称号序号 = dict()
for i in range(len(称号列表)):
    称号序号[称号列表[i].名称] = i
