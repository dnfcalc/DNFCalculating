import multiprocessing
import queue
import threading
import time
import os
import math
from typing import Iterable

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl

from .log import logger
from .calc_core import CalcData
from .common import format_time
from .minheap import MinHeap, MinHeapWithQueue, batch_size
from .producer_consumer import producer, producer_data, thread_num, thread_task
from .storex import *
from copy import *
# from .MainWindow import *
import chardet
import sys
import platform
import ctypes
from ctypes import *

from PublicReference.utils.config import *


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


preferred = None
try:
    if platform.system() != "Windows":
        dllPath = resource_path(
            os.path.join("InternalFile", "DLL", "Preferred.dylib"))
        preferred = ctypes.CDLL(dllPath)
        # logger.info("Preferred included.")
    else:
        dllPath = resource_path(
            os.path.join("InternalFile", "DLL", "Preferred.dll"))
        preferred = ctypes.WinDLL(dllPath)
except Exception as e:
    logger.error(e)

skillDataPath = resource_path("SkillData")

# 100级史诗套数据
防具套装 = ("古代祭祀的神圣仪式", "遗忘魔法师的馈赠", "天堂舞姬", "死亡阴影", "皇家裁决者宣言", "龙血玄黄", "贫瘠沙漠的遗产",
        "炙炎之盛宴", "擎天战甲", "噩梦：地狱之路", "传奇铁匠-封神", "荆棘漫天", "永恒不息之路", "命运歧路",
        "大自然的呼吸")
首饰套装 = ("上古尘封术式", "破晓曦光", "幸运三角", "精灵使的权能")
特殊套装 = ("军神的隐秘遗产", "灵宝：世间真理", "时间战争的残骸", "能量主宰")
上链左套装 = ("深渊窥视者", "圣者的黄昏", "坎坷命运", "吞噬愤怒")
镯下右套装 = ("黑魔法探求者", "时空旅行者", "穿透命运的呐喊", "狂乱追随者")
环鞋指套装 = ("地狱求道者", "次元旅行者", "天命无常", "悲剧的残骸")

部位列表 = ("上衣", "头肩", "下装", "腰带", "鞋", "手镯", "项链", "戒指", "耳环", "辅助装备", "魔法石",
        "武器")

奥兹玛部位列表 = ("头肩", "腰带", "鞋", "项链", "魔法石")

奥兹玛套装 = ('阿斯特罗斯', '贝利亚斯', '雷德梅恩', '罗什巴赫', '泰玛特')

希洛克部位列表 = ("下装", "戒指", "辅助装备")

希洛克套装 = ('奈克斯', '暗杀者', '卢克西', '守门人', '洛多斯')

部位字典 = {
    "上衣": 0,
    "头肩": 1,
    "下装": 2,
    "腰带": 3,
    "鞋": 4,
    "手镯": 5,
    "项链": 6,
    "戒指": 7,
    "耳环": 8,
    "辅助装备": 9,
    "魔法石": 10,
    "武器": 11
}

颜色 = {
    '神话': '#E0502F',
    '史诗': '#FFB400',
    '传说': '#FF7800',
    '神器': '#FF00FF',
    '稀有': '#B36BFF'
}

总套装列表 = [防具套装, 首饰套装, 特殊套装, 上链左套装, 镯下右套装, 环鞋指套装]
所有套装列表 = 防具套装 + 首饰套装 + 特殊套装 + 上链左套装 + 镯下右套装 + 环鞋指套装


def getQCSS(FileName):
    try:
        content = store.get("./ResourceFiles/Skins/" + SkinVersion + "/" +
                            FileName)
        if content == None:
            with open(
                    "./ResourceFiles/Skins/" + SkinVersion + "/" + FileName +
                    ".qcss", "rb") as fp:
                content = fp.read()
                encoding = chardet.detect(content) or {}
                content = content.decode(encoding.get("encoding") or "utf-8")
                store.set(
                    "./ResourceFiles/Skins/" + SkinVersion + "/" + FileName,
                    content)
        return content
    except Exception as error:
        return ''


# 部分控件样式
按钮样式 = getQCSS('按钮样式')
# if 按钮样式 == '' : 按钮样式 = 'QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:10px} QPushButton:hover{background-color:rgba(65,105,225,0.8)}'

按钮样式_warn = getQCSS('按钮样式_warn')
# if 按钮样式_warn == '' : 按钮样式_warn ='''QPushButton{font-size:14px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:10px} QPushButton:hover{background-color:rgba(225,5,65,0.8)}'''

套装按钮样式 = getQCSS('套装按钮样式')
# if 套装按钮样式 == '' :套装按钮样式 = '''QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}'''
按钮样式2 = 'QPushButton{background-color:rgba(0,0,0,0);border:1px;border-radius:5px} QPushButton:hover{background-color:rgba(252,224,0,0.2)}'
按钮样式3 = '''QPushButton{font-size:13px;color:white;background-color:rgba(255,255,255,0.1);border:1px;border-radius:5px} QPushButton:hover{background-color:rgba(65,105,225,0.5)}
QPushButton::menu-indicator {image:none}'''

按钮样式 = getQCSS('按钮样式')
# if 按钮样式 == '' :按钮样式 = 'QPushButton{font-size:12px;color:white;background-color:grey;border:1px;border-radius:10px}'

复选框样式 = getQCSS('复选框样式')
# if 复选框样式 == '' :复选框样式 = "QCheckBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QCheckBox:hover{background-color:rgba(65,105,225,0.8)}"
# 复选框样式 = getQCSS('复选框样式')
# if 复选框样式 == '' :复选框样式 = "QCheckBox{font-size:12px;color:white;background-color:grey;border:1px;border-radius:3px} QCheckBox:hover{background-color:rgba(65,105,225,0.8)}"

标签样式 = getQCSS('标签样式')
# if 标签样式 == '' :标签样式 = "QLabel{font-size:12px;color:white}"

页签样式 = getQCSS('页签样式')
# if 页签样式 == '' :页签样式 = '''QToolButton{font-size:13px;color:white;background-color:rgba(70,130,200,0.8)} QToolButton:hover{background-color:rgba(40,100,235,0.8)}'''

页签样式_选中 = getQCSS('页签样式_选中')
# if 页签样式_选中 == '' :页签样式_选中 = '''QToolButton{font-size:13px;color:white;background-color:rgba(200,30,30,0.8)} QToolButton:hover{background-color:rgba(235,0,0,0.8)}'''

下拉框样式 = getQCSS('下拉框样式')
# if 下拉框样式 == '' :下拉框样式 = '''QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;}
# QComboBox:disabled{font-size:12px;color:white;background-color:grey;border:1px;border-radius:5px;}  QComboBox QAbstractItemView::item {height: 18px;}
# QComboBox:hover{background-color:rgba(65,105,225,0.8)}
# QComboBox QAbstractItemView::item {height: 18px;background-color:white}
# QComboBox QAbstractItemView::item:hover,QComboBox QAbstractItemView::item:focus {background-color:rgba(179,206,255,1);color:black}
# QComboBox QScrollBar{
#     background: white !important
# }
# QComboBox QScrollBar::handle{
#     background: rgb(220,220,220) !important
# }
# '''
# 下拉框样式 = getQCSS('下拉框样式')
# if 下拉框样式 == '' :下拉框样式 = "QComboBox{font-size:12px;color:white;background-color:grey;border:1px;border-radius:5px;}  QComboBox QAbstractItemView::item {height: 18px;}"
下拉框样式_down = getQCSS('下拉框样式_down')
# if 下拉框样式_down == '' :下拉框样式_down = '''QComboBox{font-size:12px;color:white;background-color:rgba(34,157,70,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(5,185,65,0.8)}
# QComboBox QAbstractItemView::item {height: 18px;background-color:white}
# QComboBox QAbstractItemView::item:hover,QComboBox QAbstractItemView::item:focus {background-color:rgba(179,206,255,1) !important;color:black}
# QComboBox QScrollBar{
#     background: white !important
# }
# QComboBox QScrollBar::handle{
#     background: rgb(220,220,220) !important
# }
# '''
下拉框样式_warn = getQCSS('下拉框样式_warn')
# if 下拉框样式_warn == '' :下拉框样式_warn = '''QComboBox{font-size:12px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(225,5,65,0.8)}
# QComboBox QAbstractItemView::item {height: 18px;background-color:white}
# QComboBox QAbstractItemView::item:hover,QComboBox QAbstractItemView::item:focus {background-color:rgba(179,206,255,1)!important; color:black}
# QComboBox QScrollBar{
#     background: white !important
# }
# QComboBox QScrollBar::handle{
#     background: rgb(220,220,220) !important
# }
# '''
下拉框样式_detail = getQCSS('下拉框样式_detail')

输入框样式 = getQCSS('输入框样式')
# if 输入框样式 == '' :输入框样式 ='''QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QLineEdit:hover{background-color:rgba(65,105,225,0.8)}'''

标签样式_2 = getQCSS('标签样式_2')
# if 标签样式_2 == '' :标签样式_2 = "QLabel{font-size:12px;color:yellow}"

文本框样式黄 = getQCSS('文本框样式黄')
# if 文本框样式黄 == '' :文本框样式黄 = "QLineEdit{font-size:12px;color:yellow;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}"
文本框样式白 = getQCSS('文本框样式白')
# if 文本框样式白 == '' :文本框样式白 = "QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px}"

滚动条样式 = getQCSS('滚动条样式')

标题背景 = getQCSS('标题背景')

标题字体 = getQCSS('标题字体')

# 滚动条样式 = '''/*QScrollBar Style*/
# /*纵向滚动条*/
# QScrollBar {
#     background: transparent; /*背景透明*/
#     width: 10px; /*宽度*/
#     margin: 0px 0px 0px 0px; /**/
#     padding-top: 5px; /*距离上面12px*/
#     padding-bottom: 5px; /*距离底部12px*/
# }
# /*纵向滚动条上面的滑块*/
# QScrollBar::handle {
#     background: rgba(245,245,245,50);
#     width: 10px;
#     border: none;
# }
# /*纵向滚动条下部分块*/
# QScrollBar::add-page:vertical {
#     width: 10px;
#     background: transparent;
# }
# /*横向滚动条后面部分块*/
# QScrollBar::add-page:horizontal {
#     height: 10px;
#     background: transparent;
# }
# /*纵向滚动条上面部分块*/
# QScrollBar::sub-page:vertical {
#     width: 10px;
#     background: transparent;
# }
# /*横向滚动条左部分块*/
# QScrollBar::sub-page:horizontal {
#     height: 10px;
#     background: transparent;
# }
# /*纵向滚动条顶部三角形位置*/
# QScrollBar::sub-line:vertical {
#     height: 12px;
#     width: 10px;
#     background: transparent;
#     subcontrol-position: top;
# }
# /*横向滚动条左侧三角形位置*/
# QScrollBar::sub-line:horizontal {
#     height: 10px;
#     width: 12px;
#     background: transparent;
#     subcontrol-position: left;
# }
# /*纵向滚动条下面三角形部分*/
# QScrollBar::add-line:vertical {
#     height: 12px;
#     width: 10px;
#     background: transparent;
#     subcontrol-position: bottom;
# }
# /*横向滚动条右边的三角形部分*/
# QScrollBar::add-line:horizontal {
#     height: 10px;
#     width: 12px;
#     background: transparent;
#     subcontrol-position: right;
# }
# '''

游戏滚动条样式模拟 = '''/*纵向滚动条*/
QScrollBar {
    background: transparent; /*背景透明*/
    width: 12px; /*宽度*/
    margin: 0px 0px 0px 0px; /**/
    padding-top: 16px; /*距离上面12px*/
    padding-bottom: 16px; /*距离底部12px*/
    padding-right:1px;
}
/*纵向滚动条上面的滑块*/
QScrollBar::handle {
    background: rgb(36,36,36);
    width: 12px;
    border: 1px inset rgb(76,61,39);
}
/*纵向滚动条下部分块*/
QScrollBar::add-page:vertical {
    width: 11px;
    background: transparent;
}
/*横向滚动条后面部分块*/
QScrollBar::add-page:horizontal {
    height: 11px;
    background: transparent;
}
/*纵向滚动条上面部分块*/
QScrollBar::sub-page:vertical {
    width: 11px;
    background: transparent;
}
/*横向滚动条左部分块*/
QScrollBar::sub-page:horizontal {
    height: 11px;
    background: transparent;
}
/*纵向滚动条顶部三角形位置*/
QScrollBar::sub-line:vertical {
    height: 12px;
    width: 11px;
    background: transparent;
    subcontrol-position: top;
}
/*横向滚动条左侧三角形位置*/
QScrollBar::sub-line:horizontal {
    height: 12px;
    width: 11px;
    background: transparent;
    subcontrol-position: left;
}
/*纵向滚动条下面三角形部分*/
QScrollBar::add-line:vertical {
    height: 12px;
    width: 11px;
    background: transparent;
    subcontrol-position: bottom;
}
/*横向滚动条右边的三角形部分*/
QScrollBar::add-line:horizontal {
    height: 12px;
    width: 11px;
    background: transparent;
    subcontrol-position: right;
}
/*纵向滚动条向上的三角形小图标*/
QScrollBar::up-arrow:vertical {
    image: url(ResourceFiles/img/UI/up.png);
    padding-top:3px;
    padding-right:2px;
}
QScrollBar::down-arrow:vertical {
    image: url(ResourceFiles/img/UI/down.png);
    padding-bottom:4px;
    padding-right:2px;
}
'''


class MyQComboBox(QComboBox):
    def __init__(self, win, useWheel=True):
        super().__init__(win)
        self.useWheel = useWheel
        self.setView(QListView())
        self.setStyleSheet(下拉框样式)

    def addItems(self, texts: Iterable[str]):
        for text in texts:
            self.addItem(text)
        pass

    def addItem(self, text, userData=None):
        if userData is None:
            userData = text
        text = trans(text)
        super().addItem(text, userData)
        pass

    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        if self.useWheel:
            return super().wheelEvent(e)
        else:
            pass


class MyQToolButton(QToolButton):
    DoubleClickSig = pyqtSignal(str)

    def mouseDoubleClickEvent(self, e):  # 双击
        sigContent = self.objectName()
        self.DoubleClickSig.emit(sigContent)


class MyQLabel(QtWidgets.QLabel):
    # 自定义信号, 注意信号必须为类属性
    button_clicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)
