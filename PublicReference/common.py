from PublicReference.equipment.equ_list import *

装备版本 = "GF"
装备增幅版本 = "GF"

# with open("ResourceFiles/Config/release_version.json") as fp:
#     versionInfo = json.load(fp)
#     装备版本 = versionInfo['EquipmentVersion'].upper()
#     装备增幅版本 = versionInfo['ZFVersion'].upper()
# fp.close()


class 属性():
    实际名称 = ''
    角色 = ''
    职业 = ''
    版本 = 装备版本
    增幅版本 = 装备增幅版本

    武器选项 = []
    类型选择 = []
    
    类型 = ''
    防具类型 = ''
    防具精通属性 = [] 

    基础力量 = 0
    基础智力 = 0
    基础体力 = 0
    基础精神 = 0
    
    力量 = 0
    智力 = 0
    体力 = 0
    精神 = 0

    进图力量 = 0.0
    进图智力 = 0.0
    进图体力 = 0.0
    进图精神 = 0.0

    技能栏 = []
    技能序号 = {}

    装备栏 = []
    套装栏 = []
    武器类型 = ''

    是否增幅 = [0] * 12
    强化等级 = [12] * 12
    改造等级 = [5] * 12
    武器锻造等级 = 0

    护石第一栏 = '无'
    护石第二栏 = '无'
    护石第三栏 = '无'

    def 穿戴装备(self, 装备, 套装):
        self.装备栏 = 装备
        self.套装栏 = 套装
        self.武器类型 = 装备列表[装备序号[self.装备栏[11]]].类型

    def 穿戴装备计算套装(self, 装备):
        self.装备栏 = 装备
        self.适用套装计算()
        self.武器类型 = 装备列表[装备序号[self.装备栏[11]]].类型

    def 适用套装计算(self):
        套装 = []
        套装字典 = {}
        for i in self.装备栏:
            j = 装备列表[装备序号[i]].所属套装
            if j == '智慧产物':
                try:
                    k = 装备列表[装备序号[i]].所属套装2
                    套装字典[k] = 套装字典.get(k, 0) + 1
                except:
                    pass
            elif j != '无':
                套装字典[j] = 套装字典.get(j, 0) + 1

        for i in 套装字典.keys():
            if 套装字典[i] >= 2 and (i + '[2]') in 套装序号.keys():
                套装.append(i + '[2]')
            if 套装字典[i] >= 3 and (i + '[3]') in 套装序号.keys():
                套装.append(i + '[3]')
            if 套装字典[i] >= 5 and (i + '[5]') in 套装序号.keys():
                套装.append(i + '[5]')

        self.套装栏 = copy(套装)
        

    def 防具基础(self):
        for i in [0,1,2,3,4]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            if temp.等级 > 85 or self.转甲选项 == 1:
                self.力量 += temp.力量[self.防具类型]
                self.智力 += temp.智力[self.防具类型]
            else:
                self.力量 += temp.力量[temp.类型]
                self.智力 += temp.智力[temp.类型]

            精通数值 = self.防具精通计算(i)
            if '力量' in self.防具精通属性:
                self.力量 += 精通数值
            if '智力' in self.防具精通属性:
                self.智力 += 精通数值

    def 增幅基础(self):
        for i in range(0,12):
            temp = 装备列表[装备序号[self.装备栏[i]]]
            if self.是否增幅[i] and temp.所属套装 != '智慧产物':
                x = 增幅计算(temp.等级,temp.品质,self.强化等级[i],self.增幅版本)
                if '物理' in self.类型 or '力量' in self.类型:
                    self.力量 += x
                else:
                    self.智力 += x

    def 首饰基础(self):
        for i in [5,6,7]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            self.力量 += temp.力量
            self.智力 += temp.智力
            self.物理攻击力 += temp.物理攻击力
            self.魔法攻击力 += temp.魔法攻击力
            self.独立攻击力 += temp.独立攻击力

    def 特殊基础(self):
        for i in [8,9,10]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            self.力量 += temp.力量
            self.智力 += temp.智力
            self.物理攻击力 += temp.物理攻击力
            self.魔法攻击力 += temp.魔法攻击力
            self.独立攻击力 += temp.独立攻击力
        
        #耳环
        temp = 装备列表[装备序号[self.装备栏[8]]]
        if temp.所属套装 != '智慧产物':
            x = 耳环计算(temp.等级,temp.品质,self.强化等级[8])
            self.物理攻击力 += x
            self.魔法攻击力 += x
            self.独立攻击力 += x
        
        #辅助装备、魔法石
        for i in [9,10]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            if temp.所属套装 != '智慧产物':
                x = 左右计算(temp.等级,temp.品质,self.强化等级[i])
                self.力量 += x
                self.智力 += x

    def 武器基础(self):
        temp = 装备列表[装备序号[self.装备栏[11]]]

        self.力量 += temp.力量
        self.智力 += temp.智力
        self.物理攻击力 += temp.物理攻击力
        self.魔法攻击力 += temp.魔法攻击力
        self.独立攻击力 += temp.独立攻击力

        if temp.所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(temp.等级,temp.品质,self.强化等级[11],self.武器类型,'物理')
            self.魔法攻击力 += 武器计算(temp.等级,temp.品质,self.强化等级[11],self.武器类型,'魔法')
            self.独立攻击力 += 锻造计算(temp.等级,temp.品质,self.武器锻造等级)

    def 装备基础(self):
        if 调试开关 == 0:
            self.防具基础()
            self.首饰基础()
            self.特殊基础()
            self.武器基础()
            self.增幅基础()

    def 获取增幅(self, 部位):
        return self.是否增幅[部位列表.index(部位)]

    def 获取强化(self, 部位):
        return self.强化等级[部位列表.index(部位)]

    def 获取改造(self, 部位):
        return self.改造等级[部位列表.index(部位)]

    def 装备检查(self, 装备名称):
        for i in self.装备栏:
            if i == 装备名称:
                return True
        return False

    def 单技能等级加成(self, 名称, lv):
        if self.装备描述 ==1:
            return "{} Lv +{}<br>".format(名称,lv)
        else:
            for i in self.技能栏:
                if i.名称 == 名称:
                    i.等级加成(lv)            
        return ''

    def 等级溢出判断(self, 装备, 套装):
        self.穿戴装备(装备, 套装)
        self.装备属性计算()
        temp = []
        for i in self.技能栏:
            if i.等级溢出 == 1:
                temp.append(i.名称)
        return temp

class 窗口(QWidget):
    calc_done_signal = pyqtSignal()
    update_remaining_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.calc_done_signal.connect(self.calc_done)
        self.update_remaining_signal.connect(self.update_remaining)

        self.窗口属性输入()
        self.界面()
        self.布局界面()
        
        #创建配置文件夹
        path = './ResourceFiles/{}/set'.format(self.角色属性A.实际名称)
        if not os.path.exists(path):
            os.makedirs(path) 
        
        self.存档列表读取()

        #判断从哪读取数据
        if os.path.exists(path + '/attr.ini'):
            self.载入配置('set')
        else:
            self.载入配置('reset')
            
        self.click_window(0)

    def 关闭窗口(self):
        self.close()

    def closeEvent(self, event):
        self.保存配置(self.存档位置)
        self.排行窗口列表.clear()
        super().closeEvent(event)

    def 窗口属性输入(self):
        pass

    def 界面(self):
        # self.setWindowTitle(self.角色属性A.实际名称 + "搭配计算器&17173DNF专区 （点击标签栏按钮切换界面）"+"装备版本："+self.角色属性A.版本 + " 增幅版本：" + self.角色属性A.增幅版本)
        self.setWindowTitle(self.角色属性A.实际名称 + "搭配计算器&17173DNF专区 （点击标签栏按钮切换界面）")
        self.icon = QIcon('./ResourceFiles/'+self.角色属性A.实际名称 + '/技能/BUFF.png')
        self.setWindowIcon(self.icon)
        self.setStyleSheet('''QToolTip { 
                   background-color: black; 
                   color: white; 
                   border: 0px
                   }''')
        背景颜色 = QLabel(self)
        背景颜色.resize(self.width(),self.height())
        背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1)}")
        主背景透明度 = QGraphicsOpacityEffect()
        主背景透明度.setOpacity(0.15)
        self.主背景图片 = QPixmap('./ResourceFiles/'+self.角色属性A.实际名称 + "/bg.jpg")
        主背景 = QLabel(self)
        主背景.setPixmap(self.主背景图片)
        主背景.move(0, int((self.height() - 1230) / 6))
        主背景.setGraphicsEffect(主背景透明度)

        self.技能图片 = []
        for i in self.角色属性A.技能栏:
            path = './ResourceFiles/'+self.角色属性A.实际名称 + "/技能/" + i.名称 + ".png"
            self.技能图片.append(QPixmap(path))
        
        self.输出窗口列表 = []
        self.排行窗口列表 = []

        self.当前页面 = 0
        self.全选状态 = 0

        self.装备图片 = []
        self.遮罩透明度 = []
        self.装备图片按钮 = []
        for i in 装备列表:
            self.遮罩透明度.append(QGraphicsOpacityEffect())
            self.装备图片按钮.append('')
        self.装备选择状态 = []
        self.装备条件选择 = []
        for i in 装备列表:
            path = './ResourceFiles/img/装备/' + str(装备序号[i.名称]) + '.gif'
            self.装备图片.append(QMovie(path))
            self.装备选择状态.append(0)
        
        self.有效防具套装 = []
        self.有效首饰套装 = []
        self.有效特殊套装 = []
        self.有效上链左套装 = []
        self.有效镯下右套装 = []
        self.有效环鞋指套装 = []
        self.有效总套装列表 = [self.有效防具套装, self.有效首饰套装, self.有效特殊套装, self.有效上链左套装, self.有效镯下右套装, self.有效环鞋指套装]
        self.有效武器列表 = []
        self.组合名称选择 = []
        self.有效穿戴组合 = []
        self.有效穿戴套装 = []
        self.百变怪列表 = []
        self.有效部位列表 = []
        self.排行数据 = []

        # 工具栏
        self.frame_tool = QFrame(self)
        self.frame_tool.setGeometry(0, 0, self.width(), 24)
        if self.初始属性.职业分类 == '输出':
            self.页面名称 = ["装备/选择/打造", "技能/符文/药剂", "基础/细节/修正","神话属性修正","辟邪玉/希洛克/黑鸦","自选装备计算"]
        else:
            self.页面名称 = ["装备/选择/打造", "技能/符文/其它", "基础/细节/修正","神话属性修正","自选装备计算"]
        self.页面数量 = len(self.页面名称)
        self.btn_group = QButtonGroup(self.frame_tool)
        self.window_btn = []
        for i in range(0, self.页面数量):
            self.window_btn.append(QToolButton(self.frame_tool))
            self.window_btn[-1].setText(self.页面名称[i])
            self.window_btn[-1].resize(int(self.width() / self.页面数量), 24)
            self.window_btn[-1].move(self.window_btn[-1].width() * i, 0)
            self.window_btn[-1].clicked.connect(lambda state, index = i: self.click_window(index))
            self.btn_group.addButton(self.window_btn[-1], i)

        # 2. 工作区域
        self.main_frame = QFrame(self)
        self.main_frame.setGeometry(0, 25, self.width(), self.height() - self.frame_tool.height())

        # 创建堆叠布局
        self.stacked_layout = QStackedLayout(self.main_frame)
        
        self.main_frame1 = QMainWindow()
        self.main_frame2 = QMainWindow()
        self.main_frame3 = QMainWindow()
        self.main_frame4 = QMainWindow()
        self.main_frame5 = QMainWindow()
        self.main_frame6 = QMainWindow()

        self.界面1()
        self.界面2()
        self.界面3()
        self.界面4()
        if self.初始属性.职业分类 == '输出':
            self.界面6()
        self.界面5()


    def 布局界面(self):
        # 把布局界面放进去
        self.stacked_layout.addWidget(self.main_frame1)
        self.stacked_layout.addWidget(self.main_frame2)
        self.stacked_layout.addWidget(self.main_frame3)
        self.stacked_layout.addWidget(self.main_frame4)
        if self.初始属性.职业分类 == '输出':
            self.stacked_layout.addWidget(self.main_frame6)
        self.stacked_layout.addWidget(self.main_frame5)


    def 套装描述(self, i):
        temp = '<font size="3" face="宋体">'
        for n in [2, 3, 5]:
            try:
                描述 = ''
                if self.角色属性A.职业分类 == 'BUFF':
                    描述 = 套装列表[套装序号['{}[{}]'.format(i.名称, n)]].装备描述_BUFF(self.角色属性A)[:-4]
                else:
                    描述 = 套装列表[套装序号['{}[{}]'.format(i.名称, n)]].装备描述(self.角色属性A)[:-4]
                if 描述 != '':
                     temp+='<font color="#78FF1E">' + i.名称 + '[{}]</font><br>'.format(n)
                     temp+=描述
                     temp+='<br>'
            except:
                pass
        return temp[:-4] + '</font>'        

    def 单件描述(self, i):
        temp = '<font size="3" face="宋体"><font color="{}">'.format(颜色[i.品质])
        temp += i.名称+'</font><br>'+ i.类型 + '-' + i.部位 + '<br>'
        if self.角色属性A.职业分类 == 'BUFF':
            temp += i.装备描述_BUFF(self.角色属性A)
        else:
            temp += i.装备描述(self.角色属性A)
        return temp[:-4] +'</font>'

    def 界面1(self):
        self.一键站街设置输入 = []
        水平间距 = [0, 350, 640]
        counter1 = 0
        for 布局列表 in [防具套装, 上链左套装 + 镯下右套装 + 环鞋指套装 , 首饰套装 + 特殊套装]:
            counter2 = 0
            for 名称 in 布局列表:
                for i in 套装列表:
                    if i.名称 == 名称 and i.件数 == 2:
                        self.按钮 = QPushButton(i.名称, self.main_frame1)
                        self.按钮.move(水平间距[counter1] + 10, 10 + counter2 * 32)
                        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
                        self.按钮.resize(120, 28)
                        self.按钮.clicked.connect(lambda state, index = i.名称: self.套装按钮点击事件(index))
                        self.按钮.setToolTip(self.套装描述(i))            
                        counter3 = 0
                        for 品质 in ['神话', '史诗']:
                            for 部位 in ['上衣', '头肩', '下装', '鞋', '腰带', '项链', '手镯', '戒指', '辅助装备', '魔法石', '耳环']:
                                for j in range(0,len(装备列表)):
                                    if 装备列表[j].所属套装 == i.名称 and 装备列表[j].品质 == 品质 and 装备列表[j].部位 == 部位 :
                                        self.图片 = QLabel(self.main_frame1)
                                        self.图片.setMovie(self.装备图片[j])
                                        self.装备图片[j].start()
                                        self.图片.resize(28, 28)
                                        self.图片.move(水平间距[counter1] + 150 + 32 * counter3, 10 + counter2 * 32)
                                        self.按钮 = QPushButton(self.main_frame1)
                                        self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                                        self.按钮.resize(28, 28)
                                        self.按钮.setToolTip(self.单件描述(装备列表[j]))
                                        self.遮罩透明度[j].setOpacity(0.5)
                                        self.按钮.setGraphicsEffect(self.遮罩透明度[j])
                                        self.按钮.clicked.connect(lambda state, index = j: self.装备图标点击事件(index, 10))
                                        self.装备图片按钮[j] = self.按钮
                                        self.装备图片按钮[j].move(水平间距[counter1] + 150 + 32 * counter3, 10 + counter2 * 32)
                                        counter3 += 1
                counter2 += 1
            counter1 += 1
        
        counter5 = 8
        self.按钮 = QPushButton('武器列表', self.main_frame1)
        self.按钮.move(650, 15 + counter5 * 32)
        self.按钮.resize(265,28)
        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
        self.按钮.clicked.connect(lambda state, index = '无': self.套装按钮点击事件(index))
        
        counter4 = 0
        counter5 += 1
        for i in 装备列表:
            if i.部位 == '武器' and i.类型 in self.角色属性A.武器选项 and i.模式 == 0:
                self.图片 = QLabel(self.main_frame1)
                self.图片.setMovie(self.装备图片[装备序号[i.名称]])
                self.装备图片[装备序号[i.名称]].start()
                self.图片.resize(28, 28)
                self.图片.move(657 + 55 * counter4, 15 + counter5 * 32)
                self.按钮 = QPushButton(self.main_frame1)
                self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.按钮.resize(28, 28)
                self.按钮.setToolTip(self.单件描述(i))
                self.遮罩透明度[装备序号[i.名称]].setOpacity(0.5)
                self.按钮.setGraphicsEffect(self.遮罩透明度[装备序号[i.名称]])
                self.按钮.clicked.connect(lambda state, index = 装备序号[i.名称]: self.装备图标点击事件(index, 10))
                self.装备图片按钮[装备序号[i.名称]] = self.按钮
                self.装备图片按钮[装备序号[i.名称]].move(657 + 55 * counter4, 15 + counter5 * 32)
                counter4 += 1
                if counter4 % 5 == 0:
                    counter5 += 1
                    counter4 = 0
        
        if counter4 != 0:
            counter5 += 1
        self.按钮 = QPushButton('智慧产物', self.main_frame1)
        self.按钮.move(650, 20 + counter5 * 32)
        self.按钮.resize(265,28)
        self.按钮.setStyleSheet('QPushButton{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QPushButton:hover{background-color:rgba(65,105,225,0.8)}')
        self.按钮.clicked.connect(lambda state, index = '智慧产物': self.套装按钮点击事件(index))
        
        counter4 = 0
        counter5 += 1
        for i in 装备列表:
            if i.所属套装 == '智慧产物' and i.部位 != '武器' and i.模式 == 0:
                self.图片 = QLabel(self.main_frame1)
                self.图片.setMovie(self.装备图片[装备序号[i.名称]])
                self.装备图片[装备序号[i.名称]].start()
                self.图片.resize(28, 28)
                self.图片.move(657 + 55 * counter4, 20 + counter5 * 32)
                self.按钮 = QPushButton(self.main_frame1)
                self.按钮.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.按钮.resize(28, 28)
                self.按钮.setToolTip(self.单件描述(i))
                self.遮罩透明度[装备序号[i.名称]].setOpacity(0.5)
                self.按钮.setGraphicsEffect(self.遮罩透明度[装备序号[i.名称]])
                self.按钮.clicked.connect(lambda state, index = 装备序号[i.名称]: self.装备图标点击事件(index, 10))
                self.装备图片按钮[装备序号[i.名称]] = self.按钮
                self.装备图片按钮[装备序号[i.名称]].move(657 + 55 * counter4, 20 + counter5 * 32)
                counter4 += 1
                if counter4 % 5 == 0:
                    counter5 += 1
                    counter4 = 0

        self.装备打造选项=[]
        counter = 0
        for i in 部位列表:
            x = QLabel(i, self.main_frame1)
            x.resize(50,20)
            x.setAlignment(Qt.AlignCenter)
            x.setStyleSheet(标签样式)
            if counter < 5:
                x.move(10 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(270 , 500 + (counter - 5) * 25)
                else:
                    x.resize(95,20)
                    x.move(550 , 500 + (counter - 11) * 30)
            counter += 1

        counter = 0
        for i in 部位列表:
            x = MyQComboBox(self.main_frame1)
            x.addItems(['强化','增幅'])
            x.resize(55,20)
            self.装备打造选项.append(x)
            if counter < 5:
                x.move(60 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(330 , 500 + (counter - 5) * 25)
                else:
                    x.move(540 , 500 + (counter - 10) * 30)
            counter += 1
            
        counter = 0
        for i in 部位列表:
            x = MyQComboBox(self.main_frame1)
            for j in range(0,32):
                x.addItem(str(j))
            x.resize(50,20)
            self.装备打造选项.append(x)
            if counter < 5:
                x.move(120 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(390 , 500 + (counter - 5) * 25)
                else:
                    x.move(600 , 500 + (counter - 10) * 30)
            counter += 1

        counter = 0
        for i in 部位列表:
            x = MyQComboBox(self.main_frame1)
            for j in range(0,32):
                x.addItem('改造+' + str(j))
            x.resize(75,20)
            self.装备打造选项.append(x)
            if counter < 5:
                x.move(180 , 504 + counter * 30)
            else:
                if counter < 11:
                    x.move(450 , 500 + (counter - 5) * 25)
                else:
                    x.resize(110,20)
                    x.move(540 , 500 + (counter - 9) * 30)
            counter += 1

        x = MyQComboBox(self.main_frame1)
        for j in range(0,11):
            x.addItem('锻造+' + str(j))
        x.resize(110,20)
        x.move(540 , 504 + (counter - 9) * 30)
        self.装备打造选项.append(x)

        x = MyQComboBox(self.main_frame1)
        x.addItems(self.角色属性A.类型选择)
        x.resize(110,20)
        x.move(540 , 504 + (counter - 8) * 30)
        self.装备打造选项.append(x)

        x = QPushButton('一键全选', self.main_frame1)
        x.clicked.connect(lambda state, index = 1: self.批量选择(index))
        x.move(520 , 400)
        x.resize(105, 24)
        x.setStyleSheet(按钮样式)

        x = QPushButton('一键清空',self.main_frame1)
        x.clicked.connect(lambda state, index = 0: self.批量选择(index))
        x.move(520 , 430)
        x.resize(105, 24)
        x.setStyleSheet(按钮样式)

        x = QPushButton('打造↑',self.main_frame1)
        x.clicked.connect(lambda state: self.批量打造(1))
        x.move(520 , 460)
        x.resize(50, 24)
        x.setStyleSheet(按钮样式)

        x = QPushButton('打造↓',self.main_frame1)
        x.clicked.connect(lambda state: self.批量打造(-1))
        x.move(575 , 460)
        x.resize(50, 24)
        x.setStyleSheet(按钮样式)

        self.称号 = MyQComboBox(self.main_frame1)
        self.宠物 = MyQComboBox(self.main_frame1)

        x = QLabel('称号&宠物选择：', self.main_frame1)
        x.resize(130,20)
        x.move(360 , 400)
        x.setAlignment(Qt.AlignCenter)
        x.setStyleSheet(标签样式)
        
        counter = 0
        for x in [self.称号, self.宠物]:
            x.resize(160,20)
            x.move(350 , 430 + counter * 30)
            counter += 1  

        self.计算按钮1 = QPushButton('开始计算', self.main_frame1)
        self.计算按钮1.clicked.connect(lambda state: self.计算())
        self.计算按钮1.move(990, 610)
        self.计算按钮1.resize(100, 30)
        self.计算按钮1.setStyleSheet(按钮样式)

    def 界面2(self):
        pass

    def 界面3(self):
        pass

    def 界面4(self):

        #第四个布局
        self.main_frame4 = QMainWindow()
        
        self.神话属性选项 = []
        self.神话属性图片 = []

        for j in range(len(装备列表)):
            if 装备列表[j].品质 == '神话':
                self.神话属性图片.append(QLabel(self.main_frame4))
                self.神话属性图片[-1].setMovie(self.装备图片[j])
                self.神话属性图片[-1].setToolTip('<font size="3" face="宋体">' + 装备列表[j].名称 + '<br>'+ 装备列表[j].类型 + '-' + 装备列表[j].部位 + '</font>')
                self.神话属性图片[-1].resize(28, 28)
                self.神话属性图片[-1].move(-1000, -1000)
                self.装备图片[j].start()

        for i in range(4 * 35):
            self.神话属性选项.append(MyQComboBox(self.main_frame4))
            self.神话属性选项[i].resize(150, 18)
            self.神话属性选项[i].move(-1000, -1000)
            self.神话属性选项[i].currentIndexChanged.connect(lambda state, index = i:self.神话属性选项颜色更新(index))
        
        if self.初始属性.职业分类 == '输出':
            count = 0
            for i in 装备列表:
                if i.品质 == '神话':
                    描述列表 = [i.属性1描述, i.属性2描述, i.属性3描述, i.属性4描述]
                    范围列表 = [i.属性1范围, i.属性2范围, i.属性3范围, i.属性4范围]
                    for j in range(4):
                        if 描述列表[j] != '无':
                            for k in range(范围列表[j][0], 范围列表[j][1] - 1, -1):
                                if (k % 范围列表[j][2]) == 0 or k == 范围列表[j][0]:
                                    temp = 描述列表[j] + str(k)
                                    if 范围列表[j][2] == 1:
                                        temp += '%'
                                    self.神话属性选项[count * 4 + j].addItem(temp)
                        else:
                            self.神话属性选项[count * 4 + j].addItem('无')
                    count += 1            
        else:
            count = 0
            for i in 装备列表:
                if i.品质 == '神话':
                    描述列表 = [i.属性1描述_BUFF, i.属性2描述_BUFF, i.属性3描述_BUFF, i.属性4描述_BUFF]
                    范围列表 = [i.属性1范围_BUFF, i.属性2范围_BUFF, i.属性3范围_BUFF, i.属性4范围_BUFF]
                    for j in range(4):
                        if 描述列表[j] != '无':
                            for k in range(范围列表[j][0], 范围列表[j][1] - 1, -1):
                                if (k % 范围列表[j][2]) == 0 or k == 范围列表[j][0]:
                                    temp = 描述列表[j] + str(k)
                                    if 范围列表[j][2] == 1 and 'Lv' not in 描述列表[j]:
                                        temp += '%'
                                    self.神话属性选项[count * 4 + j].addItem(temp)
                        else:
                            self.神话属性选项[count * 4 + j].addItem('无')
                    count += 1
        pass

    def 界面5(self):
        pass

    def 界面6(self):
        pass

    def 基准值设置(self, x = 0):
        self.基准值.clear()
        if x == 0:
            装备 = []
            for i in self.自选装备:
                装备.append(i.currentText())
            A = deepcopy(self.初始属性)
            self.输入属性(A)
            A.穿戴装备计算套装(装备)
            B = deepcopy(A)
            self.排行窗口列表.clear()
            self.排行数据.clear()
            self.排行数据.append(装备 + [0] + A.套装栏 + ['无'])
            self.输出界面(0, '基准值')
            if A.职业分类 == '输出':
                self.基准值 = [A.伤害计算(0), B.伤害计算(1)]
            else:
                self.基准值 = [A.BUFF计算(0), B.BUFF计算(1)]
        self.自选计算(1)

    def 希洛克选择(self, index, x = 0):
        if x == 1:
            for i in range(15):
                self.希洛克遮罩透明度[i].setOpacity(0.5)
                self.希洛克选择状态[i] = 0
            return
        if index >= 100:
            序号 = int(index / 100 - 1)
            if self.初始属性.职业分类 == '输出':
            # 守门人全属强方案
                if 序号 == 3:
                    if self.角色属性A.职业 not in ('冰结师' , '鬼泣' , '死灵术士' , '气功师' , '忍者' , '暗枪士'):
                        number = self.希洛克选择状态[9] + self.希洛克选择状态[10] + self.希洛克选择状态[11]
                        if number != 3:
                            self.守门人属强.setCurrentIndex(3)
                            self.守门人全属强.setEnabled(True)
                            self.守门人全属强.setChecked(True)
                            self.守门人全属强.setStyleSheet(复选框样式)
                        else:
                            self.守门人全属强.setEnabled(False)
                            self.守门人全属强.setChecked(False)
                            self.守门人全属强.setStyleSheet(不可勾选复选框样式)
                else:
                    self.守门人全属强.setEnabled(False)
                    self.守门人全属强.setChecked(False)
                    self.守门人全属强.setStyleSheet(不可勾选复选框样式)
            count = 0
            for i in range(序号 * 3, 序号 * 3 + 3):
                count += self.希洛克选择状态[i]
            if count != 3:
                for i in range(15):
                    if i in range(序号 * 3, 序号 * 3 + 3):
                        self.希洛克遮罩透明度[i].setOpacity(0)
                        self.希洛克选择状态[i] = 1
                    else:
                        self.希洛克遮罩透明度[i].setOpacity(0.5)
                        self.希洛克选择状态[i] = 0
            else:
                for i in range(序号 * 3, 序号 * 3 + 3):
                    self.希洛克遮罩透明度[i].setOpacity(0.5)
                    self.希洛克选择状态[i] = 0
        else:
            if self.初始属性.职业分类 == '输出':
                if self.角色属性A.职业 not in ('冰结师' , '鬼泣' , '死灵术士' , '气功师' , '忍者' , '暗枪士'):
                    number = self.希洛克选择状态[9] + self.希洛克选择状态[10] + self.希洛克选择状态[11]
                    if number == 2 and self.希洛克选择状态[index] == 0 and index in [9,10,11]:
                        self.守门人属强.setCurrentIndex(3)
                        self.守门人全属强.setEnabled(True)
                        self.守门人全属强.setChecked(True)
                        self.守门人全属强.setStyleSheet(复选框样式)
                    else:
                        self.守门人全属强.setEnabled(False)
                        self.守门人全属强.setChecked(False)
                        self.守门人全属强.setStyleSheet(不可勾选复选框样式)
            if self.希洛克选择状态[index] == 0:
                for i in range(5):
                    序号 = i * 3 + index % 3
                    if self.希洛克选择状态[序号] == 1:
                        self.希洛克遮罩透明度[序号].setOpacity(0.5)
                        self.希洛克选择状态[序号] = 0
                self.希洛克遮罩透明度[index].setOpacity(0)
                self.希洛克选择状态[index] = 1
            else:
                self.希洛克遮罩透明度[index].setOpacity(0.5)
                self.希洛克选择状态[index] = 0

    def 存档更换(self):
        if self.存档位置 == self.存档选择.currentText():
            return
        box = QMessageBox(QMessageBox.Warning, "提示", "即将载入<font color='#FF0000'>{}</font>存档，是否保存当前配置到<font color='#FF0000'>{}</font>存档？".format(self.存档选择.currentText(), self.存档位置))
        box.setWindowIcon(self.icon)
        yes = box.addButton(self.tr("确定"), QMessageBox.YesRole)
        no = box.addButton(self.tr("取消"), QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton() == yes:
            self.保存配置(self.存档位置)
        self.存档位置 = self.存档选择.currentText()
        self.载入配置(self.存档位置)

    def 存档列表读取(self):
        self.存档位置 = 'set'
        path = './ResourceFiles/'+self.角色属性A.实际名称 + '/'
        setfile = []
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                if dir.startswith('set'):
                    setfile.append(dir)
        self.存档选择.clear()
        for k in setfile:
            self.存档选择.addItem(k)
        self.存档位置 = self.存档选择.currentText()

    def 全局重置(self):
        box = QMessageBox(QMessageBox.Warning, "提示", "是否恢复默认设置？")
        box.setWindowIcon(self.icon)
        yes = box.addButton(self.tr("确定"), QMessageBox.YesRole)
        no = box.addButton(self.tr("取消"), QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton() == yes:
            self.载入配置('reset')

    def 改造套装更改(self):
        self.计算标识 = 0
        名称列表 = []
        部位序号 = []
        for n in 装备列表:
            try:
                if n.关联套装 == self.改造套装.currentText():
                    名称列表.append(n.名称)
                    部位序号.append(部位字典[n.部位])
            except:
                pass
            try:
                if n.所属套装 == self.改造套装.currentText().split('[')[0]:
                    名称列表.append(n.名称)
                    部位序号.append(部位字典[n.部位])
            except:
                pass
        if self.改造套装.currentText() == '兵法之神[5]':
            for n in 装备列表:
                try:
                    if n.所属套装 in ['无相轮回的希望', '流逝轮回的记忆'] and n.部位 != '辅助装备':
                        名称列表.append(n.名称)
                        部位序号.append(部位字典[n.部位])
                except:
                    pass                 
        for n in 部位序号:
            x = -1
            for i in 装备列表:
                if 部位列表[n] == i.部位:
                    x += 1 
                    if i.名称 in 名称列表:
                        self.自选装备[n].setCurrentIndex(x)
        self.计算标识 = 1
        self.自选计算(1)

    def 神话部位更改(self):
        self.计算标识 = 0
        部位 = [-1, 0, 5, 8]
        序号 = 部位[self.神话部位选项.currentIndex()]
        if 序号 != -1:
            当前 = 装备列表[装备序号[self.自选装备[序号].currentText()]]
            x = -1
            for i in 装备列表:
                if 当前.部位 == i.部位:
                    x += 1 
                    if i.品质 == '神话' and i.所属套装 == 当前.所属套装:
                        self.自选装备[序号].setCurrentIndex(x)
        for k in [0, 5, 8]:
            if k != 序号:
                当前 = 装备列表[装备序号[self.自选装备[k].currentText()]]
                if 当前.品质 == '神话':
                    x = -1
                    for i in 装备列表:
                        if 当前.部位 == i.部位:
                            x += 1 
                            if i.品质 == '史诗' and i.所属套装 == 当前.所属套装:
                                self.自选装备[k].setCurrentIndex(x)
        self.计算标识 = 1
        self.自选计算(1)         
        
    def 自选装备更改(self, index = 0):
        try:
            self.图片列表[index] = self.装备图片[装备序号[self.自选装备[index].currentText()]]
            self.图片显示[index].setMovie(self.图片列表[index])
            self.图片列表[index].start()
        except:
            pass
        
        if self.初始属性.职业分类 == '输出':
            if self.当前页面 == 5 and self.计算标识 == 1:
                self.自选计算(1)
        else:     
            if self.当前页面 == 4 and self.计算标识 == 1:
                self.自选计算(1)

    def 自选套装更改(self, index):
        self.计算标识 = 0
        name = self.自选套装[index].currentText()
        for i in range(11):
            if self.装备锁定[i].isChecked():
                continue
            x = -1
            for j in 装备列表:
                if j.部位 == 部位列表[i]:
                    x += 1
                    try:
                        if j.所属套装2 == name:
                            self.自选装备[i].setCurrentIndex(x)
                            break
                    except:
                        if j.所属套装 == name and j.品质 != '神话':
                            self.自选装备[i].setCurrentIndex(x)
                            break
        self.计算标识 = 1
        self.自选计算(1)  

    def 辟邪玉数值选项更新(self, index):
        if self.初始属性.职业分类 == '输出':
            from PublicReference.equipment.辟邪玉 import 辟邪玉列表
        else:
            from PublicReference.equipment.辟邪玉_buff import 辟邪玉列表
        self.辟邪玉数值[index].clear()
        x = self.辟邪玉选择[index].currentIndex()
        temp = 辟邪玉列表[x].最大值 * 10
        while temp >= 辟邪玉列表[x].最小值 * 10:
            if 辟邪玉列表[x].间隔 == 1:
                self.辟邪玉数值[index].addItem(str(int(temp/10)))
            else:
                self.辟邪玉数值[index].addItem(str('%.1f' % (temp/10)) + '%')
            temp -= 辟邪玉列表[x].间隔 * 10

    def 辟邪玉属性计算(self, 属性):
        if self.初始属性.职业分类 == '输出':
            from PublicReference.equipment.辟邪玉 import 辟邪玉列表
        else:
            from PublicReference.equipment.辟邪玉_buff import 辟邪玉列表
        for i in range(4):
            x = self.辟邪玉选择[i].currentIndex()
            if self.辟邪玉数值[i].currentIndex() >= 0:
                辟邪玉列表[x].当前值 = float(self.辟邪玉数值[i].currentText().replace('%',''))
            辟邪玉列表[x].穿戴属性(属性)

    def 装备图标点击事件(self, index, sign, x = 1):
        if 装备列表[index].模式 == 0:
            try:
                #改变状态
                if sign == 10:
                    if self.装备选择状态[index] == 0:
                        self.遮罩透明度[index].setOpacity(0.0)
                        self.装备选择状态[index] = 1
                    else:
                        self.遮罩透明度[index].setOpacity(0.5)
                        self.装备选择状态[index] = 0
                #点亮
                if sign == 1:
                    self.遮罩透明度[index].setOpacity(0.0)
                    self.装备选择状态[index] = 1
                #熄灭
                if sign == 0:
                    self.遮罩透明度[index].setOpacity(0.5)
                    self.装备选择状态[index] = 0
                self.装备图片按钮[index].setGraphicsEffect(self.遮罩透明度[index])

                if x == 1:
                    self.计算模式选择.setItemText(0, '计算模式：极速模式  组合：' + self.组合数量计算(0))
                    self.计算模式选择.setItemText(1, '计算模式：套装模式  组合：' + self.组合数量计算(1))
                    self.计算模式选择.setItemText(2, '计算模式：单件模式  组合：' + self.组合数量计算(2))
            except Exception as error:
                pass

    def 套装按钮点击事件(self, index):
        count1 = 0
        count2 = 0
        for i in 装备列表:
            if i.所属套装 == index and index != '无' and i.部位 != '武器':
                count1 += self.装备选择状态[装备序号[i.名称]] 
            if i.类型 in self.角色属性A.武器选项 and index == '无':
                count2 += self.装备选择状态[装备序号[i.名称]]
        for i in 装备列表:
            if i.所属套装 == index and index != '无' and i.部位 != '武器':
                self.装备图标点击事件(装备序号[i.名称], 0 if count1 > 0 else 1)
            if i.类型 in self.角色属性A.武器选项 and index == '无':
                self.装备图标点击事件(装备序号[i.名称], 0 if count2 > 0 else 1)

    def 组合数量计算(self, sign, x = 0):
        if sign == 0 or sign == 1:
            self.有效武器列表.clear()
            for j in range(0, 6):
                self.有效总套装列表[j].clear()
            for i in range(0, len(self.装备选择状态)):
                if self.装备选择状态[i] == 1:
                    for j in range(0, 6):
                        if (装备列表[i].所属套装 in 总套装列表[j]) and (装备列表[i].所属套装 not in self.有效总套装列表[j]):
                            self.有效总套装列表[j].append(装备列表[i].所属套装)
                    if 装备列表[i].部位 == '武器':
                        self.有效武器列表.append(装备列表[i].名称)
            if sign == 0:
                counter = (len(self.有效防具套装)*len(self.有效首饰套装)*len(self.有效特殊套装)+len(self.有效防具套装)*len(self.有效上链左套装)*len(self.有效镯下右套装)*len(self.有效环鞋指套装)*4)*4*len(self.有效武器列表)
            if sign == 1:
                counter = (len(self.有效防具套装)*len(self.有效首饰套装)*len(self.有效特殊套装)+len(self.有效防具套装)*len(self.有效上链左套装)*len(self.有效镯下右套装)*len(self.有效环鞋指套装)*4+len(self.有效防具套装)*len(self.有效首饰套装)*len(self.有效特殊套装)*(len(self.有效防具套装)-1)*10)*4*len(self.有效武器列表)
    
        if sign == 2:
            self.有效部位列表.clear()
            for i in range(0, 12):
                self.有效部位列表.append([])
            for i in range(0, len(self.装备选择状态)):
                if self.装备选择状态[i] == 1:
                    self.有效部位列表[部位列表.index(装备列表[i].部位)].append(装备列表[i].名称)

            counter = 0
            for a1 in self.有效部位列表[0]:
                for a2 in self.有效部位列表[5]:
                    for a3 in self.有效部位列表[8]:
                        神话数量 = 0
                        for i in [a1, a2, a3]:
                            if 装备列表[装备序号[i]].品质 == '神话':
                                神话数量 += 1
                        if 神话数量 <= 1:
                            counter += 1
            for i in [1, 3, 2, 4, 6, 9, 7, 10, 11]:
                counter *= len(self.有效部位列表[i])

        if x == 0:
            if counter <= 9999 :
                return str(counter)
            else:
                num = -1
                while counter >= 10000:
                    counter /= 10000
                    num += 1
                name = ['万', '亿', '万亿']
                return str(round(counter, 2)) + name[num]
        if x == 1:
            return counter

    def 强化觉醒选择(self, index):
        self.觉醒选择状态=index
        if index==1:  
            self.一觉遮罩透明度.setOpacity(0.0)
            self.二觉遮罩透明度.setOpacity(0.5)
        if index==2:
            self.一觉遮罩透明度.setOpacity(0.5)
            self.二觉遮罩透明度.setOpacity(0.0)       
    
        self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
        self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)

    def 批量选择(self, index):
        if index == 1:
            if self.全选状态 == 1:
                self.全选状态 = 0
            else:
                self.全选状态 = 1
            if sum(self.装备选择状态[74:244]) == 170:
                self.批量选择(0)

        for i in 装备列表:
            if i.部位 != '武器':
                if i.品质 != '神话' or index == 0 or self.全选状态 == 0:
                    self.装备图标点击事件(装备序号[i.名称], index, x = 0)
            else:
                if i.类型 in self.角色属性A.武器选项:
                    self.装备图标点击事件(装备序号[i.名称], index, x = 0)

        self.装备图标点击事件(74, index)
    
    def 批量打造(self, x):
        for i in range(12):
            y = max(min(self.装备打造选项[i + 12].currentIndex() + x, 31), 0)
            self.装备打造选项[i + 12].setCurrentIndex(y)

    def 神话属性选项颜色更新(self, index):
        i = self.神话属性选项[index]
        if i.currentIndex() != 0:
            i.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(225,5,65,0.8)} QComboBox QAbstractItemView::item {height: 18px;}")
        else:
            i.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(65,105,225,0.8)} QComboBox QAbstractItemView::item {height: 18px;}")

    def 改造产物选项颜色更新(self, index):
        i = self.改造产物选项[index]
        if i.currentIndex() != 0:
            i.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(225,5,65,0.8)} QComboBox QAbstractItemView::item {height: 18px;}")
        else:
            i.setStyleSheet("QComboBox{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:5px;} QComboBox:hover{background-color:rgba(65,105,225,0.8)} QComboBox QAbstractItemView::item {height: 18px;}")

    def click_window(self, index):
        self.当前页面 = index
        if self.stacked_layout.currentIndex() != index:
            self.stacked_layout.setCurrentIndex(index)
        for i in self.window_btn:
            i.setStyleSheet('QToolButton{font-size:13px;color:white;background-color:rgba(70,130,200,0.8)} QToolButton:hover{background-color:rgba(40,100,235,0.8)}')
        self.window_btn[index].setStyleSheet('QToolButton{font-size:13px;color:white;background-color:rgba(200,30,30,0.8)} QToolButton:hover{background-color:rgba(235,0,0,0.8)}')

        if index == 3:
            count1 = 0
            count2 = 0
            num = 0
            自选装备名称 = []
            for i in self.自选装备:
                自选装备名称.append(i.currentText())
            for j in range(len(装备列表)):
                if 装备列表[j].品质 == '神话':
                    if self.装备选择状态[j] == 1 or 装备列表[j].名称 in 自选装备名称:
                        self.神话属性图片[num].move(int(self.width() / 7 * (count1 % 7+ 0.42)), int(self.height() / 5.2 * (count2 + 0.05)))
                        for i in range(4):
                            self.神话属性选项[num * 4 + i].move(int(self.width() / 7 * (count1 % 7) + 12), int(self.height() / 5.2 * (count2 + 0.05)) + i * 22 + 32)
                        count1 += 1
                        if count1 % 7 == 0:
                            count2 += 1
                    else:
                        self.神话属性图片[num].move(-1000,-1000)
                        for i in range(4):
                            self.神话属性选项[num * 4 + i].move(-1000,-1000)
                    num += 1
        if self.初始属性.职业分类 == '输出':
            if index ==4:
                self.智慧产物升级洗词条(1 if self.智慧产物升级.isChecked() else 0)
            if index == 5:
                self.自选计算(1)
        else:
            if index == 4:
                self.自选计算(1)
    
    def 智慧产物升级洗词条(self,x=0):
        count1 = 0
        count2 = 0
        num = 0
        for j in range(len(装备列表)):
            if 装备列表[j].所属套装 == '智慧产物' :
                if self.装备选择状态[j] == 1 and x==1:
                    self.改造产物图片[num].move(int(self.width() / 7 * (count1 % 5+ 0.42+2)), int(self.height() / 5.2 * (count2 + 0.05)))
                    for i in range(4):
                        self.改造产物选项[num * 4 + i].move(int(self.width() / 7 * (count1 % 5+2) + 12), int(self.height() / 5.2 * (count2 + 0.05)) + i * 22 + 32)
                    count1 += 1
                    if count1 % 5 == 0:
                        count2 += 1
                else:
                    self.改造产物图片[num].move(-1000,-1000)
                    for i in range(4):
                        self.改造产物选项[num * 4 + i].move(-1000,-1000)
                num += 1 

    def 修正套装计算(self, x):
        self.有效穿戴组合.clear()
        
        装备 = []
        if x == 0:
            for i in self.有效部位列表:
                装备.append(i[0])
        elif x == 1:
            for i in self.自选装备:
                装备.append(i.currentText())         

        self.有效穿戴组合.append(装备)

    def 神话数量判断(self, x = 0):
        count = 0
        for j in range(len(装备列表)):
            if 装备列表[j].品质 == '神话':
                if self.装备选择状态[j] == 1:
                    count += 1
        if x == 0:
            if count != 0:
                return False
            else:
                return True
        else:
            return count

    def 单件模式前四层组合(self):
        count = 0
        for a1 in self.有效部位列表[0]:
            for a2 in self.有效部位列表[5]:
                for a3 in self.有效部位列表[8]:
                    神话数量 = 0
                    for i in [a1, a2, a3]:
                        if 装备列表[装备序号[i]].品质 == '神话':
                            神话数量 += 1
                    if 神话数量 <= 1:
                        count += 1
        return count * len(self.有效部位列表[1])

    #计算
    def 计算(self):
        self.保存配置(self.存档位置)
        self.角色属性A = deepcopy(self.初始属性)
        self.输入属性(self.角色属性A)
        self.角色属性A.开启切装 = 切装模式
        if 调试开关 == 1:
            self.输出界面(-1)
            return
        if self.神话数量判断() and self.神话排名选项.isChecked():
            QMessageBox.information(self,"错误",  "请勾选神话装备或取消勾选神话排名模式选项") 
            return
        self.有效部位列表备份 = []
        if self.组合计算(self.计算模式选择.currentIndex()) == 0:
            if self.计算模式选择.currentIndex() == 2 and 补全模式 != 0:
                self.有效部位列表备份 = deepcopy(self.有效部位列表)
                num = 0
                for i in self.有效部位列表:
                    if len(i) == 0 or (补全模式 == 2 and self.自选装备[num].currentText() not in i):
                        i.append(self.自选装备[num].currentText())
                    num += 1
            elif self.计算模式选择.currentIndex() == 0 and self.组合计算(1) != 0:
                QMessageBox.information(self, "错误", "已更换为套装模式，请再次计算")
                self.计算模式选择.setCurrentIndex(1)
                return
            elif self.计算模式选择.currentIndex() != 2 and self.组合计算(2) != 0:
                QMessageBox.information(self, "错误", "请更换为单件模式，并再次计算")
                return
            else:
                QMessageBox.information(self,"错误",  "无有效组合，请重新选择装备")
                return
        self.计算按钮1.setEnabled(False)
        self.计算按钮1.setStyleSheet(不可点击按钮样式)
        self.计算按钮2.setEnabled(False)
        self.计算按钮2.setStyleSheet(不可点击按钮样式)
        self.计算按钮3.setEnabled(False)
        self.计算按钮3.setStyleSheet(不可点击按钮样式)
        threading.Thread(target=self.计算线程, daemon=True).start()


    def 计算线程(self):
        logger.info("开始计算")
        self.角色属性A = deepcopy(self.初始属性)
        self.输入属性(self.角色属性A)

        self.最大使用线程数 = thread_num - self.线程数选择.currentIndex()
        # -------------------------------------多线程计算流程开始-------------------------------------

        startTime = time.time()
        finished = False
        producer_data.calc_index += 1
        producer_data.produced_count = 0

        def log_result_queue_info(log_func, msg, mq: MinHeapWithQueue):
            log_func("calc#{}: {}: {} remaining_qize={} sync_batch_size={} processed_result={}, speed={:.2f}/s totalWork={}".format(
                producer_data.calc_index,
                mq.name, msg, mq.minheap_queue.qsize(), mq.minheap.batch_size, mq.minheap.processed_result_count, mq.process_results_per_second(), producer_data.produced_count
           ))
            self.update_remaining_signal.emit(str(mq.minheap.processed_result_count))

        def try_fetch_result(mq: MinHeapWithQueue):
            idx = 1
            while True:
                try:
                    minheap_to_merge = mq.minheap_queue.get(block=False)
                    mq.minheap.merge(minheap_to_merge)

                    if mq.minheap.processed_result_count >= 1000 * idx:
                        log_result_queue_info(logger.info, "try_fetch_result periodly report", mq)
                        idx = mq.minheap.processed_result_count // 1000 + 1
                except queue.Empty as error:
                    break

        def try_fetch_result_in_background(mq: MinHeapWithQueue):
            while not finished:
                log_result_queue_info(logger.info, "try_fetch_result_in_background", mq)
                try_fetch_result(mq)
                time.sleep(0.5)

        save_top_n = 2 << 64

        mq = MinHeapWithQueue("排行", MinHeap(save_top_n, batch_size), multiprocessing.Manager().Queue())

        # 异步排行线程
        fetch_result_thread = threading.Thread(target=try_fetch_result_in_background, args=(mq,), daemon=True)
        fetch_result_thread.start()

        # 异步计算搭配
        mode_index = self.计算模式选择.currentIndex()
        total_task_count = self.组合计算(self.计算模式选择.currentIndex()) # 极速模式和套装模式时
        if mode_index == 2:
            # 散件模式时
            total_task_count = self.单件模式前四层组合()

        batch_task_count = min(thread_task * thread_num, total_task_count, self.最大使用线程数)

        start_index, end_index = 0, 0
        task_batch_size = total_task_count // batch_task_count
        reminder = total_task_count % batch_task_count
        for i in range(batch_task_count):
            end_index = start_index + task_batch_size - 1
            if i < reminder:
                end_index+=1

            calc_data = CalcData()

            if self.角色属性A.职业分类 == "BUFF":
                calc_data.是输出职业 = False
                calc_data.minheap_queue = mq.minheap_queue
                calc_data.角色属性A = deepcopy(self.角色属性A)
                calc_data.角色属性A.强化等级 = copy(self.角色属性A.强化等级)
                calc_data.角色属性A.改造等级 = copy(self.角色属性A.改造等级)
                calc_data.角色属性A.是否增幅 = copy(self.角色属性A.是否增幅)
                calc_data.角色属性A.次数输入 = copy(self.角色属性A.次数输入)
            else:
                calc_data.是输出职业 = True
                calc_data.智慧产物限制 = self.智慧产物限制.currentIndex() + 1
                calc_data.minheap_queue = mq.minheap_queue
                calc_data.角色属性A = deepcopy(self.角色属性A)
                calc_data.角色属性A.装备切装 = copy(self.角色属性A.装备切装)
                calc_data.角色属性A.技能切装 = copy(self.角色属性A.技能切装)
                calc_data.角色属性A.切装修正 = copy(self.角色属性A.切装修正)
                calc_data.角色属性A.宠物次数 = copy(self.角色属性A.宠物次数)
                calc_data.角色属性A.强化等级 = copy(self.角色属性A.强化等级)
                calc_data.角色属性A.改造等级 = copy(self.角色属性A.改造等级)
                calc_data.角色属性A.是否增幅 = copy(self.角色属性A.是否增幅)
                calc_data.角色属性A.次数输入 = copy(self.角色属性A.次数输入)                
            
            calc_data.mode_index = mode_index
            calc_data.start_index = start_index
            calc_data.end_index = end_index

            calc_data.装备选择状态 = copy(self.装备选择状态)
            for i in self.有效部位列表:
                for j in i:
                    calc_data.装备选择状态[装备序号[j]] = 1
            if len(self.有效部位列表备份) != 0:
                self.有效部位列表 = deepcopy(self.有效部位列表备份)
            calc_data.拥有百变怪 = self.百变怪选项.isChecked()
            calc_data.神话属性选项 = [cb.currentIndex() for cb in self.神话属性选项]
            if self.初始属性.职业分类 == '输出':
                calc_data.改造产物选项 = [cb.currentIndex() for cb in self.改造产物选项]

            calc_data.minheap = MinHeap(save_top_n, batch_size)

            producer(calc_data)

            start_index = end_index + 1

        # 等到所有工作处理完成
        producer_data.work_queue.join()
        finished = True

        logger.warning("所有工作线程均已完成计算，总计用时={}".format(format_time(time.time() - startTime)))

        # 等待异步排行线程退出
        fetch_result_thread.join()

        # 最终将剩余结果（若有）也加入排序
        log_result_queue_info(logger.info, "after join", mq)
        try_fetch_result(mq)
        log_result_queue_info(logger.info, "after final", mq)

        # -------------------------------------多线程计算流程结束-------------------------------------

        self.排行数据.clear()
        self.伤害列表 = mq.minheap.getTop()
        for i in range(len(self.伤害列表)):
            self.排行数据.append(self.伤害列表[i][1:])

        totoalCostTime = time.time() - startTime
    #     logger.info((
    #         "计算完毕\n"
    #         "工作线程={} 总计耗时={}"
    #    ).format(
    #         thread_num, format_time(totoalCostTime),
    #    ))

        self.calc_done_signal.emit()

    def 数量显示(self, counter):
        if counter <= 9999 :
            return str(counter)
        else:
            counter /= 10000
            return ('%.2f' % counter) + '万'

    def update_remaining(self, count):
        temp = self.数量显示(int(count))
        self.计算按钮1.setText("完成:" + temp)
        self.计算按钮2.setText("完成:" + temp)
        self.计算按钮3.setText("完成:" + temp)

    def calc_done(self):
        self.计算按钮1.setText("开始计算")
        self.计算按钮1.setEnabled(True)
        self.计算按钮1.setStyleSheet(按钮样式)
        self.计算按钮2.setText("开始计算")
        self.计算按钮2.setEnabled(True)
        self.计算按钮2.setStyleSheet(按钮样式)
        self.计算按钮3.setText("开始计算")
        self.计算按钮3.setEnabled(True)
        self.计算按钮3.setStyleSheet(按钮样式)
        if len(self.排行数据) == 0:
            QMessageBox.information(self,"计算错误",  "无有效组合")
            return
        if len(self.排行数据) == 1:
            self.输出界面(0)
        else:
            self.排行窗口列表.clear()
            if self.装备限定判断():
                self.其他限定判断()
    
    def 单条排行数据判断(self, s, l):
        for i in l:
            if s[i] != self.自选装备[i].currentText():
                return 0
        return 1

    def 其他限定判断(self):
        if self.神话排名选项.isChecked():
            神话列表 = []
            对应序号 = []
            for i in range(len(self.排行数据)):
                tempstr = self.排行数据[i]
                for j in [0,5,8]:
                    if 装备列表[装备序号[tempstr[j]]].品质=='神话' and tempstr[j] not in 神话列表:
                        神话列表.append(tempstr[j])
                        对应序号.append(i)
                if len(神话列表) >= self.神话数量判断(1):
                    break
            if len(对应序号) == 0:
                QMessageBox.information(self,"计算错误",  "请取消勾选神话排名模式或重新勾选装备")
                return 
            self.排行界面({}, 对应序号)         
        elif 武器排名 == 1:
            武器列表 = []
            对应序号 = []
            for i in range(len(self.排行数据)):
                tempstr = self.排行数据[i]
                if 装备列表[装备序号[tempstr[11]]].部位=='武器' and tempstr[11] not in 武器列表:
                    武器列表.append(tempstr[11])
                    对应序号.append(i)
                if len(武器列表) >= len(self.有效武器列表):
                    break
            self.排行界面({}, 对应序号)                       
        else:
            self.排行界面()

    def 装备限定判断(self):
        temp = []
        l = []
        for i in range(12):
            if self.装备锁定[i].isChecked():
                l.append(i)
        if len(l) == 0:
            return 1
        for s in self.排行数据:
            if self.单条排行数据判断(s, l):
                temp.append(s)
        if len(temp) == 0:
            QMessageBox.information(self,"计算错误",  "无符合条件组合，请解除第五页装备限定或重新勾选")
            return 0
        self.排行数据 = copy(temp)
        return 1

    def 指定装备排序(self, dic, x, n):
        dic[x] = n
        temp = []
        num = -1
        for i in self.排行数据:
            num += 1
            sign = 1
            for n in dic.keys():
                if dic[n] != i[n]:
                    sign = 0
                    break
            if sign == 1:
                temp.append(num)
            if len(temp) == 100:
                break
        self.排行界面(dic, temp)

    def 排行界面(self, 筛选 = {}, 显示序号 = [x for x in range(100)]):
        显示序号 = 显示序号[:min(100, len(self.排行数据))]
        滚动排行 = QMainWindow()
        滚动排行.setStyleSheet('''QToolTip { 
           background-color: black; 
           color: white; 
           border: 0px
           }''')
        self.排行窗口列表.append(滚动排行)
        滚动排行.resize(630,530)
        滚动排行.setMinimumSize(630,530)
        滚动排行.setMaximumSize(630,1230)
        if len(筛选) == 0:
            # 滚动排行.setWindowTitle('当前模板配装排行（点击数字查看详情）'+"装备版本："+self.角色属性A.版本 + " 增幅版本：" + self.角色属性A.增幅版本)  
            滚动排行.setWindowTitle('当前模板配装排行（点击数字查看详情）')  
        else:
            temp = ''
            for name in 筛选.values():
                temp += name + ' | '
            滚动排行.setWindowTitle(temp[:-3])  
        滚动排行.setWindowIcon(self.icon)  
    
        背景颜色=QLabel(滚动排行)
        背景颜色.resize(630,1230)
        背景颜色.setStyleSheet("QLabel{background-color:rgba(50,50,50,1.0)}")
    
        排行背景透明度=QGraphicsOpacityEffect()
        排行背景透明度.setOpacity(0.15)
        排行背景=QLabel(滚动排行)
        排行背景.resize(630,1230)
        排行背景.setPixmap(self.主背景图片)
        排行背景.setAlignment(Qt.AlignCenter)
        排行背景.setGraphicsEffect(排行背景透明度)
    
        wrapper = QWidget()
        滚动排行.setCentralWidget(wrapper)
        滚动排行.topFiller = QWidget()
        滚动排行.topFiller.setMinimumSize(570, 50 * len(显示序号) + 30)
    
        if len(显示序号) > 10:
            初始x = -10
        else:
            初始x = 0
        初始y = 15
        x间隔 = 30
        y间隔 = 50
    
        最高伤害 = self.排行数据[显示序号[0]][12]
        尾部字符 = '%'
        if 最高伤害 > 100000000:
            最高伤害 /= 100000000
            尾部字符 = ''

        技能选项 = []
        for i in (self.细节选项输入[2] if self.角色属性A.职业分类 == '输出' else self.技能设置输入):
            技能选项.append(i.currentText().replace('Lv+1', ''))

        if 输出数据 == 1 and len(筛选) == 0:
            setfile = open('./数据记录/{}-{}.csv'.format(self.角色属性A.实际名称, time.strftime('%Y-%m-%d-%H-%M-%S')), 'w', encoding='gbk')
            for i in range(len(显示序号)):
                temp = ''
                for j in range(13):
                    temp += str(self.排行数据[显示序号[i]][j]) + ','
                temp += self.角色属性A.实际名称 + ','
                temp += 装备列表[装备序号[self.排行数据[显示序号[i]][11]]].类型
                setfile.write(temp + '\n')        
        
        for i in range(len(显示序号)):
            图片列表 = []
            for j in range(0,12):
                图片列表.append(self.装备图片[装备序号[self.排行数据[显示序号[i]][j]]])
            水平间距=[1,2,3,4,5,6.5,7.5,8.5,10,11,12,13.5]
            for j in range(0,12):
                装备 = 装备列表[装备序号[self.排行数据[显示序号[i]][j]]]
                图标 = QLabel(滚动排行.topFiller)
                图标.setMovie(图片列表[j])
                图片列表[j].start()
                图标.move(int(初始x+x间隔*水平间距[j]),int(初始y+i*y间隔))
                if self.排行数据[显示序号[i]][j] == self.排行数据[显示序号[i]][-1]:
                    图标=QLabel(滚动排行.topFiller)
                    图标.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                    图标.resize(28,28)
                    图标.move(int(初始x+x间隔*水平间距[j]),int(初始y+i*y间隔))
                
                按钮 = QPushButton(滚动排行.topFiller)
                按钮.move(int(初始x+x间隔*水平间距[j]),int(初始y+i*y间隔))
                按钮.resize(28,28)
                按钮.setToolTip(self.单件描述(装备))
                a = QGraphicsOpacityEffect()
                a.setOpacity(0.0)
                按钮.setGraphicsEffect(a)
                按钮.clicked.connect(lambda state, dic = deepcopy(筛选), x = j, n = 装备.名称: self.指定装备排序(dic, x, n))

            伤害数值 = self.排行数据[显示序号[i]][12]

            if 伤害数值 > 100000000:
                伤害数值 /= 100000000

            伤害量 = str(int(round(伤害数值,0)))

            if 最高伤害!=0:
                百分比=str(round(伤害数值/最高伤害*100,1)) + '%'
            else:
                百分比=' 0.0%'
    
            if 百分比=='100.0%':
                详情按钮=QtWidgets.QPushButton(伤害量+尾部字符+' |'+百分比,滚动排行.topFiller)
            else:
                详情按钮=QtWidgets.QPushButton(伤害量+尾部字符+' | '+百分比,滚动排行.topFiller)
    
            详情按钮.clicked.connect(lambda state, index= 显示序号[i]: self.输出界面(index))
            
            详情按钮.move(int(初始x+x间隔*15),int(初始y+i*y间隔))
            详情按钮.resize(120,30)
            temp = deepcopy(self.角色属性A)
            技能等级溢出 = temp.等级溢出判断(self.排行数据[显示序号[i]][0:12], self.排行数据[显示序号[i]][13:(len(self.排行数据[显示序号[i]]) - 1)])
            if  len(技能等级溢出) != 0:
                可调整技能 = ''
                不可调整技能 = ''
                for n in 技能等级溢出:
                    if n in 技能选项:
                        可调整技能 += n + ' '
                    else:
                        不可调整技能 += n + ' '
                if 可调整技能 != '':
                    详情按钮.setToolTip('<font size="3" face="宋体"><font color="#FF6666">' + 可调整技能 + 不可调整技能 + '</font>等级溢出，修改白金徽章或时装可以提高伤害。</font>')
                    详情按钮.setStyleSheet('QPushButton{font-size:14px;color:white;background-color:rgba(197,34,70,0.8);border:1px;border-radius:10px} QPushButton:hover{background-color:rgba(225,5,65,0.8)}')
                else:
                    详情按钮.setStyleSheet(按钮样式+"QPushButton{font-size:14px}")
                    详情按钮.setToolTip('<font size="3" face="宋体"><font color="#FF6666">' + 不可调整技能 + '</font>等级溢出</font>')
            else:
                详情按钮.setStyleSheet(按钮样式+"QPushButton{font-size:14px}")
                详情按钮.setToolTip('<font size="3" face="宋体">点击查看详情</font>')
        滚动排行.scroll = QScrollArea()
        滚动排行.scroll.setStyleSheet("QScrollArea {background-color:transparent}")
        滚动排行.scroll.viewport().setStyleSheet("background-color:transparent")
        滚动排行.scroll.setWidget(滚动排行.topFiller)
        滚动排行.vbox = QVBoxLayout()
        滚动排行.vbox.addWidget(滚动排行.scroll)
        wrapper.setLayout(滚动排行.vbox)
    
        滚动排行.show()


    def 组合计算(self, index):
        套装组合=[]
        if index <= 1:
            for a in self.有效防具套装:
                for b in self.有效首饰套装:
                    for c in self.有效特殊套装:
                        # 533
                        套装组合.append([a, a, a, a, a, b, b, b, c, c, c])
            for a in self.有效防具套装:
                for d in self.有效上链左套装:
                    for e in self.有效镯下右套装:
                        for f in self.有效环鞋指套装:
                            # 3332
                            套装组合.append([d, a, e, a, f, e, d, f, f, d, e])
                            套装组合.append([a, a, e, a, f, e, d, f, f, d, e])
                            套装组合.append([d, a, a, a, f, e, d, f, f, d, e])
                            套装组合.append([d, a, e, a, a, e, d, f, f, d, e])
        if index == 1:
            for a in self.有效防具套装:
                for b in self.有效首饰套装:
                    for c in self.有效特殊套装:
                        for d in self.有效防具套装:
                            if d != a:
                                # 2333
                                套装组合.append([a, a, a, d, d, b, b, b, c, c, c])
                                套装组合.append([a, a, d, a, d, b, b, b, c, c, c])
                                套装组合.append([a, d, a, a, d, b, b, b, c, c, c])
                                套装组合.append([d, a, a, a, d, b, b, b, c, c, c])
                                套装组合.append([a, a, d, d, a, b, b, b, c, c, c])
                                套装组合.append([a, d, a, d, a, b, b, b, c, c, c])
                                套装组合.append([d, a, a, d, a, b, b, b, c, c, c])
                                套装组合.append([a, d, d, a, a, b, b, b, c, c, c])
                                套装组合.append([d, a, d, a, a, b, b, b, c, c, c])
                                套装组合.append([d, d, a, a, a, b, b, b, c, c, c])
        count = 0
        if self.百变怪选项.isChecked():
            初始sign2 = '空'
        else:
            初始sign2 = '无'
        if index != 2:
            for temp in 套装组合:
                for k in [-1, 0, 5, 8]:
                    temp1 = []
                    sign = 0
                    sign2 = 初始sign2
                    for x in range(0,11):
                        品质 = '-史诗-'
                        if k == x:
                            品质= '-神话-'
                        index = 套装映射[temp[x] + 品质 + 部位列表[x]]
                        if self.装备选择状态[index] == 1:
                            sign += 1
                        else:
                            if sign2 == '空' and 装备列表[index].品质 != '神话' and 装备列表[index].所属套装 not in ['精灵使的权能', '大自然的呼吸', '能量主宰']:
                                sign += 1
                    if sign == 11:
                        count += len(self.有效武器列表)  
        if index == 2:
            count = 1     
            for i in self.有效部位列表:
                count *= len(i)                       
        return count
