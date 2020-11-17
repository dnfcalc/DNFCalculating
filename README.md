# DNFCalculating

执行程序下载:https://wws.lanzous.com/b01bfj76f 或 https://pan.lanzou.com/b01bfj76f

python(3.8)编写，使用 pyqt5(5.14.2) 图形 GUI 库<br>
主框架由纸飞机实现，西瓜提供数据公式并协助修改，SCUDRT 对算法进行优化修改，风之凌殇添加多进程优化<br>

## 基础安装及依赖

安装[Python](https://www.python.org/),计算器开发使用的是3.8版本<br>
安装项目依赖<br>
> pip install --user  -i https://pypi.mirrors.ustc.edu.cn/simple/ -r requirements.txt

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

## 程序目录结构说明

### build.bat

自动化生成版本的脚本,打包生成可执行程序并与资源文件压缩,同时根据提交的git commit,生成更新日志说明,版本相关文件生成在Publish目录<br>
执行脚本需要事先安装[node.js](https://nodejs.org/zh-cn/download/)及[pandoc](https://github.com/jgm/pandoc/releases/tag/2.11.0.4)

### main.py

程序入口页面,职业相关部分已经抽出,无需修改<br>


### Part 目录

职业相关文件目录,由职业名.py组成,职业名.py 负责各个职业的个性化数据<br>
若项目文件打开时图片显示不正常请将 pyqt5 版本更新至 5.14.2 或以上<br>

### ResourceFiles 目录

资源文件目录,由公用资源文件、职业资源文件及配置文件组成<br>

#### ResourceFiles/Config
* adventure_info.json : 职业加载配置
* release_version.json ：版本配置

### PublicReference 目录

公共实现部分,由 common.py base.py base_buff.py choise equipment utils 组成

#### PublicReference/common.py
奶系与输出系的公共方法

#### PublicReference/base.py base_buff.py

核心算法及主体界面绘制部分

#### PublicReference/equipment

装备及套装数据部分<br>
如需要添加修改装备.可在此处修改,注意装备的后缀数字,需要与 img/装备下的文件名一致(新增需要同步添加图标)

#### PublicReference/utils

公共工具方法,涉及到深度拷贝,最小堆排序算法,多线程,基础配置等

## 更新日志

[更新日志](https://github.com/wxh0402/DNFCalculating/blob/master/CHANGELOG.md)
