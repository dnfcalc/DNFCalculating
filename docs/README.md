## 简介

此项目为DNF装备搭配及伤害计算提供便利的工具  
执行程序下载:https://pan.lanzous.com/b01bfj76f 或 https://www.lanzou.com/b01bfj76f  
python(3.8)编写，使用 pyqt5图形 GUI 库  
主框架由纸飞机实现，西瓜协助修改，SCUDRT 对算法进行优化修改，风之凌殇添加多进程优化  

## 依赖安装

安装[Python](https://www.python.org/),计算器开发使用的是3.8版本  
安装项目依赖  
> pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ -r requirements.txt

<!-- ### 修改项目
* fork本项目
* 克隆(clone)你fork的项目到本地,如果clone速度太慢,可以在github.com后添加.cnpmjs.org,切换仓库,如
> 从  
> git clone https://github.com/wxh0402/DNFCalculating.git  
> 变成  
> git clone https://github.com.cnpmjs.org/wxh0402/DNFCalculating.git  
> 提示下载速度
* 新建分支并检出新分支,如
> git checkout -b ver0.1   -->

## macOS下运行方式

&#160; &#160; &#160; &#160; 直接在`Finder`中双击`run_mac.command`即可运行。

&#160; &#160; &#160; &#160; 或者在`终端(Terminal)`中，执行命令`python3.8 main.py`即可运行。


## 程序结构

|--　DNFCalculating  
　　　　|--　run_mac.command：macOS下运行脚本  
　　　　|--　CHANGELOG.md：程序更新记录  
　　　　|--　LICENSE：开源许可  
　　　　|--　main.py：程序主入口  
　　　　|--　README.md：程序说明  
　　　　|--　requirements.txt：项目依赖包  
　　　　|--　Characters：职业实现目录  
　　　　|--　PublicReference：公有引用方法  
　　　　|　　　|--　base.py：输出职业公有实现方法  
　　　　|　　　|--　base_buff.py：奶系职业公有实现方法  
　　　　|　　　|--　common.py：界面公有实现方法  
　　　　|　　　|--　__init__.py：初始化文件，启用多线程及日志记录  
　　　　|　　　|--　choise：选项设置  
　　　　|　　　|　　　|--　细节选项.py  
　　　　|　　　|　　　|--　选项设置.py  
　　　　|　　　|　　　|--　选项设置_buff.py  
　　　　|　　　|--　equipment：装备设置  
　　　　|　　　|　　　|--　basic_equ.py：装备公有类  
　　　　|　　　|　　　|--　equ_list.py：装备列表  
　　　　|　　　|　　　|--　基础函数.py：各类隐藏基础公式  
　　　　|　　　|　　　|--　宠物.py  
　　　　|　　　|　　　|--　宠物_buff.py  
　　　　|　　　|　　　|--　武器融合.py  
　　　　|　　　|　　　|--　武器融合_buff.py  
　　　　|　　　|　　　|--　称号.py  
　　　　|　　　|　　　|--　称号_buff.py  
　　　　|　　　|　　　|--　装备_套装.py  
　　　　|　　　|　　　|--　装备_武器.py  
　　　　|　　　|　　　|--　装备_特殊.py  
　　　　|　　　|　　　|--　装备_防具.py  
　　　　|　　　|　　　|--　装备_首饰.py  
　　　　|　　　|　　　|--　辟邪玉.py  
　　　　|　　　|　　　|--　辟邪玉_buff.py  
　　　　|　　　|--　utils：工具类  
　　　　|　　　　　　　|--　calc_core.py：装备寻优  
　　　　|　　　　　　　|--　common.py：格式化时间  
　　　　|　　　　　　　|--　config.py：配置读取  
　　　　|　　　　　　　|--　constant.py：常量  
　　　　|　　　　　　　|--　copy.py：深度拷贝  
　　　　|　　　　　　　|--　img.py：常量图片  
　　　　|　　　　　　　|--　MainWindow.py：自定义窗口  
　　　　|　　　　　　　|--　minheap.py：最小堆排序  
　　　　|　　　　　　　|--　producer_consumer.py：多进程  
　　　　|　　　　　　　|--　TitleBar.py：自定义标题栏  
　　　　|　　　　　　　|--　zipfile.py：压缩文件  
　　　　|--　ResourceFiles：资源文件夹  
　　　　|　　　|--　职业文件夹  
　　　　|　　　|　　　|--　bg.jpg：背景图  
　　　　|　　　|　　　|--　人物.png：详情界面人物图  
　　　　|　　　|　　　|--　reset：默认配置文件夹  
　　　　|　　　|　　　|　　　|--　char.json：职业特有选项存档  
　　　　|　　　|　　　|　　　|--　page_1.json：第一页选项存档  
　　　　|　　　|　　　|　　　|--　page_2.json：第二页选项存档  
　　　　|　　　|　　　|　　　|--　page_3.json：第三页选项存档  
　　　　|　　　|　　　|　　　|--　page_4.json：第四页选项存档  
　　　　|　　　|　　　|　　　|--　page_5.json：第五页选项存档  
　　　　|　　　|　　　|　　　|--　page_6.json：第六页选项存档   
　　　　|　　　|　　　|--　技能：技能图标文件夹  
　　　　|　　　|--　Config：配置文件夹  
　　　　|　　　|　　　|--　基础设置.ini  
　　　　|　　　|　　　|--　攻击目标.ini  
　　　　|　　　|　　　|--　adventure_info.json：加载职业配置  
　　　　|　　　|　　　|--　config.json：配置选项文件  
　　　　|　　　|　　　|--　release_version.json：计算器版本  
　　　　|　　　|--　img：公有图片  
　　　　|　　　|　　　|--　logo.ico  
　　　　|　　　|　　　|--　刀魂之卡赞.png  
　　　　|　　　|　　　|--　觉醒选择.png  
　　　　|　　　|　　　|--　输出背景.png  
　　　　|　　　|　　　|--　输出背景_BUFF.png  
　　　　|　　　|　　　|--　远古记忆.png  
　　　　|　　　|　　　|--　分类  
　　　　|　　　|　　　|--　头像  
　　　　|　　　|　　　|--　希洛克  
　　　　|　　　|　　　|--　装备  
　　　　|　　　|--　Skins：计算器皮肤包  
　　　　|--　Tools  
　　　　　　　　|--　图标去白点.py  
　　　　　　　　|--　神话融合图标拼接.py  
