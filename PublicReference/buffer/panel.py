from PublicReference.utils.common import to_int
from PublicReference.view.Page import Page
from PyQt5.QtWidgets import QLabel, QGraphicsOpacityEffect

from PublicReference.equipment.buff.武器融合_buff import *
from PublicReference.equipment.buff.黑鸦_buff import 装备变换属性列表, 武器变换属性列表
from PublicReference.utils.constant import *
from PublicReference.equipment.equ_list import *


class 登记窗口(Page):
    def __init__(self):
        super().__init__()

    def 初始化(self):
        self.初始化 = True
        self.初始化UI()
        self.初始化 = False

    def 初始化UI(self):
        icon = store.get("/app/window/icon")
        bgImg = store.get("/app/window/background_image")
        self.setStyleSheet('''QToolTip {
           background-color: black;
           color: white;
           border: 0px
           }''')
        self.setFixedSize(960, 560)
        self.setWindowTitle("登记设置")
        self.setWindowIcon(icon)
        backgroundColorLabel = QLabel(self)
        backgroundColorLabel.resize(self.width(), self.height())
        backgroundColorLabel.setStyleSheet(
            "QLabel{background-color:rgba(50,50,50,1)}")
        graphicsEffect = QGraphicsOpacityEffect()
        graphicsEffect.setOpacity(0.1)
        backgroundImageLabel = QLabel(self)
        backgroundImageLabel.setPixmap(bgImg)
        backgroundImageLabel.move(0, int((self.height() - 1230) / 6))
        backgroundImageLabel.setGraphicsEffect(graphicsEffect)
        borderLabel = QLabel(self)
        borderLabel.resize(self.width() - 4, self.height() - 2)
        borderLabel.move(2, -1)
        borderLabel.setStyleSheet("QLabel{border:1px solid black}")

        yesButton = QPushButton("应用", self)
        yesButton.move(700, 500)
        yesButton.resize(80, 24)
        yesButton.setStyleSheet(按钮样式)
        yesButton.clicked.connect(lambda _: self.设置换装())

        cancelButton = QPushButton("取消", self)
        cancelButton.move(790, 500)
        cancelButton.resize(80, 24)
        cancelButton.setStyleSheet(按钮样式)
        cancelButton.clicked.connect(lambda _: self.closeWindow())

        resetButton = QPushButton("全部重置", self)
        resetButton.move(700, 460)
        resetButton.resize(170, 24)
        resetButton.setStyleSheet(按钮样式)
        resetButton.clicked.connect(lambda _: self.reset())

        self.初始化自选装备UI()
        self.初始化奥兹玛UI()
        self.初始化希洛克UI()
        self.初始化遴选UI()
        self.初始化残香UI()

    def showEvent(self, event):
        self.初始化数据()
        return super().showEvent(event)

    def 初始化数据(self):
        self.初始化装备()
        self.初始化希洛克()
        self.初始化奥兹玛()
        self.初始化遴选()

    def 初始化装备(self):
        equips = store.first("/buffer/data/register/equips",
                             "/buffer/memory/equips")
        amplifies = store.first("/buffer/data/register/amplifies",
                                "/buffer/data/amplifies")
        for 部位 in range(len(equips)):
            self.自选装备[部位].setCurrentText(equips[部位])
            self.自选增幅选项[部位].setCurrentIndex(amplifies[部位])

        self.站街面板输入.setText(
            str(store.get('/buffer/data/register/display_power', '')))

    def 初始化希洛克(self):
        sirocos = store.first("/buffer/data/register/siroco",
                              "/buffer/data/siroco")
        for i in range(len(sirocos)):
            self.希洛克选择(i, sirocos[i])
        weapon_fusion = store.first("/buffer/data/register/weapon_fusion",
                                    "/buffer/data/weapon_fusion", [0] * 4)
        self.武器融合属性A.setCurrentIndex(weapon_fusion[0])
        self.武器融合属性A2.setCurrentIndex(weapon_fusion[1])
        self.武器融合属性B.setCurrentIndex(weapon_fusion[2])
        self.武器融合属性B2.setCurrentIndex(weapon_fusion[3])

    def 初始化奥兹玛(self):
        ozmas = store.first("/buffer/data/register/ozma", "/buffer/data/ozma")
        for i in range(len(ozmas)):
            self.奥兹玛选择(i, ozmas[i])

    def 初始化遴选(self):
        black_purgatory = store.first("/buffer/data/register/black_purgatory",
                                      "/buffer/data/black_purgatory")
        for i in range(len(black_purgatory)):
            self.黑鸦词条[i][1].setCurrentIndex(black_purgatory[i][1])
            if len(black_purgatory[i]) > 3:
                self.黑鸦词条[i][3].setCurrentIndex(black_purgatory[i][3])

    def reset(self):
        store.delete("^/buffer/data/register/.*$")
        self.初始化数据()

    def 设置换装(self):
        if self.初始化:
            return
        自选 = []
        增幅 = []
        黑鸦 = []

        for i in range(len(self.自选装备)):
            equip = self.自选装备[i].currentText()
            自选.append(equip)
            增幅.append(self.自选增幅选项[i].currentIndex() if equip != '无' else -1)
        for i in range(len(self.黑鸦词条)):
            黑鸦.append([
                2,
                self.黑鸦词条[i][1].currentIndex(),
                self.黑鸦词条[i][3].currentIndex(),
            ])

        store.set("/buffer/data/register/equips", 自选)
        store.set("/buffer/data/register/siroco", self.希洛克选择状态)
        store.set("/buffer/data/register/ozma", self.奥兹玛选择状态)
        store.set("/buffer/data/register/black_purgatory", 黑鸦)
        store.set("/buffer/data/register/amplifies", 增幅)
        store.set("/buffer/data/register/amplifies", 增幅)
        store.set("/buffer/data/register/weapon_fusion", [
            self.武器融合属性A.currentIndex(),
            self.武器融合属性A2.currentIndex(),
            self.武器融合属性B.currentIndex(),
            self.武器融合属性B2.currentIndex(),
        ])

        store.set('/buffer/data/register/display_power',
                  to_int(self.站街面板输入.text()))

        store.emit("/buffer/event/register_changed")
        self.closeWindow()

    def 初始化自选装备UI(self):
        count = 0
        self.装备锁定 = []
        self.自选装备 = []
        self.自选增幅选项 = []

        propertyA = store.get("/buffer/temp/property_a")

        标签 = QLabel('锁定', self)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(70, 25)
        标签.move(20, 20)

        标签 = QLabel('单件选择', self)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(240, 25)
        标签.move(70, 20)

        for i in 部位列表:

            lock = QCheckBox(i, self)
            lock.setStyleSheet(复选框样式)
            lock.resize(70, 22)
            lock.move(20, 50 + 30 * count)
            self.装备锁定.append(lock)

            x = MyQComboBox(self)
            for j in range(32):
                x.addItem(str(j))
            x.resize(55, 20)
            x.move(90, 50 + 30 * count)
            self.自选增幅选项.append(x)

            combo = MyQComboBox(self)

            self.自选装备.append(combo)
            combo.resize(220, 22)
            combo.move(150, 50 + 30 * count)
            combo.addItem("无")
            for j in equ.get_equ_list():
                if j.部位 == i:
                    if i == '武器':
                        if j.类型 in propertyA.武器选项:
                            combo.addItem(j.名称)
                    else:
                        combo.addItem(j.名称)
            count += 1
        x = 400
        y = 20

        标签 = QLabel(trans('批量选择'), self)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(160, 25)
        标签.move(x, y)

        套装类型 = ['防具', '首饰', '特殊', '上链左', '镯下右', '环鞋指']
        count = 0
        self.自选套装 = []
        for i in 套装类型:
            self.自选套装.append(MyQComboBox(self))
            套装名称 = []
            for j in equ.get_suit_list():
                if j.名称 not in 套装名称 and j.类型 == i:
                    套装名称.append(j.名称)
            y += 30
            self.自选套装[count].addItems(套装名称)
            self.自选套装[count].resize(160, 22)
            self.自选套装[count].move(400, y)
            self.自选套装[count].activated.connect(
                lambda state, index=count: self.自选套装更改(index))
            count += 1

        y += 30

        神话部位选项 = MyQComboBox(self)
        神话部位选项.addItems(['神话部位:无', '神话部位:上衣', '神话部位:手镯', '神话部位:耳环'])
        神话部位选项.resize(160, 22)
        神话部位选项.move(400, y)
        神话部位选项.activated.connect(lambda index: self.神话部位更改(index))

        y += 30

        label = QLabel('站街面板', self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(标签样式)
        label.resize(60, 25)
        label.move(x, y)

        self.站街面板输入 = QLineEdit(self)
        self.站街面板输入.move(x + 60, y)
        self.站街面板输入.resize(70, 24)
        self.站街面板输入.setStyleSheet(输入框样式)

        y += 30

        add = QPushButton('打造↑', self)
        add.clicked.connect(lambda state: self.批量打造(1))
        add.move(x, y)
        add.resize(40, 24)
        add.setStyleSheet(按钮样式)

        minus = QPushButton('打造↓', self)
        minus.clicked.connect(lambda state: self.批量打造(-1))
        minus.move(x + 60, y)
        minus.resize(40, 24)
        minus.setStyleSheet(按钮样式)

        reset = QPushButton('重置', self)
        reset.clicked.connect(lambda state: self.初始化装备())
        reset.move(x + 120, y)
        reset.resize(40, 24)
        reset.setStyleSheet(按钮样式)

    def 批量打造(self, offset):
        for i in range(len(self.自选增幅选项)):
            y = max(min(self.自选增幅选项[i].currentIndex() + offset, 31), 0)
            self.自选增幅选项[i].setCurrentIndex(y)
        pass

    def 自选套装更改(self, index):
        name = self.自选套装[index].currentText()
        for i in range(11):
            if self.装备锁定[i].isChecked():
                continue
            x = 0
            for j in equ.get_equ_list():
                if j.部位 == 部位列表[i]:
                    x += 1
                    if j.所属套装2 == name:
                        self.自选装备[i].setCurrentIndex(x)
                        break
                    elif j.所属套装 == name and j.品质 != '神话':
                        self.自选装备[i].setCurrentIndex(x)
                        break

    def 神话部位更改(self, index):
        部位 = [-1, 0, 5, 8]
        序号 = 部位[index]
        if 序号 != -1:
            当前 = equ.get_equ_by_name(self.自选装备[序号].currentText())
            x = 0
            for i in equ.get_equ_list():
                if 当前.部位 == i.部位:
                    x += 1
                    if i.品质 == '神话' and i.所属套装 == 当前.所属套装:
                        self.自选装备[序号].setCurrentIndex(x)
        for k in [0, 5, 8]:
            if k != 序号:
                当前 = equ.get_equ_by_name(self.自选装备[k].currentText())
                if 当前.品质 == '神话':
                    x = 0
                    for i in equ.get_equ_list():
                        if 当前.部位 == i.部位:
                            x += 1
                            if i.品质 == '史诗' and i.所属套装 == 当前.所属套装:
                                self.自选装备[k].setCurrentIndex(x)
        pass

    def 初始化奥兹玛UI(self):
        横坐标 = 640
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
                lambda state, index=count: self.奥兹玛套装选择(index))
            for j in range(5):
                序号 = count * 5 + j
                图片 = QLabel(self)
                图片.setPixmap(
                    QPixmap('./ResourceFiles/img/奥兹玛/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标 + 60 + j * 30 + 20, 纵坐标 + count * 32)
                self.奥兹玛遮罩透明度.append(QGraphicsOpacityEffect())
                self.奥兹玛遮罩透明度[序号].setOpacity(0.5)
                self.奥兹玛单件按钮.append(QPushButton(self))
                self.奥兹玛单件按钮[序号].setStyleSheet(
                    "background-color: rgb(0, 0, 0)")
                self.奥兹玛单件按钮[序号].resize(28, 28)
                self.奥兹玛单件按钮[序号].move(横坐标 + 60 + j * 30 + 20, 纵坐标 + count * 32)
                self.奥兹玛单件按钮[序号].setGraphicsEffect(self.奥兹玛遮罩透明度[序号])
                self.奥兹玛单件按钮[序号].clicked.connect(
                    lambda state, index=序号: self.奥兹玛选择(index))
            count += 1

    def 初始化希洛克UI(self):
        横坐标 = 700
        纵坐标 = 250
        名称 = trans(['奈克斯', '暗杀者', '卢克西', '守门人', '洛多斯'])
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
                lambda state, index=count: self.希洛克套装选择(index))
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
                self.希洛克单件按钮[序号].move(横坐标 + 60 + j * 30 + 20, 纵坐标 + count * 32)
                self.希洛克单件按钮[序号].setGraphicsEffect(self.希洛克遮罩透明度[序号])
                self.希洛克单件按钮[序号].clicked.connect(
                    lambda state, index=序号: self.希洛克选择(index))
            count += 1

    def 初始化残香UI(self):
        x = 400
        y = 320

        标签 = QLabel('残香属性', self)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(240, 25)
        标签.move(x, y)

        y += 30

        self.武器融合属性A = MyQComboBox(self)
        for j in 武器属性A列表:
            self.武器融合属性A.addItem(j.固定属性描述)
        self.武器融合属性A.resize(60, 20)
        self.武器融合属性A.move(x, y)

        self.武器融合属性A1 = MyQComboBox(self)
        self.武器融合属性A1.resize(90 + 75, 20)
        self.武器融合属性A1.move(x + 110 - 50 + 5, y)

        self.武器融合属性A2 = MyQComboBox(self)
        self.武器融合属性A2.resize(50, 20)
        self.武器融合属性A2.move(x + 205 + 20 + 10, y)
        self.武器融合属性A.currentIndexChanged.connect(
            lambda: self.希洛克武器融合词条更新(self.武器融合属性A.currentIndex()))

        y += 30
        self.武器融合属性B = MyQComboBox(self)
        for j in 武器属性B列表:
            self.武器融合属性B.addItem(j.固定属性描述)
        self.武器融合属性B.resize(60, 20)
        self.武器融合属性B.move(x, y)

        self.武器融合属性B1 = MyQComboBox(self)
        self.武器融合属性B1.resize(90 + 75, 20)
        self.武器融合属性B1.move(x + 110 - 50 + 5, y)

        self.武器融合属性B2 = MyQComboBox(self)
        self.武器融合属性B2.resize(50, 20)
        self.武器融合属性B2.move(x + 205 + 20 + 10, y)
        self.武器融合属性B.currentIndexChanged.connect(
            lambda: self.希洛克武器融合词条更新(self.武器融合属性B.currentIndex(), 1))

        y += 30

        tips = QLabel("提示:当选择无时,将按穿戴装备的设置", self)
        tips.move(x, y)
        tips.resize(240, 24)
        tips.setStyleSheet("QLabel{font-size:12px;color:rgb(211,167,106)}")

    def 初始化遴选UI(self):
        横坐标 = 30
        纵坐标 = 420

        名称 = ['武器', '戒指', '辅助装备', '下装']
        self.黑鸦词条 = []

        title = QLabel("黑鸦遴选词条", self)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(标签样式)
        title.resize(400, 25)
        title.move(横坐标, 纵坐标)

        纵坐标 += 25

        for i in range(4):
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
            for item in 装备变换属性列表:
                tem[1].addItem(item.固定属性描述)
            tem[1].currentIndexChanged.connect(
                lambda state, index=i: self.黑鸦随机词条更新(index))

            self.黑鸦词条.append(tem)
            self.黑鸦词条更新(i)

    def 希洛克套装选择(self, index):
        count = 1
        for i in range(index * 3, index * 3 + 3):
            count &= self.希洛克选择状态[i]
        count ^= 1
        for i in range(index * 3, index * 3 + 3):
            self.希洛克选择(i, count)

    def 希洛克选择(self, index, value=-1):
        if value == -1:
            value = self.希洛克选择状态[index] ^ 1
        if value == 0:
            self.希洛克遮罩透明度[index].setOpacity(0.5)
        elif value == 1:
            for i in range(5):
                序号 = i * 3 + index % 3
                if self.希洛克选择状态[序号] == 1:
                    self.希洛克遮罩透明度[序号].setOpacity(0.5)
                    self.希洛克选择状态[序号] = 0
            self.希洛克遮罩透明度[index].setOpacity(0)

        self.希洛克选择状态[index] = value

    def 奥兹玛套装选择(self, index):
        count = 1
        for i in range(index * 5, index * 5 + 5):
            count &= self.奥兹玛选择状态[i]
        count ^= 1
        for i in range(index * 5, index * 5 + 5):
            self.奥兹玛选择(i, count)

    def 奥兹玛选择(self, index, value=-1):
        if value == -1:
            value = self.奥兹玛选择状态[index] ^ 1
        if value == 0:
            self.奥兹玛遮罩透明度[index].setOpacity(0.5)
        elif value == 1:
            for i in range(5):
                序号 = i * 5 + index % 5
                if self.奥兹玛选择状态[序号] == 1:
                    self.奥兹玛遮罩透明度[序号].setOpacity(0.5)
                    self.奥兹玛选择状态[序号] = 0
            self.奥兹玛遮罩透明度[index].setOpacity(0)
        self.奥兹玛选择状态[index] = value

    def 希洛克武器融合词条更新(self, index, x=0):
        if x == 0:
            self.武器融合属性A1.clear()
            self.武器融合属性A2.clear()
            属性A = 武器属性A列表[index]
            self.武器融合属性A2.addItems(属性A.range())
            self.武器融合属性A1.addItem(属性A.随机属性描述)
        elif x == 1:
            self.武器融合属性B1.clear()
            self.武器融合属性B2.clear()
            属性B = 武器属性B列表[index]
            self.武器融合属性B2.addItems(属性B.range())
            self.武器融合属性B1.addItem(属性B.随机属性描述)

    def 黑鸦词条更新(self, index):
        for i in range(1, 4):
            self.黑鸦词条[index][i].setEnabled(True)
            self.黑鸦词条[index][i].setStyleSheet(下拉框样式)

    def 黑鸦随机词条更新(self, i):
        index = self.黑鸦词条[i][1].currentIndex()
        self.黑鸦词条[i][2].clear()
        self.黑鸦词条[i][3].clear()
        if index == 0:
            return
        变换属性 = 武器变换属性列表[index] if i == 0 else 装备变换属性列表[index]

        temp = 变换属性.最大值
        while temp >= 变换属性.最小值:
            if 变换属性.间隔 / 10 >= 1:
                self.黑鸦词条[i][3].addItem(str(int(temp)))
            else:
                self.黑鸦词条[i][3].addItem(str(temp) + '%')
            temp -= 变换属性.间隔
        self.黑鸦词条[i][2].addItem(变换属性.随机属性描述)
