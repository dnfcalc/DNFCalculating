class Siroco:

    def __init__(self) -> None:
        self.pants_fused = False
        self.rings_fused = False
        self.left_fused = False
        self.character = None
        pass

    # 设置属性
    def set_character(self, character):
        self.character = character
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
        self.character.BUFF增加(BUFF力量per=1.03, BUFF智力per=1.03)
        self.pants_fused = True
        pass
    
    # 
    def fuse_ring(self):
        self.character.觉醒增加(一觉力智per=1.03)
        self.rings_fused = True

    def fuse_left(self):
        self.character.被动增加(守护恩赐体精=80, 转职被动智力=80)
        self.left_fused = True

    def compute(self):
        if self.pants_fused and self.rings_fused:
            self.force_pants()
        if self.rings_fused and self.left_fused:
            self.force_ring()
        if self.left_fused and self.pants_fused:
            self.force_left()

        self.pants_fused = False
        self.rings_fused = False
        self.left_fused = False
        self.character = None

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
        self.character.觉醒增加(一觉力智=40)

    def force_ring(self):
        self.character.BUFF增加(
            BUFF物攻per=1.02,
            BUFF魔攻per=1.02,
            BUFF独立per=1.02
        )

    def force_left(self):
        self.character.被动进图加成 += 80
        pass

    pass

# 暗杀者
class Assassin(Siroco):

    def force_pants(self):
        self.character.觉醒增加(一觉力智=28)

    def force_rings(self):
        self.character.BUFF增加(
            BUFF物攻per=1.01,
            BUFF魔攻per=1.01,
            BUFF独立per=1.01,
            BUFF力量per=1.01,
            BUFF智力per=1.01
        )

    def force_left(self):
        self.character.被动进图加成 += 55
        pass

    pass

# 卢克西
class Roxy(Siroco):
    pass


# 守门人
class Nameless(Siroco):
    def force_pants(self):
        self.character.觉醒增加(一觉力智=20,一觉力智per=1.01)

    def force_rings(self):
        self.character.BUFF增加(
            BUFF力量per=1.01,
            BUFF智力per=1.01
        )
        self.character.被动进图加成 += 30

    def force_left(self):
        self.character.被动进图加成 += 55
        pass

# 洛多斯
class Lodos(Siroco):
    def force_pants(self):
        self.character.觉醒增加(一觉力智per=1.02)

    def force_rings(self):
        self.character.BUFF增加(
            BUFF力量per=1.02,
            BUFF智力per=1.02
        )

    def force_left(self):
        self.character.BUFF增加(
            BUFF物攻per=1.01,
            BUFF魔攻per=1.01,
            BUFF独立per=1.01,
        )
        self.character.被动进图加成 += 30
        pass


SirocoList = (Nex(), Assassin(), Roxy(), Nameless(), Lodos())

