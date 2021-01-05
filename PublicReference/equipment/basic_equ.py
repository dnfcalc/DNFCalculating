from PublicReference.utils.config import *
from PublicReference.equipment.equ_list import *

class 装备:
    名称 = ''
    模式 = 0
    图片ID = ''
    所属套装 = ''
    等级 = 0
    品质 = ''
    部位 = ''
    类型 = ''
    力量 = 0
    智力 = 0
    体力 = 0
    精神 = 0
    属性描述 = ""
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0
    属性1描述 = '无'
    属性1范围 = []
    属性1选择 = 0
    属性2描述 = '无'
    属性2范围 = []
    属性2选择 = 0
    属性3描述 = '无'
    属性3范围 = []
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0
    def 城镇属性(self, 属性):
        pass
    def 城镇属性_BUFF(self, 属性):
        pass
    def 进图属性(self, 属性):
        pass
    def 产物升级(self,属性):
        pass
    def 进图属性_BUFF(self, 属性):
        pass
    def 变换属性(self,属性):
        pass
    def 变换属性_BUFF(self,属性):
        pass
    def 其它属性(self, 属性):
        pass
    def 其它属性_BUFF(self, 属性):
        pass
    def BUFF属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        if self.部位 in ['上衣','下装','腰带','头肩','鞋']:
            self.属性描述 += ('力量 +{}<br>'.format(self.力量[属性.防具类型])) if self.力量[属性.防具类型] > 0 else '' 
            self.属性描述 += ('智力 +{}<br>'.format(self.智力[属性.防具类型])) if self.智力[属性.防具类型] > 0 else ''             
        else:
            self.属性描述 += ('力量 +{}<br>'.format(self.力量)) if self.力量 > 0 else '' 
            self.属性描述 += ('智力 +{}<br>'.format(self.智力)) if self.智力 > 0 else ''        
        self.属性描述 += ('物理攻击力 +{}<br>'.format(self.物理攻击力)) if self.物理攻击力 > 0 else ''
        self.属性描述 += ('魔法攻击力 +{}<br>'.format(self.魔法攻击力)) if self.魔法攻击力 > 0 else ''
        self.属性描述 += ('独立攻击力 +{}<br>'.format(self.独立攻击力)) if self.独立攻击力 > 0 else ''
        self.城镇属性(属性)
        self.属性描述 += '<font color="#00A2E8">进图触发：</font><br>'
        self.进图属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">进图触发：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">进图触发：</font><br>','')
        self.属性描述 += '<font color="#00A2E8">其他属性：</font><br>'
        self.其它属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">其他属性：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">其他属性：</font><br>','')
        self.属性描述 += '<font color="#00A2E8">变换属性：</font><br>'
        self.变换属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">变换属性：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">变换属性：</font><br>','')     
        属性.装备描述 = 0
        return self.属性描述 

    def 装备描述_变换属性(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        if self.部位 in ['上衣','下装','腰带','头肩','鞋']:
            self.属性描述 += ('力量 +{}<br>'.format(self.力量[属性.防具类型])) if self.力量[属性.防具类型] > 0 else '' 
            self.属性描述 += ('智力 +{}<br>'.format(self.智力[属性.防具类型])) if self.智力[属性.防具类型] > 0 else ''             
        else:
            self.属性描述 += ('力量 +{}<br>'.format(self.力量)) if self.力量 > 0 else '' 
            self.属性描述 += ('智力 +{}<br>'.format(self.智力)) if self.智力 > 0 else ''        
        self.属性描述 += ('物理攻击力 +{}<br>'.format(self.物理攻击力)) if self.物理攻击力 > 0 else ''
        self.属性描述 += ('魔法攻击力 +{}<br>'.format(self.魔法攻击力)) if self.魔法攻击力 > 0 else ''
        self.属性描述 += ('独立攻击力 +{}<br>'.format(self.独立攻击力)) if self.独立攻击力 > 0 else ''
        self.城镇属性(属性)
        self.属性描述 += '<font color="#00A2E8">进图触发：</font><br>'
        self.进图属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">进图触发：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">进图触发：</font><br>','')
        self.属性描述 += '<font color="#00A2E8">其他属性：</font><br>'
        self.其它属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">其他属性：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">其他属性：</font><br>','')
        self.属性描述 += '<font color="#00A2E8">变换属性：</font><br>'
        # self.变换属性(属性)
        # if self.属性描述.endswith('<font color="#00A2E8">变换属性：</font><br>'):
        #     self.属性描述 = self.属性描述.replace('<font color="#00A2E8">变换属性：</font><br>','')     
        属性.装备描述 = 0
        return self.属性描述 

    def 装备描述_BUFF(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        if self.部位 not in ['上衣','下装','腰带','头肩','鞋']:
            if (属性.角色 == '圣职者(女)' or 属性.角色 == '魔法师(女)') :
                self.属性描述 += ('智力 +{}<br>'.format(self.智力)) if self.智力 > 0 else ''
            else:
                self.属性描述 += ('体力 +{}<br>'.format(self.体力)) if self.体力 > 0 else ''
                self.属性描述 += ('精神 +{}<br>'.format(self.精神)) if self.精神 > 0 else '' 
        self.城镇属性_BUFF(属性)
        self.属性描述 += '<font color="#00A2E8">辅助职业专属属性:</font><br>'
        self.BUFF属性(属性)
        self.属性描述 += '<font color="#00A2E8">进图触发：</font><br>'
        self.进图属性_BUFF(属性)
        if self.属性描述.endswith('<font color="#00A2E8">进图触发：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">进图触发：</font><br>','')
        self.属性描述 += '<font color="#00A2E8">其他属性：</font><br>'
        self.其它属性_BUFF(属性)
        if self.属性描述.endswith('<font color="#00A2E8">其他属性：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">其他属性：</font><br>','')        
        属性.装备描述 = 0
        return self.属性描述 

    def 图片ID(self):
        if self.图片ID == '':
            return self.__class__.__name__.replace('装备','')
        else:
            return self.图片ID

class 改造产物(装备):
    模式 = 1
    所属套装 = '智慧产物'
    等级 = 100
    品质 = '史诗'
    力量 = 0
    智力 = 0
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0
    关联套装 = ''
    def 基础属性(self, 属性):
        pass
    def 改造属性(self, 属性, x):
        pass
    def 城镇属性(self, 属性):
        # 后续解决
        # for i in 属性.装备栏:
        #     if 装备列表[装备序号[i]].所属套装 in self.关联套装:
        #         属性.力量 += 100
        #         属性.智力 += 100
        # self.基础属性(属性)
        pass
    def 进图属性(self, 属性):
        if self.关联套装 in 属性.套装栏:
            self.改造属性(属性, 属性.获取改造(self.部位))
        pass
    def 其它属性(self, 属性):
        pass
    def 装备描述(self, 属性):
        temp = ''
        return temp

class 套装:
    属性描述 = ''
    def 城镇属性(self, 属性):
        pass;
    def 城镇属性_BUFF(self, 属性):
        pass;
    def 进图属性(self, 属性):
        pass;
    def 进图属性_BUFF(self, 属性):
        pass;
    def 其它属性(self, 属性):
        pass;
    def 其它属性_BUFF(self, 属性):
        pass;
    def 装备描述(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        self.城镇属性(属性)
        self.属性描述 += '<font color="#00A2E8">进图触发：</font><br>'
        self.进图属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">进图触发：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">进图触发：</font><br>','')
        self.属性描述 += '<font color="#00A2E8">其他属性：</font><br>'
        self.其它属性(属性)
        if self.属性描述.endswith('<font color="#00A2E8">其他属性：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">其他属性：</font><br>','')        
        属性.装备描述 = 0
        return self.属性描述 
    def 装备描述_BUFF(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        self.城镇属性_BUFF(属性)
        self.属性描述 += '<font color="#00A2E8">辅助职业专属属性:</font><br>'
        self.BUFF属性(属性)
        self.属性描述 += '<font color="#00A2E8">进图触发：</font><br>'
        self.进图属性_BUFF(属性)
        if self.属性描述.endswith('<font color="#00A2E8">进图触发：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">进图触发：</font><br>','')
        self.属性描述 += '<font color="#00A2E8">其他属性：</font><br>'
        self.其它属性_BUFF(属性)
        if self.属性描述.endswith('<font color="#00A2E8">其他属性：</font><br>'):
            self.属性描述 = self.属性描述.replace('<font color="#00A2E8">其他属性：</font><br>','')        
        属性.装备描述 = 0
        return self.属性描述 
    def BUFF属性(self, 属性):
        pass;