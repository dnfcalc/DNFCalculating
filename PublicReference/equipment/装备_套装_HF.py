from .basic_equ import *

#region  防具套装
class 套装效果0(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.最终伤害加成(0.14)
        self.属性描述 += 属性.技能攻击力加成(0.14)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass   
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=100)
        self.属性描述 += 属性.被动增加(转职被动智力=100)
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=135)

class 套装效果1(套装):
    名称 = '死亡阴影'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.16)
        self.属性描述 += 属性.所有属性强化加成(55)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.10)
        self.属性描述 += 属性.释放速度增加(0.15)
        pass  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=190)
        self.属性描述 += 属性.被动增加(转职被动智力=190)
        self.属性描述 += 属性.觉醒增加(一觉力智=220)

class 套装效果2(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.22)
        if 属性.贫瘠沙漠的遗产 != 0:
            self.属性描述 += 属性.技能攻击力加成(0 + 属性.技能栏空位 / 100)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 1, 30, 1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
        self.属性描述 += 属性.觉醒增加(一觉力智=175)

class 套装效果3(套装):
    名称 = '噩梦：地狱之路'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.16)
        self.属性描述 += 属性.最终伤害加成(0.06)
        self.属性描述 += 属性.技能攻击力加成(0.06)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
        self.属性描述 += 属性.觉醒增加(一觉力智=100)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.04)

class 套装效果4(套装):
    名称 = '永恒不息之路'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.31)
        # self.属性描述 += 属性.技能倍率加成(60, 0.20)
        # self.属性描述 += 属性.技能冷却缩减(60, 60, -0.30)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.12, BUFF智力per=1.12)
        self.属性描述 += 属性.觉醒增加(一觉力智=175)

class 套装效果5(套装):
    名称 = '天堂舞姬'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.17)
        self.属性描述 += 属性.最终伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=105)
        self.属性描述 += 属性.被动增加(转职被动智力=105)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.12, BUFF智力per=1.12)
        self.属性描述 += 属性.觉醒增加(一觉力智=135)

class 套装效果6(套装):
    名称 = '皇家裁决者宣言'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.16)
        self.属性描述 += 属性.所有属性强化加成(52)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.命中率增加(0.05)
        pass   
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.12, BUFF智力per=1.12)
        self.属性描述 += 属性.觉醒增加(一觉力智=220)

class 套装效果7(套装):
    名称 = '炙炎之盛宴'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.18)
        self.属性描述 += 属性.所有属性强化加成(40)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=100)
        self.属性描述 += 属性.被动增加(转职被动智力=100)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=175)

class 套装效果8(套装):
    名称 = '传奇铁匠-封神'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.14)
        self.属性描述 += 属性.最终伤害加成(0.14)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=80)
        self.属性描述 += 属性.被动增加(转职被动智力=80)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
        self.属性描述 += 属性.觉醒增加(一觉力智=120)

class 套装效果9(套装):
    名称 = '命运歧路'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.15)
        self.属性描述 += 属性.附加伤害加成(0.13)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
        self.属性描述 += 属性.觉醒增加(一觉力智=135)

class 套装效果10(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.08)
        self.属性描述 += 属性.伤害增加加成(0.21)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        属性.回避率 += 0.06
        pass     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=3)
        self.属性描述 += 属性.觉醒增加(一觉力智=230)

class 套装效果11(套装):
    名称 = '龙血玄黄'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.23)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.1)
        self.属性描述 += 属性.魔法暴击率增加(0.1)
        pass   
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=100)

class 套装效果12(套装):
    名称 = '擎天战甲'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.最终伤害加成(0.15)
        self.属性描述 += 属性.暴击伤害加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.06, BUFF智力per=1.06)
        self.属性描述 += 属性.觉醒增加(一觉力智=150)

class 套装效果13(套装):
    名称 = '荆棘漫天'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.12)
        self.属性描述 += 属性.暴击伤害加成(0.11)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.10)
        self.属性描述 += 属性.魔法暴击率增加(0.10)
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.12, BUFF智力per=1.12)
        self.属性描述 += 属性.觉醒增加(一觉力智=175)

class 套装效果14(套装):
    名称 = '大自然的呼吸'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.16)
        self.属性描述 += 属性.暴击伤害加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=145)
        self.属性描述 += 属性.被动增加(转职被动智力=145)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.15)
        self.属性描述 += 属性.BUFF增加(BUFF智力per=1.15)
        self.属性描述 += 属性.觉醒增加(一觉力智=60)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)

class 套装效果15(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.22)
        self.属性描述 += 属性.暴击伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=50)
        self.属性描述 += 属性.被动增加(转职被动智力=50)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.24, BUFF智力per=1.24)
        self.属性描述 += 属性.觉醒增加(一觉力智=153)

class 套装效果16(套装):
    名称 = '死亡阴影'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.最终伤害加成(0.14)
        self.属性描述 += 属性.技能攻击力加成(0.16)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=165)
        self.属性描述 += 属性.被动增加(转职被动智力=165)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.25)
        self.属性描述 += 属性.BUFF增加(BUFF智力per=1.25)
        self.属性描述 += 属性.觉醒增加(一觉力智=130)

class 套装效果17(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.15)
        self.属性描述 += 属性.所有属性强化加成(60)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 30, 48, 2)
        self.属性描述 += 属性.被动增加(守护恩赐体精=113)
        self.属性描述 += 属性.被动增加(转职被动智力=113)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.1, BUFF智力per=1.1)
        self.属性描述 += 属性.觉醒增加(一觉力智=150)

class 套装效果18(套装):
    名称 = '噩梦：地狱之路'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.所有属性强化加成(66)
        self.属性描述 += 属性.技能等级加成('所有', 1, 85, 1) 
        self.属性描述 += 属性.技能等级加成('所有', 100, 100, 1) 
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass   
    def 城镇属性_BUFF(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 1, 85, 1)
        self.属性描述 += 属性.技能等级加成('所有', 100, 100, 1)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=110)
        self.属性描述 += 属性.被动增加(转职被动智力=110)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
        self.属性描述 += 属性.觉醒增加(一觉力智=99)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.04)

class 套装效果19(套装):
    名称 = '永恒不息之路'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.最终伤害加成(0.32)
        # self.属性描述 += 属性.技能倍率加成(70, 0.20)
        # self.属性描述 += 属性.技能冷却缩减(70, 70, -0.30)    
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=3)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.15)
        self.属性描述 += 属性.BUFF增加(BUFF智力per=1.15)
        self.属性描述 += 属性.觉醒增加(一觉力智=130)

class 套装效果20(套装):
    名称 = '天堂舞姬'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.11)
        self.属性描述 += 属性.技能攻击力加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.10)
        self.属性描述 += 属性.移动速度增加(0.10)
        self.属性描述 += 属性.释放速度增加(0.15)
        pass    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=145)
        self.属性描述 += 属性.被动增加(转职被动智力=145)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
        self.属性描述 += 属性.觉醒增加(一觉力智=192)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)

class 套装效果21(套装):
    名称 = '皇家裁决者宣言'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.15)
        self.属性描述 += 属性.所有属性强化加成(62)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.05)
        self.属性描述 += 属性.移动速度增加(0.05)
        self.属性描述 += 属性.释放速度增加(0.08)
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=280)
        self.属性描述 += 属性.被动增加(转职被动智力=280)
        self.属性描述 += 属性.BUFF增加(BUFFLv=3)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.2, BUFF智力per=1.2)

class 套装效果22(套装):
    名称 = '炙炎之盛宴'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.附加伤害加成(0.10)
        self.属性描述 += 属性.技能攻击力加成(0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.05)
        self.属性描述 += 属性.魔法暴击率增加(0.05)
        pass  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 1, 48, 2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.25)
        self.属性描述 += 属性.BUFF增加(BUFF智力per=1.25)
        self.属性描述 += 属性.觉醒增加(一觉力智=100)

class 套装效果23(套装):
    名称 = '传奇铁匠-封神'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.21)
        if 属性.装备检查('天堂之翼'):
            self.属性描述 += 属性.技能冷却缩减(1, 45, 0.30)
            self.属性描述 += 属性.技能冷却缩减(60, 80, 0.30)
        else:
            self.属性描述 += 属性.技能冷却缩减(1, 45, 0.20)
            self.属性描述 += 属性.技能冷却缩减(60, 80, 0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass   
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 30, 50, 2)
        self.属性描述 += 属性.被动增加(守护恩赐体精=170)
        self.属性描述 += 属性.被动增加(转职被动智力=170)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.15, BUFF智力per=1.15)

class 套装效果24(套装):
    名称 = '命运歧路'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.12)
        self.属性描述 += 属性.暴击伤害加成(0.17)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.21)
        self.属性描述 += 属性.移动速度增加(0.21)
        self.属性描述 += 属性.释放速度增加(0.315  )
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
        self.属性描述 += 属性.觉醒增加(一觉力智=260)

class 套装效果25(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.08)
        self.属性描述 += 属性.附加伤害加成(0.21)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=125)
        self.属性描述 += 属性.被动增加(转职被动智力=125)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.32, BUFF智力per=1.32)

class 套装效果26(套装):
    名称 = '龙血玄黄'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.24)
        self.属性描述 += 属性.所有属性强化加成(24)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass 
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=70)
        self.属性描述 += 属性.被动增加(转职被动智力=70)
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.09, BUFF智力per=1.09)
        self.属性描述 += 属性.觉醒增加(一觉力智=155)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.02)

class 套装效果27(套装):
    名称 = '擎天战甲'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.32)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass  
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=285)
        self.属性描述 += 属性.被动增加(转职被动智力=285)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.2, BUFF智力per=1.2)
        self.属性描述 += 属性.觉醒增加(一觉Lv=2)

class 套装效果28(套装):
    名称 = '荆棘漫天'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.附加伤害加成(0.25)
        self.属性描述 += 属性.技能冷却缩减(1, 45, 0.15)
        self.属性描述 += 属性.技能冷却缩减(60, 80, 0.15)
        self.属性描述 += 属性.技能冷却缩减(90, 95, 0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=200)
        self.属性描述 += 属性.被动增加(转职被动智力=200)
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.11, BUFF智力per=1.11)
        self.属性描述 += 属性.觉醒增加(一觉力智=130)

class 套装效果29(套装):
    名称 = '大自然的呼吸'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.15)
        self.属性描述 += 属性.技能攻击力加成(0.13)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.05)
        self.属性描述 += 属性.移动速度增加(0.05)
        self.属性描述 += 属性.释放速度增加(0.1)
        pass
          
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.05, BUFF智力per=1.05)
        self.属性描述 += 属性.觉醒增加(一觉力智=248)
    

class 套装效果30(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.19)
        self.属性描述 += 属性.技能等级加成('所有', 1, 85, 2)
        self.属性描述 += 属性.技能等级加成('所有', 100, 100, 2)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.05)
        self.属性描述 += 属性.魔法暴击率增加(0.05)
        pass
       
    def 城镇属性_BUFF(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 1, 85, 2)
        self.属性描述 += 属性.技能等级加成('所有', 100, 100, 2)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.20, BUFF智力per=1.20)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.08)
        self.属性描述 += 属性.被动增加(守护恩赐体精=85, 转职被动智力=85)
  
    

class 套装效果31(套装):
    名称 = '死亡阴影'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.458)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.26, BUFF智力per=1.26)
        self.属性描述 += 属性.觉醒增加(一觉力智=120)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.08)
        self.属性描述 += 属性.技能等级加成('所有', 1, 30, 1)
        self.属性描述 += 属性.被动增加(守护恩赐体精=20, 转职被动智力=20)
    

class 套装效果32(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.44)
        if 属性.贫瘠沙漠的遗产 == 2:
            self.属性描述 += 属性.技能攻击力加成(0.04)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
          
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 30, 50, 2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.31, BUFF智力per=1.31)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.1)
        self.属性描述 += 属性.觉醒增加(一觉力智=15)
    

class 套装效果33(套装):
    名称 = '噩梦：地狱之路'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.46)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
        
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=80, 转职被动智力=80)
        self.属性描述 += 属性.BUFF增加(BUFFLv=3)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.29, BUFF智力per=1.29)
        self.属性描述 += 属性.觉醒增加(一觉力智=190)
    

class 套装效果34(套装):
    名称 = '永恒不息之路'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.22)
        self.属性描述 += 属性.百分比三攻加成(0.23)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.15)
        self.属性描述 += 属性.释放速度增加(0.225)
        pass
           
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.25, BUFF智力per=1.25)
        self.属性描述 += 属性.觉醒增加(一觉力智=150)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.1)
        self.属性描述 += 属性.被动增加(守护恩赐体精=50, 转职被动智力=50)
    

class 套装效果35(套装):
    名称 = '天堂舞姬'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.4)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.10)
        self.属性描述 += 属性.魔法暴击率增加(0.10)
        pass
     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.技能等级加成('所有', 30, 50, 2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.35, BUFF智力per=1.35)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)
        self.属性描述 += 属性.被动增加(守护恩赐体精=100, 转职被动智力=100) 
    

class 套装效果36(套装):
    名称 = '皇家裁决者宣言'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.属性附加加成(0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.11, BUFF智力per=1.11)
        self.属性描述 += 属性.觉醒增加(一觉力智=200)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.1)
        self.属性描述 += 属性.被动增加(守护恩赐体精=110, 转职被动智力=110)
    

class 套装效果37(套装):
    名称 = '炙炎之盛宴'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.最终伤害加成(0.26)
        self.属性描述 += 属性.技能冷却缩减(1, 100, 0.15)
        self.属性描述 += 属性.技能攻击力加成(0.08)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.05)
        self.属性描述 += 属性.攻击速度增加(0.05)
        self.属性描述 += 属性.移动速度增加(0.05)
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.13, BUFF智力per=1.13)
        self.属性描述 += 属性.觉醒增加(一觉力智=170)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.08)
        self.属性描述 += 属性.被动增加(守护恩赐体精=300, 转职被动智力=300)
          

class 套装效果38(套装):
    名称 = '传奇铁匠-封神'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.附加伤害加成(0.17)
        self.属性描述 += 属性.技能攻击力加成(0.20)
        self.属性描述 += 属性.技能冷却缩减(50, 50, 0.30)
        self.属性描述 += 属性.技能冷却缩减(85, 85, 0.30)
        self.属性描述 += 属性.技能冷却缩减(100, 100, 0.17)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.15)
        self.属性描述 += 属性.移动速度增加(0.15)
        self.属性描述 += 属性.释放速度增加(0.20)
        pass
        
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 30, 48, 2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.18, BUFF智力per=1.18)
        self.属性描述 += 属性.觉醒增加(一觉力智=130)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.08)
    

class 套装效果39(套装):
    名称 = '命运歧路'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.12)
        self.属性描述 += 属性.技能攻击力加成(0.27)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):      
        self.属性描述 += 属性.BUFF增加(BUFFLv=3)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.3, BUFF智力per=1.3)
        self.属性描述 += 属性.觉醒增加(一觉力智=90)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.07)
        self.属性描述 += 属性.被动增加(守护恩赐体精=50, 转职被动智力=50)
    

class 套装效果40(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        # self.属性描述 += 属性.暴击伤害加成(0.21)
        self.属性描述 += 属性.技能攻击力加成(0.45)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
         
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性): 
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.15,BUFF智力per=1.15) 
        self.属性描述 += 属性.被动增加(守护恩赐体精=75,转职被动智力=75)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.02)
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.觉醒增加(一觉力智=305)
    

class 套装效果41(套装):
    名称 = '龙血玄黄'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.12)
        if 属性.角色熟练度 == 0 or 属性.装备检查('战无不胜上衣'):
            self.属性描述 += 属性.附加伤害加成(0.29)
        else:
            self.属性描述 += 属性.附加伤害加成(0.28)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.15)
        self.属性描述 += 属性.移动速度增加(0.15)
        self.属性描述 += 属性.释放速度增加(0.225)
        pass
     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.27, BUFF智力per=1.27)
        self.属性描述 += 属性.觉醒增加(一觉力智=120)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.06)
    

class 套装效果42(套装):
    名称 = '擎天战甲'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.属性附加加成(0.12)
        self.属性描述 += 属性.技能攻击力加成(0.1)
        # if 属性.擎天战甲 == 0:
        #     self.属性描述 += 属性.技能攻击力加成(0.05)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.擎天战甲 == 0:
            self.属性描述 += 属性.攻击速度增加(0.2)
            self.属性描述 += 属性.移动速度增加(0.2)
            self.属性描述 += 属性.释放速度增加(0.3)
        pass
          
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):  
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.21, BUFF智力per=1.21)
        self.属性描述 += 属性.觉醒增加(一觉力智=50)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.1)
        self.属性描述 += 属性.技能等级加成('所有', 1, 50, 2)
    

class 套装效果43(套装):
    名称 = '荆棘漫天'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.10)
        self.属性描述 += 属性.技能攻击力加成(0.32)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.1)
        self.属性描述 += 属性.移动速度增加(-0.02 + 0.05)
        self.属性描述 += 属性.释放速度增加(0.1 + 0.12)
        pass
           
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):   
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.29, BUFF智力per=1.29)
        self.属性描述 += 属性.觉醒增加(一觉力智=170)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.08)
    

class 套装效果44(套装):
    名称 = '大自然的呼吸'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.最终伤害加成(0.11)
        self.属性描述 += 属性.技能攻击力加成(0.10)
        self.属性描述 += 属性.所有属性强化加成(64)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.10)
        self.属性描述 += 属性.魔法暴击率增加(0.10)
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.33)
        self.属性描述 += 属性.BUFF增加(BUFF智力per=1.33)
        self.属性描述 += 属性.觉醒增加(一觉力智=150)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.04)
    

#endregion

#region  散搭套装
class 套装效果45(套装):
    名称 = '深渊窥视者'
    件数 = 2
    类型 = '上链左'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.09)
        pass
    def 进图属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 1, 48, 2)
        pass
    def 其它属性(self, 属性):
        pass
        
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 1, 48, 2)
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.02)
    

class 套装效果46(套装):
    名称 = '圣者的黄昏'
    件数 = 2
    类型 = '上链左'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.11)
        self.属性描述 += 属性.附加伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.移动速度增加(0.05)
        pass
         
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
    

class 套装效果47(套装):
    名称 = '坎坷命运'
    件数 = 2
    类型 = '上链左'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.14)
        self.属性描述 += 属性.技能攻击力加成(0.09)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.03)
        self.属性描述 += 属性.移动速度增加(0.03)
        self.属性描述 += 属性.释放速度增加(0.045)
        if 属性.装备检查('地狱边缘'):
            属性.攻击速度 -= 0.01
            属性.移动速度 -= 0.01
            属性.释放速度 -= 0.015
        pass
        
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)
        self.属性描述 += 属性.觉醒增加(一觉力智=45)
    

class 套装效果48(套装):
    名称 = '吞噬愤怒'
    件数 = 2
    类型 = '上链左'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.10)
        self.属性描述 += 属性.暴击伤害加成(0.11)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('灭世之怒'):
            self.属性描述 += 属性.攻击速度增加(0.15)
            self.属性描述 += 属性.移动速度增加(0.15)
            self.属性描述 += 属性.释放速度增加(0.225)
        else:
            self.属性描述 += 属性.攻击速度增加(0.10)
            self.属性描述 += 属性.移动速度增加(0.10)
            self.属性描述 += 属性.释放速度增加(0.15)
        pass
       
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=25)
    

class 套装效果49(套装):
    名称 = '黑魔法探求者'
    件数 = 2
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.12)
        self.属性描述 += 属性.技能攻击力加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
            
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=48)
    

class 套装效果50(套装):
    名称 = '时空旅行者'
    件数 = 2
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.10)
        self.属性描述 += 属性.最终伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=4)
        self.属性描述 += 属性.被动增加(转职被动智力=14)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
    

class 套装效果51(套装):
    名称 = '穿透命运的呐喊'
    件数 = 2
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.23)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
        
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=25)
    

class 套装效果52(套装):
    名称 = '狂乱追随者'
    件数 = 2
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.18)
        self.属性描述 += 属性.所有属性强化加成(25)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.15)
        self.属性描述 += 属性.释放速度增加(0.225)
        pass
      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=25)
    

class 套装效果53(套装):
    名称 = '地狱求道者'
    件数 = 2
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.附加伤害加成(0.10)
        self.属性描述 += 属性.最终伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
     
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=32)
    


class 套装效果54(套装):
    名称 = '次元旅行者'
    件数 = 2
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.附加伤害加成(0.22)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.10)
        self.属性描述 += 属性.魔法暴击率增加(0.10)
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=40)
        self.属性描述 += 属性.被动增加(转职被动智力=60)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=42)
    

class 套装效果55(套装):
    名称 = '天命无常'
    件数 = 2
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.伤害增加加成(0.07)
        self.属性描述 += 属性.附加伤害加成(0.08)
        self.属性描述 += 属性.技能攻击力加成(0.05)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.天命无常 == 0:
            if 属性.装备检查('命运反抗者'):
                self.属性描述 += 属性.移动速度增加(0.08)
                self.属性描述 += 属性.攻击速度增加(0.08)
                self.属性描述 += 属性.释放速度增加(0.12)
            else:
                self.属性描述 += 属性.移动速度增加(0.07)
                self.属性描述 += 属性.攻击速度增加(0.07)
                self.属性描述 += 属性.释放速度增加(0.105)
        else:
            self.属性描述 += 属性.移动速度增加(0.02 * 属性.天命无常)
            self.属性描述 += 属性.攻击速度增加(0.02 * 属性.天命无常)
            self.属性描述 += 属性.释放速度增加(0.03 * 属性.天命无常)
        pass
         
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 30, 48, 1)
        self.属性描述 += 属性.觉醒增加(一觉力智=45)
    

class 套装效果56(套装):
    名称 = '悲剧的残骸'
    件数 = 2
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.最终伤害加成(0.23)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=25)
         

class 套装效果57(套装):
    名称 = '深渊窥视者'
    件数 = 3
    类型 = '上链左'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.13)
        pass
    def 进图属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 60, 80, 2)
        self.属性描述 += 属性.技能等级加成('所有', 50, 50, 1)
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 1)
        self.属性描述 += 属性.技能等级加成('所有', 100, 100, 1)
        pass
    def 其它属性(self, 属性):
        pass
           
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 60, 80, 2)
        self.属性描述 += 属性.技能等级加成('所有', 50, 50, 1)
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 1)
        self.属性描述 += 属性.技能等级加成('所有', 100, 100, 1)
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=163)
        self.属性描述 += 属性.被动增加(转职被动智力=198)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.06, BUFF智力per=1.06)
        self.属性描述 += 属性.觉醒增加(一觉力智=140)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.03)
    

class 套装效果58(套装):
    名称 = '圣者的黄昏'
    件数 = 3
    类型 = '上链左'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.05)
        self.属性描述 += 属性.技能攻击力加成(0.12)
        self.属性描述 += 属性.所有属性强化加成(32)
        self.属性描述 += 属性.技能冷却缩减(1, 45, 0.10)
        self.属性描述 += 属性.技能冷却缩减(60, 80, 0.10)
        self.属性描述 += 属性.技能冷却缩减(90, 95, 0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.移动速度增加(0.05)
        self.属性描述 += 属性.物理暴击率增加(0.15)
        self.属性描述 += 属性.魔法暴击率增加(0.15)
        pass
          
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=225)
        self.属性描述 += 属性.被动增加(转职被动智力=258)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.12, BUFF智力per=1.12)
        self.属性描述 += 属性.觉醒增加(一觉力智=165)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.03)
    

class 套装效果59(套装):
    名称 = '坎坷命运'
    件数 = 3
    类型 = '上链左'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.21)
        self.属性描述 += 属性.技能攻击力加成(0.1)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.03)
        self.属性描述 += 属性.移动速度增加(0.03)
        self.属性描述 += 属性.释放速度增加(0.045)
        if 属性.装备检查('地狱边缘'):
            属性.攻击速度 -= 0.01
            属性.移动速度 -= 0.01
            属性.释放速度 -= 0.015
        pass
         
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=236)
        self.属性描述 += 属性.被动增加(转职被动智力=255)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.06, BUFF智力per=1.06)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=135)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)
    

class 套装效果60(套装):
    名称 = '吞噬愤怒'
    件数 = 3
    类型 = '上链左'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.30)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
         
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=236)
        self.属性描述 += 属性.被动增加(转职被动智力=255)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.1, BUFF智力per=1.1)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=124)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.04)
    

class 套装效果61(套装):
    名称 = '黑魔法探求者'
    件数 = 3
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.属性附加加成(0.13)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.10)
        self.属性描述 += 属性.魔法暴击率增加(0.1)
        pass
           
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=38)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.06)
    

class 套装效果62(套装):
    名称 = '时空旅行者'
    件数 = 3
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.17)
        self.属性描述 += 属性.技能攻击力加成(0.14)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
        
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.1, BUFF智力per=1.1)
        self.属性描述 += 属性.觉醒增加(一觉力智=45)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)
    

class 套装效果63(套装):
    名称 = '穿透命运的呐喊'
    件数 = 3
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.17)
        self.属性描述 += 属性.技能攻击力加成(0.19)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 30, 50, 2)
        self.属性描述 += 属性.被动增加(守护恩赐体精=44)
        self.属性描述 += 属性.被动增加(转职被动智力=36)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.06, BUFF智力per=1.06)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.04)
    

class 套装效果64(套装):
    名称 = '狂乱追随者'
    件数 = 3
    类型 = '镯下右'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.16)
        self.属性描述 += 属性.技能攻击力加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
         
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=29)
        self.属性描述 += 属性.被动增加(转职被动智力=31)
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.1, BUFF智力per=1.1)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=85)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.04)
    

class 套装效果65(套装):
    名称 = '地狱求道者'
    件数 = 3
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.16)
        pass
    def 进图属性(self, 属性):
        self.属性描述 += 属性.所有属性强化加成(40)
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.15)
        self.属性描述 += 属性.移动速度增加(0.15)
        self.属性描述 += 属性.释放速度增加(0.20)
        pass
    
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=195)
        self.属性描述 += 属性.被动增加(转职被动智力=188)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.06, BUFF智力per=1.06)
        self.属性描述 += 属性.觉醒增加(一觉力智=50)
        self.属性描述 += 属性.觉醒增加(一觉Lv=2)
    
class 套装效果66(套装):
    名称 = '次元旅行者'
    件数 = 3
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.10)
        self.属性描述 += 属性.技能攻击力加成(0.18)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
         
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=80)
        self.属性描述 += 属性.被动增加(转职被动智力=120)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.12, BUFF智力per=1.12)
        self.属性描述 += 属性.觉醒增加(一觉力智=105)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
           
class 套装效果67(套装):
    名称 = '天命无常'
    件数 = 3
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.附加伤害加成(0.10)
        self.属性描述 += 属性.技能攻击力加成(0.08)
        self.属性描述 += 属性.百分比力智加成(0.07)
        if 属性.天命无常 == 0:
            if 属性.装备检查('命运反抗者'):
                self.属性描述 += 属性.百分比力智加成(0.052)
            else:
                self.属性描述 += 属性.百分比力智加成(0.046666667)
        if 属性.天命无常 == 1 or 属性.天命无常 == 2 or 属性.天命无常 == 3:
            self.属性描述 += 属性.百分比力智加成(0.02)
        if 属性.天命无常 == 4 or 属性.天命无常 == 5:
            self.属性描述 += 属性.百分比力智加成(0.05)
        if 属性.天命无常 == 6:
            self.属性描述 += 属性.百分比力智加成(0.12)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.天命无常 == 0:
            if 属性.装备检查('命运反抗者'):
                self.属性描述 += 属性.移动速度增加(0.066)
                self.属性描述 += 属性.攻击速度增加(0.066)
            else:
                self.属性描述 += 属性.移动速度增加(0.055)
                self.属性描述 += 属性.攻击速度增加(0.055 )
        if 属性.天命无常 >= 4:
            self.属性描述 += 属性.移动速度增加(0.03 * 属性.天命无常)
            self.属性描述 += 属性.攻击速度增加(0.03 * 属性.天命无常)
        pass
         
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 30, 50, 2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.11, BUFF智力per=1.11)
        self.属性描述 += 属性.觉醒增加(一觉力智=116)
    
class 套装效果68(套装):
    名称 = '悲剧的残骸'
    件数 = 3
    类型 = '环鞋指'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.29)
        self.属性描述 += 属性.技能攻击力加成(0.1)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=153)
        self.属性描述 += 属性.被动增加(转职被动智力=140)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.12, BUFF智力per=1.12)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=110)
    
#endregion

#region  首饰套装
class 套装效果69(套装):
    名称 = '上古尘封术士'
    件数 = 2
    类型 = '首饰'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.10)
        self.属性描述 += 属性.百分比三攻加成(0.14)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
       
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=60)
        self.属性描述 += 属性.被动增加(转职被动智力=60)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)
        self.属性描述 += 属性.觉醒增加(一觉力智=45)
    
class 套装效果70(套装):
    名称 = '破晓曦光'
    件数 = 2
    类型 = '首饰'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.10)
        self.属性描述 += 属性.最终伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.05)
        self.属性描述 += 属性.魔法暴击率增加(0.05)
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.03, BUFF智力per=1.03)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
    

class 套装效果71(套装):
    名称 = '幸运三角'
    件数 = 2
    类型 = '首饰'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.所有属性强化加成(77)
        self.属性描述 += 属性.三攻固定加成(77)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.07)
        self.属性描述 += 属性.魔法暴击率增加(0.07)
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=140)
        self.属性描述 += 属性.被动增加(转职被动智力=140)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.04)
        self.属性描述 += 属性.BUFF增加(BUFF智力per=1.04)
        self.属性描述 += 属性.觉醒增加(一觉力智=45)
        

class 套装效果72(套装):
    名称 = '精灵使的权能'
    件数 = 2
    类型 = '首饰'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.10)
        self.属性描述 += 属性.技能攻击力加成(0.12)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
       
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=100)
        self.属性描述 += 属性.被动增加(转职被动智力=110)
        self.属性描述 += 属性.觉醒增加(一觉力智=20)
    

class 套装效果73(套装):
    名称 = '上古尘封术士'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉Lv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)
        self.属性描述 += 属性.觉醒增加(一觉力智=8)
    

class 套装效果74(套装):
    名称 = '破晓曦光'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.属性附加加成(0.10)
        self.属性描述 += 属性.技能等级加成('所有', 100, 100, 1)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.10)
        self.属性描述 += 属性.移动速度增加(0.10)
        self.属性描述 += 属性.释放速度增加(0.15)
        pass
        
    def 城镇属性_BUFF(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 100, 100, 1)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=20)
        self.属性描述 += 属性.被动增加(转职被动智力=20)
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.03)
        self.属性描述 += 属性.BUFF增加(BUFF智力per=1.03)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=45)
    

class 套装效果75(套装):
    名称 = '幸运三角'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        if 属性.幸运三角 == 0:
            self.属性描述 += 属性.技能攻击力加成(0.2915)
        elif 属性.幸运三角 == 1:
           self.属性描述 += 属性.技能攻击力加成(0.27)
        elif 属性.幸运三角 == 2:
            self.属性描述 += 属性.技能攻击力加成(0.31)
        elif 属性.幸运三角 == 3:
            self.属性描述 += 属性.技能攻击力加成(0.34)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.幸运三角 == 0:
            self.属性描述 += 属性.攻击速度增加(0.005)
            self.属性描述 += 属性.移动速度增加(0.005)
            self.属性描述 += 属性.释放速度增加(0.0075)
        if 属性.幸运三角 == 3:
            self.属性描述 += 属性.攻击速度增加(0.10)
            self.属性描述 += 属性.移动速度增加(0.10)
            self.属性描述 += 属性.释放速度增加(0.15)
        pass
           
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉Lv=2)
        self.属性描述 += 属性.觉醒增加(一觉力智=8)
    

class 套装效果76(套装):
    名称 = '精灵使的权能'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.15)
        self.属性描述 += 属性.技能冷却缩减(1, 100, 0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.05)
        self.属性描述 += 属性.魔法暴击率增加(0.05)
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.04, BUFF智力per=1.04)
        self.属性描述 += 属性.觉醒增加(一觉Lv=2)
        self.属性描述 += 属性.觉醒增加(一觉力智=26)
    
#endregion

#region  特殊套装
class 套装效果77(套装):
    名称 = '军神的隐秘遗产'
    件数 = 2
    类型 = '特殊'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.10)
        self.属性描述 += 属性.最终伤害加成(0.08)
        if 属性.装备检查('军神的遗书'):
            if 属性.装备检查('军神的心之所念'):
                self.属性描述 += 属性.暴击伤害加成(0.05)
            if 属性.装备检查('军神的古怪耳环'):
                self.属性描述 += 属性.暴击伤害加成(0.05)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('军神的遗书'):
            if 属性.装备检查('军神的心之所念'):
                self.属性描述 += 属性.攻击速度增加(0.05)
                self.属性描述 += 属性.移动速度增加(0.10)
                self.属性描述 += 属性.释放速度增加(0.075)
            if 属性.装备检查('军神的古怪耳环'):
                self.属性描述 += 属性.移动速度增加(0.05)
        pass
         
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=230)
        self.属性描述 += 属性.被动增加(转职被动智力=205)
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.04)
        self.属性描述 += 属性.BUFF增加(BUFF智力per=1.04)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=35)
    

class 套装效果78(套装):
    名称 = '时间战争的残骸'
    件数 = 2
    类型 = '特殊'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.11)
        self.属性描述 += 属性.暴击伤害加成(0.11)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
        
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 1, 30, 2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)
        self.属性描述 += 属性.觉醒增加(一觉力智=35)
    

class 套装效果79(套装):
    名称 = '灵宝：世间真理'
    件数 = 2
    类型 = '特殊'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.附加伤害加成(0.15)
        self.属性描述 += 属性.技能攻击力加成(0.07)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 30, 50, 1)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)

class 套装效果80(套装):
    名称 = '能量主宰'
    件数 = 2
    类型 = '特殊'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.12)
        self.属性描述 += 属性.伤害增加加成(0.12)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        pass
      
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=95)
        self.属性描述 += 属性.被动增加(转职被动智力=95)
        self.属性描述 += 属性.BUFF增加(BUFFLv=2)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=35)
    

class 套装效果81(套装):
    名称 = '军神的隐秘遗产'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.技能攻击力加成(0.10)
        if 属性.军神的隐秘遗产 == 0:
            self.属性描述 += 属性.百分比力智加成(0.10)
        if 属性.军神的隐秘遗产 == 1:
            self.属性描述 += 属性.百分比力智加成(0.10)
        if 属性.军神的隐秘遗产 == 2:
            self.属性描述 += 属性.百分比力智加成(0.08)
        if 属性.军神的隐秘遗产 == 3:
            self.属性描述 += 属性.百分比力智加成(0.06)
        if 属性.军神的隐秘遗产 == 4:
            self.属性描述 += 属性.百分比力智加成(0.04)
        if 属性.军神的隐秘遗产 == 5:
            self.属性描述 += 属性.百分比力智加成(0.02)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.军神的隐秘遗产 == 0:
            self.属性描述 += 属性.攻击速度增加(0.10)
            self.属性描述 += 属性.释放速度增加(0.15)
        pass
          
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉Lv=2)
    

class 套装效果82(套装):
    名称 = '时间战争的残骸'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.10)
        self.属性描述 += 属性.技能攻击力加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.05)
        self.属性描述 += 属性.魔法暴击率增加(0.05)
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=12)
        self.属性描述 += 属性.被动增加(转职被动智力=22)
        self.属性描述 += 属性.被动增加(一觉被动Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉Lv=3)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)
          

class 套装效果83(套装):
    名称 = '灵宝：世间真理'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.暴击伤害加成(0.12)
        pass
    def 进图属性(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 1, 85, 1)
        self.属性描述 += 属性.技能等级加成('所有', 100, 100, 1)
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.10)
        self.属性描述 += 属性.移动速度增加(0.10)
        self.属性描述 += 属性.释放速度增加(0.15)
        self.属性描述 += 属性.物理暴击率增加(0.05)
        self.属性描述 += 属性.魔法暴击率增加(0.05)
        pass
       
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        self.属性描述 += 属性.技能等级加成('所有', 1, 85, 1)
        self.属性描述 += 属性.技能等级加成('所有', 100, 100, 1)
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=47)
        self.属性描述 += 属性.被动增加(转职被动智力=69)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=39)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)
    

class 套装效果84(套装):
    名称 = '能量主宰'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.附加伤害加成(0.10)
        self.属性描述 += 属性.技能攻击力加成(0.08)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.10)
        self.属性描述 += 属性.魔法暴击率增加(0.10)
        pass
    
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.被动增加(守护恩赐体精=48)
        self.属性描述 += 属性.被动增加(转职被动智力=48)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.03, BUFF智力per=1.03)
        self.属性描述 += 属性.觉醒增加(一觉Lv=2)
    
#endregion




#region  其它套装
class 套装效果85(套装):
    名称 = '超界·苍穹之云'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.百分比力智加成(0.10)
        self.属性描述 += 属性.伤害增加加成(0.13)
        self.属性描述 += 属性.技能等级加成('所有', 50, 50, 2)
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 2)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.05)
        self.属性描述 += 属性.释放速度增加(0.075)
        self.属性描述 += 属性.移动速度增加(0.05)
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
        self.属性描述 += 属性.技能等级加成('所有', 50, 50, 2)
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 2)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=6)
        self.属性描述 += 属性.觉醒增加(一觉力智=41)
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
        self.属性描述 += 属性.暴击伤害加成(0.36)
        self.属性描述 += 属性.技能等级加成('所有', 50, 50, 2)
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 2)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.17)
        self.属性描述 += 属性.释放速度增加(0.255)
        self.属性描述 += 属性.移动速度增加(0.17)
        self.属性描述 += 属性.物理暴击率增加(0.05)
        self.属性描述 += 属性.魔法暴击率增加(0.05)
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
        self.属性描述 += 属性.技能等级加成('所有', 50, 50, 2)
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 2)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.23, BUFF智力per=1.23)
        
  
        self.属性描述 += 属性.觉醒增加(一觉力智=142)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)
        self.属性描述 += 属性.被动增加(守护恩赐体精=40)
        self.属性描述 += 属性.被动增加(转职被动智力=220)
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
        self.属性描述 += 属性.技能攻击力加成(0.12)
        self.属性描述 += 属性.最终伤害加成(0.25)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.10)
        self.属性描述 += 属性.魔法暴击率增加(0.10)
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
        self.属性描述 += 属性.BUFF增加(BUFFLv=3)
        self.属性描述 += 属性.觉醒增加(一觉力智=98)
        self.属性描述 += 属性.被动增加(守护恩赐体精=120)
        self.属性描述 += 属性.被动增加(转职被动智力=120)
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
        self.属性描述 += 属性.附加伤害加成(0.48)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.17)
        self.属性描述 += 属性.释放速度增加(0.255)
        self.属性描述 += 属性.移动速度增加(0.17)
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
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.23, BUFF智力per=1.23)
        
  
        self.属性描述 += 属性.觉醒增加(一觉力智=232)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)
        self.属性描述 += 属性.被动增加(守护恩赐体精=220)
        self.属性描述 += 属性.被动增加(转职被动智力=220)
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
        self.属性描述 += 属性.技能等级加成('所有', 50, 50, 2)
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 1)
        self.属性描述 += 属性.最终伤害加成(0.25)
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
        self.属性描述 += 属性.技能等级加成('所有', 50, 50, 2)
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 1)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFFLv=6)
        self.属性描述 += 属性.觉醒增加(一觉力智=20)
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
        self.属性描述 += 属性.属性附加加成(0.35)
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 1)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.10)
        self.属性描述 += 属性.释放速度增加(0.15)
        self.属性描述 += 属性.移动速度增加(0.10)
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
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 1)
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.23, BUFF智力per=1.23)
        
  
        self.属性描述 += 属性.觉醒增加(一觉力智=163)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)
        self.属性描述 += 属性.被动增加(守护恩赐体精=340)
        self.属性描述 += 属性.被动增加(转职被动智力=520)
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
        self.属性描述 += 属性.百分比力智加成(0.35)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.06)
        self.属性描述 += 属性.释放速度增加(0.09)
        self.属性描述 += 属性.移动速度增加(0.06)
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
        self.属性描述 += 属性.BUFF增加(BUFFLv=6)
        self.属性描述 += 属性.觉醒增加(一觉力智=150)
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
        self.属性描述 += 属性.百分比三攻加成(0.45)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.06)
        self.属性描述 += 属性.释放速度增加(0.09)
        self.属性描述 += 属性.移动速度增加(0.06)
        self.属性描述 += 属性.物理暴击率增加(0.10)
        self.属性描述 += 属性.魔法暴击率增加(0.10)
        self.属性描述 += 属性.移动速度增加(0.10)
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
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.23, BUFF智力per=1.23)
        
  
        self.属性描述 += 属性.觉醒增加(一觉力智=225)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)
        self.属性描述 += 属性.被动增加(守护恩赐体精=220)
        self.属性描述 += 属性.被动增加(转职被动智力=220)
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
        self.属性描述 += 属性.所有属性强化加成(25)
        self.属性描述 += 属性.最终伤害加成(0.25)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.10)
        self.属性描述 += 属性.魔法暴击率增加(0.10)
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
        self.属性描述 += 属性.BUFF增加(BUFFLv=6)
        self.属性描述 += 属性.觉醒增加(一觉力智=150)
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
        self.属性描述 += 属性.属性附加加成(0.35)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.10)
        self.属性描述 += 属性.释放速度增加(0.15)
        self.属性描述 += 属性.移动速度增加(0.10)
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
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.23, BUFF智力per=1.23)
        
  
        self.属性描述 += 属性.觉醒增加(一觉力智=225)
        self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)
        self.属性描述 += 属性.被动增加(守护恩赐体精=220)
        self.属性描述 += 属性.被动增加(转职被动智力=220)
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
        self.属性描述 += 属性.附加伤害加成(0.12)
        self.属性描述 += 属性.百分比力智加成(0.12)
        self.属性描述 += 属性.技能攻击力加成(0.08)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.05)
        self.属性描述 += 属性.释放速度增加(0.075)
        self.属性描述 += 属性.移动速度增加(0.05)
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
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉Lv=1)
        self.属性描述 += 属性.觉醒增加(一觉力智=26)
        self.属性描述 += 属性.被动增加(守护恩赐体精=160)
        self.属性描述 += 属性.被动增加(转职被动智力=160)
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
        self.属性描述 += 属性.暴击伤害加成(0.10)
        self.属性描述 += 属性.百分比力智加成(0.08)
        self.属性描述 += 属性.技能攻击力加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.05)
        self.属性描述 += 属性.释放速度增加(0.075)
        self.属性描述 += 属性.移动速度增加(0.05)
        self.属性描述 += 属性.物理暴击率增加(0.05)
        self.属性描述 += 属性.魔法暴击率增加(0.05)
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
        self.属性描述 += 属性.BUFF增加(BUFFLv=1)
        self.属性描述 += 属性.觉醒增加(一觉Lv=2)
        self.属性描述 += 属性.觉醒增加(一觉力智=26)
        self.属性描述 += 属性.BUFF增加(BUFF力量per=1.03, BUFF智力per=1.03)
        self.属性描述 += 属性.被动增加(守护恩赐体精=247)
        self.属性描述 += 属性.被动增加(转职被动智力=209)
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
            self.属性描述 += 属性.百分比力智加成(0.15)
            self.属性描述 += 属性.附加伤害加成(0.10)
            self.属性描述 += 属性.暴击伤害加成(0.10)
            self.属性描述 += 属性.百分比三攻加成(0.13)
        elif 属性.装备检查('时空：维度冲击臂环'):
            self.属性描述 += 属性.附加伤害加成(0.05)
            self.属性描述 += 属性.暴击伤害加成(0.15)
        else:
            self.属性描述 += 属性.百分比力智加成(0.04)
            self.属性描述 += 属性.附加伤害加成(0.04)
            self.属性描述 += 属性.技能攻击力加成(0.08)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·维度冲击臂环'):
            self.属性描述 += 属性.物理暴击率增加(0.03)
            self.属性描述 += 属性.魔法暴击率增加(0.03)
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
            self.属性描述 += 属性.BUFF增加(BUFFLv=1)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.被动增加(守护恩赐体精=76)
            self.属性描述 += 属性.被动增加(转职被动智力=76)
        elif 属性.装备检查('时空·维度冲击臂环'):
            self.属性描述 += 属性.BUFF增加(BUFFLv=1)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.被动增加(一觉被动Lv=2)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)
            self.属性描述 += 属性.BUFF增加(BUFF物攻per=1.02)
        else:
            属性.智力 += 200
            self.属性描述 += 属性.BUFF增加(BUFFLv=1)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.被动增加(一觉被动Lv=2)
            self.属性描述 += 属性.觉醒增加(一觉力智=46)
            self.属性描述 += 属性.被动增加(守护恩赐体精=271)
            self.属性描述 += 属性.被动增加(转职被动智力=71)
            self.属性描述 += 属性.BUFF增加(BUFF物攻per=1.03)
    
class 套装效果98(套装):
    名称 = '暗之腐蚀'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            属性.力量 += 200
            属性.智力 += 200
            self.属性描述 += 属性.百分比力智加成(0.05)
            self.属性描述 += 属性.附加伤害加成(0.16)
            self.属性描述 += 属性.暴击伤害加成(0.23)
            self.属性描述 += 属性.技能攻击力加成(0.05)
        elif 属性.装备检查('时空：腐蚀之黑色十字耳环'):
            self.属性描述 += 属性.附加伤害加成(0.13)
            self.属性描述 += 属性.暴击伤害加成(0.05)
            self.属性描述 += 属性.技能攻击力加成(0.05)
        else:
            self.属性描述 += 属性.百分比力智加成(0.05)
            self.属性描述 += 属性.技能攻击力加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            self.属性描述 += 属性.物理暴击率增加(0.04)
            self.属性描述 += 属性.魔法暴击率增加(0.04)
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
            self.属性描述 += 属性.觉醒增加(一觉Lv=2)
            self.属性描述 += 属性.觉醒增加(一觉力智per=1.03)
            self.属性描述 += 属性.被动增加(守护恩赐体精=127)
            self.属性描述 += 属性.被动增加(转职被动智力=109)
        elif 属性.装备检查('时空·腐蚀之黑色十字耳环'):
            self.属性描述 += 属性.BUFF增加(BUFFLv=1)
            self.属性描述 += 属性.觉醒增加(一觉Lv=2)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.03, BUFF智力per=1.03)
            self.属性描述 += 属性.BUFF增加(BUFF魔攻per=1.02)
            self.属性描述 += 属性.BUFF增加(BUFF独立per=1.02)
            self.属性描述 += 属性.觉醒增加(一觉力智=30)
            self.属性描述 += 属性.被动增加(守护恩赐体精=127)
            self.属性描述 += 属性.被动增加(转职被动智力=109)
        else:
            self.属性描述 += 属性.力智固定加成(200)
            self.属性描述 += 属性.BUFF增加(BUFFLv=1)
            self.属性描述 += 属性.觉醒增加(一觉Lv=2)
            self.属性描述 += 属性.技能等级加成('所有', 1, 48, 1)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.03, BUFF智力per=1.03)
            self.属性描述 += 属性.BUFF增加(BUFF魔攻per=1.03)
            self.属性描述 += 属性.BUFF增加(BUFF独立per=1.03)
            self.属性描述 += 属性.觉醒增加(一觉力智=50)
            self.属性描述 += 属性.被动增加(守护恩赐体精=252)
            self.属性描述 += 属性.被动增加(转职被动智力=14)

class 套装效果99(套装):
    名称 = '堕落的暗黑之力'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            属性.力量 += 200
            属性.智力 += 200
            self.属性描述 += 属性.百分比三攻加成(0.12)
            self.属性描述 += 属性.伤害增加加成(0.10)
            self.属性描述 += 属性.暴击伤害加成(0.10)
            self.属性描述 += 属性.最终伤害加成(0.05)
        elif 属性.装备检查('时空：黑暗幽灵紫杉胸甲'):
            self.属性描述 += 属性.百分比三攻加成(0.06)
            self.属性描述 += 属性.伤害增加加成(0.10)
            self.属性描述 += 属性.暴击伤害加成(0.10)
        else:
            self.属性描述 += 属性.伤害增加加成(0.10)
            self.属性描述 += 属性.暴击伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            pass
        else:
            self.属性描述 += 属性.物理暴击率增加(0.04)
            self.属性描述 += 属性.魔法暴击率增加(0.04)
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
            self.属性描述 += 属性.力智固定加成(200)
            self.属性描述 += 属性.BUFF增加(BUFFLv=6)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.觉醒增加(一觉力智=80)
            self.属性描述 += 属性.被动增加(守护恩赐体精=200)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
            self.属性描述 += 属性.BUFF增加(BUFF物攻per=1.04, BUFF魔攻per=1.04, BUFF独立per=1.04)
        elif 属性.装备检查('时空·黑暗幽灵紫杉胸甲'):
            self.属性描述 += 属性.BUFF增加(BUFFLv=4)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.觉醒增加(一觉力智=15)
            self.属性描述 += 属性.被动增加(守护恩赐体精=80)
            self.属性描述 += 属性.被动增加(转职被动智力=80)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.04, BUFF智力per=1.04)
            self.属性描述 += 属性.BUFF增加(BUFF物攻per=1.03, BUFF魔攻per=1.03, BUFF独立per=1.03)
        else:
            self.属性描述 += 属性.BUFF增加(BUFFLv=3)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.觉醒增加(一觉力智=15)

class 套装效果100(套装):
    名称 = '堕落的暗黑之力'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            属性.力量 += 200
            属性.智力 += 200
            self.属性描述 += 属性.附加伤害加成(0.20)
            self.属性描述 += 属性.最终伤害加成(0.20)
            self.属性描述 += 属性.技能攻击力加成(0.16)
        elif 属性.装备检查('时空：黑暗幽灵紫杉胸甲'):
            self.属性描述 += 属性.附加伤害加成(0.07)
            self.属性描述 += 属性.最终伤害加成(0.20)
            self.属性描述 += 属性.技能攻击力加成(0.10)
        else:
            self.属性描述 += 属性.附加伤害加成(0.13)
            self.属性描述 += 属性.最终伤害加成(0.12)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            self.属性描述 += 属性.物理暴击率增加(0.08)
            self.属性描述 += 属性.魔法暴击率增加(0.08)
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
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            self.属性描述 += 属性.力智固定加成(x=200)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.33, BUFF智力per=1.33)
            self.属性描述 += 属性.觉醒增加(一觉力智=205)
            self.属性描述 += 属性.觉醒增加(一觉力智per=1.07)
            self.属性描述 += 属性.被动增加(守护恩赐体精=265)
            self.属性描述 += 属性.被动增加(转职被动智力=65)       
        elif 属性.装备检查('时空·黑暗幽灵紫杉胸甲'):
            self.属性描述 += 属性.被动增加(一觉被动Lv=2)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.29, BUFF智力per=1.29)
            self.属性描述 += 属性.觉醒增加(一觉力智=205)
            self.属性描述 += 属性.觉醒增加(一觉力智per=1.06)
            self.属性描述 += 属性.被动增加(守护恩赐体精=255)
            self.属性描述 += 属性.被动增加(转职被动智力=255) 
        else:
            self.属性描述 += 属性.被动增加(一觉被动Lv=2)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.22, BUFF智力per=1.22)
            self.属性描述 += 属性.觉醒增加(一觉力智=205)
            self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)
            self.属性描述 += 属性.被动增加(守护恩赐体精=120)
            self.属性描述 += 属性.被动增加(转职被动智力=120)
    
class 套装效果101(套装):
    名称 = '江山如画'
    件数 = 3
    类型 = '首饰'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.附加伤害加成(0.20)
        self.属性描述 += 属性.技能攻击力加成(0.10)
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
            self.属性描述 += 属性.觉醒增加(一觉力智=34)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.04, BUFF智力per=1.04)
            self.属性描述 += 属性.被动增加(守护恩赐体精=16)
            self.属性描述 += 属性.被动增加(转职被动智力=16)
        else:
            self.属性描述 += 属性.被动增加(一觉被动Lv=2)
            self.属性描述 += 属性.觉醒增加(一觉力智=26)
            self.属性描述 += 属性.被动增加(守护恩赐体精=76)
            self.属性描述 += 属性.被动增加(转职被动智力=76)

class 套装效果102(套装):
    名称 = '万物的生灭'
    件数 = 3
    类型 = '特殊'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.最终伤害加成(0.12)
        self.属性描述 += 属性.技能攻击力加成(0.20)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.05)
        self.属性描述 += 属性.魔法暴击率增加(0.05)
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
            self.属性描述 += 属性.BUFF增加(BUFFLv=1)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.觉醒增加(一觉力智=20)
            self.属性描述 += 属性.被动增加(守护恩赐体精=120)
            self.属性描述 += 属性.被动增加(转职被动智力=100)
        else:
            self.属性描述 += 属性.BUFF增加(BUFFLv=1)
            self.属性描述 += 属性.觉醒增加(一觉力智=50)
            self.属性描述 += 属性.被动增加(守护恩赐体精=120)
            self.属性描述 += 属性.被动增加(转职被动智力=100)   

class 套装效果103(套装):
    名称 = '兵法之神'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.附加伤害加成(0.12)
        属性.物理攻击力 += 200
        属性.魔法攻击力 += 200
        属性.独立攻击力 += 200
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.10)
        self.属性描述 += 属性.移动速度增加(0.10)
        self.属性描述 += 属性.释放速度增加(0.15)
        self.属性描述 += 属性.物理暴击率增加(0.05)
        self.属性描述 += 属性.魔法暴击率增加(0.05)
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

class 套装效果104(套装):
    名称 = '兵法之神'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        self.属性描述 += 属性.所有属性强化加成(25)
        self.属性描述 += 属性.百分比三攻加成(0.22)
        self.属性描述 += 属性.技能攻击力加成(0.10)
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
        self.属性描述 += 属性.所有属性强化加成(10)
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
        self.属性描述 += 属性.附加伤害加成(0.35)
        self.属性描述 += 属性.技能等级加成('所有', 50, 75, 2)
        self.属性描述 += 属性.技能等级加成('所有', 85, 85, 1)
        try:
            属性.技能栏[属性.技能序号['基础精通']].倍率 *= 1.2
        except:
            pass
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.10 * 3)
        self.属性描述 += 属性.移动速度增加(0.10 * 3)
        self.属性描述 += 属性.释放速度增加(0.15 * 3)
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
        self.属性描述 += 属性.附加伤害加成(0.40)
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.05)
        self.属性描述 += 属性.移动速度增加(0.05)
        self.属性描述 += 属性.释放速度增加(0.20)
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
        self.属性描述 += 属性.百分比三攻加成(0.12)
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
        self.属性描述 += 属性.物理暴击率增加(0.10)
        self.属性描述 += 属性.魔法暴击率增加(0.10)
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
        self.属性描述 += 属性.百分比三攻加成(0.30)
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
            self.属性描述 += 属性.所有属性强化加成(10)
            self.属性描述 += 属性.属性附加加成(0.20)
            self.属性描述 += 属性.附加伤害加成(0.09)
        elif 天御套装 == 1:
            self.属性描述 += 属性.所有属性强化加成(50)
            self.属性描述 += 属性.属性附加加成(0.25)
        elif 天御套装 == 2:
            self.属性描述 += 属性.附加伤害加成(0.45)
        pass
    def 其它属性(self, 属性):
        if 天御套装 == 0:
            self.属性描述 += 属性.攻击速度增加(0.04)
            self.属性描述 += 属性.移动速度增加(0.04)
            self.属性描述 += 属性.释放速度增加(0.05)
        elif 天御套装 == 2:
            self.属性描述 += 属性.攻击速度增加(0.20)
            self.属性描述 += 属性.移动速度增加(0.20)
            self.属性描述 += 属性.释放速度增加(0.25)
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
        self.属性描述 += 属性.百分比力智加成(0.05)
        pass
    def 进图属性(self, 属性):
        self.属性描述 += 属性.百分比三攻加成(0.40)
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.30)
        self.属性描述 += 属性.移动速度增加(0.30)
        self.属性描述 += 属性.释放速度增加(0.445)
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
        self.属性描述 += 属性.附加伤害加成(战术白字)
        pass
    def 进图属性(self, 属性):
        属性.力量 += 620
        属性.智力 += 620
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.攻击速度增加(0.20)
        self.属性描述 += 属性.移动速度增加(0.20)
        self.属性描述 += 属性.释放速度增加(0.20  )
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
        self.属性描述 += 属性.百分比力智加成(0.12)
        属性.力量 += 150
        属性.智力 += 150
        self.属性描述 += 属性.附加伤害加成(0.35)
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
        self.属性描述 += 属性.百分比力智加成(0.18)
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
        self.属性描述 += 属性.所有属性强化加成(50)
        属性.智力 += 400
        self.属性描述 += 属性.技能攻击力加成(0.18)
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
        self.属性描述 += 属性.附加伤害加成(0.18)
        self.属性描述 += 属性.冰属性强化加成(50)
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
        self.属性描述 += 属性.附加伤害加成(0.20)
        self.属性描述 += 属性.所有属性强化加成(18)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        self.属性描述 += 属性.物理暴击率增加(0.12)
        self.属性描述 += 属性.魔法暴击率增加(0.12        )
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
            self.属性描述 += 属性.百分比力智加成(0.10)
            self.属性描述 += 属性.附加伤害加成(0.05)
        else:
            self.属性描述 += 属性.百分比力智加成(0.04)
            self.属性描述 += 属性.附加伤害加成(0.04)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·维度冲击臂环'):
            pass
        else:
            self.属性描述 += 属性.物理暴击率增加(0.03)
            self.属性描述 += 属性.魔法暴击率增加(0.03)
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
            self.属性描述 += 属性.百分比力智加成(0.10)
            self.属性描述 += 属性.暴击伤害加成(0.05)
        else:
            self.属性描述 += 属性.暴击伤害加成(0.10)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·腐蚀之黑色十字耳环'):
            pass
        else:
            self.属性描述 += 属性.物理暴击率增加(0.04)
            self.属性描述 += 属性.魔法暴击率增加(0.04)
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
            self.属性描述 += 属性.百分比力智加成(0.10)
            self.属性描述 += 属性.附加伤害加成(0.05)
        else:
            self.属性描述 += 属性.百分比力智加成(0.04)
            self.属性描述 += 属性.附加伤害加成(0.04)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·先贤的馈赠手镯'):
            pass
        else:
            self.属性描述 += 属性.物理暴击率增加(0.03)
            self.属性描述 += 属性.魔法暴击率增加(0.03)
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
            self.属性描述 += 属性.百分比力智加成(0.15)
            self.属性描述 += 属性.附加伤害加成(0.10)
            self.属性描述 += 属性.技能攻击力加成(0.05)
            self.属性描述 += 属性.百分比三攻加成(0.13)
        elif 属性.装备检查('时空：先贤的馈赠手镯'):
            self.属性描述 += 属性.附加伤害加成(0.05)
            self.属性描述 += 属性.技能攻击力加成(0.05)
        else:
            self.属性描述 += 属性.百分比力智加成(0.04)
            self.属性描述 += 属性.附加伤害加成(0.04)
            self.属性描述 += 属性.技能攻击力加成(0.05)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·先贤的馈赠手镯'):
            self.属性描述 += 属性.物理暴击率增加(0.03)
            self.属性描述 += 属性.魔法暴击率增加(0.03)
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
            self.属性描述 += 属性.最终伤害加成(0.05)
            self.属性描述 += 属性.附加伤害加成(0.07)
        else:
            self.属性描述 += 属性.百分比三攻加成(0.05)
            self.属性描述 += 属性.附加伤害加成(0.07)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            pass
        else:
            self.属性描述 += 属性.物理暴击率增加(0.04)
            self.属性描述 += 属性.魔法暴击率增加(0.04)
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
    def BUFF属性(self, 属性):
        if 属性.装备检查('轮回·黑暗幽灵紫杉胸甲'):
            pass
        elif 属性.装备检查('时空·黑暗幽灵紫杉胸甲'):
            self.属性描述 += 属性.BUFF增加(BUFFLv=2)
            self.属性描述 += 属性.觉醒增加(一觉力智=65)
            self.属性描述 += 属性.被动增加(守护恩赐体精=80)
            self.属性描述 += 属性.被动增加(转职被动智力=80)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.04, BUFF智力per=1.04)
        else:
            self.属性描述 += 属性.BUFF增加(BUFFLv=3)
            self.属性描述 += 属性.觉醒增加(一觉力智=65)
    

class 套装效果124(套装):
    名称 = '鲜红血纹'
    件数 = 2
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            pass
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            self.属性描述 += 属性.百分比力智加成(0.10)
            self.属性描述 += 属性.所有属性强化加成(25)
        else:
            self.属性描述 += 属性.百分比力智加成(0.05)
            self.属性描述 += 属性.所有属性强化加成(25)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            pass
        else:
            self.属性描述 += 属性.物理暴击率增加(0.04)
            self.属性描述 += 属性.魔法暴击率增加(0.04)
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

    def BUFF属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            pass
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            self.属性描述 += 属性.BUFF增加(BUFFLv=2)
            self.属性描述 += 属性.觉醒增加(一觉力智=65)
            self.属性描述 += 属性.被动增加(守护恩赐体精=80)
            self.属性描述 += 属性.被动增加(转职被动智力=80)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.04, BUFF智力per=1.04)
        else:
            self.属性描述 += 属性.BUFF增加(BUFFLv=3)
            self.属性描述 += 属性.觉醒增加(一觉力智=65)
    

class 套装效果125(套装):
    名称 = '鲜红血纹'
    件数 = 3
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            属性.力量 += 200
            属性.智力 += 200
            self.属性描述 += 属性.附加伤害加成(0.10)
            self.属性描述 += 属性.最终伤害加成(0.10)
            self.属性描述 += 属性.所有属性强化加成(20)
            self.属性描述 += 属性.百分比三攻加成(0.05)
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            self.属性描述 += 属性.附加伤害加成(0.10)
            self.属性描述 += 属性.最终伤害加成(0.08)
            self.属性描述 += 属性.所有属性强化加成(15)
            self.属性描述 += 属性.百分比三攻加成(0.05)
        else:
            self.属性描述 += 属性.附加伤害加成(0.10)
            self.属性描述 += 属性.所有属性强化加成(10)
            self.属性描述 += 属性.百分比三攻加成(0.05)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            pass
        else:
            self.属性描述 += 属性.物理暴击率增加(0.04)
            self.属性描述 += 属性.魔法暴击率增加(0.04)
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
    def BUFF属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            self.属性描述 += 属性.力智固定加成(200)
            self.属性描述 += 属性.BUFF增加(BUFFLv=6)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.觉醒增加(一觉力智=80)
            self.属性描述 += 属性.被动增加(守护恩赐体精=200)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.08, BUFF智力per=1.08)
            self.属性描述 += 属性.BUFF增加(BUFF物攻per=1.04, BUFF魔攻per=1.04, BUFF独立per=1.04)
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            self.属性描述 += 属性.BUFF增加(BUFFLv=4)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.觉醒增加(一觉力智=15)
            self.属性描述 += 属性.被动增加(守护恩赐体精=80)
            self.属性描述 += 属性.被动增加(转职被动智力=80)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.04, BUFF智力per=1.04)
            self.属性描述 += 属性.BUFF增加(BUFF物攻per=1.03, BUFF魔攻per=1.03, BUFF独立per=1.03)
        else:
            self.属性描述 += 属性.BUFF增加(BUFFLv=3)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.觉醒增加(一觉力智=15)

class 套装效果126(套装):
    名称 = '鲜红血纹'
    件数 = 5
    类型 = '防具'
    def 城镇属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            属性.力量 += 200
            属性.智力 += 200
            self.属性描述 += 属性.所有属性强化加成(30)
            self.属性描述 += 属性.最终伤害加成(0.06)
            self.属性描述 += 属性.百分比力智加成(0.10)
            self.属性描述 += 属性.技能攻击力加成(0.16)
            self.属性描述 += 属性.百分比三攻加成(0.15)
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            self.属性描述 += 属性.所有属性强化加成(10)
            self.属性描述 += 属性.最终伤害加成(0.05)
            self.属性描述 += 属性.技能攻击力加成(0.10)
            self.属性描述 += 属性.百分比三攻加成(0.15)
        else:
            self.属性描述 += 属性.所有属性强化加成(15)
            self.属性描述 += 属性.百分比力智加成(0.05)
            self.属性描述 += 属性.百分比三攻加成(0.15)
        pass
    def 进图属性(self, 属性):
        pass
    def 其它属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            self.属性描述 += 属性.物理暴击率增加(0.08)
            self.属性描述 += 属性.魔法暴击率增加(0.08)
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
    def BUFF属性(self, 属性):
        if 属性.装备检查('轮回·鲜红血纹皮甲胸铠'):
            self.属性描述 += 属性.力智固定加成(x=200)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.33, BUFF智力per=1.33)
            self.属性描述 += 属性.觉醒增加(一觉力智=205)
            self.属性描述 += 属性.觉醒增加(一觉力智per=1.07)
            self.属性描述 += 属性.被动增加(守护恩赐体精=265)
            self.属性描述 += 属性.被动增加(转职被动智力=65)       
        elif 属性.装备检查('时空：鲜红血纹皮甲胸铠'):
            self.属性描述 += 属性.被动增加(一觉被动Lv=2)
            self.属性描述 += 属性.觉醒增加(一觉Lv=1)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.29, BUFF智力per=1.29)
            self.属性描述 += 属性.觉醒增加(一觉力智=205)
            self.属性描述 += 属性.觉醒增加(一觉力智per=1.06)
            self.属性描述 += 属性.被动增加(守护恩赐体精=255)
            self.属性描述 += 属性.被动增加(转职被动智力=255) 
        else:
            self.属性描述 += 属性.被动增加(一觉被动Lv=2)
            self.属性描述 += 属性.BUFF增加(BUFF力量per=1.22, BUFF智力per=1.22)
            self.属性描述 += 属性.觉醒增加(一觉力智=205)
            self.属性描述 += 属性.觉醒增加(一觉力智per=1.05)
            self.属性描述 += 属性.被动增加(守护恩赐体精=120)
            self.属性描述 += 属性.被动增加(转职被动智力=120)
#endregion