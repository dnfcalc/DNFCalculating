from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Page(QWidget):
    def setName(self, name):
        self.__name = name

    def name(self):
        return self.__name

    def setWindow(self, window: QWindow):
        self.__window = window

    def window(self):
        return self.__window

    def closeWindow(self):
        if self.__window is not None:
            self.__window.close()
