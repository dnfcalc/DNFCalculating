
执行程序下载:https://pan.lanzous.com/b01bfj76f 或 https://www.lanzou.com/b01bfj76f

python(3.8)编写，使用 pyqt5图形 GUI 库<br>
主框架由纸飞机实现，西瓜协助修改，SCUDRT 对算法进行优化修改，风之凌殇添加多进程优化<br>

## 依赖安装

安装[Python](https://www.python.org/),计算器开发使用的是3.8版本<br>
安装项目依赖<br>
> pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ -r requirements.txt

<!-- ### 修改项目
* fork本项目
* 克隆(clone)你fork的项目到本地,如果clone速度太慢,可以在github.com后添加.cnpmjs.org,切换仓库,如
> 从<br>
> git clone https://github.com/wxh0402/DNFCalculating.git<br>
> 变成<br>
> git clone https://github.com.cnpmjs.org/wxh0402/DNFCalculating.git<br>
> 提示下载速度
* 新建分支并检出新分支,如
> git checkout -b ver0.1<br> -->

## macOS下运行方式

&#160; &#160; &#160; &#160; 直接在`Finder`中双击`run_mac.command`即可运行。

&#160; &#160; &#160; &#160; 或者在`终端(Terminal)`中，执行命令`python3.8 main.py`即可运行。


## 程序结构

|--　DNFCalculating</br>
　　　　|--　run_mac.command：macOS下运行脚本</br>
　　　　|--　build.bat：打包脚本</br>
　　　　|--　CHANGELOG.md：程序更新记录</br>
　　　　|--　LICENSE：开源许可</br>
　　　　|--　main.py：程序主入口</br>
　　　　|--　README.md：程序说明</br>
　　　　|--　requirements.txt：项目依赖包</br>
　　　　|--　AutoRelese：项目自动发布文件包</br>
　　　　|　　　|--　ark.x64.dll：bz的zip压缩dll</br>
　　　　|　　　|--　bz.exe：bz压缩程序</br>
　　　　|　　　|--　Package.spec：pyinstaller打包配置</br>
　　　　|　　　|--　release_produce.js：更新日志自动生成程序</br>
　　　　|　　　|--　upload_cookie.json：蓝奏云上传cookie文件</br>
　　　　|　　　|--　upload_lanzouyun.py：自动上传蓝奏云文件</br>
　　　　|--　Part：职业实现目录</br>
　　　　|--　PublicReference：公有引用方法</br>
　　　　|　　　|--　base.py：输出职业公有实现方法</br>
　　　　|　　　|--　base_buff.py：奶系职业公有实现方法</br>
　　　　|　　　|--　common.py：界面公有实现方法</br>
　　　　|　　　|--　<u>　</u>init<u>　</u>.py：初始化文件，启用多线程及日志记录</br>
　　　　|　　　|--　choise：选项设置</br>
　　　　|　　　|　　　|--　细节选项.py</br>
　　　　|　　　|　　　|--　选项设置.py</br>
　　　　|　　　|　　　|--　选项设置_buff.py</br>
　　　　|　　　|--　equipment：装备设置</br>
　　　　|　　　|　　　|--　basic_equ.py：装备公有类</br>
　　　　|　　　|　　　|--　equ_list.py：装备列表</br>
　　　　|　　　|　　　|--　基础函数.py：各类隐藏基础公式</br>
　　　　|　　　|　　　|--　宠物.py</br>
　　　　|　　　|　　　|--　宠物_buff.py</br>
　　　　|　　　|　　　|--　武器融合.py</br>
　　　　|　　　|　　　|--　武器融合_buff.py</br>
　　　　|　　　|　　　|--　称号.py</br>
　　　　|　　　|　　　|--　称号_buff.py</br>
　　　　|　　　|　　　|--　装备_套装.py</br>
　　　　|　　　|　　　|--　装备_武器.py</br>
　　　　|　　　|　　　|--　装备_特殊.py</br>
　　　　|　　　|　　　|--　装备_防具.py</br>
　　　　|　　　|　　　|--　装备_首饰.py</br>
　　　　|　　　|　　　|--　辟邪玉.py</br>
　　　　|　　　|　　　|--　辟邪玉_buff.py</br>
　　　　|　　　|--　utils：工具类</br>
　　　　|　　　　　　　|--　calc_core.py：装备寻优</br>
　　　　|　　　　　　　|--　common.py：格式化时间</br>
　　　　|　　　　　　　|--　config.py：配置读取</br>
　　　　|　　　　　　　|--　constant.py：常量</br>
　　　　|　　　　　　　|--　copy.py：深度拷贝</br>
　　　　|　　　　　　　|--　minheap.py：最小堆排序</br>
　　　　|　　　　　　　|--　producer_consumer.py：多进程</br>
　　　　|　　　　　　　|--　zipfile.py：压缩文件</br>
　　　　|--　ResourceFiles：资源文件夹</br>
　　　　|　　　|--　职业文件夹</br>
　　　　|　　　|　　　|--　bg.jpg：背景图</br>
　　　　|　　　|　　　|--　人物.png：详情界面人物图</br>
　　　　|　　　|　　　|--　reset：默认配置文件夹</br>
　　　　|　　　|　　　|　　　|--　attr.ini</br>
　　　　|　　　|　　　|　　　|--　equ.ini</br>
　　　　|　　　|　　　|　　　|--　equ1.ini</br>
　　　　|　　　|　　　|　　　|--　equ2.ini</br>
　　　　|　　　|　　　|　　　|--　equ3.ini</br>
　　　　|　　　|　　　|　　　|--　equ4.ini</br>
　　　　|　　　|　　　|　　　|--　equ5.ini</br>
　　　　|　　　|　　　|　　　|--　skill1.ini</br>
　　　　|　　　|　　　|　　　|--　skill2.ini</br>
　　　　|　　　|　　　|　　　|--　skill3.ini</br>
　　　　|　　　|　　　|　　　|--　skill4.ini</br>
　　　　|　　　|　　　|--　技能：技能图标文件夹</br>
　　　　|　　　|--　Config：配置文件夹</br>
　　　　|　　　|　　　|--　adventure_info.json：加载职业配置</br>
　　　　|　　　|　　　|--　release_version.json：计算器版本</br>
　　　　|　　　|　　　|--　基础设置.ini</br>
　　　　|　　　|　　　|--　攻击目标.ini</br>
　　　　|　　　|--　img：公有图片</br>
　　　　|　　　|　　　|--　logo.ico</br>
　　　　|　　　|　　　|--　刀魂之卡赞.png</br>
　　　　|　　　|　　　|--　觉醒选择.png</br>
　　　　|　　　|　　　|--　输出背景.png</br>
　　　　|　　　|　　　|--　输出背景_BUFF.png</br>
　　　　|　　　|　　　|--　远古记忆.png</br>
　　　　|　　　|　　　|--　分类</br>
　　　　|　　　|　　　|--　头像</br>
　　　　|　　　|　　　|--　希洛克</br>
　　　　|　　　|　　　|--　装备</br>
　　　　|--　Tools</br>
　　　　　　　　|--　图标去白点.py</br>
　　　　　　　　|--　神话融合图标拼接.py</br>
