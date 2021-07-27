
from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsOpacityEffect

from PublicReference.equipment.武器融合_buff import *
from PublicReference.equipment.黑鸦_buff import 装备变换属性列表, 武器变换属性列表
from PublicReference.utils.constant import *
from PublicReference.equipment.equ_list import *

class 换装窗口(QWidget):
    def __init__(self):
        super().__init__()

    def 初始化(self, 人物面板):
        self.初始化 = True
        self.setDelegate(人物面板.更新换装)
        self.初始化UI(icon=人物面板.icon, bgImg=人物面板.主背景图片)
        self.初始化换装选择(人物面板)
        self.初始化 = False

    def 初始化UI(self, icon, bgImg):
        self.setStyleSheet('''QToolTip {
           background-color: black;
           color: white;
           border: 0px
           }''')
        self.setFixedSize(600,600)
        self.setWindowTitle("换装设置")
        self.setWindowIcon(icon)
        self.初始化背景(bgImg)

    def 初始化背景(self, bgImg):
        背景颜色 = QLabel(self)
        背景颜色.resize(self.width(), self.height())
        背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1)}")
        主背景透明度 = QGraphicsOpacityEffect()
        主背景透明度.setOpacity(0.1)
        主背景 = QLabel(self)
        主背景.setPixmap(bgImg)
        主背景.move(0, int((self.height() - 1230) / 6))
        主背景.setGraphicsEffect(主背景透明度)
        边框 = QLabel(self)
        边框.resize(self.width() - 4, self.height() - 2)
        边框.move(2, -1)
        边框.setStyleSheet("QLabel{border:1px solid black}")

    def 初始化换装选择(self, 人物面板):
        count = 0
        self.换装自选装备 = []
        self.换装装备增幅选项 = []
        for i in 部位列表:
            x = MyQComboBox(self)
            for j in range(32):
                x.addItem(str(j))
            x.resize(55, 20)
            self.换装装备增幅选项.append(x)
            x.move(30, 50 + 30 * count)
            self.换装自选装备.append(MyQComboBox(self))
            self.换装自选装备[count].resize(220, 22)
            self.换装自选装备[count].move(90, 50 + 30 * count)
            self.换装自选装备[count].currentIndexChanged.connect(
                lambda state, index=count: self.换装自选装备更改())
            for j in equ.get_equ_list():
                if j.部位 == i:
                    if i == '武器':
                        if j.类型 in 人物面板.角色属性A.武器选项:
                            self.换装自选装备[count].addItem(j.名称)
                    else:
                        self.换装自选装备[count].addItem(j.名称)
            count += 1

        self.初始化奥兹玛UI()
        self.初始化希洛克UI()
        self.初始化遴选UI()
        self.初始化武器UI()
        self.初始化换装数据(人物面板)
        self.初始化希洛克(人物面板.希洛克选择状态)
        self.初始化奥兹玛(人物面板.奥兹玛选择状态)

    def setDelegate(self, func):
        self.更新自选换装 = func

    def 初始化换装数据(self, 人物面板):
        self.初始化装备(人物面板.自选装备,人物面板.装备打造选项)

    def 初始化装备(self, 自选装备, 自选打造):
        for 部位 in range(len(自选装备)):
            self.换装自选装备[部位].setCurrentIndex(自选装备[部位].currentIndex())
            self.换装装备增幅选项[部位].setCurrentIndex(自选打造[部位 + 12].currentIndex())

    def 初始化希洛克(self, 希洛克选择状态):
        for i in range(len(希洛克选择状态)):
            if 希洛克选择状态[i] == 1:
                self.希洛克选择(i)


    def 初始化奥兹玛(self, 奥兹玛选择状态):
        for i in range(len(奥兹玛选择状态)):
            if 奥兹玛选择状态[i] == 1:
                self.奥兹玛选择(i)


    def 换装自选装备更改(self):
        """
            self.更新自选换装是一个protocol, 由 base_buff.py 实现，作用是更新换装相关数值
            def 更新换装(self, 自选换装, 自选打造, 换装奥兹玛, 换装希洛克, 换装遴选)
        """
        if self.初始化: return
        自选 = []
        增幅 = [1]*13
        黑鸦 = []

        for i in range(len(self.换装自选装备)):
            自选.append(self.换装自选装备[i].currentText())
            增幅.append(self.换装装备增幅选项[i].currentIndex())
        for i in range(len(self.黑鸦词条)):
            黑鸦.append([self.黑鸦词条[i][1].currentIndex(), self.黑鸦词条[i][3].currentIndex()])
        self.更新自选换装(自选,
                    增幅,
                    self.奥兹玛选择状态,
                    self.希洛克选择状态,
                    黑鸦)

    def 初始化奥兹玛UI(self):
        横坐标 = 320
        纵坐标 = 50
        名称 = ['阿斯特罗斯', '贝利亚斯', '雷德梅恩', '罗什巴赫', '泰玛特']
        self.奥兹玛套装按钮 = []
        self.奥兹玛单件按钮 = []
        self.奥兹玛遮罩透明度 = []
        self.奥兹玛选择状态 = [0] * 25
        count = 0
        for i in 名称:
            self.奥兹玛套装按钮.append(QPushButton(i, self))
            self.奥兹玛套装按钮[count].setStyleSheet(按钮样式)
            self.奥兹玛套装按钮[count].resize(75, 22)
            self.奥兹玛套装按钮[count].move(横坐标, 纵坐标 + 3 + count * 32)
            self.奥兹玛套装按钮[count].clicked.connect(
                lambda state, index=(count + 1) * 100: self.奥兹玛选择(index))
            for j in range(5):
                序号 = count * 5 + j
                图片 = QLabel(self)
                图片.setPixmap(
                    QPixmap('./ResourceFiles/img/奥兹玛/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标 + 60 + j * 30+20, 纵坐标 + count * 32)
                self.奥兹玛遮罩透明度.append(QGraphicsOpacityEffect())
                self.奥兹玛遮罩透明度[序号].setOpacity(0.5)
                self.奥兹玛单件按钮.append(QPushButton(self))
                self.奥兹玛单件按钮[序号].setStyleSheet(
                    "background-color: rgb(0, 0, 0)")
                self.奥兹玛单件按钮[序号].resize(28, 28)
                self.奥兹玛单件按钮[序号].move(横坐标 + 60 + j * 30+20, 纵坐标 + count * 32)
                self.奥兹玛单件按钮[序号].setGraphicsEffect(self.奥兹玛遮罩透明度[序号])
                self.奥兹玛单件按钮[序号].clicked.connect(
                    lambda state, index=序号: self.奥兹玛选择(index))
            count += 1

    def 初始化希洛克UI(self):
        横坐标 = 320
        纵坐标 = 220
        名称 = ['奈克斯', '暗杀者', '卢克西', '守门人', '洛多斯']
        self.希洛克套装按钮 = []
        self.希洛克单件按钮 = []
        self.希洛克遮罩透明度 = []
        self.希洛克选择状态 = [0] * 15
        count = 0
        for i in 名称:
            self.希洛克套装按钮.append(QPushButton(i, self))
            self.希洛克套装按钮[count].setStyleSheet(按钮样式)
            self.希洛克套装按钮[count].resize(75, 22)
            self.希洛克套装按钮[count].move(横坐标, 纵坐标 + 3 + count * 32)
            self.希洛克套装按钮[count].clicked.connect(
                lambda state, index=(count + 1) * 100: self.希洛克选择(index))
            for j in range(3):
                序号 = count * 3 + j
                图片 = QLabel(self)
                图片.setPixmap(
                    QPixmap('./ResourceFiles/img/希洛克/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标 + 60 + j * 30 + 20, 纵坐标 + count * 32)
                self.希洛克遮罩透明度.append(QGraphicsOpacityEffect())
                self.希洛克遮罩透明度[序号].setOpacity(0.5)
                self.希洛克单件按钮.append(QPushButton(self))
                self.希洛克单件按钮[序号].setStyleSheet(
                    "background-color: rgb(0, 0, 0)")
                self.希洛克单件按钮[序号].resize(28, 28)
                self.希洛克单件按钮[序号].move(横坐标 + 60 + j * 30+20, 纵坐标 + count * 32)
                self.希洛克单件按钮[序号].setGraphicsEffect(self.希洛克遮罩透明度[序号])
                self.希洛克单件按钮[序号].clicked.connect(
                    lambda state, index=序号: self.希洛克选择(index))
            count += 1

    def 初始化武器UI(self):
        横坐标 = 30
        纵坐标 = 380
        纵坐标 += 10
        self.武器融合属性A = MyQComboBox(self)
        for j in 武器属性A列表:
            self.武器融合属性A.addItem(j.固定属性描述)
        self.武器融合属性A.resize(60, 20)
        self.武器融合属性A.move(横坐标, 纵坐标 + 25)

        self.武器融合属性A1 = MyQComboBox(self)
        self.武器融合属性A1.resize(90 + 75, 20)
        self.武器融合属性A1.move(横坐标 + 110 - 50 + 5, 纵坐标 + 25)

        self.武器融合属性A2 = MyQComboBox(self)
        self.武器融合属性A2.resize(50, 20)
        self.武器融合属性A2.move(横坐标 + 205 + 20 + 10, 纵坐标 + 25)
        self.武器融合属性A.currentIndexChanged.connect(
            lambda: self.希洛克武器随机词条更新(self.武器融合属性A.currentIndex()))

        纵坐标 = 纵坐标 + 30
        self.武器融合属性B = MyQComboBox(self)
        for j in 武器属性B列表:
            self.武器融合属性B.addItem(j.固定属性描述)
        self.武器融合属性B.resize(60, 20)
        self.武器融合属性B.move(横坐标, 纵坐标 + 25)

        self.武器融合属性B1 = MyQComboBox(self)
        self.武器融合属性B1.resize(90 + 75, 20)
        self.武器融合属性B1.move(横坐标 + 110 - 50 + 5, 纵坐标 + 25)

        self.武器融合属性B2 = MyQComboBox(self)
        self.武器融合属性B2.resize(50, 20)
        self.武器融合属性B2.move(横坐标 + 205 + 20 + 10, 纵坐标 + 25)
        self.武器融合属性B.currentIndexChanged.connect(
            lambda: self.希洛克武器随机词条更新(self.武器融合属性B.currentIndex(), 1))

    def 初始化遴选UI(self):
        横坐标 = 30
        纵坐标 = 460

        名称 = ['武　　器', '戒　　指', '辅助装备', '下　　装']
        纵坐标 = 纵坐标 + 25
        self.黑鸦词条 = []
        for i in range(4):
            this_index = i
            x = QLabel(名称[i], self)
            x.setStyleSheet(标签样式 +
                            'QLabel{font-size:13px;};text-align: justify;')
            # x.setStyleSheet('text-align: justify')
            x.resize(55, 20)
            x.move(横坐标, 纵坐标 + i * 25)
            tem = []
            tem.append(MyQComboBox(self))
            """
                只允许自选，为了保持兼容不移除
            """
            if i == 0:
                tem[0].addItems(['自选数值'])
                tem[0].resize(0, 0)
                tem[0].move(横坐标 + 60, 纵坐标 + 25 * i)
                tem[0].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦词条更新(index))
            else:
                tem[0].addItems(['自选数值'])
                tem[0].resize(0, 0)
                tem[0].move(横坐标 + 60, 纵坐标 + 25 * i)
                tem[0].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦词条更新(index))
            tem.append(MyQComboBox(self))
            tem[1].resize(60, 20)
            tem[1].move(横坐标 + 156 - 91, 纵坐标 + 25 * i)

            tem.append(MyQComboBox(self))
            tem[2].resize(90 + 75, 20)
            tem[2].move(横坐标 + 266 - 50 + 5 - 91, 纵坐标 + 25 * i)

            tem.append(MyQComboBox(self))
            tem[3].resize(50, 20)
            tem[3].move(横坐标 + 361 + 20 + 10 - 91, 纵坐标 + 25 * i)
            if i > 0:
                for item in 装备变换属性列表:
                    tem[1].addItem(item.固定属性描述)
                tem[1].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦随机词条更新(index, 1))
            else:
                for item in 武器变换属性列表:
                    tem[1].addItem(item.固定属性描述)
                tem[1].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦随机词条更新(index))
            self.黑鸦词条.append(tem)
            self.黑鸦词条更新(i)

    def 希洛克选择(self, index):
        if index >= 100:
            序号 = int(index / 100 - 1)
            count = 0
            for i in range(序号 * 3, 序号 * 3 + 3):
                count += self.希洛克选择状态[i]
            if count != 3:
                for i in range(15):
                    if i in range(序号 * 3, 序号 * 3 + 3):
                        self.希洛克遮罩透明度[i].setOpacity(0)
                        self.希洛克选择状态[i] = 1
                    else:
                        self.希洛克遮罩透明度[i].setOpacity(0.5)
                        self.希洛克选择状态[i] = 0
            else:
                for i in range(序号 * 3, 序号 * 3 + 3):
                    self.希洛克遮罩透明度[i].setOpacity(0.5)
                    self.希洛克选择状态[i] = 0
        else:
            if self.希洛克选择状态[index] == 0:
                for i in range(5):
                    序号 = i * 3 + index % 3
                    if self.希洛克选择状态[序号] == 1:
                        self.希洛克遮罩透明度[序号].setOpacity(0.5)
                        self.希洛克选择状态[序号] = 0
                self.希洛克遮罩透明度[index].setOpacity(0)
                self.希洛克选择状态[index] = 1
            else:
                self.希洛克遮罩透明度[index].setOpacity(0.5)
                self.希洛克选择状态[index] = 0
        self.换装自选装备更改()

    def 奥兹玛选择(self, index):
        if index >= 100:
            序号 = int(index / 100 - 1)
            count = 0
            for i in range(序号 * 5, 序号 * 5 + 5):
                count += self.奥兹玛选择状态[i]
            if count != 5:
                for i in range(25):
                    if i in range(序号 * 5, 序号 * 5 + 5):
                        self.奥兹玛遮罩透明度[i].setOpacity(0)
                        self.奥兹玛选择状态[i] = 1
                    else:
                        self.奥兹玛遮罩透明度[i].setOpacity(0.5)
                        self.奥兹玛选择状态[i] = 0
            else:
                for i in range(序号 * 5, 序号 * 5 + 5):
                    self.奥兹玛遮罩透明度[i].setOpacity(0.5)
                    self.奥兹玛选择状态[i] = 0
        else:
            if self.奥兹玛选择状态[index] == 0:
                for i in range(5):
                    序号 = i * 5 + index % 5
                    if self.奥兹玛选择状态[序号] == 1:
                        self.奥兹玛遮罩透明度[序号].setOpacity(0.5)
                        self.奥兹玛选择状态[序号] = 0
                self.奥兹玛遮罩透明度[index].setOpacity(0)
                self.奥兹玛选择状态[index] = 1
            else:
                self.奥兹玛遮罩透明度[index].setOpacity(0.5)
                self.奥兹玛选择状态[index] = 0
        self.换装自选装备更改()

    def 希洛克武器随机词条更新(self, index, x=0):
        if x == 0:
            self.武器融合属性A1.clear()
            self.武器融合属性A2.clear()
            属性A = 武器属性A列表[index]
            temp = 属性A.最大值
            while temp >= 属性A.最小值:
                if 属性A.间隔 / 10 >= 1:
                    self.武器融合属性A2.addItem(str(int(temp)))
                else:
                    self.武器融合属性A2.addItem(str(temp) + '%')
                temp -= 属性A.间隔
            self.武器融合属性A1.addItem(属性A.随机属性描述)
        elif x == 1:
            self.武器融合属性B1.clear()
            self.武器融合属性B2.clear()
            属性B = 武器属性B列表[index]
            temp = 属性B.最大值
            while temp >= 属性B.最小值:
                if 属性B.间隔 / 10 >= 1:
                    self.武器融合属性B2.addItem(str(int(temp)))
                else:
                    self.武器融合属性B2.addItem(str(temp) + '%')
                temp -= 属性B.间隔
            self.武器融合属性B1.addItem(属性B.随机属性描述)
        self.换装自选装备更改()

    def 黑鸦词条更新(self, index):
        for i in range(1, 4):
            self.黑鸦词条[index][i].setEnabled(True)
            self.黑鸦词条[index][i].setStyleSheet(下拉框样式)

    def 黑鸦随机词条更新(self, i, x=0):
        index = self.黑鸦词条[i][1].currentIndex()
        self.黑鸦词条[i][2].clear()
        self.黑鸦词条[i][3].clear()
        if x == 0:
            武器属性 = 武器变换属性列表[index]
            temp = 武器属性.最大值
            while temp >= 武器属性.最小值:
                if 武器属性.间隔 / 10 >= 1:
                    self.黑鸦词条[i][3].addItem(str(int(temp)))
                else:
                    self.黑鸦词条[i][3].addItem(str(temp) + '%')
                temp -= 武器属性.间隔
            self.黑鸦词条[i][2].addItem(武器属性.随机属性描述)

        elif x == 1:
            装备属性 = 装备变换属性列表[index]
            temp = 装备属性.最大值
            while temp >= 装备属性.最小值:
                if 装备属性.间隔 / 10 >= 1:
                    self.黑鸦词条[i][3].addItem(str(int(temp)))
                else:
                    self.黑鸦词条[i][3].addItem(str(temp) + '%')
                temp -= 装备属性.间隔
            self.黑鸦词条[i][2].addItem(装备属性.随机属性描述)
        self.换装自选装备更改()
