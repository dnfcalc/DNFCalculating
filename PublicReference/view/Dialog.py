from PublicReference.view.Page import Page

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..utils.constant import 标题背景, 标题字体

# title bar
TITLE_BAR_HEIGHT = 25
TITLE_BUTTON_SIZE = 25
TITLE_LABEL_SIZE = 25
TITLE_BUTTON_WIDTH = 25
TITLE_BUTTON_HEIGHT = 25
TITLE_ICON_MAG = 10

RES_PATH = './ResourceFiles/img/UI/'

TITLE_MIN_ICON = RES_PATH + "min.png"
TITLE_CLS_ICON = RES_PATH + "exit.png"

WINDOW_DEFAULT_WIDTH = 800
WINDOW_DEFAULT_HEIGHT = 480


class Dialog(QMainWindow):
    def __init__(self, client: Page):
        super().__init__()

        self.hideOnClose = False

        icon = client.windowIcon()

        titleBar = self.createTitleBar()

        titleBar.setTitle(client.windowTitle())
        titleBar.setWidth(client.width())

        titleBar.setIcon(icon.pixmap(icon.actualSize(QSize(32, 32))))

        lay = QVBoxLayout()
        lay.addWidget(titleBar)
        lay.addWidget(client)
        lay.setStretch(1, 100)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        center = QWidget(self)
        center.setLayout(lay)

        self.setCentralWidget(center)
        self.setWindowTitle(client.windowTitle())
        self.setWindowIcon(icon)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def createTitleBar(self):
        titleBar = QWidget()
        titleBar.setStyleSheet('''QWidget{background:transparent}''')
        label = QLabel(titleBar)
        label.setStyleSheet(标题背景)
        iconLabel = QLabel(titleBar)
        titleLabel = QLabel(titleBar)
        iconLabel.setText('纸飞机计算器')
        # self.titleLabel.setStyleSheet('''QLabel{color:#9f8d5c}''')

        minButton = QPushButton(titleBar)
        # restoreButton = QPushButton(self)
        closeButton = QPushButton(titleBar)

        minButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE)
        # self.restoreButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE);
        closeButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE)

        iconLabel.setFixedSize(TITLE_LABEL_SIZE, TITLE_LABEL_SIZE)
        iconLabel.setStyleSheet(标题字体)

        titleLabel.setFixedHeight(TITLE_LABEL_SIZE)
        titleLabel.setStyleSheet(标题字体)

        iconLabel.setAlignment(Qt.AlignCenter)
        titleLabel.setAlignment(Qt.AlignCenter)

        minButton.setIcon(QIcon(TITLE_MIN_ICON))
        closeButton.setIcon(QIcon(TITLE_CLS_ICON))

        minButton.clicked.connect(self.showMinimized)
        # self.restoreButton.clicked.connect(self.ShowRestoreWindow)
        closeButton.clicked.connect(self.close)

        lay = QHBoxLayout(titleBar)

        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        lay.addWidget(iconLabel)
        lay.addWidget(titleLabel)
        lay.addWidget(minButton)
        # self.lay.addWidget(self.restoreButton)
        lay.addWidget(closeButton)

        titleBar.setLayout(lay)

        def setTitle(text):
            titleLabel.setText(text)

        def setTitleStyle(style):
            titleLabel.setStyleSheet(style)

        def setIcon(icon):
            iconLabel.setPixmap(
                icon.scaled(iconLabel.size() -
                            QSize(TITLE_ICON_MAG, TITLE_ICON_MAG)))

        def setWidth(width):
            label.resize(width, TITLE_BAR_HEIGHT)

        titleBar.setTitle = setTitle
        titleBar.setTitleStyle = setTitleStyle
        titleBar.setIcon = setIcon
        titleBar.setWidth = setWidth

        return titleBar

    def setHideOnClose(self, hideOnClose):
        self.hideOnClose = hideOnClose

    def showEvent(self, event):
        parent = self.parent()
        if parent is not None:
            rect = parent.geometry()
            x = rect.x() + rect.width() / 2 - self.width() / 2
            y = rect.y() + rect.height() / 2 - self.height() / 2
            self.move(int(x), int(y))
        return super().showEvent(event)

    def closeEvent(self, event):
        if (self.hideOnClose):
            self.hide()
            return
        return super().closeEvent(event)
