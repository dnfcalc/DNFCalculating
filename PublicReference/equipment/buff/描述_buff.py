from PublicReference.utils.common import to_percent


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
           BUFF独立per=1,
           BUFF力智=0,
           BUFF三攻=0,
           BUFF力智per=1,
           BUFF三攻per=1,
           ):

    if BUFF力智 > 0:
        BUFF力量 += BUFF力智
        BUFF智力 += BUFF力智
    if BUFF三攻 > 0:
        BUFF物攻 += BUFF三攻
        BUFF魔攻 += BUFF三攻
        BUFF独立 += BUFF三攻
    if BUFF力智per > 0:
        BUFF力量per *= BUFF力智per
        BUFF智力per *= BUFF力智per
    if BUFF三攻per > 0:
        BUFF物攻per *= BUFF三攻per
        BUFF魔攻per *= BUFF三攻per
        BUFF独立per *= BUFF三攻per

    buff_name = 'Lv30 Buff技能'

    if self is not None:
        if self.装备描述 == 0:
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
        buff_name = '[{}]'.format(self.技能表['BUFF'].名称)
    tem = ''
    if BUFFLv > 0:
        tem += '{}Lv +{}<br>'.format(buff_name, int(BUFFLv))
    if BUFF力量 > 0 and BUFF智力 > 0:
        tem += '{}力量、智力增加量 +{}<br>'.format(buff_name, int(BUFF力量))
    elif BUFF力量 > 0:
        tem += '{}力量增加量 +{}<br>'.format(buff_name, int(BUFF力量))
    elif BUFF智力 > 0:
        tem += '{}智力增加量 +{}<br>'.format(buff_name, int(BUFF智力))

    if BUFF力量per > 1 and BUFF智力per > 1:
        tem += '{}力量、智力增加量 +{}<br>'.format(buff_name,
                                            to_percent(BUFF力量per - 1))
    elif BUFF力量per > 1:
        tem += '{}力量增加量 +{}<br>'.format(buff_name, to_percent(BUFF力量per - 1))
    elif BUFF智力per > 1:
        tem += '{}智力增加量 +{}<br>'.format(buff_name, to_percent(BUFF智力per - 1))

    if BUFF物攻 > 0 and BUFF魔攻 > 0 and BUFF独立 > 0:
        tem += '{}物理、魔法、独立攻击力增加量 +{}<br>'.format(buff_name, int(BUFF物攻))
    elif BUFF物攻 > 0:
        tem += '{}物理攻击力增加量 +{}<br>'.format(buff_name, int(BUFF物攻))
    elif BUFF魔攻 > 0:
        tem += '{}魔法攻击力增加量 +{}<br>'.format(buff_name, int(BUFF魔攻))
    elif BUFF独立 > 0:
        tem += '{}独立攻击力增加量 +{}<br>'.format(buff_name, int(BUFF独立))

    if BUFF物攻per > 1 and BUFF魔攻per > 1 and BUFF独立per > 1:
        tem += '{}物理、魔法、独立攻击力增加量 +{}<br>'.format(
            buff_name,
            to_percent(BUFF物攻per - 1))
    elif BUFF物攻per > 1:
        tem += '{}物理攻击力增加量 +{}<br>'.format(
            buff_name,
            to_percent(BUFF物攻per - 1))
    elif BUFF魔攻per > 1:
        tem += '{}魔法攻击力增加量 +{}<br>'.format(
            buff_name,
            to_percent(BUFF魔攻per - 1))
    elif BUFF独立per > 1:
        tem += '{}独立攻击力增加量 +{}<br>'.format(
            buff_name,
            to_percent(BUFF独立per - 1))
    return tem


def 觉醒增加(self, 一觉Lv=0, 一觉力智=0, 一觉力智per=1):
    awake_name = 'Lv50主动技能'
    if self is not None:
        if self.装备描述 == 0:
            self.一觉Lv += 一觉Lv
            self.一觉力智 += 一觉力智
            self.一觉力智per *= 一觉力智per
        awake_name = '[{}]'.format(self.技能表['一次觉醒'].名称)
    tem = ''

    if 一觉Lv > 0:
        tem += '{} Lv +{}<br>'.format(awake_name, int(一觉Lv))
    if 一觉力智 > 0:
        tem += '{}力量、智力增加量 +{}<br>'.format(awake_name, int(一觉力智))
    if 一觉力智per > 1:
        tem += '{}力量、智力增加量 +{}<br>'.format(awake_name, to_percent(一觉力智per - 1))
    return tem


def 力智固定加成(self, x=0):
    if self is not None:
        if self.装备描述 == 0:
            self.力量 += x
            self.智力 += x
        if self.类型 not in ['力量', '智力']:
            return ''
    return '力量、智力 +{}<br>'.format(x)


def 体精固定加成(self, x=0):
    if self is not None:
        if self.装备描述 == 0:
            self.体力 += x
            self.精神 += x
        if self.类型 not in ['体力', '精神']:
            return ''
    return '体力、精神 +{}<br>'.format(x)


def 被动增加(self,
         转职被动Lv=0,
         转职被动智力=0,
         守护恩赐体精=0,
         信念光环体精=0,
         一觉被动Lv=0,
         一觉被动力智=0,
         被动进图加成=0
         ):
    角色 = None
    if self is not None:
        if self.装备描述 == 0:
            self.转职被动Lv += 转职被动Lv
            self.守护恩赐体精 += 守护恩赐体精
            self.转职被动智力 += 转职被动智力
            self.一觉被动Lv += 一觉被动Lv
            self.信念光环体精 += 信念光环体精
            self.一觉被动力智 += 一觉被动力智
            self.被动进图加成 += 被动进图加成
        角色 = self.角色
    tem = ''

    转职被动 = {'圣职者(男)': '[守护恩赐]', '圣职者(女)': '[启示:圣歌]',
            '魔法师(女)': '[人偶操纵者]', 'None': '[守护恩赐]、[启示:圣歌]、[人偶操纵者]'}[str(角色)]

    if 转职被动Lv > 0:
        tem += '{}技能Lv +{}<br>'.format(转职被动, int(转职被动Lv))

    if 被动进图加成 > 0:
        转职被动智力 += 被动进图加成
        信念光环体精 += 被动进图加成

    if 角色 == '圣职者(男)' or 角色 is None:
        if 守护恩赐体精 > 0:
            tem += '[守护恩赐]体力、精神 +{}<br>'.format(int(守护恩赐体精))
        if 一觉被动Lv > 0:
            tem += '[信念光环]技能Lv +{}'.format(int(一觉被动Lv))
        if 一觉被动力智 > 0:
            tem += '[信念光环]体力、精神增加量 +{}<br>'.format(int(一觉被动力智))
    if 角色 in ['圣职者(女)', '魔法师(女)'] or 角色 is None:
        觉醒被动 = {'圣职者(女)': '[虔诚信念]', '魔法师(女)': '[少女的爱]',
                'None': '[虔诚信念]、[少女的爱]'}[str(角色)]
        if 转职被动智力 > 0:
            tem += '{}智力 +{}<br>'.format(转职被动, int(转职被动智力))
        if 一觉被动Lv > 0:
            tem += '{}技能Lv +{}<br>'.format(觉醒被动, int(一觉被动Lv))
        if 一觉被动力智 > 0:
            tem += '{}力量、智力增加量 +{}<br>'.format(觉醒被动, int(一觉被动力智))
    return tem


def tooltip_trim(tempstr):
    if tempstr.endswith('<br>'):
        tempstr = tempstr[:-4]
    return tempstr