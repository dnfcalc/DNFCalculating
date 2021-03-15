import configparser
import os
import json

global 配置格式有误
global 窗口显示模式
global 切装模式
global 补全模式
global 调试开关
global 输出数据
global 普雷武器显示
global 武器排名
global 武器序号
global 天劫减防
global 天劫减抗
global 战术白字
global SkinVersion
global 觉醒开关
global 攻击目标

配置格式有误 = False
窗口显示模式 = 0
切装模式 = 0
补全模式 = 1
调试开关 = 0
输出数据 = 0
普雷武器显示 = 1
武器排名 = 0
武器序号 = -1
天劫减防 = 0 
天劫减抗 = 0
战术白字 = 0.40
SkinVersion = "DNFStyle"
觉醒开关 = 0
攻击目标 = [['120沙袋(绿)', 443243, 0, 0, 0, 0]]

conf = configparser.ConfigParser()

def readConfig(filePath):
    #基础设置##################################################################
    try:
        conf.read(filePath, encoding='utf-8')
    except:
        try:
            conf.read(filePath, encoding='utf-8-sig')
        except:
            配置格式有误 = True
            pass    

readConfig('./ResourceFiles/Config/基础设置.ini')

readConfig('./ResourceFiles/Config/基础设置.ini')

if os.path.exists("ResourceFiles/Config/set.json"):
    with open("ResourceFiles/Config/set.json",encoding='utf-8') as fp:
        setJson = json.load(fp)
        窗口显示模式 = setJson['0']
        普雷武器显示 = setJson['1']
        切装模式 = setJson['2']
        输出数据 = setJson['3']
        if 输出数据 == 1: 
            if not os.path.exists('./数据记录'): os.makedirs('./数据记录') 
        调试开关 = setJson['4']
        SkinVersion = ("DNFStyle" if setJson['5']==0 else ("LightStyle" if setJson['5']==1 else "None"))
        觉醒开关 = setJson['6']
    fp.close()

readConfig('./ResourceFiles/Config/基础设置.ini')
#补全模式
try:
    补全模式 = conf.getint('补全模式', 'value')
except:
    配置格式有误 = True
    补全模式 = 1


#排行里每把武器只会出现一次
try:
    武器排名 = conf.getint('武器排名', 'value') 
except:
    配置格式有误 = True
    武器排名 = 0

#武器序号
try:
    武器序号 = conf.getint('武器序号', 'value')
except:
    配置格式有误 = True
    武器序号 = -1

#天劫
try:
    天劫减防 = conf.getint('天劫', '减防生效')
    天劫减抗 = conf.getint('天劫', '减抗生效')
except:
    配置格式有误 = True
    天劫减防 = 0 
    天劫减抗 = 0

#战术之王的御敌套装
try:
    战术白字 = conf.getint('战术之王的御敌', '套装附加') / 100
except:
    配置格式有误 = True
    战术白字 = 0.40

#天御之灾
try:
    天御套装 = conf.getint('天御之灾', '套装属性')
except:
    配置格式有误 = True
    天御套装 = 0

#千蛛碎影减防
try:
    千蛛减防 = conf.getint('千蛛碎影', '减防生效')
except:
    配置格式有误 = True
    千蛛减防 = 0

#攻击目标##################################################################

readConfig('./ResourceFiles/Config/攻击目标.ini')

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

#攻击目标##################################################################