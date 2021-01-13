from PublicReference.equipment.equ_list import *
from PublicReference.equipment.称号_buff import *
from PublicReference.equipment.宠物_buff import *
from PublicReference.equipment.辟邪玉_buff import *
from PublicReference.equipment.武器融合_buff import *
from PublicReference.choise.选项设置_buff import *
from PublicReference.common import *


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
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

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
    
    def 体精固定加成(self,x=0,y=0):
        if self.装备描述 == 1:
            return '体力、精神 +{}<br>'.format(x)
        else:
             self.体力 += x 
             self.精神 += x
        return ''    
    

    def BUFF增加(self,BUFFLv=0,BUFF力量=0,BUFF智力=0,BUFF力量per=1,BUFF智力per=1,BUFF物攻=0,BUFF魔攻=0,BUFF独立=0,BUFF物攻per=1,BUFF魔攻per=1,BUFF独立per=1):
        if self.装备描述 == 1: 
            tem = ''
            if BUFFLv > 0:
                if self.角色 == '圣职者(女)':
                    tem += '[勇气祝福]技能Lv +{}<br>'.format(int(BUFFLv))
                elif self.角色 == '圣职者(男)':
                    tem += '[荣誉祝福]技能Lv +{}<br>'.format(int(BUFFLv))
                elif self.角色 == '魔法师(女)':
                    tem += '[禁忌诅咒]技能Lv +{}<br>'.format(int(BUFFLv))

            if BUFF力量 >0 and BUFF智力 > 0:
                tem += 'Lv30 Buff技能力量、智力增加量 +{}<br>'.format(int(BUFF力量))
            elif BUFF力量 > 0:
                tem += 'Lv30 Buff技能力量增加量 +{}<br>'.format(int(BUFF力量))
            elif BUFF智力 > 0:
                tem += 'Lv30 Buff技能智力增加量 +{}<br>'.format(int(BUFF智力))

            if BUFF力量per > 1 and BUFF智力per > 1:
                tem += 'Lv30 Buff技能力智增加量 +{}%<br>'.format(round((BUFF力量per - 1) * 100,0))
            elif BUFF力量per > 1:
                tem += 'Lv30 Buff技能力量增加量 +{}%<br>'.format(round((BUFF力量per - 1) * 100,0))
            elif BUFF智力per > 1:
                tem += 'Lv30 Buff技能智力增加量 +{}%<br>'.format(round((BUFF智力per - 1) * 100,0))

            if BUFF物攻 > 0 and BUFF魔攻 > 0 and BUFF独立 > 0:
                tem += 'Lv30 Buff技能三攻攻击力增加量 +{}<br>'.format(int(BUFF物攻))
            elif BUFF物攻 > 0:
                tem += 'Lv30 Buff技能物理攻击力增加量 +{}<br>'.format(int(BUFF物攻))
            elif BUFF魔攻 > 0:
                tem += 'Lv30 Buff技能魔法攻击力增加量 +{}<br>'.format(int(BUFF魔攻)) 
            elif BUFF独立 > 0:
                tem += 'Lv30 Buff技能独立攻击力增加量 +{}<br>'.format(int(BUFF独立))

            if BUFF物攻per > 1 and BUFF魔攻per > 1 and BUFF独立per > 1:
                tem += 'Lv30 Buff技能三攻攻击力增加量 +{}%<br>'.format(round((BUFF物攻per - 1) * 100,0))
            elif BUFF物攻per > 1:
                tem += 'Lv30 Buff技能物理攻击力增加量 +{}%<br>'.format(round((BUFF物攻per - 1) * 100,0))
            elif BUFF魔攻per > 1:
                tem += 'Lv30 Buff技能魔法攻击力增加量 +{}%<br>'.format(round((BUFF魔攻per - 1) * 100,0)) 
            elif BUFF独立per > 1:
                tem += 'Lv30 Buff技能独立攻击力增加量 +{}%<br>'.format(round((BUFF独立per - 1) * 100,0))
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

    def 被动增加(self,守护恩赐Lv=0,守护恩赐体精=0,转职被动Lv=0,转职被动智力=0,信念光环Lv=0,信念光环体精=0,一觉被动Lv=0,一觉被动力智=0):
        if self.装备描述 == 1:
            tem = ''
            if 守护恩赐Lv > 0 or 转职被动Lv > 0:
                tem += '[守护恩赐]、[启示：圣歌]、[人偶操纵者]技能Lv +{}<br>'.format(int(守护恩赐Lv if 守护恩赐Lv else 转职被动Lv))
            elif 守护恩赐体精 > 0 and self.角色 == '圣职者(男)':
                tem += '[守护恩赐]体力、精神 +{}<br>'.format(int(守护恩赐体精))
            elif 转职被动智力 > 0 and self.角色 == '圣职者(女)':
                tem += '[启示：圣歌]智力 +{}<br>'.format(int(转职被动智力))
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

    def 觉醒增加(self,一觉Lv=0,一觉力智=0,一觉力智per=1):
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
                tem += 'Lv50 主动技能力量、智力增加量 +{}%<br>'.format(round((一觉力智per - 1) * 100,0))
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
        temp = 装备列表[装备序号[self.装备栏[i]]]
        if temp.所属套装 != '智慧产物':
            return 精通体力(temp.等级, temp.品质, self.强化等级[i],部位列表[i])
        else:
            return 精通体力(temp.等级, temp.品质, self.改造等级[i], 部位列表[i])

    def 装备基础(self):
        if 装备列表[装备序号[self.装备栏[0]]].品质 == '神话':
            self.智力 += 神话上衣额外智力
            self.体力 += 神话上衣额外体力
            self.精神 += 神话上衣额外精神
        for i in [0,1,2,3,4]:
            #精通
            temp = 装备列表[装备序号[self.装备栏[i]]]
            x = self.防具精通计算(i)
            if '智力' in self.防具精通属性:
                self.智力 += x * 2
            if '体力' in self.防具精通属性:
                self.体力 += x
            if '精神' in self.防具精通属性:
                self.精神 += x * 2
            #装备属性
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
            
        for i in [9,10]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            if temp.所属套装 != '智慧产物':
                x = 左右计算(temp.等级, temp.品质, self.强化等级[i])
                self.智力 += x
                self.体力 += x
                self.精神 += x
        for i in range(0,12):
            temp = 装备列表[装备序号[self.装备栏[i]]]
            if self.是否增幅[i] and temp.所属套装 != '智慧产物':
                x = 增幅计算(temp.等级, temp.品质,self.强化等级[i],self.增幅版本)
                if '智力' in self.类型:
                    self.智力 += x
                if '体力' in self.类型:
                    self.体力 += x
                if '精神' in self.类型:
                    self.精神 += x
        for i in [5,6,7,8,9,10]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            self.智力 += temp.智力
            self.体力 += temp.体力
            self.精神 += temp.精神
     
        temp = 装备列表[装备序号[self.装备栏[11]]]
        if temp.所属套装 != '智慧产物':
            四维 = 锻造四维(temp.等级,temp.品质,self.武器锻造等级)
            self.智力 += temp.智力 + 四维
            self.体力 += temp.体力 + 四维
            self.精神 += temp.精神 + 四维


    def 技能等级加成(self, 加成类型, min, max, lv,可变 = 0):
        lv = int(lv)
        if self.装备描述 ==1:
            if 加成类型=="所有":
                if min == max:
                    return "Lv{} 技能等级+{}<br>".format(min,lv)
                else:
                    return "Lv{}-{} 技能等级+{}<br>".format(min,max,lv)
            else:
                if min == max:
                    return "Lv{} 主动技能等级+{}<br>".format(min,lv)
                else:
                    return "Lv{}-{} 主动技能等级+{}<br>".format(min,max,lv) 
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

    def 提升率计算(self, 总数据, x = 0):
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

        x1 = (self.C力智 + (self.C力智 - 950) * 1.35 + 7664) * self.C三攻

        if self.排行类型 == '物理百分比':
            x2  = (self.C力智 + (self.C力智 - 950) * 1.35 + 7664 + 力量合计) * (self.C三攻 + 物攻合计)
        elif self.排行类型 == '魔法百分比':
            x2  = (self.C力智 + (self.C力智 - 950) * 1.35 + 7664 + 智力合计) * (self.C三攻 + 魔攻合计)
        elif self.排行类型 == '物理固伤':
            x2  = (self.C力智 + (self.C力智 - 950) * 1.35 + 7664 + 力量合计) * (self.C三攻 + 独立合计)
        elif self.排行类型 == '魔法固伤':
            x2  = (self.C力智 + (self.C力智 - 950) * 1.35 + 7664 + 智力合计) * (self.C三攻 + 独立合计) 
        
        return [x2 / x1 * 100, int(self.站街系数), 力量合计, 智力合计, 物攻合计, 魔攻合计, 独立合计][x]

    def 适用数值计算(self):
        self.专属词条计算()
        for i in range(len(self.技能栏)):
            if  self.次数输入[i] == '1':
                self.智力 += self.技能栏[i].结算统计()[0]
                self.体力 += self.技能栏[i].结算统计()[1]
                self.精神 += self.技能栏[i].结算统计()[2]

        self.进图智力 += self.智力
        self.进图体力 += self.体力
        self.进图精神 += self.精神

        self.进图体力 *= 1 + self.百分比体精
        self.进图精神 *= 1 + self.百分比体精

        if self.类型 == '智力':
            self.BUFF适用面板 += self.进图智力
            for i in self.技能栏:
                if i.是否主动 == 1:
                    if i.所在等级 == 30:
                        i.适用数值 = self.BUFF适用面板
                    else:
                        i.适用数值 = self.进图智力

        elif self.类型 == '体力':
            self.BUFF适用面板 += self.进图体力
            for i in self.技能栏:
                if i.是否主动 == 1:
                    if i.所在等级 == 30:
                        i.适用数值 = self.BUFF适用面板
                    else:
                        i.适用数值 = self.进图体力

        elif self.类型 == '精神':
            self.BUFF适用面板 += self.进图精神
            for i in self.技能栏:
                if i.是否主动 == 1:
                    if i.所在等级 == 30:
                        i.适用数值 = self.BUFF适用面板
                    else:
                        i.适用数值 = self.进图精神

    #返回可能的组合列表
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
            #3332散搭
            if 套装栏[i] in 匹配1[i]:
                count.append(1)
            elif 套装栏[i] in 匹配0[i]:
                count.append(0)
            else:
                count.append(-9)
            #3233双防具
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
                i.装备栏[num * 2] = 装备列表[套装映射[装备列表[装备序号[i.装备栏[1]]].所属套装 + '-' + '史诗' + '-' + 装备列表[装备序号[i.装备栏[num * 2]]].部位]].名称
                i.套装栏[2 * num + 2] = i.套装栏[2 * num + 2].replace(装备列表[装备序号[i.装备栏[index[num]]]].所属套装, 装备列表[装备序号[i.装备栏[1]]].所属套装)
                i.切换详情 = 装备列表[装备序号[i.装备栏[num * 2]]].部位 + '：' + x1.装备栏[num * 2] + ' → ' + i.装备栏[num * 2]
                num += 1
            return [x1, x2, x3, x4]
        elif sumcount == 6:
            index = count.index(0)
            部位 = {2:6, 4:5, 6:7}
            x1 = deepcopy(属性)
            x2 = deepcopy(属性)
            x2.装备栏[index - 2] = 装备列表[套装映射[装备列表[装备序号[x2.装备栏[部位[index]]]].所属套装 + '-' + '史诗' + '-' + 装备列表[装备序号[x2.装备栏[index - 2]]].部位]].名称
            x2.套装栏[index] = x2.套装栏[index].replace(装备列表[装备序号[x2.装备栏[1]]].所属套装, 装备列表[装备序号[x2.装备栏[部位[index]]]].所属套装)
            x2.切换详情 = 装备列表[装备序号[x2.装备栏[index - 2]]].部位 + '：' + x1.装备栏[index - 2] + ' → ' + x2.装备栏[index - 2]
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
                if 装备列表[装备序号[属性.装备栏[i]]].所属套装 == 三件套名称:
                    可更换部位.append(i)
                else:
                    不可更换部位.append(i)
            x2.装备栏[可更换部位[0]] = 装备列表[套装映射[两件套名称 + '-' + '史诗' + '-' + 部位列表[可更换部位[0]]]].名称
            x3.装备栏[可更换部位[1]] = 装备列表[套装映射[两件套名称 + '-' + '史诗' + '-' + 部位列表[可更换部位[1]]]].名称
            x4.装备栏[可更换部位[2]] = 装备列表[套装映射[两件套名称 + '-' + '史诗' + '-' + 部位列表[可更换部位[2]]]].名称

            x5.装备栏[不可更换部位[0]] = 装备列表[套装映射[三件套名称 + '-' + '史诗' + '-' + 部位列表[不可更换部位[0]]]].名称
            x5.装备栏[不可更换部位[1]] = 装备列表[套装映射[三件套名称 + '-' + '史诗' + '-' + 部位列表[不可更换部位[1]]]].名称
            
            x2.切换详情 = 部位列表[可更换部位[0]] + '：' + 属性.装备栏[可更换部位[0]] + ' → ' + x2.装备栏[可更换部位[0]]
            x3.切换详情 = 部位列表[可更换部位[1]] + '：' + 属性.装备栏[可更换部位[1]] + ' → ' + x3.装备栏[可更换部位[1]]
            x4.切换详情 = 部位列表[可更换部位[2]] + '：' + 属性.装备栏[可更换部位[2]] + ' → ' + x4.装备栏[可更换部位[2]]
            x5.切换详情 = 属性.套装栏[2] + ' → ' + x5.套装栏[2]
            return [x1, x2, x3, x4, x5]
        else:
            return [deepcopy(属性)]

    def 数据计算(self):        
        总数据 = []
        if self.双装备模式 == 1 and self.次数输入[self.一觉序号] == '1':
            #用于计算一觉
            temp = deepcopy(self)

            #拷贝数据，并修改装备，返回可能的组合
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
                数据列表.append(一觉计算属性.技能栏[self.一觉序号].结算统计()[3] * (一觉计算属性.技能栏[self.三觉序号].加成倍率() if self.三觉序号 != 0 and self.次数输入[self.三觉序号] == '1' else 1)) #3是力量属性  一觉力智都是相等的
                切换列表.append(一觉计算属性.切换详情)
            
            #取一觉最大值，并修改数据
            a = max(数据列表)
            序号 = 数据列表.index(a)
            if 序号 != 0:
                temp = '<br><br>' + ((self.技能栏[self.一觉序号].名称 + '+' + self.技能栏[self.三觉序号].名称 + '：') if self.三觉序号 != 0 else (self.技能栏[self.一觉序号].名称 + '：')) + str(int(数据列表[0])) + '→' + str(int(a)) + ' (+' + str(int(a) - int(数据列表[0])) + ')'
            else:
                temp = ''
            #计算现有装备BUFF
            self.装备属性计算()
            #一觉属性替换
            替换属性 = 替换属性_temp[序号]
            self.一觉Lv = 替换属性.一觉Lv
            self.一觉力智 = 替换属性.一觉力智
            self.一觉适用数值 = 一觉计算属性_temp[序号].技能栏[self.一觉序号].适用数值 
            self.一觉力智per = 替换属性.一觉力智per
            self.技能栏[self.一觉序号] = 替换属性.技能栏[self.一觉序号]
            self.技能栏[self.三觉序号] = 替换属性.技能栏[self.三觉序号]
            self.自适应计算()
            self.适用数值计算()
            self.技能栏[self.一觉序号].适用数值 = 一觉计算属性_temp[序号].技能栏[self.一觉序号].适用数值 
            self.切换详情 = 切换列表[序号] + temp
            for i in range(len(self.技能栏)):
                if  self.次数输入[i] == '1':
                    总数据.append(self.技能栏[i].结算统计())
                else:
                    总数据.append([0, 0, 0, 0, 0, 0, 0, 0])
        else:
            self.装备属性计算()
            self.自适应计算()
            self.适用数值计算()
            for i in range(len(self.技能栏)):
                if self.次数输入[i] == '1':
                    总数据.append(self.技能栏[i].结算统计())
                else:
                    总数据.append([0, 0, 0, 0, 0, 0, 0, 0])
        return 总数据

    def 自适应计算(self):
        # 黑鸦词条计算

        # 武器词条自适应计算
        if self.希洛克武器词条 == 1:
            词条提升率 = []
            for i in range(len(武器属性组合)):
                temp = deepcopy(self)
                总数据 = []
                武器属性A = 武器属性组合[i][0]
                武器属性B = 武器属性组合[i][1]
                temp.武器属性输入(武器属性A, 武器属性B)
                temp.适用数值计算()
                if temp.双装备模式 == 1 and temp.次数输入[temp.一觉序号] == '1':
                    temp.技能栏[temp.一觉序号].适用数值 = temp.一觉适用数值
                for i in range(len(temp.技能栏)):
                    if temp.次数输入[i] == '1':
                        总数据.append(temp.技能栏[i].结算统计())
                    else:
                        总数据.append([0, 0, 0, 0, 0, 0, 0, 0])
                三觉属性 = temp.技能栏[temp.一觉序号].结算统计()[3] * (temp.技能栏[temp.三觉序号].加成倍率() - 1)
                总数据[temp.三觉序号] = [0, 0, 0, 三觉属性, 三觉属性, 0, 0, 0]
                提升率 = temp.提升率计算(总数据)
                词条提升率.append(提升率)     
            a = max(词条提升率)
            序号 = 词条提升率.index(a)
            self.自适应最高值 = 武器属性组合[序号]
            self.武器属性输入(self.自适应最高值[0], self.自适应最高值[1])
    
    def 武器属性输入(self, 武器属性A, 武器属性B):
        武器属性A = 武器属性A列表[武器属性A]
        武器属性B = 武器属性B列表[武器属性B]
        武器属性A.当前值 = int(武器属性A.最大值)
        武器属性B.当前值 = int(武器属性B.最大值)
        武器属性A.融合属性(self)
        if self.武器词条触发 == 1:
            武器属性B.融合属性(self)

    def 结果返回(self, x, 总数据):
        if x == 0:
            return self.提升率计算(总数据)
        elif x == 1:
            return 总数据
        elif x == 2:
            return self.提升率计算(总数据, self.排行系数)

    def BUFF计算(self, x = 0):
        总数据 = self.数据计算()
        return self.结果返回(x, 总数据)

    def 装备属性计算(self):
        self.装备基础()
        # self.专属词条计算()
        for i in self.装备栏:
            装备列表[装备序号[i]].城镇属性_BUFF(self)
            装备列表[装备序号[i]].BUFF属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].城镇属性_BUFF(self)
            套装列表[套装序号[i]].BUFF属性(self)
        
        if self.排行系数 == 1:
            P = deepcopy(self)
            P.站街计算()
            self.站街系数 = P.系数数值站街()

        for i in self.装备栏:
            装备列表[装备序号[i]].进图属性_BUFF(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].进图属性_BUFF(self)

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
        self.护石选项 = ['无','BUFF力量、智力+2%', 'BUFF力量、智力+4%', 'BUFF力量、智力+6%', 'BUFF力量、智力+8%']
        super().__init__()
       
    def 界面(self):
        self.setFixedSize(1120, 680)
        self.行高 = 30 
        self.输出背景图片 = QPixmap("./ResourceFiles/img/输出背景_BUFF.png")
        super().界面()

    def 界面1(self):
        super().界面1()

        #region 王座本源
        counter4 = 0
        counter5 = 15
        self.图片 = QLabel(self.main_frame1)
        self.图片.setMovie(self.装备图片[装备序号['王座本源']])
        self.装备图片[装备序号['王座本源']].start()
        self.图片.resize(28, 28)
        self.图片.move(657 + 55 * counter4, 20 + counter5 * 32)
        self.按钮 = QPushButton(self.main_frame1)
        self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.按钮.resize(28, 28)
        self.按钮.setToolTip(self.单件描述(装备列表[装备序号['王座本源']]))
        self.遮罩透明度[装备序号['王座本源']].setOpacity(0.5)
        self.按钮.setGraphicsEffect(self.遮罩透明度[装备序号['王座本源']])
        self.按钮.clicked.connect(lambda state, index = 装备序号['王座本源']: self.装备图标点击事件(index, 10))
        self.装备图片按钮[装备序号['王座本源']] = self.按钮
        self.装备图片按钮[装备序号['王座本源']].move(657 + 55 * counter4, 20 + counter5 * 32)
        #endregion

        for i in 称号列表:
            self.称号.addItem(i.名称)
        
        for i in 宠物列表:
            self.宠物.addItem(i.名称)

        标签 = QLabel(self.main_frame1)
        人物 = QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/职业.png")
        标签.setPixmap(人物)
        标签.resize(191, 523)
        标签.move(922 + int((191 - 人物.width())/2), 10)

        self.百变怪选项 = QCheckBox('百变怪   ', self.main_frame1)
        self.百变怪选项.move(660, 613)
        self.百变怪选项.resize(80, 24)
        self.百变怪选项.setToolTip('<font size="3" face="宋体">仅在极速模式和套装模式下生效</font>')
        self.百变怪选项.setStyleSheet(复选框样式)

        self.计算模式选择 = MyQComboBox(self.main_frame1)
        self.计算模式选择.addItems(['计算模式：极速模式', '计算模式：套装模式', '计算模式：单件模式'])
        self.计算模式选择.move(750, 613)
        self.计算模式选择.resize(235, 24)
        self.计算模式选择.setStyleSheet("MyQComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} MyQComboBox:hover{background-color:rgba(65,105,225,0.8)}")
        self.计算模式选择.setToolTip('<font size="3" face="宋体">极速模式：533和3332(散搭) (不含智慧产物)<br><br>套装模式：533、3332(散搭)和3233(双防具) (不含智慧产物)<br><br>单件模式：所有组合 (不含百变怪)</font>')
        
        self.切装模式选项 = QCheckBox('一觉切1件装备', self.main_frame1)
        self.切装模式选项.move(875, 580)
        self.切装模式选项.resize(105, 24)
        self.切装模式选项.setToolTip('<font size="3" face="宋体">仅对极速/套装模式中的3332散搭组合生效<br><br>默认相同打造</font>')
        self.切装模式选项.setStyleSheet(复选框样式)

        self.神话排名选项 = QCheckBox('神话排名模式', self.main_frame1)
        self.神话排名选项.move(990, 580)
        self.神话排名选项.resize(100, 24)
        self.神话排名选项.setToolTip('<font size="3" face="宋体">仅显示有神话的组合，且每件神话装备只会出现一次</font>')
        self.神话排名选项.setStyleSheet(复选框样式)
        
        self.最大使用线程数 = thread_num
        self.线程数选择 = MyQComboBox(self.main_frame1)
        self.线程数选择.move(660, 580)
        self.线程数选择.resize(80, 24)
        for i in range(thread_num, 0, -1):
            self.线程数选择.addItem('进程:' + str(i))
        if thread_num > 1 :
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
        self.排行参数.addItems(['提升率排行', '面板排行', '力量排行', '智力排行', '物攻排行', '魔攻排行', '独立排行'])
        self.排行参数.move(770, 545)
        self.排行参数.resize(100, 24)

        self.存档选择 = MyQComboBox(self.main_frame1)
        self.存档选择.move(660, 545)
        self.存档选择.resize(90, 24)
        self.存档选择.currentIndexChanged.connect(lambda state :self.存档更换())

        #一键修正按钮添加
        self.一键站街设置输入.append(QLineEdit(self.main_frame1))
        self.一键站街设置输入[0].setAlignment(Qt.AlignCenter)
        self.一键站街设置输入[0].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
        self.一键站街设置输入[0].resize(45, 24)
        self.一键站街设置输入[0].move(750, 580)

        self.一键修正按钮 = QPushButton('一键修正', self.main_frame1)
        self.一键修正按钮.clicked.connect(lambda state: self.一键修正())
        self.一键修正按钮.move(800, 580)
        self.一键修正按钮.resize(70, 24)
        self.一键修正按钮.setStyleSheet(按钮样式)



    def 界面2(self):
        # 第二个布局界面
        self.main_frame2 = QMainWindow()

        #技能等级、次数输入

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
                for j in range(0, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
            else:
                for j in range(- i.基础等级, i.等级上限 - i.基础等级 + 1):
                    self.等级调整[序号].addItem(str(j))
            for j in range(0, 2):
                self.次数输入[序号].addItem(str(j))
        
        横坐标=30
        纵坐标=0
        横坐标偏移量=60
        纵坐标偏移量=30
        词条框宽度=48
        行高 = 20
        
        counter=0
        for i in ['契约满级','等级调整','是否适用']:
            x=QLabel(i, self.main_frame2)
            x.move(横坐标+横坐标偏移量-30+50*counter,纵坐标)
            x.setStyleSheet(标签样式)
            counter+=1
        
        纵坐标+=20
        
        for i in self.角色属性A.技能栏:
            x=QLabel(self.main_frame2)
            x.setPixmap(self.技能图片[self.角色属性A.技能序号[i.名称]])
            x.resize(28,28)
            tempstr='<font size="3" face="宋体"><font color="#FF6666">'+i.名称 +i.备注 +'</font><br>'
            tempstr+='所在等级：'+str(i.所在等级)+'<br>'
            tempstr+='等级上限：'+str(i.等级上限)+'</font>'
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
            横坐标-=80
            纵坐标+=纵坐标偏移量
        
        横坐标=横坐标+80+50
        纵坐标=30
        
        for i in self.角色属性A.技能栏:
            self.次数输入[self.角色属性A.技能序号[i.名称]].resize(词条框宽度, 行高)
            self.次数输入[self.角色属性A.技能序号[i.名称]].move(横坐标,纵坐标)
            纵坐标+=纵坐标偏移量

        self.护石第一栏.addItems(self.护石选项)
        self.护石第二栏.addItems(self.护石选项)
        self.护石第三栏.addItems(self.护石选项)

       
        横坐标=395;纵坐标=20;行高=18
        x=QLabel("护石(第一栏/上)：", self.main_frame2)
        x.move(横坐标,纵坐标-5)
        x.setStyleSheet(标签样式)
        纵坐标+=21
        self.护石第一栏.move(横坐标,纵坐标)
        self.护石第一栏.resize(130, 行高)
        
        横坐标=565;纵坐标=20
        x=QLabel("护石(第二栏/下)：", self.main_frame2)
        x.move(横坐标,纵坐标-5)
        x.setStyleSheet(标签样式)
        纵坐标+=21
        self.护石第二栏.move(横坐标,纵坐标)
        self.护石第二栏.resize(130, 行高)

        横坐标=395;纵坐标=70;行高=18
        x=QLabel("护石(第三栏/韩)：", self.main_frame2)
        x.move(横坐标,纵坐标-5)
        x.setStyleSheet(标签样式)
        纵坐标+=21
        self.护石第三栏.move(横坐标,纵坐标)
        self.护石第三栏.resize(130, 行高)

        self.辟邪玉选择 = []
        self.辟邪玉数值 = []
        x=QLabel("辟邪玉选择：", self.main_frame2)
        x.move(395,115)
        x.setStyleSheet(标签样式)
        for i in range(4):
            x = MyQComboBox(self.main_frame2) 
            for j in 辟邪玉列表:
                #'[' + str(j.编号) + ']' + 
                x.addItem(j.名称)
            x.resize(200,20)
            x.move(395,140 + i * 25)
            x.currentIndexChanged.connect(lambda state, index = i:self.辟邪玉数值选项更新(index))
            self.辟邪玉选择.append(x)
            y = MyQComboBox(self.main_frame2) 
            y.resize(80,20)
            y.move(615,140 + i * 25)
            self.辟邪玉数值.append(y)

        self.复选框列表 = []
        for i in 选项设置列表:
            self.复选框列表.append(QCheckBox(i.名称, self.main_frame2))

        横坐标 = 395
        纵坐标 = 240

        x=QLabel("武器融合：", self.main_frame2)
        x.move(横坐标,纵坐标 + 5)
        x.resize(300,20)
        x.setStyleSheet(标签样式)

        self.希洛克武器选择 = MyQComboBox(self.main_frame2)
        self.希洛克武器选择.addItems(['武器词条：无', '自适应最高值', '自选词条数值'])
        self.希洛克武器选择.resize(120,20)
        self.希洛克武器选择.move(横坐标 + 60, 纵坐标 + 5)
        self.希洛克武器选择.currentIndexChanged.connect(lambda state: self.希洛克武器选择更新())
        纵坐标 += 10
        self.武器融合属性A = MyQComboBox(self.main_frame2) 
        for j in 武器属性A列表:
            self.武器融合属性A.addItem(j.固定属性描述)
        self.武器融合属性A.resize(105,20)
        self.武器融合属性A.move(横坐标,纵坐标 + 25)

        self.武器融合属性A1 = MyQComboBox(self.main_frame2)
        self.武器融合属性A1.resize(90,20)
        self.武器融合属性A1.move(横坐标 + 110,纵坐标 + 25)

        self.武器融合属性A2 = MyQComboBox(self.main_frame2) 
        self.武器融合属性A2.resize(50,20)
        self.武器融合属性A2.move(横坐标 + 205,纵坐标 + 25)
        self.武器融合属性A.currentIndexChanged.connect(lambda:self.希洛克武器随机词条更新(self.武器融合属性A.currentIndex()))

        纵坐标 = 纵坐标 + 30
        self.武器融合属性B = MyQComboBox(self.main_frame2) 
        for j in 武器属性B列表:
            self.武器融合属性B.addItem(j.固定属性描述)
        self.武器融合属性B.resize(105,20)
        self.武器融合属性B.move(横坐标,纵坐标 + 25)

        self.武器融合属性B1 = MyQComboBox(self.main_frame2)
        self.武器融合属性B1.resize(90,20)
        self.武器融合属性B1.move(横坐标 + 110,纵坐标 + 25)

        self.武器融合属性B2 = MyQComboBox(self.main_frame2) 
        self.武器融合属性B2.resize(50,20)
        self.武器融合属性B2.move(横坐标 + 205,纵坐标 + 25)
        self.武器融合属性B.currentIndexChanged.connect(lambda:self.希洛克武器随机词条更新(self.武器融合属性B.currentIndex(), 1))

        横坐标=740;纵坐标=30
        名称 = ['奈克斯', '暗杀者', '卢克西', '守门人', '洛多斯']
        self.希洛克套装按钮 = []
        self.希洛克单件按钮 = []
        self.希洛克遮罩透明度 = []
        self.希洛克选择状态 = [0] * 15 
        count = 0
        for i in 名称:
            self.希洛克套装按钮.append(QPushButton(i, self.main_frame2))
            self.希洛克套装按钮[count].setStyleSheet(按钮样式)
            self.希洛克套装按钮[count].resize(50,22)
            self.希洛克套装按钮[count].move(横坐标, 纵坐标 + 4 + count * 40)
            self.希洛克套装按钮[count].clicked.connect(lambda state, index = (count + 1) * 100:self.希洛克选择(index))
            for j in range(3):
                序号 = count * 3 + j
                图片 = QLabel(self.main_frame2)
                图片.setPixmap(QPixmap('./ResourceFiles/img/希洛克/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标+ 60 + j * 30, 纵坐标 + count * 40)
                self.希洛克遮罩透明度.append(QGraphicsOpacityEffect())
                self.希洛克遮罩透明度[序号].setOpacity(0.5)
                self.希洛克单件按钮.append(QPushButton(self.main_frame2))
                self.希洛克单件按钮[序号].setStyleSheet("background-color: rgb(0, 0, 0)")
                self.希洛克单件按钮[序号].resize(28, 28)
                self.希洛克单件按钮[序号].move(横坐标+ 60 + j * 30, 纵坐标 + count * 40)
                self.希洛克单件按钮[序号].setGraphicsEffect(self.希洛克遮罩透明度[序号])
                self.希洛克单件按钮[序号].clicked.connect(lambda state, index = 序号:self.希洛克选择(index))
            count += 1

        counter=0
        for i in self.复选框列表:
            i.setStyleSheet(复选框样式)
            i.resize(180,20)
            i.move(930,25 + counter * 28)
            if counter < 1:
                i.setChecked(True)
            counter+=1

        self.排行选项 = []
        for i in range(3):
            self.排行选项.append(MyQComboBox(self.main_frame2))

        for i in [3000,3500,4000,4500,5000,5500,6000,7000,8000,10000,12000,15000,20000]:
            self.排行选项[0].addItem('C力智:' + str(i))
        self.排行选项[0].setCurrentIndex(4)

        for i in [2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600,3700,3800,3900,4000,4200,4400,4600,4800,5000]:
            self.排行选项[1].addItem('C三攻:' + str(i))
        self.排行选项[1].setCurrentIndex(10)

        for i in ['物理百分比','魔法百分比','物理固伤','魔法固伤']:
            self.排行选项[2].addItem(i)
        
        counter=0
        for i in self.排行选项:
            i.resize(100,20)
            i.move(990,520 + counter * 28)
            counter+=1


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
            self.一觉遮罩.setStyleSheet("QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}")
            self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
            self.一觉遮罩.clicked.connect(lambda state, index=1: self.强化觉醒选择(index))
            self.二觉遮罩 = QPushButton(self.main_frame2)
            self.二觉遮罩.resize(38, 50)
            self.二觉遮罩.move(x + 47, y + 5)
            self.二觉遮罩.setStyleSheet("QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}")
            self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)
            self.二觉遮罩.clicked.connect(lambda state, index=2: self.强化觉醒选择(index))

    def 界面3(self):
        # 第三个布局界面
        self.main_frame3 = QMainWindow()

        self.属性设置输入 = []
        self.技能设置输入 = []

        宽度 = 43

        列名称1 = ["智力", "体力", "精神"]
        行名称1 = ["工会属性", "训练官BUFF", "戒指", "婚房", "冒险团", "晶体契约", "收集箱", "勋章", "名称装饰卡", "快捷栏纹章", "宠物装备-红",
                "  宠物装备-蓝  ", "  宠物装备-绿  ", "宠物附魔","皮肤", "站街修正", "进图修正"]
        名称 = QLabel("基础细节", self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(
            "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
        名称.resize(80, 25)
        名称.move(10, 5)

        for i in range(0, 3):
            名称 = QLabel(列名称1[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(宽度, 25)
            名称.move(95 + i * (宽度 + 5), 5)

        for j in range(0, 17):
            名称 = QLabel(行名称1[j], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(80, 25)
            名称.move(10, 35 + j * 30)

        for i in range(0, 3):
            Linelist = []
            for j in range(0, 17):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet(
                    "QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(95 + i * (宽度 + 5), 35 + j * 30)
            self.属性设置输入.append(Linelist)

        列名称2 = ["智力", "体力", "精神","徽章智","徽章体","徽章精","技能等级"]
        行名称2 = ["上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "左槽", "右槽", "耳环", "武器", "登记补正","穿戴称号", "光环", "武器装扮", "时装"]

        self.列名称 = 列名称1 + 列名称2
        self.行名称 = 行名称1 + 行名称2

        名称 = QLabel(" 附魔&徽章 ", self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(
            "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
        名称.resize(80, 25)
        名称.move(7 * 宽度, 5)
        for i in range(0, 7):
            名称 = QLabel(列名称2[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            if i == 6:
                名称.resize(150, 25)
            else:
                名称.resize(宽度, 25)
            名称.move(90 + 7 * 宽度 + i * (宽度 + 5), 5)

        for j in range(0, 17):
            名称 = QLabel(行名称2[j], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(80, 25)
            名称.move(7 * 宽度, 35 + j * 30)

        for i in range(0, 6):
            Linelist = []
            for j in range(0, 17):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet(
                    "QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(90 + 7 * 宽度 + i * (宽度 + 5), 35 + j * 30)
            self.属性设置输入.append(Linelist)

        for j in range(0, 17):
            self.技能设置输入.append(MyQComboBox(self.main_frame3))
            self.技能设置输入[j].addItem('无')
            self.技能设置输入[j].setStyleSheet(
                "MyQComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            self.技能设置输入[j].resize(150, 22)
            self.技能设置输入[j].move(90 + 7 * 宽度 + 6 * (宽度 + 5), 35 + j * 30)

        for j in [2, 3, 4]:
            self.技能设置输入[j].addItems(['Lv1-30(主动)Lv+1', 'Lv1-50(主动)Lv+1'])
        self.技能设置输入[2].addItems(['Lv1-35(主动)Lv+1', 'Lv30-50(主动)Lv+1'])
        self.技能设置输入[3].addItem('Lv30-50(主动)Lv+1')

        for j in [8, 9, 16]:
            for i in self.角色属性A.技能栏:
                self.技能设置输入[j].addItem(i.名称 + 'Lv+1')
        self.技能设置输入[12].addItems(['BUFFLv+1', 'BUFFLv+2','BUFFLv+3','BUFFLv+4'])
        self.技能设置输入[13].addItems(['Lv1-50(主动)Lv+1', '一觉Lv+1', '一觉Lv+2'])
        self.技能设置输入[14].addItems(['Lv1-30(所有)Lv+1', 'Lv1-50(所有)Lv+1', 'Lv1-20(所有)Lv+1', 'Lv20-30(所有)Lv+1', 'Lv1-80(所有)Lv+1'])

        if '智力' in self.角色属性A.类型选择:
            self.修正列表名称 = ['转职被动智力', 'BUFF力智%', 'BUFF三攻%', '转职被动等级', '一觉被动力智', '一觉力智%', '一觉力智']
        else:
            self.修正列表名称 = ['守护恩赐体精', 'BUFF力智%', 'BUFF三攻%', '守护恩赐等级', '信念光环体精', '一觉力智%', '一觉力智']

        Linelist = []
        for i in range(0, len(self.修正列表名称)):
            名称 = QLabel(self.修正列表名称[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(90, 25)
            名称.move(170 + 7 * 宽度 + 9 * (宽度 + 5), 35 + i * 30)
            Linelist.append(QLineEdit(self.main_frame3))
            Linelist[i].setAlignment(Qt.AlignCenter)
            Linelist[i].setStyleSheet(
                "QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
            Linelist[i].resize(60, 25)
            Linelist[i].move(270 + 7 * 宽度 + 9 * (宽度 + 5), 35 + i * 30)
        self.属性设置输入.append(Linelist)

        count = 0
        self.时装选项 = []
        for i in ['头部', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']:
            名称 = QLabel(i, self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(
                "QLabel{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px}")
            名称.resize(90, 25)
            名称.move(170 + 7 * 宽度 + 9 * (宽度 + 5), 255 + count * 30)
            self.时装选项.append(MyQComboBox(self.main_frame3))
            self.时装选项[count].addItems(['高级', '节日', '稀有', '神器'])
            self.时装选项[count].resize(60, 22)
            self.时装选项[count].move(270 + 7 * 宽度 + 9 * (宽度 + 5), 255 + count * 30)
            self.时装选项[count].currentIndexChanged.connect(lambda state, index=count: self.时装选项更新(index))
            count += 1

        self.时装选项.append(MyQComboBox(self.main_frame3))
        self.时装选项[8].addItems(['高级套装[8]', '节日套装[8]', '稀有套装[8]', '神器套装[8]'])
        self.时装选项[8].resize(160, 22)
        self.时装选项[8].move(170 + 7 * 宽度 + 9 * (宽度 + 5), 260 + count * 30)
        self.时装选项[8].currentIndexChanged.connect(lambda state, index=8: self.时装选项更新(index))

        self.计算按钮3 = QPushButton('开始计算', self.main_frame3)
        self.计算按钮3.clicked.connect(lambda state: self.计算())
        self.计算按钮3.move(990, 610)
        self.计算按钮3.resize(100, 30)
        self.计算按钮3.setStyleSheet(按钮样式)

    def 界面5(self):
        # 第五个布局
        self.main_frame5 = QMainWindow()
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
        self.图片列表 = []

        count = 0
        self.自选装备 = []
        self.装备锁定 = []
        for i in 部位列表:
            锁定选择 = QCheckBox(i, self.main_frame5)
            锁定选择.setStyleSheet(复选框样式)
            锁定选择.resize(70, 22)
            锁定选择.move(10, 50 + 30 * count)
            self.装备锁定.append(锁定选择)
            self.自选装备.append(MyQComboBox(self.main_frame5))
            self.自选装备[count].resize(220, 22)
            self.自选装备[count].move(90, 50 + 30 * count)
            self.自选装备[count].currentIndexChanged.connect(lambda state, index=count: self.自选装备更改(index))
            for j in 装备列表:
                if j.部位 == i:
                    if i == '武器':
                        if j.类型 in self.角色属性A.武器选项:
                            self.自选装备[count].addItem(j.名称)
                    else:
                        self.自选装备[count].addItem(j.名称)
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
            for j in 套装列表:
                if j.名称 not in 套装名称 and j.类型 == i:
                    套装名称.append(j.名称)
            self.自选套装[count].addItems(套装名称)
            self.自选套装[count].resize(160, 22)
            self.自选套装[count].move(330, 50 + 30 * count)
            self.自选套装[count].activated.connect(lambda state, index=count: self.自选套装更改(index))
            count += 1
        
        self.神话部位选项 = MyQComboBox(self.main_frame5)
        self.神话部位选项.addItems(['神话部位：无', '神话部位：上衣', '神话部位：手镯', '神话部位：耳环'])
        self.神话部位选项.resize(160, 22)
        self.神话部位选项.move(330, 50 + 30 * count)
        self.神话部位选项.activated.connect(lambda state: self.神话部位更改())
        
        count += 1
        #一键修正按钮添加
        self.一键站街设置输入.append(QLineEdit(self.main_frame5))
        self.一键站街设置输入[1].setAlignment(Qt.AlignCenter)
        self.一键站街设置输入[1].setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}")
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
        图片显示.resize(268, 564)
        图片显示.move(初始x, 初始y)
        人物 = QLabel(self.main_frame5)
        图片 = QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(初始x + 90 + int(45 - 图片.width() / 2), 初始y + 40)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)

        self.提升率显示=QLabel(self.main_frame5)
        self.提升率显示.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        self.提升率显示.resize(250,36)
        self.提升率显示.move(初始x + 10, 初始y + 517)
        self.提升率显示.setAlignment(Qt.AlignCenter) 

        偏移量 = 187
        x坐标 = [32, 0, 0, 32, 0, 偏移量, 偏移量 + 32, 偏移量 + 32, 偏移量, 偏移量, 偏移量 + 32, 32]
        y坐标 = [0, 0, 32, 32, 64, 0, 0, 32, 64, 32, 64, 64]

        for i in range(12):
            self.图片列表.append(self.装备图片[装备序号[self.自选装备[i].currentText()]])
            self.图片显示.append(QLabel(self.main_frame5))
            self.图片显示[i].setMovie(self.图片列表[i])
            self.图片列表[i].start()
            self.图片显示[i].resize(26, 26)
            self.图片显示[i].move(初始x + 10 + x坐标[i], 初始y + 31 + y坐标[i])
            self.图片显示[i].setAlignment(Qt.AlignCenter)

        self.面板显示 = []
        for i in range(0,11):
            self.面板显示.append(QLabel(self.main_frame5))
        const = 139
        self.面板显示[0].move(初始x, 初始y + const)
        self.面板显示[1].move(初始x + 135, 初始y + const)

        const += 36
        count = 0
        for i in [2,3,4,5,6,7]:
            self.面板显示[i].move(初始x, 初始y + const + count * 18)
            count += 1

        count = 0
        for i in [8,9,10]:
            self.面板显示[i].move(初始x + 135, 初始y + const + count * 18)
            count += 1

        for i in range(0,len(self.面板显示)):
            if i != 1:
                self.面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            else:
                self.面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(150,255,30)}")
            self.面板显示[i].resize(100,18)
            self.面板显示[i].setAlignment(Qt.AlignRight)

        self.词条显示 = []
        for i in range(0, 12):
            self.词条显示.append(QLabel(self.main_frame5))

        j = 315 + 初始y
        for i in self.词条显示:
            i.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            i.move(20 + 初始x, j)
            i.resize(180, 18)
            i.setAlignment(Qt.AlignLeft)
            j += 18

        # self.总伤害 = QLabel(self.main_frame5)
        # self.总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        # self.总伤害.resize(600, 36)
        # self.总伤害.move(200, 517 + 初始y)
        # self.总伤害.setAlignment(Qt.AlignCenter)

        self.套装名称显示 = []
        for i in range(0, 8):
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
            套装字典 = {'高级':0, '节日':0, '稀有':0, '神器':0}
            for i in range(8):
                套装字典[self.时装选项[i].currentText()] = 套装字典.get(self.时装选项[i].currentText(), 0) + 1
            #套装属性
            神器 = 套装字典['神器']
            稀有 = 套装字典['稀有'] + 神器
            if 套装字典['高级'] >= 3:
                智力 += 10; 体力 += 10; 精神 += 10
            if 稀有 >= 3 and 神器 < 3:
                智力 += 40; 体力 += 40; 精神 += 40
            if 套装字典['神器'] >= 3:
                智力 += 50; 体力 += 50; 精神 += 50
            if 套装字典['高级'] >= 8:
                智力 += 10; 体力 += 10; 精神 += 10
            if 套装字典['节日'] >= 8:
                智力 += 25; 体力 += 25; 精神 += 25
            if 稀有 >= 8 and 神器 < 8:
                智力 += 40; 体力 += 40; 精神 += 40
            if 套装字典['神器'] >= 8:
                智力 += 50; 体力 += 50; 精神 += 50
            数据 = [45, 45, 55, 65]
            智力 += 数据[self.时装选项[0].currentIndex()] #头部
            精神 += 数据[self.时装选项[0].currentIndex()] #头部
            智力 += 数据[self.时装选项[1].currentIndex()] #帽子
            精神 += 数据[self.时装选项[1].currentIndex()] #帽子
            数据 = [0, 0, 55, 65]
            体力 += 数据[self.时装选项[5].currentIndex()]  # 腰带
            数据 = [45 ,45, 55, 65]
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
            self.武器融合属性A.setStyleSheet(不可选择下拉框样式)
            self.武器融合属性A1.setStyleSheet(不可选择下拉框样式)
            self.武器融合属性A2.setStyleSheet(不可选择下拉框样式)
            # 武器融合属性B禁用
            self.武器融合属性B.setEnabled(False)
            self.武器融合属性B1.setEnabled(False)
            self.武器融合属性B2.setEnabled(False)
            self.武器融合属性B.setStyleSheet(不可选择下拉框样式)
            self.武器融合属性B1.setStyleSheet(不可选择下拉框样式)
            self.武器融合属性B2.setStyleSheet(不可选择下拉框样式)
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

    def 希洛克武器随机词条更新(self, index, x = 0):
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

    def 批量选择(self, index):
        if index == 1:
            if self.全选状态 == 1:
                self.全选状态 = 0
            else:
                self.全选状态 = 1
            if sum(self.装备选择状态[74:244]) == 170:
                self.批量选择(0)

        for i in 装备列表:
            if i.部位 != '武器':
                if i.品质 != '神话' or index == 0 or self.全选状态 == 0:
                    self.装备图标点击事件(装备序号[i.名称], index, x = 0)
            else:
                if i.类型 in self.角色属性A.武器选项:
                    self.装备图标点击事件(装备序号[i.名称], index, x = 0)

        self.装备图标点击事件(74, index)
    
    def 载入配置(self, path = 'set'):
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ3.ini', 'r', encoding='utf-8').readlines()
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
            for i in range(0,len(self.时装选项)):
                self.时装选项[i].setCurrentIndex(int(setfile[i + 6].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/attr.ini', 'r', encoding='utf-8').readlines()
            for i in range(0, 10):
                for j in range(0, len(self.属性设置输入[i])):
                    self.属性设置输入[i][j].setText(setfile[i].replace('\n', '').split(',')[j])
        
            for j in range(0, 17):
                self.技能设置输入[j].setCurrentIndex(int(setfile[10].replace('\n', '').split(',')[j]))
        except:
            pass

        try:
            self.批量选择(0)#先清空
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ.ini', 'r', encoding='utf-8').readlines()
            for i in range(0, len(装备列表)):
                if setfile[i].replace('\n', '') == '1':
                    self.装备图标点击事件(i, 1)
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ1.ini', 'r', encoding='utf-8').readlines()
            for i in range(0,len(self.装备打造选项)):
                self.装备打造选项[i].setCurrentIndex(int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ2.ini', 'r', encoding='utf-8').readlines()
            for i in range(0,len(self.装备条件选择)):
                self.装备条件选择[i].setCurrentIndex(int(setfile[i].replace('\n', '')))
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill1.ini', 'r', encoding='utf-8').readlines()
            num = 0
            self.护石第一栏.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石第二栏.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.护石第三栏.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill2.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in self.角色属性A.技能栏:
                序号 = self.角色属性A.技能序号[i.名称]
                self.等级调整[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.次数输入[序号].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill3.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(4):
                self.辟邪玉选择[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
                self.辟邪玉数值[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass
            
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill4.ini', 'r', encoding='utf-8').readlines()
            num = 0
            self.武器融合属性A.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.武器融合属性A2.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.武器融合属性B.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.武器融合属性B2.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.希洛克武器选择.setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
            self.希洛克选择(0, 1)
            for i in range(15):
                if setfile[num].replace('\n', '') == '1':
                    self.希洛克选择(i)
                num += 1
            
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ4.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(4 * 35):
                self.神话属性选项[i].setCurrentIndex(int(setfile[num].replace('\n', ''))); num += 1
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path + '/equ5.ini', 'r', encoding='utf-8').readlines()
            num = 0
            for i in range(12):
                self.自选装备[i].setCurrentIndex(int(setfile[num].replace('\n', '')));
                num += 1
            for i in range(12):
                if int(setfile[num].replace('\n', '')) == 1:
                    self.装备锁定[i].setChecked(True)
                else:
                    self.装备锁定[i].setChecked(False)
                num += 1                
        except:
            pass

    def 保存配置(self, path = 'set'):
        if self.禁用存档.isChecked():
            return
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ3.ini', 'w', encoding='utf-8')
            setfile.write(str(self.称号.currentIndex())+'\n')
            setfile.write(str(self.宠物.currentIndex())+'\n')
            setfile.write(str(self.计算模式选择.currentIndex())+'\n')
            # 百变怪 && 神话排名 && 一觉切装备 && 时装选择
            setfile.write(str(int(self.百变怪选项.isChecked())) + '\n')
            setfile.write(str(int(self.神话排名选项.isChecked())) + '\n')
            setfile.write(str(int(self.切装模式选项.isChecked())) + '\n')
            for i in range(0, len(self.时装选项)):
                setfile.write(str(self.时装选项[i].currentIndex()) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/attr.ini', 'w', encoding='utf-8')
            for i in range(0, 10):
                for j in range(0, len(self.属性设置输入[i])):
                    setfile.write(self.属性设置输入[i][j].text()+',')
                setfile.write('\n')
            for j in range(0, 17):
                setfile.write(str(self.技能设置输入[j].currentIndex())+',')
            setfile.write('\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ.ini', 'w', encoding='utf-8')
            for i in range(0, len(装备列表)):
                setfile.write(str(self.装备选择状态[i])+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ1.ini', 'w', encoding='utf-8')
            for i in range(0,len(self.装备打造选项)):
                setfile.write(str(self.装备打造选项[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ2.ini', 'w', encoding='utf-8')
            for i in range(0,len(self.装备条件选择)):
                setfile.write(str(self.装备条件选择[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill1.ini', 'w', encoding='utf-8')
            setfile.write(str(self.护石第一栏.currentIndex())+'\n')
            setfile.write(str(self.护石第二栏.currentIndex())+'\n')
            setfile.write(str(self.护石第三栏.currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill2.ini', 'w', encoding='utf-8')
            for i in self.角色属性A.技能栏:
                序号 = self.角色属性A.技能序号[i.名称]
                setfile.write(str(self.等级调整[序号].currentIndex())+'\n')
                setfile.write(str(self.次数输入[序号].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill3.ini', 'w', encoding='utf-8')
            for i in range(4):
                setfile.write(str(self.辟邪玉选择[i].currentIndex())+'\n')
                setfile.write(str(self.辟邪玉数值[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill4.ini', 'w', encoding='utf-8')
            setfile.write(str(self.武器融合属性A.currentIndex())+'\n')
            setfile.write(str(self.武器融合属性A2.currentIndex())+'\n')
            setfile.write(str(self.武器融合属性B.currentIndex())+'\n')
            setfile.write(str(self.武器融合属性B2.currentIndex())+'\n')
            setfile.write(str(self.希洛克武器选择.currentIndex())+'\n')
            for i in range(15):
                setfile.write(str(self.希洛克选择状态[i]) + '\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/equ4.ini', 'w', encoding='utf-8')
            for i in range(4 * 35):
                setfile.write(str(self.神话属性选项[i].currentIndex())+'\n')
        except:
            pass

        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path + '/equ5.ini', 'w', encoding='utf-8')
            for i in range(12):
                setfile.write(str(self.自选装备[i].currentIndex()) + '\n')
            for i in range(12):
                setfile.write(str(1 if self.装备锁定[i].isChecked() else 0) + '\n')
        except:
            pass

    # 一键修正计算
    def 一键修正(self, x = 0):
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
            装备列表[装备序号[i]].城镇属性_BUFF(self.角色属性B)
            装备列表[装备序号[i]].BUFF属性(self.角色属性B)
        for i in self.角色属性B.套装栏:
            套装列表[套装序号[i]].城镇属性_BUFF(self.角色属性B)
            套装列表[套装序号[i]].BUFF属性(self.角色属性B)
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
                QMessageBox.information(self, "错误", 名称[i] + "输入格式错误，已重置为空")
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
        QMessageBox.information(self, "自动修正计算完毕", "仅对站街修正进行了修改，使面板与输入一致<br>请自行核对其它页面 非智力/体力/精神条目")

    def 神话数量判断(self, x = 0):
        count = 0
        for j in range(len(装备列表)):
            if 装备列表[j].品质 == '神话':
                if self.装备选择状态[j] == 1:
                    count += 1
        if x == 0:
            if count != 0:
                return False
            else:
                return True
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


    def 自选计算(self, x=0):
        if x == 0:
            self.保存配置(self.存档位置)
            self.排行窗口列表.clear()
            self.排行数据.clear()

        self.角色属性A = deepcopy(self.初始属性)
        if x == 0:
            self.输入属性(self.角色属性A)
        else:
            self.输入属性(self.角色属性A, 1)

        装备 = []
        for i in self.自选装备:
            装备.append(i.currentText())

        套装 = []
        套装字典 = {}
        for i in 装备:
            j = 装备列表[装备序号[i]].所属套装
            if j == '智慧产物':
                try:
                    k = 装备列表[装备序号[i]].所属套装2
                    套装字典[k] = 套装字典.get(k, 0) + 1
                except:
                    pass
            elif j != '无':
                套装字典[j] = 套装字典.get(j, 0) + 1

        for i in 套装字典.keys():
            if 套装字典[i] >= 2 and (i + '[2]') in 套装序号.keys():
                套装.append(i + '[2]')
            if 套装字典[i] >= 3 and (i + '[3]') in 套装序号.keys():
                套装.append(i + '[3]')
            if 套装字典[i] >= 5 and (i + '[5]') in 套装序号.keys():
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

            for i in range(0, len(提升率)):
                temp = str('%.2f' % (提升率[i] * 100)) + '%'
                self.辟邪玉提升率2[i].setText(temp)
                x = 提升率排序.index(提升率[i]) / len(提升率) * 10 - 2
                y = 1 / (1 + math.exp(-x))
                颜色 = (int(255 - 80 * y), int(245 - 100 * y), int(0 + 150 * y))
                self.辟邪玉提升率1[i].setStyleSheet('QLabel{font-size:12px;color:rgb' + str(颜色) + '}')
                self.辟邪玉提升率2[i].setStyleSheet('QLabel{font-size:12px;color:rgb' + str(颜色) + '}')

            self.角色属性A = deepcopy(self.初始属性)
            self.输入属性(self.角色属性A)
            C = self.站街计算(装备, 套装)
            B = deepcopy(self.角色属性A)
            B.穿戴装备(装备, 套装)
            D = deepcopy(B)
            
            
            统计详情 = B.BUFF计算(1)
            合计力量 = 0
            合计智力 = 0
            合计物攻 = 0
            合计魔攻 = 0
            合计独立 = 0
            for i in range(0, len(B.技能栏)):
                if sum(统计详情[i]) != 0:
                    合计力量 += 统计详情[i][3]
                    合计智力 += 统计详情[i][4]
                    合计物攻 += 统计详情[i][5]
                    合计魔攻 += 统计详情[i][6]
                    合计独立 += 统计详情[i][7]
            
            总奶量 = ''
            # tempstr = ''
            if 合计力量 == 合计智力:
                总奶量 += '力智+' + str(合计力量)
            else:
                总奶量 += '力量+' + str(合计力量)
                总奶量 += '，智力+' + str(合计智力)

            if 合计物攻 == 合计魔攻 and 合计魔攻 == 合计独立:
                总奶量 += '，三攻+' + str(合计物攻)
            else:
                总奶量 += '，物攻+' + str(合计物攻)
                总奶量 += '，魔攻+' + str(合计魔攻)
                总奶量 += '，独立+' + str(合计独立)
            # self.总伤害.setText(str(tempstr))
            x = B.BUFF面板()
            y = B.一觉面板()
            self.角色属性B = deepcopy(B)
            tempstr = self.装备描述_BUFF计算(B)
            for l in range(12):
                self.图片显示[l].setToolTip(tempstr[l])

            self.面板显示[0].setText('站街：' + str(int(C.系数数值站街())))
            self.面板显示[1].setText('适用：' + str(int(B.系数数值进图())))

            self.面板显示[2].setText(' ' + x[0])
            self.面板显示[3].setText('力量：' + str(x[1]))
            self.面板显示[4].setText('智力：' + str(x[2]))
            self.面板显示[5].setText('物攻：' + str(x[3]))
            self.面板显示[6].setText('魔攻：' + str(x[4]))
            self.面板显示[7].setText('独立：' + str(x[5]))

            self.面板显示[8].setText(' ' + y[0])
            self.面板显示[9].setText('力量：' + str(y[1]))
            self.面板显示[10].setText('智力：' + str(y[2]))

            tempstr = []
            tempstr.append('BUFF力量% ：' + str(int(round(B.BUFF力量per * 100, 0))) + '%')
            tempstr.append('BUFF智力% ：' + str(int(round(B.BUFF智力per * 100, 0))) + '%')
            tempstr.append('BUFF物攻% ：' + str(int(round(B.BUFF物攻per * 100, 0))) + '%')
            tempstr.append('BUFF魔攻% ：' + str(int(round(B.BUFF魔攻per * 100, 0))) + '%')
            tempstr.append('BUFF独立% ：' + str(int(round(B.BUFF独立per * 100, 0))) + '%')
            tempstr.append('一觉力智  ：' + str(int(round(B.一觉力智, 0))))
            tempstr.append('一觉力智% ：' + str(int(round(B.一觉力智per * 100, 0))) + '%')
            if B.角色 == '圣职者(男)':
                tempstr.append('守护徽章% ：' + str(int(round(B.守护徽章per * 100, 0))) + '%')
            elif B.角色 == '圣职者(女)' or B.角色 == '圣职者(女)':
                tempstr.append('BUFF增幅率：' + str(int(round(B.BUFF额外增幅率 * 100, 0))) + '%')
            tempstr.append(str(总奶量))
            
            if self.角色属性B.希洛克武器词条 == 1:
                武器词条最高值 = self.角色属性B.自适应最高值
                武器属性A = 武器属性A列表[武器词条最高值[0]]
                武器属性B = 武器属性B列表[武器词条最高值[1]]
                tempstr.append("属性1：" +"<font style='color:gray'>"+武器属性A.固定属性描述 + '</font>，' + 武器属性A.随机属性描述 + str(武器属性A.最大值)+ ('%' if 武器属性A.间隔 / 10 < 1 else ''))
                if self.角色属性B.武器词条触发 == 1:
                    tempstr.append("属性2：" +"<font style='color:gray'>"+武器属性B.固定属性描述 + '</font>，' + 武器属性B.随机属性描述 + str(武器属性B.最大值)+ ('%' if 武器属性B.间隔 / 10 < 1 else ''))

            count = 0
            for i in tempstr:
                self.词条显示[count].setText(i)
                count += 1

            for i in self.套装名称显示:
                i.setText('')

            self.套装名称显示[0].setText(装备[11])
            self.套装名称显示[0].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")

            套装名称 = []
            套装名称.extend(套装)

            神话所在套装 = []
            for i in range(0, 11):
                if 装备列表[装备序号[装备[i]]].品质 == '神话':
                    神话所在套装.append(装备列表[装备序号[装备[i]]].所属套装)

            套装 = []
            套装件数 = []
            套装属性= []
            for i in range(0,len(套装名称)):
                temp = 套装名称[i].split('[')[0]
                if temp not in 套装:
                    套装.append(temp)
                    套装件数.append([])
                    套装属性.append('')
                if len(套装名称[i].split('['))>1:
                    件数 = 套装名称[i].split('[')[1].split(']')[0]
                    套装件数[套装.index(temp)].append(件数)
                    套装属性[套装.index(temp)] += '<font size="3" face="宋体"><font color="#78FF1E">'+套装名称[i]+'</font><br>'+套装列表[套装序号[套装名称[i]]].装备描述_BUFF(self.角色属性B)[:-4]+'</font><br>'        

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
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2] ) > 1:
                套装.append("希洛克-奈克斯")
                套装件数.append([self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]])
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
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2] ) > 1:
                套装.append("希洛克-暗杀者")
                套装件数.append([self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]])
                套装属性.append(temp)

            i = 2  # 卢克西属性2
            temp = ''
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
                temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
                pass # 下装
            if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
                temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
                pass # 戒指
            if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
                temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
                temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
                pass # 辅助装备
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2] ) > 1:
                套装.append("希洛克-卢克西")
                套装件数.append([self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]])
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
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2] ) > 1:
                套装.append("希洛克-守门人")
                套装件数.append([self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]])
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
            if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2] ) > 1:
                套装.append("希洛克-洛多斯")
                套装件数.append([self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]])
                套装属性.append(temp)

            for i in range(0,len(套装)):
                if len(套装件数[i]) >0:
                    self.套装名称显示[i + 1].setText(套装[i]+'['+str(max(套装件数[i]))+']')
                else:
                    self.套装名称显示[i + 1].setText(套装[i])
                if 套装[i] in 神话所在套装:
                    self.套装名称显示[i + 1].setStyleSheet("QLabel{font-size:12px;color:rgb(226,150,146)}")   
                else:
                    self.套装名称显示[i + 1].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
                self.套装名称显示[i + 1].setToolTip(套装属性[i][:-4])

            # for i in range(0, len(套装)):
            #     self.套装名称显示[i + 1].setText(套装[i])
            #     if 套装[i].split('[')[0] in 神话所在套装:
            #         self.套装名称显示[i + 1].setStyleSheet("QLabel{font-size:12px;color:rgb(226,150,146)}")
            #     else:
            #         self.套装名称显示[i + 1].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            #     self.套装名称显示[i + 1].setToolTip('<font size="3" face="宋体"><font color="#78FF1E">'+套装[i]+'</font><br>'+套装列表[套装序号[套装[i]]].装备描述_BUFF(B)[:-4]+'</font>')
            
            提升率 = D.BUFF计算(0)
            if len(self.基准值) != 0:
                self.提升率显示.setText(self.对比输出(提升率, self.基准值[0], 1, 1))
            else:
                self.提升率显示.setText(str(round(提升率, 2)) + '%')

        if x == 0:
            self.排行数据.append(装备 + [0] + 套装 + ['无'])
            self.输出界面(0)

    def 站街计算(self,装备名称,套装名称):
        C = deepcopy(self.角色属性A)
        C.穿戴装备(装备名称,套装名称)
        for i in C.装备栏:
            装备列表[装备序号[i]].城镇属性_BUFF(C)
            装备列表[装备序号[i]].BUFF属性(C)
        for i in C.套装栏:
            套装列表[套装序号[i]].城镇属性_BUFF(C)
            套装列表[套装序号[i]].BUFF属性(C)
        C.装备基础()
        C.站街计算()
        return C
    
    def 对比输出(self, A, B, x = 0, y = 0):
        if B == 0:
            return str(A)
        if x == 0:
            temp = int(A - B)
            if temp == 0:
                if y == 1:
                    return '不变'
                return '-'
            elif temp > 0:
                return '<font face="宋体" color= "#96FF1E">+' + str(temp) + '</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + str(temp) + '</font>'
        else:
            temp = round((A / B - 1) * 100, 2)
            if temp == 0:
                if y == 1:
                    return '不变'
                return '-'
            elif temp > 0:
                return '<font face="宋体" color= "#96FF1E">+' + str('%.2f' % temp) + '%</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + str('%.2f' % temp) + '%</font>'

    def 输出界面(self, index, name = ''):
        装备名称 = []
        套装名称 = []
        百变怪 = self.排行数据[index][-1]
        for i in range(0, 12):
            装备名称.append(self.排行数据[index][i])
        for i in range(13,len(self.排行数据[index])-1):
            套装名称.append(self.排行数据[index][i])

        C = self.站街计算(装备名称,套装名称)

        self.角色属性B = deepcopy(self.角色属性A)
        self.角色属性B.穿戴装备(装备名称,套装名称)
        # self.角色属性B.装备属性计算()
        temp = deepcopy(self.角色属性B)
        统计详情 = self.角色属性B.BUFF计算(1)
        提升率 = temp.BUFF计算(0)

        #最大输出界面限制
        if len(self.输出窗口列表)>=10:
            del self.输出窗口列表[0]
    
        输出窗口 = QWidget()
        输出窗口.setStyleSheet('''QToolTip { 
           background-color: black; 
           color: white; 
           border: 0px
           }''')
        self.输出窗口列表.append(输出窗口)
        输出窗口.setFixedSize(788, 564)
        temp = ''
        if name == '':
            temp += '详细数据'
        else:
            temp += name
        temp += '（最多显示前18个技能）'+"装备版本："+self.角色属性A.版本 + " 增幅版本：" + self.角色属性A.增幅版本
        输出窗口.setWindowTitle(temp)
        输出窗口.setWindowIcon(self.icon)  
        QLabel(输出窗口).setPixmap(self.输出背景图片)
        人物 = QLabel(输出窗口)
        图片 = QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(90 + int(45 - 图片.width() / 2), 40)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)
      
        x = self.角色属性B.BUFF面板()
        y = self.角色属性B.一觉面板()
        面板显示=[]
        for i in range(0,11):
            面板显示.append(QLabel(输出窗口))     
        面板显示[0].setText('站街：' + str(int(C.系数数值站街())))
        面板显示[1].setText('适用：' + str(int(self.角色属性B.系数数值进图())))

        面板显示[2].setText(' ' + x[0])
        面板显示[3].setText('力量：' + str(x[1]))
        面板显示[4].setText('智力：' + str(x[2]))
        面板显示[5].setText('物攻：' + str(x[3]))
        面板显示[6].setText('魔攻：' + str(x[4]))
        面板显示[7].setText('独立：' + str(x[5]))

        面板显示[8].setText(' ' + y[0])
        面板显示[9].setText('力量：' + str(y[1]))
        面板显示[10].setText('智力：' + str(y[2]))

        const = 139
        面板显示[0].move(35,const)
        面板显示[1].move(165,const)
        
        const += 36
        count = 0
        for i in  [2,3,4,5,6,7]:
            面板显示[i].move(35,const + count * 18)
            count += 1

        count = 0
        for i in  [8,9,10]:
            面板显示[i].move(165,const + count * 18)
            count += 1

        for i in range(0,len(面板显示)):
            if i != 1:
                面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
            else:
                面板显示[i].setStyleSheet("QLabel{font-size:12px;color:rgb(150,255,30)}")
            面板显示[i].resize(100,18)
            面板显示[i].setAlignment(Qt.AlignLeft)

        tempstr=[]
        tempstr.append('BUFF力量% ：'+str(int(round(self.角色属性B.BUFF力量per * 100, 0))) + '%') 
        tempstr.append('BUFF智力% ：'+str(int(round(self.角色属性B.BUFF智力per * 100, 0))) + '%') 
        tempstr.append('BUFF物攻% ：'+str(int(round(self.角色属性B.BUFF物攻per * 100, 0))) + '%')
        tempstr.append('BUFF魔攻% ：'+str(int(round(self.角色属性B.BUFF魔攻per * 100, 0))) + '%')
        tempstr.append('BUFF独立% ：'+str(int(round(self.角色属性B.BUFF独立per * 100, 0))) + '%')
        tempstr.append('一觉力智  ：'+str(int(round(self.角色属性B.一觉力智, 0))))
        tempstr.append('一觉力智% ：'+str(int(round(self.角色属性B.一觉力智per * 100, 0))) + '%')
        tempstr.append('守护徽章% ：'+str(int(round(self.角色属性B.守护徽章per * 100, 0))) + '%')
        if self.角色属性B.角色 == '圣职者(男)':
            tempstr.append('守护徽章% ：' + str(int(round(self.角色属性B.守护徽章per * 100, 0))) + '%')
        elif self.角色属性B.角色 == '圣职者(女)' or self.角色属性B.角色 == '魔法师(女)':
            tempstr.append('BUFF增幅率：' + str(int(round(self.角色属性B.BUFF额外增幅率 * 100, 0))) + '%')
    
        j=318
        for i in tempstr:
            templab=QLabel(输出窗口)
            templab.setText(i)
            templab.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            templab.move(20,j)
            templab.resize(305,18)
            templab.setAlignment(Qt.AlignLeft)
            j+=18
        
        位置 = 313
        间隔 = 20
        适用称号名称=QLabel(self.称号.currentText(),输出窗口)
        适用称号名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用称号名称.move(114, 位置)
        适用称号名称.resize(150,18)
        适用称号名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔
        适用称号名称.setToolTip('<font size="3" face="宋体"><font color="#78FF1E">' + self.称号.currentText()+'</font><br>'+称号列表[self.称号.currentIndex()].装备描述_BUFF(self.角色属性B)[:-4]+'</font>')

        适用宠物名称=QLabel(self.宠物.currentText(),输出窗口)
        适用宠物名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用宠物名称.move(114, 位置)
        适用宠物名称.resize(150,18)
        适用宠物名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔
        适用宠物名称.setToolTip('<font size="3" face="宋体"><font color="#78FF1E">' + self.宠物.currentText()+'</font><br>'+宠物列表[self.宠物.currentIndex()].装备描述_BUFF(self.角色属性B)[:-4]+'</font>')

        适用中的套装 = QLabel(装备名称[11], 输出窗口)
        适用中的套装.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用中的套装.move(132, 位置)
        适用中的套装.resize(132, 18)
        适用中的套装.setAlignment(Qt.AlignCenter)
       
        神话所在套装 = '无'
        for i in range(0, 11):
            if 装备列表[装备序号[装备名称[i]]].品质 == '神话':
                神话所在套装 = 装备列表[装备序号[装备名称[i]]].所属套装

        套装 = []
        套装件数 = []
        套装属性= []
        for i in range(0,len(套装名称)):
            temp = 套装名称[i].split('[')[0]
            if temp not in 套装:
                套装.append(temp)
                套装件数.append([])
                套装属性.append('')
            if len(套装名称[i].split('['))>1:
                件数 = 套装名称[i].split('[')[1].split(']')[0]
                套装件数[套装.index(temp)].append(件数)
                套装属性[套装.index(temp)] += '<font size="3" face="宋体"><font color="#78FF1E">'+套装名称[i]+'</font><br>'+套装列表[套装序号[套装名称[i]]].装备描述_BUFF(self.角色属性B)[:-4]+'</font><br>'        

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
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2] ) > 1:
            套装.append("希洛克-奈克斯")
            套装件数.append([self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]])
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
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2] ) > 1:
            套装.append("希洛克-暗杀者")
            套装件数.append([self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]])
            套装属性.append(temp)

        i = 2  # 卢克西属性2
        temp = ''
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
            temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
            pass # 下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
            temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
            pass # 戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            temp += '<font size="3" face="宋体"><font color="#78FF1E">下装+辅助装备</font><br>'
            temp += '施放Lv50、Lv100主动技能时,赋予所有队友持续造成伤害的buff,伤害为30秒内所受伤害的1%,效果持续5秒<br>'
            pass # 辅助装备
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2] ) > 1:
            套装.append("希洛克-卢克西")
            套装件数.append([self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]])
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
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2] ) > 1:
            套装.append("希洛克-守门人")
            套装件数.append([self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]])
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
        if (self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2] ) > 1:
            套装.append("希洛克-洛多斯")
            套装件数.append([self.希洛克选择状态[i * 3 + 0] + self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]])
            套装属性.append(temp)

        for i in range(0,len(套装)):
            位置 += 间隔
            适用套装名称 = QLabel(输出窗口)
            if len(套装件数[i]) >0:
                适用套装名称.setText(套装[i]+'['+str(max(套装件数[i]))+']')
            else:
                适用套装名称.setText(套装[i])
            适用套装名称.move(132, 位置)
            适用套装名称.resize(132, 18)
            适用套装名称.setAlignment(Qt.AlignCenter)  
            if 套装[i] in 神话所在套装:
                适用套装名称.setStyleSheet("QLabel{font-size:12px;color:rgb(226,150,146)}")   
            else:
                适用套装名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
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

        实际技能等级=[]
        for i in self.角色属性B.技能栏:
            实际技能等级.append(i.等级)

        if len(self.基准值) != 0:
            显示模式 = 1
        else:
            显示模式 = 0

        count = 0
        for i in range(0,len(self.角色属性B.技能栏)):
            if sum(统计详情[i]) != 0:
                count += 1
                
        self.行高 = 30
        if count > 0:
            self.行高 = min(int(440 / count),30)        
        j = -1

        for i in range(0,len(self.角色属性B.技能栏)):
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

        for i in range(0,len(self.角色属性B.技能栏)):
            if sum(统计详情[i]) != 0:
                for k in range(len(统计详情[i])):
                    if 统计详情[i][k] == 0:
                        统计详情[i][k] = ''
                j += 1
                每行详情=[]
                for k in range(0,10):
                    每行详情.append(QLabel(输出窗口))
                #图片
                每行详情[0].setPixmap(self.技能图片[i])
                每行详情[0].move(302, 50 + j * self.行高)
                每行详情[0].resize(28,min(28,self.行高 - 2)) 
                #等级
                每行详情[1].setText('Lv.'+str(实际技能等级[i]))
                每行详情[1].move(337, 50 + j * self.行高)
                每行详情[1].resize(30,min(28,self.行高)) 
                #智力
                if 显示模式 == 1:
                    每行详情[2].setText(self.对比输出(统计详情[i][0], self.基准值[1][i][0]))
                else:
                    每行详情[2].setText(str(统计详情[i][0]))
                每行详情[2].move(370, 50 + j * self.行高)
                每行详情[2].resize(50,min(28,self.行高))
                #体力
                if 显示模式 == 1:
                    每行详情[3].setText(self.对比输出(统计详情[i][1], self.基准值[1][i][1]))
                else:
                    每行详情[3].setText(str(统计详情[i][1]))
                每行详情[3].move(410, 50 + j * self.行高)
                每行详情[3].resize(50,min(28,self.行高)) 
                #精神
                if 显示模式 == 1:
                    每行详情[4].setText(self.对比输出(统计详情[i][2], self.基准值[1][i][2]))
                else:
                    每行详情[4].setText(str(统计详情[i][2]))
                每行详情[4].move(450, 50 + j * self.行高)
                每行详情[4].resize(50,min(28,self.行高)) 
                #力量
                if 显示模式 == 1:
                    每行详情[5].setText(self.对比输出(统计详情[i][3], self.基准值[1][i][3]))
                else:
                    每行详情[5].setText(str(统计详情[i][3]))
                每行详情[5].move(490, 50 + j * self.行高) 
                每行详情[5].resize(50,min(28,self.行高)) 
                #智力
                if 显示模式 == 1:
                    每行详情[6].setText(self.对比输出(统计详情[i][4], self.基准值[1][i][4]))
                else:
                    每行详情[6].setText(str(统计详情[i][4]))
                每行详情[6].move(530, 50 + j * self.行高)
                每行详情[6].resize(50,min(28,self.行高))
                #物攻
                if 显示模式 == 1:
                    每行详情[7].setText(self.对比输出(统计详情[i][5], self.基准值[1][i][5]))
                else:
                    每行详情[7].setText(str(统计详情[i][5]))
                每行详情[7].move(570, 50 + j * self.行高)
                每行详情[7].resize(50,min(28,self.行高))
                #魔攻
                if 显示模式 == 1:
                    每行详情[8].setText(self.对比输出(统计详情[i][6], self.基准值[1][i][6]))
                else:
                    每行详情[8].setText(str(统计详情[i][6]))
                每行详情[8].move(610, 50 + j * self.行高)
                每行详情[8].resize(50,min(28,self.行高))
                #独立
                if 显示模式 == 1:
                    每行详情[9].setText(self.对比输出(统计详情[i][7], self.基准值[1][i][7]))
                else:
                    每行详情[9].setText(str(统计详情[i][7]))
                每行详情[9].move(650, 50 + j * self.行高)
                每行详情[9].resize(50,min(28,self.行高))
     
                for l in range(1,10):
                    每行详情[l].setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
                    每行详情[l].setAlignment(Qt.AlignCenter) 

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
                tempstr += '，智力' + 对比智力

            if 对比物攻 == 对比魔攻 and 对比魔攻 == 对比独立:
                tempstr += '，三攻' + 对比物攻
            else:
                tempstr += '，物攻' + 对比物攻
                tempstr += '，魔攻' + 对比魔攻
                tempstr += '，独立' + 对比独立
        else:
            if 合计力量 == 合计智力:
                tempstr += '力智+' + str(合计力量)
            else:
                tempstr += '力量+' + str(合计力量)
                tempstr += '，智力+' + str(合计智力)

            if 合计物攻 == 合计魔攻 and 合计魔攻 == 合计独立:
                tempstr += '，三攻+' + str(合计物攻)
            else:
                tempstr += '，物攻+' + str(合计物攻)
                tempstr += '，魔攻+' + str(合计魔攻)
                tempstr += '，独立+' + str(合计独立)
            if self.角色属性B.切换详情 != '无':
                tempstr += '<br><br>' + self.角色属性B.切换详情 

        if self.角色属性B.希洛克武器词条 == 1:
            武器词条最高值 = self.角色属性B.自适应最高值
            武器属性A = 武器属性A列表[武器词条最高值[0]]
            武器属性B = 武器属性B列表[武器词条最高值[1]]
            tempstr += '<br><br>' + "属性1：" +"<font style='color:gray'>"+武器属性A.固定属性描述 + '</font>，' + 武器属性A.随机属性描述 + str(武器属性A.最大值)+ ('%' if 武器属性A.间隔 / 10 < 1 else '')
            if self.角色属性B.武器词条触发 == 1:
                tempstr += '<br><br>' + "属性2：" +"<font style='color:gray'>"+武器属性B.固定属性描述 + '</font>，' + 武器属性B.随机属性描述 + str(武器属性B.最大值)+ ('%' if 武器属性B.间隔 / 10 < 1 else '')
        
        合计=QLabel(输出窗口)
        合计.setStyleSheet("QLabel{color:rgb(104,213,237);font-size:15px}")
        合计.setText(tempstr)
        合计.resize(450,150)
        合计.move(280, 90 + j * self.行高)
        合计.setAlignment(Qt.AlignCenter) 
    
        初始x=10;初始y=31
    
        图片列表 = []

        提升率显示=QLabel(输出窗口)
 
        提升率显示.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        if 显示模式 == 1:
            提升率显示.setText(self.对比输出(提升率, self.基准值[0], 1, 1))
        else:
            提升率显示.setText(str(round(提升率, 2)) + '%')
        提升率显示.resize(250,36)
        提升率显示.move(10,517)
        提升率显示.setAlignment(Qt.AlignCenter) 
    
        数量 = [0] * 3
        for i in range(15):
            数量[i % 3] += self.希洛克选择状态[i]

        # 0 上衣 1护肩 2护腿 3腰带 4鞋子 5 手镯 6 项链 7 戒指 8 耳环 9辅助 10魔法石 11 武器
        for i in range(0,12):
            # 下装
            if 数量[0] == 1 and i == 2:
                for item in range(5):
                    if self.希洛克选择状态[item*3+0] > 0:
                        图片列表.append(QMovie('./ResourceFiles/img/希洛克/'+str(item*3+0)+'.gif'))
            elif 数量[1] == 1 and i == 7:
                for item in range(5):
                    if self.希洛克选择状态[item*3+1] > 0:
                        图片列表.append(QMovie('./ResourceFiles/img/希洛克/'+str(item*3+1)+'.gif'))
            elif 数量[2] == 1 and i == 9:
                for item in range(5):
                    if self.希洛克选择状态[item*3+2] > 0:
                        图片列表.append(QMovie('./ResourceFiles/img/希洛克/'+str(item*3+2)+'.gif')) 
            elif (self.武器融合属性A.currentIndex()+self.武器融合属性B.currentIndex() > 0 or self.角色属性B.希洛克武器词条 != 0) and i == 11:
                # 图片列表.append(QMovie('./ResourceFiles/img/希洛克/融-7.gif'))
                图片列表.append(QMovie('./ResourceFiles/img/希洛克/武器/'+ str(装备序号[self.排行数据[index][i]]) +'.gif'))    
            else:          
                图片列表.append(self.装备图片[装备序号[self.排行数据[index][i]]])
    
        偏移量=187
        x坐标=[32,0,0,32,0,偏移量,偏移量+32,偏移量+32,偏移量,偏移量,偏移量+32,32]
        y坐标=[0,0,32,32,64,0,0,32,64,32,64,64]
    
        tempstr = self.装备描述_BUFF计算(self.角色属性B)

        for i in range(0,12):
            装备图标=QLabel(输出窗口)
            装备图标.setMovie(图片列表[i])
            图片列表[i].start()
            装备图标.resize(26,26)
            装备图标.move(初始x+x坐标[i],初始y+y坐标[i])
            装备图标.setAlignment(Qt.AlignCenter) 
            装备 =  装备列表[装备序号[self.角色属性B.装备栏[i]]]
            if self.角色属性B.装备栏[i] == 百变怪:
                图标遮罩=QLabel(输出窗口)
                图标遮罩.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                图标遮罩.resize(26,26)
                图标遮罩.move(初始x+x坐标[i],初始y+y坐标[i])
                图标遮罩.setToolTip(tempstr[i])
            else:
                装备图标.setToolTip(tempstr[i])

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

    def 装备描述_BUFF计算(self, 属性):
        tempstr=[]
        数量 = [0] * 3
        for i in range(15):
            数量[i % 3] += self.希洛克选择状态[i]
        for i in range(0,12):
            装备 =  装备列表[装备序号[属性.装备栏[i]]]
            tempstr.append('<font size="3" face="宋体"><font color="' + 颜色[装备.品质] + '">' +装备.名称+'</font><br>')
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
                x = 属性.防具精通计算(i)
                tempstr[i] +='<br>防具精通: '
                for n in 属性.防具精通属性:
                    if n != '体力':
                        tempstr[i] += n + ' +' + str(2 * x) + ' '
                    else:
                        tempstr[i] += n + ' +' + str(x) + ' '

            if 装备.所属套装 != '智慧产物':  
                if 属性.强化等级[i]!=0:
                    if i in [9,10]:
                        tempstr[i]+='<br><font color="#68D5ED">+'+str(属性.强化等级[i])+' 强化: '
                        tempstr[i]+='四维 + '+str(左右计算(100,装备.品质,属性.强化等级[i])) +'</font>'

                if 属性.武器锻造等级 != 0:
                    if i==11:
                        tempstr[i]+='<br><font color="#68D5ED">+'+str(属性.武器锻造等级)+'   锻造: '
                        tempstr[i]+='四维 + '+str(锻造四维(装备.等级,装备.品质,属性.武器锻造等级))+'</font>'
                 
                if 属性.是否增幅[i]==1:
                    if tempstr[i] !='':
                        tempstr[i]+='<br>'
                    tempstr[i]+='<font color="#FF00FF">+'+str(属性.强化等级[i])+' 增幅: '
                    if '体力' in 属性.类型:
                        tempstr[i]+='异次元体力 + '+str(增幅计算(装备.等级,装备.品质,属性.强化等级[i],属性.增幅版本))+'</font>'
                    elif '精神' in 属性.类型:
                        tempstr[i]+='异次元精神 + '+str(增幅计算(装备.等级,装备.品质,属性.强化等级[i],属性.增幅版本))+'</font>'
                    elif '智力' in 属性.类型:
                        tempstr[i]+='异次元智力 + '+str(增幅计算(装备.等级,装备.品质,属性.强化等级[i],属性.增幅版本))+'</font>'

            if tempstr[i] != '':
                tempstr[i] += '<br>'
            tempstr[i] += 装备.装备描述_BUFF(属性)[:-4]

            if 数量[0] == 1 and i == 2:
                tempstr[i]+='<br>'
                tempstr[i]+='<font color="#00A2E8">希洛克融合属性</font><br>'
                tempstr[i]+='Lv30 Buff技能 力量、智力增加量 +3%'
            elif 数量[1] == 1 and i == 7:
                tempstr[i]+='<br>'
                tempstr[i]+='<font color="#00A2E8">希洛克融合属性</font><br>'
                tempstr[i]+='Lv50主动技能力量、智力增加量 +3%'
            elif 数量[2] == 1 and i == 9:
                tempstr[i]+='<br>'
                tempstr[i]+='<font color="#00A2E8">希洛克融合属性</font><br>'
                tempstr[i]+='[守护恩赐]体力、精神 +80<br>'
                tempstr[i]+='[启示：圣歌]、[人偶操纵者]智力 +80'

            elif self.角色属性B.希洛克武器词条 == 1 and i == 11:
                tempstr[i]+='<br>'
                tempstr[i]+='<font color="#00A2E8">希洛克融合属性</font><br>'
                武器词条最高值 = self.角色属性B.自适应最高值
                武器属性A = 武器属性A列表[武器词条最高值[0]]
                武器属性B = 武器属性B列表[武器词条最高值[1]]
                tempstr[i] += "属性1：" +"<font style='color:gray'>"+武器属性A.固定属性描述 + '</font>，' + 武器属性A.随机属性描述 + str(武器属性A.最大值)+ ('%' if 武器属性A.间隔 / 10 < 1 else '')+'<br>'
                if self.角色属性B.武器词条触发 == 1:
                    tempstr[i] += "属性2：" +"<font style='color:gray'>"+武器属性B.固定属性描述 + '</font>，' + 武器属性B.随机属性描述 + str(武器属性B.最大值)+ ('%' if 武器属性B.间隔 / 10 < 1 else '')+'<br>'
            elif self.角色属性B.希洛克武器词条 == 2 and i == 11:
                tempstr[i]+='<br>'
                tempstr[i]+='<font color="#00A2E8">希洛克融合属性</font><br>'
                武器属性A = 武器属性A列表[self.武器融合属性A.currentIndex()]
                武器属性B = 武器属性B列表[self.武器融合属性B.currentIndex()]
                tempstr[i] += "属性1：" +"<font style='color:gray'>"+武器属性A.固定属性描述 + '</font>，' + 武器属性A.随机属性描述 + self.武器融合属性A2.currentText()+'<br>'
                if self.角色属性B.武器词条触发 == 1:
                    tempstr[i] += "属性2：" +"<font style='color:gray'>"+武器属性B.固定属性描述 + '</font>，' + 武器属性B.随机属性描述 + self.武器融合属性B2.currentText()+'<br>'

            # elif self.希洛克武器词条[0].currentIndex() > 0 and i == 11:
            #     tempstr[i]+='<br>'
            #     tempstr[i]+='<font color="#00A2E8">希洛克融合属性</font><br>'
            #     if self.希洛克武器词条[0].currentIndex() == 1:
            #         tempstr[i]+="属性1：{} +10%<br>".format(武器词条属性[属性.词条选择[0]])
            #         if sum(数量)==3:
            #             tempstr[i]+="属性2：{} +5%<br>".format(武器词条属性[属性.词条选择[1]])
            #     else:
            #         tempstr[i]+="属性1：{} +{}%<br>".format(武器词条属性[self.希洛克武器词条[1].currentIndex()],(self.希洛克武器词条[3].currentIndex() + 3) * 2)
            #         if sum(数量)==3:
            #             tempstr[i]+="属性2：{} +{}%<br>".format(武器词条属性[self.希洛克武器词条[2].currentIndex()],(self.希洛克武器词条[4].currentIndex() + 3) * 1) 
            if tempstr[i].endswith('<br>'): tempstr[i] = tempstr[i][:-4]
            tempstr[i] += '</font>'
        return tempstr

    def 武器融合属性计算(self, 属性):
        武器融合属性A = 武器属性A列表[self.武器融合属性A.currentIndex()]
        武器融合属性B = 武器属性B列表[self.武器融合属性B.currentIndex()]
        武器融合属性A数值 = self.武器融合属性A2.currentText().replace('%','')
        武器融合属性B数值 = self.武器融合属性B2.currentText().replace('%','')
        武器融合属性A.当前值 = int(武器融合属性A数值 if 武器融合属性A数值 != '' else 0)
        武器融合属性A.融合属性(属性)
        if 属性.武器词条触发 == 1:
            武器融合属性B.当前值 = int(武器融合属性B数值 if 武器融合属性B数值 != '' else 0) 
            武器融合属性B.融合属性(属性)

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
            pass # 下装
        if (self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]) == 2:
            pass # 戒指
        if (self.希洛克选择状态[i * 3 + 2] + self.希洛克选择状态[i * 3 + 0]) == 2:
            pass # 辅助装备

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

    def 输入属性(self, 属性, x = 0):
        for i in 属性.技能栏:
            i.等级 = i.基础等级+int(self.等级调整[self.角色属性A.技能序号[i.名称]].currentText())
        
        属性.排行系数 = self.排行参数.currentIndex()
        属性.C力智 = int(self.排行选项[0].currentText().split(':')[1])
        属性.C三攻 = int(self.排行选项[1].currentText().split(':')[1])
        属性.排行类型 = self.排行选项[2].currentText()

        if self.初始属性.三觉序号 != 0:
            if self.觉醒选择状态 == 1:
                属性.技能栏[self.三觉序号].关联技能 = [属性.技能栏[self.一觉序号].名称]
            elif self.觉醒选择状态 == 2:
                属性.技能栏[self.三觉序号].关联技能 = [属性.技能栏[self.二觉序号].名称]            

        if self.切装模式选项.isChecked() and self.计算模式选择.currentIndex() != 2:
            属性.双装备模式 = 1

        count = 0
        for i in 装备列表:
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
        
        if self.护石第一栏.currentText()!= '无':
           属性.护石第一栏 = self.护石第一栏.currentText()

        if self.护石第二栏.currentText()!= '无':
           属性.护石第二栏 = self.护石第二栏.currentText()
        
        if self.护石第三栏.currentText()!= '无':
           属性.护石第三栏 = self.护石第三栏.currentText()
    
        for i in range(0,12):
            属性.是否增幅[i] = self.装备打造选项[i].currentIndex()
            属性.强化等级[i] = self.装备打造选项[i + 12].currentIndex()
            属性.改造等级[i] = self.装备打造选项[i + 24].currentIndex()
        属性.武器锻造等级 = self.装备打造选项[36].currentIndex()
        属性.类型 = self.装备打造选项[37].currentText()
        属性.次数输入.clear()
        for i in self.角色属性A.技能栏:
            序号 = self.角色属性A.技能序号[i.名称]
            属性.次数输入.append(self.次数输入[序号].currentText())
        self.希洛克属性计算(属性)
        self.基础属性(属性)

    def 技能加成判断(self, name, 属性):
        if name == 'Lv1-30(主动)Lv+1':
            属性.技能等级加成('主动',1,30,1)
            return
        if name == 'Lv1-50(主动)Lv+1':
            属性.技能等级加成('主动',1,50,1)
            return
        if name == 'Lv1-35(主动)Lv+1':
            属性.技能等级加成('主动',1,35,1)
            return
        if name == 'Lv30-50(主动)Lv+1':
            属性.技能等级加成('主动',30,50,1)
            return
        if name == 'Lv1-30(所有)Lv+1':
            属性.技能等级加成('所有',1,30,1)
            return
        if name == 'Lv1-50(所有)Lv+1':
            属性.技能等级加成('所有',1,50,1)
            return
        if name == 'Lv1-20(所有)Lv+1':
            属性.技能等级加成('所有',1,20,1)
            return
        if name == 'Lv20-30(所有)Lv+1':
            属性.技能等级加成('所有',20,30,1)
            return
        if name == 'Lv1-80(所有)Lv+1':
            属性.技能等级加成('所有',1,80,1)
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
            if name == i.名称+'Lv+1':
                i.等级加成(1)
                return
    
    def 基础属性(self, 属性):
        for i in range(0, 3):
            for j in range(0, 16):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except:
                        QMessageBox.information(self, "错误",
                                                self.行名称[j + 17 if i > 2 else j] + "：" + self.列名称[i] + "  输入格式错误，已重置为空")
                        self.属性设置输入[i][j].setText('')
        for i in range(3, 9):
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except:
                        QMessageBox.information(self, "错误",
                                                self.行名称[j + 17 if i > 2 else j] + "：" + self.列名称[i] + "  输入格式错误，已重置为空")
                        self.属性设置输入[i][j].setText('')

        temp = []
        for j in range(0, len(self.属性设置输入[9])):

            if self.属性设置输入[9][j].text() != '' and j in [1,2,5]:
                try:
                    temp.append(float(self.属性设置输入[9][j].text()) / 100)

                    if temp[-1] > 1 or temp[-1] < -.2:
                        QMessageBox.information(self, "错误", self.修正列表名称[j] + " 输入数值超出[-20,100]，已重置为空")
                        temp[-1] = 0.0
                        self.属性设置输入[9][j].setText('')
                except:
                    temp.append(0.0)
                    QMessageBox.information(self, "错误", self.修正列表名称[j] + " 输入格式错误，已重置为空")
                    self.属性设置输入[9][j].setText('')
            elif self.属性设置输入[9][j].text() != '' and j in [0,3,4,6]:
                try:
                    temp.append(int(self.属性设置输入[9][j].text()))
                except:
                    temp.append(0.0)
                    QMessageBox.information(self, "错误", self.修正列表名称[j] + " 输入格式错误，已重置为空")
                    self.属性设置输入[9][j].setText('')
            else:
                temp.append(0.0)
        #神话补正
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
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 3 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 0 and j in [1, 9, 16]:
                        属性.进图智力 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.智力 += int(self.属性设置输入[i][j].text())
        for i in [1, 4, 7]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 4 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 1 and j in [1, 9, 16]:
                        属性.进图体力 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.体力 += int(self.属性设置输入[i][j].text())
        for i in [2, 5, 8]:
            for j in range(0, 17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 5 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 2 and j in [1, 9, 16]:
                        属性.进图精神 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.精神 += int(self.属性设置输入[i][j].text())

        for i in self.技能设置输入:
            self.技能加成判断(i.currentText(), 属性)

        属性.护石计算(属性.护石第一栏)
        属性.护石计算(属性.护石第二栏)
        属性.护石计算(属性.护石第三栏)
