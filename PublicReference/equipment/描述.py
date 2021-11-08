from PublicReference.utils.common import format_range


def 四维固定加成(self, x, types: list = ['力量', '智力', '体力', '精神']):
    if self is not None:
        if self.装备描述 == 0:
            if '力量' in types:
                self.力量 += x
            if '智力' in types:
                self.智力 += x
            if '体力' in types:
                self.体力 += x
            if '精神' in types:
                self.精神 += x
    return "".join(format_range("{} +{}<br>", types, x))
