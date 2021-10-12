from PublicReference.view.Page import Page
from PyQt5.QtWidgets import QLabel, QGraphicsOpacityEffect
from PublicReference.utils.constant import *
from PublicReference.equipment.冒险家名望 import *


class 名望窗口(Page):
    def __init__(self):
        super().__init__()
        self.已初始化 = False

    def setDelegate(self, func):
        self.delegate = func

    def 初始化(self):
        self.初始化 = True
        self.名望部位列表 = list(附魔名望默认选项.keys())
        self.自选附魔名望选项 = []
        self.自选徽章名望选项 = []
        self.初始化UI()
        self.初始化 = False
        self.已初始化 = True

    def 初始化UI(self):
        icon = store.get("/app/window/icon")
        bgImg = store.get("/app/window/background_image")
        self.setStyleSheet('''QToolTip {
           background-color: black;
           color: white;
           border: 0px
           }''')
        self.setFixedSize(440, 560)
        self.setWindowTitle("名望设置")
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

        self.初始化装备UI()

    def 初始化装备UI(self):
        count = 0
        名望细节 = store.get("/fame/selection")
        徽章名望细节 = store.get("/fame/selection2")
        if 名望细节 == None:
            defaultValueTable = 附魔名望默认选项
            defaultValueTable2 = 徽章名望默认选项
        else:
            defaultValueTable = 名望细节
            defaultValueTable2 = 徽章名望细节
        for idx in range(len(self.名望部位列表)):
            部位 = self.名望部位列表[idx]
            label = QLabel(部位, self)
            label.setStyleSheet(标签样式)
            label.resize(70, 22)
            label.move(20 + int(idx / 18)* 220, 10 + 30 * (idx % 18))

            x = MyQComboBox(self)
            x.placeholderText = 部位
            values = 附魔名望选项[部位]
            defaultValue = defaultValueTable[部位]
            for value in values:
                x.addItem(str(value))
            x.currentIndexChanged.connect(lambda:self.更新名望细节())
            defaultIndex = values.index(defaultValue)
            x.setCurrentIndex(defaultIndex)
            x.resize(55, 20)
            x.move(90 + int(idx / 18) * 220, 10 + 30 * (idx % 18))
            self.自选附魔名望选项.append(x)


            徽章值 = 徽章名望选项.get(部位, None)
            if 徽章值 != None:
                徽章选项 = MyQComboBox(self)
                徽章选项.placeholderText = 部位
                徽章默认值 = defaultValueTable2[部位]
                for value in 徽章值:
                    徽章选项.addItem(str(value))
                徽章选项.currentIndexChanged.connect(lambda: self.更新名望细节())
                defaultIndex = 徽章值.index(徽章默认值)
                徽章选项.setCurrentIndex(defaultIndex)
                徽章选项.resize(55, 20)
                徽章选项.move(90 + 75 + int(idx / 18)* 220, 10 + 30 * (idx % 18))
                self.自选徽章名望选项.append(徽章选项)

        self.更新名望细节()


    def 更新名望细节(self):
        if not self.已初始化: return
        名望细节 = {}
        徽章细节 = {}
        for i in self.自选附魔名望选项:
            名望细节[i.placeholderText] = i.currentText()

        for i in self.自选徽章名望选项:
            徽章细节[i.placeholderText] = i.currentText()

        store.set("/fame/selection", 名望细节)
        store.set("/fame/selection2", 徽章细节)
        self.delegate(x=1)
