##宠物属性部分

宠物列表 = [None] * 7

class 宠物7():
    名称 = '(21)至尊·火神的化身'
    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 160
        属性.体力 += 160
        属性.精神 += 160
        属性.技能等级加成('所有',1,80,1)
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +160<br>'
        temp += '体力 +160<br>'
        temp += '精神 +160<br>'
        temp += 'Lv1-80 技能等级+1<br>'
        return temp

class 宠物6():
    名称 = '(21)普通·骑士/精灵使'
    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 150
        属性.体力 += 150
        属性.精神 += 150
        属性.技能等级加成('所有',1,80,1)
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +150<br>'
        temp += '体力 +150<br>'
        temp += '精神 +150<br>'
        temp += 'Lv1-80 技能等级+1<br>'
        return temp

class 宠物5():
    名称 = '(20)至尊·暴风圣女'
    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 150
        属性.体力 += 150
        属性.精神 += 150
        属性.技能等级加成('所有',1,50,1)
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +150<br>'
        temp += '体力 +150<br>'
        temp += '精神 +150<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        return temp

class 宠物4():
    名称 = '(19)至尊·神迹·莱恩'
    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 120
        属性.体力 += 120
        属性.精神 += 120
        属性.技能等级加成('所有',1,50,1)
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +120<br>'
        temp += '体力 +120<br>'
        temp += '精神 +120<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        return temp
class 宠物3():
    名称 = '(20)普通·神官'
    def 城镇属性_BUFF(self, 属性):
        属性.智力 += 140
        属性.体力 += 140
        属性.精神 += 140
        属性.技能等级加成('所有',1,50,1)
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +140<br>'
        temp += '体力 +140<br>'
        temp += '精神 +140<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        return temp

class 宠物2():
    名称 = '(19)普通·莱恩'
    def 城镇属性_BUFF(self, 属性):
       属性.智力 += 120
       属性.体力 += 120
       属性.精神 += 120
       属性.技能等级加成('所有',1,50,1)
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +120<br>'
        temp += '体力 +120<br>'
        temp += '精神 +120<br>'
        temp += 'Lv1-50 技能等级+1<br>'
        return temp

class 宠物1():
    名称 = '(15)迷你战争领主-SSS型'
    def 城镇属性_BUFF(self, 属性):
       属性.智力 += 10
       属性.体力 += 10
       属性.精神 += 10
       属性.技能等级加成('所有',1,50,2)
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += '智力 +10<br>'
        temp += '体力 +10<br>'
        temp += '精神 +10<br>'
        temp += 'Lv1-50 技能等级+2<br>'
        return temp

class 宠物0():
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
