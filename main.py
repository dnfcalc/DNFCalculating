import multiprocessing

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
import importlib
from PublicReference.common import *
from PublicReference.utils.calc_core import calc_core
from PublicReference.utils.producer_consumer import producer_data, consumer, thread_num
import json
import os
import traceback
# from PublicReference.utils.lanzou.api import LanZouCloud
from lanzou.api import LanZouCloud
from PublicReference.utils import zipfile
from pathlib import Path
import shutil
import sys
import time
import urllib.request
import subprocess

主进程PID = ''

if __name__ == '__main__':
    multiprocessing.freeze_support()

class 选择窗口(QMainWindow):
    计算器版本 = ''
    云端版本 = ''
    自动检查版本 = False
    网盘链接 = ''
    网盘报错 = 0

    def __init__(self):
        super().__init__()
        self.thread_init()
        self.ui()
        self.char_window = None

    def thread_init(self):
        try:
            # 工作队列
            work_queue = multiprocessing.JoinableQueue()
            work_queue.cancel_join_thread()  # or else thread that puts data will not term
            producer_data.work_queue = work_queue
            # 工作进程
            workers = []
            for i in range(thread_num):
                p = multiprocessing.Process(target=consumer, args=(work_queue, calc_core), daemon=True, name="worker#{}".format(i + 1))
                p.start()
                workers.append(p)

            # logger.info("已启动{}个工作进程".format(thread_num))

            self.worker = workers
            pass
        except Exception as error:
            return error

    def 网盘检查(self):
        try:
            lzy = LanZouCloud()
            fileURL = ''
            folder_info = lzy.get_folder_info_by_url('https://pan.lanzous.com/b01bfj76f')
            if folder_info.code != LanZouCloud.SUCCESS:
                self.网盘链接 =  ''
                self.网盘报错 = 1
                return
            # resp = urllib.request.urlopen('http://dnf.17173.com/jsq/instructions.html?j')
            for file in folder_info.files:
                if file.name.startswith("DNF计算器"):
                    self.云端版本 = file.name.replace(".zip"," 17173DNF.exe")
                    fileURL = file.url
                    if file.name.replace("DNF计算器","").replace(".zip","").replace("-",".") == self.计算器版本[5:]:
                        self.网盘链接 = ''
                        return 
            self.网盘链接 =  fileURL
        except Exception as error:
            self.网盘链接 =  ''
            self.网盘报错 = 1
            return

    def ui(self):
        角色列表 = []
        self.setStyleSheet('''QToolTip { 
                   background-color: black; 
                   color: white; 
                   border: 0px
                   }''')
        self.setMinimumSize(805,630)
        self.setMaximumSize(805,1520)
        if not os.path.exists('./ResourceFiles'):
            QMessageBox.information(self,"解压错误",  "未找到资源文件，请将压缩包中ResourceFiles解压到同目录后打开计算器")    
            return     
        with open("ResourceFiles/Config/adventure_info.json",encoding='utf-8') as fp:
            角色列表 = json.load(fp)
        fp.close()
        with open("ResourceFiles/Config/release_version.json") as fp:
            versionInfo = json.load(fp)
            self.计算器版本 += versionInfo['version'].replace('-','.')
            self.自动检查版本 = versionInfo['AutoCheckUpdate']
        fp.close()
        self.setWindowTitle('DNF搭配计算器&17173DNF专区-'+self.计算器版本+' (技能模板仅供参考，请根据自身情况修改)')
        self.icon = QIcon('ResourceFiles/img/logo.ico')
        self.setWindowIcon(self.icon)

        bgcolor = QLabel(self)
        bgcolor.resize(805,1520)
        bgcolor.setStyleSheet("QLabel{background-color:rgba(0,0,0,1)}")

        self.char_img = []
        self.family_img = []
        is_gif = os.path.exists('动态头像')
        for i in range(1, 76):
            if is_gif:
                self.char_img.append(QMovie("动态头像/"+ str(i) +".gif"))
            else:
                self.char_img.append(QPixmap("ResourceFiles/img/头像/"+ str(i) +".png"))
        for i in range(17):
            self.family_img.append(QPixmap("ResourceFiles/img/分类/"+ str(i) +".png"))

        
        wrapper = QWidget()
        self.setCentralWidget(wrapper)
        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(750, 1520)

        count = 0
        for i in range(75):
            img_box = QLabel(self.topFiller)
            if is_gif:
                img_box.setMovie(self.char_img[i])
                self.char_img[i].start()
            else:
                img_box.setPixmap(self.char_img[i])
            img_box.resize(121, 90)
            img_box.move(120 + (count % 5) * 125, 10 + int(count / 5) * 100)
            
            if i  < 75:
                if 角色列表[i]["类名"] != '空':
                    img_box_2 = QLabel(self.topFiller)
                    img_box_2.setPixmap(self.family_img[16])
                    img_box_2.resize(121, 90)
                    img_box_2.move(120 + (count % 5) * 125, 10 + int(count / 5) * 100)
                    txt_box = QLabel(self.topFiller)
                    txt_box.setStyleSheet('QLabel{font-size:13px;color:rgb(175,148,89)}')
                    txt_box.setText(角色列表[i]["显示名称"])
                    txt_box.resize(121, 24)
                    txt_box.setAlignment(Qt.AlignCenter)
                    txt_box.move(120 + (count % 5) * 125, 76 + int(count / 5) * 100)
                    butten = QPushButton(self.topFiller)
                    butten.setStyleSheet(按钮样式2)
                    butten.resize(121, 90)
                    butten.move(120 + (count % 5) * 125, 10 + int(count / 5) * 100)
                    butten.clicked.connect(lambda state, index = 角色列表[i]: self.职业版本判断(index))
                    temp = '<b>作者：<font color="#C66211">'+ 角色列表[i]["作者"] +'</font>'
                    butten.setToolTip(temp)
            else:
                img_box_2 = QLabel(self.topFiller)
                img_box_2.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.8)}")
                img_box_2.resize(121, 90)
                img_box_2.move(120 + (count % 5) * 125, 10 + int(count / 5) * 100)
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
                img_box_2.move(15, 10 + count* 100)
            img_box = QLabel(self.topFiller)
            img_box.setPixmap(self.family_img[i])
            img_box.resize(94, 90)
            img_box.setAlignment(Qt.AlignCenter)
            img_box.move(15, 10 + count* 100)
            count += 1

        # 名称 = ['检查更新', '查看源码', '使用说明', '问题反馈']
        # 链接 = []
        # 链接.append([])
        # 链接.append(['https://github.com/wxh0402/DNFCalculating'])
        # 链接.append(['https://bbs.colg.cn/thread-7917714-1-1.html', 'https://www.bilibili.com/video/BV1F54y1Q7Bz'])
        # 链接.append(['https://jq.qq.com/?_wv=1027&k=9S6c2xIb'])

        count = 0
        # for i in 名称:
        #     butten=QtWidgets.QPushButton(i, self.topFiller)
        #     if i == '检查更新':
        #         butten.clicked.connect(lambda state, index = count: self.检查更新())          
        #     elif i == '问题反馈':
        #         butten.clicked.connect(lambda state, index = count: self.问题反馈())
        #     else:
        #         butten.clicked.connect(lambda state, index = count: self.打开链接(链接[index]))
        #     butten.move(120 + 4 * 125, 10 + (count + 1) * 100)    
        #     butten.setStyleSheet(按钮样式3)
        #     butten.resize(121,90)
        #     count += 1

        butten=QtWidgets.QPushButton('首页\n手册|日志|源码', self.topFiller)
        butten.clicked.connect(lambda state, index = count: self.打开链接(['http://dnf.17173.com/jsq/?khd']))
        butten.move(120 + 4 * 125, 10 + (count + 1) * 100)    
        butten.setStyleSheet(按钮样式3)
        butten.resize(121,90)

        count += 1
    
        butten=QtWidgets.QPushButton('检查更新', self.topFiller)
        butten.clicked.connect(lambda state, index = count: self.检查更新())
        butten.move(120 + 4 * 125, 10 + (count + 1) * 100)    
        butten.setStyleSheet(按钮样式3)
        butten.resize(121,90)

        if self.自动检查版本:
            try:
                self.网盘检查()
                if self.网盘报错 == 1:
                    self.报错提示 = QMessageBox(QMessageBox.Question, "提示", "无法自动检查更新，请在每周三/四自行前往检查版本")  
                    # box.exec_()            
                if self.网盘链接 != '':
                    m_red_SheetStyle = "padding-left:3px;min-width: 25px; min-height: 16px;border-radius: 5px; background:red;color:white"
                    label = QLabel("New", self.topFiller)
                    label.move(115 + 4 * 125 + 90, 30 + (count + 1) * 100)
                    label.setStyleSheet(m_red_SheetStyle)
            except Exception as error:
                pass
        count += 1

        butten=QtWidgets.QPushButton('问题反馈', self.topFiller)
        butten.clicked.connect(lambda state, index = count: self.问题反馈())
        butten.move(120 + 4 * 125, 10 + (count + 1) * 100)    
        butten.setStyleSheet(按钮样式3)
        butten.resize(121,90)
        count += 1

        butten=QtWidgets.QPushButton('打   赏', self.topFiller)
        butten.clicked.connect(lambda state , index = count:self.打赏())
        butten.move(120 + 4 * 125, 10 + (count + 1) * 100)    
        butten.setStyleSheet(按钮样式3)
        butten.resize(121,90)
        count += 1

        butten=QtWidgets.QPushButton('', self.topFiller)
        butten.clicked.connect(lambda state, index = count: self.打开链接(['http://dnf.17173.com/?jsq']))
        butten.move(120 + 4 * 125, 10 + (count + 1) * 100)    
        butten.setStyleSheet(按钮样式3)
        butten.resize(121,90)
        count += 1

        self.scroll = QScrollArea()
        self.scroll.setStyleSheet("QScrollArea {background-color:transparent}")
        self.scroll.viewport().setStyleSheet("background-color:transparent")
        self.scroll.setWidget(self.topFiller)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        wrapper.setLayout(self.vbox)

    def 打开窗口(self, name):
        if self.char_window != None:
            self.char_window.close()
        module_name = "Part."+name
        职业 = importlib.import_module(module_name)
        self.char_window = eval("职业."+name + '()')
        self.char_window.show()
    
    def 打赏(self):
        self.w = QWidget()
        # 设置窗口大小
        self.w.resize(300, 300)
        # 移动窗口位置
        # self.w.move(600, 250)
        # 设置窗口标题
        self.w.setWindowTitle('打赏-微信')
        
        # self.w.icon = QIcon('./ResourceFiles/img/logo.ico')
        self.w.setWindowIcon(self.icon)
        主背景 = QLabel(self.w)
        主背景.setPixmap(QPixmap('./ResourceFiles/img/二维码.png'))
        # 主背景.move(0, int((self.w.height() - 1230) / 6))
        # 主背景.setGraphicsEffect(主背景透明度)

        # self.w.setStyleSheet("background-image: url(:/ResourceFiles/img/二维码.jpg);")
        # 展示窗口
        self.w.show()


    def 职业版本判断(self, index):
        try:
            if index["类名2"] == '无':
                self.打开窗口(index["类名"])
                return
            else:
                box = QMessageBox(QMessageBox.Question, "提示", "请选择要打开的版本")
            box.setWindowIcon(self.icon)
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            A = box.button(QMessageBox.Yes)
            B = box.button(QMessageBox.No)
            C = box.button(QMessageBox.Cancel)
            if index["序号"] == "41":
                A.setText('BUFF')
                B.setText('战斗')
            else:
                A.setText('二觉')
                B.setText('三觉')
            C.setText('取消')
            box.exec_()
            if box.clickedButton() == A:
                self.打开窗口(index["类名"])
            elif box.clickedButton() == B:
                self.打开窗口(index["类名2"])
            else:
                return
        except Exception as error:
            logger.error("error={} \n detail {}".format(error,traceback.print_exc()))
            return
        
    def 打开链接(self, url):
        for i in url:
            QDesktopServices.openUrl(QUrl(i))
    
    def 问题反馈(self):
        box = QMessageBox(QMessageBox.Question, "提示", "请选择反馈方式")  
        box.setWindowIcon(self.icon)
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        A = box.button(QMessageBox.Yes)
        B = box.button(QMessageBox.No)
        C = box.button(QMessageBox.Cancel)
        A.setText("B站")
        B.setText("QQ群")  
        C.setText("取消")
        box.exec_()
        if box.clickedButton() == A:
            self.打开链接(['https://www.bilibili.com/read/cv8424945'])
        if box.clickedButton() == B:
            self.打开链接(['https://jq.qq.com/?_wv=1027&k=9S6c2xIb'])

    def 检查更新(self):
        self.网盘检查()
        if self.网盘报错 == 1:
            box = QMessageBox(QMessageBox.Question, "提示", "无法自动检查更新，请手动前往官网下载")  
            box.exec_()
        elif self.网盘链接 == '':
            box = QMessageBox(QMessageBox.Question, "提示", "已经是最新版本计算器！")  
            box.exec_()
        else:
            box = QMessageBox(QMessageBox.Question, "提示", "检测到新的计算器版本,是否更新？")  
            box.setWindowIcon(self.icon)
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            A = box.button(QMessageBox.Yes)
            B = box.button(QMessageBox.No)
            C = box.button(QMessageBox.Cancel)
            A.setText("首页查看更新") 
            B.setText("自动更新")
            C.setText("取消")
            box.exec_()
            if box.clickedButton() == B:
                self.自动更新(self.网盘链接)
            if box.clickedButton() == A:
                QDesktopServices.openUrl(QUrl('http://dnf.17173.com/jsq/?khd'))

    def 自动更新(self,fileURL):
        path  = os.getcwd()+"/download"
        lzy = LanZouCloud()
        lzy.down_file_by_url(fileURL,'', path , callback=self.show_progress, downloaded_handler=self.after_downloaded)

    def after_downloaded(self,file_path):
        path = os.getcwd()
        zip_file = zipfile.ZipFile(file_path)
        zip_list = zip_file.namelist() # 得到压缩包里所有文件
        for f in zip_list:
            if not f.endswith('desktop.ini'):
                zip_file.extract(f, path)
                # extracted_path.rename(newName)
                # 循环解压文件到指定目录
        zip_file.close()
        shutil.rmtree('download')
        box = QMessageBox(QMessageBox.Question, "提示", "升级完毕,确定后打开最新版本,删除当前旧版本！")  
        box.setStandardButtons(QMessageBox.Yes)
        A = box.button(QMessageBox.Yes)
        A.setText("确定")
        box.exec_()
        if box.clickedButton() == A:
            for p in self.worker:
                if p.is_alive:
                    p.terminate()
                    p.join()
            self.close()
            newpath = os.path.join(os.getcwd(),self.云端版本)
            oldpath = sys.argv[0]
            p = subprocess.Popen([
                newpath,str(主进程PID), str(oldpath)
                # "--cwd", dirpath,
                # "--exe_name", filename,
            ], shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.wait()    
            # os.system(newpath)
        
    def show_progress(self,file_name, total_size, now_size):
        percent = now_size / total_size
        bar_len = 40  # 进度条长总度
        bar_str = '>' * round(bar_len * percent) + '=' * round(bar_len * (1 - percent))
        print('\r{:.2f}%\t[{}] {:.1f}/{:.1f}MB | {} '.format(
            percent * 100, bar_str, now_size / 1048576, total_size / 1048576, file_name), end='')
        if total_size == now_size:
            print('')  # 下载完成换行

import PyQt5.QtCore as qtc
if __name__ == '__main__':
    主进程PID = os.getpid() 
    if len(sys.argv) > 1:
        try:
            #杀老进程
            os.system("taskkill /pid {} -f".format(sys.argv[1]))
            time.sleep(5)
            if "main.py" not in sys.argv[2]:
            # 删除老版本
                os.remove(sys.argv[2])
        except Exception as error:
            logger.error("error={} \n detail {}".format(error,traceback.print_exc())) 
    if 窗口显示模式 == 1:
        if hasattr(qtc.Qt, 'AA_EnableHighDpiScaling'):
            QtWidgets.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True)
        if hasattr(qtc.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication([])
    instance = 选择窗口()
    instance.show()
    try:
        instance.报错提示.exec()
    except Exception as error:
        pass    
    try:
        with open("ResourceFiles/Config/release_version.json", "r+") as fp:
            versionInfo = json.load(fp)
            展示信息 = versionInfo['ShowChangeLog']
            versionInfo['ShowChangeLog'] = False
            fp.seek(0)
            json.dump(versionInfo,fp,ensure_ascii=False)
            fp.truncate()
        fp.close()
        if 展示信息 :
            QDesktopServices.openUrl(QUrl('http://dnf.17173.com/jsq/changlog.html#/'))
    except Exception as error:
        logger.error("error={} \n detail {}".format(error,traceback.print_exc())) 
        pass
    app.exec_()
