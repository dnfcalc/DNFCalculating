from ctypes import *

from PublicReference.common import *
from PublicReference.equipment.buff.宠物_buff import *
from PublicReference.equipment.buff.武器融合_buff import *
from PublicReference.equipment.buff.称号_buff import *
from PublicReference.equipment.buff.融合_奥兹玛_buff import OzmaList
from PublicReference.equipment.buff.融合_希洛克_buff import SirocoList
from PublicReference.equipment.buff.辟邪玉_buff import *
from PublicReference.equipment.buff.黑鸦_buff import *
from PublicReference.equipment.buff.护石_buff import *
from PublicReference.equipment.buff.描述_buff import *
from PublicReference.utils.common import to_int


class 技能:
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    等级 = 0
    基础等级 = 0
    是否主动 = 0
    站街生效 = 0
    等级溢出 = 0

    是否启用 = 1
    技能序号 = 0
    技能表 = {}

    def 等级加成(self, x):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                if self.基础等级 != self.等级上限:
                    self.等级溢出 = 1
            else:
                self.等级 += x

    def 结算统计(self, context=None):
        return [0, 0, 0, 0, 0, 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 被动技能(技能):
    是否主动 = 0
    进图加成 = 0


class 主动技能(技能):
    是否主动 = 1
    适用数值 = 0


class 觉醒技能(主动技能):
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    一觉力智 = 0
    一觉力智per = 0
    # 28 原力智 941  测试修改为 939
    力智 = [
        0, 43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346,
        379, 414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 939,
        993, 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668
    ]

    def 结算统计(self, context, compute_3rd_awake=False):
        if not compute_3rd_awake and self.名称 in context.技能表['三次觉醒'].关联技能:
            return [0] * 8
        倍率 = self.适用数值 / 750 + 1
        x = (self.力智[self.等级] + self.一觉力智) * 倍率
        values = [
            0, 0, 0,
            int(round(x * self.一觉力智per)),
            int(round(x * self.一觉力智per)), 0, 0, 0
        ]
        return values
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立

    def 技能面板(self):
        temp = []
        temp.append(self.名称)
        temp.append(
            int(round((self.力智[self.等级] + self.一觉力智) * self.一觉力智per, 0)))
        temp.append(
            int(round((self.力智[self.等级] + self.一觉力智) * self.一觉力智per, 0)))
        return temp


class 三觉技能(主动技能):
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    绑定一觉力智per = 1.08
    绑定二觉力智per = 0.23
    关联技能 = []

    def 结算统计(self, context):
        技能表 = context.技能表
        awake = 技能表['一次觉醒']
        if awake.是否启用:
            values = awake.结算统计(context, True)
            倍率 = self.加成倍率(awake.名称 in self.关联技能)
            return [int(round(i * 倍率)) for i in values]
        return [0] * 8

    def 加成倍率(self, bind_awake):
        if bind_awake:
            return round(1.08 + self.等级 * 0.01, 2)
        else:
            return round(0.23 + self.等级 * 0.01, 2)


BUFF影响技能 = ['勇气祝福', '勇气圣歌', '荣誉祝福', '禁忌诅咒', '死命召唤']


class 辅助角色属性(属性):
    职业分类 = 'BUFF'
    C力智 = 5000
    C三攻 = 3000
    系统奶系数 = 0
    系统奶基数 = 0
    排行类型 = '物理百分比'

    类型 = '固伤'

    称号触发 = False

    排行系数 = 0
    站街系数 = 0

    百分比体精 = 0.0

    被动进图加成 = 0
    守护恩赐体精 = 0
    转职被动智力 = 0

    转职被动Lv = 0
    一觉被动Lv = 0

    BUFFLv = 0
    BUFF力量per = 1
    BUFF智力per = 1
    BUFF物攻per = 1
    BUFF魔攻per = 1
    BUFF独立per = 1
    一觉Lv = 0
    一觉力智 = 0
    一觉力智per = 1

    BUFF力量 = 0
    BUFF智力 = 0
    BUFF物攻 = 0
    BUFF魔攻 = 0
    BUFF独立 = 0

    一觉被动力智 = 0
    信念光环体精 = 0

    BUFF适用面板 = 0
    BUFF补正力智 = 0
    BUFF补正体力 = 0
    BUFF补正精神 = 0

    一觉序号 = 0
    二觉序号 = 0
    三觉序号 = 0
    双装备模式 = 0
    切换详情 = '无'

    次数输入 = []
    # 是否为输出装备描述
    装备描述 = 0

    希洛克武器词条 = 0
    自适应最高值 = []
    武器词条触发 = 0
    产物升级 = 0

    def __init__(self):
        super().__init__()
        self.次数输入 = []
        self.残香词条 = [0] * 4
        self.黑鸦词条 = [[0] * 4] * 4
        self.希洛克选择状态 = [0] * 15
        self.奥兹玛选择状态 = [0] * 25
        self.自适应最高值 = []
        self.技能表 = {}
        self.觉醒择优系数 = 1.0
        self.武器词条触发 = 0
        self.buff_type = 0
        self.buff_rate = 1
        self.护石栏 = [0] * 3

    def get_data(self):
        buff = self.技能表['BUFF']
        awake = self.技能表['一次觉醒']

        other_power = 0
        other_attack = 0

        ignores = ['BUFF', '一次觉醒', '三次觉醒', '死命召唤', '勇气圣歌']

        for i in self.技能表.keys():
            if i not in ignores:
                skill = self.技能表[i]
                data = skill.结算统计(self)
                other_power += data[3]
                other_attack += data[5]

        in_int_data = (ctypes.c_int * 12)()
        in_int_data[0] = self.buff_type
        in_int_data[1] = int(buff.适用数值)
        in_int_data[2] = buff.等级
        in_int_data[3] = int(buff.BUFF力量)
        in_int_data[4] = int(buff.BUFF物攻)
        in_int_data[5] = int(awake.适用数值)
        in_int_data[6] = awake.等级
        in_int_data[7] = int(awake.一觉力智)
        in_int_data[8] = int(other_power)
        in_int_data[9] = int(other_attack)
        in_int_data[10] = int(self.C力智)
        in_int_data[11] = int(self.C三攻)

        third_awake = self.技能表['三次觉醒']

        awake_rate = 1
        if third_awake.是否启用:
            awake_rate = third_awake.加成倍率(awake.名称 in third_awake.关联技能)
            awake_rate = awake_rate + 1 if awake_rate < 1 else awake_rate

        awake_rate = awake_rate if awake.是否启用 else 0

        buff_rate = self.buff_rate if buff.是否启用 else 0

        in_double_data = (ctypes.c_double * 8)()
        in_double_data[0] = self.觉醒择优系数
        in_double_data[1] = buff_rate
        in_double_data[2] = buff.BUFF力量per
        in_double_data[3] = buff.BUFF物攻per
        in_double_data[4] = awake_rate
        in_double_data[5] = awake.一觉力智per
        in_double_data[6] = self.系统奶系数
        in_double_data[7] = self.系统奶基数
        return in_int_data, in_double_data

    def 穿戴装备(self, 装备, 套装=None):
        self.装备栏 = 装备
        self.套装栏 = 套装
        if 套装 is None or len(套装) == 0:
            self.套装栏 = equ.get_suits_by_equips(装备)
        self.武器类型 = equ.get_equ_by_name(self.装备栏[11]).类型

    def 力智固定加成(self, x=0):
        return 力智固定加成(self, x)

    def 体精固定加成(self, x=0):
        return 体精固定加成(self, x)

    def BUFF增加(self,
               BUFFLv=0,
               BUFF力量=0,
               BUFF智力=0,
               BUFF力量per=1,
               BUFF智力per=1,
               BUFF物攻=0,
               BUFF魔攻=0,
               BUFF独立=0,
               BUFF物攻per=1,
               BUFF魔攻per=1,
               BUFF独立per=1):
        return BUFF增加(self, BUFFLv, BUFF力量, BUFF智力, BUFF力量per, BUFF智力per,
                      BUFF物攻, BUFF魔攻, BUFF独立, BUFF物攻per, BUFF魔攻per, BUFF独立per)

    def 被动增加(self,
             守护恩赐体精=0,
             转职被动Lv=0,
             转职被动智力=0,
             信念光环Lv=0,
             信念光环体精=0,
             一觉被动Lv=0,
             一觉被动力智=0):
        if 信念光环Lv > 0 and 一觉被动Lv == 0:
            一觉被动Lv = 信念光环Lv
        return 被动增加(self, 转职被动Lv, 转职被动智力, 守护恩赐体精, 信念光环体精, 一觉被动Lv, 一觉被动力智)

    def 觉醒增加(self, 一觉Lv=0, 一觉力智=0, 一觉力智per=1):
        return 觉醒增加(self, 一觉Lv, 一觉力智, 一觉力智per)

    def 系数数值站街(self):
        pass

    def 系数数值进图(self):
        pass

    def 防具精通计算(self, i):
        temp = equ.get_equ_by_name(self.装备栏[i])
        if temp.所属套装 != '智慧产物':
            return 精通体力(temp.等级, temp.品质, self.强化等级[i], 部位列表[i])
        else:
            return 精通体力(temp.等级, temp.品质, self.改造等级[i], 部位列表[i])

    def 装备基础(self):
        for i in range(5):
            # 精通
            temp = equ.get_equ_by_name(self.装备栏[i])
            x = self.防具精通计算(i)
            if '智力' in self.防具精通属性:
                self.智力 += x * 2
            if '体力' in self.防具精通属性:
                self.体力 += x
            if '精神' in self.防具精通属性:
                self.精神 += x * 2
            # 装备属性
            self.智力 += temp.智力['板甲']
            self.体力 += temp.体力['板甲']
            self.精神 += temp.精神['板甲']

        for i in [9, 10]:
            temp = equ.get_equ_by_name(self.装备栏[i])
            if temp.所属套装 != '智慧产物':
                x = 左右计算(temp.等级, temp.品质, self.强化等级[i])
                self.智力 += x
                self.体力 += x
                self.精神 += x
        for i in range(12):
            temp = equ.get_equ_by_name(self.装备栏[i])
            if self.是否增幅[i] and temp.所属套装 != '智慧产物':
                x = 增幅计算(temp.等级, temp.品质, self.强化等级[i], self.增幅版本)
                if '智力' in self.类型:
                    self.智力 += x
                if '体力' in self.类型:
                    self.体力 += x
                if '精神' in self.类型:
                    self.精神 += x
        for i in [5, 6, 7, 8, 9, 10]:
            temp = equ.get_equ_by_name(self.装备栏[i])
            self.智力 += temp.智力
            self.体力 += temp.体力
            self.精神 += temp.精神

        temp = equ.get_equ_by_name(self.装备栏[11])
        if temp.所属套装 != '智慧产物':
            四维 = 锻造四维(temp.等级, temp.品质, self.武器锻造等级)
            self.智力 += temp.智力 + 四维
            self.体力 += temp.体力 + 四维
            self.精神 += temp.精神 + 四维

    def 单技能等级加成(self, 名称, lv):
        if self.装备描述 == 1:
            return "{} Lv +{}<br>".format(名称, lv)
        else:
            for i in self.技能表.keys():
                if i == 名称:
                    self.技能表[i].等级加成(lv)
        return ''

    def 等级溢出判断(self, 装备, 套装):
        self.穿戴装备(装备, 套装)
        self.装备属性计算()
        temp = []
        for skill in self.技能表.values():
            if skill.等级溢出 == 1:
                temp.append(skill.名称)
        return temp

    def 技能等级加成(self, 加成类型, min, max, lv, 可变=0):
        lv = int(lv)
        if self.装备描述 == 1:
            if 加成类型 == "所有":
                if min == max:
                    return "Lv{} 技能等级+{}<br>".format(min, lv)
                else:
                    return "Lv{}-{} 技能等级+{}<br>".format(min, max, lv)
            else:
                if min == max:
                    return "Lv{} 主动技能等级+{}<br>".format(min, lv)
                else:
                    return "Lv{}-{} 主动技能等级+{}<br>".format(min, max, lv)
        else:
            for skill in self.技能表.values():
                if skill.所在等级 >= min and skill.所在等级 <= max:
                    if 加成类型 == '所有':
                        skill.等级加成(lv)
                    else:
                        if skill.是否主动 == 1:
                            skill.等级加成(lv)
            # if 可变 > 0:
            #     self.变换词条[可变-1] = [6,2,14 + (2 if 可变 > 1 else 4), 14 + (9 if 可变 > 1 else 17)]

        return ''

    def 提升率计算(self, 总数据, x=0):

        力量合计 = 0
        智力合计 = 0
        物攻合计 = 0
        魔攻合计 = 0
        独立合计 = 0

        for i in 总数据:
            力量合计 += i[3]
            智力合计 += i[4]
            物攻合计 += i[5]
            魔攻合计 += i[6]
            独立合计 += i[7]

        x1 = (
            (self.C力智 +
             (self.C力智 - 950) * self.系统奶系数 + self.系统奶基数) / 250 + 1) * self.C三攻

        if self.排行类型 == '物理百分比':
            a = 力量合计
            b = 物攻合计
        elif self.排行类型 == '魔法百分比':
            a = 智力合计
            b = 魔攻合计
        elif self.排行类型 == '物理固伤':
            a = 力量合计
            b = 独立合计
        elif self.排行类型 == '魔法固伤':
            a = 智力合计
            b = 独立合计

        x2 = ((self.C力智 +
               (self.C力智 - 950) * self.系统奶系数 + self.系统奶基数 + a) / 250 +
              1) * (self.C三攻 + b)
        return [x2 / x1 * 100, int(self.站街系数), a, b][x]

    def 适用数值计算(self):
        self.专属词条计算()
        for skill in self.技能表.values():
            if skill.是否启用:
                结算 = skill.结算统计(self)
                self.智力 += 结算[0]
                self.体力 += 结算[1]
                self.精神 += 结算[2]

        self.进图智力 += self.智力
        self.进图体力 += self.体力
        self.进图精神 += self.精神

        self.进图体力 *= 1 + self.百分比体精
        self.进图精神 *= 1 + self.百分比体精

        进图 = 0
        BUFF补正 = 0
        if self.类型 == '智力':
            进图 = self.进图智力
            BUFF补正 = self.BUFF补正力智
        elif self.类型 == '体力':
            进图 = self.进图体力
            BUFF补正 = self.BUFF补正体力
        elif self.类型 == '精神':
            进图 = self.进图精神
            BUFF补正 = self.BUFF补正精神
        self.技能表['一次觉醒'].适用数值 = 进图
        self.技能表['BUFF'].适用数值 = 进图 + BUFF补正
        return 进图

    # 返回可能的组合列表
    def 装备替换(self, 属性: 属性) -> 属性:
        套装栏 = []
        for i in 属性.套装栏:
            套装栏.append(i.split('[')[0])
        if len(套装栏) < 7 or self.排行系数 == 1:
            return [deepcopy(属性)]

        匹配1 = [防具套装, 上链左套装, 上链左套装, 镯下右套装, 镯下右套装, 环鞋指套装, 环鞋指套装]
        匹配0 = [防具套装, 上链左套装, 防具套装, 镯下右套装, 防具套装, 环鞋指套装, 防具套装]
        匹配 = [防具套装, 防具套装, 防具套装, 首饰套装, 首饰套装, 特殊套装, 特殊套装]

        count = []
        count2 = 0

        for i in range(7):
            # 3332散搭
            if 套装栏[i] in 匹配1[i]:
                count.append(1)
            elif 套装栏[i] in 匹配0[i]:
                count.append(0)
            else:
                count.append(-9)
            # 3233双防具
            if 套装栏[i] in 匹配[i]:
                count2 += 1

        sumcount = sum(count)

        if sumcount == 7:
            x1 = deepcopy(属性)
            x2 = deepcopy(属性)
            x3 = deepcopy(属性)
            x4 = deepcopy(属性)
            num = 0
            index = [6, 5, 7]
            for i in [x2, x3, x4]:
                i.装备栏[num * 2] = equ.get_equ_by_index(
                    equ.get_equ_by_name(i.装备栏[1]).所属套装, '史诗',
                    equ.get_equ_by_name(i.装备栏[num * 2]).部位).名称
                i.套装栏[2 * num + 2] = i.套装栏[2 * num + 2].replace(
                    equ.get_equ_by_name(i.装备栏[index[num]]).所属套装,
                    equ.get_equ_by_name(i.装备栏[1]).所属套装)
                i.切换详情 = trans(equ.get_equ_by_name(
                    i.装备栏[num * 2]).部位) + ':' + trans(
                        x1.装备栏[num * 2]) + ' → ' + trans(i.装备栏[num * 2])
                num += 1
            return [x1, x2, x3, x4]
        elif sumcount == 6:
            index = count.index(0)
            部位 = {2: 6, 4: 5, 6: 7}
            x1 = deepcopy(属性)
            x2 = deepcopy(属性)
            x2.装备栏[index - 2] = equ.get_equ_by_index(
                equ.get_equ_by_name(x2.装备栏[部位[index]]).所属套装, '史诗',
                equ.get_equ_by_name(x2.装备栏[index - 2]).部位).名称
            x2.套装栏[index] = x2.套装栏[index].replace(
                equ.get_equ_by_name(x2.装备栏[1]).所属套装,
                equ.get_equ_by_name(x2.装备栏[部位[index]]).所属套装)
            x2.切换详情 = trans(equ.get_equ_by_name(
                x2.装备栏[index - 2]).部位) + ':' + trans(
                    x1.装备栏[index - 2]) + ' → ' + trans(x2.装备栏[index - 2])
            return [x1, x2]
        elif count2 == 7 and 套装栏[1] != 套装栏[2]:
            x1 = deepcopy(属性)
            x2 = deepcopy(属性)
            x3 = deepcopy(属性)
            x4 = deepcopy(属性)
            x5 = deepcopy(属性)
            两件套名称 = 属性.套装栏[2].split('[')[0]
            三件套名称 = 属性.套装栏[1].split('[')[0]
            x2.套装栏[1] = x2.套装栏[1].replace(三件套名称, 两件套名称)
            x3.套装栏[1] = x3.套装栏[1].replace(三件套名称, 两件套名称)
            x4.套装栏[1] = x4.套装栏[1].replace(三件套名称, 两件套名称)
            x5.套装栏[2] = x5.套装栏[2].replace(两件套名称 + '[2]', 三件套名称 + '[5]')
            可更换部位 = []
            不可更换部位 = []
            for i in range(5):
                if equ.get_equ_by_name(属性.装备栏[i]).所属套装 == 三件套名称:
                    可更换部位.append(i)
                else:
                    不可更换部位.append(i)
            x2.装备栏[可更换部位[0]] = equ.get_equ_by_index(两件套名称, '史诗',
                                                    部位列表[可更换部位[0]]).名称
            x3.装备栏[可更换部位[1]] = equ.get_equ_by_index(两件套名称, '史诗',
                                                    部位列表[可更换部位[1]]).名称
            x4.装备栏[可更换部位[2]] = equ.get_equ_by_index(两件套名称, '史诗',
                                                    部位列表[可更换部位[2]]).名称
            x5.装备栏[不可更换部位[0]] = equ.get_equ_by_index(三件套名称, '史诗',
                                                     部位列表[不可更换部位[0]]).名称
            x5.装备栏[不可更换部位[1]] = equ.get_equ_by_index(三件套名称, '史诗',
                                                     部位列表[不可更换部位[1]]).名称

            x2.切换详情 = trans(部位列表[可更换部位[0]]) + ':' + trans(
                属性.装备栏[可更换部位[0]]) + ' → ' + trans(x2.装备栏[可更换部位[0]])
            x3.切换详情 = trans(部位列表[可更换部位[1]]) + ':' + trans(
                属性.装备栏[可更换部位[1]]) + ' → ' + trans(x3.装备栏[可更换部位[1]])
            x4.切换详情 = trans(部位列表[可更换部位[2]]) + ':' + trans(
                属性.装备栏[可更换部位[2]]) + ' → ' + trans(x4.装备栏[可更换部位[2]])
            x5.切换详情 = trans(属性.套装栏[2]) + ' → ' + trans(x5.套装栏[2])
            return [x1, x2, x3, x4, x5]
        else:
            return [deepcopy(属性)]

    def 希洛克计算(self, 希洛克选择状态=None):

        if 希洛克选择状态 is None:
            希洛克选择状态 = self.希洛克选择状态

        sirocos = []

        for i in range(15):
            if 希洛克选择状态[i] == 1:
                siroco = SirocoList[i // 3]
                if siroco not in sirocos:
                    siroco.set_character(self)
                    sirocos.append(siroco)
                siroco.fuse(i % 3)

        for siroco in sirocos:
            siroco.compute()

        # 自选词条
        if self.希洛克武器词条 == 2:
            武器融合属性A = 武器属性A列表[self.残香词条[0]]
            武器融合属性A数值 = 武器融合属性A.最大值 - 武器融合属性A.间隔 * self.残香词条[1]
            武器融合属性A.当前值 = int(武器融合属性A数值)
            武器融合属性A.融合属性(self)
            if sum(希洛克选择状态) == 3:
                武器融合属性B = 武器属性B列表[self.残香词条[2]]

                武器融合属性B数值 = 武器融合属性B.最大值 - 武器融合属性B.间隔 * self.残香词条[3]
                武器融合属性B.当前值 = int(武器融合属性B数值)
                武器融合属性B.融合属性(self)

    def 奥兹玛计算(self, 奥兹玛选择状态=None):
        if 奥兹玛选择状态 is None:
            奥兹玛选择状态 = self.奥兹玛选择状态

        for i in range(25):
            if 奥兹玛选择状态[i] == 1:
                func = OzmaList[i // 5]
                func(self)
        return

    # 仅计算自选黑鸦遴选词条
    def 黑鸦计算(self, 黑鸦词条=None):
        if 黑鸦词条 is None:
            黑鸦词条 = self.黑鸦词条

        for i in range(0, 4):
            # 自选词条
            if 黑鸦词条[i][0] == 2:
                属性列表 = 装备变换属性列表 if i > 0 else 武器变换属性列表
                装备属性 = 属性列表[黑鸦词条[i][1]]
                value = 黑鸦词条[i][2]
                if isinstance(value, int):
                    value = 装备属性.最大值 - 黑鸦词条[i][2] * 装备属性.间隔
                else:
                    value = 装备属性.当前值
                装备属性.当前值 = value
                装备属性.变换属性(self)

    def compute(self, match=None, handle=None):
        if match is None:

            def match(skill):
                return skill.是否启用

        if handle is None:

            def handle(skill, values):
                return values

        data = []
        for skill in self.技能表.values():
            values = skill.结算统计(self) if match(skill) else [0] * 8
            values = handle(skill, values)
            data.append(values)
        self.awake_computed = False
        return data

    def 预计算(self, 自动切装=False):
        if self.双装备模式 == 1 and 自动切装:
            # 用于计算一觉
            temp = deepcopy(self)
            # 拷贝数据,并修改装备,返回可能的组合
            数据列表 = []
            切换列表 = []
            替换属性_temp = []
            可能组合 = self.装备替换(temp)
            for 一觉计算属性 in 可能组合:
                一觉计算属性.装备属性计算()
                一觉计算属性.适用数值计算()
                替换属性_temp.append(一觉计算属性)
                一觉计算属性.awake_computed = False
                一觉 = 一觉计算属性.技能表['一次觉醒']
                三觉 = 一觉计算属性.技能表['三次觉醒']
                数据 = 三觉.结算统计(一觉计算属性)[3]
                if 一觉.名称 not in 三觉.关联技能:
                    数据 += 一觉.结算统计(一觉计算属性)[3]
                一觉计算属性.awake_computed = False
                数据列表.append(数据)  # 3是力量属性  一觉力智都是相等的
                切换列表.append(一觉计算属性.切换详情)
                # 取一觉最大值,并修改数据
            a = max(数据列表)
            序号 = 数据列表.index(a)
            if 序号 != 0:
                temp = '<br><br>'
                一觉 = self.技能表['一次觉醒']
                三觉 = self.技能表['三次觉醒']
                b = int(数据列表[0])
                c = int(a) - int(b)
                if 一觉.名称 not in 三觉.关联技能:
                    temp += trans(一觉.名称) + '+'
                temp += "{}:{}->{}(+{})".format(trans(三觉.名称), b, a, c)
            else:
                temp = ''
                # 计算现有装备BUFF
            self.装备属性计算()
            # 一觉属性替换
            替换属性 = 替换属性_temp[序号]
            self.一觉Lv = 替换属性.一觉Lv
            self.一觉力智 = 替换属性.一觉力智
            self.一觉力智per = 替换属性.一觉力智per

            P = deepcopy(self)
            适用数值 = P.适用数值计算()
            适用数值补正 = 替换属性.技能表['一次觉醒'].适用数值 - 适用数值

            self.自适应计算()
            self.适用数值计算()

            self.技能表['一次觉醒'].等级 = 替换属性.技能表['一次觉醒'].等级
            self.技能表['二次觉醒'].等级 = 替换属性.技能表['二次觉醒'].等级
            self.技能表['三次觉醒'].等级 = 替换属性.技能表['三次觉醒'].等级
            self.技能表['一次觉醒'].适用数值 += 适用数值补正
            self.切换详情 = 切换列表[序号] + temp

        else:
            self.装备属性计算()
            self.自适应计算()
            self.适用数值计算()

    def 自适应计算(self):

        try:
            temp = deepcopy(self)
            temp.适用数值计算()

            in_pre_range = (ctypes.c_int * 6)()
            if self.希洛克武器词条 == 1:
                in_pre_range[0] = 1
                in_pre_range[1] = 1

            for i in range(4):
                if self.黑鸦词条[i][0] == 1:
                    in_pre_range[i + 2] = 1
            in_int_data, in_double_data = temp.get_data()
            preferred.cal_index_buff(in_pre_range, in_int_data, in_double_data)

            if self.希洛克武器词条 == 1:
                a = in_pre_range[0]
                b = in_pre_range[1]
                self.自适应最高值 = [a, b]
                self.武器属性输入(a, b)

            if self.黑鸦词条[0][0] == 1:
                self.武器变换属性自适应 = in_pre_range[2]
                self.黑鸦武器输入(in_pre_range[2])

            self.防具变换属性自适应 = in_pre_range[3:]
            self.黑鸦属性输入(in_pre_range[3:])
            pass
        except Exception as e:
            self.旧版自适应计算()
        pass

    def 旧版自适应计算(self):

        # 黑鸦词条计算
        黑鸦选择 = [0, 0, 0, 0]
        for i in range(4):
            if self.黑鸦词条[i][0] == 1:
                黑鸦选择[i] = 1
        # 武器词条自适应计算
        if self.希洛克武器词条 == 1:
            词条提升率 = []
            for i in range(len(武器属性组合)):
                temp = deepcopy(self)
                # 总数据 = []
                武器属性A = 武器属性组合[i][0]
                武器属性B = 武器属性组合[i][1]
                temp.武器属性输入(武器属性A, 武器属性B)

                提升率 = temp.择优提升率计算()
                词条提升率.append(提升率)
            a = max(词条提升率)
            序号 = 词条提升率.index(a)
            self.自适应最高值 = 武器属性组合[序号]
            self.武器属性输入(self.自适应最高值[0], self.自适应最高值[1])

        # 先择优黑鸦防具部分
        if 黑鸦选择[1] + 黑鸦选择[2] + 黑鸦选择[3] > 0:
            词条提升率 = []
            for i in range(len(防具变换属性组合)):
                temp = deepcopy(self)
                # 总数据 = []
                temp.黑鸦属性输入(防具变换属性组合[i])
                提升率 = temp.择优提升率计算()
                词条提升率.append(提升率)
            a = max(词条提升率)
            序号 = 词条提升率.index(a)
            self.防具变换属性自适应 = 防具变换属性组合[序号]
            self.黑鸦属性输入(self.防具变换属性自适应)

        # 再择优武器部分
        if 黑鸦选择[0] > 0:
            词条提升率 = []
            for i in range(7):
                temp = deepcopy(self)
                # 总数据 = []
                temp.黑鸦武器输入(i)
                if temp.实际名称 == 'BUFF·神启·圣骑士':
                    if i == 0:
                        temp.是否加觉醒 = 1
                    else:
                        temp.是否加觉醒 = 0
                提升率 = temp.择优提升率计算()
                词条提升率.append(提升率)
            a = max(词条提升率)
            序号 = 词条提升率.index(a)
            self.武器变换属性自适应 = 序号
            self.黑鸦武器输入(序号)
            if 序号 == 0 and self.实际名称 == 'BUFF·神启·圣骑士':
                self.是否加觉醒 = 1

    def 替换技能(self, skill, name):
        skill.技能表 = self.技能表
        self.技能表[name] = skill

    def 武器属性输入(self, index_a, index_b):
        武器属性A = 武器属性A列表[index_a]
        武器属性A.当前值 = int(武器属性A.最大值)
        武器属性A.融合属性(self)
        if self.武器词条触发 == 1:
            武器属性B = 武器属性B列表[index_b]
            武器属性B.当前值 = int(武器属性B.最大值)
            武器属性B.融合属性(self)
        else:
            index_b = 0
        self.残香词条 = [index_a, 0, index_b, 0]

    def 黑鸦属性输入(self, indices):
        for i in range(1, 4):
            if self.黑鸦词条[i][0] == 1:
                index = indices[i - 1]
                装备属性 = 装备变换属性列表[index]
                装备属性.当前值 = int(装备属性.最大值)
                装备属性.变换属性(self)
                self.黑鸦词条[i] = [1, index, 装备属性.最大值]

    def 黑鸦武器输入(self, index):
        if self.黑鸦词条[0][0] == 1:
            if index > 0:
                黑鸦武器 = 武器变换属性列表[index]
                黑鸦武器.当前值 = int(黑鸦武器.最大值)
                黑鸦武器.变换属性(self)
                self.黑鸦词条[0] = [1, index, 黑鸦武器.最大值]
            else:
                self.技能等级加成('所有', 50, 50, 2)
                self.技能等级加成('所有', 85, 85, 2)
                self.技能等级加成('所有', 100, 100, 2)
            if self.装备检查('世界树之精灵'):
                self.技能等级加成('所有', 50, 50, 2)

    def 择优提升率计算(self):
        总数据 = []
        self.适用数值计算()
        if self.双装备模式 == 1 and self.技能表['一次觉醒'].是否启用:
            if self.实际名称 == 'BUFF·神启·圣骑士':
                if self.是否加觉醒 == 1:
                    self.技能表['一次觉醒'].适用数值 += self.一觉切装加二觉增加体精

        def handle(skill, values):
            if skill.所在等级 in [50, 100]:
                values = [int(round(i * self.觉醒择优系数)) for i in values]
            return values

        self.compute(None, handle)

        return self.提升率计算(总数据)

    def 结果返回(self, x, 总数据):
        if x == 0:
            return self.提升率计算(总数据)
        elif x == 1:
            return 总数据
        elif x == 2:
            return self.提升率计算(总数据, self.排行系数)

    def BUFF计算(self, x=0):
        self.预计算(自动切装=True)
        总数据 = self.compute()
        return self.结果返回(x, 总数据)

    def 装备属性计算(self, x=0):
        self.装备基础()
        # self.专属词条计算()

        equips = [equ.get_equ_by_name(i) for i in self.装备栏]
        suits = [equ.get_suit_by_name(i) for i in self.套装栏]

        for equip in equips:
            equip.城镇属性_BUFF(self)
            equip.BUFF属性(self)

            觉醒词条 = self.黑鸦词条[0][0]

            # 黑鸦武器觉醒词条
            if 觉醒词条 == 3 and equip.部位 == '武器':
                self.技能等级加成('所有', 50, 50, 2)
                self.技能等级加成('所有', 85, 85, 2)
                self.技能等级加成('所有', 100, 100, 2)
            if equip.名称 == '世界树之精灵' and 觉醒词条 > 0:
                self.技能等级加成('所有', 50, 50, -2)
                self.技能等级加成('所有', 85, 85, -2)
                self.技能等级加成('所有', 100, 100, -2)
                if 觉醒词条 > 1:
                    self.技能等级加成('所有', 50, 50, 2)

        for suit in suits:
            suit.城镇属性_BUFF(self)
            suit.BUFF属性(self)

        self.黑鸦计算()
        self.希洛克计算()
        self.奥兹玛计算()

        if self.排行系数 == 1 or x:
            P = deepcopy(self)
            P.站街计算()
            self.站街系数 = P.系数数值站街()

        if x:
            return

        for equip in equips:
            equip.进图属性_BUFF(self)

        for suit in suits:
            suit.进图属性_BUFF(self)

    def 专属词条计算(self):
        pass

    def 站街计算(self):
        self.专属词条计算()

        for skill in self.技能表.values():
            if skill.站街生效 == 1:
                skill.进图加成 = 0
                结算 = skill.结算统计(self)
                self.智力 += 结算[0]
                self.体力 += 结算[1]
                self.精神 += 结算[2]

    def 护石计算(self):
        indices = self.护石栏
        for i in indices:
            Talismans(self, i)

    def BUFF面板(self):
        return self.技能表['BUFF'].技能面板()

    def 一觉面板(self):
        return self.技能表['一次觉醒'].技能面板()
