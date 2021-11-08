from .描述_buff import BUFF增加


def Talismans(self, i):
    values = [0, 0.02, 0.04, 0.06, 0.08]
    value = round(1 + values[i], 2)
    BUFF增加(self, BUFF力量per=value, BUFF智力per=value)
