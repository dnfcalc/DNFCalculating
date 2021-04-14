import sys
from .TitleBar import *


class MainWindow(QMainWindow):
    def __init__(self, client):
        super().__init__()
        self.InitializeWindow(client)

    def InitializeWindow(self, client):
        self.setWindowTitle(client.windowTitle())
        self.icon = client.windowIcon()
        self.setWindowIcon(self.icon)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.InitializeViews(client)

    def InitializeViews(self, client):
        self.client = client
        self.titleBar = TitleBar(self)
        self.center = QWidget(self)
        self.setCentralWidget(self.center)

        self.lay = QVBoxLayout()
        self.center.setLayout(self.lay)

        self.lay.addWidget(self.titleBar)
        self.lay.addWidget(self.client)
        self.lay.setStretch(1, 100)
        self.lay.setSpacing(0)
        self.lay.setContentsMargins(0, 0, 0, 0)

        self.titleBar.SetTitle(client.windowTitle())
        self.titleBar.SetWidth(client.width())

        self.titleBar.SetIcon(
            self.icon.pixmap(self.icon.actualSize(QSize(32, 32))))

    def closeEvent(self, event):
        self.client.close()
        super().close()

    # def LoadStyleFromQss(self, f):
    #     file = open(f)
    #     lines = file.readlines()
    #     file.close()
    #     res = ''
    #     for line in lines:
    #         res += line

    #     return res
