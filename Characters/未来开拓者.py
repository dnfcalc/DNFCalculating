from PublicReference.base import *

# 2020.6.29 
# 2029.8.14 添加韩服新护石,添加引力源光弹护石和能量禁锢护石相关选项

# 武器源力剑
# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '源力剑':
#             return round(self.CD / self.恢复 * 1.05, 1)
            
# 源力剑精通
class 未来开拓者技能0(被动技能):
    名称 = '源力剑精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    谍影专用倍率 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 <= 20:
            return round(1 + (0.05 + 0.01 * self.等级) * self.谍影专用倍率, 5)
        else:
            return round(1 + (0.25 + 0.02 * (self.等级 - 20)) * self.谍影专用倍率, 5)

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


# 细胞弱化
class 未来开拓者技能1(被动技能):
    名称 = '细胞弱化'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1
    
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)


# 源能增幅一觉被动
class 未来开拓者技能2(被动技能):
    名称 = '源能增幅'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


# 二觉被动
class 未来开拓者技能3(被动技能):
    名称 = '源力汇聚'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


# 卓越之力
class 未来开拓者技能4(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 超卓之心
class 未来开拓者技能5(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


# 觉醒之抉择
class 未来开拓者技能6(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)
            
# 源光斩
class 未来开拓者技能7(主动技能):
    名称 = '源光斩'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    攻击段数 = 2
    基础 = 1443.00 - 146.85
    成长 = 146.85
    CD = 5
    TP成长 = 0.08
    TP上限 = 5


# 旋转源能波
class 未来开拓者技能8(主动技能):
    名称 = '旋转源能波'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    攻击段数 = 2
    基础 = 1896.00 - 193.16
    成长 = 193.16
    CD = 5
    TP成长 = 0.10
    TP上限 = 5

# 源能护盾，未提炼
class 未来开拓者技能9(主动技能):
    名称 = '源能护盾'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    攻击段数 = 2
    基础 = 2996.00 - 310.67
    成长 = 310.67
    CD = 8
    TP成长 = 0.08
    TP上限 = 5


# 镭射源能枪
class 未来开拓者技能10(主动技能):
    名称 = '镭射源能枪'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    攻击段数 = 2
    基础 = 3116.00 - 316.33
    成长 = 316.33
    CD = 10
    TP成长 = 0.10
    TP上限 = 5


# 源能波刃
class 未来开拓者技能11(主动技能):
    名称 = '源能波刃'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    攻击段数 = 11
    基础 = 3138.00 - 318.48
    成长 = 318.48
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

#能量飞鱼弹
class 未来开拓者技能12(主动技能):
    名称 = '能量飞鱼弹'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    攻击段数 = 1
    基础 = 3254.00 - 330.23
    成长 = 330.23
    CD = 7.5
    TP成长 = 0.10
    TP上限 = 5
    
# 脉冲斩
class 未来开拓者技能13(主动技能):
    名称 = '脉冲斩'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    攻击段数 = 8
    基础 = 4080.00 - 413.84
    成长 = 413.84
    CD = 10
    TP成长 = 0.10
    TP上限 = 5


# 电磁领域
class 未来开拓者技能14(主动技能):
    名称 = '电磁领域'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    攻击段数 = 3
    基础 = 6673.00 - 677.71
    成长 = 677.71
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


# 引力源光弹
class 未来开拓者技能15(主动技能):
    名称 = '引力源光弹'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    
    基础 = 593 - 60
    成长 = 60
    攻击次数 = 8
    
    基础2 = 1673 - 170
    成长2 = 170
    攻击次数2 = 1
   
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1
    是否装备护石 = 0
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 1.28 
            self.是否装备护石 = 1
        elif x == 1:
            self.攻击次数2 = 1.60 #修改位置 
            self.是否装备护石 = 1


# 光裂斩，护石取最大蓄气
class 未来开拓者技能16(主动技能):
    名称 = '光裂斩'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    攻击段数 = 1
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    基础 = 5612 - 569
    成长 = 569
    攻击次数 = 1
    
    基础2 = 747 - 76
    成长2 = 76
    攻击次数2 = 5
   

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 1.98 * 1.06
            self.攻击次数2 = 0
        elif x == 1:
            self.攻击次数 = 1.98 * 1.14#修改位置
            self.攻击次数2 = 0

# 光导裂地斩
class 未来开拓者技能17(主动技能):
    名称 = '光导裂地斩'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    攻击段数 = 6
    基础 = 6247 - 633.5
    成长 = 633.5
    攻击次数 = 1
    
    基础2 = 9512 - 965
    成长2 = 965
    攻击次数2 = 1
   
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.17
            self.攻击次数2 *= 1.2
        elif x == 1:
            self.攻击次数 *= 1.17
            self.攻击次数2 *= 1.33#修改位置


# 一觉，非提炼
class 未来开拓者技能18(主动技能):
    名称 = '超能场域'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    攻击段数 = 13
    基础 = 2012 - 12 * 131.4
    成长 = 131.4
    攻击次数 = 13
    
    基础2 = 112716 - 7361 * 12
    成长2 = 7361
    攻击次数2 = 1
   
    CD = 145


# 能量禁锢
class 未来开拓者技能19(主动技能):
    名称 = '能量禁锢'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1


    基础 = 792 - 81
    成长 = 81
    攻击次数 = 10

    基础2 = 3397 - 344.5
    成长2 = 344.5
    攻击次数2 = 1

    # 爆炸次数 = 0
    是否装备护石 = 0
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 14 * 0.8 #14是测试结论
            self.是否装备护石 =1
            # self.攻击次数2 += self.爆炸次数* 0.33
        elif x == 1:
            self.攻击次数 = 14 * 0.89#修改位置
            self.是否装备护石 =1
            # self.攻击次数2 += self.爆炸次数 *0.33
        
        
# 离散能量波

class 未来开拓者技能20(主动技能):
    名称 = '离散能量波'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    
    基础 = 1658 - 168.5
    成长 = 168.5
    攻击次数 = 10
    
    基础2 = 7109 - 721.5
    成长2 = 721.5
    攻击次数2 = 1 

    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.9
            self.攻击次数 = 15 * 0.75
            self.攻击次数2 *= 1.4
        elif x == 1:
            self.CD *= 0.9
            self.攻击次数 = 15 * 0.75
            self.攻击次数2 *= 1.66#修改位置
 
# 绝望圆舞
class 未来开拓者技能21(主动技能):
    名称 = '绝望圆舞'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    攻击段数 = 8
    基础 = 38894.00 - 3946.60
    成长 = 3946.60
    CD = 40
    
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *=1.35

# CEAB-2超能爆发，满蓄
class 未来开拓者技能22(主动技能):
    名称 = 'CEAB-2超能爆发'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    攻击段数 = 1
    基础 = 44464.00 - 4510.92
    成长 = 4510.92
    CD = 45
    
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.39
            self.CD *= 0.9

# 二觉，1.5秒后c
class 未来开拓者技能23(主动技能):
    名称 = '终焉：超世界崩坏'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    攻击段数 = 17
    
    基础 = 1800 - 216.33333 * 5
    成长 = 216.33333
    攻击次数 = 6
    
    基础2 = 168632 - 20286.5 *5
    成长2 = 20286.5
    攻击次数2 = 1 

    CD = 180


未来开拓者技能列表 = []
i = 0
while i >= 0:
    try:
        exec('未来开拓者技能列表.append(未来开拓者技能' + str(i) + '())')
        i += 1
    except:
        i = -1

未来开拓者技能序号 = dict()
for i in range(len(未来开拓者技能列表)):
    未来开拓者技能序号[未来开拓者技能列表[i].名称] = i

未来开拓者一觉序号 = 0
未来开拓者二觉序号 = 0
未来开拓者三觉序号 = 0
for i in 未来开拓者技能列表:
    if i.所在等级 == 50:
        未来开拓者一觉序号 = 未来开拓者技能序号[i.名称]
    if i.所在等级 == 85:
        未来开拓者二觉序号 = 未来开拓者技能序号[i.名称]
    if i.所在等级 == 100:
        未来开拓者三觉序号 = 未来开拓者技能序号[i.名称]

未来开拓者护石选项 = ['无']
for i in 未来开拓者技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        未来开拓者护石选项.append(i.名称)

未来开拓者符文选项 = ['无']
for i in 未来开拓者技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        未来开拓者符文选项.append(i.名称)


class 未来开拓者角色属性(角色属性):
    实际名称 = '未来开拓者'
    角色 = '枪剑士'
    职业 = '源能专家'

    武器选项 = ['源力剑']
    
    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 2.0
    
    远古记忆 = 0
    
    引力源光弹充能次数 = 0
    能量禁锢爆炸次数 = 0
    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(未来开拓者技能列表)
        self.技能序号 = deepcopy(未来开拓者技能序号)

    def 数据计算(self, x = 0, y = -1):
        self.预处理()
        #初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)

        #能量禁锢护石
        if self.技能栏[self.技能序号['能量禁锢']].是否装备护石 == 1:
            技能单次伤害[self.技能序号['能量禁锢']] += (0.33*self.能量禁锢爆炸次数)*(self.技能栏[self.技能序号['能量禁锢']].基础2 + self.技能栏[self.技能序号['能量禁锢']].成长2 * self.技能栏[self.技能序号['能量禁锢']].等级)*(1 + self.技能栏[self.技能序号['能量禁锢']].TP成长 * self.技能栏[self.技能序号['能量禁锢']].TP等级) * self.技能栏[self.技能序号['能量禁锢']].倍率 *self.伤害指数*i.被动倍率

        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        #引力源光弹护石
        if self.技能栏[self.技能序号['引力源光弹']].是否装备护石 == 1:
            if self.宠物次数[self.技能序号['引力源光弹']] < self.引力源光弹充能次数:
                技能总伤害[self.技能序号['CEAB-2超能爆发']] += (技能单次伤害[self.技能序号['引力源光弹']] * 0.3 * self.引力源光弹充能次数 * (1+self.白兔子技能*0.20 + self.年宠技能*0.10*self.宠物次数[self.技能序号['引力源光弹']]/self.引力源光弹充能次数+self.斗神之吼秘药*0.12))
            else:
                技能总伤害[self.技能序号['CEAB-2超能爆发']] += (技能单次伤害[self.技能序号['引力源光弹']] * 0.3 * self.引力源光弹充能次数 * (1+self.白兔子技能*0.20 + self.年宠技能*0.10+self.斗神之吼秘药*0.12))
        
        #返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)
      
class 未来开拓者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 未来开拓者角色属性()
        self.角色属性A = 未来开拓者角色属性()
        self.角色属性B = 未来开拓者角色属性()
        self.一觉序号 = 未来开拓者一觉序号
        self.二觉序号 = 未来开拓者二觉序号
        self.三觉序号 = 未来开拓者三觉序号
        self.护石选项 = deepcopy(未来开拓者护石选项)
        self.符文选项 = deepcopy(未来开拓者符文选项)

    def 引力源光弹充能次数判断(self, 警告,选项变更):
        引力源光弹次数 = 0
        超能爆发次数 = 0

        if self.次数输入[15].currentText() != '/CD':
            引力源光弹次数 = int(self.次数输入[15].currentText())
        else:
            引力源光弹次数 = 100
        if self.次数输入[22].currentText() != '/CD':
            超能爆发次数 = int(self.次数输入[22].currentText())
        else:
            超能爆发次数 = 100

        sign = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '引力源光弹' and 引力源光弹次数 != 0 and 超能爆发次数 != 0 :
                sign = 1

        充能次数上限 = 1
        if 引力源光弹次数 != 0 and 超能爆发次数 !=0 and (self.次数输入[22].currentText() != '/CD' or self.次数输入[15].currentText() != '/CD'):
            if 超能爆发次数 >= 引力源光弹次数:
                充能次数上限 = 引力源光弹次数
            else:
                充能次数上限 = 超能爆发次数
            # self.引力源光弹护石选项.setCurrentIndex(充能次数上限)
        if self.引力源光弹护石选项.currentIndex() >   充能次数上限 and sign == 1 and (self.次数输入[15].currentText() != '/CD' or self.次数输入[22].currentText() != '/CD' )and 警告 == 0 :
            self.引力源光弹护石选项.setCurrentIndex(充能次数上限)
            if 选项变更 == 0:
                QMessageBox.information(self,"错误",  "输入的充能次数超过上限，已自动修正") 
            警告 = 1   
        elif self.引力源光弹护石选项.currentIndex() <   充能次数上限 and sign == 1 and (self.次数输入[15].currentText() != '/CD' or self.次数输入[22].currentText() != '/CD' )and 选项变更 == 1:
            self.引力源光弹护石选项.setCurrentIndex(充能次数上限)
            选项变更= 0
        elif self.次数输入[15].currentText() == '/CD' and self.次数输入[22].currentText() == '/CD' and 选项变更 == 1:
            self.引力源光弹护石选项.setCurrentIndex(1)

        if sign == 0:
            self.引力源光弹护石选项.setEnabled(False)
            self.引力源光弹护石选项.setStyleSheet(不可选择下拉框样式)
            self.引力源光弹护石选项.setCurrentIndex(0)
        else:
            self.引力源光弹护石选项.setEnabled(True)
            self.引力源光弹护石选项.setStyleSheet(下拉框样式)
    flag1 = 0
    flag2 = 0
    flag3 = 0
    def 能量禁锢爆炸次数判断(self,警告):
        能量禁锢次数 = 0 
        能量飞鱼弹次数 = 0 
        源能护盾次数 = 0
        
 

        if self.次数输入[19].currentText() != '/CD':
            能量禁锢次数 = int(self.次数输入[19].currentText())
        else:
            能量禁锢次数 = 1
        if self.次数输入[12].currentText() != '/CD':
            能量飞鱼弹次数 = int(self.次数输入[12].currentText())
        else:
            能量飞鱼弹次数 = 2
        if self.次数输入[9].currentText() != '/CD':
            源能护盾次数 = int(self.次数输入[9].currentText())
        else:
            源能护盾次数 = 2



        sign2 = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '能量禁锢' and 能量禁锢次数 != 0 and (能量飞鱼弹次数+源能护盾次数) != 0:
                sign2 = 1


        护石 = []
        for i in range(3):
            护石.append(self.护石栏[i].currentText())
        if "能量禁锢" in 护石:
            self.flag1 = 1
        elif "能量禁锢" not in 护石 :
            self.flag1 = 0
        if self.flag1 == 1 and self.flag2 ==0:
            self.flag2 = 1
            self.flag3 = 1
        elif  self.flag1 == 1 and self.flag2 ==1:
            self.flag3 = 0
        if self.flag1 == 0 and self.flag2 ==1:    
            self.flag2 = 0
        if self.flag3 == 1:
            警告 = False
        护石 = []


        if 能量禁锢次数 != 0:
            if 能量禁锢次数 == 1:
                if(能量飞鱼弹次数+源能护盾次数) >= 2:
                    self.能量禁锢护石选项.setCurrentIndex(2)
                else:
                    self.能量禁锢护石选项.setCurrentIndex(能量飞鱼弹次数+源能护盾次数)
            else:
                self.能量禁锢护石选项.setCurrentIndex(2)
        else:
            self.能量禁锢护石选项.setCurrentIndex(0)
        if (能量飞鱼弹次数+源能护盾次数) < (能量禁锢次数*2)  and sign2 == 1 and 警告 == False and(self.次数输入[9].currentText() != '/CD' and self.次数输入[12].currentText() != '/CD'):
            QMessageBox.information(self,"错误",  "能量飞鱼弹与源能护盾次数不足以为能量禁锢提供"+str(能量禁锢次数*2)+"次爆炸，建议修改技能及爆炸次数，若不修改则按输入的数值计算") 
            警告 = True

        if sign2 == 0:
            self.能量禁锢护石选项.setEnabled(False)
            self.能量禁锢护石选项.setStyleSheet(不可选择下拉框样式)
            self.能量禁锢护石选项.setCurrentIndex(0)
        else:
            self.能量禁锢护石选项.setEnabled(True)
            self.能量禁锢护石选项.setStyleSheet(下拉框样式)

    def 界面(self):
        super().界面()


        self.引力源光弹护石选项=MyQComboBox(self.main_frame2)
        for i in range(100):
            self.引力源光弹护石选项.addItem('引力源光弹充能次数：'+str(i))
        self.引力源光弹护石选项.resize(160,20)
        self.引力源光弹护石选项.move(300,480)
        self.引力源光弹护石选项.setCurrentIndex(1)
        self.引力源光弹护石选项.setToolTip('修改对CEAB-2进行充能的次数，每次CEAB-2上限一次，受宠物技能影响。仅佩戴引力源光弹护石时生效')

        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(lambda state: self.引力源光弹充能次数判断(警告= 1,选项变更= 1))
        self.次数输入[15].currentIndexChanged.connect(lambda state: self.引力源光弹充能次数判断(警告= 0,选项变更= 1))
        self.次数输入[22].currentIndexChanged.connect(lambda state: self.引力源光弹充能次数判断(警告= 0,选项变更= 1))
        self.引力源光弹护石选项.currentIndexChanged.connect(lambda state: self.引力源光弹充能次数判断(警告= 0,选项变更= 0))




        self.能量禁锢护石选项=MyQComboBox(self.main_frame2)
        self.能量禁锢护石选项.addItem('能量禁锢爆炸次数：0')
        self.能量禁锢护石选项.addItem('能量禁锢爆炸次数：1')
        self.能量禁锢护石选项.addItem('能量禁锢爆炸次数：2')
        self.能量禁锢护石选项.resize(160,20)
        self.能量禁锢护石选项.move(300,390)
        self.能量禁锢护石选项.setCurrentIndex(2)
        self.能量禁锢护石选项.setToolTip('修改每次能量禁锢爆炸次数，与源能护盾、能量飞鱼弹释放次数关联，仅佩戴能量禁锢护石时生效')
        # bldic = {True:1,False:0}
        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(lambda state: self.能量禁锢爆炸次数判断(警告 = True ))

        self.次数输入[19].currentIndexChanged.connect(lambda state: self.能量禁锢爆炸次数判断(警告= False))
        self.次数输入[12].currentIndexChanged.connect(lambda state: self.能量禁锢爆炸次数判断(警告= False))
        self.次数输入[9].currentIndexChanged.connect(lambda state: self.能量禁锢爆炸次数判断(警告= False))


    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)


        属性.引力源光弹充能次数 = self.引力源光弹护石选项.currentIndex()
        # 属性.技能栏[属性.技能序号['能量禁锢']].爆炸次数 = self.能量禁锢护石选项.currentIndex()
        属性.能量禁锢爆炸次数 = self.能量禁锢护石选项.currentIndex()


    
