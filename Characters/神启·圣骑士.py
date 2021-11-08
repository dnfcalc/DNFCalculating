from PublicReference.buffer.base import *


class 神启·圣骑士技能0(被动技能):
    名称 = '启示圣歌'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 31
    额外智力 = 0
    站街生效 = 1
    智力 = [0, 86, 90, 94, 98, 102, 107, 112, 117, 123, 129, 135, 141, 147, 154, 161, 169, 177, 185, 193, 201, 210, 219, 229, 238, 248, 258, 269, 279, 290, 301,
          313, 325, 337, 349, 361, 375, 388, 401, 415, 429, 443, 457, 473, 487, 503, 519, 535, 551, 567, 584, 598, 614, 630, 646, 662, 677, 693, 709, 725, 741]

    def 智力加成(self):
        return self.智力[self.等级] + self.额外智力 + self.进图加成

    def 结算统计(self,context):
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 神启·圣骑士技能1(主动技能):
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
    三攻 = [0, 38, 40, 42, 43, 44, 46, 48, 49, 51, 52, 53, 55, 57, 58, 60, 61, 62, 64, 66, 68, 69, 70, 72, 74, 75, 77, 78, 79, 81, 83, 84, 86, 87, 88, 90, 92, 93, 95,
          96, 98, 100, 101, 103, 104, 105, 107, 109, 110, 112, 113, 114, 116, 118, 119, 121, 122, 123, 126, 127, 129, 130, 131, 133, 135, 136, 138, 139, 140, 143, 144]
    力智 = [0, 148, 158, 169, 179, 189, 198, 208, 218, 228, 239, 249, 259, 269, 279, 290, 299, 309, 319, 329, 339, 349, 360, 370, 380, 390, 399, 409, 420, 430, 440, 450, 460, 470, 481,
          491, 500, 510, 520, 530, 541, 551, 561, 571, 581, 592, 601, 611, 621, 631, 641, 651, 662, 672, 682, 692, 701, 711, 722, 732, 742, 752, 762, 772, 783, 793, 802, 812, 822, 832, 843]

    def 结算统计(self,context):
        倍率 = self.适用数值 / 665 + 1
        temp = [0, 0, 0]  # 智力,体力,精神
        temp.append(int(round(
            (self.力智[self.等级] + self.BUFF力量) * self.BUFF力量per * 倍率, 3)))  # 力量
        temp.append(int(round(
            (self.力智[self.等级] + self.BUFF智力) * self.BUFF智力per * 倍率, 3)))  # 智力
        temp.append(int(round(
            (self.三攻[self.等级] + self.BUFF物攻) * self.BUFF物攻per * 倍率, 3)))  # 物攻
        temp.append(int(round(
            (self.三攻[self.等级] + self.BUFF魔攻) * self.BUFF魔攻per * 倍率, 3)))  # 魔攻
        temp.append(int(round(
            (self.三攻[self.等级] + self.BUFF独立) * self.BUFF独立per * 倍率, 3)))  # 独立
        return temp

    def 技能面板(self):
        temp = []
        temp.append(self.名称)
        temp.append(
            int(round((self.力智[self.等级] + self.BUFF力量) * self.BUFF力量per)))
        temp.append(
            int(round((self.力智[self.等级] + self.BUFF智力) * self.BUFF智力per)))
        temp.append(
            int(round((self.三攻[self.等级] + self.BUFF物攻) * self.BUFF物攻per)))
        temp.append(
            int(round((self.三攻[self.等级] + self.BUFF魔攻) * self.BUFF魔攻per)))
        temp.append(
            int(round((self.三攻[self.等级] + self.BUFF独立) * self.BUFF独立per)))
        return temp


class 神启·圣骑士技能2(主动技能):
    名称 = '勇气圣歌'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 24
    增幅倍率 = 0.15

    def 结算统计(self,context):
        buff = context.技能表['BUFF']
        if buff.是否启用:
            values = buff.结算统计(context)
            return [int(round(i * self.增幅倍率)) for i in values]
        return [0]*8


class 神启·圣骑士技能3(主动技能):
    名称 = '神光十字'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    力智 = 72

    def 力智加成(self):
        return self.力智 + self.等级 * 6

    def 结算统计(self,context):
        return [0, 0, 0, self.力智加成(), self.力智加成(), 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 神启·圣骑士技能4(被动技能):
    名称 = '虔诚信念'
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

    def 结算统计(self,context):
        return [self.力智加成(), 0, 0, self.力智加成(), self.力智加成(), 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 神启·圣骑士技能5(觉醒技能):
    名称 = '圣光天启'
    pass


class 神启·圣骑士技能6(被动技能):
    名称 = '大天使的庇护'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    站街生效 = 1
    智力 = [0, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330,
          340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540]

    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self,context):
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 神启·圣骑士技能7(主动技能):
    名称 = '救赎彼岸：惩戒圣枪'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5

    def 结算统计(self,context):
        return [0, 0, 0, 0, 0, 0, 0, 0]


class 神启·圣骑士技能8(被动技能):
    名称 = '圣天使之光'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    站街生效 = 1
    智力 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340,
          350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]

    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self,context):
        return [self.智力加成(), 0, 0, 0, 0, 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 神启·圣骑士技能9(三觉技能):
    名称 = '祈愿·天使赞歌'
    关联技能 = ['救赎彼岸：惩戒圣枪']
    pass




技能表 = {}
技能栏 = []
i = 0
while i >= 0:
    try:
        skill: 技能 = eval("神启·圣骑士技能"+str(i)+"()")
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


class 神启·圣骑士角色属性(辅助角色属性):
    实际名称 = '神启·圣骑士'
    角色 = '圣职者(女)'
    职业 = '圣骑士'

    武器选项 = ['十字架']

    防具类型 = '板甲'
    防具精通属性 = ['智力']

    def __init__(self):
        super().__init__()
        self.武器选项 = ['十字架']
        self.防具精通属性 = ['智力']
        self.类型选择 = ['智力']
        self.类型 = '智力'
        self.技能表 = deepcopy(技能表)
        self.技能栏 = list(self.技能表.values())
        self.一觉序号 = self.技能表['一次觉醒'].技能序号
        self.二觉序号 = self.技能表['二次觉醒'].技能序号
        self.三觉序号 = self.技能表['三次觉醒'].技能序号
        基础属性输入(self)

    def 专属词条计算(self):

        self.技能表['启示圣歌'].等级加成(self.转职被动Lv)
        self.技能表['启示圣歌'].额外智力 += self.转职被动智力
        self.技能表['启示圣歌'].进图加成 += self.被动进图加成

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

        self.技能表['虔诚信念'].等级加成(self.一觉被动Lv)
        self.技能表['虔诚信念'].额外力智 = self.一觉被动力智

    def 系数数值站街(self):
        return self.智力

    def 系数数值进图(self):
        return self.进图智力

    def get_data(self):
        self.buff_rate = 1.15 if self.技能表['勇气圣歌'].是否启用 else 1
        return super().get_data()


class 神启·圣骑士(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 神启·圣骑士角色属性()
        self.角色属性A = deepcopy(self.初始属性)
        self.角色属性B = deepcopy(self.初始属性)
