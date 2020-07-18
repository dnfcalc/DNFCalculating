
#有意添加职业或优化程序的加群 1019815121 沟通

import multiprocessing

from PyQt5.QtCore import QUrl
import PyQt5.QtCore as qtc
from Part.sum import *
from PublicReference.calc_core import calc_core
from PublicReference.producer_consumer import producer_data, consumer, 工作线程数

if __name__ == '__main__':
    multiprocessing.freeze_support()

窗口列表 = []

def 打开窗口(index):
    if len(窗口列表) != 0:
        窗口列表[-1].关闭窗口()
        窗口列表.clear()
    exec('窗口列表.append('+ index +'())')
    窗口列表[-1].show()

class 选择窗口(QMainWindow):
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
        self.setMinimumSize(805,630)
        self.setMaximumSize(805,1520)
        self.setWindowTitle('DNF-100SS搭配计算器-2020.7.18 (技能模板仅供参考，请根据自身情况修改)')
        self.icon = QIcon('ResourceFiles/img/logo.ico')
        self.setWindowIcon(self.icon)

        if not os.path.exists('./ResourceFiles'):
            QMessageBox.information(self,"解压错误",  "未找到ResourceFiles(资源文件)，请完整解压再打开main") 

        背景颜色 = QLabel(self)
        背景颜色.resize(805,1520)
        背景颜色.setStyleSheet("QLabel{background-color:rgba(0,0,0,1)}")

        self.头像图片 = []
        self.分类图片 = []
        for i in range(1, 76):
            self.头像图片.append(QPixmap("ResourceFiles/img/头像/"+ str(i) +".png"))
        for i in range(17):
            self.分类图片.append(QPixmap("ResourceFiles/img/分类/"+ str(i) +".png"))

        wrapper = QWidget()
        self.setCentralWidget(wrapper)
        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(750, 1520)

        按钮样式2 = 'QPushButton{background-color:rgba(0,0,0,0);border:1px;border-radius:5px} QPushButton:hover{background-color:rgba(252,224,0,0.2)}'

        count = 0
        for i in range(75):
            图标显示 = QLabel(self.topFiller)
            图标显示.setPixmap(self.头像图片[i])
            图标显示.resize(121, 90)
            图标显示.move(120 + (count % 5) * 125, 10 + int(count / 5) * 100)
            if (i + 1) in 完成职业:
                if 角色列表[角色序号[i + 1]].类名 != '空':
                    图标显示2 = QLabel(self.topFiller)
                    图标显示2.setPixmap(self.分类图片[16])
                    图标显示2.resize(121, 90)
                    图标显示2.move(120 + (count % 5) * 125, 10 + int(count / 5) * 100)
                    文字显示 = QLabel(self.topFiller)
                    文字显示.setStyleSheet('QLabel{font-size:13px;color:rgb(175,148,89)}')
                    文字显示.setText(角色列表[角色序号[i + 1]].显示名称)
                    文字显示.resize(121, 24)
                    文字显示.setAlignment(Qt.AlignCenter)
                    文字显示.move(120 + (count % 5) * 125, 76 + int(count / 5) * 100)
                    按钮 = QPushButton(self.topFiller)
                    按钮.setStyleSheet(按钮样式2)
                    按钮.resize(121, 90)
                    按钮.move(120 + (count % 5) * 125, 10 + int(count / 5) * 100)
                    按钮.clicked.connect(lambda state, index = 角色列表[角色序号[i + 1]]: self.职业版本判断(index))
                    temp = '<b>作者：<font color="#FF0000">'+ 角色列表[角色序号[i + 1]].作者 +'</font><br><br>'
                    temp += '时间：'+角色列表[角色序号[i + 1]].时间 +'<br><br>'
                    temp += '备注：'+角色列表[角色序号[i + 1]].备注 +'</b>'
                    按钮.setToolTip(temp)
            else:
                图标显示2 = QLabel(self.topFiller)
                图标显示2.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.8)}")
                图标显示2.resize(121, 90)
                图标显示2.move(120 + (count % 5) * 125, 10 + int(count / 5) * 100)
            count += 1

        count = 0
        for i in range(15):
            sign = 1
            for j in range(i * 5 + 1, i * 5 + 6):
                if j not in 完成职业:
                    sign = 0
                    break
            if sign == 1:
                图标显示2 = QLabel(self.topFiller)
                图标显示2.setPixmap(self.分类图片[15])
                图标显示2.resize(94, 90)
                图标显示2.setAlignment(Qt.AlignCenter)
                图标显示2.move(15, 10 + count* 100)
            图标显示 = QLabel(self.topFiller)
            图标显示.setPixmap(self.分类图片[i])
            图标显示.resize(94, 90)
            图标显示.setAlignment(Qt.AlignCenter)
            图标显示.move(15, 10 + count* 100)
            count += 1

        按钮样式3 = 'QPushButton{font-size:13px;color:white;background-color:rgba(255,255,255,0.1);border:1px;border-radius:5px} QPushButton:hover{background-color:rgba(65,105,225,0.5)}'

        名称 = ['查看更新', '查看源码', '使用说明', '问题反馈']
        链接 = []
        链接.append(['https://pan.lanzou.com/b01bfj76f', 'https://wws.lanzous.com/b01bfj76f'])
        链接.append(['https://github.com/wxh0402/DNFCalculating'])
        链接.append(['https://bbs.colg.cn/thread-7917714-1-1.html', 'https://www.bilibili.com/video/BV1F54y1Q7Bz'])
        链接.append(['https://jq.qq.com/?_wv=1027&k=bqgkCT40'])

        count = 0
        for i in 名称:
            链接按钮=QtWidgets.QPushButton(i, self.topFiller)
            链接按钮.clicked.connect(lambda state, index = count: self.打开链接(链接[index]))
            链接按钮.move(120 + 4 * 125, 10 + (count + 1) * 100)    
            链接按钮.setStyleSheet(按钮样式3)
            链接按钮.resize(121,90)
            count += 1

        链接按钮=QtWidgets.QPushButton('打开设置', self.topFiller)
        链接按钮.clicked.connect(lambda state : os.system('notepad.exe "./ResourceFiles/set.ini"'))
        链接按钮.move(120 + 4 * 125, 10 + (count + 1) * 100)    
        链接按钮.setStyleSheet(按钮样式3)
        链接按钮.resize(121,90)
        count += 1

        self.scroll = QScrollArea()
        self.scroll.setStyleSheet("QScrollArea {background-color:transparent}")
        self.scroll.viewport().setStyleSheet("background-color:transparent")
        self.scroll.setWidget(self.topFiller)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        wrapper.setLayout(self.vbox)

    def 职业版本判断(self, index):
        try:
            if index.类名2 == '无':
                打开窗口(index.类名)
                return
            box = QMessageBox(QMessageBox.Question, "提示", "请选择要打开的版本")
            box.setWindowIcon(self.icon)

            if '神思者' in index.类名:
                box.setStandardButtons(QMessageBox.Yes | QMessageBox.Retry | QMessageBox.No | QMessageBox.Abort | QMessageBox.Cancel) #Retry
                A = box.button(QMessageBox.Yes)
                B = box.button(QMessageBox.Retry)
                C = box.button(QMessageBox.No)
                D = box.button(QMessageBox.Abort)
                E = box.button(QMessageBox.Cancel)
                box.setDefaultButton(QMessageBox.Yes)
                A.setText('BUFF')
                B.setText('战斗')
                C.setText('BUFF(三觉)')
                D.setText('战斗(三觉)')
                E.setText('取消')
                box.exec_()
                if box.clickedButton() == A:
                    打开窗口(index.类名)
                elif box.clickedButton() == B:
                    打开窗口(index.类名2)
                elif box.clickedButton() == C:
                    打开窗口(index.类名3)
                elif box.clickedButton() == D:
                    打开窗口(index.类名4)
                else:
                    return
            else:
                box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
                A = box.button(QMessageBox.Yes)
                B = box.button(QMessageBox.No)
                C = box.button(QMessageBox.Cancel)
                A.setText('二觉')
                B.setText('三觉')
                C.setText('取消')
                box.exec_()
                if box.clickedButton() == A:
                    打开窗口(index.类名)
                elif box.clickedButton() == B:
                    打开窗口(index.类名2)
                else:
                    return
        except:
            return

    def 打开链接(self, url):
        for i in url:
            QDesktopServices.openUrl(QUrl(i))

if __name__ == '__main__':
    if 窗口显示模式 == 1:
        if hasattr(qtc.Qt, 'AA_EnableHighDpiScaling'):
            QtWidgets.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True)
        if hasattr(qtc.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication([])
    a = 选择窗口()
    a.show()
    app.exec_()
