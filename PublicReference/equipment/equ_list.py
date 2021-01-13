#装备属性部分
# import json
# import os

装备版本 = "GF"

# with open("ResourceFiles/Config/release_version.json") as fp:
#     versionInfo = json.load(fp)
#     装备版本 = versionInfo['EquipmentVersion']
# fp.close()

from PublicReference.utils.config import *
from .基础函数 import *


# if 装备版本.upper() == "GF":
from .装备_武器 import *
from .装备_防具 import *
from .装备_首饰 import *
from .装备_特殊 import *
from .装备_套装 import *
    
# else:
#     from .装备_武器_HF import *
#     from .装备_防具_HF import *
#     from .装备_首饰_HF import *
#     from .装备_特殊_HF import *
#     from .装备_套装_HF import *


装备列表 = []
i = 0
while i >= 0:
    try: exec('装备列表.append(装备'+str(i)+'())'); i += 1
    except: i = -1

装备序号 = {}
套装映射 = {}
for i in range(len(装备列表)):
    装备序号[装备列表[i].名称] = i
    套装映射[装备列表[i].所属套装 + '-' + 装备列表[i].品质 + '-' + 装备列表[i].部位] = i

套装列表 = []
i = 0
while i >= 0:
    try: exec('套装列表.append(套装效果'+str(i)+'())'); i += 1
    except: i = -1

套装序号 = {}
for i in range(len(套装列表)):
    套装序号[套装列表[i].名称 + '[' + str(套装列表[i].件数) + ']'] = i
