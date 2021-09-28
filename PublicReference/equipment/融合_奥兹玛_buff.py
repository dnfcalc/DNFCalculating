
# 阿斯特罗斯
def Astaroth(self):
    self.BUFF增加(BUFF物攻per=1.01, BUFF魔攻per=1.01, BUFF独立per=1.01)
    self.觉醒增加(一觉力智=22)
    self.被动增加(守护恩赐体精=55, 转职被动智力=55)
    pass

# 贝利亚斯
def Berias(self):
    self.被动增加(守护恩赐体精=138, 转职被动智力=138)
    pass

# 雷德梅恩
def Redmayne(self):
    self.BUFF增加(BUFF力量per=1.02, BUFF智力per=1.02)
    self.觉醒增加(一觉力智=25)
    self.被动增加(守护恩赐体精=46, 转职被动智力=46)

# 罗什巴赫
def Rosenbach(self):
    self.BUFF增加(BUFF力量per=1.01, BUFF智力per=1.01)
    self.BUFF增加(BUFF物攻per=1.01, BUFF魔攻per=1.01, BUFF独立per=1.01)
    self.觉醒增加(一觉力智=37)


# 泰玛特
def Tiamat(self):
    self.BUFF增加(BUFF力量per=1.03, BUFF智力per=1.03)
    self.觉醒增加(一觉力智=21, 一觉力智per=1.01)
    pass


OzmaList = (Astaroth, Berias, Redmayne, Rosenbach, Tiamat)
