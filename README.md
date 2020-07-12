# DNFCalculating

执行程序下载:https://wws.lanzous.com/b01bfj76f 或 https://pan.lanzou.com/b01bfj76f

python（3.8）编写，使用 pyqt5（5.14.2） 图形 GUI 库<br>
主框架由纸飞机实现，西瓜提供数据公式并协助修改，SCUDRT 对算法进行优化修改，风之凌殇添加多进程优化<br>

## 程序目录结构说明

### Part 目录

职业相关文件目录,由职业名.py 及 sum.py 组成,职业名.py 负责各个职业的个性化数据,sum.py 负责引用所有职业<br>
若项目文件打开时图片显示不正常请将 pyqt5 版本更新至 5.14.2 或以上<br>

### ResourceFiles 目录

资源文件目录,由公用资源文件及职业资源文件组成<br>

### main.py

程序入口页面,职业相关部分已经抽出,无需修改<br>

### PublicReference 目录

公共实现部分,由 base.py 装备.py 装备函数.py 组成

#### PublicReference/base.py

核心算法及主体界面绘制部分<br>
常规无需修改该部分,如需要优化程序的效率及部分算法，可尝试修改<br>
主体核心可优化空间比较大,但由于接触 PY 才几个礼拜,对 PY 多核心运算的不熟悉,暂不打算修改,欢迎尝试优化

#### PublicReference/装备.py

装备及套装数据部分<br>
如需要添加修改装备.可在此处修改,注意装备的后缀数字,需要与 img/装备下的文件名一致(新增需要同步添加图标)

#### PublicReference/装备函数.py

一些计算公式部分,除非公式出现偏差,否则无需修改<br>
