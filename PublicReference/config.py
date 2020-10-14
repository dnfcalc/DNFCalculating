import configparser
from PublicReference.constant import *

conf = configparser.ConfigParser()

#基础设置##################################################################
try:
    conf.read('./ResourceFiles/Config/基础设置.ini', encoding='utf-8')
except:
    conf.read('./ResourceFiles/Config/基础设置.ini', encoding='gbk')
    
#窗口缩放
try:
    窗口显示模式 = conf.getint('窗口显示', 'value')
except:
    窗口显示模式 = 0

#切装模式
try:
    切装模式 = conf.getint('切装模式', 'value')
except:
    切装模式 = 0

#补全模式
try:
    补全模式 = conf.getint('补全模式', 'value')
except:
    补全模式 = 1

#不计算装备属性，武器类型为角色武器选项第一个
try:
    调试开关 = conf.getint('调试开关', 'value')
except:
    调试开关 = 0

#输出搭配和伤害数据到csv
try:
    输出数据 = conf.getint('输出数据', 'value')
except:
    输出数据 = 0

if 输出数据 == 1:
    if not os.path.exists('./数据记录'):
        os.makedirs('./数据记录') 

#控制夜语黑瞳武器是否显示在第一页
try:
    普雷武器显示 =  1 - conf.getint('夜语黑瞳', 'value')
except:
    普雷武器显示 = 1

#排行里每把武器只会出现一次
try:
    武器排名 = conf.getint('武器排名', 'value') 
except:
    武器排名 = 0

#武器序号
try:
    武器序号 = conf.getint('武器序号', 'value')
except:
    武器序号 = -1

#天劫
try:
    天劫减防 = conf.getint('天劫', '减防生效')
    天劫减抗 = conf.getint('天劫', '减抗生效')
except:
    天劫减防 = 0 
    天劫减抗 = 0

#战术之王的御敌套装
try:
    战术白字 = conf.getint('战术之王的御敌', '套装附加') / 100
except:
    战术白字 = 0.40

#天御之灾
try:
    天御套装 = conf.getint('天御之灾', '套装属性')
except:
    天御套装 = 0

#千蛛碎影减防
try:
    千蛛减防 = conf.getint('千蛛碎影', '减防生效')
except:
    千蛛减防 = 0


#攻击目标##################################################################
try:
    conf.read('./ResourceFiles/Config/攻击目标.ini', encoding='utf-8')
except:
    conf.read('./ResourceFiles/Config/攻击目标.ini', encoding='gbk')

#怪物属性
攻击目标 = []
for i in range(100):
    try: 
        temp = []
        item = 'item' + str(i)
        temp.append(conf.get(item, '名称'))
        temp.append(conf.getint(item, '防御'))
        temp.append(conf.getint(item, '火抗'))
        temp.append(conf.getint(item, '冰抗'))
        temp.append(conf.getint(item, '光抗'))
        temp.append(conf.getint(item, '暗抗'))
        攻击目标.append(temp)
    except: 
        break

if len(攻击目标) == 0:
    攻击目标 = [['120沙袋(绿)', 443243, 0, 0, 0, 0]]
