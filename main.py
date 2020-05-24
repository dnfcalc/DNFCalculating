from 风暴骑兵 import *
from 毁灭者 import *
from 极诣枪炮师男 import *
from 机械之灵 import *
from 芙蕾雅 import *
from 大将军 import *
from 极诣弹药专家男 import *
from 屠戮之魂 import *
from 极诣契魔者 import *
from 极诣狂战士 import *
from 极诣流浪武士 import *
from 毒神绝 import *
app = QApplication([])

选择窗口 = QWidget()
选择窗口.setFixedSize(220, 550)
选择窗口.setWindowTitle('职业选择')

按钮样式 = 'QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QPushButton:hover{background-color:rgba(65,105,225,0.8)}'

选择窗口.setWindowIcon(QIcon('img/icon.png'))
背景颜色 = QLabel(选择窗口)
背景颜色.resize(选择窗口.width(),选择窗口.height())
背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1)}")
主背景透明度 = QGraphicsOpacityEffect()
主背景透明度.setOpacity(0.25)
主背景图片 = QPixmap("img/bg.jpg")
主背景 = QLabel(选择窗口)
主背景.setPixmap(主背景图片)
主背景.setGraphicsEffect(主背景透明度)

窗口列表 = []
count = 0
for i in ['风暴骑兵', '毁灭者', '极诣枪炮师男', '机械之灵', '芙蕾雅', '大将军', '极诣弹药专家男', '极诣契魔者', '极诣流浪武士', '极诣狂战士', '屠戮之魂', '毒神绝']:
    x = QPushButton(i,选择窗口)
    x.clicked.connect(lambda state, index = i: 打开窗口(index))
    x.move(30 , 30 + 40 * count)
    x.resize(160, 28)
    x.setStyleSheet(按钮样式)
    count += 1

def 打开窗口(index):
    if len(窗口列表) != 0:
        窗口列表[-1].关闭窗口()
    exec('窗口列表.append('+index+'())')
    窗口列表[-1].show()

选择窗口.show()
app.exec_()  