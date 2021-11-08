from .描述_buff import *

# 阿斯特罗斯


def Astaroth(self):
    return BUFF增加(self, BUFF三攻per=1.01) + 觉醒增加(self, 一觉力智=22) + 被动增加(
        self, 守护恩赐体精=55, 转职被动智力=55)


# 贝利亚斯


def Berias(self):
    return 被动增加(self, 守护恩赐体精=138, 转职被动智力=138)


# 雷德梅恩


def Redmayne(self):
    return BUFF增加(self, BUFF力智per=1.02) + 觉醒增加(self, 一觉力智=25) + 被动增加(
        self, 守护恩赐体精=46, 转职被动智力=46)


# 罗什巴赫


def Rosenbach(self):
    return BUFF增加(self, BUFF力智per=1.01, BUFF三攻per=1.01) + 觉醒增加(self, 一觉力智=37)


# 泰玛特


def Tiamat(self):
    return BUFF增加(self, BUFF力智per=1.03) + 觉醒增加(self, 一觉力智=21, 一觉力智per=1.01)


OzmaList = (Astaroth, Berias, Redmayne, Rosenbach, Tiamat)
