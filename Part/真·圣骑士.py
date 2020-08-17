from PublicReference.base_buff import *

class 真·圣骑士技能0(被动技能):
    名称 = '启示圣歌'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 31
    额外智力 = 0
    站街生效 = 1
    智力 = [0, 86, 90, 94, 98, 102, 107, 112, 117, 123, 129, 135, 141, 147, 154, 161, 169, 177, 185, 193, 201, 210, 219, 229, 238, 248, 258, 269, 279, 290, 301, 313, 325, 337, 349, 361, 375, 388, 401, 415, 429, 443, 457, 473, 487, 503, 519, 535, 551, 567, 584, 598, 614, 630, 646, 662, 677, 693, 709, 725, 741]
    def 智力加成(self):
        return self.智力[self.等级] + self.额外智力

    def 结算统计(self): 
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class 真·圣骑士技能1(主动技能):
    名称 = '勇气祝福'
    所在等级 = 30
    等级上限 = 40
    基础等级 = 10
    BUFF力量per = 0
    BUFF智力per = 0
    BUFF物攻per = 0
    BUFF魔攻per = 0
    BUFF独立per = 0
    BUFF力量 = 0
    BUFF智力 = 0
    BUFF物攻 = 0
    BUFF魔攻 = 0
    BUFF独立 = 0
    三攻 = [0, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54, 55, 57, 58, 60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 87]
    力智 = [0, 131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247, 256, 264, 273, 282, 291, 300, 309, 318, 327, 336, 345, 353, 362, 371, 380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478]
    def 结算统计(self):
        倍率 = self.适用数值 / 665 + 1
        temp = []
        temp.append(0) #智力
        temp.append(0) #体力
        temp.append(0) #精神
        temp.append(int(round((self.力智[self.等级] + self.BUFF力量) * self.BUFF力量per, 3) * 倍率)) #力量
        temp.append(int(round((self.力智[self.等级] + self.BUFF智力) * self.BUFF智力per, 3) * 倍率)) #智力
        temp.append(int(round((self.三攻[self.等级] + self.BUFF物攻) * self.BUFF物攻per, 3) * 倍率)) #物攻
        temp.append(int(round((self.三攻[self.等级] + self.BUFF魔攻) * self.BUFF魔攻per, 3) * 倍率)) #魔攻
        temp.append(int(round((self.三攻[self.等级] + self.BUFF独立) * self.BUFF独立per, 3) * 倍率)) #独立
        return temp

    def BUFF面板(self):
        temp = []
        temp.append(self.名称)
        temp.append(int(round((self.力智[self.等级] + self.BUFF力量) * self.BUFF力量per, 0)))
        temp.append(int(round((self.力智[self.等级] + self.BUFF智力) * self.BUFF智力per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF物攻) * self.BUFF物攻per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF魔攻) * self.BUFF魔攻per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF独立) * self.BUFF独立per, 0)))
        return temp

class 真·圣骑士技能2(主动技能):
    名称 = '勇气圣歌'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 24
    增幅倍率 = 0.30
    def 结算统计(self): 
        return [0, 0, 0, 0, 0, 0, 0, 0]

class 真·圣骑士技能3(被动技能):
    名称 = '虔诚信念'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    额外力智 = 0
    力智 = [0, 14, 37, 59, 82, 104, 127, 149, 172, 194, 217, 239, 262, 284, 307, 329, 352, 374, 397, 419, 442, 464, 487, 509, 532, 554, 577, 599, 622, 644, 667, 689, 712, 734, 757, 779, 802, 824, 847, 869, 892]
    三攻 = 22
    def 力智加成(self):
        return self.力智[self.等级] + self.额外力智

    def 三攻加成(self):
        if self.等级 > 0:
            return self.三攻 + self.等级
        else:
            return 0

    def 结算统计(self): 
        return [self.力智加成(), 0, 0, self.力智加成(), self.力智加成(), self.三攻加成(), self.三攻加成(), self.三攻加成()]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class 真·圣骑士技能4(主动技能):
    名称 = '圣光天启'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    一觉力智 = 0
    一觉力智per = 0
    #28 原力智 941  测试修改为 939
    力智 = [0, 43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379, 414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 939, 993, 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668]
    def 结算统计(self):
        倍率 = self.适用数值 / 750 + 1
        x = (self.力智[self.等级] + self.一觉力智) * 倍率
        return [0, 0, 0, int(x * self.一觉力智per), int(x * self.一觉力智per), 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

    def 一觉面板(self):
        temp = []
        temp.append(self.名称)
        temp.append(int(round((self.力智[self.等级] + self.一觉力智) * self.一觉力智per, 0)))
        temp.append(int(round((self.力智[self.等级] + self.一觉力智) * self.一觉力智per, 0)))
        return temp

class 真·圣骑士技能5(被动技能):
    名称 = '大天使的庇护'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    站街生效 = 1
    智力 = [0, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540]
    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self): 
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class 真·圣骑士技能6(主动技能):
    名称 = '救赎彼岸：惩戒圣枪'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    def 结算统计(self):
        return [0, 0, 0, 0, 0, 0, 0, 0]

class 真·圣骑士技能7(被动技能):
    名称 = '三觉被动'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    站街生效 = 1
    智力 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]
    def 智力加成(self):
        return self.智力[self.等级]
    def 结算统计(self): 
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class 真·圣骑士技能8(主动技能):
    名称 = '三觉'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']
    绑定一觉力智per = 1.08
    绑定二觉力智per = 0.23

    def 结算统计(self):
        return [0, 0, 0, 0, 0, 0, 0, 0]

    def 加成倍率(self):
        if self.关联技能 == ['圣光天启']:
            return round(0.08 + self.等级 * 0.01, 2)
        else:
            return round(0.23 + self.等级 * 0.01, 2)


真·圣骑士技能列表 = []
i = 0
while i >= 0:
    try:
        exec('真·圣骑士技能列表.append(真·圣骑士技能'+str(i)+'())')
        i += 1
    except:
        i = -1

真·圣骑士技能序号 = dict()
for i in range(len(真·圣骑士技能列表)):
    真·圣骑士技能序号[真·圣骑士技能列表[i].名称] = i
    
真·圣骑士一觉序号 = 0
真·圣骑士二觉序号 = 0
真·圣骑士三觉序号 = 0
for i in 真·圣骑士技能列表:
    if i.所在等级 == 50:
        真·圣骑士一觉序号 = 真·圣骑士技能序号[i.名称]
    if i.所在等级 == 85:
        真·圣骑士二觉序号 = 真·圣骑士技能序号[i.名称]
    if i.所在等级 == 100:
        真·圣骑士三觉序号 = 真·圣骑士技能序号[i.名称]

class 真·圣骑士角色属性(角色属性):
    实际名称 = '真·圣骑士'
    角色 = '圣职者(女)'
    职业 = '圣骑士'

    系数类型选择 = ['智力']

    武器选项 = ['十字架']

    一觉序号 = 4
    三觉序号 = 8

    防具类型 = '板甲'
    防具精通属性 = ['智力']

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(真·圣骑士技能列表)
        self.技能序号 = deepcopy(真·圣骑士技能序号)

    def 专属词条计算(self):
        
        self.技能栏[self.技能序号['启示圣歌']].等级加成(self.转职被动Lv)
        self.技能栏[self.技能序号['启示圣歌']].额外智力 += self.转职被动智力
        
        # self.技能栏[self.技能序号['勇气圣歌']].增幅倍率 += self.BUFF额外增幅率

        self.技能栏[self.技能序号['勇气祝福']].等级加成(self.BUFFLv)
        self.技能栏[self.技能序号['勇气祝福']].BUFF力量per = self.BUFF力量per
        self.技能栏[self.技能序号['勇气祝福']].BUFF智力per = self.BUFF智力per
        self.技能栏[self.技能序号['勇气祝福']].BUFF物攻per = self.BUFF物攻per
        self.技能栏[self.技能序号['勇气祝福']].BUFF魔攻per = self.BUFF魔攻per
        self.技能栏[self.技能序号['勇气祝福']].BUFF独立per = self.BUFF独立per
        self.技能栏[self.技能序号['勇气祝福']].BUFF力量 = self.BUFF力量
        self.技能栏[self.技能序号['勇气祝福']].BUFF智力 = self.BUFF智力
        self.技能栏[self.技能序号['勇气祝福']].BUFF物攻 = self.BUFF物攻
        self.技能栏[self.技能序号['勇气祝福']].BUFF魔攻 = self.BUFF魔攻
        self.技能栏[self.技能序号['勇气祝福']].BUFF独立 = self.BUFF独立

        self.技能栏[self.技能序号['圣光天启']].等级加成(self.一觉Lv)
        self.技能栏[self.技能序号['圣光天启']].一觉力智 = self.一觉力智
        self.技能栏[self.技能序号['圣光天启']].一觉力智per = self.一觉力智per

        self.技能栏[self.技能序号['虔诚信念']].等级加成(self.一觉被动Lv)
        self.技能栏[self.技能序号['虔诚信念']].额外力智 = self.一觉被动力智

    def BUFF计算(self, x = 0):
        总数据 = self.数据计算()
        关联技能 = self.技能栏[self.技能序号['三觉']].关联技能

        if self.次数输入[self.技能序号['勇气圣歌']] == '1':
            for j in range(8):
                总数据[self.技能序号['勇气圣歌']][j] = int(总数据[self.技能序号['勇气祝福']][j] * self.技能栏[self.技能序号['勇气圣歌']].增幅倍率)
        for j in range(8):
            if '圣光天启' in 关联技能:
                总数据[self.技能序号['三觉']][j] = int(总数据[self.技能序号['圣光天启']][j] * (self.技能栏[self.技能序号['三觉']].绑定一觉力智per + self.技能栏[self.技能序号['三觉']].等级 * 0.01))
                总数据[self.技能序号['圣光天启']][j] = 0
            elif '救赎彼岸：惩戒圣枪' in 关联技能:
                总数据[self.技能序号['三觉']][j] = int(总数据[self.技能序号['圣光天启']][j] * (self.技能栏[self.技能序号['三觉']].绑定二觉力智per + self.技能栏[self.技能序号['三觉']].等级 * 0.01))
        
        return self.结果返回(x, 总数据)
        
    def 数据计算(self):        
        总数据 = []
        if self.双装备模式 == 1 and self.次数输入[self.一觉序号] == '1':
            #用于计算一觉
            temp = deepcopy(self)
            
            #计算现有装备BUFF
            self.装备属性计算()
            self.适用数值计算()
            for i in range(len(self.技能栏)):
                if  self.次数输入[i] == '1':
                    总数据.append(self.技能栏[i].结算统计())
                else:
                    总数据.append([0, 0, 0, 0, 0, 0, 0, 0])

            #拷贝数据，并修改装备，返回可能的组合
            数据列表 = []
            切换列表 = []
            可能组合 = self.装备替换(temp)
            for 一觉计算属性 in 可能组合:
                一觉计算属性.装备属性计算()
                一觉计算属性.适用数值计算()
                数据列表.append(一觉计算属性.技能栏[self.一觉序号].结算统计()[3] * 一觉计算属性.技能栏[self.三觉序号].加成倍率()) #3是力量属性  一觉力智都是相等的
                切换列表.append(一觉计算属性.切换详情)
            
            #取一觉最大值，并修改数据
            a = max(数据列表)
            序号 = 数据列表.index(a)
            self.切换详情 = 切换列表[序号]
            总数据[self.一觉序号] = [0, 0, 0, int(a / 可能组合[序号].技能栏[self.三觉序号].加成倍率()), int(a / 可能组合[序号].技能栏[self.三觉序号].加成倍率()), 0, 0, 0]
            self.切换详情 = 切换列表[序号]

            self.技能栏[self.一觉序号] = deepcopy(可能组合[序号].技能栏[self.一觉序号])
            self.技能栏[self.三觉序号] = deepcopy(可能组合[序号].技能栏[self.三觉序号])

        else:
            self.装备属性计算()
            self.适用数值计算()
            for i in range(len(self.技能栏)):
                if  self.次数输入[i] == '1':
                    总数据.append(self.技能栏[i].结算统计())
                else:
                    总数据.append([0, 0, 0, 0, 0, 0, 0, 0])

        return 总数据
    
class 真·圣骑士(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 真·圣骑士角色属性()
        self.角色属性A = 真·圣骑士角色属性()
        self.角色属性B = 真·圣骑士角色属性()
        self.一觉序号 = 真·圣骑士一觉序号
        self.二觉序号 = 真·圣骑士二觉序号
        self.三觉序号 = 真·圣骑士三觉序号

    def 强化觉醒选择(self, index):
        self.觉醒选择状态 = index
        if index == 1:
            self.一觉遮罩透明度.setOpacity(0.0)
            self.二觉遮罩透明度.setOpacity(0.5)
        if index == 2:
            self.一觉遮罩透明度.setOpacity(0.5)
            self.二觉遮罩透明度.setOpacity(0.0)

        self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
        self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)



    def 界面(self):
        super().界面()
        
        #三觉强化选择
        self.觉醒选择状态 = 2
        self.一觉遮罩透明度 = QGraphicsOpacityEffect()
        self.一觉遮罩透明度.setOpacity(0.5)
        self.二觉遮罩透明度 = QGraphicsOpacityEffect()
        self.二觉遮罩透明度.setOpacity(0.0)
        横坐标 = 250
        纵坐标 = 230
        x = 横坐标;
        y = 纵坐标
        self.觉醒选择 = QLabel(self.main_frame2)
        self.觉醒选择.setPixmap(QPixmap('./ResourceFiles/img/觉醒选择.png'))
        self.觉醒选择.resize(120, 100)
        self.觉醒选择.move(x, y - 20)

        x = 横坐标;
        y = 纵坐标
        self.一觉图片 = QLabel(self.main_frame2)
        self.一觉图片.setPixmap(self.技能图片[self.一觉序号])
        self.一觉图片.resize(28, 28)
        self.一觉图片.move(x + 7, y + 8)
        self.二觉图片 = QLabel(self.main_frame2)
        self.二觉图片.setPixmap(self.技能图片[self.二觉序号])
        self.二觉图片.resize(28, 28)
        self.二觉图片.move(x + 52, y + 8)
        self.一觉遮罩 = QPushButton(self.main_frame2)
        self.一觉遮罩.resize(38, 50)
        self.一觉遮罩.move(x + 2, y + 5)
        self.一觉遮罩.setStyleSheet("QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}")
        self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
        self.一觉遮罩.clicked.connect(lambda state, index=1: self.强化觉醒选择(index))
        self.二觉遮罩 = QPushButton(self.main_frame2)
        self.二觉遮罩.resize(38, 50)
        self.二觉遮罩.move(x + 47, y + 5)
        self.二觉遮罩.setStyleSheet("QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}")
        self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)
        self.二觉遮罩.clicked.connect(lambda state, index=2: self.强化觉醒选择(index))
    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        if self.觉醒选择状态 == 1:
            属性.技能栏[self.三觉序号].关联技能 = [属性.技能栏[self.一觉序号].名称]
        if self.觉醒选择状态 == 2:
            属性.技能栏[self.三觉序号].关联技能 = [属性.技能栏[self.二觉序号].名称]
