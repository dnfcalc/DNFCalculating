import PyQt5.QtCore as qtc
import multiprocessing
from PyQt5.QtCore import QUrl, QThread
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import importlib
from PublicReference.common import *
from PublicReference.utils.usage_counter import increase_counter
from PublicReference.view.MainWindow import *
from PublicReference.utils.calc_core import calc_core
from PublicReference.utils.producer_consumer import producer_data, consumer, thread_num
import traceback
from PublicReference.utils import zipfile, uniqueCode, img
from PublicReference.utils import img
from PublicReference.utils.LZextends import *
from PublicReference.view import NotificationButton
import sys
import time
import subprocess
import base64
import requests
import random
import datetime

# 配置PyQt5环境变量
import PyQt5

dirname = os.path.dirname(PyQt5.__file__)
plugin_path = os.path.join(dirname, 'Qt5', 'plugins')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

主进程PID = ''
偏移量 = 25
目录 = ''

if __name__ == '__main__':
    multiprocessing.freeze_support()


class Worker(QThread):
    sinOut = pyqtSignal(int)

    def __init__(self, parent=None, fileURL=''):
        super(Worker, self).__init__(parent)
        self.working = True
        self.fileURL = fileURL

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()

    def run(self):
        path = os.getcwd() + "/__ZFJtemp"
        try:
            # os.rename(sys.argv[0],sys.argv[0]+'.del')
            lzy = LZextends().lzy
            lzy.down_file_by_url(self.fileURL,
                                 '',
                                 path,
                                 callback=self.show_progress,
                                 downloaded_handler=self.after_downloaded)
        except Exception as error:
            self.sinOut.emit(100)

    def show_progress(self, file_name, total_size, now_size):
        self.sinOut.emit(int(now_size / total_size * 100))

    def after_downloaded(self, file_path):
        try:
            if ("main.py" not in sys.argv[0]) and ("exe" in sys.argv[0]):
                os.rename(sys.argv[0], sys.argv[0] + '.del')
            # sys.argv[0] = sys.argv[0] + '.del'
        except Exception as error:
            logger.error("error={} \n detail {}".format(
                error, traceback.print_exc()))
            pass
        path = os.getcwd()
        zip_file = zipfile.ZipFile(file_path)
        zip_list = zip_file.namelist()  # 得到压缩包里所有文件
        for f in zip_list:
            # if not f.endswith('desktop.ini'):
            zip_file.extract(f, path)
            # extracted_path.rename(newName)
            # 循环解压文件到指定目录
        zip_file.close()
        # print(path+'\download')
        try:
            os.system('RMDIR /Q /S "{}"'.format(
                os.path.join(os.getcwd(), '__ZFJtemp')))
        except Exception as error:
            logger.error("error={} \n detail {}".format(
                error, traceback.print_exc()))
            pass
        self.working = False


class 选择窗口(QWidget):
    计算器版本 = ''
    云端版本 = ''
    # 自动检查版本 = False
    网盘链接 = ''
    网盘报错 = 0
    通知时间 = ''

    _signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        # self.thread_init()
        self.ui()
        self.char_window = None

    def thread_init(self):
        try:
            # 工作队列
            work_queue = multiprocessing.JoinableQueue()
            work_queue.cancel_join_thread(
            )  # or else thread that puts data will not term
            producer_data.work_queue = work_queue
            # 工作进程
            workers = []
            for i in range(thread_num):
                p = multiprocessing.Process(target=consumer,
                                            args=(work_queue, calc_core),
                                            daemon=True,
                                            name="worker#{}".format(i + 1))
                p.start()
                workers.append(p)

            # logger.info("已启动{}个工作进程".format(thread_num))

            self.worker = workers
            pass
        except Exception as error:
            return error

    def 网盘检查(self):
        return
        if 目录.endswith('py'):
            return
        try:
            lzy = LZextends().lzy
            fileURL = ''
            folder_info = lzy.get_folder_info_by_url(
                'https://wwx.lanzoux.com/b01bfj76f')
            if folder_info.code != LanZouCloud.SUCCESS:
                self.网盘链接 = ''
                self.网盘报错 = 1
                return
            # resp = urllib.request.urlopen('http://dnf.17173.com/jsq/instructions.html?j')
            for file in folder_info.files:
                if file.name.startswith("DNF计算器"):
                    self.云端版本 = file.name.replace(".zip", " 17173DNF.exe")
                    fileURL = file.url
                    if file.name.replace("DNF计算器",
                                         "").replace(".zip", "").replace(
                                             "-", ".") == self.计算器版本[5:]:
                        self.网盘链接 = ''
                        return
            self.网盘链接 = fileURL
        except Exception as error:
            self.网盘链接 = ''
            self.网盘报错 = 1
            return

    def ui(self):
        角色列表 = []
        self.setStyleSheet('''QToolTip {
                   background-color: black;
                   color: white;
                   border: 0px
                   }''')
        self.setMinimumSize(805, 625)
        self.setMaximumSize(805, 1520)
        if not os.path.exists('./ResourceFiles'):
            QMessageBox.information(self, "解压错误",
                                    "未找到资源文件，请将压缩包中ResourceFiles解压到同目录后打开计算器")
            return
        with open("ResourceFiles/Config/adventure_info.json",
                  encoding='utf-8') as fp:
            角色列表 = json.load(fp)
        fp.close()
        self.计算器版本 = currentVersion
        # self.自动检查版本 = versionInfo['AutoCheckUpdate']
        fp.close()
        self.setWindowTitle(trans('DNF搭配计算器&17173DNF专区'))
        self.icon = QIcon('ResourceFiles/img/logo.ico')
        self.setWindowIcon(self.icon)

        bgcolor = QLabel(self)
        bgcolor.resize(805, 1520)
        # bgcolor.setStyleSheet("QLabel{background-color:rgba(0,0,0,1)}")
        bgcolor.setStyleSheet("QLabel{background:url('" +
                              trans('ResourceFiles/img/分类') + "/bg.png')}")
        self.char_img = []
        self.family_img = []
        is_gif = os.path.exists('动态头像')
        for i in range(1, 76):
            if is_gif:
                self.char_img.append(QMovie("动态头像/" + str(i) + ".gif"))
            else:
                if i == 30 and not 多语言开关 == 0:
                    self.char_img.append(
                        QPixmap(
                            trans("ResourceFiles/img/头像/") + str(i) + ".png"))
                else:
                    self.char_img.append(
                        QPixmap("ResourceFiles/img/头像/" + str(i) + ".png"))
        for i in range(17):
            self.family_img.append(
                QPixmap("" + trans('ResourceFiles/img/分类') + "/" + str(i) +
                        ".png"))

        #wrapper = QWidget()
        # self.setCentralWidget(wrapper)
        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(750, 1520)

        count = 0
        reason = ''
        canUse = -1
        try:
            code = get_mac_address()
            repJson = requests.get(
                "https://i_melon.gitee.io/dnfcalculating/ban.json",
                timeout=2).json()
            if not code == '':
                if code in [
                        '2190155ee92d17e8cc3b0c9892fd5ac7',
                        '1ba5ea8fa16964666f0c0a85e89c3e96',
                        '2e3d28298db82f8b23dc9fa6aac14b6d',
                        'f8b3cf5c269c97a8d6d2d97ecf769a06'
                ]:
                    canUse = random.randint(0, 75)
                    reason = '呵呵'
                reason = repJson[code]['reason']
                if reason != '': canUse = random.randint(0, 75)
        # except:
        #     reason = '获取异常列表错误'
        #     canUse = random.randint(0, 75)
        #     pass
        # try:
        except:
            pass
        for i in range(75):
            img_box = QLabel(self.topFiller)
            if is_gif:
                img_box.setMovie(self.char_img[i])
                self.char_img[i].start()
            else:
                img_box.setPixmap(self.char_img[i])
            img_box.resize(121, 90)
            img_box.move(100 + 偏移量 + (count % 5) * 125,
                         10 + int(count / 5) * 100)
            if i < 75:
                if 角色列表[i]["类名"] != '空':
                    img_box_2 = QLabel(self.topFiller)
                    img_box_2.setPixmap(self.family_img[16])
                    img_box_2.resize(121, 90)
                    img_box_2.move(100 + 偏移量 + (count % 5) * 125,
                                   10 + int(count / 5) * 100)
                    txt_box = QLabel(self.topFiller)
                    txt_box.setStyleSheet(
                        'QLabel{font-size:13px;color:rgb(175,148,89)}')
                    txt_box.setText(trans(角色列表[i]["显示名称"]))
                    txt_box.resize(121, 24)
                    txt_box.setAlignment(Qt.AlignCenter)
                    txt_box.move(100 + 偏移量 + (count % 5) * 125,
                                 76 + int(count / 5) * 100)
                    butten = QPushButton(self.topFiller)
                    butten.setStyleSheet(按钮样式2)
                    butten.resize(121, 90)
                    butten.move(100 + 偏移量 + (count % 5) * 125,
                                10 + int(count / 5) * 100)
                    if canUse > 0 and i != canUse:
                        butten.clicked.connect(
                            lambda state, reason=reason: self.弹窗警告(reason))
                    else:
                        butten.clicked.connect(
                            lambda state, index=角色列表[i]: self.职业版本判断(index))
                    # temp = '<b>作者：<font color="#C66211">' + 角色列表[i][
                    #     "作者"] + '</font>'
                    # butten.setToolTip(temp)
            else:
                img_box_2 = QLabel(self.topFiller)
                img_box_2.setStyleSheet(
                    "QLabel{background-color:rgba(0,0,0,0.8)}")
                img_box_2.resize(121, 90)
                img_box_2.move(100 + 偏移量 + (count % 5) * 125,
                               10 + int(count / 5) * 100)
            count += 1

        count = 0
        for i in range(15):
            sign = 1
            for j in range(i * 5 + 1, i * 5 + 6):
                if j > 75:
                    sign = 0
                    break
            if sign == 1:
                img_box_2 = QLabel(self.topFiller)
                img_box_2.setPixmap(self.family_img[15])
                img_box_2.resize(94, 90)
                img_box_2.setAlignment(Qt.AlignCenter)
                img_box_2.move(偏移量, 10 + count * 100)
            img_box = QLabel(self.topFiller)
            img_box.setPixmap(self.family_img[i])
            img_box.resize(94, 90)
            img_box.setAlignment(Qt.AlignCenter)
            img_box.move(偏移量, 10 + count * 100)
            count += 1

        # 为了女鬼调整位置
        count = 1

        butten = QtWidgets.QPushButton(
            '  ' + trans('首页') + '\n  ' + trans('设置|打赏|反馈'), self.topFiller)

        # butten = QtWidgets.QPushButton(" " + trans(''), self.topFiller)
        menu = QMenu()
        action_0 = QAction(trans('设置'), parent=menu)
        action_0.triggered.connect(lambda state: self.openSet())
        action_1 = QAction(trans('BUG反馈-Gitee'), parent=menu)
        action_1.triggered.connect(lambda state: self.打开链接([
            'https://gitee.com/i_melon/DNFCalculating/issues?state=all'
        ], "Gitee"))
        action_2 = QAction('联系我们-QQ-1群', parent=menu)
        action_2.triggered.connect(lambda state: self.打开链接(
            ['https://jq.qq.com/?_wv=1027&k=VSNtZ1xv'], "QQ群"))
        action_3 = QAction('联系我们-QQ-2群', parent=menu)
        action_3.triggered.connect(lambda state: self.打开链接(
            ['https://jq.qq.com/?_wv=1027&k=QMgadVkA'], "QQ群"))
        action_4 = QAction('联系我们-QQ-3群', parent=menu)
        action_4.triggered.connect(lambda state: self.打开链接(
            ['https://jq.qq.com/?_wv=1027&k=ekQXpyq0'], "QQ群"))
        action_5 = QAction(trans('打赏'), parent=menu)
        action_5.triggered.connect(lambda state, index=count: self.打赏())
        action_6 = QAction('联系我们-解除限制', parent=menu)
        action_6.triggered.connect(lambda state: self.打开链接([
            'https://gitee.com/i_melon/DNFCalculating/issues/I4IOO7'
        ], "解除限制"))
        action_7 = QAction(QIcon('ResourceFiles/img/logo.ico'),
                           trans('手册 源码 日志'),
                           parent=menu)
        action_7.triggered.connect(
            lambda state: self.打开链接(['http://dnf.17173.com/jsq/?khd'], "首页"))
        menu.addAction(action_7)
        menu.addSeparator()
        menu.addAction(action_0)
        menu.addSeparator()
        menu.addAction(action_5)
        menu.addSeparator()
        menu.addAction(action_1)
        menu.addSeparator()
        menu.addAction(action_2)
        menu.addAction(action_3)
        menu.addAction(action_4)
        menu.addAction(action_6)
        butten.setMenu(menu)
        # butten.clicked.connect(lambda state, index = count: self.问题反馈())
        # menu=QMenu()
        # action_0 = QAction('手册',parent=menu)
        # action_1 = QAction('日志',parent=menu)
        # action_2 = QAction('源码',parent=menu)
        # menu.addAction(action_0)
        # menu.addAction(action_1)
        # menu.addAction(action_2)
        # butten.setMenu(menu)
        butten.move(100 + 偏移量 + 4 * 125, 10 + (count + 1) * 100)
        butten.setStyleSheet(按钮样式3)
        butten.resize(121, 90)

        count += 1

        butten = QtWidgets.QPushButton(trans('检查更新'), self.topFiller)
        butten.clicked.connect(lambda state, index=count: self.检查更新())
        butten.move(100 + 偏移量 + 4 * 125, 10 + (count + 1) * 100)
        butten.setStyleSheet(按钮样式3)
        butten.resize(121, 90)
        self.配置错误 = QMessageBox(
            QMessageBox.Question, "提示",
            "配置文件有误，程序将以默认设置开启！\n请检查以下文件\nResourceFiles\\Config\\基础设置.ini\nResourceFiles\\Config\\攻击目标.ini\nResourceFiles\\Skins\\Skin.ini\n是否以UTF-8编码存储且文件内格式正确"
        )
        self.版本提示 = QMessageBox(
            QMessageBox.Question, "用户须知",
            trans("此工具为开源免费软件\n如遇二次售卖获利,请协助反馈举报~") +
            '\n同时,计算器预设了埋点,收集使用情况供功能分析优化并限制滥用工具的情况,如:职业打开情况、页签打开情况、按钮使用情况等')
        self.版本提示.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.版本提示A = self.版本提示.button(QMessageBox.Yes)
        self.版本提示B = self.版本提示.button(QMessageBox.No)
        self.版本提示A.setText('已知悉')
        self.版本提示B.setText('退出')

        try:
            if 自动检查更新 == 0:
                repJson = requests.get(
                    "https://i_melon.gitee.io/dnfcalculating/notice.json",
                    timeout=2).json()
                self.通知时间 = repJson[0]['time']
                self.消息通知 = QMessageBox(QMessageBox.Question, "通知",
                                        repJson[0]['info'])
                self.消息通知.setWindowIcon(self.icon)
                confirm = NotificationButton.ConfirmButton(self.消息通知)
                self.消息通知.setWindowFlags(Qt.Window | Qt.WindowTitleHint
                                         | Qt.CustomizeWindowHint)
                self.消息通知.addButton(confirm, QMessageBox.YesRole)
        except Exception as error:
            pass
        self.版本提示.setWindowIcon(self.icon)
        self.配置错误.setWindowIcon(self.icon)

        if 自动检查更新 == 0:
            try:
                self.网盘检查()
                if self.网盘报错 == 1:
                    self.报错提示 = QMessageBox(QMessageBox.Question, "提示",
                                            trans("无法自动检查更新，请在每周三/四自行前往检查版本"))
                    self.报错提示.setWindowIcon(self.icon)
                    # box.exec_()
                if self.网盘链接 != '':
                    m_red_SheetStyle = "padding-left:3px;min-width: 25px; min-height: 16px;border-radius: 5px; background:red;color:white"
                    label = QLabel("New", self.topFiller)
                    label.move(115 + 4 * 125 + 90, 30 + (count + 1) * 100)
                    label.setStyleSheet(m_red_SheetStyle)
            except Exception as error:
                pass
        count += 1
        count += 1

        # butten = QtWidgets.QPushButton('打   赏', self.topFiller)
        # butten.clicked.connect(lambda state, index=count: self.打赏())
        # butten.move(100 + 偏移量 + 4 * 125, 10 + (count + 1) * 100)
        # butten.setStyleSheet(按钮样式3)
        # butten.resize(121, 90)
        # count += 1

        butten = QtWidgets.QPushButton('', self.topFiller)
        butten.clicked.connect(lambda state, index=count: self.打开链接(
            ['http://dnf.17173.com/?jsq'], "首页"))
        butten.move(100 + 偏移量 + 4 * 125, 10 + (count + 1) * 100)
        butten.setStyleSheet(按钮样式3)
        butten.resize(121, 90)
        count += 1

        self.scroll = QScrollArea()
        self.scroll.setFrameShape(QFrame.NoFrame)
        self.scroll.setStyleSheet("QScrollArea {background-color:transparent}")
        self.scroll.setStyleSheet(游戏滚动条样式模拟)
        self.scroll.viewport().setStyleSheet("background-color:transparent")
        self.scroll.setWidget(self.topFiller)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.setLayout(self.vbox)

    def openSet(self):
        increase_counter(ga_category="其余功能使用", name="设置")
        self.processpid = []
        self.setWindow = SetWindows(self.worker, self)
        # self.setWindow._signal.connect(self.closeSet)
        self.win = MainWindow(self.setWindow)
        self.win.show()

    def closeSet(self, parameter):
        if parameter == 1:
            win.close()

    def 打开窗口(self, name):
        if self.char_window != None:
            self.char_window.close()
        if "." in name:
            className = name.split(".")[1]
        else:
            className = name
        module_name = "Characters." + name
        职业 = importlib.import_module(module_name)
        char = eval("职业." + className + '()')
        increase_counter(ga_category="职业使用", name=className)
        if get_mac_address() != '':
            increase_counter(ga_category="用户职业使用", name=get_mac_address())
        try:
            self.char_window = MainWindow(char)
            self.char_window.show()
        except Exception as e:
            print(e)

    def 打赏(self):
        self.w = QWidget()
        self.w.resize(300, 300)
        self.w.setWindowTitle('打赏-微信')
        self.w.setWindowIcon(self.icon)
        主背景 = QLabel(self.w)
        赞赏码 = QPixmap()
        赞赏码.loadFromData(base64.b64decode(img.二维码))
        主背景.setPixmap(赞赏码)
        increase_counter(ga_category="其余功能使用", name="打赏")
        self.w.show()

    def 弹窗警告(self, reason):
        box = QMessageBox(
            QMessageBox.Question, "提示",
            "{}由于{},您已被限制使用计算器，每次开启仅能随机使用一个职业<br>如需解除，请于设置=>解除限制内申请".format(
                get_mac_address(), reason))
        box.setWindowIcon(self.icon)
        box.setStandardButtons(QMessageBox.Yes)
        box.exec_()

    def 职业版本判断(self, index):
        try:
            if index["类名2"] == '无':
                self.打开窗口(index["类名"])
                return
            else:
                box = QMessageBox(QMessageBox.Question, "提示", "请选择要打开的版本")
            box.setWindowIcon(self.icon)
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No
                                   | QMessageBox.Cancel)
            if index["序号"] in ["40", "41"]:
                if index["类名3"] != '无':
                    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No
                                           | QMessageBox.YesToAll
                                           | QMessageBox.Cancel)
                A = box.button(QMessageBox.Yes)
                B = box.button(QMessageBox.No)
                A.setText('BUFF')
                B.setText('战斗')
                if index["类名3"] != '无':
                    C = box.button(QMessageBox.YesToAll)
                    C.setText('前瞻版本-战斗')
            else:
                A = box.button(QMessageBox.Yes)
                B = box.button(QMessageBox.No)
                A.setText('国服版本')
                B.setText('前瞻版本')

            E = box.button(QMessageBox.Cancel)
            E.setText('取消')
            box.exec_()
            try:
                if box.clickedButton() == A:
                    self.打开窗口(index["类名"])
                elif box.clickedButton() == B:
                    self.打开窗口(index["类名2"])
                elif box.clickedButton() == C:
                    self.打开窗口(index["类名3"])
                # elif box.clickedButton() == D:
                #     self.打开窗口(index["类名4"])
                else:
                    return
            except Exception as error:
                pass
        except Exception as error:
            logger.error("error={} \n detail {}".format(
                error, traceback.print_exc()))
            return

    def 打开链接(self, url, name=''):
        if name != '':
            increase_counter(ga_category="其余功能使用", name=name)
        for i in url:
            QDesktopServices.openUrl(QUrl(i))

    def 检查更新(self):
        increase_counter(ga_category="其余功能使用", name="检查更新")
        self.网盘检查()
        if self.网盘报错 == 1:
            box = QMessageBox(QMessageBox.Question, "提示", "无法自动检查更新，请手动前往官网下载")
            box.setWindowIcon(self.icon)
            box.exec_()
        elif self.网盘链接 == '':
            box = QMessageBox(QMessageBox.Question, "提示", "已经是最新版本计算器！")
            box.setWindowIcon(self.icon)
            box.exec_()
        else:
            box = QMessageBox(QMessageBox.Question, "提示", "检测到新的计算器版本,是否更新？")
            box.setWindowIcon(self.icon)
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No
                                   | QMessageBox.Cancel)
            A = box.button(QMessageBox.Yes)
            B = box.button(QMessageBox.No)
            C = box.button(QMessageBox.Cancel)
            A.setText("首页查看更新")
            B.setText("自动更新")
            C.setText(trans("取消"))
            box.exec_()
            if box.clickedButton() == B:
                self.update()
            if box.clickedButton() == A:
                QDesktopServices.openUrl(QUrl('http://dnf.17173.com/jsq/?khd'))

    def processBar(self, process):
        if process < 100:
            self.pbar.setFormat("Downloading..." + str(process) + '%')
            self.pbar.setValue(process)
        else:
            self.遮罩.hide()
            self.pbar.hide()
            path = os.getcwd()
            box = QMessageBox(QMessageBox.Question, "提示",
                              "升级完毕,确定后打开最新版本,删除当前旧版本！")
            box.setWindowIcon(self.icon)
            box.setStandardButtons(QMessageBox.Yes)
            A = box.button(QMessageBox.Yes)
            A.setText(trans("确定"))
            box.exec_()
            if box.clickedButton() == A:
                for p in self.worker:
                    if p.is_alive:
                        p.terminate()
                        p.join()
                newpath = os.path.join(os.getcwd(), "DNF计算器 17173DNF.exe")
                oldpath = sys.argv[0] + '.del'
                p = subprocess.Popen(
                    [
                        newpath,
                        str(主进程PID),
                        str(oldpath)
                        # "--cwd", dirpath,
                        # "--exe_name", filename,
                    ],
                    shell=True,
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
                    | subprocess.DETACHED_PROCESS,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
                p.wait()
                self._signal.emit(1)

    def update(self):
        self.遮罩 = QLabel(self)
        self.遮罩.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.8)}")
        self.遮罩.resize(805, 625)
        self.遮罩.move(0, 0)
        self.遮罩.show()
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.move(325, 300)
        self.pbar.setStyleSheet('''
            QProgressBar{
                border: 2px solid grey;
                border-radius:5px;
                text-align:center;
            }
            QProgressBar::chunk {
                background-color: #05B8CC;
                width: 10px;
            }
        ''')
        self.pbar.setFormat("Downloading...")
        self.pbar.show()
        self.thread = Worker(fileURL=self.网盘链接)
        self.thread.sinOut.connect(self.processBar)
        self.thread.start()


class SetWindows(QWidget):
    # _signal = QtCore.pyqtSignal(int)

    def __init__(self, worker, parWin):
        super().__init__()
        self.worker = worker
        self.parWin = parWin
        self.ui()
        self.read()

    def closeEvent(self, event):
        self.保存设置()
        super().closeEvent(event)

    def read(self):
        if not os.path.exists("ResourceFiles/Config/set.json"):
            return
        with open("ResourceFiles/Config/set.json", encoding='utf-8') as fp:
            set_info = json.load(fp)
        fp.close()
        for i in set_info.keys():
            try:
                self.ComboBoxList[int(i)].setCurrentIndex(set_info[i])
            except:
                pass

    def ui(self):
        self.setStyleSheet('''QToolTip {
                   background-color: black;
                   color: white;
                   border: 0px
                   }''')
        self.height = 625
        with open(trans("ResourceFiles/Config/config.json"),
                  encoding='utf-8') as fp:
            self.height = len(json.load(fp)) * 50 + 20
        fp.close()

        self.setMinimumSize(805, 625)
        self.setWindowTitle(trans('全局设置选项(需重启计算器生效)'))
        self.icon = QIcon('ResourceFiles/img/logo.ico')
        self.setWindowIcon(self.icon)

        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(750, self.height)
        bgcolor = QLabel(self)
        bgcolor.resize(805, 625)
        bgcolor.setStyleSheet("QLabel{background:url('" +
                              trans('ResourceFiles/img/分类') + "/bg.png')}")

        with open(trans("ResourceFiles/Config/Config.json"),
                  encoding='utf-8') as fp:
            set_info = json.load(fp)
        fp.close()

        self.ComboBoxList = {}
        num = 0
        for i in set_info:
            txt_box = QLabel(self.topFiller)
            txt_box.setText('{}. {}'.format(num + 1, i['说明']))
            txt_box.resize(700, 20)
            txt_box.move(50, 10 + 50 * num)
            txt_box.setStyleSheet(
                'QLabel{font-size:13px;color:rgb(175,148,89)}')
            txt2_box = QLabel(self.topFiller)
            txt2_box.setText(i['名称'])
            txt2_box.resize(70, 20)
            txt2_box.move(60, 30 + 50 * num + 5)
            txt2_box.setStyleSheet(
                'QLabel{font-size:13px;color:rgb(175,148,89)}')
            self.ComboBoxList[num] = MyQComboBox(self.topFiller,
                                                 useWheel=False)
            self.ComboBoxList[num].addItems(i['选项'])
            self.ComboBoxList[num].resize(100, 20)
            self.ComboBoxList[num].move(50 + 80, 30 + 50 * num + 5)
            self.ComboBoxList[num].setCurrentIndex(i['default'])
            num += 1

        self.scroll = QScrollArea()
        self.scroll.setFrameShape(QFrame.NoFrame)
        self.scroll.setStyleSheet("QScrollArea {background-color:transparent}")
        self.scroll.setStyleSheet(游戏滚动条样式模拟)
        self.scroll.viewport().setStyleSheet("background-color:transparent")
        self.scroll.setWidget(self.topFiller)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.setLayout(self.vbox)

    def 保存设置(self):
        set_data = {}
        for i in self.ComboBoxList.keys():
            set_data[i] = self.ComboBoxList[i].currentIndex()
        with open("ResourceFiles/Config/set.json", "w",
                  encoding='utf-8') as fp:
            json.dump(set_data, fp)
        fp.close()
        box = QMessageBox(QMessageBox.Warning, "提示", "保存完毕，重启计算器才能生效，是否重启")
        box.setWindowIcon(self.icon)
        yes = box.addButton(self.tr(trans("确定")), QMessageBox.YesRole)
        no = box.addButton(self.tr(trans("取消")), QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton() == yes:
            self.立即重启()

    # def 返回原页(self):
    #     #用self.close()无法关闭，所以用发射信号的方法在父窗口关闭页面
    #     self.是否保存 = 0
    #     data_int = 1
    #     # 发送信号
    #     self._signal.emit(data_int)

    def 立即重启(self):
        for p in self.worker:
            if p.is_alive:
                p.terminate()
                p.join()
        # self.close()
        self.parWin.close()
        if 目录.endswith('py'):
            python = sys.executable
            os.execl(python, python, *sys.argv)
        else:
            os.startfile(目录)
        # 用的是杀死进程的方法，有机会改改
        os.system("taskkill /pid {} -f".format(主进程PID))
        # self.close()


if __name__ == '__main__':
    主进程PID = os.getpid()
    目录 = sys.argv[0]
    if len(sys.argv) > 1:
        try:
            # 杀老进程
            os.system("taskkill /pid {} -f".format(sys.argv[1]))
            time.sleep(2)
            if ("main.py" not in sys.argv[2]) and ("del" in sys.argv[2]):
                # 删除老版本
                os.remove(sys.argv[2])
                # shutil.rmtree('download')
        except Exception as error:
            logger.error("error={} \n detail {}".format(
                error, traceback.print_exc()))
    if 窗口显示模式 == 1:
        if hasattr(qtc.Qt, 'AA_EnableHighDpiScaling'):
            QtWidgets.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling,
                                                True)
        if hasattr(qtc.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps,
                                                True)
    app = QApplication([])

    try:
        instance = 选择窗口()
        instance._signal.connect(instance.closeSet)
        win = MainWindow(instance)
        win.show()
    except Exception as error:
        logger.error("error={} \n detail {}".format(error,
                                                    traceback.print_exc()))

    用户须知 = False

    try:
        instance.报错提示.exec()
    except Exception as error:
        pass
    if "main.py" not in sys.argv[0]:
        try:
            with open("ResourceFiles/Config/release_version.json", "r+") as fp:
                versionInfo = json.load(fp)
                展示信息 = versionInfo['ShowChangeLog']
                用户须知 = versionInfo['agreement']
                versionInfo['ShowChangeLog'] = False
                fp.seek(0)
                json.dump(versionInfo, fp, ensure_ascii=False)
                fp.truncate()
            fp.close()
            if not os.path.exists("ResourceFiles/Config/notice_version.json"):
                with open("ResourceFiles/Config/notice_version.json",
                          "w",
                          encoding='utf-8') as fp:
                    json.dump({"time": ""}, fp)
                pass
            with open("ResourceFiles/Config/notice_version.json", "r+") as fp:
                versionInfo = json.load(fp)
                通知时间 = versionInfo['time']
                versionInfo['time'] = instance.通知时间
                fp.seek(0)
                json.dump(versionInfo, fp, ensure_ascii=False)
                fp.truncate()
            fp.close()
            if ("main.py" not in sys.argv[0]) and 配置格式有误:
                instance.配置错误.exec()
            if not 用户须知:
                instance.版本提示.exec()
                if instance.版本提示.clickedButton() == instance.版本提示A:
                    with open("ResourceFiles/Config/release_version.json",
                              "r+") as fp:
                        versionInfo = json.load(fp)
                        versionInfo['agreement'] = True
                        用户须知 = True
                        fp.seek(0)
                        json.dump(versionInfo, fp, ensure_ascii=False)
                        fp.truncate()
                    fp.close()
                else:
                    os.system("taskkill /pid {} -f".format(主进程PID))

            if ("main.py" not in sys.argv[0]
                ) and instance.通知时间 != 通知时间 and 多语言开关 == 0 and 自动检查更新 == 0:
                instance.消息通知.exec()
            if ("main.py" not in sys.argv[0]) and 展示信息 and 多语言开关 == 0:
                QDesktopServices.openUrl(
                    QUrl('http://dnf.17173.com/jsq/changlog.html#/'))

        except Exception as error:
            logger.error("error={} \n detail {}".format(
                error, traceback.print_exc()))
            pass
    else:
        用户须知 = True
    if 用户须知:
        instance.thread_init()
        app.exec_()
