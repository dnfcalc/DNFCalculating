import multiprocessing

from PyQt5.QtCore import QUrl

from Part.sum import *
from PublicReference.calc_core import calc_core
from PublicReference.producer_consumer import producer_data, consumer, 工作线程数

if __name__ == '__main__':
    multiprocessing.freeze_support()

窗口列表 = []


def 打开窗口(index):
    名称 = 角色列表[index].类名
    if len(窗口列表) != 0:
        窗口列表[-1].关闭窗口()
    exec('窗口列表.append('+ 名称 +'())')
    窗口列表[-1].show()


class 选择窗口(QWidget):
    def __init__(self):
        super().__init__()
        self.初始化工作进程()
        self.界面()

    def 初始化工作进程(self):
        # 工作队列
        work_queue = multiprocessing.JoinableQueue()
        work_queue.cancel_join_thread()  # or else thread that puts data will not term
        producer_data.work_queue = work_queue
        # 工作进程
        workers = []
        for i in range(工作线程数):
            p = multiprocessing.Process(target=consumer, args=(work_queue, calc_core), daemon=True, name="worker#{}".format(i + 1))
            p.start()
            workers.append(p)

        logger.info("已启动{}个工作进程".format(工作线程数))

        self.worker = workers
        pass

    def 界面(self):
        self.setFixedSize(700, 500)
        self.setWindowTitle('DNF-100SS搭配计算器-2020.6.20')
        self.setWindowIcon(QIcon('ResourceFiles/img/icon.png'))
        按钮样式2 = 'QPushButton{font-size:13px;color:white;background-color:rgba(255,255,255,0.1);border:1px;border-radius:5px} QPushButton:hover{background-color:rgba(65,105,225,0.5)} '
        背景颜色 = QLabel(self)
        背景颜色.resize(self.width(),self.height())
        背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1)}")
        主背景透明度 = QGraphicsOpacityEffect()
        主背景透明度.setOpacity(0.25)
        主背景图片 = QPixmap("ResourceFiles/img/bg.jpg")
        主背景 = QLabel(self)
        主背景.setPixmap(主背景图片)
        主背景.setGraphicsEffect(主背景透明度)

        查看更新=QtWidgets.QPushButton('查看更新', self)
        查看更新.clicked.connect(lambda state: self.打开查看更新())
        查看源码=QtWidgets.QPushButton('查看源码', self)
        查看源码.clicked.connect(lambda state: self.打开查看源码())
        查看更新.move(int(self.width() / 2 * 0.3),self.height() - 40)
        查看源码.move(int(self.width() / 2 * 1.3),self.height() - 40)
        查看更新.setStyleSheet(按钮样式2)
        查看源码.setStyleSheet(按钮样式2)
        查看更新.resize(150,30)
        查看源码.resize(150,30)

        self.按钮列表 = []
        for i in range(len(角色列表)):
            self.按钮列表.append(QPushButton(角色列表[i].名称, self))
            self.按钮列表[i].move(-1000, -1000)
            self.按钮列表[i].resize(100, 28)
            self.按钮列表[i].setStyleSheet(按钮样式)
            self.按钮列表[i].clicked.connect(lambda state, index = i: 打开窗口(index))

        self.日期列表 = []
        self.作者列表 = []
        self.备注列表 = []
        for i in range(len(角色列表)):
            temp = ''
            if 角色列表[i].备注 != '无' and 角色列表[i].备注 != '':
                temp = '  <font color="#FF0000">' + 角色列表[i].备注 + '</font>'
            self.日期列表.append(QLabel('日期：' + 角色列表[i].时间, self))
            self.作者列表.append(QLabel('作者：' + 角色列表[i].作者, self))
            self.备注列表.append(QLabel(temp, self))
            self.日期列表[i].move(-1000, -1000)
            self.作者列表[i].move(-1000, -1000)
            self.备注列表[i].move(-1000, -1000)

            self.日期列表[i].resize(100, 28)
            self.作者列表[i].resize(200, 28)
            self.备注列表[i].resize(350, 28)

            self.日期列表[i].setStyleSheet(标签样式)
            self.作者列表[i].setStyleSheet(标签样式)
            self.备注列表[i].setStyleSheet(标签样式)

        self.选择框 = MyQComboBox(self)
        self.选择框.move(20, 10)
        self.选择框.resize(660, 24)
        self.选择框.currentIndexChanged.connect(lambda state: self.界面修改())
        self.选择框.addItem('所有：合计' +str(len(角色列表)) + '个')
        for i in range(len(角色类型)):
            temp = ''
            for j in 类型角色[i]:
                temp += j +' '
            self.选择框.addItem(角色类型[i] + '：' + temp)

    def 打开查看更新(self):
        QDesktopServices.openUrl(QUrl("https://pan.lanzou.com/b01bfj76f"))
        QDesktopServices.openUrl(QUrl("https://wws.lanzous.com/b01bfj76f"))

    def 打开查看源码(self):
        QDesktopServices.openUrl(QUrl("https://github.com/wxh0402/DNFCalculating"))

    def 界面修改(self):
        if self.选择框.currentIndex() == 0:
            count1 = 0
            count2 = 0
            for i in range(len(角色列表)):
                self.按钮列表[i].move(20 + 115 * count2, 45 + 40 * count1)
                count1 += 1
                if count1 % 10 == 0:
                    count1 = 0
                    count2 += 1
            for i in range(len(角色列表)):
                self.日期列表[i].move(-1000, -1000)
                self.作者列表[i].move(-1000, -1000)
                self.备注列表[i].move(-1000, -1000)
        else:
            序号 = self.选择框.currentIndex() - 1
            间隔 = min(int(400 / len(类型角色[序号])) , 45)
            count1 = 0
            for i in range(len(角色列表)):
                if 角色列表[i].角色 != 角色类型[序号]:
                    self.按钮列表[i].move(-1000, -1000)
                    self.日期列表[i].move(-1000, -1000)
                    self.作者列表[i].move(-1000, -1000)
                    self.备注列表[i].move(-1000, -1000)
                else:
                    self.按钮列表[i].move(20, 45 + 间隔 * count1)
                    self.日期列表[i].move(130, 45 + 间隔 * count1)
                    self.作者列表[i].move(230, 45 + 间隔 * count1)
                    self.备注列表[i].move(400, 45 + 间隔 * count1)
                    count1 += 1


if __name__ == '__main__':
    app = QApplication([])
    a = 选择窗口()
    a.show()
    app.exec_()
