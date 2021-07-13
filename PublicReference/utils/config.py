import configparser
import os
import json

global 配置格式有误
global 窗口显示模式
global 切装模式
global 调试开关
global 输出数据
global 普雷武器显示
global 武器排名
global SkinVersion
global 觉醒开关
global 攻击目标

global 天劫光环
global 战术白字

配置格式有误 = False

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


def readDefault():
    data = {}
    with open("ResourceFiles/Config/config.json", encoding='utf-8') as fp:
        setJson = json.load(fp)
        num = 0
        for i in setJson:
            data[str(num)] = i['default']
            num += 1
    fp.close()
    return data


def readSet(filePath):
    data = readDefault()
    if os.path.exists(filePath):
        with open(filePath, encoding='utf-8') as fp:
            setJson = json.load(fp)
            data.update(setJson)
        fp.close()
    return data


setJson = readSet("ResourceFiles/Config/set.json")
窗口显示模式 = setJson['0']
普雷武器显示 = setJson['1']
切装模式 = setJson['2']
输出数据 = setJson['3']
调试开关 = setJson['4']
SkinVersion = ["DNFStyle", "LightStyle", "None"][setJson['5']]
觉醒开关 = setJson['6']
武器排名 = setJson['7']
自动检查更新 = setJson['8']
天劫光环 = setJson['9']
战术白字 = 0.40 + 0.05 * setJson['10']
天御套装 = setJson['11']
千蛛减防 = setJson['12']

if 输出数据 == 1:
    if not os.path.exists('./数据记录'):
        os.makedirs('./数据记录')

#攻击目标##################################################################

readConfig('./ResourceFiles/Config/攻击目标.ini')

# 怪物属性
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
