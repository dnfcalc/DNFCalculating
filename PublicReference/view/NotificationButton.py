from PyQt5.QtGui import *
from PublicReference.common import *


class ConfirmButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setEnabled(False)
        # self.setText("test")
        self.time = QTimer(self)
        self.count = 10
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)
        self.time.start()

    def Refresh(self):
        # print(self.count)
        if self.count > 0:
            self.setText("(" + str(self.count) + "s) 确认")
            self.count -= 1
        else:
            self.time.stop()
            self.setEnabled(True)
            self.setText("确认")
