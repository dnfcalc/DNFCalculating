from PublicReference.base import *

class 毒神绝技能0(主动技能):
    名称 = '抛沙'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 409.1
    成长 = 52.6
    CD = 3.0
    TP成长 = 0.08
    TP上限 = 7

class 毒神绝技能1(主动技能):
    名称 = '擒月炎'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2390.0
    成长 = 220.5
    CD = 5.5
    TP成长 = 0.10
    TP上限 = 7

class 毒神绝技能2(主动技能):
    名称 = '毒影针'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2897.7
    成长 = 227.3
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

class 毒神绝技能3(主动技能):
    名称 = '双重投掷'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    是否有伤害 = 0
    关联技能 = ['抛沙']
    关联技能2 = ['街头风暴']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.60 + 0.04* self.等级, 5)
    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.98 + 0.02* self.等级, 5)

class 毒神绝技能4(被动技能):
    名称 = '爪精通'
    所在等级 = 25
    等级上限 = 30
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.01* self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.01* self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.01* self.等级, 5)

class 毒神绝技能5(主动技能):
    名称 = '砖袭'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2094.6
    成长 = 236.9
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

class 毒神绝技能6(主动技能):
    名称 = '挑衅'
    所在等级 = 35
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.15 + 0.01* self.等级, 5)

class 毒神绝技能7(主动技能):
    名称 = '伏虎霸王拳'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 6060.0
    成长 = 680.5
    CD = 15.0
    TP上限 = 7
    TP成长 = 0.089

class 毒神绝技能8(被动技能):
    名称 = '狂霸王拳'
    所在等级 = 40
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['伏虎霸王拳']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.03* self.等级, 5)

class 毒神绝技能9(主动技能):
    名称 = '裂地飞沙'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 10339.8
    成长 = 799.8
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.27
        self.CD *= 1.00

class 毒神绝技能10(主动技能):
    名称 = '毒雷引爆'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 8649.44
    成长 = 665.56
    CD = 24.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.07
        self.CD *= 0.90

class 毒神绝技能11(主动技能):
    名称 = '街头风暴'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 8132.2
    成长 = 1622.8
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.227

class 毒神绝技能12(被动技能):
    名称 = '猛毒之血'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.015 * self.等级, 5)

class 毒神绝技能13(主动技能):
    名称 = '死亡毒雾'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 25214.0
    成长 = 7742.0
    CD = 145

class 毒神绝技能14(主动技能):
    名称 = '猛毒擒月炎'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 14442.3
    成长 = 1631.3
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.173
        self.CD *= 0.80


class 毒神绝技能15(主动技能):
    名称 = '爆碎砖袭'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 16047.5
    成长 = 1789.6
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.119
        self.CD *= 1.00

class 毒神绝技能16(被动技能):
    名称 = '猛毒之伤'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)

class 毒神绝技能17(主动技能):
    名称 = '连环毒爆弹'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 40368.8
    成长 = 4558.2
    CD = 40.0

class 毒神绝技能18(主动技能):
    名称 = '毒龙轰天雷'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 39663.2
    成长 = 4394.8
    CD = 45.0

class 毒神绝技能19(主动技能):
    名称 = '万毒噬心诀'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 47534.2
    成长 = 14404.3
    CD = 180.0
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

class 毒神绝技能20(主动技能):
    名称 = '万毒噬心诀x4'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 7179
    成长 = 1258
    CD = 1.0

class 毒神绝技能21(主动技能):
    名称 = '万毒噬心诀x5'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 10410
    成长 = 1617.5
    CD = 1.5


class 毒神绝技能22(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 毒神绝技能23(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 毒神绝技能24(被动技能):
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

毒神绝技能列表 = []
i = 0
while i >= 0:
    try:
        exec('毒神绝技能列表.append(毒神绝技能'+str(i)+'())')
        i += 1
    except:
        i = -1

毒神绝技能序号 = dict()
for i in range(len(毒神绝技能列表)):
    毒神绝技能序号[毒神绝技能列表[i].名称] = i

毒神绝一觉序号 = 0
毒神绝二觉序号 = 19
毒神绝三觉序号 = 0
for i in 毒神绝技能列表:
    if i.所在等级 == 50:
        毒神绝一觉序号 = 毒神绝技能序号[i.名称]
    if i.所在等级 == 100:
        毒神绝三觉序号 = 毒神绝技能序号[i.名称]

毒神绝护石选项 = ['无']
for i in 毒神绝技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        毒神绝护石选项.append(i.名称)

毒神绝符文选项 = ['无']
for i in 毒神绝技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        毒神绝符文选项.append(i.名称)

class 毒神绝角色属性(角色属性):

    职业名称 = '毒神绝'

    武器选项 = ['爪']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比']
    
    #默认
    伤害类型 = '魔法百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量','智力']

    主BUFF = 9.50
   
    #基础属性(含唤醒)
    基础力量 = 976.0
    基础智力 = 959.0
    
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

    死亡毒雾力智开关 = 0
  
    def __init__(self):
        self.技能栏= copy.deepcopy(毒神绝技能列表)
        self.技能序号= copy.deepcopy(毒神绝技能序号)

    def 站街力量(self):
        return int(max(self.力量,self.智力))

    def 站街智力(self):
        return self.站街力量()

    def 面板力量(self):
        if self.系统奶 == False:
            return max(int(int((self.力量 + self.进图力量)) * (1 + self.百分比力智)),int(int((self.智力 + self.进图智力)) * (1 + self.百分比力智)))
        else:
            return max(int(int((self.力量 + int((self.力量 - self.基础力量) * 1.35 + 7664) +self.进图力量)) * (1 + self.百分比力智)),int(int((self.智力 + int((self.智力 - self.基础智力) * 1.35 + 7664) +self.进图智力)) * (1 + self.百分比力智)))

    def 面板智力(self):
        return self.面板力量()

    def 装备基础(self):
        self.力量 += 防具力量[self.防具类型]
        self.智力 += 防具智力[self.防具类型]
        if 装备列表[装备序号[self.装备栏[0]]].品质 == '神话':
            self.力量 += 神话上衣额外力量[self.防具类型]
            self.智力 += 神话上衣额外智力[self.防具类型]

        for i in [0,1,2,3,4]:
            if 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 精通计算(100,装备列表[装备序号[self.装备栏[i]]].品质,self.强化等级[i],部位列表[i])
            else:
                x = 精通计算(100,装备列表[装备序号[self.装备栏[i]]].品质,0,部位列表[i])
            if '力量' in self.防具精通属性:
                self.力量 += x
            if '智力' in self.防具精通属性:
                self.智力 += x
  

        for i in [9,10]:
            if 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 左右计算(100,'史诗',self.强化等级[i])
                self.力量 += x
                self.智力 += x

        for i in range(0,12):
            if self.是否增幅[i] and 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 增幅计算(100,装备列表[装备序号[self.装备栏[i]]].品质,self.强化等级[i])
                self.力量 += x
                self.智力 += x

        if 装备列表[装备序号[self.装备栏[11]]].所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(100,'史诗',self.强化等级[11],self.武器类型,'物理')
            self.魔法攻击力 += 武器计算(100,'史诗',self.强化等级[11],self.武器类型,'魔法')
            self.独立攻击力 += 锻造计算(100,'史诗',self.武器锻造等级)
        
        if 装备列表[装备序号[self.装备栏[8]]].所属套装 != '智慧产物':
            x = 耳环计算(100,装备列表[装备序号[self.装备栏[8]]].品质,self.强化等级[8])
            self.物理攻击力 += x
            self.魔法攻击力 += x
            self.独立攻击力 += x

        for i in [5,6,7,8,9,10,11]:
            self.力量 += 装备列表[装备序号[self.装备栏[i]]].力量
            self.智力 += 装备列表[装备序号[self.装备栏[i]]].智力
            self.物理攻击力 += 装备列表[装备序号[self.装备栏[i]]].物理攻击力
            self.魔法攻击力 += 装备列表[装备序号[self.装备栏[i]]].魔法攻击力
            self.独立攻击力 += 装备列表[装备序号[self.装备栏[i]]].独立攻击力

    def 伤害计算(self, x = 0):
        self.装备基础()

        for i in self.装备栏:
            装备列表[装备序号[i]].城镇属性(self)
            装备列表[装备序号[i]].进图属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].城镇属性(self)
            套装列表[套装序号[i]].进图属性(self)

        self.所有属性强化(self.进图属强)
        # Will添加
        self.CD倍率计算()
        self.加算冷却计算()

        if self.死亡毒雾力智开关 == 1:
            self.力量+= self.技能栏[self.技能序号['死亡毒雾']].等级 * 6.5 + 91
            self.智力+= self.技能栏[self.技能序号['死亡毒雾']].等级 * 6.5 + 91

        基准倍率 = 1.5 * (1 - 443215 / (443215 + 20000)) * (0.9 + self.主BUFF/10)

        面板 = (self.面板智力()/250+1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻)
 
        属性倍率=1.05+0.0045*max(self.火属性强化,self.冰属性强化,self.光属性强化,self.暗属性强化)
        增伤倍率=1+self.伤害增加
        增伤倍率*=1+self.暴击伤害
        增伤倍率*=1+self.最终伤害
        增伤倍率*=self.技能攻击力
        增伤倍率*=1+self.持续伤害*(1-0.1*self.持续伤害计算比例)
        增伤倍率*=1+self.附加伤害+self.属性附加*属性倍率
        伤害指数=面板*属性倍率*增伤倍率*基准倍率/100
        
        self.被动倍率计算()

        self.技能栏[self.技能序号['万毒噬心诀x4']].等级 = self.技能栏[self.技能序号['万毒噬心诀']].等级
        self.技能栏[self.技能序号['万毒噬心诀x5']].等级 = self.技能栏[self.技能序号['万毒噬心诀']].等级

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
                    if self.次数输入[self.技能序号[i.名称]] != '0':
                        技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]])+i.基础释放次数)
                    else:
                        技能释放次数.append(0)
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

class 毒神绝(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 毒神绝角色属性()
        self.角色属性A = 毒神绝角色属性()
        self.角色属性B = 毒神绝角色属性()
        self.一觉序号 = 毒神绝一觉序号
        self.二觉序号 = 毒神绝二觉序号
        self.三觉序号 = 毒神绝三觉序号
        self.护石选项 = copy.deepcopy(毒神绝护石选项)
        self.符文选项 = copy.deepcopy(毒神绝符文选项)

     
    def 界面(self):
        self.setWindowTitle(self.角色属性A.职业名称 + "搭配计算器")
        self.icon = QIcon('./ResourceFiles/'+self.角色属性A.职业名称 + '/技能/BUFF.png')
        self.setWindowIcon(self.icon)
        #窗口大小
        self.setFixedSize(1120, 680)

        背景颜色 = QLabel(self)
        背景颜色.resize(self.width(),self.height())
        背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1)}")

        主背景透明度 = QGraphicsOpacityEffect()
        主背景透明度.setOpacity(0.25)
        self.主背景图片 = QPixmap('./ResourceFiles/'+self.角色属性A.职业名称 + "/bg.jpg")
        主背景 = QLabel(self)
        主背景.setPixmap(self.主背景图片)
        主背景.setGraphicsEffect(主背景透明度)

        self.技能图片 = []
        for i in self.角色属性A.技能栏:
            path = './ResourceFiles/'+self.角色属性A.职业名称 + "/技能/" + i.名称 + ".png"
            self.技能图片.append(QPixmap(path))
        
        self.输出窗口列表 = []
        self.排行窗口列表 = []
        
        self.装备图片 = []
        self.遮罩透明度 = []
        self.装备图片按钮 = []
        for i in 装备列表:
            self.遮罩透明度.append(QGraphicsOpacityEffect())
            self.装备图片按钮.append('')
        self.装备选择状态 = []
        self.装备条件选择 = []
        for i in 装备列表:
            path = './ResourceFiles/img/装备/' + str(装备序号[i.名称]) + '.gif'
            self.装备图片.append(QMovie(path))
            self.装备选择状态.append(0)
        self.输出背景图片 = QPixmap('./ResourceFiles/'+self.角色属性A.职业名称 + "/输出背景.png")
        self.有效防具套装 = []
        self.有效首饰套装 = []
        self.有效特殊套装 = []
        self.有效上链左套装 = []
        self.有效镯下右套装 = []
        self.有效环鞋指套装 = []
        self.有效总套装列表 = [self.有效防具套装, self.有效首饰套装, self.有效特殊套装, self.有效上链左套装, self.有效镯下右套装, self.有效环鞋指套装]
        self.有效武器列表 = []
        self.组合名称选择 = []
        self.有效穿戴组合 = []
        self.有效穿戴套装 = []
        self.百变怪列表 = []
        self.有效部位列表 = []
        self.排行数据 = []

        # 工具栏
        self.frame_tool = QFrame(self)
        self.frame_tool.setGeometry(0, 0, self.width(), 24)

        self.页面名称 = ["装备选择", "其它设置", "基础属性"]
        self.页面数量 = len(self.页面名称)
        self.btn_group = QButtonGroup(self.frame_tool)
        for i in range(0, self.页面数量):
            self.window_btn = QToolButton(self.frame_tool)
            self.window_btn.setText(self.页面名称[i])
            self.window_btn.resize(int(self.width() / self.页面数量), 24)
            self.window_btn.move(self.window_btn.width() * i, 0)
            self.window_btn.setStyleSheet('QToolButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);} QToolButton:hover{background-color:rgba(65,105,225,0.8)}')
            self.window_btn.clicked.connect(lambda state, index = i: self.click_window(index))
            self.btn_group.addButton(self.window_btn, i)

        # 2. 工作区域
        self.main_frame = QFrame(self)
        self.main_frame.setGeometry(0, 25, self.width(), self.height() - self.frame_tool.height())

        # 创建堆叠布局
        self.stacked_layout = QStackedLayout(self.main_frame)

        # 第一个布局界面
        self.main_frame1 = QMainWindow()
        水平间距 = [0, 350, 640]
        counter1 = 0
        for 布局列表 in [防具套装, 上链左套装 + 镯下右套装 + 环鞋指套装 , 首饰套装 + 特殊套装]:
            counter2 = 0
            for 名称 in 布局列表:
                for i in 套装列表:
                    if i.名称 == 名称 and i.件数 == 2:
                        self.按钮 = QPushButton(i.名称, self.main_frame1)
                        self.按钮.move(水平间距[counter1] + 10, 10 + counter2 * 32)
                        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
                        self.按钮.resize(120, 28)
                        self.按钮.clicked.connect(lambda state, index = i.名称: self.套装按钮点击事件(index))
                        counter3 = 0
                        for 品质 in ['神话', '史诗']:
                            for j in range(0,len(装备列表)):
                                if 装备列表[j].所属套装 == i.名称 and 装备列表[j].品质 == 品质:
                                    self.图片 = QLabel(self.main_frame1)
                                    self.图片.setMovie(self.装备图片[j])
                                    self.装备图片[j].start()
                                    self.图片.resize(28, 28)
                                    self.图片.move(水平间距[counter1] + 150 + 32 * counter3, 10 + counter2 * 32)
                                    self.按钮 = QPushButton(self.main_frame1)
                                    self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                                    self.按钮.resize(28, 28)
                                    self.按钮.setToolTip(装备列表[j].名称 + '\n'+ 装备列表[j].类型 + '-' + 装备列表[j].部位)
                                    self.遮罩透明度[j].setOpacity(0.5)
                                    self.按钮.setGraphicsEffect(self.遮罩透明度[j])
                                    self.按钮.clicked.connect(lambda state, index = j: self.装备图标点击事件(index, 10))
                                    self.装备图片按钮[j] = self.按钮
                                    self.装备图片按钮[j].move(水平间距[counter1] + 150 + 32 * counter3, 10 + counter2 * 32)
                                    counter3 += 1
                counter2 += 1
            counter1 += 1
        
        counter5 = 8
        self.按钮 = QPushButton('武器列表', self.main_frame1)
        self.按钮.move(650, 30 + counter5 * 32)
        self.按钮.resize(265,28)
        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
        self.按钮.clicked.connect(lambda state, index = '无': self.套装按钮点击事件(index))
        
        counter4 = 0
        counter5 += 1
        for i in 装备列表:
            if i.部位 == '武器' and i.类型 in self.角色属性A.武器选项:
                self.图片 = QLabel(self.main_frame1)
                self.图片.setMovie(self.装备图片[装备序号[i.名称]])
                self.装备图片[装备序号[i.名称]].start()
                self.图片.resize(28, 28)
                self.图片.move(657 + 55 * counter4, 30 + counter5 * 32)
                self.按钮 = QPushButton(self.main_frame1)
                self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.按钮.resize(28, 28)
                self.按钮.setToolTip(i.名称 + '\n' + i.类型) 
                self.遮罩透明度[装备序号[i.名称]].setOpacity(0.5)
                self.按钮.setGraphicsEffect(self.遮罩透明度[装备序号[i.名称]])
                self.按钮.clicked.connect(lambda state, index = 装备序号[i.名称]: self.装备图标点击事件(index, 10))
                self.装备图片按钮[装备序号[i.名称]] = self.按钮
                self.装备图片按钮[装备序号[i.名称]].move(657 + 55 * counter4, 30 + counter5 * 32)
                counter4 += 1
                if counter4 % 5 == 0:
                    counter5 += 1
                    counter4 = 0
        
        if counter4 != 0:
            counter5 += 1
        self.按钮 = QPushButton('智慧产物', self.main_frame1)
        self.按钮.move(650, 50 + counter5 * 32)
        self.按钮.resize(265,28)
        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
        self.按钮.clicked.connect(lambda state, index = '智慧产物': self.套装按钮点击事件(index))
        
        counter4 = 0
        counter5 += 1
        for i in 装备列表:
            if i.所属套装 == '智慧产物' and i.部位 != '武器':
                self.图片 = QLabel(self.main_frame1)
                self.图片.setMovie(self.装备图片[装备序号[i.名称]])
                self.装备图片[装备序号[i.名称]].start()
                self.图片.resize(28, 28)
                self.图片.move(657 + 55 * counter4, 50 + counter5 * 32)
                self.按钮 = QPushButton(self.main_frame1)
                self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.按钮.resize(28, 28)
                self.按钮.setToolTip(i.名称 + '\n' + i.类型+ '-' + i.部位) 
                self.遮罩透明度[装备序号[i.名称]].setOpacity(0.5)
                self.按钮.setGraphicsEffect(self.遮罩透明度[装备序号[i.名称]])
                self.按钮.clicked.connect(lambda state, index = 装备序号[i.名称]: self.装备图标点击事件(index, 10))
                self.装备图片按钮[装备序号[i.名称]] = self.按钮
                self.装备图片按钮[装备序号[i.名称]].move(657 + 55 * counter4, 50 + counter5 * 32)
                counter4 += 1
                if counter4 % 5 == 0:
                    counter5 += 1
                    counter4 = 0
        
        标签 = QLabel('装备条件设置', self.main_frame1)
        标签.move(940, 5)
        标签.resize(170,20)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        self.装备条件选择.clear()
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['角色熟练度：英雄', '角色熟练度：传说'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['技能栏空位：0', '技能栏空位：1', '技能栏空位：2', '技能栏空位：3', '技能栏空位：4', '技能栏空位：5', '技能栏空位：6'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['命运的抉择：数学期望', '命运的抉择：黄字+35%', '命运的抉择：爆伤+35%', '命运的抉择：白字+35%', '命运的抉择：终伤+35%', '命运的抉择：三攻+35%'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['骰子：数学期望', '骰子：1点', '骰子：2点', '骰子：3点', '骰子：4点', '骰子：5点', '骰子：6点'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['悲剧的残骸：数学期望', '悲剧的残骸：HP高于70%', '悲剧的残骸：HP70-30%', '悲剧的残骸：HP低于30%'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['先知者预言：数学期望', '先知者预言：属白+5%', '先知者预言：技攻+10%', '先知者预言：技攻+15%'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['贫瘠沙漠的遗产：无', '贫瘠沙漠的遗产：霸体', '贫瘠沙漠的遗产：无伤'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['幸运三角：数学期望', '幸运三角：7效果', '幸运三角：77效果', '幸运三角：777效果'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['擎天战甲：过充电状态', '擎天战甲：过负荷状态'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['持续伤害适用：100%', '持续伤害适用：90%', '持续伤害适用：80%', '持续伤害适用：70%', '持续伤害适用：60%', '持续伤害适用：50%', '持续伤害适用：40%', '持续伤害适用：30%', '持续伤害适用：20%', '持续伤害适用：10%', '持续伤害适用：0%'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['军神的隐秘遗产：120%以上', '军神的隐秘遗产：120-100%', '军神的隐秘遗产：100-80%', '军神的隐秘遗产：80-60%', '军神的隐秘遗产：60-40%', '军神的隐秘遗产：40%以下'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['太极天帝剑：阳', '太极天帝剑：阴'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['绿色生命的面容：无', '绿色生命的面容：阴暗面'])
        self.装备条件选择.append(QComboBox(self.main_frame1))
        self.装备条件选择[-1].addItems(['希洛克融合：无','希洛克：奈克斯(伤害增幅)', '希洛克：暗杀者(冷却缩减)', '希洛克：卢克西(觉醒增幅)', '希洛克：罗德斯(霸体抗性)', '希洛克：守门将(45-最低)', '希洛克：守门将(90-平均)', '希洛克：守门将(135-最高)'])
        for i in range(0, len(self.装备条件选择)):
            self.装备条件选择[i].resize(170, 20)
            self.装备条件选择[i].setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QComboBox:hover{background-color:rgba(65,105,225,0.8)}")
            self.装备条件选择[i].move(940, 30 + 28 * i)


        self.装备打造选项=[]
        counter = 0
        for i in 部位列表:
            x = QLabel(i, self.main_frame1)
            x.resize(50,20)
            x.setAlignment(Qt.AlignCenter)
            x.setStyleSheet(标签样式)
            if counter < 5:
                x.move(10 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(270 , 500 + (counter - 5) * 25)
                else:
                    x.resize(95,20)
                    x.move(550 , 500 + (counter - 11) * 30)
            counter += 1

        counter = 0
        for i in 部位列表:
            x = QComboBox(self.main_frame1)
            x.addItems(['强化','增幅'])
            x.resize(55,20)
            x.setStyleSheet(下拉框样式)
            self.装备打造选项.append(x)
            if counter < 5:
                x.move(60 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(330 , 500 + (counter - 5) * 25)
                else:
                    x.move(540 , 500 + (counter - 10) * 30)
            counter += 1
            
        counter = 0
        for i in 部位列表:
            x = QComboBox(self.main_frame1)
            for j in range(0,21):
                x.addItem(str(j))
            x.resize(50,20)
            x.setStyleSheet(下拉框样式)
            self.装备打造选项.append(x)
            if counter < 5:
                x.move(120 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(390 , 500 + (counter - 5) * 25)
                else:
                    x.move(600 , 500 + (counter - 10) * 30)
            counter += 1

        counter = 0
        for i in 部位列表:
            x = QComboBox(self.main_frame1)
            for j in range(0,21):
                x.addItem('改造+' + str(j))
            x.resize(75,20)
            x.setStyleSheet(下拉框样式)
            self.装备打造选项.append(x)
            if counter < 5:
                x.move(180 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(450 , 500 + (counter - 5) * 25)
                else:
                    x.resize(110,20)
                    x.move(540 , 500 + (counter - 9) * 30)
            counter += 1

        x = QComboBox(self.main_frame1)
        for j in range(0,9):
            x.addItem('锻造+' + str(j))
        x.resize(110,20)
        x.move(540 , 504 + (counter - 9) * 30)
        x.setStyleSheet(下拉框样式)
        self.装备打造选项.append(x)

        x = QComboBox(self.main_frame1)
        x.addItems(self.角色属性A.伤害类型选择)
        x.resize(110,20)
        x.move(540 , 504 + (counter - 8) * 30)
        x.setStyleSheet(下拉框样式)
        self.装备打造选项.append(x)

        self.称号 = QComboBox(self.main_frame1)
        self.称号.addItems(['(2020)伟大的意志', '(2019)神选之英杰', '(2020)使徒降临', '(2019)超越极限者', '(2018)神之试炼', '(2015)哥特绮梦'])
        
        self.宠物 = QComboBox(self.main_frame1)
        self.宠物.addItems(['(2020)至尊', '(2019)至尊·进化', '(2020)普通', '(2019)普通'])

        x = QLabel('称号&宠物选择：', self.main_frame1)
        x.resize(130,20)
        x.move(360 , 400)
        x.setAlignment(Qt.AlignCenter)
        x.setStyleSheet(标签样式)
        
        counter = 0
        for x in [self.称号, self.宠物]:
            x.resize(130,20)
            x.move(360 , 430 + counter * 30)
            x.setStyleSheet(下拉框样式)  
            counter += 1    

        x = QPushButton('一键全选', self.main_frame1)
        x.clicked.connect(lambda state, index = 1: self.批量选择(index))
        x.move(505 , 400)
        x.resize(115, 24)
        x.setStyleSheet(按钮样式)

        x = QPushButton('一键清空',self.main_frame1)
        x.clicked.connect(lambda state, index = 0: self.批量选择(index))
        x.move(505 , 430)
        x.resize(115, 24)
        x.setStyleSheet(按钮样式)

        x = QPushButton('一键10/12/8/5',self.main_frame1)
        x.clicked.connect(lambda state: self.批量打造())
        x.move(505 , 460)
        x.resize(115, 24)
        x.setStyleSheet(按钮样式)

        self.百变怪选项 = QCheckBox('百变怪   ', self.main_frame1)
        self.百变怪选项.move(660, 613)
        self.百变怪选项.resize(80, 24)
        self.百变怪选项.setToolTip('仅在极速模式和套装模式下生效')
        self.百变怪选项.setStyleSheet(复选框样式)

        self.计算模式选择 = QComboBox(self.main_frame1)
        self.计算模式选择.addItems(['计算模式：极速模式', '计算模式：套装模式', '计算模式：单件模式'])
        self.计算模式选择.move(750, 613)
        self.计算模式选择.resize(235, 24)
        self.计算模式选择.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QComboBox:hover{background-color:rgba(65,105,225,0.8)}")


        self.神话排名选项 = QCheckBox('神话排名模式', self.main_frame1)
        self.神话排名选项.move(880, 580)
        self.神话排名选项.resize(100, 24)
        self.神话排名选项.setToolTip('仅显示有神话的组合，且每件神话装备只会出现一次')
        self.神话排名选项.setStyleSheet(复选框样式)

        self.显示选项 = QCheckBox('亿为单位显示', self.main_frame1)
        self.显示选项.move(990, 580)
        self.显示选项.resize(100, 24)
        self.显示选项.setStyleSheet(复选框样式)

        self.计算按钮1 = QPushButton('开始计算', self.main_frame1)
        self.计算按钮1.clicked.connect(lambda state: self.计算())
        self.计算按钮1.move(990, 610)
        self.计算按钮1.resize(100, 30)
        self.计算按钮1.setStyleSheet(按钮样式)

        # 第二个布局界面
        self.main_frame2 = QMainWindow()

        #技能等级、TP、次数输入、宠物次数
        self.BUFF输入 = QLineEdit(self.main_frame2)
        self.时间输入 = QComboBox(self.main_frame2)
        self.护石第一栏 = QComboBox(self.main_frame2)
        self.护石第二栏 = QComboBox(self.main_frame2)
        self.符文 = []
        self.符文效果 = []

        self.觉醒选择状态 = 2
        
        self.等级调整 = []
        self.TP输入 = []
        self.次数输入 = []
        self.宠物次数 = []
        
        for i in self.角色属性A.技能栏:
            self.等级调整.append(QComboBox(self.main_frame2))
            if i.是否有伤害 == 1 and i.TP上限 != 0:
                self.TP输入.append(QComboBox(self.main_frame2))
            else:
                self.TP输入.append('')
            if i.是否有伤害 == 1:
                self.次数输入.append(QComboBox(self.main_frame2))
                self.宠物次数.append(QComboBox(self.main_frame2))
            else:
                self.次数输入.append('')
                self.宠物次数.append('')
        
        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.所在等级 == 50 or i.所在等级 == 85:
                for j in range(0, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
            else:
                for j in range(- i.基础等级, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
        
            if i.是否有伤害 == 1 and i.TP上限 != 0:
                for j in range(0, i.TP上限+1):
                    self.TP输入[序号].addItem(str(j))
        
            if i.是否有伤害 == 1:
                self.次数输入[序号].addItem('/CD')
                for j in range(0, 100):
                    self.次数输入[序号].addItem(str(j))
                    self.宠物次数[序号].addItem(str(j))
        
        #三觉强化选择
        self.一觉遮罩透明度 = QGraphicsOpacityEffect()
        self.一觉遮罩透明度.setOpacity(0.5)
        self.二觉遮罩透明度 = QGraphicsOpacityEffect()
        self.二觉遮罩透明度.setOpacity(0.0)

        横坐标=10
        纵坐标=0
        横坐标偏移量=60
        纵坐标偏移量=30
        词条框宽度=48
        行高 = 20
        
        counter=0
        for i in ["契约满级","等级调整"," TP等级","释放次数","宠物次数"]:
            x=QLabel(i, self.main_frame2)
            x.move(横坐标+横坐标偏移量-30+50*counter,纵坐标)
            x.setStyleSheet(标签样式)
            counter+=1
        
        纵坐标+=20
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                x=QLabel(self.main_frame2)
                x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
                x.resize(28,28)
                tempstr='<font color="#FF0000"><b>'+i.名称+'</b></font><br>'
                tempstr+='所在等级：<b>'+str(i.所在等级)+'</b><br>'
                tempstr+='等级上限：<b>'+str(i.等级上限)+'</b>'
                if i.是否主动==1:
                    tempstr+='<br>百分比：<b>'+str(int(i.基础))+' + 等级 x '+str(int(i.成长))+'</b>'
                    if i.TP上限 !=0:
                        tempstr+='<br>TP成长：<b>'+str(int(i.TP成长*100))+'%</b>'
                        tempstr+='<br>TP上限：<b>'+str(i.TP上限)+'</b>'
                x.setToolTip(tempstr)
                x.move(横坐标,纵坐标+7)
                横坐标+=40
                x=QLabel('Lv'+str(i.基础等级), self.main_frame2)
                x.resize(40,28)
                x.move(横坐标,纵坐标+7)
                x.setStyleSheet(标签样式)
                横坐标+=40
                self.等级调整[self.角色属性A.技能序号[i.名称]].resize(词条框宽度,行高)
                self.等级调整[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标+10)
                self.等级调整[self.角色属性A.技能序号[i.名称]].setStyleSheet(下拉框样式)
                横坐标-=80
                纵坐标+=纵坐标偏移量
        
        横坐标=横坐标+80+50
        纵坐标=30
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                if i.是否主动==1:
                    if i.TP上限!=0:
                        self.TP输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                        self.TP输入[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标)
                        self.TP输入[self.角色属性A.技能序号[i.名称]].setStyleSheet(下拉框样式)
                纵坐标+=纵坐标偏移量
        
        横坐标=横坐标+50
        纵坐标=30
        
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 1:
                if i.是否主动==1:
                    self.次数输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                    self.次数输入[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标)
                    self.次数输入[self.角色属性A.技能序号[i.名称]].setStyleSheet(下拉框样式)
                    self.宠物次数[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
                    self.宠物次数[self.角色属性A.技能序号[i.名称]].move(横坐标+50,纵坐标)
                    self.宠物次数[self.角色属性A.技能序号[i.名称]].setStyleSheet(下拉框样式)
                纵坐标+=纵坐标偏移量

        横坐标=横坐标+120
        纵坐标=20
        for i in self.角色属性A.技能栏:
            if i.是否有伤害 == 0:
                x=QLabel(self.main_frame2)
                x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
                x.resize(28,28)
                tempstr='<font color="#FF0000"><b>'+i.名称+'</b></font><br>'
                tempstr+='所在等级：<b>'+str(i.所在等级)+'</b><br>'
                tempstr+='等级上限：<b>'+str(i.等级上限)+'</b>'
                x.setToolTip(tempstr)
                x.move(横坐标,纵坐标+7)
                横坐标+=40
                x=QLabel('Lv'+str(i.基础等级), self.main_frame2)
                x.resize(40,28)
                x.move(横坐标,纵坐标+7)
                x.setStyleSheet(标签样式)
                横坐标+=40
                self.等级调整[self.角色属性A.技能序号[i.名称]].resize(词条框宽度,行高)
                self.等级调整[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标+10)
                self.等级调整[self.角色属性A.技能序号[i.名称]].setStyleSheet(下拉框样式)
                横坐标-=80
                纵坐标+=纵坐标偏移量
        
        x=横坐标+20;y=纵坐标+60
        self.觉醒选择=QLabel(self.main_frame2)
        self.觉醒选择.setPixmap(QPixmap('./ResourceFiles/'+self.角色属性A.职业名称 + "/技能/觉醒选择.png"))
        self.觉醒选择.resize(120,100)
        self.觉醒选择.move(x,y-20)
        
        self.BUFF=QLabel(self.main_frame2)
        self.BUFF.setPixmap(QPixmap('./ResourceFiles/'+self.角色属性A.职业名称 + "/技能/BUFF.png"))
        self.BUFF.resize(28,28)
        self.BUFF.move(x-2,y-40)
        self.BUFF.setToolTip( '最高值参考：' + str((self.角色属性A.主BUFF - 1) * 100))
        
        self.BUFF输入.setText(str((self.角色属性A.主BUFF - 1) * 100))
        self.BUFF输入.resize(50, 25)
        self.BUFF输入.move(x+38,y-38)
        self.BUFF输入.setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QLineEdit:hover{background-color:rgba(65,105,225,0.8)}")
        self.BUFF输入.setAlignment(Qt.AlignCenter)

        self.死亡毒雾力智开关=QCheckBox('死亡毒雾力智',self.main_frame2)
        self.死亡毒雾力智开关.resize(100,20)
        self.死亡毒雾力智开关.move(x-5,y+80)
        self.死亡毒雾力智开关.setStyleSheet(复选框样式)

        
        self.一觉图片=QLabel(self.main_frame2)
        self.一觉图片.setPixmap(self.技能图片[self.一觉序号])
        self.一觉图片.resize(28,28)
        self.一觉图片.move(x+7,y+8)
        self.二觉图片=QLabel(self.main_frame2)
        self.二觉图片.setPixmap(self.技能图片[self.二觉序号])
        self.二觉图片.resize(28,28)
        self.二觉图片.move(x+52,y+8)
        self.一觉遮罩=QPushButton(self.main_frame2)
        self.一觉遮罩.resize(38,50)
        self.一觉遮罩.move(x+2,y+5)
        self.一觉遮罩.setStyleSheet("QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}")
        self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
        self.一觉遮罩.clicked.connect(lambda state, index = 1:self.强化觉醒选择(index))
        self.二觉遮罩=QPushButton(self.main_frame2)
        self.二觉遮罩.resize(38,50)
        self.二觉遮罩.move(x+47,y+5)
        self.二觉遮罩.setStyleSheet("QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}")
        self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)
        self.二觉遮罩.clicked.connect(lambda state, index = 2:self.强化觉醒选择(index))

        self.护石第一栏.addItems(self.护石选项)
        self.护石第二栏.addItems(self.护石选项)

        for i in range(0,6):
            self.符文.append(QComboBox(self.main_frame2))
            self.符文[i].addItems(self.符文选项)
            self.符文效果.append(QComboBox(self.main_frame2))
            self.符文效果[i].addItems(符文效果选项)
        
        横坐标=480;纵坐标=20;行高=18
        x=QLabel("护石(第一栏/上)：", self.main_frame2)
        x.move(横坐标,纵坐标-5)
        x.setStyleSheet(标签样式)
        纵坐标+=21
        self.护石第一栏.move(横坐标,纵坐标)
        self.护石第一栏.resize(130, 行高)
        self.护石第一栏.setStyleSheet(下拉框样式)
        纵坐标+=25
        for i in range(0,3):
            tempstr='符文'+str(i+1)+'选择: '
            x=QLabel(tempstr, self.main_frame2)
            x.move(横坐标,纵坐标-5)
            x.setStyleSheet(标签样式)
            纵坐标+=21
            self.符文[i].move(横坐标,纵坐标)
            self.符文[i].resize(130, 行高)
            self.符文[i].setStyleSheet(下拉框样式)
            纵坐标+=21
            self.符文效果[i].move(横坐标,纵坐标)
            self.符文效果[i].resize(130,行高)
            self.符文效果[i].setStyleSheet(下拉框样式)
            纵坐标+=25
        
        横坐标=650;纵坐标=20
        x=QLabel("护石(第二栏/下)：", self.main_frame2)
        x.move(横坐标,纵坐标-5)
        x.setStyleSheet(标签样式)
        纵坐标+=21
        self.护石第二栏.move(横坐标,纵坐标)
        self.护石第二栏.resize(130, 行高)
        self.护石第二栏.setStyleSheet(下拉框样式)
        纵坐标+=25
        for i in range(3,6):
            tempstr='符文'+str(i+1)+'选择: '
            x=QLabel(tempstr, self.main_frame2)
            x.move(横坐标,纵坐标-5)
            x.setStyleSheet(标签样式)
            纵坐标+=21
            self.符文[i].move(横坐标,纵坐标)
            self.符文[i].resize(130, 行高)
            self.符文[i].setStyleSheet(下拉框样式)
            纵坐标+=21
            self.符文效果[i].move(横坐标,纵坐标)
            self.符文效果[i].resize(130,行高)
            self.符文效果[i].setStyleSheet(下拉框样式)
            纵坐标+=25

        self.复选框列表 = []
        self.复选框列表.append(QCheckBox('顶级力量灵药     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('顶级智力灵药     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('斗神之吼秘药     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('赛丽亚的特调酷饮 ', self.main_frame2))
        self.复选框列表.append(QCheckBox('魔界战力释放秘药 ', self.main_frame2))
        self.复选框列表.append(QCheckBox('宠物次数适用(10%)', self.main_frame2))
        self.复选框列表.append(QCheckBox('称号效果触发     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('精神刺激灵药     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('虚祖皇家能量秘药 ', self.main_frame2))
        self.复选框列表.append(QCheckBox('黄金羊毛         ', self.main_frame2))
        self.复选框列表.append(QCheckBox('白兔子(20%全程)  ', self.main_frame2))
        self.复选框列表.append(QCheckBox('雷米迪亚蛋糕     ', self.main_frame2))
        self.复选框列表.append(QCheckBox('系统奶BUFF      ', self.main_frame2))

        counter=0
        for i in self.复选框列表:
            i.setStyleSheet(复选框样式)
            i.resize(125,20)
            i.move(970,10 + counter * 28)
            if counter < 7 and counter > 1:
                i.setChecked(True)
            counter+=1
        if '物理' in self.角色属性A.伤害类型:
            self.复选框列表[0].setChecked(True)
        if '魔法' in self.角色属性A.伤害类型:
            self.复选框列表[1].setChecked(True)

        x=QLabel("时间输入：", self.main_frame2)
        x.move(850, 618)
        x.resize(70, 20)
        x.setStyleSheet(标签样式)
        self.时间输入.addItems(['1', '5', '10', '20', '25', '30', '60'])
        self.时间输入.move(920, 617)
        self.时间输入.resize(50, 20)
        self.时间输入.setStyleSheet(下拉框样式)

        self.计算按钮2 = QPushButton('开始计算', self.main_frame2)
        self.计算按钮2.clicked.connect(lambda state: self.计算())
        self.计算按钮2.move(990, 610)
        self.计算按钮2.resize(100, 30)
        self.计算按钮2.setStyleSheet(按钮样式)

        # 第三个布局界面
        self.main_frame3 = QMainWindow()

        名称列表 = ["上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "耳环", "辅助装备", "魔法石", "武器", "称号", "宠物", "宠物装备","光环", "武器装扮", "皮肤", "时装", "勋章", "快捷栏装备"]
        
        self.属性设置输入 = []
        self.技能设置输入 = []

        宽度 = 43
        
        列名称1 = ["力量", "智力", "物攻", "魔攻", "独立", "属强", "白字"]
        行名称1 = ["工会属性", "训练官BUFF", "戒指", "婚房", "冒险团", "晶体契约", "收集箱", "勋章", "名称装饰卡", "副武器/盾牌", "快捷栏纹章", "  宠物装备-红  ", "  宠物装备-蓝  ", "  宠物装备-绿  ", "宠物附魔", "站街修正", "进图修正"]
        名称 = QLabel("基础细节",self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
        名称.resize(80, 25)
        名称.move(10,5)
       
        for i in range(0, 7):
            名称 = QLabel(列名称1[i],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(宽度, 25)
            名称.move(95 + i*(宽度 + 5), 5)
    
        for j in range(0, 17):
            名称 = QLabel(行名称1[j],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(80, 25)
            名称.move(10, 35 + j*30)
    
        for i in range(0, 7):
            Linelist = []
            for j in range(0, 17):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(95 + i*(宽度 + 5), 35 + j*30)
            self.属性设置输入.append(Linelist)
    
        列名称2 = ["力量", "智力", "物攻", "魔攻", "独立", "属强", "徽章力", "徽章智", "所有攻", "技能"]
        行名称2 = ["上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "左槽", "右槽", "耳环", "武器", "称号", "光环", "武器装扮", "皮肤", "时装"]

        self.列名称 = 列名称1 + 列名称2
        self.行名称 = 行名称1 + 行名称2

        名称 = QLabel(" 附魔&徽章 ",self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
        名称.resize(80, 25)
        名称.move(140+7*宽度,5)
        for i in range(0, 10):
            名称 = QLabel(列名称2[i],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            if i == 9:
                名称.resize(150, 25)
            else:
                名称.resize(宽度, 25)
            名称.move(225+7*宽度 + i*(宽度 + 5), 5)
    
        for j in range(0, 17):
            名称 = QLabel(行名称2[j],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(80, 25)
            名称.move(140+7*宽度, 35 + j*30)
    
        for i in range(0, 9):
            Linelist = []
            for j in range(0, 17):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(225+7*宽度 + i*(宽度 + 5), 35 + j*30)
            self.属性设置输入.append(Linelist)
    
        for j in range(0, 17):
            self.技能设置输入.append(QComboBox(self.main_frame3))
            self.技能设置输入[j].addItem('无')
            self.技能设置输入[j].setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            self.技能设置输入[j].resize(150, 22)
            self.技能设置输入[j].move(225+7*宽度 + 9*(宽度 + 5), 35 + j*30)
    
        for j in [2, 3, 4]:
            self.技能设置输入[j].addItems(['Lv1-30(主动)Lv+1', 'Lv1-50(主动)Lv+1'])
    
        for j in [8, 9, 16]:
            for i in self.角色属性A.技能栏:
                self.技能设置输入[j].addItem(i.名称+'Lv+1')
        self.技能设置输入[12].addItem('Lv1-50(主动)Lv+1')
        self.技能设置输入[13].addItems(['Lv1-30(所有)Lv+1', 'Lv1-50(所有)Lv+1'])

        self.修正列表名称 = ['力智%', '三攻%', '黄字', '白字', '属白', '爆伤', '终伤', '技攻']
        
        Linelist = []
        for i in range(0, len(self.修正列表名称)):
            名称 = QLabel(self.修正列表名称[i],self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet("QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(60, 25)
            名称.move(250 + i*65, 570)
            Linelist.append(QLineEdit(self.main_frame3))
            Linelist[i].setAlignment(Qt.AlignCenter)
            Linelist[i].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            Linelist[i].resize(60, 22)
            Linelist[i].move(250 + i*65, 610)
        self.属性设置输入.append(Linelist)

        self.计算按钮3 = QPushButton('开始计算', self.main_frame3)
        self.计算按钮3.clicked.connect(lambda state: self.计算())
        self.计算按钮3.move(990, 610)
        self.计算按钮3.resize(100, 30)
        self.计算按钮3.setStyleSheet(按钮样式)

        # 把布局界面放进去
        self.stacked_layout.addWidget(self.main_frame1)
        self.stacked_layout.addWidget(self.main_frame2)
        self.stacked_layout.addWidget(self.main_frame3)
    
    def 输入属性(self, 属性):
        super().输入属性(属性)
        if self.死亡毒雾力智开关.isChecked():
            属性.死亡毒雾力智开关 = 1