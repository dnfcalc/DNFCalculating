class 装备:
    名称 = ''
    模式 = 0
    图片ID = ''
    所属套装 = ''
    等级 = 0
    品质 = ''
    部位 = ''
    类型 = ''
    力量 = 0
    智力 = 0
    体力 = 0
    精神 = 0
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0
    def 城镇属性(self, 属性):
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 其它属性_BUFF(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        return temp
    def 装备描述_BUFF(self, 属性):
        temp = ''
        return temp
    def BUFF属性(self, 属性):
        pass
    def 图片ID(self):
        if self.图片ID == '':
            return self.__class__.__name__.replace('装备','')
        else:
            return self.图片ID

class 改造产物(装备):
    模式 = 1
    所属套装 = '智慧产物'
    等级 = 100
    品质 = '史诗'
    力量 = 0
    智力 = 0
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0
    关联套装 = ''
    def 基础属性(self, 属性):
        pass
    def 改造属性(self, 属性, x):
        pass
    def 城镇属性(self, 属性):
        for i in 属性.装备栏:
            if 装备列表[装备序号[i]].所属套装 in self.关联套装:
                属性.力量 += 100
                属性.智力 += 100
        self.基础属性(属性)
        pass
    def 进图属性(self, 属性):
        if self.关联套装 in 属性.套装栏:
            self.改造属性(属性, 属性.获取改造(self.部位))
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        return temp

class 飘零之花武器(装备):
    模式 = 0
    所属套装 = '智慧产物'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    物攻成长 = 0
    魔攻成长 = 0
    独立成长 = 115
    力智成长 = 20
    def 城镇属性(self, 属性):
        改造等级 = 属性.获取改造(self.部位)
        属性.技能攻击力加成(0.35)
        属性.附加伤害加成(0.50)
        属性.百分比力智加成(0.20)
        属性.物理攻击力 += self.物攻成长 * 改造等级
        属性.魔法攻击力 += self.魔攻成长 * 改造等级
        属性.独立攻击力 += self.独立成长 * 改造等级
        属性.力量 += self.力智成长 * 改造等级
        属性.智力 += self.力智成长 * 改造等级
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        if self.力量 != 0:
            temp += '力量 +' + str(self.力量) + '<br>'
        if self.智力 != 0:
            temp += '智力 +' + str(self.智力) + '<br>'
        temp += '物理攻击力 +' + str(self.物理攻击力) + '<br>'
        temp += '魔法攻击力 +' + str(self.魔法攻击力) + '<br>'
        temp += '独立攻击力 +' + str(self.独立攻击力) + '<br>'
        改造等级 = 属性.获取改造(self.部位)
        if 改造等级 >= 5:
            temp += '技能攻击力 +35%<br>'
            temp += '附加伤害 +50%<br>'
            temp += '百分比力智 +20%<br>'
        if 改造等级 > 0:
            temp += '<font color="#FF8200">改造属性(+' + str(改造等级) + ')：</font><br>'
            temp += '力量 +' + str(self.力智成长 * 改造等级) + '<br>'
            temp += '智力 +' + str(self.力智成长 * 改造等级) + '<br>'
            temp += '物理攻击力 +' + str(self.物攻成长 * 改造等级) + '<br>'
            temp += '魔法攻击力 +' + str(self.魔攻成长 * 改造等级) + '<br>'
            temp += '独立攻击力 +' + str(self.独立成长 * 改造等级) + '<br>'
        return temp        