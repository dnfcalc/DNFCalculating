from .描述_buff import *


class Siroco:
    def __init__(self) -> None:
        self.pants_fused = False
        self.ring_fused = False
        self.left_fused = False
        self.character = None
        self.text = ''
        pass

    # 设置属性
    def set_character(self, character):
        self.character = character
        self.text = ''
        pass

    # 融合
    def fuse(self, index):
        if index == 0:
            self.fuse_pants()
        elif index == 1:
            self.fuse_ring()
        elif index == 2:
            self.fuse_left()
        pass

    # 融合下装
    def fuse_pants(self):
        BUFF增加(self.character, BUFF力智per=1.03)
        self.pants_fused = True
        pass

    #
    def fuse_ring(self):
        觉醒增加(self.character, 一觉力智per=1.03)
        self.ring_fused = True

    def fuse_left(self):
        被动增加(self.character, 守护恩赐体精=80, 转职被动智力=80)
        self.left_fused = True

    def compute(self):
        if self.pants_fused and self.ring_fused:
            self.text += '<font size="3" face="宋体"><font color="#78FF1E">下装+戒指</font><br>'
            self.force_pants()
        if self.ring_fused and self.left_fused:
            self.text += '<font size="3" face="宋体"><font color="#78FF1E">戒指+辅助装备</font><br>'
            self.force_ring()
        if self.left_fused and self.pants_fused:
            self.text += '<font size="3" face="宋体"><font color="#78FF1E">辅助装备+下装</font><br>'
            self.force_left()
        text = self.text
        self.pants_fused = False
        self.ring_fused = False
        self.left_fused = False
        self.character = None
        self.text = ''
        return text

    def force_pants(self):
        pass

    def force_ring(self):
        pass

    def force_left(self):
        pass

    pass


# 奈克斯
class Nex(Siroco):
    def force_pants(self):
        self.text += 觉醒增加(self.character, 一觉力智=40)

    def force_ring(self):
        self.text += 被动增加(self.character, 被动进图加成=80)

    def force_left(self):
        self.text += BUFF增加(self.character, BUFF三攻per=1.02)

    pass


# 暗杀者


class Assassin(Siroco):
    def force_pants(self):
        self.text += 觉醒增加(self.character, 一觉力智=28)

    def force_ring(self):
        self.text += 被动增加(self.character, 被动进图加成=55)

    def force_left(self):
        self.text += BUFF增加(self.character, BUFF力智per=1.01, BUFF三攻per=1.01)

    pass


# 卢克西


class Roxy(Siroco):
    def force_ring(self):
        self.text += "释放Lv50、Lv100主动技能时,所有队员持续伤害+1%,效果持续5秒<br>"

    def force_left(self):
        self.text += "释放Lv50、Lv100主动技能时,所有队员持续伤害+1%,效果持续5秒<br>"

    def force_pants(self):
        self.text += "释放Lv50、Lv100主动技能时,所有队员持续伤害+1%,效果持续5秒<br>"

    pass


# 守门人
class Nameless(Siroco):
    def force_pants(self):
        self.text += 觉醒增加(self.character, 一觉力智=20, 一觉力智per=1.01)

    def force_ring(self):
        self.text += 被动增加(self.character, 被动进图加成=55)

    def force_left(self):
        self.text += BUFF增加(self.character, BUFF力智per=1.01)
        self.text += 被动增加(self.character, 被动进图加成=30)


# 洛多斯


class Lodos(Siroco):
    def force_pants(self):
        self.text += 觉醒增加(self.character, 一觉力智per=1.02)

    def force_ring(self):
        self.text += BUFF增加(self.character, BUFF力智per=1.02)

    def force_left(self):
        self.text += BUFF增加(self.character, BUFF三攻per=1.01)
        self.text += 被动增加(self.character, 被动进图加成=30)
        pass


SirocoList = (Nex(), Assassin(), Roxy(), Nameless(), Lodos())
