from math import *

from PublicReference.base import *

class 刹那永恒主动技能(主动技能):
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return round((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率,2)
    def 等效CD(self, 武器类型):
        if 武器类型 == '魔杖':
            return round(self.CD / self.恢复 * 1.0, 1)
        if 武器类型 == '法杖':
            return round(self.CD / self.恢复 * 1.1, 1)

class 刹那永恒技能0(刹那永恒主动技能):
    名称 = '冰魄剑'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 566
    成长 = 64.56
    攻击次数 = 2
    基础2 = 679.2
    成长2 = 77.47
    攻击次数2 = 1
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 7

class 刹那永恒技能1(被动技能):
    名称 = '冰武精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.01 * self.等级, 5)

class 刹那永恒技能2(刹那永恒主动技能):
    名称 = '寒冰连枪'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1583
    成长 = 180.63
    CD = 3.0
    TP成长 = 0.10
    TP上限 = 7

class 刹那永恒技能3(刹那永恒主动技能):
    名称 = '冰魄旋枪'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3652
    成长 = 410.47
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7

class 刹那永恒技能4(刹那永恒主动技能):
    名称 = '冰霜之径'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (30 + self.等级 * 4)

    def 加成倍率(self, 武器类型):
            return 1.0


class 刹那永恒技能5(被动技能):
    名称 = '冰之领悟'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return (1.02 + self.等级 * 0.01)
        else:
            return (1.12 + (self.等级 - 10) * 0.02)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return (1.02 + self.等级 * 0.01)
        else:
            return (1.12 + (self.等级 - 10) * 0.02)


class 刹那永恒技能6(刹那永恒主动技能):
    名称 = '冰魄之弓'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5524
    成长 = 625.77
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7


class 刹那永恒技能7(刹那永恒主动技能):
    名称 = '破冰飞刃'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5200.8
    成长 = 589.92
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

class 刹那永恒技能8(被动技能):
    名称 = '水晶剑'
    所在等级 = 30
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['冰魄剑']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return (1.25 + (self.等级-1) * 0.0125)


class 刹那永恒技能9(刹那永恒主动技能):
    名称 = '旋冰穿刺'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7354
    成长 = 830
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 7


class 刹那永恒技能10(刹那永恒主动技能):
    名称 = '冰魄锤击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8341
    成长 = 942
    CD = 18.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.27
        self.成长 *= 1.27

class 刹那永恒技能11(刹那永恒主动技能):
    名称 = '极冰绽放'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 1358
    成长 = 153.8
    攻击次数 = 4
    基础2 = 7250
    成长2 = 818.6
    攻击次数2 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.11
        self.成长 *= 1.11
        self.基础2 *= 1.23
        self.成长2 *= 1.23
        self.CD *= 0.90


class 刹那永恒技能12(刹那永恒主动技能):
    名称 = '冰雪风暴'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 789.3
    成长 = 89.26
    攻击次数 = 14
    基础2 = 7716
    成长2 = 871.29
    攻击次数2 = 1
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.攻击次数 = 16
        self.基础2 *= 1.15
        self.成长2 *= 1.15

class 刹那永恒技能13(被动技能):
    名称 = '冰封奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

class 刹那永恒技能14(刹那永恒主动技能):
    名称 = '千旋冰轮破'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 41381.22
    成长 = 12507.19
    CD = 145.0

class 刹那永恒技能15(刹那永恒主动技能):
    名称 = '冰凌破'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 18151
    成长 = 2046.1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.22
        self.成长 *= 1.22

class 刹那永恒技能16(刹那永恒主动技能):
    名称 = '千里冰封'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 25834
    成长 = 2917
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.18667
        self.成长 *= 1.18667

class 刹那永恒技能17(被动技能):
    名称 = '冰之技艺'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['冰魄之弓','破冰飞刃','冰雪风暴','千旋冰轮破','冰凌破','千里冰封','极冰领域','永罪冰狱']
    关联技能2 = ['冰魄剑','寒冰连枪','冰魄旋枪','旋冰穿刺','冰魄锤击','极冰绽放','碎冰破']
    
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.03 * self.等级, 5)


class 刹那永恒技能18(刹那永恒主动技能):
    名称 = '碎冰破'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 45452
    成长 = 5132.0
    CD = 40.0

class 刹那永恒技能19(刹那永恒主动技能):
    名称 = '极冰领域'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 36582
    成长 = 4130.0
    CD = 40.0

class 刹那永恒技能20(刹那永恒主动技能):
    名称 = '永罪冰狱'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 75014
    成长 = 22647.0
    CD = 180.0

class 刹那永恒技能21(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 刹那永恒技能22(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 刹那永恒技能23(被动技能):
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




刹那永恒技能列表 = []
i = 0
while i >= 0:
    try:
        exec('刹那永恒技能列表.append(刹那永恒技能'+str(i)+'())')
        i += 1
    except:
        i = -1

刹那永恒技能序号 = dict()
for i in range(len(刹那永恒技能列表)):
    刹那永恒技能序号[刹那永恒技能列表[i].名称] = i

刹那永恒一觉序号 = 0
刹那永恒二觉序号 = 0
刹那永恒三觉序号 = 0
for i in 刹那永恒技能列表:
    if i.所在等级 == 50:
        刹那永恒一觉序号 = 刹那永恒技能序号[i.名称]
    if i.所在等级 == 85:
        刹那永恒二觉序号 = 刹那永恒技能序号[i.名称]
    if i.所在等级 == 100:
        刹那永恒三觉序号 = 刹那永恒技能序号[i.名称]

刹那永恒护石选项 = ['无']
for i in 刹那永恒技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        刹那永恒护石选项.append(i.名称)

刹那永恒符文选项 = ['无']
for i in 刹那永恒技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        刹那永恒符文选项.append(i.名称)


class 刹那永恒角色属性(角色属性):

    职业名称 = '刹那永恒'

    武器选项 = ['魔杖','法杖']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比']
    
    #默认
    伤害类型 = '魔法百力比'
    防具类型 = '皮甲'
    防具精通属性 = ['智力']

    主BUFF = 1.800
   
    #基础属性(含唤醒)
    基础力量 = 774.0
    基础智力 = 976.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
  
    def __init__(self):
        self.技能栏= copy.deepcopy(刹那永恒技能列表)
        self.技能序号= copy.deepcopy(刹那永恒技能序号)
    def 伤害计算(self, x = 0):
        self.装备基础()

        for i in self.装备栏:
            装备列表[装备序号[i]].城镇属性(self)
            装备列表[装备序号[i]].进图属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].城镇属性(self)
            套装列表[套装序号[i]].进图属性(self)
        self.冰属性强化 += self.技能栏[self.技能序号['冰霜之径']].属强加成()
        self.所有属性强化(self.进图属强)
        # Will添加
        self.CD倍率计算()
        self.加算冷却计算()

        基准倍率 = 1.5 * self.主BUFF * (1 - 443215 / (443215 + 20000))

        if self.伤害类型 == '物理百分比':
            面板 = (self.面板力量()/250+1) * (self.物理攻击力 + self.进图物理攻击力) * (1 + self.百分比三攻)
        if self.伤害类型 == '魔法百分比':
            面板 = (self.面板智力()/250+1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻)
        if self.伤害类型 == '物理固伤':
            面板 = (self.面板力量()/250+1) * (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻)
        if self.伤害类型 == '魔法固伤':
            面板 = (self.面板智力()/250+1) * (self.独立攻击力 + self.进图独立攻击力) * (1 + self.百分比三攻)

        属性倍率=1.05+0.0045*max(self.火属性强化,self.冰属性强化,self.光属性强化,self.暗属性强化)
        增伤倍率=1+self.伤害增加
        增伤倍率*=1+self.暴击伤害
        增伤倍率*=1+self.最终伤害
        增伤倍率*=self.技能攻击力
        增伤倍率*=1+self.持续伤害*(1-0.1*self.持续伤害计算比例)
        增伤倍率*=1+self.附加伤害+self.属性附加*属性倍率
        伤害指数=面板*属性倍率*增伤倍率*基准倍率/100
        
        self.被动倍率计算()

        技能释放次数=[]
        技能单次伤害=[]
        技能总伤害=[]
    
        #技能单次伤害计算
        for i in self.技能栏:
            if i.是否主动==1:
                技能单次伤害.append(i.等效百分比(self.武器类型)*伤害指数*i.被动倍率)
            else:
                技能单次伤害.append(0)
      
        #技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                if self.次数输入[self.技能序号[i.名称]] =='/CD':
                    技能释放次数.append(int(self.时间输入/i.等效CD(self.武器类型) + 1 +i.基础释放次数))
                else:
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]])+i.基础释放次数)
            else:
                技能释放次数.append(0)
    
        #单技能伤害合计
    
        for i in self.技能栏:
            if i.是否主动==1 and 技能释放次数[self.技能序号[i.名称]] != 0:
                技能总伤害.append(技能单次伤害[self.技能序号[i.名称]]*技能释放次数[self.技能序号[i.名称]]*(1+self.白兔子技能*0.20+self.年宠技能*0.10*self.宠物次数[self.技能序号[i.名称]]/技能释放次数[self.技能序号[i.名称]]+self.斗神之吼秘药*0.12))
            else:
                技能总伤害.append(0)
    
        总伤害=0
        for i in self.技能栏:
            总伤害+=技能总伤害[self.技能序号[i.名称]]
        
        if x==0:
            return 总伤害
    
        if x==1:
            详细数据=[]
            for i in range(0,len(self.技能栏)):
                详细数据.append(技能释放次数[i])
                详细数据.append(技能总伤害[i])
                if 技能释放次数[i]!=0:
                    详细数据.append(技能总伤害[i]/技能释放次数[i])
                else:
                    详细数据.append(0)
                if 总伤害!=0:
                    详细数据.append(技能总伤害[i]/总伤害*100)
                else:
                    详细数据.append(0)
            return 详细数据
            
    def 冰属性强化加成(self):
        冰属性强化值 = 0
        for i in self.技能栏:
            if i.名称 != '冰霜之径':
              冰属性强化值 += 0
            else:
              冰属性强化值 += i.属强加成()
        return (冰属性强化值)

class 刹那永恒(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 刹那永恒角色属性()
        self.角色属性A = 刹那永恒角色属性()
        self.角色属性B = 刹那永恒角色属性()
        self.一觉序号 = 刹那永恒一觉序号
        self.二觉序号 = 刹那永恒二觉序号
        self.三觉序号 = 刹那永恒三觉序号
        self.护石选项 = copy.deepcopy(刹那永恒护石选项)
        self.符文选项 = copy.deepcopy(刹那永恒符文选项)
    def 输出界面(self, index):
        装备名称 = []
        套装名称 = []
        百变怪 = self.排行数据[index][-1]
        for i in range(0, 12):
            装备名称.append(self.排行数据[index][i])
        for i in range(13,len(self.排行数据[index])-1):
            套装名称.append(self.排行数据[index][i])

        C = copy.deepcopy(self.角色属性A)
        C.技能栏 = copy.deepcopy(self.角色属性A.技能栏)
        C.穿戴装备(装备名称,套装名称)
        for i in C.装备栏:
            装备列表[装备序号[i]].城镇属性(C)
        for i in C.套装栏:
            套装列表[套装序号[i]].城镇属性(C)
        C.装备基础()

        self.角色属性B = copy.deepcopy(self.角色属性A)
        self.角色属性B.技能栏 = copy.deepcopy(self.角色属性A.技能栏)
        self.角色属性B.穿戴装备(装备名称,套装名称)
        #for i in self.角色属性B.装备栏:
        #    装备列表[装备序号[i]].其它属性(self.角色属性B)
        #for i in self.角色属性B.套装栏:
        #    套装列表[套装序号[i]].其它属性(self.角色属性B)
        统计详情 = self.角色属性B.伤害计算(1)

        #最大输出界面限制
        if len(self.输出窗口列表)>=10:
            del self.输出窗口列表[0]
    
        输出窗口 = QWidget()
        self.输出窗口列表.append(输出窗口)
        输出窗口.setFixedSize(788, 564)
        输出窗口.setWindowTitle('详细数据')
        输出窗口.setWindowIcon(self.icon)  
        QLabel(输出窗口).setPixmap(self.输出背景图片)
      
        excel=[]
        for i in range(0,len(self.角色属性B.技能栏)):
            excel.append(统计详情[i*4+1])
        excel.sort()
    
        实际技能等级=[]
        技能等效CD=[]
        for i in self.角色属性B.技能栏:
            实际技能等级.append(i.等级)
            if i.是否主动==1:
                技能等效CD.append(i.等效CD(self.角色属性B.武器类型))
            else:
                技能等效CD.append(0)
    
        总伤害数值=0
    
        for i in range(0,len(self.角色属性B.技能栏)):
            j=len(self.角色属性B.技能栏)-1-excel.index(统计详情[i*4+1])
            if 统计详情[i*4] != 0:
                每行详情=[]
                for k in range(0,7):
                    每行详情.append(QLabel(输出窗口))
    
                #图片
                每行详情[0].setPixmap(self.技能图片[i])
                tempstr='<font color="#FF0000"><b>'+self.角色属性B.技能栏[i].名称+'</b></font><br>'
                tempstr+='基础百分比：<b>'+str(int(self.角色属性B.技能栏[i].等效百分比(self.角色属性B.武器类型)))+'%</b><br>'
                if self.角色属性B.技能栏[i].TP上限!=0:
                    tempstr+='TP倍率：<b>'+str(round((1+self.角色属性B.技能栏[i].TP成长*self.角色属性B.技能栏[i].TP等级)*100,1))+'%</b><br>'
                tempstr+='被动倍率：<b>'+str(round(self.角色属性B.技能栏[i].被动倍率*100,1))+'%</b><br>'
                if self.角色属性B.技能栏[i].倍率!=0:
                    tempstr+='其它倍率：<b>'+str(round(self.角色属性B.技能栏[i].倍率*100,1))+'%</b><br>'
                tempstr+='CD显示：<b>'+str(round(self.角色属性B.技能栏[i].CD,2))+'s</b><br>'
                tempstr+='CD恢复：<b>'+str(round(self.角色属性B.技能栏[i].恢复*100,1))+'%</b>'
                每行详情[0].setToolTip(tempstr)
    
                每行详情[0].move(302, 50+j*29)
                #等级
                每行详情[1].setText('Lv.'+str(实际技能等级[i]))
                每行详情[1].move(337, 50+j*29)
                每行详情[1].resize(30,28) 
                #CD
                每行详情[2].setText(str(技能等效CD[i])+'s')
                每行详情[2].move(380, 50+j*29)
                每行详情[2].resize(36,28)
                #次数
                每行详情[3].setText(str(统计详情[i*4]))
                每行详情[3].move(418, 50+j*29)
                每行详情[3].resize(30,28) 
                #总伤害
                总伤害数值+=int(统计详情[i*4+1])
                每行详情[4].setText(self.格式化输出(str(int(统计详情[i*4+1]))))
                每行详情[4].move(448, 50+j*29)
                每行详情[4].resize(108,28) 
                #平均伤害
                每行详情[5].setText(self.格式化输出(str(int(统计详情[i*4+2]))))
                每行详情[5].move(555, 50+j*29) 
                每行详情[5].resize(108,28) 
                #占比
                每行详情[6].setText(str(round(统计详情[i*4+3],1))+'%')
                每行详情[6].move(660, 50+j*29)
                每行详情[6].resize(108,28)
     
                for l in range(1,7):
                    每行详情[l].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
                    每行详情[l].setAlignment(Qt.AlignCenter) 
    
        #被动详情
        num=0
        for i in range(0,len(self.角色属性B.技能栏)):
            # Will修改
            if self.角色属性B.技能栏[i].关联技能 != ['无']:
                被动数据=QLabel(输出窗口)
                被动数据.setPixmap(self.技能图片[i])
                tempstr='<font color="#FF0000"><b>'+self.角色属性B.技能栏[i].名称+'</b></font><br>'
                tempstr+='加成倍率：<b>'+str(round(self.角色属性B.技能栏[i].加成倍率(self.角色属性B.武器类型)*100-100,2))+'%</b><br>'
                tempstr+='关联技能：<b>'
                for j in self.角色属性B.技能栏[i].关联技能:
                    tempstr+=j
                    if j != self.角色属性B.技能栏[i].关联技能[-1]:
                        tempstr+=','
                tempstr+='</b><br>'
                # Will添加
                if self.角色属性B.技能栏[i].关联技能2 != ['无']:
                    tempstr+='加成倍率：<b>'+str(round(self.角色属性B.技能栏[i].加成倍率2(self.角色属性B.武器类型)*100-100,2))+'%</b><br>'
                    tempstr+='关联技能：<b>'
                    for k in self.角色属性B.技能栏[i].关联技能2:
                        tempstr+=k
                        if k != self.角色属性B.技能栏[i].关联技能2[-1]:
                            tempstr+=','
                    tempstr+='</b><br>'
                if self.角色属性B.技能栏[i].关联技能3 != ['无']:
                    tempstr+='加成倍率：<b>'+str(round(self.角色属性B.技能栏[i].加成倍率3(self.角色属性B.武器类型)*100-100,2))+'%</b><br>'
                    tempstr+='关联技能：<b>'
                    for l in self.角色属性B.技能栏[i].关联技能3:
                        tempstr+=l
                        if l != self.角色属性B.技能栏[i].关联技能3[-1]:
                            tempstr+=','
                    tempstr+='</b><br>'
                被动数据.setToolTip(tempstr)
                被动数据.move(300+num*40, 500)
                被动等级=QLabel(输出窗口)
                被动等级.setText('Lv.'+str(实际技能等级[i]))
                被动等级.move(300-6+num*40, 480)
                被动等级.resize(40,28)
                if 实际技能等级[i] != 0:
                    被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
                else:
                    被动等级.setStyleSheet("QLabel{font-size:12px;color:rgb(255,0,0)}")
                被动等级.setAlignment(Qt.AlignCenter)  
                num+=1
    
        适用中的套装=QLabel(装备名称[11],输出窗口)
        适用中的套装.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")   
        适用中的套装.move(132, 138+180)
        适用中的套装.resize(132,18)
        适用中的套装.setAlignment(Qt.AlignCenter)   
    
        神话所在套装 = '无'
        for i in range(0,11):
            if 装备列表[装备序号[装备名称[i]]].品质 == '神话':
                神话所在套装 = 装备列表[装备序号[装备名称[i]]].所属套装
        for i in range(0,len(套装名称)):
            适用套装名称=QLabel(输出窗口)
            适用套装名称.setText(套装名称[i])
            适用套装名称.move(132,158+180+i*20)
            适用套装名称.resize(132,18)
            适用套装名称.setAlignment(Qt.AlignCenter)  
            if 神话所在套装 == 套装名称[i].split('[')[0]:
                适用套装名称.setStyleSheet("QLabel{font-size:12px;color:rgb(224,146,151)}")   
            else:
                适用套装名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")  
    
        面板显示=[]
        for i in range(0,17):
            面板显示.append(QLabel(输出窗口))        
    
        面板显示[0].setText(str(int(self.角色属性B.面板力量())))
        面板显示[1].setText(str(int(self.角色属性B.面板物理攻击力())))
        面板显示[2].setText(str(int(self.角色属性B.面板智力())))
        面板显示[3].setText(str(int(self.角色属性B.面板魔法攻击力())))
        
        面板显示[5].setText(str(int(self.角色属性B.火属性强化)))
        面板显示[6].setText(str(int(self.角色属性B.冰属性强化)))
        面板显示[7].setText(str(int(self.角色属性B.光属性强化)))
        面板显示[8].setText(str(int(self.角色属性B.暗属性强化)))
        
        tempstr = '<font color="#FFFFFF">'+str(int(C.站街独立攻击力()))+'</font>   '
        tempstr += '<font color="#96FF32">'+str(int(self.角色属性B.面板独立攻击力()))+'</font>'
        面板显示[4].setText(tempstr)

        面板显示[9].setText(str(int(C.站街力量())))
        面板显示[10].setText(str(int(C.站街物理攻击力())))
        面板显示[11].setText(str(int(C.站街智力())))
        面板显示[12].setText(str(int(C.站街魔法攻击力())))
        
        面板显示[13].setText(str(int(C.火属性强化)))
        面板显示[14].setText(str(int(C.冰属性强化 + C.冰属性强化加成())))
        面板显示[15].setText(str(int(C.光属性强化)))
        面板显示[16].setText(str(int(C.暗属性强化)))
        
        const = 139
        count = 0
        for i in  [9,10,0,1]:
            面板显示[i].move(20,const + count * 18)
            count += 1

        count = 0
        for i in  [11,12,2,3]:
            面板显示[i].move(150,const + count * 18)
            count += 1

        面板显示[4].move(150,const + count * 18)

        count = 5
        for i in  [5,6,7,8]:
            面板显示[i].move(150,const + count * 18)
            count += 1

        count = 5
        for i in  [13,14,15,16]:
            面板显示[i].move(20,const + count * 18)
            count += 1
      
        for i in range(0,len(面板显示)):
            if i >= 9:
                面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            else:
                面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(150,255,30)}")
            面板显示[i].resize(100,18)
            面板显示[i].setAlignment(Qt.AlignRight)
    
        tempstr=[]
        tempstr.append('力智：'+str(int(round(self.角色属性B.百分比力智*100,0)))+'%') 
        tempstr.append('三攻：'+str(int(round(self.角色属性B.百分比三攻*100,0)))+'%') 
        tempstr.append('黄字：'+str(int(round(self.角色属性B.伤害增加*100,0)))+'%')
        tempstr.append('白字：'+str(int(round(self.角色属性B.附加伤害*100,0)))+'%')
        tempstr.append('属白：'+str(int(round(self.角色属性B.属性附加*100,0)))+'%')
        tempstr.append('爆伤：'+str(int(round(self.角色属性B.暴击伤害*100,0)))+'%')
        tempstr.append('终伤：'+str(int(round(self.角色属性B.最终伤害*100,0)))+'%')
        tempstr.append('技攻：'+str(int(round(self.角色属性B.技能攻击力*100-100,0)))+'%')
        tempstr.append('持续：'+str(int(round(self.角色属性B.持续伤害*100,0)))+'%') 
        
        j=318
        for i in tempstr:
            templab=QLabel(输出窗口)
            templab.setText(i)
            templab.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            templab.move(20,j)
            templab.resize(305,18)
            templab.setAlignment(Qt.AlignLeft)
            j+=18
    
        总伤害=QLabel(输出窗口)
        总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        总伤害.setText(self.格式化输出(str(总伤害数值)))
        总伤害.resize(250,36)
        总伤害.move(10,517)
        总伤害.setAlignment(Qt.AlignCenter) 
    
        初始x=10;初始y=31
    
        图片列表 = []
    
        for i in range(0,12):
            图片列表.append(self.装备图片[装备序号[self.排行数据[index][i]]])
    
        偏移量=187
        x坐标=[32,0,0,32,0,偏移量,偏移量+32,偏移量+32,偏移量,偏移量,偏移量+32,32]
        y坐标=[0,0,32,32,64,0,0,32,64,32,64,64]
    
        tempstr=[]
        for i in range(0,12):
            tempstr.append('')
            装备 =  装备列表[装备序号[self.角色属性B.装备栏[i]]]
            if 装备.所属套装 != '智慧产物':  
                if self.角色属性B.强化等级[i]!=0:
                    if i==8:
                        tempstr[i]+='<font color="#00A2E8">+'+str(self.角色属性B.强化等级[i])+' 强化: '
                        tempstr[i]+='三攻 + '+str(耳环计算(100,装备.品质,self.角色属性B.强化等级[i]))+'</font>'
                    if i in [9,10]:
                        tempstr[i]+='<font color="#00A2E8">+'+str(self.角色属性B.强化等级[i])+' 强化: '
                        tempstr[i]+='四维 + '+str(左右计算(100,装备.品质,self.角色属性B.强化等级[i])) +'</font>'
                    if i==11:
                        tempstr[i]+='<font color="#00A2E8">+'+str(self.角色属性B.强化等级[i])+' 强化: '
                        tempstr[i]+='物理攻击力 + '+str(武器计算(100,装备.品质,self.角色属性B.强化等级[i],装备.类型,'物理'))+'</font><br>'
                        tempstr[i]+='<font color="#00A2E8">+'+str(self.角色属性B.强化等级[i])+' 强化: '
                        tempstr[i]+='魔法攻击力 + '+str(武器计算(100,装备.品质,self.角色属性B.强化等级[i],装备.类型,'魔法'))+'</font>'

                if self.角色属性B.武器锻造等级!=0:
                    if i==11:
                        tempstr[i]+='<br><font color="#00A2E8">+'+str(self.角色属性B.武器锻造等级)+'   锻造: '
                        tempstr[i]+='独立攻击力 + '+str(锻造计算(100,装备.品质,self.角色属性B.武器锻造等级))+'</font>'

                if self.角色属性B.是否增幅[i]==1:
                    if tempstr[i] !='':
                        tempstr[i]+='<br>'
                    tempstr[i]+='<font color="#FF00FF">+'+str(self.角色属性B.强化等级[i])+' 增幅: '
                    if '物理' in self.角色属性B.伤害类型:
                        tempstr[i]+='异次元力量 + '+str(增幅计算(100,装备.品质,self.角色属性B.强化等级[i]))+'</font>'
                    else:
                        tempstr[i]+='异次元智力 + '+str(增幅计算(100,装备.品质,self.角色属性B.强化等级[i]))+'</font>'
 
        for i in range(0,12):
            装备图标=QLabel(输出窗口)
            装备图标.setMovie(图片列表[i])
            图片列表[i].start()
            装备图标.resize(26,26)
            装备图标.move(初始x+x坐标[i],初始y+y坐标[i])
            装备图标.setAlignment(Qt.AlignCenter) 

            if self.角色属性B.装备栏[i] == 百变怪:
                图标遮罩=QLabel(输出窗口)
                图标遮罩.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                图标遮罩.resize(26,26)
                图标遮罩.move(初始x+x坐标[i],初始y+y坐标[i])
                if tempstr[i]!='':
                    图标遮罩.setToolTip('<b>'+"{:<12}".format(self.角色属性B.装备栏[i])+'<br>'+tempstr[i]+'</b>')
                else:
                    图标遮罩.setToolTip('<b>'+"{:<12}".format(self.角色属性B.装备栏[i])+'</b>')
            else:
                if tempstr[i]!='':
                    装备图标.setToolTip('<b>'+"{:<12}".format(self.角色属性B.装备栏[i])+'<br>'+tempstr[i]+'</b>')
                else:
                    装备图标.setToolTip('<b>'+"{:<12}".format(self.角色属性B.装备栏[i])+'</b>')
           
        for i in range(0,12):
            装备 =  装备列表[装备序号[self.角色属性B.装备栏[i]]]
            打造状态=QLabel(输出窗口)
            if 装备.所属套装 != '智慧产物':    
                打造状态.setText('+'+str(self.角色属性B.强化等级[i]))
                if self.角色属性B.是否增幅[i]==1:
                    打造状态.setStyleSheet("QLabel{color:rgb(228,88,169);font-size:12px;font-weight:Bold}")
                else:
                    打造状态.setStyleSheet("QLabel{color:rgb(25,199,234);font-size:12px;font-weight:Bold}")
                
            else:
                打造状态.setText('+'+str(self.角色属性B.改造等级[i]))
                打造状态.setStyleSheet("QLabel{color:rgb(249,141,62);font-size:12px;font-weight:Bold;}")
            
            打造状态.move(初始x+x坐标[i]+13,初始y+y坐标[i]-8)
        
        装备 =  装备列表[装备序号[self.角色属性B.装备栏[11]]]
        if 装备.所属套装 != '智慧产物' and self.角色属性B.武器锻造等级 != 0:
            打造状态=QLabel(输出窗口)
            打造状态.setText('+'+str(self.角色属性B.武器锻造等级))
            打造状态.setStyleSheet("QLabel{color:rgb(232,104,24);font-size:12px;font-weight:Bold}")
            打造状态.move(初始x+x坐标[11]+13,初始y+y坐标[11]+20)

        输出窗口.show()  