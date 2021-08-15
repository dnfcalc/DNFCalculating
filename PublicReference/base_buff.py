from PublicReference.equipment.equ_list import *
from PublicReference.equipment.称号_buff import *
from PublicReference.equipment.宠物_buff import *
from PublicReference.equipment.辟邪玉_buff import *
from PublicReference.equipment.武器融合_buff import *
from PublicReference.equipment.黑鸦_buff import *
from PublicReference.choise.选项设置_buff import *
from PublicReference.common import *
from PublicReference.buff_panel import *
from PublicReference.view.DialogRegister import DefaultDialogRegister
from PublicReference.utils.store import Store

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

    def 等级加成(self, x):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                if self.基础等级 != self.等级上限:
                    self.等级溢出 = 1
            else:
                self.等级 += x

    def 结算统计(self):
        return [0, 0, 0, 0, 0, 0, 0, 0]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 被动技能(技能):
    是否主动 = 0
    进图加成 = 0


class 主动技能(技能):
    是否主动 = 1
    适用数值 = 0


史诗防具智力Lv100 = {"上衣": 149, "头肩": 139, "下装": 149, "腰带": 130, "鞋": 130}
史诗防具体力Lv100 = {"上衣": 54, "头肩": 43, "下装": 54, "腰带": 32, "鞋": 32}
史诗防具精神Lv100 = {"上衣": 0, "头肩": 0, "下装": 0, "腰带": 0, "鞋": 0}
神话上衣额外智力 = 1
神话上衣额外体力 = 1
神话上衣额外精神 = 0

传说防具智力Lv100 = {"上衣": 47, "头肩": 39, "下装": 47, "腰带": 29, "鞋": 29}
传说防具体力Lv100 = {"上衣": 52, "头肩": 42, "下装": 52, "腰带": 31, "鞋": 31}
传说防具精神Lv100 = {"上衣": 0, "头肩": 0, "下装": 0, "腰带": 0, "鞋": 0}

防具智力Lv95 = {"上衣": 46, "头肩": 37, "下装": 46, "腰带": 28, "鞋": 28}
防具体力Lv95 = {"上衣": 52, "头肩": 41, "下装": 52, "腰带": 31, "鞋": 31}
防具精神Lv95 = {"上衣": 0, "头肩": 0, "下装": 0, "腰带": 0, "鞋": 0}


class 角色属性(属性):
    职业分类 = 'BUFF'
    C力智 = 5000
    C三攻 = 3000
    系统奶系数 = 0
    系统奶基数 = 0
    排行类型 = '物理百分比'
    称号触发 = False

    排行系数 = 0
    站街系数 = 0

    百分比体精 = 0.0

    被动进图加成 = 0
    守护恩赐体精 = 0
    守护徽章per = 0
    转职被动智力 = 0
    BUFF额外增幅率 = 0

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

    def 力智固定加成(self, x=0, y=0):
        if self.装备描述 == 1:
            return '力量、智力 +{}<br>'.format(x)
        else:
            self.力量 += x
            self.智力 += x
        return ''

    def 体精固定加成(self, x=0, y=0):
        if self.装备描述 == 1:
            return '体力、精神 +{}<br>'.format(x)
        else:
            self.体力 += x
            self.精神 += x
        return ''

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
        if self.装备描述 == 1:
            tem = ''
            if BUFFLv > 0:
                if self.角色 == '圣职者(女)':
                    tem += '[勇气祝福]技能Lv +{}<br>'.format(int(BUFFLv))
                elif self.角色 == '圣职者(男)':
                    tem += '[荣誉祝福]技能Lv +{}<br>'.format(int(BUFFLv))
                elif self.角色 == '魔法师(女)':
                    tem += '[禁忌诅咒]技能Lv +{}<br>'.format(int(BUFFLv))

            if BUFF力量 > 0 and BUFF智力 > 0:
                tem += 'Lv30 Buff技能力量、智力增加量 +{}<br>'.format(int(BUFF力量))
            elif BUFF力量 > 0:
                tem += 'Lv30 Buff技能力量增加量 +{}<br>'.format(int(BUFF力量))
            elif BUFF智力 > 0:
                tem += 'Lv30 Buff技能智力增加量 +{}<br>'.format(int(BUFF智力))

            if BUFF力量per > 1 and BUFF智力per > 1:
                tem += 'Lv30 Buff技能力智增加量 +{}%<br>'.format(
                    round((BUFF力量per - 1) * 100, 0))
            elif BUFF力量per > 1:
                tem += 'Lv30 Buff技能力量增加量 +{}%<br>'.format(
                    round((BUFF力量per - 1) * 100, 0))
            elif BUFF智力per > 1:
                tem += 'Lv30 Buff技能智力增加量 +{}%<br>'.format(
                    round((BUFF智力per - 1) * 100, 0))

            if BUFF物攻 > 0 and BUFF魔攻 > 0 and BUFF独立 > 0:
                tem += 'Lv30 Buff技能三攻攻击力增加量 +{}<br>'.format(int(BUFF物攻))
            elif BUFF物攻 > 0:
                tem += 'Lv30 Buff技能物理攻击力增加量 +{}<br>'.format(int(BUFF物攻))
            elif BUFF魔攻 > 0:
                tem += 'Lv30 Buff技能魔法攻击力增加量 +{}<br>'.format(int(BUFF魔攻))
            elif BUFF独立 > 0:
                tem += 'Lv30 Buff技能独立攻击力增加量 +{}<br>'.format(int(BUFF独立))

            if BUFF物攻per > 1 and BUFF魔攻per > 1 and BUFF独立per > 1:
                tem += 'Lv30 Buff技能三攻攻击力增加量 +{}%<br>'.format(
                    round((BUFF物攻per - 1) * 100, 0))
            elif BUFF物攻per > 1:
                tem += 'Lv30 Buff技能物理攻击力增加量 +{}%<br>'.format(
                    round((BUFF物攻per - 1) * 100, 0))
            elif BUFF魔攻per > 1:
                tem += 'Lv30 Buff技能魔法攻击力增加量 +{}%<br>'.format(
                    round((BUFF魔攻per - 1) * 100, 0))
            elif BUFF独立per > 1:
                tem += 'Lv30 Buff技能独立攻击力增加量 +{}%<br>'.format(
                    round((BUFF独立per - 1) * 100, 0))
            return tem
        else:
            self.BUFFLv += BUFFLv
            self.BUFF力量 += BUFF力量
            self.BUFF智力 += BUFF智力
            self.BUFF物攻 += BUFF物攻
            self.BUFF魔攻 += BUFF魔攻
            self.BUFF独立 += BUFF独立
            self.BUFF力量per *= BUFF力量per
            self.BUFF智力per *= BUFF智力per
            self.BUFF物攻per *= BUFF物攻per
            self.BUFF魔攻per *= BUFF魔攻per
            self.BUFF独立per *= BUFF独立per
        return ''

    def 被动增加(self,
             守护恩赐Lv=0,
             守护恩赐体精=0,
             转职被动Lv=0,
             转职被动智力=0,
             信念光环Lv=0,
             信念光环体精=0,
             一觉被动Lv=0,
             一觉被动力智=0):
        if self.装备描述 == 1:
            tem = ''
            if 守护恩赐Lv > 0 or 转职被动Lv > 0:
                tem += '[守护恩赐]、[启示:圣歌]、[人偶操纵者]技能Lv +{}<br>'.format(
                    int(守护恩赐Lv if 守护恩赐Lv else 转职被动Lv))
            elif 守护恩赐体精 > 0 and self.角色 == '圣职者(男)':
                tem += '[守护恩赐]体力、精神 +{}<br>'.format(int(守护恩赐体精))
            elif 转职被动智力 > 0 and self.角色 == '圣职者(女)':
                tem += '[启示:圣歌]智力 +{}<br>'.format(int(转职被动智力))
            elif 转职被动智力 > 0 and self.角色 == '魔法师(女)':
                tem += '[人偶操纵者]智力 +{}<br>'.format(int(转职被动智力))
            elif 信念光环Lv > 0:
                tem += '[信念光环]技能Lv +{}'.format(int(信念光环Lv))
            elif 一觉被动Lv > 0:
                if self.角色 == '圣职者(女)':
                    tem += '[虔诚信念]技能Lv +{}<br>'.format(int(一觉被动Lv))
                elif self.角色 == '魔法师(女)':
                    tem += '[少女的爱]技能Lv +{}<br>'.format(int(一觉被动Lv))
            elif 信念光环体精 > 0:
                tem += '[信念光环]体力、精神增加量 +{}<br>'.format(int(信念光环体精))
            elif 一觉被动力智 > 0:
                tem += '[虔诚信念]、[少女的爱]力量、智力增加量 +{}<br>'.format(int(一觉被动力智))
            return tem
        else:
            self.转职被动Lv += 转职被动Lv
            self.守护恩赐体精 += 守护恩赐体精
            self.转职被动智力 += 转职被动智力
            self.一觉被动Lv += 一觉被动Lv
            self.信念光环体精 += 信念光环体精
            self.一觉被动力智 += 一觉被动力智
        return ''

    def 觉醒增加(self, 一觉Lv=0, 一觉力智=0, 一觉力智per=1):
        if self.装备描述 == 1:
            tem = ''
            if 一觉Lv > 0:
                if self.角色 == '圣职者(女)':
                    tem += '[圣光天启]技能Lv +{}<br>'.format(int(一觉Lv))
                elif self.角色 == '圣职者(男)':
                    tem += '[天启之珠]技能Lv +{}<br>'.format(int(一觉Lv))
                elif self.角色 == '魔法师(女)':
                    tem += '[开幕！人偶剧场]技能Lv +{}<br>'.format(int(一觉Lv))
            elif 一觉力智 > 0:
                tem += 'Lv50 主动技能力量、智力增加量 +{}<br>'.format(int(一觉力智))
            elif 一觉力智per > 1:
                tem += 'Lv50 主动技能力量、智力增加量 +{}%<br>'.format(
                    round((一觉力智per - 1) * 100, 0))
            return tem
        else:
            self.一觉Lv += 一觉Lv
            self.一觉力智 += 一觉力智
            self.一觉力智per *= 一觉力智per
        return ''

    def 系数数值站街(self):
        if self.类型 == '智力':
            return self.智力
        elif self.类型 == '体力':
            return self.体力
        elif self.类型 == '精神':
            return self.精神

    def 系数数值进图(self):
        if self.类型 == '智力':
            return self.进图智力
        elif self.类型 == '体力':
            return self.进图体力
        elif self.类型 == '精神':
            return self.进图精神

    def 防具精通计算(self, i):
        temp = equ.get_equ_by_name(self.装备栏[i])
        if temp.所属套装 != '智慧产物':
            return 精通体力(temp.等级, temp.品质, self.强化等级[i], 部位列表[i])
        else:
            return 精通体力(temp.等级, temp.品质, self.改造等级[i], 部位列表[i])

    def 装备基础(self):
        if equ.get_equ_by_name(self.装备栏[0]).品质 == '神话':
            self.智力 += 神话上衣额外智力
            self.体力 += 神话上衣额外体力
            self.精神 += 神话上衣额外精神
        for i in [0, 1, 2, 3, 4]:
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
            if temp.等级 == 100 and temp.品质 in ['史诗', '神话']:
                self.智力 += 史诗防具智力Lv100[temp.部位]
                self.体力 += 史诗防具体力Lv100[temp.部位]
                self.精神 += 史诗防具精神Lv100[temp.部位]
            elif temp.等级 == 95 and temp.品质 == '史诗':
                self.智力 += 防具智力Lv95[temp.部位]
                self.体力 += 防具体力Lv95[temp.部位]
                self.精神 += 防具精神Lv95[temp.部位]
            elif temp.等级 == 100 and temp.品质 == '传说':
                self.智力 += 传说防具智力Lv100[temp.部位]
                self.体力 += 传说防具体力Lv100[temp.部位]
                self.精神 += 传说防具精神Lv100[temp.部位]

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
            for i in self.技能栏:
                if i.所在等级 >= min and i.所在等级 <= max:
                    if 加成类型 == '所有':
                        i.等级加成(lv)
                    else:
                        if i.是否主动 == 1:
                            i.等级加成(lv)
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

        x1 = ((self.C力智 + (self.C力智 - 950) * self.系统奶系数 +
               self.系统奶基数) / 250 + 1) * self.C三攻

        if self.排行类型 == '物理百分比':
            x2 = ((self.C力智 + (self.C力智 - 950) * self.系统奶系数 + self.系统奶基数 + 力量合计) / 250 +
                  1) * (self.C三攻 + 物攻合计)
        elif self.排行类型 == '魔法百分比':
            x2 = ((self.C力智 + (self.C力智 - 950) * self.系统奶系数 + self.系统奶基数 + 智力合计) / 250 +
                  1) * (self.C三攻 + 魔攻合计)
        elif self.排行类型 == '物理固伤':
            x2 = ((self.C力智 + (self.C力智 - 950) * self.系统奶系数 + self.系统奶基数 + 力量合计) / 250 +
                  1) * (self.C三攻 + 独立合计)
        elif self.排行类型 == '魔法固伤':
            x2 = ((self.C力智 + (self.C力智 - 950) * self.系统奶系数 + self.系统奶基数 + 智力合计) / 250 +
                  1) * (self.C三攻 + 独立合计)

        return [x2 / x1 * 100, int(self.站街系数), 力量合计, 智力合计, 物攻合计, 魔攻合计, 独立合计][x]

    def 适用数值计算(self):
        self.专属词条计算()
        for i in range(len(self.技能栏)):
            if self.次数输入[i] != 0:
                self.智力 += self.技能栏[i].结算统计()[0]
                self.体力 += self.技能栏[i].结算统计()[1]
                self.精神 += self.技能栏[i].结算统计()[2]

        self.进图智力 += self.智力
        self.进图体力 += self.体力
        self.进图精神 += self.精神

        self.进图体力 *= 1 + self.百分比体精
        self.进图精神 *= 1 + self.百分比体精

        if self.类型 == '智力':
            self.BUFF适用面板 += self.进图智力 + self.BUFF补正力智
            for i in self.技能栏:
                if i.是否主动 == 1:
                    if i.所在等级 == 30:
                        i.适用数值 = self.BUFF适用面板
                    else:
                        i.适用数值 = self.进图智力

        elif self.类型 == '体力':
            self.BUFF适用面板 += self.进图体力 + self.BUFF补正体力
            for i in self.技能栏:
                if i.是否主动 == 1:
                    if i.所在等级 == 30:
                        i.适用数值 = self.BUFF适用面板
                    else:
                        i.适用数值 = self.进图体力

        elif self.类型 == '精神':
            self.BUFF适用面板 += self.进图精神 + self.BUFF补正精神
            for i in self.技能栏:
                if i.是否主动 == 1:
                    if i.所在等级 == 30:
                        i.适用数值 = self.BUFF适用面板
                    else:
                        i.适用数值 = self.进图精神

    # 返回可能的组合列表
    def 装备替换(self, 属性):
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
                i.装备栏[num * 2] = equ.get_equ_by_index(equ.get_equ_by_name(i.装备栏[1]).所属套装, '史诗',
                                                      equ.get_equ_by_name(i.装备栏[num * 2]).部位).名称
                i.套装栏[2 * num + 2] = i.套装栏[2 * num + 2].replace(
                    equ.get_equ_by_name(i.装备栏[index[num]]).所属套装,
                    equ.get_equ_by_name(i.装备栏[1]).所属套装)
                i.切换详情 = equ.get_equ_by_name(i.装备栏[num * 2]).部位 + ':' + x1.装备栏[
                    num * 2] + ' → ' + i.装备栏[num * 2]
                num += 1
            return [x1, x2, x3, x4]
        elif sumcount == 6:
            index = count.index(0)
            部位 = {2: 6, 4: 5, 6: 7}
            x1 = deepcopy(属性)
            x2 = deepcopy(属性)
            x2.装备栏[index - 2] = equ.get_equ_by_index(equ.get_equ_by_name(x2.装备栏[部位[index]]).所属套装, '史诗',
                                                     equ.get_equ_by_name(x2.装备栏[index - 2]).部位).名称
            x2.套装栏[index] = x2.套装栏[index].replace(
                equ.get_equ_by_name(x2.装备栏[1]).所属套装, equ.get_equ_by_name(x2.装备栏[部位[index]]).所属套装)
            x2.切换详情 = equ.get_equ_by_name(x2.装备栏[index - 2]).部位 + ':' + x1.装备栏[
                index - 2] + ' → ' + x2.装备栏[index - 2]
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
            x2.装备栏[可更换部位[0]] = equ.get_equ_by_index(两件套名称, '史诗', 部位列表[可更换部位[0]]).名称
            x3.装备栏[可更换部位[1]] = equ.get_equ_by_index(两件套名称, '史诗', 部位列表[可更换部位[1]]).名称
            x4.装备栏[可更换部位[2]] = equ.get_equ_by_index(两件套名称, '史诗', 部位列表[可更换部位[2]]).名称
            x5.装备栏[不可更换部位[0]] = equ.get_equ_by_index(三件套名称, '史诗', 部位列表[不可更换部位[0]]).名称
            x5.装备栏[不可更换部位[1]] = equ.get_equ_by_index(三件套名称, '史诗', 部位列表[不可更换部位[1]]).名称

            x2.切换详情 = 部位列表[可更换部位[0]] + ':' + 属性.装备栏[可更换部位[0]] + ' → ' + x2.装备栏[
                可更换部位[0]]
            x3.切换详情 = 部位列表[可更换部位[1]] + ':' + 属性.装备栏[可更换部位[1]] + ' → ' + x3.装备栏[
                可更换部位[1]]
            x4.切换详情 = 部位列表[可更换部位[2]] + ':' + 属性.装备栏[可更换部位[2]] + ' → ' + x4.装备栏[
                可更换部位[2]]
            x5.切换详情 = 属性.套装栏[2] + ' → ' + x5.套装栏[2]
            return [x1, x2, x3, x4, x5]
        else:
            return [deepcopy(属性)]

    def 数据计算(self):
        总数据 = []
        if self.双装备模式 == 1 and self.次数输入[self.一觉序号] != 0:
            # 用于计算一觉
            temp = deepcopy(self)

            # 拷贝数据,并修改装备,返回可能的组合
            数据列表 = []
            切换列表 = []
            一觉计算属性_temp = []
            替换属性_temp = []
            可能组合 = self.装备替换(temp)
            for 一觉计算属性 in 可能组合:
                一觉计算属性.装备属性计算()
                替换属性_temp.append(deepcopy(一觉计算属性))
                一觉计算属性.适用数值计算()
                一觉计算属性_temp.append(一觉计算属性)
                数据列表.append(
                    一觉计算属性.技能栏[self.一觉序号].结算统计()[3] *
                    (一觉计算属性.技能栏[self.三觉序号].加成倍率() if self.三觉序号 != 0 and
                                                     self.次数输入[self.三觉序号] != 0 else 1))  # 3是力量属性  一觉力智都是相等的
                切换列表.append(一觉计算属性.切换详情)

            # 取一觉最大值,并修改数据
            a = max(数据列表)
            序号 = 数据列表.index(a)
            if 序号 != 0:
                temp = '<br><br>' + (
                    (self.技能栏[self.一觉序号].名称 + '+' + self.技能栏[self.三觉序号].名称 +
                     ':') if self.三觉序号 != 0 else
                    (self.技能栏[self.一觉序号].名称 + ':')) + str(int(
                    数据列表[0])) + '→' + str(
                    int(a)) + ' (+' + str(int(a) - int(数据列表[0])) + ')'
            else:
                temp = ''
            # 计算现有装备BUFF
            self.装备属性计算()
            # 一觉属性替换
            替换属性 = 替换属性_temp[序号]
            self.一觉Lv = 替换属性.一觉Lv
            self.一觉力智 = 替换属性.一觉力智
            self.一觉适用数值 = 一觉计算属性_temp[序号].技能栏[self.一觉序号].适用数值
            self.一觉力智per = 替换属性.一觉力智per
            self.技能栏[self.一觉序号] = 替换属性.技能栏[self.一觉序号]
            self.技能栏[self.三觉序号] = 替换属性.技能栏[self.三觉序号]
            if self.实际名称 == 'BUFF·神启·圣骑士':
                if self.类型 == '体力':
                    temp1 = 一觉计算属性_temp[序号].技能栏[
                        一觉计算属性_temp[序号].技能序号['神圣洗礼：信仰之翼']].结算统计()[1]
                elif self.类型 == '精神':
                    temp1 = 一觉计算属性_temp[序号].技能栏[
                        一觉计算属性_temp[序号].技能序号['神圣洗礼：信仰之翼']].结算统计()[2]
                一觉计算属性_temp[序号].技能等级加成('所有', 85, 85, 2)
                if self.类型 == '体力':
                    temp2 = 一觉计算属性_temp[序号].技能栏[
                        一觉计算属性_temp[序号].技能序号['神圣洗礼：信仰之翼']].结算统计()[1]
                elif self.类型 == '精神':
                    temp2 = 一觉计算属性_temp[序号].技能栏[
                        一觉计算属性_temp[序号].技能序号['神圣洗礼：信仰之翼']].结算统计()[2]
                self.一觉切装加二级增加体精 = (temp2 - temp1) * (1 +
                                                      一觉计算属性_temp[序号].百分比体精)
                self.是否加觉醒 = 0
            self.自适应计算()
            self.适用数值计算()
            if self.实际名称 == 'BUFF·神启·圣骑士':
                if self.是否加觉醒 == 1:
                    一觉计算属性_temp[序号].技能栏[self.一觉序号].适用数值 += self.一觉切装加二级增加体精
            self.技能栏[self.一觉序号].适用数值 = 一觉计算属性_temp[序号].技能栏[self.一觉序号].适用数值
            self.切换详情 = 切换列表[序号] + temp
            for i in range(len(self.技能栏)):
                if self.次数输入[i] != 0:
                    总数据.append(self.技能栏[i].结算统计())
                else:
                    总数据.append([0, 0, 0, 0, 0, 0, 0, 0])
            总数据[self.一觉序号] = [
                int(x * self.次数输入[self.一觉序号]) for x in 总数据[self.一觉序号]
            ]
        else:
            self.装备属性计算()
            self.自适应计算()
            self.适用数值计算()
            for i in range(len(self.技能栏)):
                if self.次数输入[i] != 0:
                    总数据.append(self.技能栏[i].结算统计())
                else:
                    总数据.append([0, 0, 0, 0, 0, 0, 0, 0])
            总数据[self.一觉序号] = [
                int(x * self.次数输入[self.一觉序号]) for x in 总数据[self.一觉序号]
            ]
            self.一觉数据 = 总数据[self.一觉序号]
        self.一觉数据 = []
        self.一觉数据.append(int(总数据[self.一觉序号][3]))
        self.一觉数据.append(int(总数据[self.一觉序号][4]))
        return 总数据

    def 自适应计算(self):

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
                # temp.适用数值计算()
                # if temp.双装备模式 == 1 and temp.次数输入[temp.一觉序号] != 0:
                #     temp.技能栏[temp.一觉序号].适用数值 = temp.一觉适用数值
                # for i in range(len(temp.技能栏)):
                #     if temp.次数输入[i] != 0:
                #         总数据.append(temp.技能栏[i].结算统计())
                #     else:
                #         总数据.append([0, 0, 0, 0, 0, 0, 0, 0])
                # for i in range(len(temp.技能栏)):
                #     if i.名称 == '勇气圣歌':
                #         if self.次数输入[self.技能序号['勇气圣歌']] != 0:
                #             总数据[self.技能序号['勇气圣歌']][j] = int(总数据[self.技能序号['勇气祝福']][j] * self.技能栏[self.技能序号['勇气圣歌']].增幅倍率)
                #     if i.名称 == '死命召唤':
                #         if self.次数输入[self.技能序号['死命召唤']] != 0:
                #             总数据[self.技能序号['死命召唤']][j] = int(总数据[self.技能序号['禁忌诅咒']][j] * self.技能栏[self.技能序号['死命召唤']].增幅倍率)
                #     if i.名称 == '小魔女的偏爱':
                #         if self.次数输入[self.技能序号['小魔女的偏爱']] != 0:
                #             总数据[self.技能序号['禁忌诅咒']][j] = int(总数据[self.技能序号['禁忌诅咒']][j] * (1 + self.技能栏[self.技能序号['小魔女的偏爱']].增幅倍率))
                # 总数据[temp.一觉序号] = [int(x*temp.次数输入[temp.一觉序号]) for x in 总数据[temp.一觉序号]]
                # 三觉属性 = 总数据[temp.一觉序号][3] * (temp.技能栏[temp.三觉序号].加成倍率() - 1)
                # 总数据[temp.三觉序号] = [0, 0, 0, 三觉属性, 三觉属性, 0, 0, 0]
                # 提升率 = temp.提升率计算(总数据)
                提升率 = self.择优提升率计算(temp)
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
                黑鸦戒指 = 防具变换属性组合[i][0]
                黑鸦辅助 = 防具变换属性组合[i][1]
                黑鸦下装 = 防具变换属性组合[i][2]
                temp.黑鸦属性输入(黑鸦戒指, 黑鸦辅助, 黑鸦下装)
                # temp.适用数值计算()
                # if temp.双装备模式 == 1 and temp.次数输入[temp.一觉序号] != 0:
                #     temp.技能栏[temp.一觉序号].适用数值 = temp.一觉适用数值
                # for i in range(len(temp.技能栏)):
                #     if temp.次数输入[i] != 0:
                #         总数据.append(temp.技能栏[i].结算统计())
                #     else:
                #         总数据.append([0, 0, 0, 0, 0, 0, 0, 0])
                # for i in range(len(temp.技能栏)):
                #     if i.名称 == '勇气圣歌':
                #         if self.次数输入[self.技能序号['勇气圣歌']] != 0:
                #             总数据[self.技能序号['勇气圣歌']][j] = int(总数据[self.技能序号['勇气祝福']][j] * self.技能栏[self.技能序号['勇气圣歌']].增幅倍率)
                #     if i.名称 == '死命召唤':
                #         if self.次数输入[self.技能序号['死命召唤']] != 0:
                #             总数据[self.技能序号['死命召唤']][j] = int(总数据[self.技能序号['禁忌诅咒']][j] * self.技能栏[self.技能序号['死命召唤']].增幅倍率)
                #     if i.名称 == '小魔女的偏爱':
                #         if self.次数输入[self.技能序号['小魔女的偏爱']] != 0:
                #             总数据[self.技能序号['禁忌诅咒']][j] = int(总数据[self.技能序号['禁忌诅咒']][j] * (1 + self.技能栏[self.技能序号['小魔女的偏爱']].增幅倍率))
                # 总数据[temp.一觉序号] = [int(x*temp.次数输入[temp.一觉序号]) for x in 总数据[temp.一觉序号]]
                # 三觉属性 = 总数据[temp.一觉序号][3] * (temp.技能栏[temp.三觉序号].加成倍率() - 1)
                # 总数据[temp.三觉序号] = [0, 0, 0, 三觉属性, 三觉属性, 0, 0, 0]
                # 提升率 = temp.提升率计算(总数据)
                提升率 = self.择优提升率计算(temp)
                词条提升率.append(提升率)
            a = max(词条提升率)
            序号 = 词条提升率.index(a)
            self.防具变换属性自适应 = 防具变换属性组合[序号]
            self.黑鸦属性输入(self.防具变换属性自适应[0], self.防具变换属性自适应[1],
                        self.防具变换属性自适应[2])

        # 再择优武器部分
        if 黑鸦选择[0] > 0:
            词条提升率 = []
            for i in range(7):
                temp = deepcopy(self)
                # 总数据 = []
                temp.黑鸦武器输入(i)
                # temp.适用数值计算()
                # if temp.双装备模式 == 1 and temp.次数输入[temp.一觉序号] != 0:
                #     temp.技能栏[temp.一觉序号].适用数值 = temp.一觉适用数值
                # for i in range(len(temp.技能栏)):
                #     if temp.次数输入[i] != 0:
                #         总数据.append(temp.技能栏[i].结算统计())
                #     else:
                #         总数据.append([0, 0, 0, 0, 0, 0, 0, 0])
                # for i in range(len(temp.技能栏)):
                #     if i.名称 == '勇气圣歌':
                #         if self.次数输入[self.技能序号['勇气圣歌']] != 0:
                #             总数据[self.技能序号['勇气圣歌']][j] = int(总数据[self.技能序号['勇气祝福']][j] * self.技能栏[self.技能序号['勇气圣歌']].增幅倍率)
                #     if i.名称 == '死命召唤':
                #         if self.次数输入[self.技能序号['死命召唤']] != 0:
                #             总数据[self.技能序号['死命召唤']][j] = int(总数据[self.技能序号['禁忌诅咒']][j] * self.技能栏[self.技能序号['死命召唤']].增幅倍率)
                #     if i.名称 == '小魔女的偏爱':
                #         if self.次数输入[self.技能序号['小魔女的偏爱']] != 0:
                #             总数据[self.技能序号['禁忌诅咒']][j] = int(总数据[self.技能序号['禁忌诅咒']][j] * (1 + self.技能栏[self.技能序号['小魔女的偏爱']].增幅倍率))
                # 总数据[temp.一觉序号] = [int(x*temp.次数输入[temp.一觉序号]) for x in 总数据[temp.一觉序号]]
                # 三觉属性 = 总数据[temp.一觉序号][3] * (temp.技能栏[temp.三觉序号].加成倍率() - 1)
                # 总数据[temp.三觉序号] = [0, 0, 0, 三觉属性, 三觉属性, 0, 0, 0]
                if temp.实际名称 == 'BUFF·神启·圣骑士':
                    if i == 0:
                        temp.是否加觉醒 = 1
                    else:
                        temp.是否加觉醒 = 0
                提升率 = self.择优提升率计算(temp)
                词条提升率.append(提升率)
            a = max(词条提升率)
            序号 = 词条提升率.index(a)
            self.武器变换属性自适应 = 序号
            self.黑鸦武器输入(序号)
            if 序号 == 0 and self.实际名称 == 'BUFF·神启·圣骑士':
                self.是否加觉醒 = 1
            # print(self.武器变换属性自适应)

    def 武器属性输入(self, 武器属性A, 武器属性B):
        武器属性A = 武器属性A列表[武器属性A]
        武器属性B = 武器属性B列表[武器属性B]
        武器属性A.当前值 = int(武器属性A.最大值)
        武器属性B.当前值 = int(武器属性B.最大值)
        武器属性A.融合属性(self)
        if self.武器词条触发 == 1:
            武器属性B.融合属性(self)

    def 黑鸦属性输入(self, 黑鸦戒指, 黑鸦辅助, 黑鸦下装):
        黑鸦戒指 = 装备变换属性列表[黑鸦戒指]
        黑鸦辅助 = 装备变换属性列表[黑鸦辅助]
        黑鸦下装 = 装备变换属性列表[黑鸦下装]
        黑鸦戒指.当前值 = int(黑鸦戒指.最大值)
        黑鸦辅助.当前值 = int(黑鸦辅助.最大值)
        黑鸦下装.当前值 = int(黑鸦下装.最大值)
        if self.黑鸦词条[1][0] == 1:
            黑鸦戒指.变换属性(self)
        if self.黑鸦词条[2][0] == 1:
            黑鸦辅助.变换属性(self)
        if self.黑鸦词条[3][0] == 1:
            黑鸦下装.变换属性(self)

    def 黑鸦武器输入(self, 黑鸦武器):
        if 黑鸦武器 > 0:
            黑鸦武器 = 武器变换属性列表[黑鸦武器]
            黑鸦武器.当前值 = int(黑鸦武器.最大值)
            黑鸦武器.变换属性(self)
        else:
            self.技能等级加成('所有', 50, 50, 2)
            self.技能等级加成('所有', 85, 85, 2)
            self.技能等级加成('所有', 100, 100, 2)
        if self.装备检查('世界树之精灵'):
            self.技能等级加成('所有', 50, 50, 2)

    def 择优提升率计算(self, temp):
        总数据 = []
        temp.适用数值计算()
        if temp.双装备模式 == 1 and temp.次数输入[temp.一觉序号] != 0:
            temp.技能栏[temp.一觉序号].适用数值 = temp.一觉适用数值
            if temp.实际名称 == 'BUFF·神启·圣骑士':
                if temp.是否加觉醒 == 1:
                    temp.技能栏[temp.一觉序号].适用数值 += temp.一觉切装加二级增加体精
        for i in range(len(temp.技能栏)):
            if temp.次数输入[i] != 0:
                总数据.append(temp.技能栏[i].结算统计())
            else:
                总数据.append([0, 0, 0, 0, 0, 0, 0, 0])
        for i in range(len(temp.技能栏)):
            if temp.技能栏[i].名称 == '勇气圣歌':
                if temp.次数输入[temp.技能序号['勇气圣歌']] != 0:
                    for j in range(8):
                        总数据[temp.技能序号['勇气圣歌']][j] = int(
                            总数据[temp.技能序号['勇气祝福']][j] *
                            temp.技能栏[temp.技能序号['勇气圣歌']].增幅倍率)
            if temp.技能栏[i].名称 == '死命召唤':
                if temp.次数输入[temp.技能序号['死命召唤']] != 0:
                    for j in range(8):
                        总数据[temp.技能序号['死命召唤']][j] = int(
                            总数据[temp.技能序号['禁忌诅咒']][j] *
                            temp.技能栏[temp.技能序号['死命召唤']].增幅倍率)
            if temp.技能栏[i].名称 == '小魔女的偏爱':
                if temp.次数输入[temp.技能序号['小魔女的偏爱']] != 0:
                    for j in range(8):
                        总数据[temp.技能序号['禁忌诅咒']][j] = int(
                            总数据[temp.技能序号['禁忌诅咒']][j] *
                            (1 + temp.技能栏[temp.技能序号['小魔女的偏爱']].增幅倍率))
        总数据[temp.一觉序号] = [
            int(x * temp.次数输入[temp.一觉序号]) for x in 总数据[temp.一觉序号]
        ]
        三觉属性 = 总数据[temp.一觉序号][3] * (temp.技能栏[temp.三觉序号].加成倍率() - 1)
        总数据[temp.三觉序号] = [0, 0, 0, 三觉属性, 三觉属性, 0, 0, 0]
        return temp.提升率计算(总数据)

    def 结果返回(self, x, 总数据):
        # if self.次数输入[self.一觉序号] != 0:
        #     if 总数据[self.一觉序号][3] != 0:
        #         总数据[self.一觉序号][3] = int(总数据[self.一觉序号][3]*self.次数输入[self.一觉序号])
        #         总数据[self.一觉序号][4] = int(总数据[self.一觉序号][4]*self.次数输入[self.一觉序号])
        #     #三觉CD大于一觉CD,因而增加一觉次数多于三觉次数的情况
        #     elif round(self.次数输入[self.一觉序号],2) > round(self.次数输入[self.三觉序号],2):
        #         总数据[self.一觉序号][3] = int(self.一觉数据[0] * (round(self.次数输入[self.一觉序号],2)-round(self.次数输入[self.三觉序号],2)))
        #         总数据[self.一觉序号][3] = int(self.一觉数据[1] * (round(self.次数输入[self.一觉序号],2)-round(self.次数输入[self.三觉序号],2)))
        # if self.次数输入[self.三觉序号] != 0:
        #     总数据[self.三觉序号][3] = int(总数据[self.三觉序号][3]*self.次数输入[self.三觉序号])
        #     总数据[self.三觉序号][4] = int(总数据[self.三觉序号][4]*self.次数输入[self.三觉序号])
        if x == 0:
            return self.提升率计算(总数据)
        elif x == 1:
            return 总数据
        elif x == 2:
            return self.提升率计算(总数据, self.排行系数)

    def BUFF计算(self, x=0):
        总数据 = self.数据计算()
        return self.结果返回(x, 总数据)

    def 装备属性计算(self):
        self.装备基础()
        # self.专属词条计算()
        for i in self.装备栏:
            equ.get_equ_by_name(i).城镇属性_BUFF(self)
            equ.get_equ_by_name(i).BUFF属性(self)
            if self.黑鸦词条[0][0] > 0 and equ.get_equ_by_name(i).名称 == '世界树之精灵':
                self.技能等级加成('所有', 50, 50, -2)
                self.技能等级加成('所有', 85, 85, -2)
                self.技能等级加成('所有', 100, 100, -2)
            # 黑鸦武器觉醒词条
            if self.黑鸦词条[0][0] == 3 and equ.get_equ_by_name(i).部位 == '武器':
                self.技能等级加成('所有', 50, 50, 2)
                self.技能等级加成('所有', 85, 85, 2)
                self.技能等级加成('所有', 100, 100, 2)
            # 世界树之精灵洗词条的特殊处理,没考虑择优的时候,针对的是自选
            if self.黑鸦词条[0][0] > 1 and equ.get_equ_by_name(i).名称 == '世界树之精灵':
                self.技能等级加成('所有', 50, 50, 2)

        for i in self.套装栏:
            equ.get_suit_by_name(i).城镇属性_BUFF(self)
            equ.get_suit_by_name(i).BUFF属性(self)

        if self.排行系数 == 1:
            P = deepcopy(self)
            P.站街计算()
            self.站街系数 = P.系数数值站街()

        for i in self.装备栏:
            equ.get_equ_by_name(i).进图属性_BUFF(self)

        for i in self.套装栏:
            equ.get_suit_by_name(i).进图属性_BUFF(self)

    def 专属词条计算(self):
        pass

    def 站街计算(self):
        self.专属词条计算()
        for i in self.技能栏:
            if i.站街生效 == 1:
                i.进图加成 = 0
                self.智力 += i.结算统计()[0]
                self.体力 += i.结算统计()[1]
                self.精神 += i.结算统计()[2]

    def 护石计算(self, 护石选项):
        if 护石选项 == 'BUFF力量、智力+2%':
            self.BUFF力量per *= 1.02
            self.BUFF智力per *= 1.02
        elif 护石选项 == 'BUFF力量、智力+4%':
            self.BUFF力量per *= 1.04
            self.BUFF智力per *= 1.04
        elif 护石选项 == 'BUFF力量、智力+6%':
            self.BUFF力量per *= 1.06
            self.BUFF智力per *= 1.06
        elif 护石选项 == 'BUFF力量、智力+8%':
            self.BUFF力量per *= 1.08
            self.BUFF智力per *= 1.08

    def BUFF面板(self):
        for i in self.技能栏:
            try:
                return i.BUFF面板()
            except:
                pass

    def 一觉面板(self):
        for i in self.技能栏:
            try:
                return i.一觉面板()
            except:
                pass


class 角色窗口(窗口):
    def __init__(self):
        self.护石选项 = [
            '无', 'BUFF力量、智力+2%', 'BUFF力量、智力+4%', 'BUFF力量、智力+6%', 'BUFF力量、智力+8%'
        ]
        self.store = Store()
        super().__init__()
        self.登记启用 = False
        self.store.bind(self,"希洛克选择状态","/buffer/data/siroco")
        self.store.bind(self,"奥兹玛选择状态","/buffer/data/ozma")
        self.store.bind(self,"登记启用","/buffer/data/register_enable")


    def 称号描述(self):
        temp = '<font size="3" face="宋体">'
        temp += '<font color="#78FF1E">' + self.称号.currentText(
        ) + '</font><br>'
        temp += 称号列表[self.称号.currentIndex()].装备描述_BUFF(self.角色属性B)[:-4]
        temp += '</font>'
        return temp

    def 宠物描述(self):
        temp = '<font size="3" face="宋体">'
        temp += '<font color="#78FF1E">' + self.宠物.currentText(
        ) + '</font><br>'
        temp += 宠物列表[self.宠物.currentIndex()].装备描述_BUFF(self.角色属性B)[:-4]
        temp += '</font>'
        return temp

    def 界面(self):
        self.setFixedSize(1120, 680)
        self.窗口高度 = 680
        self.行高 = 30
        self.输出背景图片 = QPixmap("./ResourceFiles/img/输出背景_BUFF.png")
        super().界面()

    def 界面1(self):
        super().界面1()

        for i in 称号列表:
            self.称号.addItem(i.名称)

        for i in 宠物列表:
            self.宠物.addItem(i.名称)

        标签 = QLabel(self.main_frame1)
        人物 = QPixmap('./ResourceFiles/' + self.角色属性A.实际名称 + "/职业.png")
        标签.setPixmap(人物)
        标签.resize(191, 523)
        标签.move(922 + int((191 - 人物.width()) / 2), 10)

        self.百变怪选项 = QCheckBox('百变怪   ', self.main_frame1)
        self.百变怪选项.move(660, 613)
        self.百变怪选项.resize(80, 24)
        self.百变怪选项.setToolTip('<font size="3" face="宋体">仅在极速模式和套装模式下生效</font>')
        self.百变怪选项.setStyleSheet(复选框样式)

        self.计算模式选择 = MyQComboBox(self.main_frame1)
        self.计算模式选择.addItems(['计算模式:极速模式', '计算模式:套装模式', '计算模式:单件模式'])
        self.计算模式选择.move(750, 613)
        self.计算模式选择.resize(235, 24)
        self.计算模式选择.setStyleSheet(下拉框样式)
        self.计算模式选择.setToolTip(
            '<font size="3" face="宋体">极速模式:533和3332(散搭) (不含智慧产物)<br><br>套装模式:533、3332(散搭)和3233(双防具) (不含智慧产物)<br><br>单件模式:所有组合 (不含百变怪)</font>'
        )

        self.切装模式选项 = QCheckBox('一觉切1件装备', self.main_frame1)
        self.切装模式选项.move(875, 580)
        self.切装模式选项.resize(105, 24)
        self.切装模式选项.setToolTip(
            '<font size="3" face="宋体">仅对极速/套装模式中的3332散搭组合生效<br><br>默认相同打造</font>'
        )
        self.切装模式选项.setStyleSheet(复选框样式)

        self.神话排名选项 = QCheckBox('神话排名模式', self.main_frame1)
        self.神话排名选项.move(990, 580)
        self.神话排名选项.resize(100, 24)
        self.神话排名选项.setToolTip(
            '<font size="3" face="宋体">仅显示有神话的组合,且每件神话装备只会出现一次</font>')
        self.神话排名选项.setStyleSheet(复选框样式)

        self.最大使用线程数 = thread_num
        self.线程数选择 = MyQComboBox(self.main_frame1)
        self.线程数选择.move(660, 580)
        self.线程数选择.resize(80, 24)
        for i in range(thread_num, 0, -1):
            self.线程数选择.addItem('进程:' + str(i))
        if thread_num > 1:
            self.线程数选择.setCurrentIndex(1)

        self.禁用存档 = QCheckBox('禁用自动存档', self.main_frame1)
        self.禁用存档.move(990, 545)
        self.禁用存档.resize(100, 24)
        self.禁用存档.setStyleSheet(复选框样式)

        重置按钮 = QPushButton('全局重置', self.main_frame1)
        重置按钮.clicked.connect(lambda state: self.全局重置())
        重置按钮.move(880, 545)
        重置按钮.resize(100, 24)
        重置按钮.setStyleSheet(按钮样式)

        self.排行参数 = MyQComboBox(self.main_frame1)
        self.排行参数.addItems(
            ['提升率排行', '面板排行', '力量排行', '智力排行', '物攻排行', '魔攻排行', '独立排行'])
        self.排行参数.move(770, 545)
        self.排行参数.resize(100, 24)

        self.存档选择 = MyQComboBox(self.main_frame1)
        self.存档选择.move(660, 545)
        self.存档选择.resize(90, 24)
        self.存档选择.currentIndexChanged.connect(lambda state: self.存档更换())

        # 一键修正按钮添加
        self.一键站街设置输入.append(QLineEdit(self.main_frame1))
        self.一键站街设置输入[0].setAlignment(Qt.AlignCenter)
        self.一键站街设置输入[0].setStyleSheet(输入框样式)
        self.一键站街设置输入[0].resize(45, 24)
        self.一键站街设置输入[0].move(750, 580)

        self.一键修正按钮 = QPushButton('一键修正', self.main_frame1)
        self.一键修正按钮.clicked.connect(lambda state: self.一键修正())
        self.一键修正按钮.move(800, 580)
        self.一键修正按钮.resize(70, 24)
        self.一键修正按钮.setStyleSheet(按钮样式)


        增幅选项 = []
        for i in range(12):
            combo =  self.装备打造选项[i+12] 
            combo.currentIndexChanged.connect(lambda :self.store.emit("/buffer/data/amplifies"))
            增幅选项.append(combo)
        self.store.compute("/buffer/data/amplifies",lambda : [i.currentIndex() for i in 增幅选项],None)

    def 界面2(self):
        # 第二个布局界面
        self.main_frame2 = QWidget()

        # 技能等级、次数输入

        self.护石第一栏 = MyQComboBox(self.main_frame2)
        self.护石第二栏 = MyQComboBox(self.main_frame2)
        self.护石第三栏 = MyQComboBox(self.main_frame2)

        self.等级调整 = []
        self.次数输入 = []

        for i in self.角色属性A.技能栏:
            self.等级调整.append(MyQComboBox(self.main_frame2))
            self.次数输入.append(MyQComboBox(self.main_frame2))

        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            if i.所在等级 == 50 or i.所在等级 == 85:
                for j in range(i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
            else:
                for j in range(-i.基础等级, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
            for j in range(2):
                self.次数输入[序号].addItem(str(j))
            if 序号 == self.一觉序号:
                self.次数输入[序号].addItem('填写')
                self.次数输入[序号].activated.connect(
                    lambda state, index=序号: self.BUFF次数输入填写(index))

        横坐标 = 30
        纵坐标 = 0
        横坐标偏移量 = 60
        纵坐标偏移量 = 30
        词条框宽度 = 48
        行高 = 20

        counter = 0
        for i in ['契约满级', '等级调整', '是否适用']:
            x = QLabel(i, self.main_frame2)
            x.move(横坐标 + 横坐标偏移量 - 30 + 50 * counter, 纵坐标 + 5)
            x.setStyleSheet(标签样式)
            counter += 1

        纵坐标 += 20

        for i in self.角色属性A.技能栏:
            x = QLabel(self.main_frame2)
            x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
            x.resize(28, 28)
            tempstr = '<font size="3" face="宋体"><font color="#FF6666">' + \
                      i.名称 + i.备注 + '</font><br>'
            tempstr += '所在等级:' + str(i.所在等级) + '<br>'
            tempstr += '等级上限:' + str(i.等级上限) + '</font>'
            x.setToolTip(tempstr)
            x.move(横坐标, 纵坐标 + 7)
            横坐标 += 40
            x = QLabel('Lv' + str(i.基础等级), self.main_frame2)
            x.resize(40, 28)
            x.move(横坐标, 纵坐标 + 7)
            x.setStyleSheet(标签样式)
            横坐标 += 40
            self.等级调整[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
            self.等级调整[self.角色属性A.技能序号[i.名称]].move(横坐标, 纵坐标 + 10)
            横坐标 -= 80
            纵坐标 += 纵坐标偏移量

        横坐标 = 横坐标 + 80 + 50
        纵坐标 = 30

        for i in self.角色属性A.技能栏:
            self.次数输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
            self.次数输入[self.角色属性A.技能序号[i.名称]].move(横坐标, 纵坐标)
            纵坐标 += 纵坐标偏移量

        self.护石第一栏.addItems(self.护石选项)
        self.护石第二栏.addItems(self.护石选项)
        self.护石第三栏.addItems(self.护石选项)
        self.护石栏 = [self.护石第一栏, self.护石第二栏, self.护石第三栏]

        横坐标 = 395
        纵坐标 = 20
        行高 = 18
        x = QLabel("护石Ⅰ:", self.main_frame2)
        x.move(横坐标, 纵坐标)
        x.setStyleSheet(标签样式)
        纵坐标 += 21
        self.护石第一栏.move(横坐标, 纵坐标)
        self.护石第一栏.resize(130, 行高)

        横坐标 = 565
        纵坐标 = 20
        x = QLabel("护石Ⅱ:", self.main_frame2)
        x.move(横坐标, 纵坐标)
        x.setStyleSheet(标签样式)
        纵坐标 += 21
        self.护石第二栏.move(横坐标, 纵坐标)
        self.护石第二栏.resize(130, 行高)

        横坐标 = 395
        纵坐标 = 70
        行高 = 18
        x = QLabel("护石Ⅲ:", self.main_frame2)
        x.move(横坐标, 纵坐标)
        x.setStyleSheet(标签样式)
        纵坐标 += 21
        self.护石第三栏.move(横坐标, 纵坐标)
        self.护石第三栏.resize(130, 行高)

        self.辟邪玉选择 = []
        self.辟邪玉数值 = []
        x = QLabel("辟邪玉选择:", self.main_frame2)
        x.move(395, 115 + 5)
        x.setStyleSheet(标签样式)
        for i in range(4):
            x = MyQComboBox(self.main_frame2)
            for j in 辟邪玉列表:
                # '[' + str(j.编号) + ']' +
                x.addItem(j.名称)
            x.resize(200, 20)
            x.move(395, 140 + i * 25)
            x.currentIndexChanged.connect(
                lambda state, index=i: self.辟邪玉数值选项更新(index))
            self.辟邪玉选择.append(x)
            y = MyQComboBox(self.main_frame2)
            y.resize(80, 20)
            y.move(615, 140 + i * 25)
            self.辟邪玉数值.append(y)

        self.复选框列表 = []
        for i in 选项设置列表:
            self.复选框列表.append(QCheckBox(i.名称, self.main_frame2))

        横坐标 = 395
        纵坐标 = 240

        x = QLabel("武器融合:", self.main_frame2)
        x.move(横坐标, 纵坐标 + 5)
        x.resize(300, 20)
        x.setStyleSheet(标签样式)

        self.希洛克武器选择 = MyQComboBox(self.main_frame2)
        self.希洛克武器选择.addItems(['武器词条:无', '自适应最高值', '自选词条数值'])
        self.希洛克武器选择.resize(120, 20)
        self.希洛克武器选择.move(横坐标 + 60, 纵坐标 + 5)
        self.希洛克武器选择.currentIndexChanged.connect(
            lambda state: self.希洛克武器选择更新())
        纵坐标 += 10
        self.武器融合属性A = MyQComboBox(self.main_frame2)
        for j in 武器属性A列表:
            self.武器融合属性A.addItem(j.固定属性描述)
        self.武器融合属性A.resize(60, 20)
        self.武器融合属性A.move(横坐标, 纵坐标 + 25)

        self.武器融合属性A1 = MyQComboBox(self.main_frame2)
        self.武器融合属性A1.resize(90 + 75, 20)
        self.武器融合属性A1.move(横坐标 + 110 - 50 + 5, 纵坐标 + 25)

        self.武器融合属性A2 = MyQComboBox(self.main_frame2)
        self.武器融合属性A2.resize(50, 20)
        self.武器融合属性A2.move(横坐标 + 205 + 20 + 10, 纵坐标 + 25)
        self.武器融合属性A.currentIndexChanged.connect(
            lambda: self.希洛克武器随机词条更新(self.武器融合属性A.currentIndex()))

        x = QLabel("择优方向", self.main_frame2)
        x.move(横坐标 + 335, 纵坐标 + 15)
        x.resize(300, 20)
        x.setStyleSheet(标签样式)

        择优方向 = MyQComboBox(self.main_frame2)
        择优方向.addItem('觉醒自适应数值')
        择优方向.addItem('续航向:觉醒0.7系数')
        择优方向.addItem('爆发向:觉醒1.0系数')
        择优方向.resize(138, 20)
        择优方向.move(横坐标 + 300, 纵坐标 + 40)
        择优方向.currentIndexChanged.connect(
            lambda: self.调整太阳系数(择优方向.currentIndex()))

        纵坐标 = 纵坐标 + 30
        self.武器融合属性B = MyQComboBox(self.main_frame2)
        for j in 武器属性B列表:
            self.武器融合属性B.addItem(j.固定属性描述)
        self.武器融合属性B.resize(60, 20)
        self.武器融合属性B.move(横坐标, 纵坐标 + 25)

        self.武器融合属性B1 = MyQComboBox(self.main_frame2)
        self.武器融合属性B1.resize(90 + 75, 20)
        self.武器融合属性B1.move(横坐标 + 110 - 50 + 5, 纵坐标 + 25)

        self.武器融合属性B2 = MyQComboBox(self.main_frame2)
        self.武器融合属性B2.resize(50, 20)
        self.武器融合属性B2.move(横坐标 + 205 + 20 + 10, 纵坐标 + 25)
        self.武器融合属性B.currentIndexChanged.connect(
            lambda: self.希洛克武器随机词条更新(self.武器融合属性B.currentIndex(), 1))

        纵坐标 = 纵坐标 + 60
        标签 = QLabel('黑鸦遴选词条', self.main_frame2)
        标签.setStyleSheet(标签样式 + 'QLabel{font-size:13px;}')
        标签.resize(410, 20)
        标签.move(横坐标, 纵坐标)
        标签.setAlignment(Qt.AlignCenter)

        名称 = ['武　　器', '戒　　指', '辅助装备', '下　　装']
        纵坐标 = 纵坐标 + 25
        self.黑鸦词条 = []
        for i in range(4):
            this_index = i
            x = QLabel(名称[i], self.main_frame2)
            x.setStyleSheet(标签样式 +
                            'QLabel{font-size:13px;};text-align: justify;')
            # x.setStyleSheet('text-align: justify')
            x.resize(55, 20)
            x.move(横坐标, 纵坐标 + i * 25)
            tem = []
            tem.append(MyQComboBox(self.main_frame2))
            if i == 0:
                tem[0].addItems(['无', '计算最高', '自选数值', '自选数值-觉醒'])
                tem[0].resize(91, 20)
                tem[0].move(横坐标 + 60, 纵坐标 + 25 * i)
                tem[0].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦词条更新(index))
            else:
                tem[0].addItems(['无', '计算最高', '自选数值'])
                tem[0].resize(91, 20)
                tem[0].move(横坐标 + 60, 纵坐标 + 25 * i)
                tem[0].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦词条更新(index))
            tem.append(MyQComboBox(self.main_frame2))
            tem[1].resize(60, 20)
            tem[1].move(横坐标 + 156, 纵坐标 + 25 * i)

            tem.append(MyQComboBox(self.main_frame2))
            tem[2].resize(90 + 75, 20)
            tem[2].move(横坐标 + 266 - 50 + 5, 纵坐标 + 25 * i)

            tem.append(MyQComboBox(self.main_frame2))
            tem[3].resize(50, 20)
            tem[3].move(横坐标 + 361 + 20 + 10, 纵坐标 + 25 * i)
            if i > 0:
                for item in 装备变换属性列表:
                    tem[1].addItem(item.固定属性描述)
                tem[1].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦随机词条更新(index, 1))
            else:
                for item in 武器变换属性列表:
                    tem[1].addItem(item.固定属性描述)
                tem[1].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦随机词条更新(index))
            self.黑鸦词条.append(tem)
            self.黑鸦词条更新(i)

        横坐标 = 740
        纵坐标 = 30
        名称 = ['奈克斯', '暗杀者', '卢克西', '守门人', '洛多斯']
        self.希洛克套装按钮 = []
        self.希洛克单件按钮 = []
        self.希洛克遮罩透明度 = []
        self.希洛克选择状态 = [0] * 15



        count = 0
        for i in 名称:
            self.希洛克套装按钮.append(QPushButton(i, self.main_frame2))
            self.希洛克套装按钮[count].setStyleSheet(按钮样式)
            self.希洛克套装按钮[count].resize(50, 22)
            self.希洛克套装按钮[count].move(横坐标, 纵坐标 + 3 + count * 40)
            self.希洛克套装按钮[count].clicked.connect(
                lambda state, index=(count + 1) * 100: self.希洛克选择(index))
            for j in range(3):
                序号 = count * 3 + j
                图片 = QLabel(self.main_frame2)
                图片.setPixmap(
                    QPixmap('./ResourceFiles/img/希洛克/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标 + 60 + j * 30, 纵坐标 + count * 40)
                self.希洛克遮罩透明度.append(QGraphicsOpacityEffect())
                self.希洛克遮罩透明度[序号].setOpacity(0.5)
                self.希洛克单件按钮.append(QPushButton(self.main_frame2))
                self.希洛克单件按钮[序号].setStyleSheet(
                    "background-color: rgb(0, 0, 0)")
                self.希洛克单件按钮[序号].resize(28, 28)
                self.希洛克单件按钮[序号].move(横坐标 + 60 + j * 30, 纵坐标 + count * 40)
                self.希洛克单件按钮[序号].setGraphicsEffect(self.希洛克遮罩透明度[序号])
                self.希洛克单件按钮[序号].clicked.connect(
                    lambda state, index=序号: self.希洛克选择(index))
            count += 1

        横坐标 = 395
        纵坐标 = 480
        名称 = ['阿斯特罗斯', '贝利亚斯', '雷德梅恩', '罗什巴赫', '泰玛特']
        self.奥兹玛套装按钮 = []
        self.奥兹玛单件按钮 = []
        self.奥兹玛遮罩透明度 = []
        self.奥兹玛选择状态 = [0] * 25

        count = 0
        for i in 名称:
            self.奥兹玛套装按钮.append(QPushButton(i, self.main_frame2))
            self.奥兹玛套装按钮[count].setStyleSheet(按钮样式)
            self.奥兹玛套装按钮[count].resize(75, 22)
            self.奥兹玛套装按钮[count].move(横坐标, 纵坐标 + 3 + count * 32)
            self.奥兹玛套装按钮[count].clicked.connect(
                lambda state, index=(count + 1) * 100: self.奥兹玛选择(index))
            for j in range(5):
                序号 = count * 5 + j
                图片 = QLabel(self.main_frame2)
                图片.setPixmap(
                    QPixmap('./ResourceFiles/img/奥兹玛/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标 + 60 + j * 30 + 20, 纵坐标 + count * 32)
                self.奥兹玛遮罩透明度.append(QGraphicsOpacityEffect())
                self.奥兹玛遮罩透明度[序号].setOpacity(0.5)
                self.奥兹玛单件按钮.append(QPushButton(self.main_frame2))
                self.奥兹玛单件按钮[序号].setStyleSheet(
                    "background-color: rgb(0, 0, 0)")
                self.奥兹玛单件按钮[序号].resize(28, 28)
                self.奥兹玛单件按钮[序号].move(横坐标 + 60 + j * 30 + 20, 纵坐标 + count * 32)
                self.奥兹玛单件按钮[序号].setGraphicsEffect(self.奥兹玛遮罩透明度[序号])
                self.奥兹玛单件按钮[序号].clicked.connect(
                    lambda state, index=序号: self.奥兹玛选择(index))
            count += 1

        counter = 0
        for i in self.复选框列表:
            i.setStyleSheet(复选框样式)
            i.resize(180, 20)
            i.move(930, 25 + counter * 28)
            if counter < 1:
                i.setChecked(True)
            counter += 1

        self.排行选项 = []
        for i in range(4):
            self.排行选项.append(MyQComboBox(self.main_frame2))
        self.排行选项[0].setEditable(True)
        for i in [
            3000, 3500, 4000, 4500, 5000, 5500, 6000, 7000, 8000, 10000,
            12000, 15000, 20000
        ]:
            self.排行选项[0].addItem('C力智:' + str(i))
        self.排行选项[0].setCurrentIndex(4)

        self.排行选项[1].setEditable(True)
        for i in [
            2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900,
            3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900,
            4000, 4200, 4400, 4600, 4800, 5000
        ]:
            self.排行选项[1].addItem('C三攻:' + str(i))
        self.排行选项[1].setCurrentIndex(10)

        for i in ['物理百分比', '魔法百分比', '物理固伤', '魔法固伤']:
            self.排行选项[2].addItem(i)

        for i in ['无系统奶', '希洛克系统奶', '黑鸦系统奶']:
            self.排行选项[3].addItem(i)

        counter = 0
        for i in self.排行选项:
            i.resize(100, 20)
            i.move(990, 490 + counter * 28)
            counter += 1

        self.计算按钮2 = QPushButton('开始计算', self.main_frame2)
        self.计算按钮2.clicked.connect(lambda state: self.计算())
        self.计算按钮2.move(990, 610)
        self.计算按钮2.resize(100, 30)
        self.计算按钮2.setStyleSheet(按钮样式)

        if self.初始属性.三觉序号 != 0:
            self.觉醒选择状态 = 2
            self.一觉遮罩透明度 = QGraphicsOpacityEffect()
            self.一觉遮罩透明度.setOpacity(0.5)
            self.二觉遮罩透明度 = QGraphicsOpacityEffect()
            self.二觉遮罩透明度.setOpacity(0.0)
            x = 250
            y = 230
            self.觉醒选择 = QLabel(self.main_frame2)
            self.觉醒选择.setPixmap(QPixmap('./ResourceFiles/img/觉醒选择.png'))
            self.觉醒选择.resize(120, 100)
            self.觉醒选择.move(x, y - 20)
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
            self.一觉遮罩.setStyleSheet(
                "QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}"
            )
            self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
            self.一觉遮罩.clicked.connect(
                lambda state, index=1: self.强化觉醒选择(index))
            self.二觉遮罩 = QPushButton(self.main_frame2)
            self.二觉遮罩.resize(38, 50)
            self.二觉遮罩.move(x + 47, y + 5)
            self.二觉遮罩.setStyleSheet(
                "QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}"
            )
            self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)
            self.二觉遮罩.clicked.connect(
                lambda state, index=2: self.强化觉醒选择(index))
        self.武器融合属性A.setEnabled(False)
        self.武器融合属性A1.setEnabled(False)
        self.武器融合属性A2.setEnabled(False)
        self.武器融合属性A.setStyleSheet(下拉框样式)
        self.武器融合属性A1.setStyleSheet(下拉框样式)
        self.武器融合属性A2.setStyleSheet(下拉框样式)
        # 武器融合属性B禁用
        self.武器融合属性B.setEnabled(False)
        self.武器融合属性B1.setEnabled(False)
        self.武器融合属性B2.setEnabled(False)
        self.武器融合属性B.setStyleSheet(下拉框样式)
        self.武器融合属性B1.setStyleSheet(下拉框样式)
        self.武器融合属性B2.setStyleSheet(下拉框样式)

    def 界面3(self):
        # 第三个布局界面
        self.main_frame3 = QWidget()

        self.属性设置输入 = []
        self.技能设置输入 = []

        宽度 = 43

        列名称1 = ["智力", "体力", "精神"]
        行名称1 = [
            "工会属性", "训练官BUFF", "戒指", "婚房", "冒险团", "晶体契约", "收集箱", "勋章", "名称装饰卡",
            "快捷栏纹章", "宠物装备-红", "  宠物装备-蓝  ", "  宠物装备-绿  ", "宠物附魔", "皮肤",
            "站街修正", "进图修正"
        ]
        名称 = QLabel("基础细节", self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(标签样式)
        名称.resize(80, 25)
        名称.move(10, 5)

        for i in range(3):
            名称 = QLabel(列名称1[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(宽度, 25)
            名称.move(95 + i * (宽度 + 5), 5)

        for j in range(17):
            名称 = QLabel(行名称1[j], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(80, 25)
            名称.move(10, 35 + j * 30)

        for i in range(3):
            Linelist = []
            for j in range(19):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet(输入框样式)
                if j < 17:
                    Linelist[j].resize(宽度, 22)
                    Linelist[j].move(95 + i * (宽度 + 5), 35 + j * 30)
                else:
                    Linelist[j].resize(0, 0)
            self.属性设置输入.append(Linelist)

        列名称2 = ["智力", "体力", "精神", "徽章智", "徽章体", "徽章精", "技能等级及选项"]
        行名称2 = [
            "上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "左槽", "右槽", "耳环",
            "武器", "BUFF等级补正", "穿戴称号", "穿戴光环", "武器装扮", "时装", "宠物登记补正", "光环登记补正"
        ]

        self.列名称 = 列名称1 + 列名称2
        self.行名称 = 行名称1 + 行名称2

        名称 = QLabel(" 附魔&徽章 ", self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(标签样式)
        名称.resize(80, 25)
        名称.move(7 * 宽度, 5)
        for i in range(7):
            名称 = QLabel(列名称2[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            if i == 6:
                名称.resize(150, 25)
            else:
                名称.resize(宽度, 25)
            名称.move(90 + 7 * 宽度 + i * (宽度 + 5), 5)

        for j in range(19):
            名称 = QLabel(行名称2[j], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(80, 25)
            名称.move(7 * 宽度, 35 + j * 30)

        for i in range(6):
            Linelist = []
            for j in range(19):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet(输入框样式)
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(90 + 7 * 宽度 + i * (宽度 + 5), 35 + j * 30)
            self.属性设置输入.append(Linelist)

        for j in range(19):
            self.技能设置输入.append(MyQComboBox(self.main_frame3))
            self.技能设置输入[j].addItem('无')
            self.技能设置输入[j].setStyleSheet(下拉框样式)
            self.技能设置输入[j].resize(150, 22)
            self.技能设置输入[j].move(90 + 7 * 宽度 + 6 * (宽度 + 5), 35 + j * 30)

        for j in [2, 3, 4]:
            self.技能设置输入[j].addItems(['Lv1-30(主动)Lv+1', 'Lv1-50(主动)Lv+1'])
        self.技能设置输入[2].addItems(['Lv1-35(主动)Lv+1', 'Lv30-50(主动)Lv+1'])
        self.技能设置输入[3].addItem('Lv30-50(主动)Lv+1')

        for j in [8, 9, 16]:
            for i in self.角色属性A.技能栏:
                self.技能设置输入[j].addItem(i.名称 + 'Lv+1')
        self.技能设置输入[12].addItems(
            ['BUFFLv+1', 'BUFFLv+2', 'BUFFLv+3', 'BUFFLv+4'])
        self.技能设置输入[13].addItems(['Lv1-50(主动)Lv+1', '一觉Lv+1', '一觉Lv+2'])
        self.技能设置输入[14].addItems([
            'Lv1-30(所有)Lv+1', 'Lv1-50(所有)Lv+1', 'Lv1-20(所有)Lv+1',
            'Lv20-30(所有)Lv+1', 'Lv1-80(所有)Lv+1'
        ])

        self.技能设置输入[17].addItems(['BUFF力智+3%', 'BUFF三攻+3%', 'BUFF力智、三攻+3%'])
        self.技能设置输入[18].addItems(['BUFF力智+3%'])

        if '智力' in self.角色属性A.类型选择:
            self.修正列表名称 = [
                '转职被动智力', 'BUFF力智%', 'BUFF三攻%', '转职被动等级', '一觉被动力智', '一觉力智%',
                '一觉力智'
            ]
        else:
            self.修正列表名称 = [
                '守护恩赐体精', 'BUFF力智%', 'BUFF三攻%', '守护恩赐等级', '信念光环体精', '一觉力智%',
                '一觉力智'
            ]

        Linelist = []
        for i in range(len(self.修正列表名称)):
            名称 = QLabel(self.修正列表名称[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(90, 25)
            名称.move(170 + 7 * 宽度 + 9 * (宽度 + 5), 35 + i * 30)
            Linelist.append(QLineEdit(self.main_frame3))
            Linelist[i].setAlignment(Qt.AlignCenter)
            Linelist[i].setStyleSheet(输入框样式)
            Linelist[i].resize(60, 25)
            Linelist[i].move(270 + 7 * 宽度 + 9 * (宽度 + 5), 35 + i * 30)
        self.属性设置输入.append(Linelist)

        count = 0
        self.时装选项 = []
        for i in ['头部', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']:
            名称 = QLabel(i, self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(90, 25)
            名称.move(170 + 7 * 宽度 + 9 * (宽度 + 5), 255 + count * 30)
            self.时装选项.append(MyQComboBox(self.main_frame3))
            self.时装选项[count].addItems(['高级', '节日', '稀有', '神器'])
            self.时装选项[count].resize(60, 22)
            self.时装选项[count].move(270 + 7 * 宽度 + 9 * (宽度 + 5),
                                  255 + count * 30)
            self.时装选项[count].currentIndexChanged.connect(
                lambda state, index=count: self.时装选项更新(index))
            count += 1

        self.时装选项.append(MyQComboBox(self.main_frame3))
        self.时装选项[8].addItems(['高级套装[8]', '节日套装[8]', '稀有套装[8]', '神器套装[8]'])
        self.时装选项[8].resize(160, 22)
        self.时装选项[8].move(170 + 7 * 宽度 + 9 * (宽度 + 5), 260 + count * 30)
        self.时装选项[8].currentIndexChanged.connect(
            lambda state, index=8: self.时装选项更新(index))

        self.计算按钮3 = QPushButton('开始计算', self.main_frame3)
        self.计算按钮3.clicked.connect(lambda state: self.计算())
        self.计算按钮3.move(990, 610)
        self.计算按钮3.resize(100, 30)
        self.计算按钮3.setStyleSheet(按钮样式)

    def 界面5(self):
        # 第五个布局
        self.main_frame5 = QWidget()
        标签 = QLabel('单件选择', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(240, 25)
        标签.move(70, 20)

        标签 = QLabel('锁定', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(70, 25)
        标签.move(10, 20)

        self.图片显示 = []

        count = 0
        
        
        self.装备锁定 = []
        self.自选装备 = []
        self.self_selects = []

        def equips_getter():
            return [i.currentText() for i in self.自选装备]

        def equips_setter(value):
            self.self_selects = value

        self.store.compute("/buffer/data/equips",equips_getter, equips_setter)

        for i in 部位列表:
            锁定选择 = QCheckBox(i, self.main_frame5)
            锁定选择.setStyleSheet(复选框样式)
            锁定选择.resize(70, 22)
            锁定选择.move(10, 50 + 30 * count)
            self.装备锁定.append(锁定选择)
            
            combo = MyQComboBox(self.main_frame5)
            combo.resize(220, 22)
            combo.move(90, 50 + 30 * count)

            self.自选装备.append(combo)
            combo.currentIndexChanged.connect(lambda _: self.store.emit("/buffer/data/equips"))
            combo.currentIndexChanged.connect(lambda index,part=count: self.自选装备更改(part))
            for j in equ.get_equ_list():
                if j.部位 == i:
                    if i == '武器':
                        if j.类型 in self.角色属性A.武器选项:
                            combo.addItem(j.名称)
                    else:
                        combo.addItem(j.名称)
            count += 1

        self.计算标识 = 1
        标签 = QLabel('批量选择', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(160, 25)
        标签.move(330, 20)

        套装类型 = ['防具', '首饰', '特殊', '上链左', '镯下右', '环鞋指']
        count = 0
        self.自选套装 = []
        for i in 套装类型:
            self.自选套装.append(MyQComboBox(self.main_frame5))
            套装名称 = []
            for j in equ.get_suit_list():
                if j.名称 not in 套装名称 and j.类型 == i:
                    套装名称.append(j.名称)
            self.自选套装[count].addItems(套装名称)
            self.自选套装[count].resize(160, 22)
            self.自选套装[count].move(330, 50 + 30 * count)
            self.自选套装[count].activated.connect(
                lambda state, index=count: self.自选套装更改(index))
            count += 1

        self.神话部位选项 = MyQComboBox(self.main_frame5)
        self.神话部位选项.addItems(['神话部位:无', '神话部位:上衣', '神话部位:手镯', '神话部位:耳环'])
        self.神话部位选项.resize(160, 22)
        self.神话部位选项.move(330, 50 + 30 * count)
        self.神话部位选项.activated.connect(lambda state: self.神话部位更改())

        count += 1
        # 一键修正按钮添加
        self.一键站街设置输入.append(QLineEdit(self.main_frame5))
        self.一键站街设置输入[1].setAlignment(Qt.AlignCenter)
        self.一键站街设置输入[1].setStyleSheet(输入框样式)
        self.一键站街设置输入[1].resize(45, 24)
        self.一键站街设置输入[1].move(330, 80 + 30 * count)

        self.一键修正按钮 = QPushButton('一键修正', self.main_frame5)
        self.一键修正按钮.clicked.connect(lambda state: self.一键修正(1))
        self.一键修正按钮.move(330 + 60, 80 + 30 * count)
        self.一键修正按钮.resize(80, 24)
        self.一键修正按钮.setStyleSheet(按钮样式)

        标签 = QLabel('辟邪玉提升率(理论值仅供参考)', self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(200, 25)
        标签.move(525, 20)

        self.辟邪玉提升率1 = []
        self.辟邪玉提升率2 = []
        count = 0
        for i in 辟邪玉列表:
            if i.名称 != '无':
                if i.间隔 < 1:
                    temp = i.名称 + '+' + str(i.最大值) + '%'
                else:
                    temp = i.名称 + '+' + str(i.最大值)
                self.辟邪玉提升率1.append(QLabel(temp, self.main_frame5))
                self.辟邪玉提升率1[count].setAlignment(Qt.AlignCenter)
                self.辟邪玉提升率1[count].setStyleSheet(标签样式)
                self.辟邪玉提升率1[count].resize(180, 25)
                self.辟邪玉提升率1[count].move(500, 50 + 30 * count)
                self.辟邪玉提升率2.append(QLabel('0.00%', self.main_frame5))
                self.辟邪玉提升率2[count].setAlignment(Qt.AlignCenter)
                self.辟邪玉提升率2[count].setStyleSheet(标签样式)
                self.辟邪玉提升率2[count].resize(60, 25)
                self.辟邪玉提升率2[count].move(690, 50 + 30 * count)
                count += 1

        初始x = 805
        初始y = 20
        图片显示 = QLabel(self.main_frame5)
        图片显示.setPixmap(self.输出背景图片)
        图片显示.setAlignment(Qt.AlignTop)
        图片显示.resize(268, 546)
        图片显示.move(初始x, 初始y + 11)
        人物 = QLabel(self.main_frame5)
        图片 = QPixmap('./ResourceFiles/' + self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(初始x + 90 + int(45 - 图片.width() / 2), 初始y + 40)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)

        self.提升率显示 = QLabel(self.main_frame5)
        self.提升率显示.setStyleSheet(
            "QLabel{color:rgb(255,255,255);font-size:25px}")
        self.提升率显示.resize(250, 36)
        self.提升率显示.move(初始x + 10, 初始y + 517)
        self.提升率显示.setAlignment(Qt.AlignCenter)

        偏移量 = 187
        x坐标 = [
            32, 0, 0, 32, 0, 偏移量, 偏移量 + 32, 偏移量 + 32, 偏移量, 偏移量, 偏移量 + 32, 32
        ]
        y坐标 = [0, 0, 32, 32, 64, 0, 0, 32, 64, 32, 64, 64]

        for i in range(12):
            self.图片显示.append(QLabel(self.main_frame5))
            self.图片显示[i].setMovie(equ.get_img_by_name(self.self_selects[i]))
            self.图片显示[i].resize(26, 26)
            self.图片显示[i].move(初始x + 10 + x坐标[i], 初始y + 31 + y坐标[i])
            self.图片显示[i].setAlignment(Qt.AlignCenter)

        self.面板显示 = []
        for i in range(11):
            self.面板显示.append(QLabel(self.main_frame5))
        const = 139
        self.面板显示[0].move(初始x, 初始y + const)
        self.面板显示[1].move(初始x + 135, 初始y + const)

        const += 36
        count = 0
        for i in [2, 3, 4, 5, 6, 7]:
            self.面板显示[i].move(初始x, 初始y + const + count * 18)
            count += 1

        count = 0
        for i in [8, 9, 10]:
            self.面板显示[i].move(初始x + 135, 初始y + const + count * 18)
            count += 1

        for i in range(len(self.面板显示)):
            if i != 1:
                self.面板显示[i].setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(255,255,255)}")
            else:
                self.面板显示[i].setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(150,255,30)}")
            self.面板显示[i].resize(100, 18)
            self.面板显示[i].setAlignment(Qt.AlignRight)

        self.词条显示 = []
        for i in range(12):
            self.词条显示.append(QLabel(self.main_frame5))

        j = 315 + 初始y
        for i in self.词条显示:
            i.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            i.move(8 + 初始x, j)
            i.resize(300, 18)
            i.setAlignment(Qt.AlignLeft)
            j += 18

        # self.总伤害 = QLabel(self.main_frame5)
        # self.总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        # self.总伤害.resize(600, 36)
        # self.总伤害.move(200, 517 + 初始y)
        # self.总伤害.setAlignment(Qt.AlignCenter)

        self.套装名称显示 = []
        for i in range(9):
            self.套装名称显示.append(QLabel(self.main_frame5))
            self.套装名称显示[i].move(132 + 初始x, 138 + 180 + 20 * i + 初始y)
            self.套装名称显示[i].resize(132, 18)
            self.套装名称显示[i].setAlignment(Qt.AlignCenter)

        自选计算按钮 = QPushButton('查看详情', self.main_frame5)
        自选计算按钮.clicked.connect(lambda state: self.自选计算())
        自选计算按钮.move(995, 610)
        自选计算按钮.resize(80, 28)
        自选计算按钮.setStyleSheet(按钮样式)

        self.基准值 = []

        设置基准值 = QPushButton('设为基准', self.main_frame5)
        设置基准值.clicked.connect(lambda state: self.基准值设置())
        设置基准值.move(900, 610)
        设置基准值.resize(80, 28)
        设置基准值.setStyleSheet(按钮样式)

        清空基准值 = QPushButton('清空基准', self.main_frame5)
        清空基准值.clicked.connect(lambda state: self.基准值设置(1))
        清空基准值.move(805, 610)
        清空基准值.resize(80, 28)
        清空基准值.setStyleSheet(按钮样式)


        换装选项 = QCheckBox('启用登记',self.main_frame5)

        换装选项.toggled.connect(lambda checked :self.启用换装登记(checked))
        换装选项.move(320, 340)
        换装选项.resize(70, 28)
        换装选项.setStyleSheet(复选框样式)

        换装设置 = QPushButton('登记设置', self.main_frame5)
        换装设置.clicked.connect(lambda _: self.换装设置())
        换装设置.move(390, 340)
        换装设置.resize(80, 28)
        换装设置.setStyleSheet(按钮样式)
        
    def 启用换装登记(self,checked):
        self.登记启用 = checked        
        self.更新换装()

    def 换装设置(self):             
        def createClient():
            self.store.compute("/buffer/temp/property_a",lambda : self.角色属性A)
            # 换装更新事件
            self.store.watch("/buffer/event/register_changed",lambda _,: self.更新换装())
            # 设置图标和背景 临时做法
            self.store.const("/app/window/icon",self.icon)
            self.store.const("/app/window/background_image",self.主背景图片)
            client = 换装窗口()
            client.初始化(self.store)
            return client
        DefaultDialogRegister.showDialog("buff_panel", createClient,self)

    def 更新换装(self):
        self.自选换装装备 = self.store.get("/buffer/data/register/equips")
        self.自选换装打造 =self.store.get("/buffer/data/register/amplifies")
        self.换装奥兹玛 = self.store.get("/buffer/data/register/ozma")
        self.换装希洛克 = self.store.get("/buffer/data/register/siroco")
        self.换装遴选 = self.store.get("/buffer/data/register/black_purgatory")
        self.自选计算(1)

    def 时装选项更新(self, index):
        if index == 8:
            count = 0
            for i in self.时装选项:
                if count != 8:
                    i.setCurrentIndex(self.时装选项[8].currentIndex())
                count += 1
            return
        else:
            智力, 体力, 精神 = 0, 0, 0
            套装字典 = {'高级': 0, '节日': 0, '稀有': 0, '神器': 0}
            for i in range(8):
                套装字典[self.时装选项[i].currentText()] = 套装字典.get(
                    self.时装选项[i].currentText(), 0) + 1
            # 套装属性
            神器 = 套装字典['神器']
            稀有 = 套装字典['稀有'] + 神器
            if 套装字典['高级'] >= 3:
                智力 += 10
                体力 += 10
                精神 += 10
            if 稀有 >= 3 and 神器 < 3:
                智力 += 40
                体力 += 40
                精神 += 40
            if 套装字典['神器'] >= 3:
                智力 += 50
                体力 += 50
                精神 += 50
            if 套装字典['高级'] >= 8:
                智力 += 10
                体力 += 10
                精神 += 10
            if 套装字典['节日'] >= 8:
                智力 += 25
                体力 += 25
                精神 += 25
            if 稀有 >= 8 and 神器 < 8:
                智力 += 40
                体力 += 40
                精神 += 40
            if 套装字典['神器'] >= 8:
                智力 += 50
                体力 += 50
                精神 += 50
            数据 = [45, 45, 55, 65]
            智力 += 数据[self.时装选项[0].currentIndex()]  # 头部
            精神 += 数据[self.时装选项[0].currentIndex()]  # 头部
            智力 += 数据[self.时装选项[1].currentIndex()]  # 帽子
            精神 += 数据[self.时装选项[1].currentIndex()]  # 帽子
            数据 = [0, 0, 55, 65]
            体力 += 数据[self.时装选项[5].currentIndex()]  # 腰带
            数据 = [45, 45, 55, 65]
            体力 += 数据[self.时装选项[7].currentIndex()]  # 鞋子

            数据 = [0, 20, 0, 0]
            智力 += 数据[self.时装选项[6].currentIndex()]  # 下装
            体力 += 数据[self.时装选项[6].currentIndex()]  # 下装
            精神 += 数据[self.时装选项[6].currentIndex()]  # 下装

            self.属性设置输入[3][16].setText(str(智力))
            self.属性设置输入[4][16].setText(str(体力))
            self.属性设置输入[5][16].setText(str(精神))

    def 希洛克武器选择更新(self):
        if self.希洛克武器选择.currentIndex() != 2:
            # 武器融合属性A禁用
            self.武器融合属性A.setEnabled(False)
            self.武器融合属性A1.setEnabled(False)
            self.武器融合属性A2.setEnabled(False)
            self.武器融合属性A.setStyleSheet(下拉框样式)
            self.武器融合属性A1.setStyleSheet(下拉框样式)
            self.武器融合属性A2.setStyleSheet(下拉框样式)
            # 武器融合属性B禁用
            self.武器融合属性B.setEnabled(False)
            self.武器融合属性B1.setEnabled(False)
            self.武器融合属性B2.setEnabled(False)
            self.武器融合属性B.setStyleSheet(下拉框样式)
            self.武器融合属性B1.setStyleSheet(下拉框样式)
            self.武器融合属性B2.setStyleSheet(下拉框样式)
        else:
            # 武器融合属性A启用
            self.武器融合属性A.setEnabled(True)
            self.武器融合属性A1.setEnabled(True)
            self.武器融合属性A2.setEnabled(True)
            self.武器融合属性A.setStyleSheet(下拉框样式)
            self.武器融合属性A1.setStyleSheet(下拉框样式)
            self.武器融合属性A2.setStyleSheet(下拉框样式)
            # 武器融合属性B启用
            self.武器融合属性B.setEnabled(True)
            self.武器融合属性B1.setEnabled(True)
            self.武器融合属性B2.setEnabled(True)
            self.武器融合属性B.setStyleSheet(下拉框样式)
            self.武器融合属性B1.setStyleSheet(下拉框样式)
            self.武器融合属性B2.setStyleSheet(下拉框样式)

    def 调整太阳系数(self, index):
        if index > 0:
            self.次数输入[self.一觉序号].setEditable(True)
            self.次数输入[self.一觉序号].setCurrentIndex(2)
            self.次数输入[self.一觉序号].setCurrentText('0.7' if index == 1 else '1')
            self.次数输入[self.一觉序号].setStyleSheet(下拉框样式)
        else:
            self.次数输入[self.一觉序号].setEditable(False)
            self.次数输入[self.一觉序号].setCurrentIndex(1)
            self.次数输入[self.一觉序号].setStyleSheet(下拉框样式)

    def 希洛克武器随机词条更新(self, index, x=0):
        if x == 0:
            self.武器融合属性A1.clear()
            self.武器融合属性A2.clear()
            属性A = 武器属性A列表[index]
            temp = 属性A.最大值
            while temp >= 属性A.最小值:
                if 属性A.间隔 / 10 >= 1:
                    self.武器融合属性A2.addItem(str(int(temp)))
                else:
                    self.武器融合属性A2.addItem(str(temp) + '%')
                temp -= 属性A.间隔
            self.武器融合属性A1.addItem(属性A.随机属性描述)

        elif x == 1:
            self.武器融合属性B1.clear()
            self.武器融合属性B2.clear()
            属性B = 武器属性B列表[index]
            temp = 属性B.最大值
            while temp >= 属性B.最小值:
                if 属性B.间隔 / 10 >= 1:
                    self.武器融合属性B2.addItem(str(int(temp)))
                else:
                    self.武器融合属性B2.addItem(str(temp) + '%')
                temp -= 属性B.间隔
            self.武器融合属性B1.addItem(属性B.随机属性描述)

    def 黑鸦词条更新(self, index):
        if self.黑鸦词条[index][0].currentIndex() < 2:
            for i in range(1, 4):
                self.黑鸦词条[index][i].setEnabled(False)
                self.黑鸦词条[index][i].setStyleSheet(下拉框样式)
        elif index == 0 and self.黑鸦词条[index][0].currentIndex() == 3:
            for i in range(1, 4):
                self.黑鸦词条[0][i].setEnabled(False)
                self.黑鸦词条[0][i].setStyleSheet(下拉框样式)
        else:
            for i in range(1, 4):
                self.黑鸦词条[index][i].setEnabled(True)
                self.黑鸦词条[index][i].setStyleSheet(下拉框样式)

    def 黑鸦随机词条更新(self, i, x=0):
        index = self.黑鸦词条[i][1].currentIndex()
        self.黑鸦词条[i][2].clear()
        self.黑鸦词条[i][3].clear()
        if x == 0:
            武器属性 = 武器变换属性列表[index]
            temp = 武器属性.最大值
            while temp >= 武器属性.最小值:
                if 武器属性.间隔 / 10 >= 1:
                    self.黑鸦词条[i][3].addItem(str(int(temp)))
                else:
                    self.黑鸦词条[i][3].addItem(str(temp) + '%')
                temp -= 武器属性.间隔
            self.黑鸦词条[i][2].addItem(武器属性.随机属性描述)

        elif x == 1:
            装备属性 = 装备变换属性列表[index]
            temp = 装备属性.最大值
            while temp >= 装备属性.最小值:
                if 装备属性.间隔 / 10 >= 1:
                    self.黑鸦词条[i][3].addItem(str(int(temp)))
                else:
                    self.黑鸦词条[i][3].addItem(str(temp) + '%')
                temp -= 装备属性.间隔
            self.黑鸦词条[i][2].addItem(装备属性.随机属性描述)

    def BUFF次数输入填写(self, x):
        if self.次数输入[x].currentIndex() == 2:
            self.次数输入[x].setEditable(True)
            self.次数输入[x].clearEditText()
            self.次数输入[x].setStyleSheet(下拉框样式)
        elif self.次数输入[x].currentIndex() == 2:
            temp = self.次数输入[x].currentText()
            self.次数输入[x].removeItem(3)
            self.次数输入[x].setCurrentIndex(2)
            self.次数输入[x].setEditable(True)
            self.次数输入[x].clearEditText()
            self.次数输入[x].setStyleSheet(下拉框样式)
            self.次数输入[x].setCurrentText(temp)
        else:
            self.次数输入[x].setEditable(False)

    def 批量选择(self, index):
        if index == 1:
            if self.全选状态 == 1:
                self.全选状态 = 0
            else:
                self.全选状态 = 1
            if sum(self.装备选择状态[74:244]) == 170:
                self.批量选择(0)

        for i in equ.get_equ_list():
            if i.部位 != '武器':
                if i.品质 != '神话' or index == 0 or self.全选状态 == 0:
                    self.装备图标点击事件(equ.get_id_by_name(i.名称), index, x=0)
            else:
                if i.类型 in self.角色属性A.武器选项:
                    self.装备图标点击事件(equ.get_id_by_name(i.名称), index, x=0)

        self.装备图标点击事件(74, index)

    def 载入配置(self, path='set'):
        filepath = './ResourceFiles/{}/{}/'.format(self.角色属性A.实际名称, path)
        if os.path.exists(os.path.join(filepath,"page_1.json")) or os.path.exists(os.path.join(filepath,"store.json")):
            self.载入json(path)
            return
        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/equ3.ini',
                           'r',
                           encoding='utf-8').readlines()
            self.称号.setCurrentIndex(int(setfile[0].replace('\n', '')))
            self.宠物.setCurrentIndex(int(setfile[1].replace('\n', '')))
            self.计算模式选择.setCurrentIndex(int(setfile[2].replace('\n', '')))
            # 百变怪 && 神话排名 && 一觉切装备 && 时装选项
            if int(setfile[3].replace('\n', '')):
                self.百变怪选项.setChecked(True)
            if int(setfile[4].replace('\n', '')):
                self.神话排名选项.setChecked(True)
            if int(setfile[5].replace('\n', '')):
                self.切装模式选项.setChecked(True)
            for i in range(len(self.时装选项)):
                self.时装选项[i].setCurrentIndex(
                    int(setfile[i + 6].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/attr.ini',
                           'r',
                           encoding='utf-8').readlines()
            for i in range(10):
                for j in range(len(self.属性设置输入[i])):
                    self.属性设置输入[i][j].setText(setfile[i].replace(
                        '\n', '').split(',')[j])

            for j in range(19):
                self.技能设置输入[j].setCurrentIndex(
                    int(setfile[10].replace('\n', '').split(',')[j]))
        except:
            pass

        try:
            self.批量选择(0)  # 先清空
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/equ.ini',
                           'r',
                           encoding='utf-8').readlines()
            for i in equ.get_equ_id_list():
                if setfile[i].replace('\n', '') == '1':
                    self.装备图标点击事件(i, 1)
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/equ1.ini',
                           'r',
                           encoding='utf-8').readlines()
            for i in range(len(self.装备打造选项)):
                self.装备打造选项[i].setCurrentIndex(
                    int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/equ2.ini',
                           'r',
                           encoding='utf-8').readlines()
            for i in range(len(self.装备条件选择)):
                self.装备条件选择[i].setCurrentIndex(
                    int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/skill1.ini',
                           'r',
                           encoding='utf-8').readlines()
            num = 0
            self.护石第一栏.setCurrentIndex(int(setfile[num].replace('\n', '')))
            num += 1
            self.护石第二栏.setCurrentIndex(int(setfile[num].replace('\n', '')))
            num += 1
            self.护石第三栏.setCurrentIndex(int(setfile[num].replace('\n', '')))
            num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/skill2.ini',
                           'r',
                           encoding='utf-8').readlines()
            num = 0
            for i in self.角色属性A.技能栏:
                序号 = self.角色属性A.技能序号[i.名称]
                self.等级调整[序号].setCurrentIndex(
                    int(setfile[num].replace('\n', '')))
                num += 1
                temp1 = (int(setfile[num].replace('\n', '')))
                if temp1 < 2:
                    self.次数输入[序号].setCurrentIndex(
                        int(setfile[num].replace('\n', '')))
                elif temp1 == 2:
                    self.次数输入[序号].setCurrentIndex(2)
                    self.次数输入[序号].setEditable(True)
                    self.次数输入[序号].clearEditText()
                    self.次数输入[序号].setStyleSheet(下拉框样式)
                num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/skill3.ini',
                           'r',
                           encoding='utf-8').readlines()
            num = 0
            for i in range(4):
                self.辟邪玉选择[i].setCurrentIndex(
                    int(setfile[num].replace('\n', '')))
                num += 1
                self.辟邪玉数值[i].setCurrentIndex(
                    int(setfile[num].replace('\n', '')))
                num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/skill4.ini',
                           'r',
                           encoding='utf-8').readlines()
            num = 0
            self.武器融合属性A.setCurrentIndex(int(setfile[num].replace('\n', '')))
            num += 1
            self.武器融合属性A2.setCurrentIndex(int(setfile[num].replace('\n', '')))
            num += 1
            self.武器融合属性B.setCurrentIndex(int(setfile[num].replace('\n', '')))
            num += 1
            self.武器融合属性B2.setCurrentIndex(int(setfile[num].replace('\n', '')))
            num += 1
            self.希洛克武器选择.setCurrentIndex(int(setfile[num].replace('\n', '')))
            num += 1
            self.希洛克选择(0, 1)
            for i in range(15):
                if setfile[num].replace('\n', '') == '1':
                    self.希洛克选择(i)
                num += 1
            for i in range(4):
                self.黑鸦词条[i][0].setCurrentIndex(
                    int(setfile[num].replace('\n', '')))
                num += 1
                self.黑鸦词条[i][1].setCurrentIndex(
                    int(setfile[num].replace('\n', '')))
                num += 1
                self.黑鸦词条[i][2].setCurrentIndex(
                    int(setfile[num].replace('\n', '')))
                num += 1
                self.黑鸦词条[i][3].setCurrentIndex(
                    int(setfile[num].replace('\n', '')))
                num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/skill6.ini',
                           'r',
                           encoding='utf-8').readlines()
            num = 0
            for i in self.角色属性A.技能栏:
                序号 = self.角色属性A.技能序号[i.名称]
                if 序号 == self.一觉序号 or 序号 == self.三觉序号:
                    if self.次数输入[序号].currentIndex() == 2:
                        self.次数输入[序号].setCurrentText(
                            (setfile[num].replace('\n', '')))
                        num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path +
                           '/equ4.ini',
                           'r',
                           encoding='utf-8').readlines()
            num = 0
            for i in range(4 * 35):
                self.神话属性选项[i].setCurrentIndex(
                    int(setfile[num].replace('\n', '')))
                num += 1
        except:
            pass



    def 设置技能选项(self, 序号, info):
        try:
            self.等级调整[序号].setCurrentIndex(info['等级'])
        except:
            pass

        try:
            if type(info['次数']) == type('str'):
                self.次数输入[序号].setCurrentIndex(2)
                self.次数输入[序号].setEditable(True)
                self.次数输入[序号].clearEditText()
                self.次数输入[序号].setCurrentText(info['次数'])
                self.次数输入[序号].setStyleSheet(下拉框样式)
            else:
                self.次数输入[序号].setCurrentIndex(info['次数'])
        except:
            pass

    def 获取技能选项(self, 序号):
        info = {}
        try:
            info['等级'] = self.等级调整[序号].currentIndex()
        except:
            info['等级'] = 0

        try:
            info['次数'] = self.次数输入[序号].currentIndex()
        except:
            info['次数'] = 0
        if info['次数'] == 2 and self.次数输入[序号].currentText() != '':
            try:
                info['次数'] = str(
                    round(max(0, float(self.次数输入[序号].currentText())), 3))
            except:
                info['次数'] = 0
        return info

    def 载入旧版json(self,path = 'set',page= [0,1,2,3,4]):
        filepath = './ResourceFiles/{}/{}'.format(self.角色属性A.实际名称,path)

        if 0 in page:
            # 第一页(装备/选择/打造)
            try:
                filename = 'page_1.json'
                set_data = {}
                with open(os.path.join(filepath, filename), encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                self.store.set("/buffer/data/title",set_data['称号'])
                self.store.set("/buffer/data/pet",set_data['宠物'])
                self.store.set('/buffer/data/compute_mode',set_data["计算模式"])
                self.store.set('/buffer/data/ditto_checked',set_data["百变怪"])
                self.store.set('/buffer/data/myth_top_checked',set_data['神话排名勾选'])
                self.store.set('/buffer/data/awakening_switch_checked',set_data['切装模式选项'])
                self.store.set('/buffer/data/thread_count',set_data['线程数量'])
                self.store.set("/buffer/data/equip_checked",set_data['装备勾选'])
                self.store.set("/buffer/data/equip_forges",set_data['装备打造'])
            except Exception as error:
                logger.error(error)

        if 1 in page:
            # 第二页(技能/符文/药剂)
            try:
                filename = 'page_2.json'
                set_data = {}
                with open(os.path.join(filepath, filename), encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                self.store.set("/buffer/data/awakening_binding",set_data['觉醒选择'])
                self.store.set("/buffer/data/talismans",set_data['护石栏'])
                self.store.set("/buffer/data/consumables",set_data['药剂勾选'])
                self.store.set("/buffer/data/skill",set_data['技能选项'])
                self.store.set("/buffer/data/weapon_fusion",[set_data['武器融合属性A'],set_data['武器融合属性A2'],set_data['武器融合属性B'],set_data['武器融合属性B2']])
                self.store.set("/buffer/data/siroco_weapon",set_data['希洛克武器选择'])
                self.store.set("/buffer/data/jude_effects",set_data['辟邪玉效果'])
                self.store.set('/buffer/data/jude_values',set_data['辟邪玉数值'])
                self.store.set('/buffer/data/top_options',set_data['排行选项'])
                self.store.set('/buffer/data/black_purgatory',set_data['黑鸦选择'])
                self.store.set('/buffer/data/siroco',set_data['希洛克选择'])
                self.store.set('/buffer/data/ozma',set_data['奥兹玛选择'])
            except Exception as error:
                    logger.error(error)

        if 2 in page:
            # 第三页(基础/细节/修正)
            try:
                filename = 'page_3.json'
                set_data = {}
                with open(os.path.join(filepath, filename), encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()

                self.store.set("/buffer/data/avatar",set_data['时装选项'])
                self.store.set("/buffer/data/detail_values",set_data['细节数值'])
                self.store.set("/buffer/data/detail_options",set_data['细节选项'])
            except Exception as error:
                    logger.error(error)

        if 3 in page:
            # 第四页(神话属性修正)
            try:
                filename = 'page_4.json'
                set_data = {}
                with open(os.path.join(filepath, filename), encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                self.store.set("/buffer/data/myth_properties",set_data['神话属性修正'])
            except Exception as error:
                    logger.error(error)
        if 4 in page:
            # 第五页(自选装备计算)
            try:
                filename = 'page_5.json'
                set_data = {}
                with open(os.path.join(filepath, filename), encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                self.store.set("/buffer/data/equip_selects",set_data['自选装备'])
                self.store.set("/buffer/data/equip_locked",set_data['装备锁定'])
            except Exception as error:
                logger.error(error)


    def 载入json(self, path='set', page=[0, 1, 2, 3, 4]):

        filepath = './ResourceFiles/{}/{}'.format(self.角色属性A.实际名称, path)

        filename = os.path.join(filepath,"store.json")


        if os.path.exists(filename):          
            try:
                set_data = {}
                with open(filename, encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                self.store.imports(set_data)
            except Exception as error:
                logger.error(error)
        else:
            self.载入旧版json(path,page)

        if 0 in page:
            try:
                self.称号.setCurrentIndex(self.store.get("/buffer/data/title",0))
            except Exception as error:
                    logger.error(error)
            try:
                self.宠物.setCurrentIndex(self.store.get("/buffer/data/pet",0))
            except Exception as error:
                    logger.error(error)
            try:
                self.计算模式选择.setCurrentIndex(self.store.get("/buffer/data/compute_mode",1))
            except Exception as error:
                logger.error(error)
            try:
                self.百变怪选项.setChecked(self.store.get("/buffer/data/ditto_checked",1))
            except Exception as error:
                logger.error(error)
            try:
                self.神话排名选项.setChecked(self.store.get("/buffer/data/myth_top_checked",0))
            except Exception as error:
                logger.error(error)
            try:
                self.切装模式选项.setChecked(self.store.get("/buffer/data/awakening_switch_checked",1))
            except Exception as error:
                logger.error(error)
            try:
                self.线程数选择.setCurrentIndex(self.store.get("/buffer/data/thread_count",12))
            except Exception as error:
                logger.error(error)    
                
            try:
                self.批量选择(0)
                num = 0
                data = self.store.get("/buffer/data/equip_checked",[])
                for i in data:
                        if i == 1:
                            self.装备图标点击事件(num, 1)
                        num += 1
            except Exception as error:
                    logger.error(error)
            try:
                num = 0
                data = self.store.get("/buffer/data/equip_forges",[])
                for i in data:
                            self.装备打造选项[num].setCurrentIndex(i)
                            num += 1
            except Exception as error:
                logger.error(error)

        if 1 in page:
            try:
                try:
                    self.强化觉醒选择(self.store.get('/buffer/data/awakening_binding'))
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = self.store.get('/buffer/data/talismans')

                    for i in data:
                        self.护石栏[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = self.store.get('/buffer/data/consumables')
                    for i in data:
                        self.复选框列表[num].setChecked(i)
                        num += 1
                except Exception as error:
                    logger.error(error)

                data = self.store.get('/buffer/data/skill',{})

                for i in self.角色属性A.技能栏:
                    try:
                        序号 = self.角色属性A.技能序号[i.名称]
                        self.设置技能选项(序号, data[i.名称])
                    except Exception as error:
                        logger.error(error)

                data = self.store.get('/buffer/data/weapon_fusion',[0,0,0,0])

                try:
                    self.武器融合属性A.setCurrentIndex(data[0])
                except Exception as error:
                    logger.error(error)
                try:
                    self.武器融合属性A2.setCurrentIndex(data[1])
                except Exception as error:
                    logger.error(error)
                try:
                    self.武器融合属性B.setCurrentIndex(data[2])
                except Exception as error:
                    logger.error(error)
                try:
                    self.武器融合属性B2.setCurrentIndex(data[3])
                except Exception as error:
                    logger.error(error)

                
                try:
                    self.希洛克武器选择.setCurrentIndex(self.store.get('/buffer/data/siroco_weapon'))
                except Exception as error:
                    logger.error(error)
                try:
                    data = self.store.get('/buffer/data/jude_effects')
                    num = 0
                    for i in data:
                        self.辟邪玉选择[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = self.store.get('/buffer/data/jude_values')                   
                    num = 0
                    for i in data:
                        self.辟邪玉数值[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = self.store.get('/buffer/data/top_options')                   
                    num = 0
                    for i in data:
                        self.排行选项[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = self.store.get('/buffer/data/black_purgatory')                   
                    x = 0
                    for i in data:
                        y = 0
                        for j in i:
                            self.黑鸦词条[x][y].setCurrentIndex(j)
                            y += 1
                        x += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = self.store.get("/buffer/data/siroco")
                    num = 0
                    for i in data:
                        if i == 1:
                            self.希洛克选择(num)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = self.store.get("/buffer/data/ozma")
                    num = 0
                    for i in data:
                        if i == 1:
                            self.奥兹玛选择(num)
                        num += 1
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)
        if 2 in page:
            try:
                try:
                    num = 0
                    data = self.store.get("/buffer/data/avatar")
                    for i in data:
                        self.时装选项[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    x = 0
                    data = self.store.get("/buffer/data/detail_values")
                    for i in data:
                        y = 0
                        for j in i:
                            self.属性设置输入[x][y].setText(j)
                            y += 1
                        x += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = self.store.get("/buffer/data/detail_options")
                    for i in data:
                        self.技能设置输入[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 3 in page:
            try:
                num = 0
                data = self.store.get("/buffer/data/myth_properties")
                for i in data:
                        self.神话属性选项[num].setCurrentIndex(i)
                        num += 1
            except Exception as error:
                logger.error(error)
        if 4 in page:
            try:
                try:
                    num = 0
                    data = self.store.get('/buffer/data/equip_selects')
                    for i in data:
                        self.自选装备[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = self.store.get('/buffer/data/equip_locked')
                    for i in data:
                        self.装备锁定[num].setChecked(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

    def 奥兹玛选择(self, index):
        super().奥兹玛选择(index)
        self.store.emit("/buffer/data/ozma")
    
    def 希洛克希洛克选择(self, index, x):
        super().希洛克选择(index, x)
        self.store.emit("/buffer/data/siroco")
     

    def 保存json(self, path='set', page=[0, 1, 2, 3, 4]):

        if 0 in page:
            # 第一页(装备/选择/打造)
            try:
                self.store.set('/buffer/data/title',self.称号.currentIndex())
                self.store.set('/buffer/data/pet',self.宠物.currentIndex())
                self.store.set('/buffer/data/compute_mode',self.计算模式选择.currentIndex())
                self.store.set('/buffer/data/ditto_checked',self.百变怪选项.isChecked())

                self.store.set('/buffer/data/myth_top_checked',self.神话排名选项.isChecked())
                self.store.set('/buffer/data/awakening_switch_checked',self.切装模式选项.isChecked())
                self.store.set('/buffer/data/thread_count',self.线程数选择.currentIndex())
                self.store.set('/buffer/data/equip_checked',self.装备选择状态)
                self.store.set('/buffer/data/equip_forges',[i.currentIndex() for i in self.装备打造选项])

            except Exception as error:
                logger.error(error)

        if 1 in page:
            # 第二页(技能/符文/药剂)
            try:

                self.store.set('/buffer/data/awakening_binding',self.觉醒选择状态)
                self.store.set('/buffer/data/talismans',[i.currentIndex() for i in self.护石栏])
                self.store.set('/buffer/data/consumables',[i.isChecked() for i in self.复选框列表])

                skill = {}
                for i in self.角色属性A.技能栏:
                    序号 = self.角色属性A.技能序号[i.名称]
                    skill[i.名称] = self.获取技能选项(序号)
                self.store.set('/buffer/data/skill',skill)

                data = [self.武器融合属性A.currentIndex(),self.武器融合属性A2.currentIndex(),self.武器融合属性B.currentIndex(),self.武器融合属性B2.currentIndex()]

                self.store.set("/buffer/data/weapon_fusion",data)

                self.store.set("/buffer/data/siroco_weapon",self.希洛克武器选择.currentIndex())


                self.store.set("/buffer/data/jude_effects",[i.currentIndex() for i in self.辟邪玉选择])
                self.store.set("/buffer/data/jude_values",[i.currentIndex() for i in self.辟邪玉数值])


                self.store.set("/buffer/data/black_purgatory",[[j.currentIndex() for j in i] for i in self.黑鸦词条])

                self.store.set("/buffer/data/top_options",[i.currentIndex() for i in self.排行选项])

            except Exception as error:
                logger.error(error)

        if 2 in page:
            # 第三页(基础/细节/修正)
            try:
                # 时装选项
                self.store.set("/buffer/data/avatar",[i.currentIndex() for i in self.时装选项])
                # 细节数值
                self.store.set("/buffer/data/detail_values",[[j.text() for j in i] for i in self.属性设置输入])
                # 细节选项
                self.store.set("/buffer/data/detail_options",[i.currentIndex() for i in self.技能设置输入])

            except Exception as error:
                logger.error(error)

        if 3 in page:
            # 第四页(神话属性修正)
            try:
                # 神话属性修正
                self.store.set("/buffer/data/myth_properties",[i.currentIndex() for i in self.神话属性选项])
            except Exception as error:
                logger.error(error)

        if 4 in page:
            # 第五页(自选装备计算)
            try:
                self.store.set("/buffer/data/equip_selects",[i.currentIndex() for i in self.自选装备])
                self.store.set("/buffer/data/equip_locked",[i.isChecked() for i in self.装备锁定])
            except Exception as error:
                logger.error(error)
        try:
            filepath = './ResourceFiles/{}/{}'.format(self.角色属性A.实际名称, path)
            filename = "store.json"
            set_data = self.store.exports(lambda i: str.startswith(i,"/buffer/data"))
            with open(os.path.join(filepath, filename), "w",
                          encoding='utf-8') as fp:
                    json.dump(set_data, fp, ensure_ascii=False, indent=4)
            fp.close()
        except Exception as error:
            logger.error(error)

            

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        self.保存json(path)
    
    def closeEvent(self, event):
        DefaultDialogRegister.dispose()
        return super().closeEvent(event)

    # 一键修正计算
    def 一键修正(self, x=0):
        sign = -1
        try:
            if self.一键站街设置输入[0].text() != '' or self.一键站街设置输入[1].text() != '':
                sign = 1
        except:
            pass
        if sign == -1:
            QMessageBox.information(self, "错误", "请在按钮左侧输入站街数值")
            return

        if x == 0:
            if self.组合计算(2) == 0:
                QMessageBox.information(self, "错误", "请勾选齐全身上穿戴的装备")
                return
            if self.组合计算(2) > 1:
                QMessageBox.information(self, "错误", "请勿勾选身上未穿戴的装备")
                return

        self.修正套装计算(x)
        self.角色属性B = deepcopy(self.初始属性)
        self.输入属性(self.角色属性B)
        self.角色属性B.穿戴装备计算套装(self.有效穿戴组合[0])
        for i in self.角色属性B.装备栏:
            equ.get_equ_by_name(i).城镇属性_BUFF(self.角色属性B)
            equ.get_equ_by_name(i).BUFF属性(self.角色属性B)
        for i in self.角色属性B.套装栏:
            equ.get_suit_by_name(i).城镇属性_BUFF(self.角色属性B)
            equ.get_suit_by_name(i).BUFF属性(self.角色属性B)
        self.角色属性B.装备基础()
        self.角色属性B.站街计算()
        self.面板修正(self.角色属性B.类型, x)

    def 面板修正(self, 类型, x):
        数据 = []
        原始数据 = []
        名称 = ['站街面板']
        for i in range(1):
            try:
                if self.一键站街设置输入[i + x].text() != '':
                    数据.append(int(self.一键站街设置输入[i + x].text()))
                else:
                    数据.append(0)
            except:
                QMessageBox.information(self, "错误", 名称[i] + "输入格式错误,已重置为空")
                self.一键站街设置输入[i + x].setText('')
                数据.append(0)

        if 数据[0] == 0:
            QMessageBox.information(self, "错误", "请输入站街面板")
            return

        for i in range(3):
            if self.属性设置输入[i][15].text() != '':
                原始数据.append(int(self.属性设置输入[i][15].text()))
            else:
                原始数据.append(0)

        self.站街面板修正(类型, 数据, 原始数据)
        self.click_window(2)
        QMessageBox.information(
            self, "自动修正计算完毕", "仅对站街修正进行了修改,使面板与输入一致<br>请自行核对其它页面 非智力/体力/精神条目")

    def click_window(self, index):
        self.当前页面 = index
        if self.stacked_layout.currentIndex() != index:
            self.stacked_layout.setCurrentIndex(index)
        for i in self.window_btn:
            i.setStyleSheet(页签样式)
        self.window_btn[index].setStyleSheet(页签样式_选中)

        if index == 3:
            count1 = 0
            count2 = 0
            num = 0
            width = 1100
            height = 680
            page4_height = 0
            for j in equ.get_equ_id_list():
                temp = equ.get_equ_by_id(j)
                if temp.品质 == '神话':
                    if self.装备选择状态[j] == 1 or temp.名称 in self.self_selects:
                        self.神话属性图片[num].move(
                            int(width / 7 * (count1 % 7 + 0.42)),
                            int(height / 5.2 * (count2 + 0.05)) - 3)
                        for i in range(4):
                            self.神话属性选项[num * 4 + i].move(
                                int(width / 7 * (count1 % 7) + 6),
                                int(height / 5.2 * (count2 + 0.05)) -
                                3 + i * 22 + 32)
                        count1 += 1
                        if count1 % 7 == 0:
                            count2 += 1
                        page4_height += 1
                    else:
                        self.神话属性图片[num].move(-1000, -1000)
                        for i in range(4):
                            self.神话属性选项[num * 4 + i].move(-1000, -1000)
                    num += 1
            page4_height = max(ceil(page4_height / 7) * 130, height)
            self.main_frame4.setMinimumSize(width, page4_height)
        if index == 4:
            self.自选计算(1)

    def 神话数量判断(self, x=0):
        count = 0
        for j in equ.get_equ_id_list():
            if equ.get_equ_by_id(j).品质 == '神话':
                if self.装备选择状态[j] == 1:
                    count += 1
        if x == 0:
            return count == 0 
        else:
            return count

    def 站街面板修正(self, 类型, 输入面板, 修正面板):
        if 类型 == '智力':
            修正前面板 = int(self.角色属性B.系数数值站街())
            修正后面板 = 输入面板[0] - 修正前面板 + 修正面板[0]
            self.属性设置输入[0][15].setText(str(int(修正后面板)))
        elif 类型 == '体力':
            修正前面板 = int(self.角色属性B.系数数值站街())
            修正后面板 = 输入面板[0] - 修正前面板 + 修正面板[1]
            self.属性设置输入[1][15].setText(str(int(修正后面板)))
        elif 类型 == '精神':
            修正前面板 = int(self.角色属性B.系数数值站街())
            修正后面板 = 输入面板[0] - 修正前面板 + 修正面板[2]
            self.属性设置输入[2][15].setText(str(int(修正后面板)))

    def 换装套装(self):
        换装套装 = []
        换装套装字典 = {}
        换装装备 = []
        if hasattr(self, "自选换装装备"):
            for i in self.自选换装装备:
                换装装备.append(i)
            for i in 换装装备:
                j = equ.get_equ_by_name(i).所属套装
                if j == '智慧产物':
                    try:
                        k = equ.get_equ_by_name(i).所属套装2
                        换装套装字典[k] = 换装套装字典.get(k, 0) + 1
                    except:
                        pass
                elif j != '无':
                    换装套装字典[j] = 换装套装字典.get(j, 0) + 1
        for i in 换装套装字典.keys():
            if 换装套装字典[i] >= 2 and (i + '[2]') in equ.get_suit_name():
                换装套装.append(i + '[2]')
            if 换装套装字典[i] >= 3 and (i + '[3]') in equ.get_suit_name():
                换装套装.append(i + '[3]')
            if 换装套装字典[i] >= 5 and (i + '[5]') in equ.get_suit_name():
                换装套装.append(i + '[5]')
        return 换装套装, 换装装备

    def 换装计算(self):
        换装套装, 换装装备 = self.换装套装()
        if not self.登记启用: return None
        t装备打造 = []
        t黑鸦词条 = []
        t希洛克选择状态 = self.希洛克选择状态
        t奥兹玛选择状态 = self.奥兹玛选择状态

        #  保存
        try:
            for i in range(len(换装装备)): # bugfix
                打造 = []
                打造.append(self.装备打造选项[i].currentIndex())
                打造.append(self.装备打造选项[i+12].currentIndex())
                t装备打造.append(打造)
                self.装备打造选项[i].setCurrentIndex(1)  # 增幅
                self.装备打造选项[i + 12].setCurrentIndex(self.自选换装打造[i])      
        except Exception as e:
            print(e)
        try:
            for i in range(4):
                词条 = []           
                词条.append(self.黑鸦词条[i][0].currentIndex())
                词条.append(self.黑鸦词条[i][1].currentIndex())
                词条.append(self.黑鸦词条[i][3].currentIndex())
                t黑鸦词条.append(词条)
                self.黑鸦词条[i][0].setCurrentIndex(2)  # 自选数值
                self.黑鸦词条[i][1].setCurrentIndex(self.换装遴选[i][0])  # 自选数值
                self.黑鸦词条[i][3].setCurrentIndex(self.换装遴选[i][1])  # 自选数值
        except Exception as e:
            print(e)
        try:
            self.希洛克选择状态 = self.换装希洛克
        except Exception as e:
            print(e)
            pass
        try:
            self.奥兹玛选择状态 = self.换装奥兹玛
        except Exception as e:
            print(e)
            pass
        BUFF = deepcopy(self.初始属性)
        self.输入属性(BUFF)
        BUFF.穿戴装备(换装装备, 换装套装)

        for i in range(len(t装备打造)):          
            self.装备打造选项[i].setCurrentIndex(t装备打造[i][0])  # 增幅
            self.装备打造选项[i + 12].setCurrentIndex(t装备打造[i][1])

        for i in range(len(t黑鸦词条)):     
            self.黑鸦词条[i][0].setCurrentIndex(t黑鸦词条[i][0])  # 自选数值
            self.黑鸦词条[i][1].setCurrentIndex(t黑鸦词条[i][1])  # 自选数值
            self.黑鸦词条[i][3].setCurrentIndex(t黑鸦词条[i][2])  # 自选数值

        self.希洛克选择状态 = t希洛克选择状态
        self.奥兹玛选择状态 = t奥兹玛选择状态
        #  恢复
        return BUFF

    def 自选计算(self, x=0):
        BUFF = None
        if x == 0:
            self.保存配置(self.存档位置)
            self.关闭排行窗口()
            self.排行数据.clear()

        self.角色属性A = deepcopy(self.初始属性)
        if x == 0:
            self.输入属性(self.角色属性A)
        else:
            self.输入属性(self.角色属性A, 1)

        if self.是否计算 != 1:
            self.click_window(1)
            return

        装备 = self.self_selects
        套装 = []
        套装字典 = {}

        for i in 装备:
            j = equ.get_equ_by_name(i).所属套装
            if j == '智慧产物':
                try:
                    k = equ.get_equ_by_name(i).所属套装2
                    套装字典[k] = 套装字典.get(k, 0) + 1
                except:
                    pass
            elif j != '无':
                套装字典[j] = 套装字典.get(j, 0) + 1

        for i in 套装字典.keys():
            if 套装字典[i] >= 2 and (i + '[2]') in equ.get_suit_name():
                套装.append(i + '[2]')
            if 套装字典[i] >= 3 and (i + '[3]') in equ.get_suit_name():
                套装.append(i + '[3]')
            if 套装字典[i] >= 5 and (i + '[5]') in equ.get_suit_name():
                套装.append(i + '[5]')

        if x != 0:
            伤害列表 = []
            for i in 辟邪玉列表:
                i.当前值 = i.最大值
                temp = deepcopy(self.角色属性A)
                i.穿戴属性(temp)
                temp.穿戴装备(装备, 套装)
                伤害列表.append(temp.BUFF计算(0))

            提升率 = []
            for i in range(1, len(伤害列表)):
                if 伤害列表[0] != 0:
                    提升率.append(伤害列表[i] / 伤害列表[0] - 1)
                else:
                    提升率.append(0)

            提升率排序 = copy(提升率)
            提升率排序.sort(reverse=True)

            for i in range(len(提升率)):
                temp = str('%.2f' % (提升率[i] * 100)) + '%'
                self.辟邪玉提升率2[i].setText(temp)
                x = 提升率排序.index(提升率[i]) / len(提升率) * 10 - 2
                y = 1 / (1 + math.exp(-x))
                if SkinVersion == 'None':
                    颜色 = (0, 0, 0)
                else:
                    颜色 = (int(255 - 80 * y), int(245 - 100 * y),
                          int(0 + 150 * y))
                self.辟邪玉提升率1[i].setStyleSheet(
                    'QLabel{font-size:12px;color:rgb' + str(颜色) + '}')
                self.辟邪玉提升率2[i].setStyleSheet(
                    'QLabel{font-size:12px;color:rgb' + str(颜色) + '}')


            self.角色属性A = deepcopy(self.初始属性)

            self.输入属性(self.角色属性A)
            C = self.站街计算(装备, 套装)
            B = deepcopy(self.角色属性A)
            B.穿戴装备(装备, 套装)
            D = deepcopy(B)



            统计详情 = B.BUFF计算(1)
            # 双切 Start
            if self.登记启用:
                BUFF = self.换装计算()

            if BUFF is not None:
                BUFF统计详情 = BUFF.BUFF计算(1)
                B.BUFF力量per = BUFF.BUFF力量per
                B.BUFF智力per = BUFF.BUFF智力per
                B.BUFF独立per = BUFF.BUFF独立per
                B.BUFF魔攻per = BUFF.BUFF魔攻per
                B.BUFF物攻per = BUFF.BUFF物攻per            
            # 双切 End
            合计力量 = 0
            合计智力 = 0
            合计物攻 = 0
            合计魔攻 = 0
            合计独立 = 0

            for i in range(len(B.技能栏)):
                if sum(统计详情[i]) != 0:   
                    详情 = 统计详情[i]  # 如果设置切装 则适用切装的属性
                    if BUFF is not None and B.技能栏[i].名称 in ['禁忌诅咒', '死命召唤', '勇气祝福', '勇气圣歌', '荣誉祝福']:
                        详情 = BUFF统计详情[i]
                    合计力量 += 详情[3]
                    合计智力 += 详情[4]
                    合计物攻 += 详情[5]
                    合计魔攻 += 详情[6]
                    合计独立 += 详情[7]

            总奶量 = ''
            # tempstr = ''
            if 合计力量 == 合计智力:
                总奶量 += '力智+' + str(合计力量)
            else:
                总奶量 += '力量+' + str(合计力量)
                总奶量 += ',智力+' + str(合计智力)

            if 合计物攻 == 合计魔攻 and 合计魔攻 == 合计独立:
                总奶量 += ',三攻+' + str(合计物攻)
            else:
                总奶量 += ',物攻+' + str(合计物攻)
                总奶量 += ',魔攻+' + str(合计魔攻)
                总奶量 += ',独立+' + str(合计独立)
            # self.总伤害.setText(str(tempstr))

            if self.登记启用:
                x = BUFF.BUFF面板()
            else:
                x = B.BUFF面板()
            y = B.一觉面板()
            self.角色属性B = deepcopy(B)
            tempstr = self.装备描述_BUFF计算(B)
            图片列表 = self.获取装备图片(装备)
            for i in range(12):
                self.图片显示[i].setToolTip(tempstr[i])
                self.图片显示[i].setMovie(图片列表[i])

            self.面板显示[0].setText('站街:' + str(int(C.系数数值站街())))
            self.面板显示[1].setText('适用:' + str(int(B.系数数值进图())))

            self.面板显示[2].setText(' ' + x[0])

            self.面板显示[3].setText('力量:' + str(x[1]))
            self.面板显示[4].setText('智力:' + str(x[2]))
            self.面板显示[5].setText('物攻:' + str(x[3]))
            self.面板显示[6].setText('魔攻:' + str(x[4]))
            self.面板显示[7].setText('独立:' + str(x[5]))

            self.面板显示[8].setText(' ' + y[0])
            self.面板显示[9].setText('力量:' + str(y[1]))
            self.面板显示[10].setText('智力:' + str(y[2]))

            tempstr = []
            tempstr.append('BUFF力量% :' +
                           str(int(round(B.BUFF力量per * 100, 0))) + '%')
            tempstr.append('BUFF智力% :' +
                           str(int(round(B.BUFF智力per * 100, 0))) + '%')
            tempstr.append('BUFF物攻% :' +
                           str(int(round(B.BUFF物攻per * 100, 0))) + '%')
            tempstr.append('BUFF魔攻% :' +
                           str(int(round(B.BUFF魔攻per * 100, 0))) + '%')
            tempstr.append('BUFF独立% :' +
                           str(int(round(B.BUFF独立per * 100, 0))) + '%')
            tempstr.append('一觉力智  :' + str(int(round(B.一觉力智, 0))))
            tempstr.append('一觉力智% :' + str(int(round(B.一觉力智per * 100, 0))) +
                           '%')
            if B.角色 == '圣职者(男)':
                tempstr.append('守护徽章% :' +
                               str(int(round(B.守护徽章per * 100, 0))) + '%')
            elif B.角色 == '圣职者(女)' or B.角色 == '圣职者(女)':
                tempstr.append('BUFF增幅率:' +
                               str(int(round(B.BUFF额外增幅率 * 100, 0))) + '%')
            tempstr.append(str(总奶量))

            # if self.角色属性B.希洛克武器词条 == 1:
            #     武器词条最高值 = self.角色属性B.自适应最高值
            #     武器属性A = 武器属性A列表[武器词条最高值[0]]
            #     武器属性B = 武器属性B列表[武器词条最高值[1]]
            #     tempstr.append("属性1:" +"<font style='color:gray'>"+武器属性A.固定属性描述 + '</font>')
            #     if self.角色属性B.武器词条触发 == 1:
            #         tempstr.append("属性2:" +"<font style='color:gray'>"+武器属性B.固定属性描述 + '</font>')

            if self.角色属性B.希洛克武器词条 == 1:
                temp = ""
                武器词条最高值 = self.角色属性B.自适应最高值
                武器属性A = 武器属性A列表[武器词条最高值[0]]
                武器属性B = 武器属性B列表[武器词条最高值[1]]
                # tempstr += '<br><br>' + "属性1:" +"<font style='color:gray'>"+武器属性A.固定属性描述 + '</font>,' + 武器属性A.随机属性描述 + str(武器属性A.最大值)+ ('%' if 武器属性A.间隔 / 10 < 1 else '')
                temp += "残香 属性1:" + "<font style='color:gray'>" + 武器属性A.固定属性描述 + '</font>'
                if self.角色属性B.武器词条触发 == 1:
                    # tempstr += "| 属性2:" +"<font style='color:gray'>"+武器属性B.固定属性描述 + '</font>,' + 武器属性B.随机属性描述 + str(武器属性B.最大值)+ ('%' if 武器属性B.间隔 / 10 < 1 else '')
                    temp += " | 属性2:" + "<font style='color:gray'>" + 武器属性B.固定属性描述 + '</font>'
                tempstr.append(temp)

            if self.角色属性B.黑鸦词条[0][0] == 1 or self.角色属性B.黑鸦词条[1][
                0] == 1 or self.角色属性B.黑鸦词条[2][0] == 1 or self.角色属性B.黑鸦词条[
                3][0] == 1:
                temp = ""
                temp += "遴选"
                if self.角色属性B.黑鸦词条[0][0] == 1:
                    if self.角色属性B.武器变换属性自适应 > 0:
                        黑鸦武器 = 武器变换属性列表[self.角色属性B.武器变换属性自适应]
                        temp += " 武器:" + "<font style='color:gray'>" + 黑鸦武器.固定属性描述 + '</font>'
                    else:
                        temp += " 武器:" + "<font style='color:gray'>" + '觉醒' + '</font>'
                if self.角色属性B.黑鸦词条[1][0] == 1:
                    黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[0]]
                    temp += " 戒指:" + "<font style='color:gray'>" + 黑鸦.固定属性描述 + '</font>'
                if self.角色属性B.黑鸦词条[2][0] == 1:
                    黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[1]]
                    temp += " 辅助:" + "<font style='color:gray'>" + 黑鸦.固定属性描述 + '</font>'
                if self.角色属性B.黑鸦词条[3][0] == 1:
                    黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[2]]
                    temp += " 下装:" + "<font style='color:gray'>" + 黑鸦.固定属性描述 + '</font>'

                tempstr.append(temp)

            count = 0
            for i in tempstr:
                self.词条显示[count].setText(i)
                count += 1

            for i in self.套装名称显示:
                i.setText('')

            self.套装名称显示[0].setText(装备[11])
            self.套装名称显示[0].setStyleSheet(
                "QLabel{font-size:12px;color:rgb(255,255,255)}")

            套装名称 = []
            套装名称.extend(套装)

            神话所在套装 = []
            for i in range(11):
                if equ.get_equ_by_name(装备[i]).品质 == '神话':
                    神话所在套装.append(equ.get_equ_by_name(装备[i]).所属套装)

            套装 = []
            套装件数 = []
            套装属性 = []
            for i in range(len(套装名称)):
                temp = 套装名称[i].split('[')[0]
                if temp not in 套装:
                    套装.append(temp)
                    套装件数.append([])
                    套装属性.append('')
                if len(套装名称[i].split('[')) > 1:
                    件数 = 套装名称[i].split('[')[1].split(']')[0]
                    套装件数[套装.index(temp)].append(件数)
                    套装属性[套装.index(
                        temp
                    )] += '<font size="3" face="宋体"><font color="#78FF1E">' + 套装名称[
                        i] + '</font><br>' + equ.get_suit_by_name(套装名称[i]).装备描述_BUFF(
                        self.角色属性B)[:-4] + '</font><br>'

            数量 = [0] * 3
            for i in range(15):
                数量[i % 3] += self.希洛克选择状态[i]

            i = 0  # 奈克斯属性2
            temp = ''
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
                temp += 'Lv50主动技能力量、智力增加量+40<br>'
            if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
                temp += '[守护恩赐]体力、精神+80<br>'
                temp += '[启示:圣歌][人偶操纵者]智力+80<br>'
            if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
                temp += 'Lv50主动技能物攻、魔攻、独立增加量+2%<br>'
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                self.希洛克选择状态[i * 3 + 2]) > 1:
                套装.append("希洛克-奈克斯")
                套装件数.append([
                    self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                    self.希洛克选择状态[i * 3 + 2]
                ])
                套装属性.append(temp)

            i = 1  # 暗杀者属性2
            temp = ''
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
                temp += 'Lv50主动技能力量、智力增加量+28<br>'
            if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
                temp += '[守护恩赐]体力、精神+55<br>'
                temp += '[启示:圣歌][人偶操纵者]智力+55<br>'
            if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
                temp += 'Lv50主动技能物攻、魔攻、独立增加量+1%<br>'
                temp += 'Lv50主动技能力量、智力增加量+1%<br>'
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                self.希洛克选择状态[i * 3 + 2]) > 1:
                套装.append("希洛克-暗杀者")
                套装件数.append([
                    self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                    self.希洛克选择状态[i * 3 + 2]
                ])
                套装属性.append(temp)

            i = 2  # 卢克西属性2
            temp = ''
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
                temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
                pass  # 下装
            if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
                temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
                pass  # 戒指
            if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
                temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
                pass  # 辅助装备
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                self.希洛克选择状态[i * 3 + 2]) > 1:
                套装.append("希洛克-卢克西")
                套装件数.append([
                    self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                    self.希洛克选择状态[i * 3 + 2]
                ])
                套装属性.append(temp)

            i = 3  # 守门人属性2
            temp = ''
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
                temp += 'Lv50主动技能力量、智力增加量+1%<br>'
                temp += 'Lv50主动技能力量、智力增加量+20<br>'
            if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
                temp += '[守护恩赐]体力、精神+55<br>'
                temp += '[启示:圣歌][人偶操纵者]智力+55<br>'
            if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
                temp += 'Lv30Buff技能力量、智力增加量+1%<br>'
                temp += '[守护恩赐]体力、精神+30<br>'
                temp += '[启示:圣歌][人偶操纵者]智力+30<br>'
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                self.希洛克选择状态[i * 3 + 2]) > 1:
                套装.append("希洛克-守门人")
                套装件数.append([
                    self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                    self.希洛克选择状态[i * 3 + 2]
                ])
                套装属性.append(temp)

            i = 4  # 洛多斯属性2
            temp = ''
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
                temp += 'Lv50主动技能力量、智力增加量+2%<br>'
                # 属性.一觉力智per *= 1.02  # 下装
            if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
                temp += 'Lv30Buff技能力量、智力增加量+2%<br>'
            if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
                temp += 'Lv30Buff技能物理、魔法、独立攻击力增加量+1%<br>'
                temp += '[守护恩赐]体力、精神+30<br>'
                temp += '[启示:圣歌][人偶操纵者]智力+30<br>'
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                self.希洛克选择状态[i * 3 + 2]) > 1:
                套装.append("希洛克-洛多斯")
                套装件数.append([
                    self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                    self.希洛克选择状态[i * 3 + 2]
                ])
                套装属性.append(temp)

            for i in range(len(套装)):
                if len(套装件数[i]) > 0:
                    self.套装名称显示[i + 1].setText(套装[i] + '[' +
                                               str(max(套装件数[i])) + ']')
                else:
                    self.套装名称显示[i + 1].setText(套装[i])
                if 套装[i] in 神话所在套装:
                    self.套装名称显示[i + 1].setStyleSheet(
                        "QLabel{font-size:12px;color:rgb(226,150,146)}")
                else:
                    self.套装名称显示[i + 1].setStyleSheet(
                        "QLabel{font-size:12px;color:rgb(255,255,255)}")
                self.套装名称显示[i + 1].setToolTip(套装属性[i][:-4])

            提升率 = D.BUFF计算(0)
            if len(self.基准值) != 0:
                self.提升率显示.setText(self.对比输出(提升率, self.基准值[0], 1, 1))
            else:
                self.提升率显示.setText(str(round(提升率, 2)) + '%')

        if x == 0:
            self.排行数据.append(装备 + [0] + 套装 + ['无'])
            self.输出界面(0)

    def 站街计算(self, 装备名称, 套装名称):
        C = deepcopy(self.角色属性A)
        C.穿戴装备(装备名称, 套装名称)
        for i in C.装备栏:
            equ.get_equ_by_name(i).城镇属性_BUFF(C)
            equ.get_equ_by_name(i).BUFF属性(C)
        for i in C.套装栏:
            equ.get_suit_by_name(i).城镇属性_BUFF(C)
            equ.get_suit_by_name(i).BUFF属性(C)
        C.装备基础()
        C.站街计算()
        return C

    def 对比输出(self, A, B, x=0, y=0):
        if B == 0:
            return str(A)
        if x == 0:
            temp = int(A - B)
            if temp == 0:
                if y == 1:
                    return '不变'
                return '-'
            elif temp > 0:
                return '<font face="宋体" color= "#96FF1E">+' + str(
                    temp) + '</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + str(
                    temp) + '</font>'
        else:
            temp = round((A / B - 1) * 100, 2)
            if temp == 0:
                if y == 1:
                    return '不变'
                return '-'
            elif temp > 0:
                return '<font face="宋体" color= "#96FF1E">+' + str(
                    '%.2f' % temp) + '%</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + str(
                    '%.2f' % temp) + '%</font>'

    def 输出界面(self, index, name=''):
        装备名称 = []
        套装名称 = []
        百变怪 = self.排行数据[index][-1]
        for i in range(12):
            装备名称.append(self.排行数据[index][i])
        for i in range(13, len(self.排行数据[index]) - 1):
            套装名称.append(self.排行数据[index][i])

        C = self.站街计算(装备名称, 套装名称)

        self.角色属性B = deepcopy(self.角色属性A)
        self.角色属性B.穿戴装备(装备名称, 套装名称)
        # 双切 Start

        if self.登记启用 :
            try:
                换装套装, 换装装备 = self.换装套装()
            except:
                pass

        temp = deepcopy(self.角色属性B)
        统计详情 = self.角色属性B.BUFF计算(1)
        提升率 = temp.BUFF计算(0)


        if self.登记启用:
            双切属性 = self.换装计算()
            双切详情 = 双切属性.BUFF计算(1)
            self.输入属性(self.角色属性B)
            self.角色属性B.切换详情 = '换装详情: <br>' + '<br>'.join([' , '.join(换装装备[i:i+4]) for i in range(0, len(换装装备), 4)])
        # 双切 end
        # self.角色属性B.装备属性计算()

        # 最大输出界面限制
        if len(self.输出窗口列表) >= 10:
            del self.输出窗口列表[0]

        输出窗口 = QWidget()
        输出窗口.setStyleSheet('''QToolTip {
           background-color: black;
           color: white;
           border: 0px
           }''')
        输出窗口.setFixedSize(788, 546)
        pox_y = 18
        pox_y2 = 11
        temp = ''
        if name == '':
            temp += '详细数据'
        else:
            temp += name
        # temp += '（最多显示前18个技能）'+"装备版本:"+self.角色属性A.版本 + " 增幅版本:" + self.角色属性A.增幅版本
        输出窗口.setWindowTitle(temp)
        输出窗口.setWindowIcon(self.icon)
        QLabel(输出窗口).setPixmap(self.输出背景图片)
        人物 = QLabel(输出窗口)
        图片 = QPixmap('./ResourceFiles/' + self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(90 + int(45 - 图片.width() / 2), 40 - pox_y2)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)

        y = self.角色属性B.一觉面板()

        if self.登记启用:
            x = 双切属性.BUFF面板()
        else:
            x = self.角色属性B.BUFF面板()

        面板显示 = []
        for i in range(11):
            面板显示.append(QLabel(输出窗口))
        面板显示[0].setText('站街:' + str(int(C.系数数值站街())))
        面板显示[1].setText('适用:' + str(int(self.角色属性B.系数数值进图())))

        面板显示[2].setText(' ' + x[0])
        面板显示[3].setText('力量:' + str(x[1]))
        面板显示[4].setText('智力:' + str(x[2]))
        面板显示[5].setText('物攻:' + str(x[3]))
        面板显示[6].setText('魔攻:' + str(x[4]))
        面板显示[7].setText('独立:' + str(x[5]))

        面板显示[8].setText(' ' + y[0])
        面板显示[9].setText('力量:' + str(y[1]))
        面板显示[10].setText('智力:' + str(y[2]))

        const = 139
        面板显示[0].move(35, const - pox_y2)
        面板显示[1].move(165, const - pox_y2)

        const += 36
        count = 0
        for i in [2, 3, 4, 5, 6, 7]:
            面板显示[i].move(35, const + count * 18 - pox_y2)
            count += 1

        count = 0
        for i in [8, 9, 10]:
            面板显示[i].move(165, const + count * 18 - pox_y2)
            count += 1

        for i in range(len(面板显示)):
            if i != 1:
                面板显示[i].setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(255,255,255)}")
            else:
                面板显示[i].setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(150,255,30)}")
            面板显示[i].resize(100, 18)
            面板显示[i].setAlignment(Qt.AlignLeft)
        if self.登记启用:
            self.角色属性B.BUFF力量per = 双切属性.BUFF力量per
            self.角色属性B.BUFF智力per = 双切属性.BUFF智力per
            self.角色属性B.BUFF独立per = 双切属性.BUFF独立per
            self.角色属性B.BUFF魔攻per = 双切属性.BUFF魔攻per
            self.角色属性B.BUFF物攻per = 双切属性.BUFF物攻per
            self.角色属性B.BUFFLv = 双切属性.BUFFLv
            self.角色属性B.BUFF力量 = 双切属性.BUFF力量
            self.角色属性B.BUFF智力 = 双切属性.BUFF智力
            self.角色属性B.BUFF物攻 = 双切属性.BUFF物攻
            self.角色属性B.BUFF魔攻 = 双切属性.BUFF魔攻
            self.角色属性B.BUFF独立 = 双切属性.BUFF独立
        tempstr = []
        tempstr.append('BUFF力量% :' +
                       str(int(round(self.角色属性B.BUFF力量per * 100, 0))) + '%')
        tempstr.append('BUFF智力% :' +
                       str(int(round(self.角色属性B.BUFF智力per * 100, 0))) + '%')
        tempstr.append('BUFF物攻% :' +
                       str(int(round(self.角色属性B.BUFF物攻per * 100, 0))) + '%')
        tempstr.append('BUFF魔攻% :' +
                       str(int(round(self.角色属性B.BUFF魔攻per * 100, 0))) + '%')
        tempstr.append('BUFF独立% :' +
                       str(int(round(self.角色属性B.BUFF独立per * 100, 0))) + '%')
        tempstr.append('一觉力智  :' + str(int(round(self.角色属性B.一觉力智, 0))))
        tempstr.append('一觉力智% :' +
                       str(int(round(self.角色属性B.一觉力智per * 100, 0))) + '%')
        tempstr.append('守护徽章% :' +
                       str(int(round(self.角色属性B.守护徽章per * 100, 0))) + '%')
        if self.角色属性B.角色 == '圣职者(男)':
            tempstr.append('守护徽章% :' +
                           str(int(round(self.角色属性B.守护徽章per * 100, 0))) + '%')
        elif self.角色属性B.角色 == '圣职者(女)' or self.角色属性B.角色 == '魔法师(女)':
            tempstr.append('BUFF增幅率:' +
                           str(int(round(self.角色属性B.BUFF额外增幅率 * 100, 0))) +
                           '%')

        j = 318
        for i in tempstr:
            templab = QLabel(输出窗口)
            templab.setText(i)
            templab.setStyleSheet(
                "QLabel{font-size:12px;color:rgb(104,213,237)}")
            templab.move(20, j - pox_y2)
            templab.resize(305, 18)
            templab.setAlignment(Qt.AlignLeft)
            j += 18

        位置 = 313
        间隔 = 20
        适用称号名称 = QLabel(self.称号.currentText(), 输出窗口)
        适用称号名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用称号名称.move(114, 位置 - pox_y2)
        适用称号名称.resize(150, 18)
        适用称号名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔
        适用称号名称.setToolTip(self.称号描述())

        适用宠物名称 = QLabel(self.宠物.currentText(), 输出窗口)
        适用宠物名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用宠物名称.move(114, 位置 - pox_y2)
        适用宠物名称.resize(150, 18)
        适用宠物名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔
        适用宠物名称.setToolTip(self.宠物描述())

        适用中的套装 = QLabel(装备名称[11], 输出窗口)
        适用中的套装.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用中的套装.move(132, 位置 - pox_y2)
        适用中的套装.resize(132, 18)
        适用中的套装.setAlignment(Qt.AlignCenter)

        神话所在套装 = '无'
        for i in range(11):
            temp = equ.get_equ_by_name(装备名称[i])
            if temp.品质 == '神话':
                神话所在套装 = temp.所属套装

        套装 = []
        套装件数 = []
        套装属性 = []
        for i in range(len(套装名称)):
            temp = 套装名称[i].split('[')[0]
            if temp not in 套装:
                套装.append(temp)
                套装件数.append([])
                套装属性.append('')
            if len(套装名称[i].split('[')) > 1:
                件数 = 套装名称[i].split('[')[1].split(']')[0]
                套装件数[套装.index(temp)].append(件数)
                套装属性[套装.index(
                    temp
                )] += '<font size="3" face="宋体"><font color="#78FF1E">' + 套装名称[
                    i] + '</font><br>' + equ.get_suit_by_name(套装名称[i]).装备描述_BUFF(
                    self.角色属性B)[:-4] + '</font><br>'

        数量 = [0] * 3
        for i in range(15):
            数量[i % 3] += self.希洛克选择状态[i]

        i = 0  # 奈克斯属性2
        temp = ''
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
            temp += 'Lv50主动技能力量、智力增加量+40<br>'
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
            temp += '[守护恩赐]体力、精神+80<br>'
            temp += '[启示:圣歌][人偶操纵者]智力+80<br>'
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
            temp += 'Lv50主动技能物攻、魔攻、独立增加量+2%<br>'
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
            self.希洛克选择状态[i * 3 + 2]) > 1:
            套装.append("希洛克-奈克斯")
            套装件数.append([
                self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                self.希洛克选择状态[i * 3 + 2]
            ])
            套装属性.append(temp)

        i = 1  # 暗杀者属性2
        temp = ''
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
            temp += 'Lv50主动技能力量、智力增加量+28<br>'
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
            temp += '[守护恩赐]体力、精神+55<br>'
            temp += '[启示:圣歌][人偶操纵者]智力+55<br>'
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
            temp += 'Lv50主动技能物攻、魔攻、独立增加量+1%<br>'
            temp += 'Lv50主动技能力量、智力增加量+1%<br>'
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
            self.希洛克选择状态[i * 3 + 2]) > 1:
            套装.append("希洛克-暗杀者")
            套装件数.append([
                self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                self.希洛克选择状态[i * 3 + 2]
            ])
            套装属性.append(temp)

        i = 2  # 卢克西属性2
        temp = ''
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
            temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
            pass  # 下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
            temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
            pass  # 戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
            temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
            pass  # 辅助装备
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
            self.希洛克选择状态[i * 3 + 2]) > 1:
            套装.append("希洛克-卢克西")
            套装件数.append([
                self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                self.希洛克选择状态[i * 3 + 2]
            ])
            套装属性.append(temp)

        i = 3  # 守门人属性2
        temp = ''
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
            temp += 'Lv50主动技能力量、智力增加量+1%<br>'
            temp += 'Lv50主动技能力量、智力增加量+20<br>'
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
            temp += '[守护恩赐]体力、精神+55<br>'
            temp += '[启示:圣歌][人偶操纵者]智力+55<br>'
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
            temp += 'Lv30Buff技能力量、智力增加量+1%<br>'
            temp += '[守护恩赐]体力、精神+30<br>'
            temp += '[启示:圣歌][人偶操纵者]智力+30<br>'
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
            self.希洛克选择状态[i * 3 + 2]) > 1:
            套装.append("希洛克-守门人")
            套装件数.append([
                self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                self.希洛克选择状态[i * 3 + 2]
            ])
            套装属性.append(temp)

        i = 4  # 洛多斯属性2
        temp = ''
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
            temp += 'Lv50主动技能力量、智力增加量+2%<br>'
            # 属性.一觉力智per *= 1.02  # 下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
            temp += 'Lv30Buff技能力量、智力增加量+2%<br>'
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
            temp += 'Lv30Buff技能物理、魔法、独立攻击力增加量+1%<br>'
            temp += '[守护恩赐]体力、精神+30<br>'
            temp += '[启示:圣歌][人偶操纵者]智力+30<br>'
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
            self.希洛克选择状态[i * 3 + 2]) > 1:
            套装.append("希洛克-洛多斯")
            套装件数.append([
                self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] +
                self.希洛克选择状态[i * 3 + 2]
            ])
            套装属性.append(temp)

        for i in range(len(套装)):
            位置 += 间隔
            适用套装名称 = QLabel(输出窗口)
            if len(套装件数[i]) > 0:
                适用套装名称.setText(套装[i] + '[' + str(max(套装件数[i])) + ']')
            else:
                适用套装名称.setText(套装[i])
            适用套装名称.move(132, 位置 - pox_y2)
            适用套装名称.resize(132, 18)
            适用套装名称.setAlignment(Qt.AlignCenter)
            if 套装[i] in 神话所在套装:
                适用套装名称.setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(226,150,146)}")
            else:
                适用套装名称.setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(255,255,255)}")
            适用套装名称.setToolTip(套装属性[i][:-4])

        合计力量 = 0
        合计智力 = 0
        合计物攻 = 0
        合计魔攻 = 0
        合计独立 = 0

        基准值合计力量 = 0
        基准值合计智力 = 0
        基准值合计物攻 = 0
        基准值合计魔攻 = 0
        基准值合计独立 = 0

        实际技能等级 = []
        for i in self.角色属性B.技能栏:
            实际技能等级.append(i.等级)

        if len(self.基准值) != 0:
            显示模式 = 1
        else:
            显示模式 = 0

        count = 0
        for i in range(len(self.角色属性B.技能栏)):
            if sum(统计详情[i]) != 0:
                count += 1

        self.行高 = 30
        if count > 0:
            self.行高 = min(int(440 / count), 30)
        j = -1


        for i in range(len(self.角色属性B.技能栏)):
            if sum(统计详情[i]) != 0:
                j += 1
                每行详情 = []
                for k in range(10):
                    每行详情.append(QLabel(输出窗口))

                # 图片
                每行详情[0].setPixmap(self.技能图片[i])
                每行详情[0].move(302, 50 + j * self.行高 - pox_y)
                每行详情[0].resize(28, min(28, self.行高 - 2))
                # 等级
                每行详情[1].setText('Lv.' + str(实际技能等级[i]))
                每行详情[1].move(337, 50 + j * self.行高 - pox_y)
                每行详情[1].resize(30, min(28, self.行高))
                if self.登记启用 and self.角色属性B.技能栏[i].名称 in ['禁忌诅咒', '死命召唤', '勇气祝福', '勇气圣歌', '荣誉祝福']:
                    统计详情[i] = 双切详情[i]
                    每行详情[1].setText('Lv.' + str(双切属性.技能栏[i].等级))
                
                for k in range(8):
                    详情 = str(统计详情[i][k])
                    if 显示模式 == 1:
                        详情 = self.对比输出(统计详情[i][k], self.基准值[1][i][k])
                    if 详情 == '0' or 详情 == 0:
                        详情 = ''                   
                    每行详情[k+2].setText(详情)
                    每行详情[k+2].move(370 + k * 40, 50 + j * self.行高 - pox_y)
                    每行详情[k+2].resize(50, min(28, self.行高))
               
                for l in range(1, 10):
                    if self.登记启用 and self.角色属性B.技能栏[i].名称 in ['禁忌诅咒', '死命召唤', '勇气祝福', '勇气圣歌', '荣誉祝福']:
                        每行详情[l].setStyleSheet(
                            "QLabel{font-size:12px;color:rgb(255,0,0)}")
                    else:
                        每行详情[l].setStyleSheet(
                            "QLabel{font-size:12px;color:rgb(255,255,255)}")
                    每行详情[l].setAlignment(Qt.AlignCenter)

        for i in range(len(self.角色属性B.技能栏)):
            if 显示模式 == 1:
                基准值合计力量 += self.基准值[1][i][3]
                基准值合计智力 += self.基准值[1][i][4]
                基准值合计物攻 += self.基准值[1][i][5]
                基准值合计魔攻 += self.基准值[1][i][6]
                基准值合计独立 += self.基准值[1][i][7]
            合计力量 += 统计详情[i][3]
            合计智力 += 统计详情[i][4]
            合计物攻 += 统计详情[i][5]
            合计魔攻 += 统计详情[i][6]
            合计独立 += 统计详情[i][7]
        tempstr = ''
        if 显示模式 == 1:
            对比力量 = self.对比输出(合计力量, 基准值合计力量, 0, 1)
            对比智力 = self.对比输出(合计智力, 基准值合计智力, 0, 1)
            对比物攻 = self.对比输出(合计物攻, 基准值合计物攻, 0, 1)
            对比魔攻 = self.对比输出(合计魔攻, 基准值合计魔攻, 0, 1)
            对比独立 = self.对比输出(合计独立, 基准值合计独立, 0, 1)
            if 对比力量 == 对比智力:
                tempstr += '力智' + 对比力量
            else:
                tempstr += '力量' + 对比力量
                tempstr += ',智力' + 对比智力

            if 对比物攻 == 对比魔攻 and 对比魔攻 == 对比独立:
                tempstr += ',三攻' + 对比物攻
            else:
                tempstr += ',物攻' + 对比物攻
                tempstr += ',魔攻' + 对比魔攻
                tempstr += ',独立' + 对比独立
        else:
            if 合计力量 == 合计智力:
                tempstr += '力智+' + str(合计力量)
            else:
                tempstr += '力量+' + str(合计力量)
                tempstr += ',智力+' + str(合计智力)

            if 合计物攻 == 合计魔攻 and 合计魔攻 == 合计独立:
                tempstr += ',三攻+' + str(合计物攻)
            else:
                tempstr += ',物攻+' + str(合计物攻)
                tempstr += ',魔攻+' + str(合计魔攻)
                tempstr += ',独立+' + str(合计独立)
            if self.角色属性B.切换详情 != '无':
                tempstr += '<br><br>' + self.角色属性B.切换详情

        if self.角色属性B.希洛克武器词条 == 1:
            武器词条最高值 = self.角色属性B.自适应最高值
            武器属性A = 武器属性A列表[武器词条最高值[0]]
            武器属性B = 武器属性B列表[武器词条最高值[1]]
            # tempstr += '<br><br>' + "属性1:" +"<font style='color:gray'>"+武器属性A.固定属性描述 + '</font>,' + 武器属性A.随机属性描述 + str(武器属性A.最大值)+ ('%' if 武器属性A.间隔 / 10 < 1 else '')
            tempstr += "<br><br>" + "残香 属性1:" + \
                       "<font style='color:gray'>" + 武器属性A.固定属性描述 + '</font>'
            if self.角色属性B.武器词条触发 == 1:
                # tempstr += "| 属性2:" +"<font style='color:gray'>"+武器属性B.固定属性描述 + '</font>,' + 武器属性B.随机属性描述 + str(武器属性B.最大值)+ ('%' if 武器属性B.间隔 / 10 < 1 else '')
                tempstr += " | 属性2:" + "<font style='color:gray'>" + 武器属性B.固定属性描述 + '</font>'

        if self.角色属性B.黑鸦词条[0][0] == 1 or self.角色属性B.黑鸦词条[1][
            0] == 1 or self.角色属性B.黑鸦词条[2][0] == 1 or self.角色属性B.黑鸦词条[3][
            0] == 1:
            tempstr += "<br><br>" + "遴选"
            if self.角色属性B.黑鸦词条[0][0] == 1:
                if self.角色属性B.武器变换属性自适应 > 0:
                    黑鸦武器 = 武器变换属性列表[self.角色属性B.武器变换属性自适应]
                    tempstr += " 武器:" + "<font style='color:gray'>" + 黑鸦武器.固定属性描述 + '</font>'
                else:
                    tempstr += " 武器:" + "<font style='color:gray'>" + '觉醒' + '</font>'
            if self.角色属性B.黑鸦词条[1][0] == 1:
                黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[0]]
                tempstr += " 戒指:" + "<font style='color:gray'>" + 黑鸦.固定属性描述 + '</font>'
            if self.角色属性B.黑鸦词条[2][0] == 1:
                黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[1]]
                tempstr += " 辅助:" + "<font style='color:gray'>" + 黑鸦.固定属性描述 + '</font>'
            if self.角色属性B.黑鸦词条[3][0] == 1:
                黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[2]]
                tempstr += " 下装:" + "<font style='color:gray'>" + 黑鸦.固定属性描述 + '</font>'

        合计 = QLabel(输出窗口)
        合计.setStyleSheet("QLabel{color:rgb(104,213,237);font-size:15px}")
        合计.setText(tempstr)
        if self.登记启用:
            合计.setStyleSheet("QLabel{color:rgb(104,213,237);font-size:12px}")
        合计.resize(450, 300)
        合计.move(280, 30 + j * self.行高 - pox_y2)
        合计.setAlignment(Qt.AlignCenter)

        初始x = 10
        初始y = 31

        图片列表 = self.获取装备图片(self.排行数据[index])

        提升率显示 = QLabel(输出窗口)

        提升率显示.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        if 显示模式 == 1:
            提升率显示.setText(self.对比输出(提升率, self.基准值[0], 1, 1))
        else:
            提升率显示.setText(str(round(提升率, 2)) + '%')
        提升率显示.resize(250, 36)
        提升率显示.move(10, 517 - pox_y2)
        提升率显示.setAlignment(Qt.AlignCenter)

        
        图片列表 = self.获取装备图片(self.排行数据[index])
        偏移量 = 187
        x坐标 = [
            32, 0, 0, 32, 0, 偏移量, 偏移量 + 32, 偏移量 + 32, 偏移量, 偏移量, 偏移量 + 32, 32
        ]
        y坐标 = [0, 0, 32, 32, 64, 0, 0, 32, 64, 32, 64, 64]

        tempstr = self.装备描述_BUFF计算(self.角色属性B)

        for i in range(12):
            x = 初始x + x坐标[i]
            y = 初始y + y坐标[i] - pox_y2
            装备图标 = QLabel(输出窗口)
            装备图标.setMovie(图片列表[i])
            装备图标.resize(26, 26)
            装备图标.move(x, y)
            装备图标.setAlignment(Qt.AlignCenter)
            装备 = equ.get_equ_by_name(self.角色属性B.装备栏[i])
            if self.角色属性B.装备栏[i] == 百变怪:
                图标遮罩 = QLabel(输出窗口)
                图标遮罩.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                图标遮罩.resize(26, 26)
                图标遮罩.move(x, y)
                图标遮罩.setToolTip(tempstr[i])
            else:
                装备图标.setToolTip(tempstr[i])
        
        for i in range(12):
            装备 = equ.get_equ_by_name(self.角色属性B.装备栏[i])
            打造状态 = QLabel(输出窗口)
            if 装备.所属套装 != '智慧产物':
                打造状态.setText('+' + str(self.角色属性B.强化等级[i]))
                if self.角色属性B.是否增幅[i] == 1:
                    打造状态.setStyleSheet(
                        "QLabel{color:rgb(228,88,169);font-size:12px;font-weight:Bold}"
                    )
                else:
                    打造状态.setStyleSheet(
                        "QLabel{color:rgb(25,199,234);font-size:12px;font-weight:Bold}"
                    )

            else:
                打造状态.setText('+' + str(self.角色属性B.改造等级[i]))
                打造状态.setStyleSheet(
                    "QLabel{color:rgb(249,141,62);font-size:12px;font-weight:Bold;}"
                )

            打造状态.move(初始x + x坐标[i] + 13, 初始y + y坐标[i] - 8 - pox_y2)

        装备 = equ.get_equ_by_name(self.角色属性B.装备栏[11])
        if 装备.所属套装 != '智慧产物' and self.角色属性B.武器锻造等级 != 0:
            打造状态 = QLabel(输出窗口)
            打造状态.setText('+' + str(self.角色属性B.武器锻造等级))
            打造状态.setStyleSheet(
                "QLabel{color:rgb(232,104,24);font-size:12px;font-weight:Bold}"
            )
            打造状态.move(初始x + x坐标[11] + 13, 初始y + y坐标[11] + 20 - pox_y2)

        if self.登记启用:
            #换装装备图表显示
            偏移量 = 80
            x坐标 = [
                32, 0, 0, 32, 0, 偏移量, 偏移量 + 32, 偏移量 + 32, 偏移量, 偏移量, 偏移量 + 32, 32
            ]
            y坐标 = [0, 0, 32, 32, 64, 0, 0, 32, 64, 32, 64, 64]
            图片列表2 = self.获取装备图片(换装装备)
            for i in range(12):
                x = 初始x + x坐标[i] + 600
                y = 初始y + y坐标[i] - pox_y2 + 150
                装备图标 = QLabel(输出窗口)
                装备图标.setMovie(图片列表2[i])
                装备图标.resize(26, 26)
                装备图标.move(x, y)
                装备图标.setAlignment(Qt.AlignCenter)
                if self.排行数据[index][i] == 换装装备[i]:
                    图标遮罩 = QLabel(输出窗口)
                    图标遮罩.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.8)}")
                    图标遮罩.resize(26, 26)
                    图标遮罩.move(x, y)


        输出显示 = MainWindow(输出窗口)
        self.输出窗口列表.append(输出显示)
        输出显示.show()

    def 装备描述_BUFF计算(self, property):
        tempstr = []
        数量 = [0] * 3
        for i in range(15):
            数量[i % 3] += self.希洛克选择状态[i]
        for i in range(12):
            装备 = equ.get_equ_by_name(property.装备栏[i])
            tempstr.append('<font size="3" face="宋体"><font color="' +
                           颜色[装备.品质] + '">' + 装备.名称 + '</font><br>')
            if 装备.所属套装 != '无':
                if 装备.所属套装 != '智慧产物':
                    y = ' ' + 装备.所属套装
                else:
                    try:
                        y = ' ' + 装备.所属套装2
                    except:
                        y = ' '
            else:
                y = ' '
            if i == 11:
                y += ' ' + 装备.类型
            tempstr[i] += 'Lv' + str(装备.等级) + ' ' + 装备.品质 + y

            if i < 5:
                x = property.防具精通计算(i)
                tempstr[i] += '<br>防具精通: '
                for n in property.防具精通属性:
                    if n != '体力':
                        tempstr[i] += n + ' +' + str(2 * x) + ' '
                    else:
                        tempstr[i] += n + ' +' + str(x) + ' '

            if 装备.所属套装 != '智慧产物':
                if property.强化等级[i] != 0:
                    if i in [9, 10]:
                        tempstr[i] += '<br><font color="#68D5ED">+' + str(
                            property.强化等级[i]) + ' 强化: '
                        tempstr[i] += '四维 + ' + str(
                            左右计算(100, 装备.品质, property.强化等级[i])) + '</font>'

                if property.武器锻造等级 != 0:
                    if i == 11:
                        tempstr[i] += '<br><font color="#68D5ED">+' + str(
                            property.武器锻造等级) + '   锻造: '
                        tempstr[i] += '四维 + ' + str(
                            锻造四维(装备.等级, 装备.品质, property.武器锻造等级)) + '</font>'

                if property.是否增幅[i] == 1:
                    if tempstr[i] != '':
                        tempstr[i] += '<br>'
                    tempstr[i] += '<font color="#FF00FF">+' + str(
                        property.强化等级[i]) + ' 增幅: '
                    if '体力' in property.类型:
                        tempstr[i] += '异次元体力 + ' + str(
                            增幅计算(装备.等级, 装备.品质, property.强化等级[i],
                                 property.增幅版本)) + '</font>'
                    elif '精神' in property.类型:
                        tempstr[i] += '异次元精神 + ' + str(
                            增幅计算(装备.等级, 装备.品质, property.强化等级[i],
                                 property.增幅版本)) + '</font>'
                    elif '智力' in property.类型:
                        tempstr[i] += '异次元智力 + ' + str(
                            增幅计算(装备.等级, 装备.品质, property.强化等级[i],
                                 property.增幅版本)) + '</font>'

            if tempstr[i] != '':
                tempstr[i] += '<br>'
            if 装备.所属套装 != '智慧产物':
                if i == 2 and property.黑鸦词条[3][0] != 0:
                    tempstr[i] += 装备.装备描述_变换属性_BUFF(property)
                    if property.黑鸦词条[3][0] == 1:
                        tempstr[i] += self.黑鸦属性描述(
                            property.防具变换属性自适应[2], 装备变换属性列表[property.防具变换属性自适应[2]].最大值, 1)
                    else:
                        tempstr[i] += self.黑鸦属性描述(property.黑鸦词条[3][1], property.黑鸦词条[3][2],
                                                  1)
                    # 下装
                elif i == 7 and property.黑鸦词条[1][0] != 0:
                    tempstr[i] += 装备.装备描述_变换属性_BUFF(property)
                    if property.黑鸦词条[1][0] == 1:
                        tempstr[i] += self.黑鸦属性描述(
                            property.防具变换属性自适应[0], 装备变换属性列表[property.防具变换属性自适应[0]].最大值, 1)
                    else:
                        tempstr[i] += self.黑鸦属性描述(property.黑鸦词条[1][1], property.黑鸦词条[1][2],
                                                  1)
                    # 戒指
                elif i == 9 and property.黑鸦词条[2][0] != 0:
                    tempstr[i] += 装备.装备描述_变换属性_BUFF(property)
                    if property.黑鸦词条[2][0] == 1:
                        tempstr[i] += self.黑鸦属性描述(
                            property.防具变换属性自适应[1], 装备变换属性列表[property.防具变换属性自适应[0]].最大值, 1)
                    else:
                        tempstr[i] += self.黑鸦属性描述(property.黑鸦词条[2][1], property.黑鸦词条[2][2],
                                                  1)
                    # 辅助
                elif i == 11 and property.黑鸦词条[0][0] != 0:
                    tempstr[i] += 装备.装备描述_变换属性_BUFF(property)
                    if property.黑鸦词条[0][0] == 3 and not 装备.名称 == '世界树之精灵':
                        tempstr[i] += 'Lv50 技能等级+2<br>'
                        tempstr[i] += 'Lv85 技能等级+2<br>'
                        tempstr[i] += 'Lv100 技能等级+2<br>'
                    elif property.黑鸦词条[0][0] == 2:
                        tempstr[i] += self.黑鸦属性描述(property.黑鸦词条[0][1], property.黑鸦词条[0][2])
                        if 装备.名称 == '世界树之精灵':
                            tempstr[i] = tempstr[i].replace(
                                'Lv50 技能等级+2<br>', '')
                            tempstr[i] = tempstr[i].replace(
                                'Lv85 技能等级+2<br>', '')
                            tempstr[i] = tempstr[i].replace(
                                'Lv100 技能等级+2<br>', '')
                    # 世界树之精灵特殊处理,没考虑择优的时候,针对的是自选
                    if 装备.名称 == '世界树之精灵' and property.黑鸦词条[0][0] > 1:
                        tempstr[i] += 'Lv50 技能等级+2<br>'
                    if property.黑鸦词条[0][0] == 1:
                        if property.武器变换属性自适应 == 0:
                            tempstr[i] += 'Lv50 技能等级+2<br>'
                            tempstr[i] += 'Lv85 技能等级+2<br>'
                            tempstr[i] += 'Lv100 技能等级+2<br>'
                        else:
                            tempstr[i] += self.黑鸦属性描述(
                                property.武器变换属性自适应, 装备变换属性列表[property.武器变换属性自适应].最大值, 1)
                        if 装备.名称 == '世界树之精灵':
                            tempstr[i] += 'Lv50 技能等级+2<br>'
                # 武器
            else:
                tempstr[i] += 装备.装备描述_BUFF(property)

            if 数量[0] == 1 and i == 2:
                # tempstr[i]+='<br>'
                tempstr[i] += '<font color="#00A2E8">希洛克融合属性:</font><br>'
                tempstr[i] += 'Lv30 Buff技能 力量、智力增加量 +3%'
            elif 数量[1] == 1 and i == 7:
                # tempstr[i]+='<br>'
                tempstr[i] += '<font color="#00A2E8">希洛克融合属性:</font><br>'
                tempstr[i] += 'Lv50主动技能力量、智力增加量 +3%'
            elif 数量[2] == 1 and i == 9:
                # tempstr[i]+='<br>'
                tempstr[i] += '<font color="#00A2E8">希洛克融合属性:</font><br>'
                tempstr[i] += '[守护恩赐]体力、精神 +80<br>'
                tempstr[i] += '[启示:圣歌]、[人偶操纵者]智力 +80'

            elif self.角色属性B.希洛克武器词条 == 1 and i == 11:
                # tempstr[i]+='<br>'
                tempstr[i] += '<font color="#00A2E8">希洛克融合属性:</font><br>'
                武器词条最高值 = self.角色属性B.自适应最高值
                武器属性A = 武器属性A列表[武器词条最高值[0]]
                武器属性B = 武器属性B列表[武器词条最高值[1]]
                tempstr[
                    i] += "属性1:" + "<font style='color:gray'>" + 武器属性A.固定属性描述 + '</font>,' + 武器属性A.随机属性描述 + str(
                    武器属性A.最大值) + ('%'
                                  if 武器属性A.间隔 / 10 < 1 else '') + '<br>'
                if self.角色属性B.武器词条触发 == 1:
                    tempstr[
                        i] += "属性2:" + "<font style='color:gray'>" + 武器属性B.固定属性描述 + '</font>,' + 武器属性B.随机属性描述 + str(
                        武器属性B.最大值) + ('%' if 武器属性B.间隔 / 10 < 1 else
                                      '') + '<br>'
            elif self.角色属性B.希洛克武器词条 == 2 and i == 11:
                # tempstr[i]+='<br>'
                tempstr[i] += '<font color="#00A2E8">希洛克融合属性:</font><br>'
                武器属性A = 武器属性A列表[self.武器融合属性A.currentIndex()]
                武器属性B = 武器属性B列表[self.武器融合属性B.currentIndex()]
                tempstr[
                    i] += "属性1:" + "<font style='color:gray'>" + 武器属性A.固定属性描述 + '</font>,' + 武器属性A.随机属性描述 + self.武器融合属性A2.currentText(
                ) + '<br>'
                if self.角色属性B.武器词条触发 == 1:
                    tempstr[
                        i] += "属性2:" + "<font style='color:gray'>" + 武器属性B.固定属性描述 + '</font>,' + 武器属性B.随机属性描述 + self.武器融合属性B2.currentText(
                    ) + '<br>'
            # elif self.希洛克武器词条[0].currentIndex() > 0 and i == 11:
            #     tempstr[i]+='<br>'
            #     tempstr[i]+='<font color="#00A2E8">希洛克融合属性:</font><br>'
            #     if self.希洛克武器词条[0].currentIndex() == 1:
            #         tempstr[i]+="属性1:{} +10%<br>".format(武器词条属性[属性.词条选择[0]])
            #         if sum(数量)==3:
            #             tempstr[i]+="属性2:{} +5%<br>".format(武器词条属性[属性.词条选择[1]])
            #     else:
            #         tempstr[i]+="属性1:{} +{}%<br>".format(武器词条属性[self.希洛克武器词条[1].currentIndex()],(self.希洛克武器词条[3].currentIndex() + 3) * 2)
            #         if sum(数量)==3:
            #             tempstr[i]+="属性2:{} +{}%<br>".format(武器词条属性[self.希洛克武器词条[2].currentIndex()],(self.希洛克武器词条[4].currentIndex() + 3) * 1)
            if tempstr[i].endswith('<br>'):
                tempstr[i] = tempstr[i][:-4]
            tempstr[i] += '</font>'
        return tempstr

    def 黑鸦属性描述(self, index, value, x=0):
        tempstr = ''
        if x == 0:
            武器属性 = 武器变换属性列表[index]
            tempstr += "<font style='color:gray'>" + 武器属性.固定属性描述 + '</font>,' + 武器属性.随机属性描述 + str(
                value) + ('%' if 武器属性.间隔 / 10 < 1 else '') + '<br>'
        else:
            装备属性 = 装备变换属性列表[index]
            tempstr += "<font style='color:gray'>" + 装备属性.固定属性描述 + '</font>,' + 装备属性.随机属性描述 + str(
                value) + ('%' if 装备属性.间隔 / 10 < 1 else '') + '<br>'
        return tempstr

    def 武器融合属性计算(self, 属性):
        武器融合属性A = 武器属性A列表[self.武器融合属性A.currentIndex()]
        武器融合属性B = 武器属性B列表[self.武器融合属性B.currentIndex()]
        武器融合属性A数值 = self.武器融合属性A2.currentText().replace('%', '')
        武器融合属性B数值 = self.武器融合属性B2.currentText().replace('%', '')
        武器融合属性A.当前值 = int(武器融合属性A数值 if 武器融合属性A数值 != '' else 0)
        武器融合属性A.融合属性(属性)
        if 属性.武器词条触发 == 1:
            武器融合属性B.当前值 = int(武器融合属性B数值 if 武器融合属性B数值 != '' else 0)
            武器融合属性B.融合属性(属性)

    def 黑鸦属性计算(self, 属性):
        for i in range(4):
            if self.黑鸦词条[i][0].currentIndex() == 2:
                if i == 0:
                    武器属性 = 武器变换属性列表[self.黑鸦词条[i][1].currentIndex()]
                    武器属性数值 = self.黑鸦词条[i][3].currentText().replace('%', '')
                    武器属性.当前值 = int(武器属性数值 if 武器属性数值 != '' else 0)
                    武器属性.变换属性(属性)
                else:
                    装备属性 = 装备变换属性列表[self.黑鸦词条[i][1].currentIndex()]
                    装备属性数值 = self.黑鸦词条[i][3].currentText().replace('%', '')
                    装备属性.当前值 = int(装备属性数值 if 装备属性数值 != '' else 0)
                    装备属性.变换属性(属性)

    def 希洛克属性计算(self, 属性):
        数量 = [0] * 3
        for i in range(15):
            数量[i % 3] += self.希洛克选择状态[i]

        # 下装属性1
        if 数量[0] == 1:
            属性.BUFF力量per *= 1.03
            属性.BUFF智力per *= 1.03

        # 戒指属性1
        if 数量[1] == 1:
            属性.一觉力智per *= 1.03

        # 辅助装备属性1
        if 数量[2] == 1:
            属性.守护恩赐体精 += 80
            属性.转职被动智力 += 80

        i = 0  # 奈克斯属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.一觉力智 += 40
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.被动进图加成 += 80
            # 属性.守护恩赐体精 += 80
            # 属性.转职被动智力 += 80  # 戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.BUFF物攻per *= 1.02
            属性.BUFF魔攻per *= 1.02
            属性.BUFF独立per *= 1.02  # 辅助装备

        i = 1  # 暗杀者属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.一觉力智 += 28
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.被动进图加成 += 55
            # 属性.守护恩赐体精 += 55
            # 属性.转职被动智力 += 55  # 戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.BUFF物攻per *= 1.01
            属性.BUFF魔攻per *= 1.01
            属性.BUFF独立per *= 1.01
            属性.BUFF力量per *= 1.01
            属性.BUFF智力per *= 1.01  # 辅助装备

        i = 2  # 卢克西属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            pass  # 下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            pass  # 戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            pass  # 辅助装备

        i = 3  # 守门人属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.一觉力智per *= 1.01
            属性.一觉力智 += 20
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.被动进图加成 += 55
            # 属性.守护恩赐体精 += 55
            # 属性.转职被动智力 += 55  # 戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.BUFF力量per *= 1.01
            属性.BUFF智力per *= 1.01
            属性.被动进图加成 += 30
            # 属性.守护恩赐体精 += 30
            # 属性.转职被动智力 += 30  # 辅助装备

        i = 4  # 洛多斯属性2
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            属性.一觉力智per *= 1.02  # 下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            属性.BUFF力量per *= 1.02
            属性.BUFF智力per *= 1.02  # 戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            属性.BUFF物攻per *= 1.01
            属性.BUFF魔攻per *= 1.01
            属性.BUFF独立per *= 1.01
            属性.被动进图加成 += 30
            # 属性.守护恩赐体精 += 30
            # 属性.转职被动智力 += 30  # 辅助装备

    def 奥兹玛属性计算(self, 属性):
        # region 阿斯特罗斯
        for i in range(0,4):
            if self.奥兹玛选择状态[i] == 1:
                属性.BUFF增加(BUFF物攻per=1.01, BUFF魔攻per=1.01, BUFF独立per=1.01)
                属性.觉醒增加(一觉力智=22)
                属性.被动增加(守护恩赐体精=55, 转职被动智力=55)
        # endregion
        # region 贝利亚斯
        for i in range(5,9):
            if self.奥兹玛选择状态[i] == 1:
                属性.被动增加(守护恩赐体精=138, 转职被动智力=138)
        # endregion
        # region 雷德梅恩
        for i in range(10,14):
            if self.奥兹玛选择状态[i] == 1:
                属性.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)
                属性.觉醒增加(一觉力智=25)
                属性.被动增加(守护恩赐体精=46, 转职被动智力=46)
        # endregion
        # region 罗什巴赫
        for i in range(15,19):
            if self.奥兹玛选择状态[i] == 1:
                属性.BUFF增加(BUFF力量per=1.01, BUFF智力per=1.01)
                属性.BUFF增加(BUFF物攻per=1.01, BUFF魔攻per=1.01, BUFF独立per=1.01)
                属性.觉醒增加(一觉力智=37)
        # endregion
        # region 泰玛特
        for i in range(20,24):
            if self.奥兹玛选择状态[i] == 1:
                属性.BUFF增加(BUFF力量per=1.03, BUFF智力per=1.03)
                属性.觉醒增加(一觉力智=21, 一觉力智per=1.01)
        # endregion

    def 输入属性(self, 属性, x=0):
        for i in 属性.技能栏:
            i.等级 = i.基础等级 + int(self.等级调整[self.角色属性A.技能序号[i.名称]].currentText())

        属性.排行系数 = self.排行参数.currentIndex()
        属性.C力智 = int(''.join(filter(str.isdigit, self.排行选项[0].currentText())))
        属性.C三攻 = int(''.join(filter(str.isdigit, self.排行选项[1].currentText())))

        # if ':' in self.排行选项[0].currentText():
        #     属性.C力智 = int(self.排行选项[0].currentText().split(':')[1])
        # else:
        #     属性.C力智 = int(self.排行选项[0].currentText())
        # if ':' in self.排行选项[1].currentText():
        #     属性.C三攻 = int(self.排行选项[1].currentText().split(':')[1])
        # else:
        #     属性.C三攻 = int(self.排行选项[1].currentText())
        属性.排行类型 = self.排行选项[2].currentText()

        if self.排行选项[3].currentIndex() == 0:
            pass
        elif self.排行选项[3].currentIndex() == 1:
            属性.系统奶系数 = 1.35
            属性.系统奶基数 = 7664
        elif self.排行选项[3].currentIndex() == 2:
            属性.系统奶系数 = 2.31
            属性.系统奶基数 = 4581

        if self.初始属性.三觉序号 != 0:
            if self.觉醒选择状态 == 1:
                属性.技能栏[self.三觉序号].关联技能 = [属性.技能栏[self.一觉序号].名称]
            elif self.觉醒选择状态 == 2:
                属性.技能栏[self.三觉序号].关联技能 = [属性.技能栏[self.二觉序号].名称]

        if self.切装模式选项.isChecked() and self.计算模式选择.currentIndex() != 2:
            属性.双装备模式 = 1

        count = 0
        for i in equ.get_equ_list():
            if i.品质 == '神话':
                i.属性1选择_BUFF = self.神话属性选项[count * 4 + 0].currentIndex()
                i.属性2选择_BUFF = self.神话属性选项[count * 4 + 1].currentIndex()
                i.属性3选择_BUFF = self.神话属性选项[count * 4 + 2].currentIndex()
                i.属性4选择_BUFF = self.神话属性选项[count * 4 + 3].currentIndex()
                count += 1

        if x == 0:
            self.辟邪玉属性计算(属性)

        if sum(self.希洛克选择状态) == 3:
            属性.武器词条触发 = 1

        if self.希洛克武器选择.currentIndex() == 1:
            属性.希洛克武器词条 = 1
        if self.希洛克武器选择.currentIndex() == 2:
            属性.希洛克武器词条 = 2
            self.武器融合属性计算(属性)

        for i in range(len(self.复选框列表)):
            if self.复选框列表[i].isChecked():
                选项设置列表[i].适用效果(属性)

        称号列表[self.称号.currentIndex()].城镇属性_BUFF(属性)
        if 属性.称号触发:
            称号列表[self.称号.currentIndex()].触发属性(属性)

        宠物列表[self.宠物.currentIndex()].城镇属性_BUFF(属性)

        if self.护石第一栏.currentText() != '无':
            属性.护石第一栏 = self.护石第一栏.currentText()

        if self.护石第二栏.currentText() != '无':
            属性.护石第二栏 = self.护石第二栏.currentText()

        if self.护石第三栏.currentText() != '无':
            属性.护石第三栏 = self.护石第三栏.currentText()

        for i in range(12):
            属性.是否增幅[i] = self.装备打造选项[i].currentIndex()
            属性.强化等级[i] = self.装备打造选项[i + 12].currentIndex()
            属性.改造等级[i] = self.装备打造选项[i + 24].currentIndex()
        属性.武器锻造等级 = self.装备打造选项[36].currentIndex()
        属性.类型 = self.装备打造选项[37].currentText()
        属性.次数输入.clear()
        self.是否计算 = 1
        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            temp = self.角色属性A.一觉序号
            if 序号 == self.角色属性A.一觉序号 or 序号 == self.角色属性A.三觉序号:
                if self.次数输入[序号].currentIndex() == 2:
                    if self.次数输入[序号].currentText() != '':
                        try:
                            temp1 = int(float(self.次数输入[序号].currentText()))
                            temp2 = (float(self.次数输入[序号].currentText()))
                            if temp1 >= 0 and temp1 < 1000:
                                if temp1 == temp2:
                                    属性.次数输入.append(
                                        int(float(
                                            self.次数输入[序号].currentText())))
                                else:
                                    属性.次数输入.append(
                                        int((float(self.次数输入[序号].currentText())
                                             + 0.001) * 100) / 100)
                                    self.次数输入[序号].setCurrentText(
                                        str(
                                            int((float(
                                                self.次数输入[序号].currentText()) +
                                                 0.001) * 100) / 100))
                            else:
                                QMessageBox.information(
                                    self, "错误",
                                    "“" + i.名称 + "”" + "技能次数超出取值范围,请重新输入")
                                self.是否计算 = 0
                                break
                        except:
                            QMessageBox.information(
                                self, "错误",
                                "“" + i.名称 + "”" + "技能次数输入格式错误,请重新输入")
                            self.是否计算 = 0
                            break
                    else:
                        QMessageBox.information(
                            self, "错误", "“" + i.名称 + "”" + "技能次数输入为空,请重新输入")
                        self.是否计算 = 0
                        break
                else:
                    属性.次数输入.append(int(self.次数输入[序号].currentText()))
            else:
                属性.次数输入.append(int(self.次数输入[序号].currentText()))
        self.黑鸦属性计算(属性)
        self.希洛克属性计算(属性)
        self.奥兹玛属性计算(属性)
        self.基础属性(属性)
        属性.黑鸦词条 = []
        for i in range(4):
            temp = [
                self.黑鸦词条[i][0].currentIndex(),
                self.黑鸦词条[i][1].currentIndex(),
                self.黑鸦词条[i][3].currentText(),
            ]
            属性.黑鸦词条.append(temp)

    def 技能加成判断(self, name, 属性):
        if name == 'Lv1-30(主动)Lv+1':
            属性.技能等级加成('主动', 1, 30, 1)
            return
        if name == 'Lv1-50(主动)Lv+1':
            属性.技能等级加成('主动', 1, 50, 1)
            return
        if name == 'Lv1-35(主动)Lv+1':
            属性.技能等级加成('主动', 1, 35, 1)
            return
        if name == 'Lv30-50(主动)Lv+1':
            属性.技能等级加成('主动', 30, 50, 1)
            return
        if name == 'Lv1-30(所有)Lv+1':
            属性.技能等级加成('所有', 1, 30, 1)
            return
        if name == 'Lv1-50(所有)Lv+1':
            属性.技能等级加成('所有', 1, 50, 1)
            return
        if name == 'Lv1-20(所有)Lv+1':
            属性.技能等级加成('所有', 1, 20, 1)
            return
        if name == 'Lv20-30(所有)Lv+1':
            属性.技能等级加成('所有', 20, 30, 1)
            return
        if name == 'Lv1-80(所有)Lv+1':
            属性.技能等级加成('所有', 1, 80, 1)
            return

        if name == '一觉Lv+1':
            属性.一觉Lv += 1
            return
        if name == '一觉Lv+2':
            属性.一觉Lv += 2
            return
        if name == 'BUFFLv+1':
            属性.BUFFLv += 1
            return
        if name == 'BUFFLv+2':
            属性.BUFFLv += 2
            return
        if name == 'BUFFLv+3':
            属性.BUFFLv += 3
            return
        if name == 'BUFFLv+4':
            属性.BUFFLv += 4
            return
        for i in 属性.技能栏:
            if name == i.名称 + 'Lv+1':
                i.等级加成(1)
                return
        if name == 'BUFF力智+3%':
            属性.BUFF增加(BUFF力量per=1.03, BUFF智力per=1.03)
        if name == 'BUFF三攻+3%':
            属性.BUFF增加(BUFF物攻per=1.03, BUFF魔攻per=1.03, BUFF独立per=1.03)
        if name == 'BUFF力智、三攻+3%':
            属性.BUFF增加(BUFF力量per=1.03,
                      BUFF智力per=1.03,
                      BUFF物攻per=1.03,
                      BUFF魔攻per=1.03,
                      BUFF独立per=1.03)

    def 基础属性(self, 属性):
        for i in range(3):
            for j in range(16):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except:
                        QMessageBox.information(
                            self, "错误", self.行名称[j + 17 if i > 2 else j] +
                                        ":" + self.列名称[i] + "  输入格式错误,已重置为空")
                        self.属性设置输入[i][j].setText('')
        for i in range(3, 9):
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except:
                        QMessageBox.information(
                            self, "错误", self.行名称[j + 17 if i > 2 else j] +
                                        ":" + self.列名称[i] + "  输入格式错误,已重置为空")
                        self.属性设置输入[i][j].setText('')

        temp = []
        for j in range(len(self.属性设置输入[9])):

            if self.属性设置输入[9][j].text() != '' and j in [1, 2, 5]:
                try:
                    temp.append(float(self.属性设置输入[9][j].text()) / 100)

                    if temp[-1] > 1 or temp[-1] < -.2:
                        QMessageBox.information(
                            self, "错误",
                            self.修正列表名称[j] + " 输入数值超出[-20,100],已重置为空")
                        temp[-1] = 0.0
                        self.属性设置输入[9][j].setText('')
                except:
                    temp.append(0.0)
                    QMessageBox.information(self, "错误",
                                            self.修正列表名称[j] + " 输入格式错误,已重置为空")
                    self.属性设置输入[9][j].setText('')
            elif self.属性设置输入[9][j].text() != '' and j in [0, 3, 4, 6]:
                try:
                    temp.append(int(self.属性设置输入[9][j].text()))
                except:
                    temp.append(0.0)
                    QMessageBox.information(self, "错误",
                                            self.修正列表名称[j] + " 输入格式错误,已重置为空")
                    self.属性设置输入[9][j].setText('')
            else:
                temp.append(0.0)
        # 神话补正
        if 属性.类型 == '智力':
            属性.转职被动智力 += int(temp[0])
            属性.BUFF力量per *= 1 + temp[1]
            属性.BUFF智力per *= 1 + temp[1]
            属性.BUFF物攻per *= 1 + temp[2]
            属性.BUFF魔攻per *= 1 + temp[2]
            属性.BUFF独立per *= 1 + temp[2]
            属性.转职被动Lv += int(temp[3])
            属性.一觉被动力智 += int(temp[4])
            属性.一觉力智per *= 1 + temp[5]
            属性.一觉力智 += int(temp[6])
        else:
            属性.守护恩赐体精 += int(temp[0])
            属性.BUFF力量per *= 1 + temp[1]
            属性.BUFF智力per *= 1 + temp[1]
            属性.BUFF物攻per *= 1 + temp[2]
            属性.BUFF魔攻per *= 1 + temp[2]
            属性.BUFF独立per *= 1 + temp[2]
            属性.转职被动Lv += int(temp[3])
            属性.信念光环体精 += int(temp[4])
            属性.一觉力智per *= 1 + temp[5]
            属性.一觉力智 += int(temp[6])
        for i in [0, 3, 6]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 3 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 0 and j in [1, 9, 16]:
                        属性.进图智力 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.智力 += int(self.属性设置输入[i][j].text())
            for j in range(17, 19):
                if self.属性设置输入[i][j].text() != '':
                    属性.BUFF补正力智 += int(self.属性设置输入[i][j].text())
        for i in [1, 4, 7]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 4 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 1 and j in [1, 9, 16]:
                        属性.进图体力 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.体力 += int(self.属性设置输入[i][j].text())
            for j in range(17, 19):
                if self.属性设置输入[i][j].text() != '':
                    属性.BUFF补正体力 += int(self.属性设置输入[i][j].text())
        for i in [2, 5, 8]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 5 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 2 and j in [1, 9, 16]:
                        属性.进图精神 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.精神 += int(self.属性设置输入[i][j].text())
            for j in range(17, 19):
                if self.属性设置输入[i][j].text() != '':
                    属性.BUFF补正精神 += int(self.属性设置输入[i][j].text())
        for i in self.技能设置输入:
            self.技能加成判断(i.currentText(), 属性)

        属性.护石计算(属性.护石第一栏)
        属性.护石计算(属性.护石第二栏)
        属性.护石计算(属性.护石第三栏)
