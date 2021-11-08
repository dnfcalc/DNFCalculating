# 装备属性部分
# import json
# import os

from PublicReference.utils.constant import *
from .装备_套装 import *
from .装备_特殊 import *
from .装备_首饰 import *
from .装备_防具 import *
from .装备_武器 import *
from .基础函数 import *
from .融合_希洛克 import 希洛克
from .融合_奥兹玛 import 奥兹玛

装备版本 = "GF"

# with open("ResourceFiles/Config/release_version.json") as fp:
#     versionInfo = json.load(fp)
#     装备版本 = versionInfo['EquipmentVersion']
# fp.close()

# if 装备版本.upper() == "GF":

# else:
#     from .装备_武器_HF import *
#     from .装备_防具_HF import *
#     from .装备_首饰_HF import *
#     from .装备_特殊_HF import *
#     from .装备_套装_HF import *


class equipment():
    def __init__(self):
        self.load_equ()
        self.load_suit()

    def load_equ(self):
        self.equ_list = {}
        self.equ_id = {}
        self.equ_tuple = ()
        self.equ_id_tuple = ()
        self.index = {}
        for i in range(535):  #534件装备
            temp = eval('装备{}()'.format(i))
            self.equ_list[i] = temp
            self.equ_id[temp.名称] = i
            self.equ_tuple += (temp, )
            self.equ_id_tuple += (i, )
            key = '{}\t{}\t{}'.format(temp.所属套装, temp.品质, temp.部位)
            self.index[key] = i

    def load_suit(self):
        self.suit_list = {}
        self.suit_id = {}
        self.suit_name = ()
        self.suit_tuple = ()
        for i in range(127):  #126个套装效果
            temp = eval('套装效果{}()'.format(i))
            self.suit_list[i] = temp
            self.suit_tuple += (temp, )
            key = '{}[{}]'.format(temp.名称, temp.件数)
            self.suit_id[key] = i
            self.suit_name += (key, )

    def load_img(self):
        self.equ_img = {}
        #基础装备图标 0~999
        for i in self.get_equ_id_list():
            path = './ResourceFiles/img/装备/{}.gif'.format(i)
            img = QMovie(path)
            img.start()
            self.equ_img[i] = img
        #奥兹玛图标 1000~1024
        for i in range(25):
            path = './ResourceFiles/img/奥兹玛/{}.gif'.format(i)
            img = QMovie(path)
            img.start()
            self.equ_img[1000 + i] = img
        #希洛克图标 1100~1114
        for i in range(15):
            path = './ResourceFiles/img/希洛克/{}.gif'.format(i)
            img = QMovie(path)
            img.start()
            self.equ_img[1100 + i] = img
        #希洛克武器图标 2000~2999
        path = './ResourceFiles/img/希洛克/武器/'
        for i in os.listdir(path):
            img = QMovie(os.path.join(path, i))
            img.start()
            self.equ_img[2000 + int(i.split('.')[0])] = img

    def get_suits_by_equips(self, equips):
        suits = []
        dictionary = {}
        for i in equips:
            item = self.get_equ_by_name(i)
            if item.所属套装2 != '无':
                j = item.所属套装2
                k = item.所属套装
                if k != '智慧产物':
                    dictionary[k] = dictionary.get(k, 0) + 1
            else:
                j = item.所属套装
            if j != '无':
                dictionary[j] = dictionary.get(j, 0) + 1

        for i in dictionary.keys():
            if dictionary[i] >= 2:
                temp = '{}[{}]'.format(i, 2)
                if temp in self.suit_name:
                    suits.append(temp)
                if dictionary[i] >= 3:
                    temp = '{}[{}]'.format(i, 3)
                    if temp in self.suit_name:
                        suits.append(temp)
                    if dictionary[i] >= 5:
                        temp = '{}[{}]'.format(i, 5)
                        if temp in self.suit_name:
                            suits.append(temp)
        for i in suits:
            try:
                temp = i.replace(i.split('[')[0], self.get_suit_by_name(i).子套装)
                if temp in suits:
                    suits.remove(temp)
            except:
                pass
        return suits

    def get_suit_by_id(self, id):
        return self.suit_list.get(id, 套装())

    def get_suit_by_name(self, name):
        return self.get_suit_by_id(self.suit_id.get(name, 0))

    def get_equ_by_id(self, id):
        return self.equ_list.get(id, 装备())

    def get_img_by_id(self, id):
        return self.equ_img.get(id, QMovie(''))

    def get_equ_by_name(self, name):
        return self.get_equ_by_id(self.equ_id.get(name, 0))

    def get_img_by_name(self, name, num=0):
        id = self.equ_id.get(name, 0)
        # if id+num in self.equ_id_tuple:
        id += num
        return self.get_img_by_id(id)

    def get_id_by_name(self, name):
        return self.equ_id.get(name, 0)

    def get_equ_list(self):
        return self.equ_tuple

    def get_suit_list(self):
        return self.suit_tuple

    def get_equ_id_list(self):
        return self.equ_id_tuple

    def get_suit_name(self):
        return self.suit_name

    def get_id_by_index(self, suit, quality, part):
        key = '{}\t{}\t{}'.format(suit, quality, part)
        return self.index.get(key, 0)

    def get_equ_by_index(self, suit, quality, part):
        id = self.get_id_by_index(suit, quality, part)
        return self.get_equ_by_id(id)


equ = equipment()
