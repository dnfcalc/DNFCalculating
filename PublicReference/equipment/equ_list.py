#装备属性部分

from PublicReference.utils.config import *
from .装备_武器 import *
from .装备_防具 import *
from .装备_首饰 import *
from .装备_特殊 import *
from .装备_套装 import *
from .基础函数 import *


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
