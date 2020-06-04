from Part.sum import *
from PyQt5.QtCore import QUrl

app = QApplication([])

选择窗口 = QWidget()
选择窗口.setFixedSize(20 + 115 * len(角色列表), 10 * 45)
选择窗口.setWindowTitle('DNF-100SS搭配计算器-2020.6.4')

按钮样式2 = 'QPushButton{font-size:13px;color:white;background-color:rgba(255,255,255,0.1);border:1px;border-radius:5px} QPushButton:hover{background-color:rgba(65,105,225,0.5)}'

选择窗口.setWindowIcon(QIcon('ResourceFiles/img/icon.png'))
背景颜色 = QLabel(选择窗口)
背景颜色.resize(选择窗口.width(),选择窗口.height())
背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1)}")
主背景透明度 = QGraphicsOpacityEffect()
主背景透明度.setOpacity(0.25)
主背景图片 = QPixmap("ResourceFiles/img/bg.jpg")
主背景 = QLabel(选择窗口)
主背景.setPixmap(主背景图片)
主背景.setGraphicsEffect(主背景透明度)

窗口列表 = []
count2 = 0
for j in 角色列表:
    count1 = 0
    for i in j:
        x = QPushButton(i,选择窗口)
        x.clicked.connect(lambda state, index = i: 打开窗口(index))
        x.move(20 + 115 * count2 , 20 + 40 * count1)
        x.resize(100, 28)
        x.setStyleSheet(按钮样式)
        count1 += 1
    count2 += 1

def 打开窗口(index):
    if len(窗口列表) != 0:
        窗口列表[-1].关闭窗口()
    exec('窗口列表.append('+index+'())')
    窗口列表[-1].show()


def 打开查看更新():
    QDesktopServices.openUrl(QUrl("https://lanzous.com/b01bfj76f"))

查看更新=QtWidgets.QPushButton('查看更新', 选择窗口)
查看更新.clicked.connect(打开查看更新)

def 打开查看源码():
    QDesktopServices.openUrl(QUrl("https://github.com/wxh0402/DNFCalculating"))

查看源码=QtWidgets.QPushButton('查看源码', 选择窗口)
查看源码.clicked.connect(打开查看源码)

def 打开制作人员():
    QMessageBox.information(选择窗口,"制作人员",
    "主框架由纸飞机实现，西瓜提供数据公式并协助修改，SCUDRT对算法进行优化修改<br>\
    各职业实现：<br>\
    女大枪(纸飞机)、男大枪(幕城&纸飞机)、剑魔(爱敏&777&纸飞机)<br>\
    狂战士(爱敏&纸飞机)、剑豪(爱敏&纸飞机)、光枪(爱敏&纸飞机)<br>\
    毒王(雅男&纸飞机)、女机械(贝壳)、女弹药(西瓜)、男机械(韩械)<br>\
    男弹药(小一)、冰洁(平静)、元素(碳末&平静)、剑影(亚索)<br>\
    男漫游(Garson)、审判(Paxis)、特工(碳末)、剑宗(亚索)<br>\
    念皇(球)、魔皇(碳末)、念帝(疯)、风法(龙卷风)<br>")

制作人员=QtWidgets.QPushButton('制作人员', 选择窗口)
制作人员.clicked.connect(打开制作人员)

查看更新.move(int(选择窗口.width() / 3 * 0.2),选择窗口.height() - 40)
查看源码.move(int(选择窗口.width() / 3 * 1.2),选择窗口.height() - 40)
制作人员.move(int(选择窗口.width() / 3 * 2.2),选择窗口.height() - 40)
查看更新.setStyleSheet(按钮样式2)
查看源码.setStyleSheet(按钮样式2)
制作人员.setStyleSheet(按钮样式2)

查看更新.resize(150,30)
查看源码.resize(150,30)
制作人员.resize(150,30)

选择窗口.show()
app.exec_()  