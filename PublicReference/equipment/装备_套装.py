class 套装:
    def 城镇属性(self, 属性):
        pass;
    def 城镇属性_BUFF(self, 属性):
        pass;
    def 进图属性(self, 属性):
        pass;
    def 进图属性_BUFF(self, 属性):
        pass;
    def 其它属性(self, 属性):
        pass;
    def 其它属性_BUFF(self, 属性):
        pass;
    def 装备描述(self, 属性):
        temp = ''
        return temp
    def 装备描述_BUFF(self, 属性):
        temp = ''
        return temp
    def BUFF属性(self, 属性):
        pass;
#region  防具套装
class 套装效果0(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.最终伤害加成(0.14)
        属性.技能攻击力加成(0.14)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '最终伤害 +14%<br>'
        temp += '技能攻击力 +14%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 100
        属性.转职被动智力 += 100
        属性.BUFFLv += 2
        属性.一觉Lv += 1
        属性.一觉力智 += 135
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += 'Lv30 技能等级 +2<br>'
        temp += 'Lv50 技能等级 +1<br>'
        if 属性.角色 == '圣职者(男)':
            temp += '[天启之珠]力量、智力 +135<br>'
            temp += '[守护恩赐]体力、精神 +100<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[圣光天启] 力量、智力 +135<br>'
            temp += '[启示圣歌] 智力 +100<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[开幕！人偶剧场]力量、智力 +135<br>'
            temp += '[人偶操纵者]智力 +100<br>'
        return temp

class 套装效果1(套装):
    名称 = '死亡阴影'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.14)
        属性.所有属性强化加成(55)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.10
        属性.释放速度 += 0.15
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +14%<br>'
        temp += '所有属性强化 +55<br>'
        temp += '攻击速度 +10%<br>'
        temp += '释放速度 +15%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 190
        属性.转职被动智力 += 190
        属性.一觉力智 += 220
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[天启之珠]力量、智力 +220<br>'
            temp += '[守护恩赐]体力、精神 +190<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[圣光天启]力量、智力 +220<br>'
            temp += '[启示圣歌]智力 +190<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[开幕！人偶剧场]力量、智力 +220<br>'
            temp += '[人偶操纵者]智力 +190<br>'
        return temp

class 套装效果2(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.22)
        if 属性.贫瘠沙漠的遗产 != 0:
            属性.技能攻击力加成(0 + 属性.技能栏空位 / 100)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +22%<br>'
        if 属性.贫瘠沙漠的遗产 != 0:
            temp += '技能攻击力 +' +str(属性.技能栏空位) +'%<br>'
        return temp  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.技能等级加成('所有', 1, 30, 1)
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉力智 += 175
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[天启之珠]力量、智力 +175<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[圣光天启]力量、智力 +175<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +175<br>'
        temp += 'Lv1-30 技能等级 +1<br>'
        return temp

class 套装效果3(套装):
    名称 = '噩梦：地狱之路'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.16)
        属性.最终伤害加成(0.06)
        属性.技能攻击力加成(0.06)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +16%<br>'
        temp += '最终伤害 +6%<br>'
        temp += '技能攻击力 +6%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉力智 += 100
        属性.一觉力智per *= 1.04
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[天启之珠]力量、智力 +100<br>'
            temp += '[天启之珠]力量、智力 +4%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[圣光天启]力量、智力 +100<br>'
            temp += '[圣光天启]力量、智力 +4%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +100<br>'
            temp += '[开幕！人偶剧场]力量、智力 +4%<br>'
        return temp

class 套装效果4(套装):
    名称 = '永恒不息之路'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.32)
        属性.技能倍率加成(60, 0.20)
        属性.技能冷却缩减(60, 60, -0.30)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +32%<br>'
        temp += 'Lv60技能：<br>攻击力 +20% CD +30%<br>'
        return temp       
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.12
        属性.BUFF智力per *= 1.12
        属性.一觉力智 += 175
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +12%<br>'
            temp += '[天启之珠]力量、智力 +175<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +12%<br>'
            temp += '[圣光天启]力量、智力 +175<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +12%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +175<br>'
        return temp

class 套装效果5(套装):
    名称 = '天堂舞姬'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.17)
        属性.最终伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +17%<br>'
        temp += '最终伤害 +10%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 105
        属性.转职被动智力 += 105
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.12
        属性.BUFF智力per *= 1.12
        属性.一觉力智 += 135
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +12%<br>'
            temp += '[天启之珠]力量、智力 +135<br>'
            temp += '[守护恩赐]体力、精神 +105<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +12%<br>'
            temp += '[圣光天启]力量、智力 +135<br>'
            temp += '[启示圣歌]智力 +105<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +12%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +135<br>'
            temp += '[人偶操纵者]智力 +105<br>'
        return temp

class 套装效果6(套装):
    名称 = '皇家裁决者宣言'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.16)
        属性.所有属性强化加成(52)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.命中率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +16%<br>'
        temp += '所有属性强化 +52<br>'
        temp += '命中率 +5%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFF力量per *= 1.12
        属性.BUFF智力per *= 1.12
        属性.一觉力智 += 220
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +12%<br>'
            temp += '[天启之珠]力量、智力 +220<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +12%<br>'
            temp += '[圣光天启]力量、智力 +220<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +12%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +220<br>'
        return temp

class 套装效果7(套装):
    名称 = '炙炎之盛宴'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.18)
        属性.所有属性强化加成(40)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +18%<br>'
        temp += '所有属性强化 +40<br>'
        return temp  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 100
        属性.转职被动智力 += 100
        属性.BUFFLv += 1
        属性.一觉力智 += 175
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]力量、智力 +175<br>'
            temp += '[守护恩赐]体力、精神 +100<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]力量、智力 +175<br>'
            temp += '[启示圣歌]智力 +100<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]力量、智力 +175<br>'
            temp += '[人偶操纵者]智力 +100<br>'
        return temp

class 套装效果8(套装):
    名称 = '传奇铁匠-封神'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.14)
        属性.最终伤害加成(0.14)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +14%<br>'
        temp += '最终伤害 +14%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 80
        属性.转职被动智力 += 80
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉力智 += 120
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[天启之珠]力量、智力 +120<br>'
            temp += '[守护恩赐]体力、精神 +80<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[圣光天启]力量、智力 +120<br>'
            temp += '[启示圣歌]智力 +80<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +120<br>'
            temp += '[人偶操纵者]智力 +80<br>'
        return temp

class 套装效果9(套装):
    名称 = '命运歧路'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.15)
        属性.附加伤害加成(0.13)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +15%<br>'
        temp += '附加伤害 +13%<br>'
        return temp   
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉力智 += 135
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[天启之珠]力量、智力 +135<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[圣光天启]力量、智力 +135<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +135<br>'
        return temp

class 套装效果10(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.08)
        属性.伤害增加加成(0.21)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.回避率 += 0.06
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +8%<br>'
        temp += '伤害增加 +21%<br>'
        temp += '回避率 +6%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 3
        属性.一觉力智 += 230
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +3<br>'
            temp += '[天启之珠]力量、智力 +230<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +3<br>'
            temp += '[圣光天启]力量、智力 +230<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +3<br>'
            temp += '[开幕！人偶剧场]力量、智力 +230<br>'
        return temp

class 套装效果11(套装):
    名称 = '龙血玄黄'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.23)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.1
        属性.魔法暴击率 += 0.1
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +23%<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉Lv += 1
        属性.一觉力智 += 100
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[天启之珠]力量、智力 +100<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[圣光天启]力量、智力 +100<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +100<br>'
        return temp

class 套装效果12(套装):
    名称 = '擎天战甲'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.14)
        属性.暴击伤害加成(0.14)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +14%<br>'
        temp += '暴击伤害 +14%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.06
        属性.BUFF智力per *= 1.06
        属性.一觉力智 += 150
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +6%<br>'
            temp += '[天启之珠]力量、智力 +150<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +6%<br>'
            temp += '[圣光天启]力量、智力 +150<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +6%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +150<br>'
        return temp

class 套装效果13(套装):
    名称 = '荆棘漫天'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.12)
        属性.暴击伤害加成(0.11)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.10
        属性.魔法暴击率 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +12%<br>'
        temp += '暴击伤害 +11%<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.12
        属性.BUFF智力per *= 1.12
        属性.一觉力智 += 175
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +12%<br>'
            temp += '[天启之珠]力量、智力 +175<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +12%<br>'
            temp += '[圣光天启]力量、智力 +175<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +12%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +175<br>'
        return temp

class 套装效果14(套装):
    名称 = '大自然的呼吸'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.16)
        属性.暴击伤害加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +16%<br>'
        temp += '暴击伤害 +15%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 145
        属性.转职被动智力 += 145
        属性.BUFF力量per *= 1.15
        属性.BUFF智力per *= 1.15
        属性.一觉力智 += 60
        属性.一觉力智per *= 1.05
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +15%<br>'
            temp += '[天启之珠]力量、智力 +60<br>'
            temp += '[天启之珠]力量、智力 +5%<br>'
            temp += '[守护恩赐]体力、精神 +145<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +15%<br>'
            temp += '[圣光天启]力量、智力 +60<br>'
            temp += '[圣光天启]力量、智力 +5%<br>'
            temp += '[启示圣歌]智力 +145<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +15%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +60<br>'
            temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
            temp += '[人偶操纵者]智力 +145<br>'
        return temp

class 套装效果15(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.22)
        属性.暴击伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +22%<br>'
        temp += '暴击伤害 +10%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 50
        属性.转职被动智力 += 50
        属性.BUFF力量per *= 1.24
        属性.BUFF智力per *= 1.24
        属性.一觉力智 += 153
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +24%<br>'
            temp += '[天启之珠]力量、智力 +153<br>'
            temp += '[守护恩赐]体力、精神 +50<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +24%<br>'
            temp += '[圣光天启]力量、智力 +153<br>'
            temp += '[启示圣歌]智力 +50<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +24%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +153<br>'
            temp += '[人偶操纵者]智力 +50<br>'
        return temp

class 套装效果16(套装):
    名称 = '死亡阴影'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.最终伤害加成(0.14)
        属性.技能攻击力加成(0.16)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '最终伤害 +14%<br>'
        temp += '技能攻击力 +16%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 165
        属性.转职被动智力 += 165
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.25
        属性.BUFF智力per *= 1.25
        属性.一觉力智 += 130
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +25%<br>'
            temp += '[天启之珠]力量、智力 +130<br>'
            temp += '[守护恩赐]体力、精神 +165<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +25%<br>'
            temp += '[圣光天启]力量、智力 +130<br>'
            temp += '[启示圣歌]智力 +165<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +25%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +130<br>'
            temp += '[人偶操纵者]智力 +165<br>'
        return temp

class 套装效果17(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.技能攻击力加成(0.15)
        属性.所有属性强化加成(60)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '技能攻击力 +15%<br>'
        temp += '所有属性强化 +60<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 113
        属性.转职被动智力 += 113
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.1
        属性.BUFF智力per *= 1.1
        属性.一觉被动Lv += 2
        属性.一觉力智 += 150
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += 'Lv30-48 技能等级 +2<br>'
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +10%<br>'
            temp += '[天启之珠]力量、智力 +150<br>'
            temp += '[守护恩赐]体力、精神 +113<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +10%<br>'
            temp += '[圣光天启]力量、智力 +150<br>'
            temp += '[启示圣歌]智力 +113<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +10%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +150<br>'
            temp += '[人偶操纵者]智力 +113<br>'
        return temp

class 套装效果18(套装):
    名称 = '噩梦：地狱之路'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.所有属性强化加成(66)
        属性.技能等级加成('所有', 1, 85, 1) 
        属性.技能等级加成('所有', 100, 100, 1) 
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '所有属性强化 +66<br>'
        temp += 'Lv1-85 技能等级+1<br>'
        temp += 'Lv100  技能等级+1<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        属性.技能等级加成('所有', 1, 85, 1)
        属性.技能等级加成('所有', 100, 100, 1)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 110
        属性.转职被动智力 += 110
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉力智 += 99
        属性.一觉力智per *= 1.04
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[天启之珠]力量、智力 +99<br>'
            temp += '[天启之珠]力量、智力 +4%<br>'
            temp += '[守护恩赐]体力、精神 +110<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[圣光天启]力量、智力 +99<br>'
            temp += '[圣光天启]力量、智力 +4%<br>'
            temp += '[启示圣歌]智力 +110<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +99<br>'
            temp += '[开幕！人偶剧场]力量、智力 +4%<br>'
            temp += '[人偶操纵者]智力 +110<br>'
        temp += 'Lv1-85 技能等级 +1<br>'
        temp += 'Lv100 技能等级 +1<br>'
        return temp

class 套装效果19(套装):
    名称 = '永恒不息之路'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.最终伤害加成(0.32)
        属性.技能倍率加成(70, 0.20)
        属性.技能冷却缩减(70, 70, -0.30)    
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '最终伤害 +32%<br>'
        temp += 'Lv70技能：<br>攻击力 +20% CD +30%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 3
        属性.BUFF力量per *= 1.15
        属性.BUFF智力per *= 1.15
        属性.一觉力智 += 130
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +3<br>'
            temp += '[荣誉祝福]力量、智力 +15%<br>'
            temp += '[天启之珠]力量、智力 +130<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +3<br>'
            temp += '[勇气祝福]力量、智力 +15%<br>'
            temp += '[圣光天启]力量、智力 +130<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +3<br>'
            temp += '[禁忌诅咒]力量、智力 +15%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +130<br>'
        return temp

class 套装效果20(套装):
    名称 = '天堂舞姬'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.11)
        属性.伤害增加加成(0.16)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.10
        属性.移动速度 += 0.10
        属性.释放速度 += 0.15
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +11%<br>'
        temp += '伤害增加 +16%<br>'
        temp += '攻击速度 +10%<br>'
        temp += '移动速度 +10%<br>'
        temp += '释放速度 +15%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 145
        属性.转职被动智力 += 145
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉力智 += 192
        属性.一觉力智per *= 1.05
    def 装备描述(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[圣光天启]力量、智力 +5%<br>'
            temp += '[圣光天启]力量、智力 +192<br>'
            temp += '[守护恩赐]体力、精神 +145<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[天启之珠]力量、智力 +5%<br>'
            temp += '[天启之珠]力量、智力 +192<br>'
            temp += '[启示圣歌]智力 +145<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +192<br>'
            temp += '[人偶操纵者]智力 +145<br>'
        return temp

class 套装效果21(套装):
    名称 = '皇家裁决者宣言'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.15)
        属性.所有属性强化加成(62)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.05
        属性.移动速度 += 0.05
        属性.释放速度 += 0.08
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +15%<br>'
        temp += '所有属性强化 +62<br>'
        temp += '攻击速度 +5%<br>'
        temp += '移动速度 +5%<br>'
        temp += '释放速度 +8%<br>'
        return temp  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 280
        属性.转职被动智力 += 280
        属性.BUFFLv += 3
        属性.BUFF力量per *= 1.2
        属性.BUFF智力per *= 1.2
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +3<br>'
            temp += '[荣誉祝福]力量、智力 +20%<br>'
            temp += '[守护恩赐]体力、精神 +280<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +3<br>'
            temp += '[勇气祝福]力量、智力 +20%<br>'
            temp += '[启示圣歌]智力 +280<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +3<br>'
            temp += '[禁忌诅咒]力量、智力 +20%<br>'
            temp += '[人偶操纵者]智力 +280<br>'
        return temp

class 套装效果22(套装):
    名称 = '炙炎之盛宴'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.10)
        属性.技能攻击力加成(0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.05
        属性.魔法暴击率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +10%<br>'
        temp += '技能攻击力 +20%<br>'
        temp += '物理暴击率 +5%<br>'
        temp += '魔法暴击率 +5%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.技能等级加成('所有', 1, 48, 2)
        属性.BUFF力量per *= 1.25
        属性.BUFF智力per *= 1.25
        属性.一觉力智 += 100
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +25%<br>'
            temp += '[天启之珠]力量、智力 +100<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +25%<br>'
            temp += '[圣光天启]力量、智力 +100<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +25%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +100<br>'
        temp += 'Lv1-48 技能等级 +2<br>'
        return temp

class 套装效果23(套装):
    名称 = '传奇铁匠-封神'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.21)
        if 属性.装备检查('天堂之翼'):
            属性.技能冷却缩减(1, 45, 0.30)
            属性.技能冷却缩减(60, 80, 0.30)
        else:
            属性.技能冷却缩减(1, 45, 0.20)
            属性.技能冷却缩减(60, 80, 0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +21%<br>'
        if 属性.装备检查('天堂之翼'):
            temp += 'Lv1-45  技能CD-30%<br>'
            temp += 'Lv60-80 技能CD-30%<br>'
        else:
            temp += 'Lv1-45  技能CD-20%<br>'
            temp += 'Lv60-80 技能CD-20%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 250
        属性.转职被动智力 += 250
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.15
        属性.BUFF智力per *= 1.15
        属性.一觉被动Lv += 2
        属性.一觉Lv += 2
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += 'Lv30-50 技能等级 +2<br>'
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +15%<br>'
            temp += '[守护恩赐]体力、精神 +250<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +15%<br>'
            temp += '[启示圣歌]智力 +250<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +15%<br>'
            temp += '[人偶操纵者]智力 +250<br>'
        return temp

class 套装效果24(套装):
    名称 = '命运歧路'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.12)
        属性.暴击伤害加成(0.17)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.21
        属性.移动速度 += 0.21
        属性.释放速度 += 0.315  
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +12%<br>'
        temp += '暴击伤害 +17%<br>'
        temp += '攻击速度 +21%<br>'
        temp += '移动速度 +21%<br>'
        temp += '释放速度 +31.5%<br>'
        return temp   
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉力智 += 260
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[天启之珠]力量、智力 +260<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[圣光天启]力量、智力 +260<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +260<br>'
        return temp

class 套装效果25(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.08)
        属性.附加伤害加成(0.21)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +8%<br>'
        temp += '附加伤害 +21%<br>'
        return temp 
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 125
        属性.转职被动智力 += 125
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.32
        属性.BUFF智力per *= 1.32
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +32%<br>'
            temp += '[守护恩赐]体力、精神 +125<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +32%<br>'
            temp += '[启示圣歌]智力 +125<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +32%<br>'
            temp += '[人偶操纵者]智力 +125<br>'
        return temp

class 套装效果26(套装):
    名称 = '龙血玄黄'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.24)
        属性.所有属性强化加成(24)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +24%<br>'
        temp += '所有属性强化 +24<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 150
        属性.转职被动智力 += 150
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.09
        属性.BUFF智力per *= 1.09
        属性.一觉力智 += 155
        属性.一觉力智per *= 1.02
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +9%<br>'
            temp += '[天启之珠]力量、智力 +155<br>'
            temp += '[天启之珠]力量、智力 +2%<br>'
            temp += '[守护恩赐]体力、精神 +150<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +9%<br>'
            temp += '[圣光天启]力量、智力 +155<br>'
            temp += '[圣光天启]力量、智力 +2%<br>'
            temp += '[启示圣歌]智力 +150<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +9%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +155<br>'
            temp += '[开幕！人偶剧场]力量、智力 +2%<br>'
            temp += '[人偶操纵者]智力 +150<br>'
        return temp

class 套装效果27(套装):
    名称 = '擎天战甲'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.32)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +32%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 285
        属性.转职被动智力 += 285
        属性.BUFF力量per *= 1.2
        属性.BUFF智力per *= 1.2
        属性.一觉Lv += 2
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[天启之珠]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +20%<br>'
            temp += '[守护恩赐]体力、精神 +285<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[圣光天启]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +20%<br>'
            temp += '[启示圣歌]智力 +285<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[开幕！人偶剧场]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +20%<br>'
            temp += '[人偶操纵者]智力 +285<br>'
        return temp

class 套装效果28(套装):
    名称 = '荆棘漫天'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.25)
        属性.技能冷却缩减(1, 45, 0.15)
        属性.技能冷却缩减(60, 80, 0.15)
        属性.技能冷却缩减(90, 95, 0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +25%<br>'
        temp += 'Lv1-45  技能CD-15%<br>'
        temp += 'Lv60-80 技能CD-15%<br>'
        temp += 'Lv90-95 技能CD-15%<br>'
        return temp 
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 200
        属性.转职被动智力 += 200
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.11
        属性.BUFF智力per *= 1.11
        属性.一觉力智 += 130
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +11%<br>'
            temp += '[天启之珠]力量、智力 +130<br>'
            temp += '[守护恩赐]体力、精神 +200<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +11%<br>'
            temp += '[圣光天启]力量、智力 +130<br>'
            temp += '[启示圣歌]智力 +200<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +11%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +130<br>'
            temp += '[人偶操纵者]智力 +200<br>'
        return temp

class 套装效果29(套装):
    名称 = '大自然的呼吸'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.15)
        属性.技能攻击力加成(0.13)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.05
        属性.移动速度 += 0.05
        属性.释放速度 += 0.1
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +15%<br>'
        temp += '技能攻击力 +13%<br>'
        temp += '攻击速度 +5%<br>'
        temp += '移动速度 +5%<br>'
        temp += '释放速度 +10%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.05
        属性.BUFF智力per *= 1.05
        属性.一觉力智 += 248
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +5%<br>'
            temp += '[天启之珠]力量、智力 +248<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +5%<br>'
            temp += '[圣光天启]力量、智力 +248<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +5%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +248<br>'
        return temp

class 套装效果30(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.13)
        属性.技能等级加成('所有', 1, 85, 2)
        属性.技能等级加成('所有', 100, 100, 2)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.05
        属性.魔法暴击率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +13%<br>'
        temp += 'Lv1-85 技能等级+2<br>'
        temp += 'Lv100  技能等级+2<br>'
        temp += '物理暴击率 +5%<br>'
        temp += '魔法暴击率 +5%<br>'
        return temp   
    def 城镇属性_BUFF(self, 属性):
        属性.技能等级加成('所有', 1, 85, 2)
        属性.技能等级加成('所有', 100, 100, 2)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFF力量per *= 1.06
        属性.BUFF智力per *= 1.06
        属性.一觉力智per *= 1.08
  
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +6%<br>'
            temp += '[天启之珠]力量、智力 +8%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +6%<br>'
            temp += '[圣光天启]力量、智力 +8%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +6%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +8%<br>'
        temp += 'Lv1-85 技能等级 +2<br>'
        temp += 'Lv100 技能等级 +2<br>'
        return temp

class 套装效果31(套装):
    名称 = '死亡阴影'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.技能攻击力加成(0.46)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '技能攻击力 +46%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFF力量per *= 1.12
        属性.BUFF智力per *= 1.12
        属性.一觉力智 += 120
        属性.一觉力智per *= 1.08
        属性.技能等级加成('所有', 1, 30, 1)
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +12%<br>'
            temp += '[天启之珠]力量、智力 +120<br>'
            temp += '[天启之珠]力量、智力 +8%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +12%<br>'
            temp += '[圣光天启]力量、智力 +120<br>'
            temp += '[圣光天启]力量、智力 +8%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +12%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +120<br>'
            temp += '[开幕！人偶剧场]力量、智力 +8%<br>'
        temp += 'Lv1-30 技能等级 +1<br>'
        return temp

class 套装效果32(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.技能攻击力加成(0.42)
        if 属性.贫瘠沙漠的遗产 == 2:
            属性.技能攻击力加成(0.04)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '技能攻击力 +42%<br>'
        if 属性.贫瘠沙漠的遗产 == 2:
            temp += '技能攻击力 +4%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.14
        属性.BUFF智力per *= 1.14
        属性.一觉被动Lv += 2
        属性.一觉Lv += 2
        属性.一觉力智per *= 1.1
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += 'Lv30-50 技能等级 +2<br>'
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +14%<br>'
            temp += '[天启之珠]力量、智力 +10%<br>'   
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +14%<br>'
            temp += '[圣光天启]力量、智力 +10%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +14%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +10%<br>'
        return temp

class 套装效果33(套装):
    名称 = '噩梦：地狱之路'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.技能攻击力加成(0.46)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '技能攻击力 +46%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 80  
        属性.转职被动智力 += 80
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.15
        属性.BUFF智力per *= 1.15
        属性.一觉力智 += 185
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +15%<br>'
            temp += '[天启之珠]力量、智力 +185<br>'
            temp += '[守护恩赐]体力、精神 +80<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +15%<br>'
            temp += '[圣光天启]力量、智力 +185<br>'
            temp += '[启示圣歌]智力 +80<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +15%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +185<br>'
            temp += '[人偶操纵者]智力 +80<br>'
        return temp

class 套装效果34(套装):
    名称 = '永恒不息之路'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.23)
        属性.伤害增加加成(0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.15
        属性.释放速度 += 0.225
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +23%<br>'
        temp += '伤害增加 +20%<br>'
        temp += '攻击速度 +15%<br>'
        temp += '释放速度 +22.5%<br>'
        return temp       
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.04
        属性.BUFF智力per *= 1.04
        属性.一觉力智 += 150
        属性.一觉力智per *= 1.1
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +4%<br>'
            temp += '[天启之珠]力量、智力 +150<br>'
            temp += '[天启之珠]力量、智力 +10%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +4%<br>'
            temp += '[圣光天启]力量、智力 +150<br>'
            temp += '[圣光天启]力量、智力 +10%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +4%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +150<br>'
            temp += '[开幕！人偶剧场]力量、智力 +10%<br>' 
        return temp

class 套装效果35(套装):
    名称 = '天堂舞姬'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.12)
        属性.技能攻击力加成(0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.10
        属性.魔法暴击率 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +12%<br>'
        temp += '技能攻击力 +20%<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        return temp 
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 100   
        属性.转职被动智力 += 100
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.12
        属性.BUFF智力per *= 1.12
        属性.一觉被动Lv += 2
        属性.一觉Lv += 2
        属性.一觉力智per *= 1.05
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += 'Lv30-50 技能等级 +2<br>'
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +12%<br>'
            temp += '[天启之珠]力量、智力 +5%<br>'
            temp += '[守护恩赐]体力、精神 +100<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +12%<br>'
            temp += '[圣光天启]力量、智力 +5%<br>'
            temp += '[启示圣歌]智力 +100<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +12%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
            temp += '[人偶操纵者]智力 +100<br>'
        return temp

class 套装效果36(套装):
    名称 = '皇家裁决者宣言'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.属性附加加成(0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '属性附加 +20%<br>'
        return temp  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.一觉力智 += 180
        属性.一觉力智per *= 1.1
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[天启之珠]力量、智力 +180<br>'
            temp += '[天启之珠]力量、智力 +10%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[圣光天启]力量、智力 +180<br>'
            temp += '[圣光天启]力量、智力 +10%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[开幕！人偶剧场]力量、智力 +180<br>'
            temp += '[开幕！人偶剧场]力量、智力 +10%<br>'
        return temp

class 套装效果37(套装):
    名称 = '炙炎之盛宴'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.最终伤害加成(0.22)
        属性.技能冷却缩减(1, 100, 0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.05
        属性.攻击速度 += 0.05
        属性.移动速度 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '最终伤害 +22%<br>'
        temp += 'Lv1-100 技能CD-15%<br>'
        temp += '攻击速度 +5%<br>'
        temp += '攻击速度 +5%<br>'
        temp += '移动速度 +5%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 300
        属性.转职被动智力 += 300
        属性.BUFFLv += 2
        属性.一觉力智 += 70
        属性.一觉力智per *= 1.08
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[天启之珠]力量、智力 +70<br>'
            temp += '[天启之珠]力量、智力 +8%<br>'
            temp += '[守护恩赐]体力、精神 +300<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[圣光天启]力量、智力 +70<br>'
            temp += '[圣光天启]力量、智力 +8%<br>'
            temp += '[启示圣歌]智力 +300<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[开幕！人偶剧场]力量、智力 +70<br>'
            temp += '[开幕！人偶剧场]力量、智力 +8%<br>'
            temp += '[人偶操纵者]智力 +300<br>'
        return temp      

class 套装效果38(套装):
    名称 = '传奇铁匠-封神'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.27)
        属性.技能冷却缩减(50, 50, 0.30)
        属性.技能冷却缩减(85, 85, 0.30)
        属性.技能冷却缩减(100, 100, 0.17)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.15
        属性.移动速度 += 0.15
        属性.释放速度 += 0.20
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +27%<br>'
        temp += 'Lv50  技能CD-30%<br>'
        temp += 'Lv85  技能CD-30%<br>'
        temp += 'Lv100 技能CD-17%<br>'
        temp += '攻击速度 +15%<br>'
        temp += '移动速度 +15%<br>'
        temp += '释放速度 +20%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.06
        属性.BUFF智力per *= 1.06
        属性.一觉被动Lv += 2
        属性.一觉力智 += 20
        属性.一觉力智per *= 1.07
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += 'Lv30-48 技能等级 +2<br>'
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +6%<br>'
            temp += '[天启之珠]力量、智力 +20<br>'
            temp += '[天启之珠]力量、智力 +7%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +6%<br>'
            temp += '[圣光天启]力量、智力 +20<br>'
            temp += '[圣光天启]力量、智力 +7%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +6%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +20<br>'
            temp += '[开幕！人偶剧场]力量、智力 +7%<br>'
        return temp

class 套装效果39(套装):
    名称 = '命运歧路'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.11)
        属性.最终伤害加成(0.30)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +11%<br>'
        temp += '最终伤害 +30%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):      
        属性.BUFFLv += 3
        属性.BUFF力量per *= 1.17
        属性.BUFF智力per *= 1.17
        属性.一觉力智per *= 1.07
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +3<br>'
            temp += '[荣誉祝福]力量、智力 +17%<br>'
            temp += '[天启之珠]力量、智力 +7%<br>'   
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +3<br>'
            temp += '[勇气祝福]力量、智力 +17%<br>'
            temp += '[圣光天启]力量、智力 +7%<br>'   
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +3<br>'
            temp += '[禁忌诅咒]力量、智力 +17%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +7%<br>'
        return temp

class 套装效果40(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.21)
        属性.技能攻击力加成(0.25)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +21%<br>'
        temp += '技能攻击力 +25%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):  
        属性.BUFFLv += 2
        属性.一觉力智 += 305
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[天启之珠]力量、智力 +305<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[圣光天启]力量、智力 +305<br>' 
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[开幕！人偶剧场]力量、智力 +305<br>'
        return temp

class 套装效果41(套装):
    名称 = '龙血玄黄'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.角色熟练度 == 0 or 属性.装备检查('战无不胜上衣'):
            属性.附加伤害加成(0.41)
        else:
            属性.附加伤害加成(0.40)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.15
        属性.移动速度 += 0.15
        属性.释放速度 += 0.225
        pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.角色熟练度 == 0 or 属性.装备检查('战无不胜上衣'):
            temp += '附加伤害 +41%<br>'
        else:
            temp += '附加伤害 +40%<br>'
        temp += '攻击速度 +15%<br>'
        temp += '移动速度 +15%<br>'
        temp += '释放速度 +22.5%<br>'
        return temp 
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.1
        属性.BUFF智力per *= 1.1
        属性.一觉力智 += 120
        属性.一觉力智per *= 1.06
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +10%<br>'
            temp += '[天启之珠]力量、智力 +120<br>'
            temp += '[天启之珠]力量、智力 +6%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +10%<br>'
            temp += '[圣光天启]力量、智力 +120<br>'
            temp += '[圣光天启]力量、智力 +6%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +10%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +120<br>'
            temp += '[开幕！人偶剧场]力量、智力 +6%<br>'
        return temp

class 套装效果42(套装):
    名称 = '擎天战甲'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.属性附加加成(0.12)
        if 属性.擎天战甲 == 0:
            属性.技能攻击力加成(0.05)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.擎天战甲 == 0:
            属性.攻击速度 += 0.2
            属性.移动速度 += 0.2
            属性.释放速度 += 0.3
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '属性附加 +12%<br>'
        if 属性.擎天战甲 == 0:
            temp += '技能攻击力 +5%<br>'
            temp += '攻击速度 +20%<br>'
            temp += '移动速度 +20%<br>'
            temp += '释放速度 +30%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):  
        属性.BUFF力量per *= 1.07
        属性.BUFF智力per *= 1.07
        属性.一觉力智 += 50
        属性.一觉力智per *= 1.1
        属性.技能等级加成('所有', 1, 50, 2)
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +7%<br>'
            temp += '[天启之珠]力量、智力 +50<br>'
            temp += '[天启之珠]力量、智力 +10%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +7%<br>'
            temp += '[圣光天启]力量、智力 +50<br>'
            temp += '[圣光天启]力量、智力 +10%<br>' 
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +7%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +50<br>'
            temp += '[开幕！人偶剧场]力量、智力 +10%<br>'
        temp += 'Lv1-50 技能等级 +2<br>'
        return temp

class 套装效果43(套装):
    名称 = '荆棘漫天'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.10)
        属性.技能攻击力加成(0.28)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.1
        属性.移动速度 += -0.02
        属性.释放速度 += 0.1
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +10%<br>'
        temp += '技能攻击力 +28%<br>'
        temp += '攻击速度 +10%<br>'
        temp += '移动速度 -2%<br>'
        temp += '释放速度 +10%<br>'
        return temp       
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):   
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.1
        属性.BUFF智力per *= 1.1
        属性.一觉力智 += 150
        属性.一觉力智per *= 1.08
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +10%<br>'
            temp += '[天启之珠]力量、智力 +150<br>'
            temp += '[天启之珠]力量、智力 +8%<br>'    
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +10%<br>'
            temp += '[圣光天启]力量、智力 +150<br>'
            temp += '[圣光天启]力量、智力 +8%<br>'   
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +10%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +150<br>'
            temp += '[开幕！人偶剧场]力量、智力 +8%<br>'  
        return temp

class 套装效果44(套装):
    名称 = '大自然的呼吸'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.最终伤害加成(0.11)
        属性.技能攻击力加成(0.10)
        属性.所有属性强化加成(64)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.10
        属性.魔法暴击率 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '最终伤害 +11%<br>'
        temp += '技能攻击力 +10%<br>'
        temp += '所有属性强化 +64<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.15
        属性.BUFF智力per *= 1.15
        属性.一觉力智 += 130
        属性.一觉力智per *= 1.04
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +15%<br>'
            temp += '[天启之珠]力量、智力 +130<br>'
            temp += '[天启之珠]力量、智力 +4%<br>' 
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +15%<br>'
            temp += '[圣光天启]力量、智力 +130<br>'
            temp += '[圣光天启]力量、智力 +4%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +15%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +130<br>'
            temp += '[开幕！人偶剧场]力量、智力 +4%<br>'
        return temp

#endregion

#region  散搭套装
class 套装效果45(套装):
    名称 = '深渊窥视者'
    件数 = 2
    类型 = '上链左'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.09)
        pass
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 1, 48, 2)
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +9%<br>'
        temp += 'Lv1-48 技能等级+2<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        属性.技能等级加成('所有', 1, 48, 2)
        pass
    def BUFF属性(self, 属性):
        属性.一觉力智per *= 1.02
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[天启之珠]力量、智力 +2%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[圣光天启]力量、智力 +2%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[开幕！人偶剧场]力量、智力 +2%<br>'
        temp += 'Lv1-48 技能等级 +2<br>'
        return temp

class 套装效果46(套装):
    名称 = '圣者的黄昏'
    件数 = 2
    类型 = '上链左'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.11)
        属性.附加伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.移动速度 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +11%<br>'
        temp += '附加伤害 +10%<br>'
        temp += '移动速度 +5%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉Lv += 1
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
        return temp

class 套装效果47(套装):
    名称 = '坎坷命运'
    件数 = 2
    类型 = '上链左'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.14)
        属性.技能攻击力加成(0.09)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.03
        属性.移动速度 += 0.03
        属性.释放速度 += 0.045
        if 属性.装备检查('地狱边缘'):
            属性.攻击速度 -= 0.01
            属性.移动速度 -= 0.01
            属性.释放速度 -= 0.015
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +14%<br>'
        temp += '技能攻击力 +9%<br>'
        temp += '攻击速度 +3%<br>'
        temp += '移动速度 +3%<br>'
        temp += '释放速度 +4.5%<br>'
        if 属性.装备检查('地狱边缘'):
            temp += '攻击速度 -1%<br>'
            temp += '移动速度 -1%<br>'
            temp += '释放速度 -1.5%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.02
        属性.BUFF智力per *= 1.02
        属性.一觉力智 += 45
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +2%<br>'
            temp += '[天启之珠]力量、智力 +45<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +2%<br>'
            temp += '[圣光天启]力量、智力 +45<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +2%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +45<br>'
        return temp

class 套装效果48(套装):
    名称 = '吞噬愤怒'
    件数 = 2
    类型 = '上链左'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.10)
        属性.暴击伤害加成(0.11)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('灭世之怒'):
            属性.攻击速度 += 0.15
            属性.移动速度 += 0.15
            属性.释放速度 += 0.225
        else:
            属性.攻击速度 += 0.10
            属性.移动速度 += 0.10
            属性.释放速度 += 0.15
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +10%<br>'
        temp += '暴击伤害 +11%<br>'
        if 属性.装备检查('灭世之怒'):
            temp += '攻击速度 +15%<br>'
            temp += '移动速度 +15%<br>'
            temp += '释放速度 +22.5%<br>'
        else:
            temp += '攻击速度 +10%<br>'
            temp += '移动速度 +10%<br>'
            temp += '释放速度 +15%<br>'
        return temp   
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.一觉Lv += 1
        属性.一觉力智 += 25
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[天启之珠]力量、智力 +25<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[圣光天启]力量、智力 +25<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]力量、智力 +25<br>'
        return temp

class 套装效果49(套装):
    名称 = '黑魔法探求者'
    件数 = 2
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.12)
        属性.技能攻击力加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +12%<br>'
        temp += '技能攻击力 +10%<br>'
        return temp        
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉力智 += 48
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]力量、智力 +48<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]力量、智力 +48<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]力量、智力 +48<br>'
        return temp

class 套装效果50(套装):
    名称 = '时空旅行者'
    件数 = 2
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.10)
        属性.最终伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +10%<br>'
        temp += '最终伤害 +10%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 36
        属性.转职被动智力 += 46
        属性.BUFFLv += 1
        属性.一觉Lv += 1
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[守护恩赐]体力、精神 +36<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[启示圣歌]智力 +46<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[人偶操纵者]智力 +46<br>'
        return temp

class 套装效果51(套装):
    名称 = '穿透命运的呐喊'
    件数 = 2
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.23)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +23%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉力智 += 25
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]力量、智力 +25<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]力量、智力 +25<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]力量、智力 +25<br>'
        return temp

class 套装效果52(套装):
    名称 = '狂乱追随者'
    件数 = 2
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.18)
        属性.所有属性强化加成(25)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.15
        属性.释放速度 += 0.225
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +18%<br>'
        temp += '所有属性强化 +25<br>'
        temp += '攻击速度 +15%<br>'
        temp += '释放速度 +22.5%<br>'
        return temp  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉力智 += 25
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]力量、智力 +25<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]力量、智力 +25<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]力量、智力 +25<br>'
        return temp

class 套装效果53(套装):
    名称 = '地狱求道者'
    件数 = 2
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.10)
        属性.最终伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +10%<br>'
        temp += '最终伤害 +10%<br>'
        return temp 
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉力智 += 32
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]力量、智力 +32<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]力量、智力 +32<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]力量、智力 +32<br>'
        return temp


class 套装效果54(套装):
    名称 = '次元旅行者'
    件数 = 2
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.22)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.10
        属性.魔法暴击率 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +22%<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 40
        属性.转职被动智力 += 60
        属性.BUFFLv += 1
        属性.一觉力智 += 42
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]力量、智力 +42<br>'
            temp += '[守护恩赐]体力、精神 +40<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]力量、智力 +42<br>'
            temp += '[启示圣歌]智力 +60<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]力量、智力 +42<br>'
            temp += '[人偶操纵者]智力 +60<br>'
        return temp

class 套装效果55(套装):
    名称 = '天命无常'
    件数 = 2
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        属性.伤害增加加成(0.07)
        属性.附加伤害加成(0.08)
        属性.技能攻击力加成(0.05)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.天命无常 == 0:
            if 属性.装备检查('命运反抗者'):
                属性.移动速度 += 0.08
                属性.攻击速度 += 0.08
                属性.释放速度 += 0.12
            else:
                属性.移动速度 += 0.07
                属性.攻击速度 += 0.07
                属性.释放速度 += 0.105
        else:
            属性.移动速度 += 0.02 * 属性.天命无常
            属性.攻击速度 += 0.02 * 属性.天命无常
            属性.释放速度 += 0.03 * 属性.天命无常
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '伤害增加 +7%<br>'
        temp += '附加伤害 +8%<br>'
        temp += '技能攻击力 +5%<br>'
        if 属性.天命无常 == 0:
            if 属性.装备检查('命运反抗者'):
                temp += '移动速度 +8%<br>'
                temp += '攻击速度 +8%<br>'
                temp += '释放速度 +12%<br>'
            else:
                temp += '移动速度 +7%<br>'
                temp += '攻击速度 +7%<br>'
                temp += '释放速度 +10.5%<br>'
        else:
            temp += '移动速度 +' +str(2*属性.天命无常) +'%<br>'
            temp += '攻击速度 +' +str(2*属性.天命无常) +'%<br>'
            temp += '释放速度 +' +str(3*属性.天命无常) +'%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉被动Lv += 1
        属性.一觉力智 += 45
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += 'Lv30-48 技能等级 +1<br>'
        if 属性.角色 == '圣职者(男)':
            temp += '[天启之珠]力量、智力 +45<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[圣光天启]力量、智力 +45<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[开幕！人偶剧场]力量、智力 +45<br>'
        return temp

class 套装效果56(套装):
    名称 = '悲剧的残骸'
    件数 = 2
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        属性.最终伤害加成(0.23)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '最终伤害 +23%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉力智 += 25
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]力量、智力 +25<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]力量、智力 +25<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]力量、智力 +25<br>'
        return temp     

class 套装效果57(套装):
    名称 = '深渊窥视者'
    件数 = 3
    类型 = '上链左'
    def 城镇属性(self, 属性):
        属性.技能攻击力加成(0.13)
        pass
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 60, 80, 2)
        属性.技能等级加成('所有', 50, 50, 1)
        属性.技能等级加成('所有', 85, 85, 1)
        属性.技能等级加成('所有', 100, 100, 1)
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '技能攻击力 +13%<br>'
        temp += 'Lv60-80 技能等级+2<br>'
        temp += 'Lv50  技能等级+1<br>'
        temp += 'Lv85  技能等级+1<br>'
        temp += 'Lv100 技能等级+1<br>'
        return temp       
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        属性.技能等级加成('所有', 60, 80, 2)
        属性.技能等级加成('所有', 50, 50, 1)
        属性.技能等级加成('所有', 85, 85, 1)
        属性.技能等级加成('所有', 100, 100, 1)
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 195
        属性.转职被动智力 += 230
        属性.BUFF力量per *= 1.06
        属性.BUFF智力per *= 1.06
        属性.一觉力智 += 120
        属性.一觉力智per *= 1.03
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +6%<br>'
            temp += '[天启之珠]力量、智力 +120<br>'
            temp += '[天启之珠]力量、智力 +3%<br>'
            temp += '[守护恩赐]体力、精神 +195<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +6%<br>'
            temp += '[圣光天启]力量、智力 +120<br>'
            temp += '[圣光天启]力量、智力 +3%<br>'
            temp += '[启示圣歌]智力 +230<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +6%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +120<br>'
            temp += '[开幕！人偶剧场]力量、智力 +3%<br>'
            temp += '[人偶操纵者]智力 +230<br>'
        temp += 'Lv60-80 技能等级 +2'
        temp += 'Lv50、Lv85、Lv100 技能等级 +1<br>'
        return temp

class 套装效果58(套装):
    名称 = '圣者的黄昏'
    件数 = 3
    类型 = '上链左'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.05)
        属性.技能攻击力加成(0.12)
        属性.所有属性强化加成(32)
        属性.技能冷却缩减(1, 45, 0.10)
        属性.技能冷却缩减(60, 80, 0.10)
        属性.技能冷却缩减(90, 95, 0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.移动速度 += 0.05
        属性.物理暴击率 += 0.15
        属性.魔法暴击率 += 0.15
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +5%<br>'
        temp += '技能攻击力 +12%<br>'
        temp += '所有属性强化 +32<br>'
        temp += 'Lv1-45  技能CD-10%<br>'
        temp += 'Lv60-80 技能CD-10%<br>'
        temp += 'Lv90-95 技能CD-10%<br>'
        temp += '移动速度 +5%<br>'
        temp += '物理暴击率 +15%<br>'
        temp += '魔法暴击率 +15%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 225
        属性.转职被动智力 += 258
        属性.BUFF力量per *= 1.12
        属性.BUFF智力per *= 1.12
        属性.一觉力智 += 125
        属性.一觉力智per *= 1.03
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +12%<br>'
            temp += '[天启之珠]力量、智力 +125<br>'
            temp += '[天启之珠]力量、智力 +3%<br>'
            temp += '[守护恩赐]体力、精神 +225<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +12%<br>'
            temp += '[圣光天启]力量、智力 +125<br>'
            temp += '[圣光天启]力量、智力 +3%<br>'
            temp += '[启示圣歌]智力 +258<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +12%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +125<br>'
            temp += '[开幕！人偶剧场]力量、智力 +3%<br>'
            temp += '[人偶操纵者]智力 +258<br>'
        return temp

class 套装效果59(套装):
    名称 = '坎坷命运'
    件数 = 3
    类型 = '上链左'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.20)
        属性.技能攻击力加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.03
        属性.移动速度 += 0.03
        属性.释放速度 += 0.045
        if 属性.装备检查('地狱边缘'):
            属性.攻击速度 -= 0.01
            属性.移动速度 -= 0.01
            属性.释放速度 -= 0.015
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +20%<br>'
        temp += '技能攻击力 +10%<br>'
        temp += '攻击速度 +3%<br>'
        temp += '移动速度 +3%<br>'
        temp += '释放速度 +4.5%<br>'
        if 属性.装备检查('地狱边缘'):
            temp += '攻击速度 -1%<br>'
            temp += '移动速度 -1%<br>'
            temp += '释放速度 -1.5%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 236
        属性.转职被动智力 += 255
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.06
        属性.BUFF智力per *= 1.06
        属性.一觉Lv += 1
        属性.一觉力智 += 74
        属性.一觉力智per *= 1.05
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +6%<br>'
            temp += '[天启之珠]力量、智力 +74<br>'
            temp += '[天启之珠]力量、智力 +5%<br>'
            temp += '[守护恩赐]体力、精神 +236<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +6%<br>'
            temp += '[圣光天启]力量、智力 +74<br>'
            temp += '[圣光天启]力量、智力 +5%<br>'
            temp += '[启示圣歌]智力 +255<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +6%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +74<br>'
            temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
            temp += '[人偶操纵者]智力 +255<br>'
        return temp

class 套装效果60(套装):
    名称 = '吞噬愤怒'
    件数 = 3
    类型 = '上链左'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.30)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +30%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 236
        属性.转职被动智力 += 255
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.1
        属性.BUFF智力per *= 1.1
        属性.一觉Lv += 1
        属性.一觉力智 += 99
        属性.一觉力智per *= 1.04
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +10%<br>'
            temp += '[天启之珠]力量、智力 +99<br>'
            temp += '[天启之珠]力量、智力 +4%<br>'
            temp += '[守护恩赐]体力、精神 +236<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +10%<br>'
            temp += '[圣光天启]力量、智力 +9<br>'
            temp += '[圣光天启]力量、智力 +4%<br>'
            temp += '[启示圣歌]智力 +255<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +10%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +99<br>'
            temp += '[开幕！人偶剧场]力量、智力 +4%<br>'
            temp += '[人偶操纵者]智力 +255<br>'
        return temp

class 套装效果61(套装):
    名称 = '黑魔法探求者'
    件数 = 3
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        属性.属性附加加成(0.13)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.10
        属性.魔法暴击率 += 0.1
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '属性附加 +13%<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        return temp       
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉Lv += 1
        属性.一觉力智 += 38
        属性.一觉力智per *= 1.06
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[天启之珠]力量、智力 +38<br>'
            temp += '[天启之珠]力量、智力 +6%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[圣光天启]力量、智力 +38<br>'
            temp += '[圣光天启]力量、智力 +6%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +38<br>'
            temp += '[开幕！人偶剧场]力量、智力 +6%<br>'
        return temp

class 套装效果62(套装):
    名称 = '时空旅行者'
    件数 = 3
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.17)
        属性.技能攻击力加成(0.13)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +17%<br>'
        temp += '技能攻击力 +13%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.1
        属性.BUFF智力per *= 1.1
        属性.一觉力智 += 45
        属性.一觉力智per *= 1.05
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +10%<br>'
            temp += '[天启之珠]力量、智力 +45<br>'
            temp += '[天启之珠]力量、智力 +5%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +10%<br>'
            temp += '[圣光天启]力量、智力 +45<br>'
            temp += '[圣光天启]力量、智力 +5%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +10%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +45<br>'
            temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
        return temp

class 套装效果63(套装):
    名称 = '穿透命运的呐喊'
    件数 = 3
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.14)
        属性.技能攻击力加成(0.16)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +14%<br>'
        temp += '技能攻击力 +16%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 76
        属性.转职被动智力 += 68
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.06
        属性.BUFF智力per *= 1.06
        属性.一觉被动Lv += 2
        属性.一觉Lv += 2
        属性.一觉力智per *= 1.04
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += 'Lv30-50 技能等级 +2<br>'
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +6%<br>'
            temp += '[天启之珠]力量、智力 +4%<br>'
            temp += '[守护恩赐]体力、精神 +76<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +6%<br>'
            temp += '[圣光天启]力量、智力 +4%<br>'
            temp += '[启示圣歌]智力 +68<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +6%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +4%<br>'
            temp += '[人偶操纵者]智力 +68<br>'
        return temp

class 套装效果64(套装):
    名称 = '狂乱追随者'
    件数 = 3
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.16)
        属性.技能攻击力加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +16%<br>'
        temp += '技能攻击力 +15%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 36
        属性.转职被动智力 += 38
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.1
        属性.BUFF智力per *= 1.1
        属性.一觉Lv += 1
        属性.一觉力智 += 85
        属性.一觉力智per *= 1.04
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +10%<br>'
            temp += '[天启之珠]力量、智力 +85<br>'
            temp += '[守护恩赐]体力、精神 +36<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +10%<br>'
            temp += '[圣光天启]力量、智力 +85<br>'
            temp += '[启示圣歌]智力 +38<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +10%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +85<br>'
            temp += '[人偶操纵者]智力 +38<br>'
        return temp

class 套装效果65(套装):
    名称 = '地狱求道者'
    件数 = 3
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        属性.技能攻击力加成(0.16)
        pass
    def 进图属性(self, 属性):
        属性.所有属性强化加成(40)
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.15
        属性.移动速度 += 0.15
        属性.释放速度 += 0.20
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '技能攻击力 +16%<br>'
        temp += '所有属性强化 +40<br>'
        temp += '攻击速度 +15%<br>'
        temp += '移动速度 +15%<br>'
        temp += '释放速度 +20%<br>'
        return temp
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 195
        属性.转职被动智力 += 188
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.06
        属性.BUFF智力per *= 1.06
        属性.一觉Lv += 2
    def 装备描述(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +6%<br>'
            temp += '[守护恩赐]体力、精神 +195<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +6%<br>'
            temp += '[启示圣歌]智力 +188<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +6%<br>'
            temp += '[人偶操纵者]智力 +188<br>'
        return temp
class 套装效果66(套装):
    名称 = '次元旅行者'
    件数 = 3
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.10)
        属性.技能攻击力加成(0.18)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +10%<br>'
        temp += '技能攻击力 +18%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 80
        属性.转职被动智力 += 120
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉Lv += 1
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[守护恩赐]体力、精神 +80<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[启示圣歌]智力 +120<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[人偶操纵者]智力 +120<br>'
        return temp       
class 套装效果67(套装):
    名称 = '天命无常'
    件数 = 3
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.10)
        属性.技能攻击力加成(0.07)
        属性.百分比力智加成(0.07)
        if 属性.天命无常 == 0:
            if 属性.装备检查('命运反抗者'):
                属性.百分比力智加成(0.056)
            else:
                属性.百分比力智加成(0.046666667)
        if 属性.天命无常 == 4 or 属性.天命无常 == 5:
            属性.百分比力智加成(0.07)
        if 属性.天命无常 == 6:
            属性.百分比力智加成(0.14)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.天命无常 == 0:
            if 属性.装备检查('命运反抗者'):
                属性.移动速度 += 0.066
                属性.攻击速度 += 0.066
            else:
                属性.移动速度 += 0.055
                属性.攻击速度 += 0.055 
        if 属性.天命无常 >= 4:
            属性.移动速度 += 0.03 * 属性.天命无常
            属性.攻击速度 += 0.03 * 属性.天命无常
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +10%<br>'
        temp += '技能攻击力 +7%<br>'
        temp += '百分比力智 +7%<br>'
        if 属性.天命无常 == 0:
            if 属性.装备检查('命运反抗者'):
                temp += '百分比力智 +5.6%<br>'
                temp += '移动速度 +6.6%<br>'
                temp += '攻击速度 +6.6%<br>'
            else:
                temp += '移动速度 +5.5%<br>'
                temp += '攻击速度 +5.5%<br>'
                temp += '百分比力智 +4.6666667%<br>'
        if 属性.天命无常 == 4 or 属性.天命无常 == 5:
            temp += '百分比力智 +7%<br>'
            temp += '移动速度 +' +str(3 * 属性.天命无常) +'%<br>'
            temp += '攻击速度 +' +str(3 * 属性.天命无常) +'%<br>'
        if 属性.天命无常 == 6:
            temp += '百分比力智 +14%<br>'
            temp += '移动速度 +' +str(3 * 属性.天命无常) +'%<br>'
            temp += '攻击速度 +' +str(3 * 属性.天命无常) +'%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.08
        属性.BUFF智力per *= 1.08
        属性.一觉被动Lv += 2
        属性.一觉Lv += 2
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += 'Lv30-50 技能等级 +2<br>'
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +8%<br>'
            temp += '[天启之珠]力量、智力 +35<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +8%<br>'
            temp += '[圣光天启]力量、智力 +35<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +8%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +35<br>'
        return temp
class 套装效果68(套装):
    名称 = '悲剧的残骸'
    件数 = 3
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.29)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +29%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 171
        属性.转职被动智力 += 158
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.1
        属性.BUFF智力per *= 1.1
        属性.一觉Lv += 1
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +10%<br>' 
            temp += '[守护恩赐]体力、精神 +171<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +10%<br>'
            temp += '[启示圣歌]智力 +158<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +10%<br>'
            temp += '[人偶操纵者]智力 +158<br>'
        return temp
#endregion

#region  首饰套装
class 套装效果69(套装):
    名称 = '上古尘封术士'
    件数 = 2
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.10)
        属性.百分比三攻加成(0.14)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +10%<br>'
        temp += '百分比三攻 +14%<br>'
        return temp   
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 60
        属性.转职被动智力 += 60
        属性.BUFF力量per *= 1.02
        属性.BUFF智力per *= 1.02
        属性.一觉力智 += 45
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +2%<br>'
            temp += '[天启之珠]力量、智力 +45<br>'
            temp += '[守护恩赐]体力、精神 +60<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +2%<br>'
            temp += '[圣光天启]力量、智力 +45<br>'
            temp += '[启示圣歌]智力 +60<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +2%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +45<br>'
            temp += '[人偶操纵者]智力 +60<br>'
        return temp
class 套装效果70(套装):
    名称 = '破晓曦光'
    件数 = 2
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.10)
        属性.最终伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.05
        属性.魔法暴击率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +10%<br>'
        temp += '最终伤害 +10%<br>'
        temp += '物理暴击率 +5%<br>'
        temp += '魔法暴击率 +5%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFF力量per *= 1.03
        属性.BUFF智力per *= 1.03
        属性.一觉Lv += 1
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +3%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +3%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +3%<br>'
        return temp

class 套装效果71(套装):
    名称 = '幸运三角'
    件数 = 2
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.所有属性强化加成(77)
        属性.物理攻击力 += 77
        属性.魔法攻击力 += 77
        属性.独立攻击力 += 77
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.07
        属性.魔法暴击率 += 0.07
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '所有属性强化 +77<br>'
        temp += '物理暴击率 +7%<br>'
        temp += '魔法暴击率 +7%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 140
        属性.转职被动智力 += 140
        属性.BUFF力量per *= 1.04
        属性.BUFF智力per *= 1.04
        属性.一觉力智 += 45
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +4%<br>'
            temp += '[天启之珠]力量、智力 +45<br>'
            temp += '[守护恩赐]体力、精神 +140<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +4%<br>'
            temp += '[圣光天启]力量、智力 +45<br>'
            temp += '[启示：圣歌]智力 +140<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +4%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +45<br>'
            temp += '[人偶操控者]智力 +140<br>'
        return temp    

class 套装效果72(套装):
    名称 = '精灵使的权能'
    件数 = 2
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.10)
        属性.技能攻击力加成(0.12)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +10%<br>'
        temp += '技能攻击力 +12%<br>'
        return temp   
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 100
        属性.转职被动智力 += 110
        属性.一觉力智 += 20
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[天启之珠]力量、智力 +20<br>'
            temp += '[守护恩赐]体力、精神 +100<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[圣光天启]力量、智力 +20<br>'
            temp += '[启示圣歌]智力 +110<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[开幕！人偶剧场]力量、智力 +20<br>'
            temp += '[人偶操纵者]智力 +110<br>'
        return temp

class 套装效果73(套装):
    名称 = '上古尘封术士'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +20%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉Lv += 1
        属性.一觉力智 += 26
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[天启之珠]力量、智力 +26<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[圣光天启]力量、智力 +26<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]力量、智力 +26<br>'
        return temp

class 套装效果74(套装):
    名称 = '破晓曦光'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.属性附加加成(0.10)
        属性.技能等级加成('所有', 100, 100, 1)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.10
        属性.移动速度 += 0.10
        属性.释放速度 += 0.15
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '属性附加 +10%<br>'
        temp += 'Lv100 技能等级+1<br>'
        temp += '攻击速度 +10%<br>'
        temp += '移动速度 +10%<br>'
        temp += '释放速度 +15%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        属性.技能等级加成('所有', 100, 100, 1)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 100
        属性.转职被动智力 += 100
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.04
        属性.BUFF智力per *= 1.04
        属性.一觉Lv += 1
        属性.一觉力智 += 45
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +4%<br>'
            temp += '[天启之珠]力量、智力 +45<br>'
            temp += '[守护恩赐]体力、精神 +100<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +4%<br>'
            temp += '[圣光天启]力量、智力 +45<br>'
            temp += '[启示圣歌]智力 +100<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +4%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +45<br>'
            temp += '[人偶操纵者]智力 +100<br>'
        temp += 'Lv100 技能等级 +1<br>'
        return temp

class 套装效果75(套装):
    名称 = '幸运三角'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        if 属性.幸运三角 == 0:
            属性.技能攻击力加成(0.2915)
        elif 属性.幸运三角 == 1:
           属性.技能攻击力加成(0.27)
        elif 属性.幸运三角 == 2:
            属性.技能攻击力加成(0.31)
        elif 属性.幸运三角 == 3:
            属性.技能攻击力加成(0.34)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.幸运三角 == 0:
            属性.攻击速度 += 0.005
            属性.移动速度 += 0.005
            属性.释放速度 += 0.0075
        if 属性.幸运三角 == 3:
            属性.攻击速度 += 0.10
            属性.移动速度 += 0.10
            属性.释放速度 += 0.15  
        pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.幸运三角 == 0:
            temp += '技能攻击力 +29.15%<br>'
            temp += '攻击速度 +0.5%<br>'
            temp += '移动速度 +0.5%<br>'
            temp += '释放速度 +0.75%<br>'
        if 属性.幸运三角 == 1:
            temp += '技能攻击力 +27%<br>'
        if 属性.幸运三角 == 2:
            temp += '技能攻击力 +31%<br>'
        if 属性.幸运三角 == 3:
            temp += '技能攻击力 +34%<br>'
            temp += '攻击速度 +10%<br>'
            temp += '移动速度 +10%<br>'
            temp += '释放速度 +15%<br>'
        return temp       
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉Lv += 2
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +2<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +2<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +2<br>'
        return temp

class 套装效果76(套装):
    名称 = '精灵使的权能'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.10)
        属性.技能冷却缩减(1, 100, 0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.05
        属性.魔法暴击率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +10%<br>'
        temp += 'Lv1-100 技能CD-10%<br>'
        temp += '物理暴击率 +5%<br>'
        temp += '魔法暴击率 +5%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.03
        属性.BUFF智力per *= 1.03
        属性.一觉Lv += 1
        属性.一觉力智 += 26
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +3%<br>'
            temp += '[天启之珠]力量、智力 +26<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +3%<br>'
            temp += '[圣光天启]力量、智力 +26<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +3%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +26<br>'
        return temp
#endregion

#region  特殊套装
class 套装效果77(套装):
    名称 = '军神的隐秘遗产'
    件数 = 2
    类型 = '特殊'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.10)
        属性.最终伤害加成(0.08)
        if 属性.装备检查('军神的遗书'):
            if 属性.装备检查('军神的心之所念'):
                属性.暴击伤害加成(0.05)
            if 属性.装备检查('军神的古怪耳环'):
                属性.暴击伤害加成(0.05)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('军神的遗书'):
            if 属性.装备检查('军神的心之所念'):
                属性.攻击速度 += 0.05
                属性.移动速度 += 0.10
                属性.释放速度 += 0.075
            if 属性.装备检查('军神的古怪耳环'):
                属性.移动速度 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +10%<br>'
        temp += '最终伤害 +8%<br>'
        if 属性.装备检查('军神的遗书'):
            if 属性.装备检查('军神的心之所念'):
                temp += '暴击伤害 +5%<br>'
                temp += '攻击速度 +5%<br>'
                temp += '移动速度 +10%<br>'
                temp += '释放速度 +7.5%<br>'
            if 属性.装备检查('军神的古怪耳环'):
                temp += '暴击伤害 +5%<br>'
                temp += '移动速度 +5%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 230
        属性.转职被动智力 += 230
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.04
        属性.BUFF智力per *= 1.04
        属性.一觉Lv += 1
        属性.一觉力智 += 35
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +4%<br>'
            temp += '[天启之珠]力量、智力 +35<br>'
            temp += '[守护恩赐]体力、精神 +230<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +4%<br>'
            temp += '[圣光天启]力量、智力 +35<br>'
            temp += '[启示圣歌]智力 +230<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +4%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +35<br>'
            temp += '[人偶操纵者]智力 +230<br>'
        return temp

class 套装效果78(套装):
    名称 = '时间战争的残骸'
    件数 = 2
    类型 = '特殊'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.11)
        属性.暴击伤害加成(0.11)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +11%<br>'
        temp += '暴击伤害 +11%<br>'
        return temp    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.技能等级加成('所有', 1, 30, 2)
        属性.BUFF力量per *= 1.02
        属性.BUFF智力per *= 1.02
        属性.一觉力智 += 35
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +2%<br>'
            temp += '[天启之珠]力量、智力 +35<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +2%<br>'
            temp += '[圣光天启]力量、智力 +35<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +2%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +35<br>'
        temp += 'Lv1-30 技能等级 +2<br>'
        return temp

class 套装效果79(套装):
    名称 = '灵宝：世间真理'
    件数 = 2
    类型 = '特殊'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.15)
        属性.技能攻击力加成(0.07)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +15%<br>'
        temp += '技能攻击力 +7%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.BUFF力量per *= 1.02
        属性.BUFF智力per *= 1.02
        属性.一觉被动Lv += 1
        属性.一觉Lv += 1
    def 装备描述_BUFF(self, 属性):
        temp = ''
        temp += 'Lv30-50 技能等级 +1<br>'
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +2%<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +2%<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +2%<br>'
        return temp

class 套装效果80(套装):
    名称 = '能量主宰'
    件数 = 2
    类型 = '特殊'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.12)
        属性.伤害增加加成(0.12)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +12%<br>'
        temp += '伤害增加 +12%<br>'
        return temp  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 95
        属性.转职被动智力 += 95
        属性.BUFFLv += 2
        属性.BUFF力量per *= 1.02
        属性.BUFF智力per *= 1.02
        属性.一觉Lv += 1
        属性.一觉力智 += 35
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +2<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[荣誉祝福]力量、智力 +2%<br>'
            temp += '[天启之珠]力量、智力 +35<br>'
            temp += '[守护恩赐]体力、精神 +95<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +2<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[勇气祝福]力量、智力 +2%<br>'
            temp += '[圣光天启]力量、智力 +35<br>'
            temp += '[启示圣歌]智力 +95<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +2<br>'
            temp += '[开幕！人偶剧场]]技能等级 +1<br>'
            temp += '[禁忌诅咒]力量、智力 +2%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +35<br>'
            temp += '[人偶操纵者]智力 +95<br>'
        return temp

class 套装效果81(套装):
    名称 = '军神的隐秘遗产'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        属性.技能攻击力加成(0.10)
        if 属性.军神的隐秘遗产 == 0:
            属性.百分比力智加成(0.10)
        if 属性.军神的隐秘遗产 == 1:
            属性.百分比力智加成(0.10)
        if 属性.军神的隐秘遗产 == 2:
            属性.百分比力智加成(0.08)
        if 属性.军神的隐秘遗产 == 3:
            属性.百分比力智加成(0.06)
        if 属性.军神的隐秘遗产 == 4:
            属性.百分比力智加成(0.04)
        if 属性.军神的隐秘遗产 == 5:
            属性.百分比力智加成(0.02)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.军神的隐秘遗产 == 0:
            属性.攻击速度 += 0.10
            属性.释放速度 += 0.15
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '技能攻击力 +10%<br>'
        if 属性.军神的隐秘遗产 == 0:
            temp += '百分比力智 +10%<br>'
        if 属性.军神的隐秘遗产 == 1:
            temp += '百分比力智 +10%<br>'
        if 属性.军神的隐秘遗产 == 2:
            temp += '百分比力智 +8%<br>'
        if 属性.军神的隐秘遗产 == 3:
            temp += '百分比力智 +6%<br>'
        if 属性.军神的隐秘遗产 == 4:
            temp += '百分比力智 +4%<br>'
        if 属性.军神的隐秘遗产 == 5:
            temp += '百分比力智 +2%<br>'
        temp += '攻击速度 +10%<br>'
        temp += '释放速度 +15%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉Lv += 2
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +2<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +2<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +2<br>'
        return temp

class 套装效果82(套装):
    名称 = '时间战争的残骸'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.10)
        属性.技能攻击力加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.05
        属性.魔法暴击率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +10%<br>'
        temp += '技能攻击力 +10%<br>'
        temp += '物理暴击率 +5%<br>'
        temp += '魔法暴击率 +5%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 75
        属性.转职被动智力 += 85
        属性.一觉被动Lv += 1
        属性.一觉Lv += 2
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[信念光环]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +2%<br>'
            temp += '[守护恩赐]体力、精神 +75<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[虔诚信念]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +2%<br>'
            temp += '[启示圣歌]智力 +85<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[少女的爱]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +2%<br>'
            temp += '[人偶操纵者]智力 +85<br>'
        return temp      

class 套装效果83(套装):
    名称 = '灵宝：世间真理'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.12)
        pass
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 1, 85, 1)
        属性.技能等级加成('所有', 100, 100, 1)
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.10
        属性.移动速度 += 0.10
        属性.释放速度 += 0.15
        属性.物理暴击率 += 0.05
        属性.魔法暴击率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +12%<br>'
        temp += 'Lv1-85 技能等级+1<br>'
        temp += 'Lv100  技能等级+1<br>'
        temp += '攻击速度 +10%<br>'
        temp += '移动速度 +10%<br>'
        temp += '释放速度 +15%<br>'
        temp += '物理暴击率 +5%<br>'
        temp += '魔法暴击率 +5%<br>'
        return temp   
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        属性.技能等级加成('所有', 1, 85, 1)
        属性.技能等级加成('所有', 100, 100, 1)
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 100
        属性.转职被动智力 += 122
        属性.一觉Lv += 1
        属性.一觉力智 += 39
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[天启之珠]力量、智力 +39<br>'
            temp += '[守护恩赐]体力、精神 +100<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[圣光天启]力量、智力 +39<br>'
            temp += '[启示圣歌]智力 +122<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[开幕！人偶剧场]]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]力量、智力 +39<br>'
            temp += '[人偶操纵者]智力 +122<br>'
        temp += 'Lv1-85 技能等级 +1<br>'
        temp += 'Lv100 技能等级 +1<br>'
        return temp

class 套装效果84(套装):
    名称 = '能量主宰'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.10)
        属性.技能攻击力加成(0.08)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.10
        属性.魔法暴击率 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +10%<br>'
        temp += '技能攻击力 +8%<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.守护恩赐体精 += 110
        属性.转职被动智力 += 110
        属性.BUFF力量per *= 1.02
        属性.BUFF智力per *= 1.02
        属性.一觉Lv += 2
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[天启之珠]技能等级 +2<br>'
            temp += '[荣誉祝福]力量、智力 +2%<br>'
            temp += '[守护恩赐]体力、精神 +110<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[圣光天启]技能等级 +2<br>'
            temp += '[勇气祝福]力量、智力 +2%<br>'
            temp += '[启示圣歌]智力 +110<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[开幕！人偶剧场]]技能等级 +2<br>'
            temp += '[禁忌诅咒]力量、智力 +2%<br>'
            temp += '[人偶操纵者]智力 +110<br>'
        return temp
#endregion

#region  其它套装
class 套装效果85(套装):
    名称 = '超界·苍穹之云'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.10)
        属性.伤害增加加成(0.13)
        属性.技能等级加成('所有', 50, 50, 2)
        属性.技能等级加成('所有', 85, 85, 2)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.05
        属性.释放速度 += 0.075
        属性.移动速度 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +10%<br>'
        temp += '伤害增加 +13%<br>'
        temp += 'Lv50 技能等级+2<br>'
        temp += 'Lv85 技能等级+2<br>'
        temp += '攻击速度 +5%<br>'
        temp += '释放速度 +7.5%<br>'
        temp += '移动速度 +5%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        属性.技能等级加成('所有', 50, 50, 2)
        属性.技能等级加成('所有', 85, 85, 2)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 6
        属性.一觉力智 += 41
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +6<br>'
            temp += '[天启之珠]力量、智力 +41<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +6<br>'
            temp += '[圣光天启]力量、智力 +41<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +6<br>'
            temp += '[开幕！人偶剧场]力量、智力 +41<br>'
        temp += 'Lv50 技能等级 +2<br>'
        temp += 'Lv85 技能等级 +2<br>'
        return temp
class 套装效果86(套装):
    名称 = '超界·苍穹之云'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.36)
        属性.技能等级加成('所有', 50, 50, 2)
        属性.技能等级加成('所有', 85, 85, 2)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.17
        属性.释放速度 += 0.255
        属性.移动速度 += 0.17
        属性.物理暴击率 += 0.05
        属性.魔法暴击率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +36%<br>'
        temp += 'Lv50 技能等级+2<br>'
        temp += 'Lv85 技能等级+2<br>'
        temp += '攻击速度 +17%<br>'
        temp += '释放速度 +25.5%<br>'
        temp += '移动速度 +17%<br>'
        temp += '物理暴击率 +5%<br>'
        temp += '魔法暴击率 +5%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        属性.技能等级加成('所有', 50, 50, 2)
        属性.技能等级加成('所有', 85, 85, 2)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFF力量per *= 1.23
        属性.BUFF智力per *= 1.23
        
  
        属性.一觉力智 += 142
        属性.一觉力智per *= 1.05
        属性.守护恩赐体精 += 40
        属性.转职被动智力 += 220
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +23%<br>'
           
            temp += '[天启之珠]力量、智力 +142<br>'
            temp += '[天启之珠]力量、智力 +5%<br>'
            temp += '[守护恩赐]体力、精神 +40<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +23%<br>'
           
            temp += '[圣光天启]力量、智力 +142<br>'
            temp += '[圣光天启]力量、智力 +5%<br>'
            temp += '[启示：圣歌]智力 +220<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +23%<br>'
          
            temp += '[开幕！人偶剧场]力量、智力 +142<br>'
            temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
            temp += '[人偶操控者]智力 +220<br>'
        temp += 'Lv50 技能等级 +2<br>'
        temp += 'Lv85 技能等级 +2<br>'
        return temp
class 套装效果87(套装):
    名称 = '超界·永恒的季节'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.技能攻击力加成(0.12)
        属性.最终伤害加成(0.25)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.10
        属性.魔法暴击率 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '技能攻击力 +12%<br>'
        temp += '最终伤害 +25%<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 3
        属性.一觉力智 += 98
        属性.守护恩赐体精 += 120
        属性.转职被动智力 += 120
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +3<br>'
            temp += '[天启之珠]力量、智力 +98<br>'
            temp += '[守护恩赐]体力、精神 +120<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +3<br>'
            temp += '[圣光天启]力量、智力 +98<br>'
            temp += '[启示：圣歌]智力 +120<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +3<br>'
            temp += '[开幕！人偶剧场]力量、智力 +98<br>'
            temp += '[人偶操控者]智力 +120<br>'
        return temp
class 套装效果88(套装):
    名称 = '超界·永恒的季节'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.48)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.17
        属性.释放速度 += 0.255
        属性.移动速度 += 0.17
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +48%<br>'
        temp += '攻击速度 +17%<br>'
        temp += '释放速度 +25.5%<br>'
        temp += '移动速度 +17%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFF力量per *= 1.23
        属性.BUFF智力per *= 1.23
        
  
        属性.一觉力智 += 232
        属性.一觉力智per *= 1.05
        属性.守护恩赐体精 += 220
        属性.转职被动智力 += 220
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +23%<br>'
           
            temp += '[天启之珠]力量、智力 +232<br>'
            temp += '[天启之珠]力量、智力 +5%<br>'
            temp += '[守护恩赐]体力、精神 +220<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +23%<br>'
           
            temp += '[圣光天启]力量、智力 +232<br>'
            temp += '[圣光天启]力量、智力 +5%<br>'
            temp += '[启示：圣歌]智力 +220<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +23%<br>'
          
            temp += '[开幕！人偶剧场]力量、智力 +232<br>'
            temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
            temp += '[人偶操控者]智力 +220<br>'
        return temp     

class 套装效果89(套装):
    名称 = '超界·亿万年的星光'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.技能等级加成('所有', 50, 50, 2)
        属性.技能等级加成('所有', 85, 85, 1)
        属性.最终伤害加成(0.25)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += 'Lv50 技能等级+2<br>'
        temp += 'Lv85 技能等级+1<br>'
        temp += '最终伤害 +25%<br>'
        return temp 
    def 城镇属性_BUFF(self, 属性):
        属性.技能等级加成('所有', 50, 50, 2)
        属性.技能等级加成('所有', 85, 85, 1)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 6
        属性.一觉力智 += 20
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +6<br>'
            temp += '[天启之珠]力量、智力 +20<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +6<br>'
            temp += '[圣光天启]力量、智力 +20<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +6<br>'
            temp += '[开幕！人偶剧场]力量、智力 +20<br>'
        temp += 'Lv50 技能等级 +2<br>'
        temp += 'Lv85 技能等级 +1<br>'
        return temp
class 套装效果90(套装):
    名称 = '超界·亿万年的星光'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.属性附加加成(0.35)
        属性.技能等级加成('所有', 85, 85, 1)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.10
        属性.释放速度 += 0.15
        属性.移动速度 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '属性附加 +35%<br>'
        temp += 'Lv85 技能等级+1<br>'
        temp += '攻击速度 +10%<br>'
        temp += '释放速度 +15%<br>'
        temp += '移动速度 +10%<br>'
        return temp  
    def 城镇属性_BUFF(self, 属性):
        属性.技能等级加成('所有', 85, 85, 1)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFF力量per *= 1.23
        属性.BUFF智力per *= 1.23
        
  
        属性.一觉力智 += 163
        属性.一觉力智per *= 1.05
        属性.守护恩赐体精 += 340
        属性.转职被动智力 += 520
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +23%<br>'
           
            temp += '[天启之珠]力量、智力 +163<br>'
            temp += '[天启之珠]力量、智力 +5%<br>'
            temp += '[守护恩赐]体力、精神 +340<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +23%<br>'
           
            temp += '[圣光天启]力量、智力 +163<br>'
            temp += '[圣光天启]力量、智力 +5%<br>'
            temp += '[启示：圣歌]智力 +520<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +23%<br>'
          
            temp += '[开幕！人偶剧场]力量、智力 +163<br>'
            temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
            temp += '[人偶操控者]智力 +520<br>'
        temp += 'Lv85 技能等级 +1<br>'
        return temp
class 套装效果91(套装):
    名称 = '超界·精灵的荣耀'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.35)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.06
        属性.释放速度 += 0.09
        属性.移动速度 += 0.06
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +35%<br>'
        temp += '攻击速度 +6%<br>'
        temp += '释放速度 +9%<br>'
        temp += '移动速度 +6%<br>'
        return temp  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 6
        属性.一觉力智 += 150
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +6<br>'
            temp += '[天启之珠]力量、智力 +150<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +6<br>'
            temp += '[圣光天启]力量、智力 +150<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +6<br>'
            temp += '[开幕！人偶剧场]力量、智力 +150<br>'
        return temp
class 套装效果92(套装):
    名称 = '超界·精灵的荣耀'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.45)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.06
        属性.释放速度 += 0.09
        属性.移动速度 += 0.06
        属性.物理暴击率 += 0.10
        属性.魔法暴击率 += 0.10
        属性.移动速度 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +45%<br>'
        temp += '攻击速度 +6%<br>'
        temp += '释放速度 +9%<br>'
        temp += '移动速度 +6%<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        temp += '移动速度 +10%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFF力量per *= 1.23
        属性.BUFF智力per *= 1.23
        
  
        属性.一觉力智 += 225
        属性.一觉力智per *= 1.05
        属性.守护恩赐体精 += 220
        属性.转职被动智力 += 220
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +23%<br>'
           
            temp += '[天启之珠]力量、智力 +225<br>'
            temp += '[天启之珠]力量、智力 +5%<br>'
            temp += '[守护恩赐]体力、精神 +220<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +23%<br>'
           
            temp += '[圣光天启]力量、智力 +225<br>'
            temp += '[圣光天启]力量、智力 +5%<br>'
            temp += '[启示：圣歌]智力 +220<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +23%<br>'
          
            temp += '[开幕！人偶剧场]力量、智力 +225<br>'
            temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
            temp += '[人偶操控者]智力 +220<br>'
        return temp
class 套装效果93(套装):
    名称 = '超界·幸运的五彩石'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.所有属性强化加成(25)
        属性.最终伤害加成(0.25)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.10
        属性.魔法暴击率 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '所有属性强化 +25<br>'
        temp += '最终伤害 +25%<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 6
        属性.一觉力智 += 150
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +6<br>'
            temp += '[天启之珠]力量、智力 +150<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +6<br>'
            temp += '[圣光天启]力量、智力 +150<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +6<br>'
            temp += '[开幕！人偶剧场]力量、智力 +150<br>'
        return temp  

class 套装效果94(套装):
    名称 = '超界·幸运的五彩石'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.属性附加加成(0.35)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.10
        属性.释放速度 += 0.15
        属性.移动速度 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '属性附加 +35%<br>'
        temp += '攻击速度 +10%<br>'
        temp += '释放速度 +15%<br>'
        temp += '移动速度 +10%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFF力量per *= 1.23
        属性.BUFF智力per *= 1.23
        
  
        属性.一觉力智 += 225
        属性.一觉力智per *= 1.05
        属性.守护恩赐体精 += 220
        属性.转职被动智力 += 220
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]力量、智力 +23%<br>'
           
            temp += '[天启之珠]力量、智力 +225<br>'
            temp += '[天启之珠]力量、智力 +5%<br>'
            temp += '[守护恩赐]体力、精神 +220<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]力量、智力 +23%<br>'
           
            temp += '[圣光天启]力量、智力 +225<br>'
            temp += '[圣光天启]力量、智力 +5%<br>'
            temp += '[启示：圣歌]智力 +220<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]力量、智力 +23%<br>'
          
            temp += '[开幕！人偶剧场]力量、智力 +225<br>'
            temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
            temp += '[人偶操控者]智力 +220<br>'
        return temp
class 套装效果95(套装):
    名称 = '黑暗的第一权能'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.12)
        属性.百分比力智加成(0.12)
        属性.技能攻击力加成(0.08)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.05
        属性.释放速度 += 0.075
        属性.移动速度 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +12%<br>'
        temp += '百分比力智 +12%<br>'
        temp += '技能攻击力 +8%<br>'
        temp += '攻击速度 +5%<br>'
        temp += '释放速度 +7.5%<br>'
        temp += '移动速度 +5%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉Lv += 1
        属性.一觉力智 += 26
        属性.守护恩赐体精 += 160
        属性.转职被动智力 += 160
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +1<br>'
            temp += '[守护恩赐]体力、精神 +160<br>'
            temp += '[天启之珠]力量、智力 +26<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +1<br>'
            temp += '[启示：圣歌]智力 +160<br>'
            temp += '[圣光天启]力量、智力 +26<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +1<br>'
            temp += '[人偶操控者]智力 +160<br>'
            temp += '[开幕！人偶剧场]力量、智力 +26<br>'
        return temp

class 套装效果96(套装):
    名称 = '黑暗的第二权能'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        属性.暴击伤害加成(0.10)
        属性.百分比力智加成(0.08)
        属性.技能攻击力加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.05
        属性.释放速度 += 0.075
        属性.移动速度 += 0.05
        属性.物理暴击率 += 0.05
        属性.魔法暴击率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '暴击伤害 +10%<br>'
        temp += '百分比力智 +8%<br>'
        temp += '技能攻击力 +15%<br>'
        temp += '攻击速度 +5%<br>'
        temp += '释放速度 +7.5%<br>'
        temp += '移动速度 +5%<br>'
        temp += '物理暴击率 +5%<br>'
        temp += '魔法暴击率 +5%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉Lv += 2
        属性.一觉力智 += 26
        属性.BUFF力量per *= 1.03
        属性.BUFF智力per *= 1.03
        属性.守护恩赐体精 += 247
        属性.转职被动智力 += 209
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.角色 == '圣职者(男)':
            temp += '[荣誉祝福]技能等级 +1<br>'
            temp += '[天启之珠]技能等级 +2<br>'
            temp += '[守护恩赐]体力、精神 +247<br>'
            temp += '[荣誉祝福]力量、智力 +3%<br>'
            temp += '[天启之珠]力量、智力 +26<br>'
        elif 属性.角色 == '圣职者(女)':
            temp += '[勇气祝福]技能等级 +1<br>'
            temp += '[圣光天启]技能等级 +2<br>'
            temp += '[启示：圣歌]智力 +209<br>'
            temp += '[勇气祝福]力量、智力 +3%<br>'
            temp += '[圣光天启]力量、智力 +26<br>'
        elif 属性.角色 == '魔法师(女)':
            temp += '[禁忌诅咒]技能等级 +1<br>'
            temp += '[开幕！人偶剧场]技能等级 +2<br>'
            temp += '[人偶操控者]智力 +209<br>'
            temp += '[禁忌诅咒]力量、智力 +3%<br>'
            temp += '[开幕！人偶剧场]力量、智力 +26<br>'
        return temp      

class 套装效果97(套装):
    名称 = '维度崩坏'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·维度冲击臂环'):
            属性.力量 += 200
            属性.智力 += 200
            属性.百分比力智加成(0.15)
            属性.附加伤害加成(0.10)
            属性.暴击伤害加成(0.10)
            属性.百分比三攻加成(0.13)
        elif 属性.装备检查('时空：维度冲击臂环'):
            属性.附加伤害加成(0.05)
            属性.暴击伤害加成(0.15)
        else:
            属性.百分比力智加成(0.04)
            属性.附加伤害加成(0.04)
            属性.技能攻击力加成(0.08)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·维度冲击臂环'):
            属性.物理暴击率 += 0.03
            属性.魔法暴击率 += 0.03
        else:
            pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·维度冲击臂环'):
            temp += '力量 +200<br>'
            temp += '智力 +200<br>'
            temp += '百分比力智 +15%<br>'
            temp += '附加伤害 +10%<br>'
            temp += '暴击伤害 +10%<br>'
            temp += '百分比三攻 +13%<br>'
            temp += '物理暴击率 +3%<br>'
            temp += '魔法暴击率 +3%<br>'
        elif 属性.装备检查('时空：维度冲击臂环'):
            temp += '附加伤害 +5%<br>'
            temp += '暴击伤害 +15%<br>'
        else:
            temp += '百分比力智 +4%<br>'
            temp += '附加伤害 +4%<br>'
            temp += '技能攻击力 +8%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        if 属性.装备检查('维度冲击臂环'):
            属性.BUFFLv += 1
            属性.一觉Lv += 1
            属性.守护恩赐体精 += 76
            属性.转职被动智力 += 76
        elif 属性.装备检查('时空·维度冲击臂环'):
            属性.BUFFLv += 1
            属性.一觉Lv += 1
            属性.一觉被动Lv += 2
            属性.BUFF力量per *= 1.02
            属性.BUFF智力per *= 1.02
            属性.BUFF物攻per *= 1.02
        else:
            属性.智力 += 200
            属性.BUFFLv += 1
            属性.一觉Lv += 1
            属性.一觉被动Lv += 2
            属性.一觉力智 += 46
            属性.守护恩赐体精 += 271
            属性.转职被动智力 += 71
            属性.BUFF物攻per *= 1.03
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.装备检查('维度冲击臂环'):
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +1<br>'
                temp += '[天启之珠]技能等级 +1<br>'
                temp += '[守护恩赐]体力、精神 +76<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[勇气祝福]技能等级 +1<br>'
                temp += '[圣光天启]技能等级 +1<br>'
                temp += '[启示：圣歌]智力 +76<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[禁忌诅咒]技能等级 +1<br>'
                temp += '[开幕！人偶剧场]技能等级 +1<br>'
                temp += '[人偶操控者]智力 +76<br>'
        elif 属性.装备检查('时空·维度冲击臂环'):
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +1<br>'
                temp += '[天启之珠]技能等级 +1<br>'
                temp += '[信念光环]技能等级 +2<br>'
                temp += '[荣誉祝福]力量、智力 +2%<br>'
                temp += '[荣誉祝福]物理攻击力增加量 +2%<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[勇气祝福]技能等级 +1<br>'
                temp += '[圣光天启]技能等级 +1<br>'
                temp += '[虔诚信念]技能等级 +2<br>'
                temp += '[勇气祝福]力量、智力 +2%<br>'
                temp += '[勇气祝福]物理攻击力增加量 +2%<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[禁忌诅咒]技能等级 +1<br>'
                temp += '[开幕！人偶剧场]技能等级 +1<br>'
                temp += '[少女的爱]技能等级 +2<br>'
                temp += '[禁忌诅咒]力量、智力 +2%<br>'
                temp += '[禁忌诅咒]物理攻击力增加量 +2%<br>'
        else:
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +1<br>'
                temp += '[天启之珠]技能等级 +1<br>'
                temp += '[信念光环]技能等级 +2<br>'
                temp += '[天启之珠]力量、智力 +46<br>'
                temp += '[荣誉祝福]物理攻击力增加量 +3%<br>'
                temp += '[守护恩赐]体力、精神 +271<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '智力 +200<br>'
                temp += '[勇气祝福]技能等级 +1<br>'
                temp += '[圣光天启]技能等级 +1<br>'
                temp += '[虔诚信念]技能等级 +2<br>'
                temp += '[圣光天启]力量、智力 +46<br>'
                temp += '[勇气祝福]物理攻击力增加量 +3%<br>'
                temp += '[启示：圣歌]智力 +71<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '智力 +200<br>'
                temp += '[禁忌诅咒]技能等级 +1<br>'
                temp += '[开幕！人偶剧场]技能等级 +1<br>'
                temp += '[少女的爱]技能等级 +2<br>'
                temp += '[开幕！人偶剧场]力量、智力 +46<br>'
                temp += '[禁忌诅咒]物理攻击力增加量 +3%<br>'
                temp += '[人偶操控者]智力 +71<br>'
        return temp
class 套装效果98(套装):
    名称 = '暗之腐蚀'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            属性.力量 += 200
            属性.智力 += 200
            属性.百分比力智加成(0.05)
            属性.附加伤害加成(0.16)
            属性.暴击伤害加成(0.23)
            属性.技能攻击力加成(0.05)
        elif 属性.装备检查('时空：腐蚀之黑色十字耳环'):
            属性.附加伤害加成(0.13)
            属性.暴击伤害加成(0.05)
            属性.技能攻击力加成(0.05)
        else:
            属性.百分比力智加成(0.05)
            属性.技能攻击力加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            属性.物理暴击率 += 0.04
            属性.魔法暴击率 += 0.04
        else:
            pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            temp += '力量 +200<br>'
            temp += '智力 +200<br>'
            temp += '百分比力智 +5%<br>'
            temp += '附加伤害 +16%<br>'
            temp += '暴击伤害 +23%<br>'
            temp += '技能攻击力 +5%<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        elif 属性.装备检查('时空：腐蚀之黑色十字耳环'):
            temp += '附加伤害 +13%<br>'
            temp += '暴击伤害 +5%<br>'
            temp += '技能攻击力 +5%<br>'
        else:
            temp += '百分比力智 +5%<br>'
            temp += '技能攻击力 +15%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        if 属性.装备检查('腐蚀之黑色十字耳环'):
            属性.一觉Lv += 2
            属性.一觉力智per *= 1.03
            属性.守护恩赐体精 += 127
            属性.转职被动智力 += 109
        elif 属性.装备检查('时空·腐蚀之黑色十字耳环'):
            属性.BUFFLv += 1
            属性.一觉Lv += 2
            属性.BUFF力量per *= 1.03
            属性.BUFF智力per *= 1.03
            属性.BUFF魔攻per *= 1.02
            属性.BUFF独立per *= 1.02
            属性.一觉力智 += 30
            属性.守护恩赐体精 += 127
            属性.转职被动智力 += 109
        else:
            属性.智力 += 200
            属性.BUFFLv += 1
            属性.一觉Lv += 2
            属性.技能等级加成('所有', 1, 48, 1)
            属性.BUFF力量per *= 1.03
            属性.BUFF智力per *= 1.03
            属性.BUFF魔攻per *= 1.03
            属性.BUFF独立per *= 1.03
            属性.一觉力智 += 50
            属性.守护恩赐体精 += 252
            属性.转职被动智力 += 14
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.装备检查('腐蚀之黑色十字耳环'):
            if 属性.角色 == '圣职者(男)':
                temp += '[天启之珠]技能等级 +2<br>'
                temp += '[天启之珠]力量、智力 +3%<br>'
                temp += '[守护恩赐]体力、精神 +127<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[圣光天启]技能等级 +2<br>'
                temp += '[圣光天启]力量、智力 +3%<br>'
                temp += '[启示：圣歌]智力 +109<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[开幕！人偶剧场]技能等级 +2<br>'
                temp += '[开幕！人偶剧场]力量、智力 +3%<br>'
                temp += '[人偶操控者]智力 +109<br>'
        elif 属性.装备检查('时空·腐蚀之黑色十字耳环'):
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +1<br>'
                temp += '[天启之珠]技能等级 +2<br>'
                temp += '[荣誉祝福]力量、智力 +3%<br>'
                temp += '[荣誉祝福]魔法、独立攻击力增加量 +2%<br>'
                temp += '[天启之珠]力量、智力 +30<br>'
                temp += '[守护恩赐]体力、精神 +127<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[勇气祝福]技能等级 +1<br>'
                temp += '[圣光天启]技能等级 +2<br>'
                temp += '[勇气祝福]力量、智力 +3%<br>'
                temp += '[勇气祝福]魔法、独立攻击力增加量 +2%<br>'
                temp += '[圣光天启]力量、智力 +30<br>'
                temp += '[启示：圣歌]智力 +109<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[禁忌诅咒]技能等级 +1<br>'
                temp += '[开幕！人偶剧场]技能等级 +2<br>'
                temp += '[禁忌诅咒]力量、智力 +3%<br>'
                temp += '[禁忌诅咒]魔法、独立攻击力增加量 +2%<br>'
                temp += '[开幕！人偶剧场]力量、智力 +50<br>'
                temp += '[人偶操控者]智力 +109<br>'
        else:   
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +1<br>'
                temp += '[天启之珠]技能等级 +2<br>'
                temp += '[荣誉祝福]力量、智力 +3%<br>'
                temp += '[荣誉祝福]魔法、独立攻击力增加量 +3%<br>'
                temp += '[天启之珠]力量、智力 +50<br>'
                temp += '[守护恩赐]体力、精神 +252<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '智力 +200<br>'
                temp += '[勇气祝福]技能等级 +1<br>'
                temp += '[圣光天启]技能等级 +2<br>'
                temp += '[勇气祝福]力量、智力 +3%<br>'
                temp += '[勇气祝福]魔法、独立攻击力增加量 +3%<br>'
                temp += '[圣光天启]力量、智力 +50<br>'
                temp += '[启示：圣歌]智力 +14<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '智力 +200<br>'
                temp += '[禁忌诅咒]技能等级 +1<br>'
                temp += '[开幕！人偶剧场]技能等级 +2<br>'
                temp += '[禁忌诅咒]力量、智力 +3%<br>'
                temp += '[禁忌诅咒]魔法、独立攻击力增加量 +3%<br>'
                temp += '[开幕！人偶剧场]力量、智力 +50<br>'
                temp += '[人偶操控者]智力 +14<br>'
            temp += 'Lv1-48 技能Lv+1<br>'
        return temp
class 套装效果99(套装):
    名称 = '堕落的暗黑之力'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            属性.力量 += 200
            属性.智力 += 200
            属性.百分比三攻加成(0.12)
            属性.伤害增加加成(0.10)
            属性.暴击伤害加成(0.10)
            属性.最终伤害加成(0.05)
        elif 属性.装备检查('时空：黑暗幽灵紫杉胸甲'):
            属性.百分比三攻加成(0.06)
            属性.伤害增加加成(0.10)
            属性.暴击伤害加成(0.10)
        else:
            属性.伤害增加加成(0.10)
            属性.暴击伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            pass
        else:
            属性.物理暴击率 += 0.04
            属性.魔法暴击率 += 0.04
        pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            temp += '力量 +200<br>'
            temp += '智力 +200<br>'
            temp += '百分比三攻 +12%<br>'
            temp += '伤害增加 +10%<br>'
            temp += '暴击伤害 +10%<br>'
            temp += '最终伤害 +5%<br>'
        elif 属性.装备检查('时空：黑暗幽灵紫杉胸甲'):
            temp += '百分比三攻 +6%<br>'
            temp += '伤害增加 +10%<br>'
            temp += '暴击伤害 +10%<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        else:
            temp += '伤害增加 +10%<br>'
            temp += '暴击伤害 +10%<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):

        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            属性.智力 += 200
            属性.BUFFLv += 6
            属性.一觉Lv += 1
            属性.一觉力智 += 80
            属性.守护恩赐体精 += 200
            属性.BUFF力量per *= 1.08
            属性.BUFF智力per *= 1.08
            属性.BUFF物攻per *= 1.04
            属性.BUFF魔攻per *= 1.04
            属性.BUFF独立per *= 1.04
        elif 属性.装备检查('时空·黑暗幽灵紫杉胸甲'):
            属性.BUFFLv += 4
            属性.一觉Lv += 1
            属性.一觉力智 += 15
            属性.守护恩赐体精 += 80
            属性.转职被动智力 += 80
            属性.BUFF力量per *= 1.04
            属性.BUFF智力per *= 1.04
            属性.BUFF物攻per *= 1.03
            属性.BUFF魔攻per *= 1.03
            属性.BUFF独立per *= 1.03
        else:
            属性.BUFFLv += 3
            属性.一觉Lv += 1
            属性.一觉力智 += 15
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +6<br>'
                temp += '[天启之珠]技能等级 +1<br>'
                temp += '[荣誉祝福]力量、智力 +8%<br>'
                temp += '[荣誉祝福]物理、魔法、独立攻击力增加量 +4%<br>'
                temp += '[天启之珠]力量、智力 +80<br>'
                temp += '[守护恩赐]体力、精神 +200<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '智力 +200<br>'
                temp += '[勇气祝福]技能等级 +6<br>'
                temp += '[圣光天启]技能等级 +1<br>'
                temp += '[勇气祝福]力量、智力 +8%<br>'
                temp += '[勇气祝福]物理、魔法、独立攻击力增加量 +4%<br>'
                temp += '[圣光天启]力量、智力 +80<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '智力 +200<br>'
                temp += '[禁忌诅咒]技能等级 +6<br>'
                temp += '[开幕！人偶剧场]技能等级 +1<br>'
                temp += '[禁忌诅咒]力量、智力 +8%<br>'
                temp += '[禁忌诅咒]物理、魔法、独立攻击力增加量 +4%<br>'
                temp += '[开幕！人偶剧场]力量、智力 +80<br>'
        elif 属性.装备检查('时空·黑暗幽灵紫杉胸甲'):
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +4<br>'
                temp += '[天启之珠]技能等级 +1<br>'
                temp += '[荣誉祝福]力量、智力 +4%<br>'
                temp += '[荣誉祝福]物理、魔法、独立攻击力增加量 +3%<br>'
                temp += '[天启之珠]力量、智力 +15<br>'
                temp += '[守护恩赐]体力、精神 +80<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[勇气祝福]技能等级 +4<br>'
                temp += '[圣光天启]技能等级 +1<br>'
                temp += '[勇气祝福]力量、智力 +4%<br>'
                temp += '[勇气祝福]物理、魔法、独立攻击力增加量 +3%<br>'
                temp += '[圣光天启]力量、智力 +15<br>'
                temp += '[启示：圣歌]智力 +80<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[禁忌诅咒]技能等级 +4<br>'
                temp += '[开幕！人偶剧场]技能等级 +1<br>'
                temp += '[禁忌诅咒]力量、智力 +4%<br>'
                temp += '[禁忌诅咒]物理、魔法、独立攻击力增加量 +3%<br>'
                temp += '[开幕！人偶剧场]力量、智力 +15<br>'
                temp += '[人偶操控者]智力 +80<br>'
        else:
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +3<br>'
                temp += '[天启之珠]技能等级 +1<br>'
                temp += '[天启之珠]力量、智力 +15<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[勇气祝福]技能等级 +3<br>'
                temp += '[圣光天启]技能等级 +1<br>'
                temp += '[圣光天启]力量、智力 +15<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[禁忌诅咒]技能等级 +3<br>'
                temp += '[开幕！人偶剧场]技能等级 +1<br>'
                temp += '[开幕！人偶剧场]力量、智力 +15<br>'
        return temp
class 套装效果100(套装):
    名称 = '堕落的暗黑之力'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            属性.力量 += 200
            属性.智力 += 200
            属性.附加伤害加成(0.20)
            属性.最终伤害加成(0.20)
            属性.技能攻击力加成(0.16)
        elif 属性.装备检查('时空：黑暗幽灵紫杉胸甲'):
            属性.附加伤害加成(0.07)
            属性.最终伤害加成(0.20)
            属性.技能攻击力加成(0.10)
        else:
            属性.附加伤害加成(0.13)
            属性.最终伤害加成(0.12)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            属性.物理暴击率 += 0.08
            属性.魔法暴击率 += 0.08
        else:
            pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            temp += '力量 +200<br>'
            temp += '智力 +200<br>'
            temp += '附加伤害 +20%<br>'
            temp += '最终伤害 +20%<br>'
            temp += '技能攻击力 +16%<br>'
            temp += '物理暴击率 +8%<br>'
            temp += '魔法暴击率 +8%<br>'
        elif 属性.装备检查('时空：黑暗幽灵紫杉胸甲'):
            temp += '附加伤害 +7%<br>'
            temp += '最终伤害 +20%<br>'
            temp += '技能攻击力 +10%<br>'
        else:        
            temp += '附加伤害 +13%<br>'
            temp += '最终伤害 +12%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        if 属性.装备检查('黑暗幽灵紫杉胸甲'):
            属性.一觉被动Lv += 2
            属性.BUFF力量per *= 1.22
            属性.BUFF智力per *= 1.22
            属性.一觉力智 += 205
            属性.一觉力智per *= 1.05
            属性.守护恩赐体精 += 120
            属性.转职被动智力 += 120
            
      
        elif 属性.装备检查('时空·黑暗幽灵紫杉胸甲'):
            属性.一觉被动Lv += 2
            属性.一觉Lv += 1
            属性.BUFF力量per *= 1.29
            属性.BUFF智力per *= 1.29
            属性.一觉力智 += 205
            属性.一觉力智per *= 1.06
            属性.守护恩赐体精 += 255
            属性.转职被动智力 += 255
            
      
        else:
            属性.智力 += 200
            属性.BUFF力量per *= 1.33
            属性.BUFF智力per *= 1.33
            属性.一觉力智 += 205
            属性.一觉力智per *= 1.07
            属性.守护恩赐体精 += 265
            属性.转职被动智力 += 65
            
      
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.装备检查('黑暗幽灵紫杉胸甲'):
            if 属性.角色 == '圣职者(男)':
                temp += '[信念光环]技能等级 +2<br>'
                temp += '[荣誉祝福]力量、智力 +22%<br>'
                temp += '[天启之珠]力量、智力 +205<br>'
                temp += '[天启之珠]力量、智力 +5%<br>'
                temp += '[守护恩赐]体力、精神 +120<br>'
               
            elif 属性.角色 == '圣职者(女)':
                temp += '[虔诚信念]技能等级 +2<br>'
                temp += '[勇气祝福]力量、智力 +22%<br>'
                temp += '[圣光天启]力量、智力 +205<br>'
                temp += '[圣光天启]力量、智力 +5%<br>'
                temp += '[启示：圣歌]智力 +120<br>'
               
            elif 属性.角色 == '魔法师(女)':
                temp += '[少女的爱]技能等级 +2<br>'
                temp += '[禁忌诅咒]力量、智力 +22%<br>'
                temp += '[开幕！人偶剧场]力量、智力 +205<br>'
                temp += '[开幕！人偶剧场]力量、智力 +5%<br>'
                temp += '[人偶操控者]智力 +120<br>'
              
        elif 属性.装备检查('时空·黑暗幽灵紫杉胸甲'):
            if 属性.角色 == '圣职者(男)':
                temp += '[信念光环]技能等级 +2<br>'
                temp += '[荣誉祝福]技能等级 +1<br>'
                temp += '[荣誉祝福]力量、智力 +29%<br>'
                temp += '[天启之珠]力量、智力 +205<br>'
                temp += '[天启之珠]力量、智力 +6%<br>'
                temp += '[守护恩赐]体力、精神 +255<br>'
               
            elif 属性.角色 == '圣职者(女)':
                temp += '[虔诚信念]技能等级 +2<br>'
                temp += '[勇气祝福]技能等级 +1<br>'
                temp += '[勇气祝福]力量、智力 +29%<br>'
                temp += '[圣光天启]力量、智力 +205<br>'
                temp += '[圣光天启]力量、智力 +6%<br>'
                temp += '[启示：圣歌]智力 +255<br>'
               
            elif 属性.角色 == '魔法师(女)':
                temp += '[少女的爱]技能等级 +2<br>'
                temp += '[禁忌诅咒]技能等级 +1<br>'
                temp += '[禁忌诅咒]力量、智力 +29%<br>'
                temp += '[开幕！人偶剧场]力量、智力 +205<br>'
                temp += '[开幕！人偶剧场]力量、智力 +6%<br>'
                temp += '[人偶操控者]智力 +205<br>'
              
        else:
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]力量、智力 +33%<br>'
                temp += '[天启之珠]力量、智力 +205<br>'
                temp += '[天启之珠]力量、智力 +7%<br>'
                temp += '[守护恩赐]体力、精神 +265<br>'
               
            elif 属性.角色 == '圣职者(女)':
                temp += '智力 +200<br>'
                temp += '[勇气祝福]力量、智力 +33%<br>'
                temp += '[圣光天启]力量、智力 +205<br>'
                temp += '[圣光天启]力量、智力 +7%<br>'
                temp += '[启示：圣歌]智力 +65<br>'
               
            elif 属性.角色 == '魔法师(女)':
                temp += '智力 +200<br>'
                temp += '[禁忌诅咒]力量、智力 +33%<br>'
                temp += '[开幕！人偶剧场]力量、智力 +205<br>'
                temp += '[开幕！人偶剧场]力量、智力 +7%<br>'
                temp += '[人偶操控者]智力 +65<br>'
              
        return temp
class 套装效果101(套装):
    名称 = '江山如画'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.20)
        属性.技能攻击力加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +20%<br>'
        temp += '技能攻击力 +10%<br>'
        return temp     
    def 城镇属性_BUFF(self, 属性):
        pass

    def 进图属性_BUFF(self, 属性):
        pass

    def BUFF属性(self, 属性):
        if 属性.装备检查('轮回·维度冲击臂环'):
            pass
        elif 属性.装备检查('时空·维度冲击臂环'):
            属性.一觉力智 += 34
            属性.BUFF力量per *= 1.04
            属性.BUFF智力per *= 1.04
            属性.守护恩赐体精 += 16
            属性.转职被动智力 += 16
        else:
            属性.一觉被动Lv += 2
            属性.一觉力智 += 26
            属性.守护恩赐体精 += 76
            属性.转职被动智力 += 76
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·维度冲击臂环'):
            temp += '无<br>'
        elif 属性.装备检查('时空·维度冲击臂环'):
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]力量、智力 +4%<br>'
                temp += '[天启之珠]力量、智力 +34<br>'
                temp += '[守护恩赐]体力、精神 +16<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[勇气祝福]力量、智力 +4%<br>'
                temp += '[圣光天启]力量、智力 +34<br>'
                temp += '[启示：圣歌]智力 +16<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[禁忌诅咒]力量、智力 +4%<br>'
                temp += '[开幕！人偶剧场]力量、智力 +34<br>'
                temp += '[人偶操控者]智力 +16<br>'
        else:
            if 属性.角色 == '圣职者(男)':
                temp += '[信念光环]技能等级 +2<br>'
                temp += '[天启之珠]力量、智力 +26<br>'
                temp += '[守护恩赐]体力、精神 +76<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[虔诚信念]技能等级 +2<br>'
                temp += '[圣光天启]力量、智力 +26<br>'
                temp += '[启示：圣歌]智力 +76<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[少女的爱]技能等级 +2<br>'
                temp += '[开幕！人偶剧场]力量、智力 +26<br>'
                temp += '[人偶操控者]智力 +76<br>'
        return temp

class 套装效果102(套装):
    名称 = '万物的生灭'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        属性.最终伤害加成(0.12)
        属性.技能攻击力加成(0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.05
        属性.魔法暴击率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '最终伤害 +12%<br>'
        temp += '技能攻击力 +20%<br>'
        temp += '物理暴击率 +5%<br>'
        temp += '魔法暴击率 +5%<br>'
        return temp
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            pass
        elif 属性.装备检查('时空·腐蚀之黑色十字耳环'):
            属性.BUFFLv += 1
            属性.一觉Lv += 1
            属性.一觉力智 += 20
            属性.守护恩赐体精 += 120
            属性.转职被动智力 += 100
        else:
            属性.BUFFLv += 1
            属性.一觉力智 += 50
            属性.守护恩赐体精 += 120
            属性.转职被动智力 += 100
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            temp += '无<br>'
        elif 属性.装备检查('时空·腐蚀之黑色十字耳环'):
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +1<br>'
                temp += '[天启之珠]技能等级 +1<br>'
                temp += '[天启之珠]力量、智力 +20<br>'
                temp += '[守护恩赐]体力、精神 +120<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[勇气祝福]技能等级 +1<br>'
                temp += '[圣光天启]技能等级 +1<br>'
                temp += '[圣光天启]力量、智力 +20<br>'
                temp += '[启示：圣歌]智力 +100<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[禁忌诅咒]技能等级 +1<br>'
                temp += '[开幕！人偶剧场]技能等级 +1<br>'
                temp += '[开幕！人偶剧场]力量、智力 +20<br>'
                temp += '[人偶操控者]智力 +100<br>'
        else:
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +1<br>'
                temp += '[天启之珠]力量、智力 +50<br>'
                temp += '[守护恩赐]体力、精神 +120<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[勇气祝福]技能等级 +1<br>'
                temp += '[圣光天启]力量、智力 +50<br>'
                temp += '[启示：圣歌]智力 +100<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[禁忌诅咒]技能等级 +1<br>'
                temp += '[开幕！人偶剧场]力量、智力 +50<br>'
                temp += '[人偶操控者]智力 +120<br>'
        return temp     

class 套装效果103(套装):
    名称 = '兵法之神'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.12)
        属性.物理攻击力 += 200
        属性.魔法攻击力 += 200
        属性.独立攻击力 += 200
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.10
        属性.移动速度 += 0.10
        属性.释放速度 += 0.15
        属性.物理暴击率 += 0.05
        属性.魔法暴击率 += 0.05
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +12%<br>'
        temp += '物理攻击力 +200<br>'
        temp += '魔法攻击力 +200<br>'
        temp += '独立攻击力 +200<br>'
        temp += '攻击速度 +10%<br>'
        temp += '移动速度 +10%<br>'
        temp += '释放速度 +15%<br>'
        temp += '物理暴击率 +5%<br>'
        temp += '魔法暴击率 +5%<br>'
        return temp      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
           pass
        elif 属性.装备检查('时空·黑暗幽灵紫杉胸甲'):
            属性.BUFFLv += 2
            属性.一觉力智 += 65
            属性.守护恩赐体精 += 80
            属性.转职被动智力 += 80
            属性.BUFF力量per *= 1.04
            属性.BUFF智力per *= 1.04
        else:
            属性.BUFFLv += 3
            属性.一觉力智 += 65
    def 装备描述_BUFF(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            temp += '无<br>'
        elif 属性.装备检查('时空·黑暗幽灵紫杉胸甲'):
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +2<br>'
                temp += '[荣誉祝福]力量、智力 +4%<br>'
                temp += '[天启之珠]力量、智力 +65<br>'
                temp += '[守护恩赐]体力、精神 +80<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[勇气祝福]技能等级 +2<br>'
                temp += '[勇气祝福]力量、智力 +4%<br>'
                temp += '[圣光天启]力量、智力 +65<br>'
                temp += '[启示：圣歌]智力 +80<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[禁忌诅咒]技能等级 +2<br>'
                temp += '[禁忌诅咒]力量、智力 +4%<br>'
                temp += '[开幕！人偶剧场]力量、智力 +65<br>'
                temp += '[人偶操控者]智力 +80<br>'
        else:
            if 属性.角色 == '圣职者(男)':
                temp += '[荣誉祝福]技能等级 +3<br>'
                temp += '[天启之珠]力量、智力 +65<br>'
            elif 属性.角色 == '圣职者(女)':
                temp += '[勇气祝福]技能等级 +3<br>'
                temp += '[圣光天启]力量、智力 +65<br>'
            elif 属性.角色 == '魔法师(女)':
                temp += '[禁忌诅咒]技能等级 +3<br>'
                temp += '[开幕！人偶剧场]力量、智力 +65<br>'
        return temp
class 套装效果104(套装):
    名称 = '兵法之神'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.所有属性强化加成(25)
        属性.百分比三攻加成(0.22)
        属性.技能攻击力加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '所有属性强化 +25<br>'
        temp += '百分比三攻 +22%<br>'
        temp += '技能攻击力 +10%<br>'
        return temp  

class 套装效果105(套装):
    名称 = '流逝轮回的记忆'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.百分比减防 += 0.02
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比减防 +5%<br>'
        temp += '(BOSS：实际2%)<br>'
        return temp        

class 套装效果106(套装):
    名称 = '无相轮回的希望'
    件数 = 2
    类型 = '特殊'
    def 城镇属性(self, 属性):
        pass
    def 进图属性(self, 属性):
        属性.所有属性强化加成(10)
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '所有属性强化 +10<br>'
        return temp 

class 套装效果107(套装):
    名称 = '魔战无双'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.35)
        属性.技能等级加成('所有', 50, 75, 2)
        属性.技能等级加成('所有', 85, 85, 1)
        try:
            属性.技能栏[属性.技能序号['基础精通']].倍率 *= 1.2
        except:
            pass
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.10 * 3
        属性.移动速度 += 0.10 * 3
        属性.释放速度 += 0.15 * 3
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +35%<br>'
        temp += 'Lv50-75 技能等级+2<br>'
        temp += 'Lv85 技能等级+1<br>'
        temp += '基础精通效果 +20%<br>'
        temp += '攻击速度 +10% x3<br>'
        temp += '移动速度 +10% x3<br>'
        temp += '释放速度 +15% x3<br>'
        return temp     

class 套装效果108(套装):
    名称 = '霸域英豪'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.物理攻击力 += 300
        属性.魔法攻击力 += 300
        属性.独立攻击力 += 300
        属性.力量 += 220
        属性.智力 += 220
        pass
    def 进图属性(self, 属性):
        属性.附加伤害加成(0.40)
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.05
        属性.移动速度 += 0.05
        属性.释放速度 += 0.20
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '物理攻击力 +300<br>'
        temp += '魔法攻击力 +300<br>'
        temp += '独立攻击力 +300<br>'
        temp += '力量 +200<br>'
        temp += '智力 +200<br>'
        temp += '附加伤害 +40%<br>'
        temp += '攻击速度 +5%<br>'
        temp += '移动速度 +5%<br>'
        temp += '释放速度 +20%<br>'
        return temp      

class 套装效果109(套装):
    名称 = '千蛛碎影'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比三攻加成(0.12)
        属性.黄字 = max(属性.黄字, 0.45)
        if 属性.职业 == '街霸':
            for i in 属性.技能栏:
                if i.是否有伤害 == 1:
                    i.中毒倍率 += 0.3
                    if 属性.角色 == '格斗家(男)':
                        i.感电倍率 += 0.3
                    else:
                        i.涂毒倍率 += 0.3
                    i.出血倍率 += 0.3
                    i.灼伤倍率 += 0.3
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.10
        属性.魔法暴击率 += 0.10
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '中毒、涂毒伤害 +30%<br>'
        temp += '感电伤害 +30%<br>'
        temp += '出血伤害 +30%<br>'
        temp += '灼伤伤害 +30%<br>'
        temp += '百分比三攻 +12%<br>'
        temp += '黄字 +45%(取最高值)<br>'
        temp += '物理暴击率 +10%<br>'
        temp += '魔法暴击率 +10%<br>'
        return temp     

class 套装效果110(套装):
    名称 = '誓血之盟'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        pass
    def 进图属性(self, 属性):
        属性.百分比三攻加成(0.30)
        属性.爆伤 = max(属性.爆伤, 0.20)
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比三攻 +30%<br>'
        temp += '爆伤 +20%(取最高值)<br>'
        return temp    

class 套装效果111(套装):
    名称 = '天御之灾'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        pass
    def 进图属性(self, 属性):
        if 天御套装 == 0:
            属性.所有属性强化加成(10)
            属性.属性附加加成(0.20)
            属性.附加伤害加成(0.09)
        elif 天御套装 == 1:
            属性.所有属性强化加成(50)
            属性.属性附加加成(0.25)
        elif 天御套装 == 2:
            属性.附加伤害加成(0.45)
        pass
    def 其它属性(self, 属性):
        if 天御套装 == 0:
            属性.攻击速度 += 0.04
            属性.移动速度 += 0.04
            属性.释放速度 += 0.05
        elif 天御套装 == 2:
            属性.攻击速度 += 0.20
            属性.移动速度 += 0.20
            属性.释放速度 += 0.25            
        pass
    def 装备描述(self, 属性):
        temp = ''
        if 天御套装 == 0:
            temp += '所有属性强化 +10<br>'
            temp += '属性附加 +20%<br>'
            temp += '附加伤害 +9%<br>'
            temp += '攻击速度 +4%<br>'
            temp += '移动速度 +4%<br>'
            temp += '释放速度 +5%<br>'
        elif 天御套装 == 1:
            temp += '所有属性强化 +50<br>'
            temp += '属性附加 +25%<br>'
        elif 天御套装 == 2:
            temp += '附加伤害 +45%<br>'
            temp += '攻击速度 +20%<br>'
            temp += '移动速度 +20%<br>'
            temp += '释放速度 +25%<br>'
        return temp     

class 套装效果112(套装):
    名称 = '最佳球手的绝杀'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.05)
        pass
    def 进图属性(self, 属性):
        属性.百分比三攻加成(0.40)
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.30
        属性.移动速度 += 0.30
        属性.释放速度 += 0.445
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +5%<br>'
        temp += '百分比三攻 +40%<br>'
        temp += '攻击速度 +30%<br>'
        temp += '移动速度 +30%<br>'
        temp += '释放速度 +44.5%<br>'
        return temp   

class 套装效果113(套装):
    名称 = '战术之王的御敌'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(战术白字)
        pass
    def 进图属性(self, 属性):
        属性.力量 += 620
        属性.智力 += 620
        pass
    def 其它属性(self, 属性):
        属性.攻击速度 += 0.20
        属性.移动速度 += 0.20
        属性.释放速度 += 0.20  
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +' + str(int(战术白字 * 100)) +'%<br>'
        temp += '攻击速度 +20%<br>'
        temp += '移动速度 +20%<br>'
        temp += '释放速度 +20%<br>'
        return temp
    

class 套装效果114(套装):
    名称 = '杀意决'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.12)
        属性.力量 += 150
        属性.智力 += 150
        属性.附加伤害加成(0.35)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +12%<br>'
        temp += '力量 +150<br>'
        temp += '智力 +150<br>'
        temp += '附加伤害 +35%<br>'
        return temp


class 套装效果115(套装):
    名称 = '逝魔之力'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        属性.百分比力智加成(0.18)
        属性.魔法攻击力 += 550
        属性.独立攻击力 += 550
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '百分比力智 +18%<br>'
        temp += '魔法攻击力 +550<br>'
        temp += '独立攻击力 +550<br>'
        return temp
    

class 套装效果116(套装):
    名称 = '天劫'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        pass
    def 进图属性(self, 属性):
        属性.所有属性强化加成(50)
        属性.智力 += 400
        属性.技能攻击力加成(0.18)
        属性.百分比减防 += 0.10 * 天劫减防
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '所有属性强化 +50<br>'
        temp += '智力 +400<br>'
        temp += '技能攻击力 +18%<br>'
        if 天劫减防 == 1:
            temp += '百分比减防 +20%<br>'
            temp += '(BOSS：实际10%)<br>'
        return temp  

class 套装效果117(套装):
    名称 = '冰雪公主的霜语首饰'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.18)
        属性.冰属性强化加成(50)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +18%<br>'
        temp += '冰属性强化 +50<br>'
        return temp  

class 套装效果118(套装):
    名称 = '精炼的异界魔石首饰'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        属性.附加伤害加成(0.20)
        属性.所有属性强化加成(18)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.物理暴击率 += 0.12
        属性.魔法暴击率 += 0.12        
        pass
    def 装备描述(self, 属性):
        temp = ''
        temp += '附加伤害 +20%<br>'
        temp += '所有属性强化 +18<br>'
        temp += '物理暴击率 +12%<br>'
        temp += '魔法暴击率 +12%<br>'
        return temp
#endregion

#region 新增传说两件套 &光环套
class 套装效果119(套装):
    名称 = '维度崩坏'
    件数 = 2
    类型 = '首饰'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·维度冲击臂环'):
            pass
        elif 属性.装备检查('时空：维度冲击臂环'):
            属性.百分比力智加成(0.10)
            属性.附加伤害加成(0.05)
        else:
            属性.百分比力智加成(0.04)
            属性.附加伤害加成(0.04)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·维度冲击臂环'):
            pass
        else:
            属性.物理暴击率 += 0.03
            属性.魔法暴击率 += 0.03
        pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·维度冲击臂环'):
            temp += '无<br>'
        elif 属性.装备检查('时空：维度冲击臂环'):
            temp += '百分比力智 +10%<br>'
            temp += '附加伤害 +5%<br>'
            temp += '物理暴击率 +3%<br>'
            temp += '魔法暴击率 +3%<br>'
        else:
            temp += '百分比力智 +4%<br>'
            temp += '附加伤害 +4%<br>'
            temp += '物理暴击率 +3%<br>'
            temp += '魔法暴击率 +3%<br>'
        return temp   


class 套装效果120(套装):
    名称 = '暗之腐蚀'
    件数 = 2
    类型 = '特殊'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            pass
        elif 属性.装备检查('时空：腐蚀之黑色十字耳环'):
            属性.百分比力智加成(0.10)
            属性.暴击伤害加成(0.05)
        else:
            属性.暴击伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            pass
        else:
            属性.物理暴击率 += 0.04
            属性.魔法暴击率 += 0.04
        pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            temp += '无<br>'
        elif 属性.装备检查('时空：腐蚀之黑色十字耳环'):
            temp += '百分比力智 +10%<br>'
            temp += '暴击伤害 +5%<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        else:
            temp += '暴击伤害 +10%<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        return temp   

class 套装效果121(套装):
    名称 = '先贤的馈赠'
    件数 = 2
    类型 = '首饰'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·先贤的馈赠手镯'):
            pass
        elif 属性.装备检查('时空：先贤的馈赠手镯'):
            属性.百分比力智加成(0.10)
            属性.附加伤害加成(0.05)
        else:
            属性.百分比力智加成(0.04)
            属性.附加伤害加成(0.04)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·先贤的馈赠手镯'):
            pass
        else:
            属性.物理暴击率 += 0.03
            属性.魔法暴击率 += 0.03
        pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·先贤的馈赠手镯'):
            temp += '无<br>'
        elif 属性.装备检查('时空：先贤的馈赠手镯'):
            temp += '百分比力智 +10%<br>'
            temp += '附加伤害 +5%<br>'
            temp += '物理暴击率 +3%<br>'
            temp += '魔法暴击率 +3%<br>'
        else:
            temp += '百分比力智 +4%<br>'
            temp += '附加伤害 +4%<br>'
            temp += '物理暴击率 +3%<br>'
            temp += '魔法暴击率 +3%<br>'
        return temp      

class 套装效果122(套装):
    名称 = '先贤的馈赠'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·先贤的馈赠手镯'):
            属性.力量 += 200
            属性.智力 += 200
            属性.百分比力智加成(0.15)
            属性.附加伤害加成(0.10)
            属性.技能攻击力加成(0.05)
            属性.百分比三攻加成(0.13)
        elif 属性.装备检查('时空：先贤的馈赠手镯'):
            属性.附加伤害加成(0.05)
            属性.技能攻击力加成(0.05)
        else:
            属性.百分比力智加成(0.04)
            属性.附加伤害加成(0.04)
            属性.技能攻击力加成(0.05)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·先贤的馈赠手镯'):
            属性.物理暴击率 += 0.03
            属性.魔法暴击率 += 0.03
        else:
            pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·先贤的馈赠手镯'):
            temp += '力量 +200<br>'
            temp += '智力 +200<br>'
            temp += '百分比力智 +15%<br>'
            temp += '附加伤害 +10%<br>'
            temp += '技能攻击力 +5%<br>'
            temp += '百分比三攻 +13%<br>'
            temp += '物理暴击率 +3%<br>'
            temp += '魔法暴击率 +3%<br>'
        elif 属性.装备检查('时空：先贤的馈赠手镯'):
            temp += '附加伤害 +5%<br>'
            temp += '技能攻击力 +5%<br>'
        else:
            temp += '百分比力智 +4%<br>'
            temp += '附加伤害 +4%<br>'
            temp += '技能攻击力 +5%<br>'
        return temp      

class 套装效果123(套装):
    名称 = '堕落的暗黑之力'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            pass
        elif 属性.装备检查('时空：黑暗幽灵紫杉胸甲'):
            属性.最终伤害加成(0.05)
            属性.附加伤害加成(0.07)
        else:
            属性.百分比三攻加成(0.05)
            属性.附加伤害加成(0.07)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            pass
        else:
            属性.物理暴击率 += 0.04
            属性.魔法暴击率 += 0.04
        pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            temp += '无<br>'
        elif 属性.装备检查('时空：黑暗幽灵紫杉胸甲'):
            temp += '最终伤害 +5%<br>'
            temp += '附加伤害 +7%<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        else:
            temp += '百分比三攻 +5%<br>'
            temp += '附加伤害 +7%<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        return temp

class 套装效果124(套装):
    名称 = '鲜红血纹'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            pass
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            属性.百分比力智加成(0.10)
            属性.所有属性强化加成(25)
        else:
            属性.百分比力智加成(0.05)
            属性.所有属性强化加成(25)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            pass
        else:
            属性.物理暴击率 += 0.04
            属性.魔法暴击率 += 0.04
        pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            temp += '无<br>'
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            temp += '百分比力智 +10%<br>'
            temp += '所有属性强化 +25<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        else:
            temp += '百分比力智 +5%<br>'
            temp += '所有属性强化 +25<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        return temp    

class 套装效果125(套装):
    名称 = '鲜红血纹'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            属性.力量 += 200
            属性.智力 += 200
            属性.附加伤害加成(0.10)
            属性.最终伤害加成(0.10)
            属性.所有属性强化加成(20)
            属性.百分比三攻加成(0.05)
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            属性.附加伤害加成(0.10)
            属性.最终伤害加成(0.08)
            属性.所有属性强化加成(15)
            属性.百分比三攻加成(0.05)
        else:
            属性.附加伤害加成(0.10)
            属性.所有属性强化加成(10)
            属性.百分比三攻加成(0.05)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            pass
        else:
            属性.物理暴击率 += 0.04
            属性.魔法暴击率 += 0.04
        pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            temp += '力量 +200<br>'
            temp += '智力 +200<br>'
            temp += '附加伤害 +10%<br>'
            temp += '最终伤害 +10%<br>'
            temp += '所有属性强化 +20<br>'
            temp += '百分比三攻 +5%<br>'
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            temp += '附加伤害 +10%<br>'
            temp += '最终伤害 +8%<br>'
            temp += '所有属性强化 +15<br>'
            temp += '百分比三攻 +5%<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        else:
            temp += '附加伤害 +10%<br>'
            temp += '所有属性强化 +10<br>'
            temp += '百分比三攻 +5%<br>'
            temp += '物理暴击率 +4%<br>'
            temp += '魔法暴击率 +4%<br>'
        return temp        

class 套装效果126(套装):
    名称 = '鲜红血纹'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            属性.力量 += 200
            属性.智力 += 200
            属性.所有属性强化加成(30)
            属性.最终伤害加成(0.06)
            属性.百分比力智加成(0.10)
            属性.技能攻击力加成(0.16)
            属性.百分比三攻加成(0.15)
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            属性.所有属性强化加成(10)
            属性.最终伤害加成(0.05)
            属性.技能攻击力加成(0.10)
            属性.百分比三攻加成(0.15)
        else:
            属性.所有属性强化加成(15)
            属性.百分比力智加成(0.05)
            属性.百分比三攻加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            属性.物理暴击率 += 0.08
            属性.魔法暴击率 += 0.08
        else:
            pass
    def 装备描述(self, 属性):
        temp = ''
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            temp += '力量 +200<br>'
            temp += '智力 +200<br>'
            temp += '所有属性强化 +30<br>'
            temp += '最终伤害 +6%<br>'
            temp += '百分比力智 +10%<br>'
            temp += '技能攻击力 +16%<br>'
            temp += '百分比三攻 +15%<br>'
            temp += '物理暴击率 +8%<br>'
            temp += '魔法暴击率 +8%<br>'
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            temp += '所有属性强化 +10<br>'
            temp += '最终伤害 +5%<br>'
            temp += '技能攻击力 +10%<br>'
            temp += '百分比三攻 +15%<br>'
        else:
            temp += '所有属性强化 +15<br>'
            temp += '百分比力智 +5%<br>'
            temp += '百分比三攻 +15%<br>'
        return temp    
#endregion