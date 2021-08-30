from .Page import Page
from .Dialog import *
from PyQt5.QtCore import *


class DialogRegister:
    def __init__(self):
        self.dialogs = {}

    def showDialog(self, name: str, client: Page, parent=None):
        if self.dialogs.__contains__(name) == False:
            if callable(client):  # 如果传入函数 可以懒加载
                client = client()
            dialog = Dialog(client)
            client.setWindow(dialog)
            dialog.setHideOnClose(True)
            dialog.setWindowModality(Qt.WindowModality.WindowModal)
            if (parent is not None):
                dialog.setParent(parent)
            self.dialogs[name] = dialog
        self.dialogs[name].show()

    def dispose(self):
        for name in self.dialogs.keys():
            dialog: Dialog = self.dialogs[name]
            dialog.setHideOnClose(False)
            dialog.close()
        self.dialogs.clear()

    def close(self, name: str):
        if self.dialogs.__contains__(name):
            dialog = self.dialogs[name]
            dialog.close()


DefaultDialogRegister = DialogRegister()
