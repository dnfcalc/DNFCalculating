from PublicReference.equipment.equ_list import *
from PublicReference.equipment.防具基础 import 设置防具基础
from PublicReference.utils.config import trans, 千蛛减防, 天御套装, 战术白字, 天劫光环, 普雷武器显示

进图触发title = trans('<font color="#00A2E8">{进图触发}：</font><br>')
其他属性title = trans('<font color="#00A2E8">{其他属性}：</font><br>')
遴选属性title = trans('<font color="#00A2E8">{遴选属性}：</font><br>')
辅助属性title = trans('<font color="#00A2E8">{辅助职业专属属性}：</font><br>')
改造遴选title = trans('<font color="#FF8200">{遴选属性}：</font><br>')
神话属性title = trans('<font color="#00A2E8">{神话属性}：</font><br>')
期望属性title = trans('<font color="#00A2E8">{期望属性}:</font><br>')
改造属性title = trans('<font color="#FF8200">{改造属性}(+$)：</font><br>')


class 装备:
    名称 = ''
    模式 = 0
    图片ID = ''
    所属套装 = ''
    所属套装2 = '无'
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

    def __init__(self) -> None:
        if self.部位 in ['上衣', '下装', '腰带', '头肩', '鞋']:
            设置防具基础(self)
        pass

    def 城镇属性(self, 属性):
        pass

    def 城镇属性_BUFF(self, 属性):
        pass

    def 进图属性(self, 属性):
        pass

    def 产物升级(self, 属性):
        pass

    def 进图属性_BUFF(self, 属性):
        pass

    def 变换属性(self, 属性):
        pass

    def 变换属性_BUFF(self, 属性):
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

        力量 = 0
        智力 = 0

        if self.部位 in ['上衣', '下装', '腰带', '头肩', '鞋']:
            力量 = self.力量[属性.防具类型]
            智力 = self.智力[属性.防具类型]
        else:
            力量 = self.力量
            智力 = self.智力

        self.属性描述 += ('{} +{}<br>'.format(trans('力量'), 力量)) if 力量 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(trans('智力'), 智力)) if 智力 > 0 else ''

        self.属性描述 += ('{} +{}<br>'.format(
            trans('物理攻击力'), self.物理攻击力)) if self.物理攻击力 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(
            trans('魔法攻击力'), self.魔法攻击力)) if self.魔法攻击力 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(
            trans('独立攻击力'), self.独立攻击力)) if self.独立攻击力 > 0 else ''

        self.城镇属性(属性)
        self.属性描述 += 进图触发title
        self.进图属性(属性)
        if self.属性描述.endswith(进图触发title):
            self.属性描述 = self.属性描述.replace(进图触发title, '')
        self.属性描述 += 其他属性title
        self.其它属性(属性)
        if self.属性描述.endswith(其他属性title):
            self.属性描述 = self.属性描述.replace(其他属性title, '')
        self.属性描述 += 遴选属性title
        self.变换属性(属性)
        if self.属性描述.endswith(遴选属性title):
            self.属性描述 = self.属性描述.replace(遴选属性title, '')
        属性.装备描述 = 0
        return self.属性描述

    def 装备描述_变换属性(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        力量 = 0
        智力 = 0
        if self.部位 in ['上衣', '下装', '腰带', '头肩', '鞋']:
            力量 = self.力量[属性.防具类型]
            智力 = self.智力[属性.防具类型]
        else:
            力量 = self.力量
            智力 = self.智力

        self.属性描述 += ('{} +{}<br>'.format(trans('力量'), 力量)) if 力量 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(trans('智力'), 智力)) if 智力 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(
            trans('物理攻击力'), self.物理攻击力)) if self.物理攻击力 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(
            trans('魔法攻击力'), self.魔法攻击力)) if self.魔法攻击力 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(
            trans('独立攻击力'), self.独立攻击力)) if self.独立攻击力 > 0 else ''

        self.城镇属性(属性)
        self.属性描述 += 进图触发title
        self.进图属性(属性)
        if self.属性描述.endswith(进图触发title):
            self.属性描述 = self.属性描述.replace(进图触发title, '')
        self.属性描述 += 其他属性title
        self.其它属性(属性)
        if self.属性描述.endswith(其他属性title):
            self.属性描述 = self.属性描述.replace(其他属性title, '')
        self.属性描述 += 遴选属性title
        属性.装备描述 = 0
        return self.属性描述

    def 装备描述_BUFF(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        智力 = 0
        力量 = 0
        体力 = 0
        精神 = 0
        if self.部位 in ['上衣', '下装', '腰带', '头肩', '鞋']:
            智力 = self.智力['板甲']
            力量 = self.力量['板甲']
            体力 = self.体力['板甲']
            精神 = self.精神['板甲']
        else:
            智力 = self.智力
            力量 = self.力量
            体力 = self.体力
            精神 = self.精神

        self.属性描述 += ('{} +{}<br>'.format(trans("智力"), 智力)) if 智力 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(trans('力量'), 力量)) if 力量 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(trans('体力'), 体力)) if 体力 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(trans('精神'), 精神)) if 精神 > 0 else ''

        self.城镇属性_BUFF(属性)
        self.属性描述 += 辅助属性title
        self.BUFF属性(属性)
        self.属性描述 += 进图触发title
        self.进图属性_BUFF(属性)
        if self.属性描述.endswith(进图触发title):
            self.属性描述 = self.属性描述.replace(进图触发title, '')
        self.属性描述 += 其他属性title
        self.其它属性_BUFF(属性)
        if self.属性描述.endswith(其他属性title):
            self.属性描述 = self.属性描述.replace(其他属性title, '')
        属性.装备描述 = 0
        return self.属性描述

    def 装备描述_变换属性_BUFF(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''

        智力 = 0
        力量 = 0
        体力 = 0
        精神 = 0
        if self.部位 in ['上衣', '下装', '腰带', '头肩', '鞋']:
            智力 = self.智力['板甲']
            力量 = self.力量['板甲']
            体力 = self.体力['板甲']
            精神 = self.精神['板甲']
        else:
            智力 = self.智力
            力量 = self.力量
            体力 = self.体力
            精神 = self.精神

        self.属性描述 += ('{} +{}<br>'.format(trans("智力"), 智力)) if 智力 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(trans('力量'), 力量)) if 力量 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(trans('体力'), 体力)) if 体力 > 0 else ''
        self.属性描述 += ('{} +{}<br>'.format(trans('精神'), 精神)) if 精神 > 0 else ''

        self.城镇属性_BUFF(属性)
        self.属性描述 += 辅助属性title
        self.BUFF属性(属性)
        self.属性描述 += 进图触发title
        self.进图属性_BUFF(属性)
        if self.属性描述.endswith(进图触发title):
            self.属性描述 = self.属性描述.replace(进图触发title, '')
        self.属性描述 += 其他属性title
        self.其它属性_BUFF(属性)
        if self.属性描述.endswith(其他属性title):
            self.属性描述 = self.属性描述.replace(其他属性title, '')
        self.属性描述 += 遴选属性title
        属性.装备描述 = 0
        return self.属性描述

    def 图片ID(self):
        if self.图片ID == '':
            return self.__class__.__name__.replace('装备', '')
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
        pass

    def 城镇属性_BUFF(self, 属性):
        pass

    def 进图属性(self, 属性):
        pass

    def 进图属性_BUFF(self, 属性):
        pass

    def 其它属性(self, 属性):
        pass

    def 其它属性_BUFF(self, 属性):
        pass

    def 装备描述(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''

        self.城镇属性(属性)

        self.属性描述 += 进图触发title
        self.进图属性(属性)
        if self.属性描述.endswith(进图触发title):
            self.属性描述 = self.属性描述.replace(进图触发title, '')
        self.属性描述 += 其他属性title
        self.其它属性(属性)
        if self.属性描述.endswith(其他属性title):
            self.属性描述 = self.属性描述.replace(其他属性title, '')
        属性.装备描述 = 0
        return self.属性描述

    def 装备描述_BUFF(self, 属性):
        属性.装备描述 = 1
        self.属性描述 = ''
        self.城镇属性_BUFF(属性)
        self.属性描述 += 辅助属性title
        self.BUFF属性(属性)
        self.属性描述 += 进图触发title
        self.进图属性_BUFF(属性)
        if self.属性描述.endswith(进图触发title):
            self.属性描述 = self.属性描述.replace(进图触发title, '')
        self.属性描述 += 其他属性title
        self.其它属性_BUFF(属性)
        if self.属性描述.endswith(其他属性title):
            self.属性描述 = self.属性描述.replace(其他属性title, '')
        属性.装备描述 = 0
        return self.属性描述

    def BUFF属性(self, 属性):
        pass
