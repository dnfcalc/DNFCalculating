##希洛克词条融合属性部分

class 词条属性():
    描述 = ''
    def 加成属性(self, 属性, x):
        pass

class 词条属性0(词条属性):
    描述 = '力智'
    def 加成属性(self, 属性, x):
        属性.百分比力智加成(x)
        pass

class 词条属性1(词条属性):
    描述 = '三攻'
    def 加成属性(self, 属性, x):
        属性.百分比三攻加成(x)
        pass

class 词条属性2(词条属性):
    描述 = '黄字'
    def 加成属性(self, 属性, x):
        属性.伤害增加加成(x)
        pass

class 词条属性3(词条属性):
    描述 = '白字'
    def 加成属性(self, 属性, x):
        属性.附加伤害加成(x)
        pass

class 词条属性4(词条属性):
    描述 = '爆伤'
    def 加成属性(self, 属性, x):
        属性.暴击伤害加成(x)
        pass

class 词条属性5(词条属性):
    描述 = '终伤'
    def 加成属性(self, 属性, x):
        属性.最终伤害加成(x)
        pass

class 词条属性6(词条属性):
    描述 = '觉醒Lv'
    def 加成属性(self, 属性, x):
        属性.技能等级加成("所有",50,50,x)
        属性.技能等级加成("所有",85,85,x)
        属性.技能等级加成("所有",100,100,x)
        pass

词条属性列表 = []

for i in range(6):
    exec('词条属性列表.append(词条属性{}())'.format(i))

黑鸦武器属性列表 = []
for i in range(7):
    exec('黑鸦武器属性列表.append(词条属性{}())'.format(i))

