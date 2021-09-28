from PublicReference.base_buff import *


class 知源·小魔女技能0(被动技能):
    名称 = '人偶操纵者'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 31
    额外智力 = 0
    站街生效 = 1
    智力 = [0, 69, 73, 77, 81, 85, 90, 95, 100, 106, 112, 118, 124, 130, 137, 144, 152, 160, 168, 176, 184, 193, 202, 212, 221, 231, 241, 252, 262, 273, 284,
          296, 308, 320, 332, 344, 358, 371, 384, 398, 412, 426, 440, 456, 470, 486, 502, 518, 534, 550, 567, 581, 597, 613, 629, 645, 660, 676, 692, 708, 724]

    def 智力加成(self):
        return self.智力[self.等级] + self.额外智力 + self.进图加成

    def 结算统计(self):
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 知源·小魔女技能1(主动技能):
    名称 = '小魔女的偏爱'
    所在等级 = 20
    等级上限 = 40
    基础等级 = 10
    增幅倍率 = 0.15

    def 结算统计(self):
        return [0, 0, 0, 0, 0, 0, 0, 0]


class 知源·小魔女技能2(主动技能):
    名称 = '禁忌诅咒'
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
    三攻 = [0, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54, 55, 57, 58,
          60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 87]
    力智 = [0, 131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247, 256, 264, 273, 282, 291,
          300, 309, 318, 327, 336, 345, 353, 362, 371, 380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478]

    def 结算统计(self):
        倍率 = self.适用数值 / 665 + 1

        偏爱 = self.技能表['小魔女的偏爱']
        if 偏爱.是否启用:
            倍率 *= 1 + 偏爱.增幅倍率

        temp = [0, 0, 0]  # 智力,体力,精神
        temp.append(int(round((self.力智[self.等级] + self.BUFF力量) * self.BUFF力量per * 倍率,3)))  # 力量
        temp.append(int(round((self.力智[self.等级] + self.BUFF智力) * self.BUFF智力per * 倍率,3)))  # 智力
        temp.append(int(round((self.三攻[self.等级] + self.BUFF物攻) * self.BUFF物攻per * 倍率,3)))  # 物攻
        temp.append(int(round((self.三攻[self.等级] + self.BUFF魔攻) * self.BUFF魔攻per * 倍率,3)))  # 魔攻
        temp.append(int(round((self.三攻[self.等级] + self.BUFF独立) * self.BUFF独立per * 倍率,3)))  # 独立

        return temp

    def 技能面板(self):
        temp = []
        temp.append(self.名称)
        temp.append(int(round((self.力智[self.等级] + self.BUFF力量) * self.BUFF力量per, 0)))
        temp.append(int(round((self.力智[self.等级] + self.BUFF智力) * self.BUFF智力per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF物攻) * self.BUFF物攻per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF魔攻) * self.BUFF魔攻per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF独立) * self.BUFF独立per, 0)))
        return temp


class 知源·小魔女技能3(主动技能):
    名称 = '死命召唤'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 24
    增幅倍率 = 0.25

    def 结算统计(self):
        if(self.技能表['BUFF'].是否启用 == 1):
            values = self.技能表['BUFF'].结算统计()
            return [int(round(i * self.增幅倍率)) for i in values]
        return [0]*8


class 知源·小魔女技能4(被动技能):
    名称 = '少女的爱'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    额外力智 = 0
    力智 = [0, 14, 37, 59, 82, 104, 127, 149, 172, 194, 217, 239, 262, 284, 307, 329, 352, 374, 397, 419, 442,
          464, 487, 509, 532, 554, 577, 599, 622, 644, 667, 689, 712, 734, 757, 779, 802, 824, 847, 869, 892]
    三攻 = 22

    def 力智加成(self):
        return self.力智[self.等级] + self.额外力智

    def 三攻加成(self):
        if self.等级 > 0:
            return self.三攻 + self.等级
        else:
            return 0

    def 结算统计(self):
        return [self.力智加成(), 0, 0, self.力智加成(), self.力智加成(), 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 知源·小魔女技能5(主动技能):
    名称 = '开幕！人偶剧场'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    一觉力智 = 0
    一觉力智per = 0
    # 28 原力智 941  测试修改为 939
    力智 = [0, 43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379, 414, 449, 487, 526, 567, 608,
          651, 696, 741, 789, 838, 888, 939, 993, 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668]

    def 结算统计(self, 计算三觉=False):
        if 计算三觉 is False and self.名称 in self.技能表['三次觉醒'].关联技能:
            return [0]*8
        倍率 = self.适用数值 / 750 + 1
        x = (self.力智[self.等级] + self.一觉力智) * 倍率
        return [0, 0, 0, int(round(x * self.一觉力智per)), int(round(x * self.一觉力智per)), 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立

    def 技能面板(self):
        temp = []
        temp.append(self.名称)
        temp.append(int(round((self.力智[self.等级] + self.一觉力智) * self.一觉力智per, 0)))
        temp.append(int(round((self.力智[self.等级] + self.一觉力智) * self.一觉力智per, 0)))
        return temp


class 知源·小魔女技能6(被动技能):
    名称 = '冥月绽放'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    站街生效 = 1
    智力 = [0, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330,
          340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540]

    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self):
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 知源·小魔女技能7(主动技能):
    名称 = '人偶之森'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5

    def 结算统计(self):
        return [0, 0, 0, 0, 0, 0, 0, 0]


class 知源·小魔女技能8(被动技能):
    名称 = '不祥的微笑'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    站街生效 = 1
    智力 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340,
          350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]

    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self):
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 知源·小魔女技能9(主动技能):
    名称 = '终幕！人偶剧场'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['人偶之森']
    绑定一觉力智per = 1.08
    绑定二觉力智per = 0.23

    def 结算统计(self):
        if(self.技能表['一次觉醒'].是否启用 == 1):
            values = self.技能表['一次觉醒'].结算统计(True)
            倍率 = self.加成倍率()
            return [int(round(i * 倍率)) for i in values]
        return [0]*8

    def 加成倍率(self):
        if '开幕！人偶剧场' in self.关联技能:
            return round(1.08 + self.等级 * 0.01, 2)
        else:
            return round(0.23 + self.等级 * 0.01, 2)


技能表 = {}
技能栏 = []
i = 0
while i >= 0:
    try:            
        skill: 技能 = eval("知源·小魔女技能"+str(i)+"()")
        skill.技能序号 = i
        skill.技能表 = 技能表
        名称 = skill.名称
        if skill.所在等级 == 30:
            名称 = 'BUFF'
        elif skill.所在等级 == 50:
            名称 = '一次觉醒'
        elif skill.所在等级 == 85:
            名称 = '二次觉醒'
        elif skill.所在等级 == 100:
            名称 = '三次觉醒'
        技能表[名称] = skill
        技能栏.append(skill)
        i += 1
    except:
        i = -1


class 知源·小魔女角色属性(辅助角色属性):
    实际名称 = '知源·小魔女'
    角色 = '魔法师(女)'
    职业 = '小魔女'

    武器选项 = ['扫把']

    防具类型 = '板甲'
    防具精通属性 = ['智力']

    def __init__(self):
        super().__init__()
        self.武器选项 = ['扫把']
        self.防具精通属性 = ['智力']
        self.类型选择 = ['智力']
        self.类型 = '智力'
        self.技能表 = deepcopy(技能表)
        self.技能栏 = list(self.技能表.values())
        self.buff_type = 1
        self.一觉序号 = self.技能表['一次觉醒'].技能序号
        self.二觉序号 = self.技能表['二次觉醒'].技能序号
        self.三觉序号 = self.技能表['三次觉醒'].技能序号
        基础属性输入(self)

    def 系数数值站街(self):
        return self.智力

    def 系数数值进图(self):
        return self.进图智力

    def 专属词条计算(self):

        self.技能表['人偶操纵者'].等级加成(self.转职被动Lv)
        self.技能表['人偶操纵者'].额外智力 += self.转职被动智力
        self.技能表['人偶操纵者'].进图加成 += self.被动进图加成

        self.技能表['BUFF'].等级加成(self.BUFFLv)
        self.技能表['BUFF'].BUFF力量per = self.BUFF力量per
        self.技能表['BUFF'].BUFF智力per = self.BUFF智力per
        self.技能表['BUFF'].BUFF物攻per = self.BUFF物攻per
        self.技能表['BUFF'].BUFF魔攻per = self.BUFF魔攻per
        self.技能表['BUFF'].BUFF独立per = self.BUFF独立per
        self.技能表['BUFF'].BUFF力量 = self.BUFF力量
        self.技能表['BUFF'].BUFF智力 = self.BUFF智力
        self.技能表['BUFF'].BUFF物攻 = self.BUFF物攻
        self.技能表['BUFF'].BUFF魔攻 = self.BUFF魔攻
        self.技能表['BUFF'].BUFF独立 = self.BUFF独立

        self.技能表['一次觉醒'].等级加成(self.一觉Lv)
        self.技能表['一次觉醒'].一觉力智 = self.一觉力智
        self.技能表['一次觉醒'].一觉力智per = self.一觉力智per

        self.技能表['少女的爱'].等级加成(self.一觉被动Lv)
        self.技能表['少女的爱'].额外力智 = self.一觉被动力智

    def get_data(self):
        buff_rate = 1.25 if self.技能表['死命召唤'].是否启用 else 1
        buff_rate *= 1.15 if self.技能表['小魔女的偏爱'].是否启用 else 1
        self.buff_rate = buff_rate
        return super().get_data()

class 知源·小魔女(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 知源·小魔女角色属性()
        self.登记属性 = deepcopy(self.初始属性)

        self.角色属性A = deepcopy(self.初始属性)
        self.角色属性B = deepcopy(self.初始属性)
