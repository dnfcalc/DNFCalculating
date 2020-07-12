import configparser

conf = configparser.ConfigParser()
conf.read('./ResourceFiles/set.ini', encoding='utf-8')

#不计算装备属性，武器类型为角色武器选项第一个
调试开关 = conf.getint('调试开关', 'value')

#输出搭配和伤害数据到csv
输出数据 = conf.getint('输出数据', 'value')

#控制夜语黑瞳武器是否显示在第一页
普雷武器显示 =  1 - conf.getint('夜语黑瞳', 'value')

#排行里每把武器只会出现一次
武器排名 = conf.getint('武器排名', 'value') 

#怪物属性
防御输入 = conf.getint('怪物属性', '防御')
火抗输入 = conf.getint('怪物属性', '火抗')
冰抗输入 = conf.getint('怪物属性', '冰抗')
光抗输入 = conf.getint('怪物属性', '光抗')
暗抗输入 = conf.getint('怪物属性', '暗抗')

#武器序号
武器序号 = conf.getint('武器序号', 'value')

#天劫
天劫减防 = conf.getint('天劫', '减防生效')
天劫减抗 = conf.getint('天劫', '减抗生效')

#战术之王的御敌套装
战术白字 = conf.getint('战术之王的御敌', '套装附加') / 100

#天御之灾
天御套装 = conf.getint('天御之灾', '套装属性')

#千蛛碎影减防
千蛛减防 = conf.getint('千蛛碎影', '减防生效')