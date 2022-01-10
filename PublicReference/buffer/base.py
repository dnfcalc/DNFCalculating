from ctypes import *

from .panel import *
from .property import *
from PublicReference.choise.选项设置_buff import *
from PublicReference.common import *
from PublicReference.utils.common import *
from PublicReference.view.DialogRegister import DefaultDialogRegister
from PublicReference.equipment.冒险家名望 import *


class 角色窗口(窗口):
    def __init__(self):
        self.初始属性: 辅助角色属性 = None
        self.护石选项 = [
            '无', 'BUFF力量、智力+2%', 'BUFF力量、智力+4%', 'BUFF力量、智力+6%', 'BUFF力量、智力+8%'
        ]
        self.登记启用 = False
        super().__init__()

        store.bind(self, "登记启用", "/{type}/data/register_enable")

    def 称号描述(self):
        temp = '<font size="3" face="宋体">'
        temp += '<font color="#78FF1E">' + trans(
            self.称号.currentData()) + '</font><br>'
        temp += 称号列表[self.称号.currentIndex()].装备描述_BUFF(self.角色属性B)[:-4]
        temp += '</font>'
        return temp

    def 宠物描述(self):
        temp = '<font size="3" face="宋体">'
        temp += '<font color="#78FF1E">' + self.宠物.currentData(
        ) + '</font><br>'
        temp += 宠物列表[self.宠物.currentIndex()].装备描述_BUFF(self.角色属性B)[:-4]
        temp += '</font>'
        return temp

    def 界面(self):
        self.setFixedSize(1120, 680)
        self.窗口高度 = 680
        self.行高 = 30
        self.输出背景图片 = QPixmap(trans("./ResourceFiles/img/输出背景_BUFF.png"))
        super().界面()

    def 界面1(self):
        super().界面1()
        # increase_counter(ga_category="buffer界面", name="装备/选择/打造")

        for i in 称号列表:
            self.称号.addItem(trans(i.显示名称), i.名称)

        for i in 宠物列表:
            self.宠物.addItem(trans(i.显示名称), i.名称)

        标签 = QLabel(self.main_frame1)
        人物 = QPixmap('./ResourceFiles/' + self.角色属性A.实际名称 + "/职业.png")
        标签.setPixmap(人物)
        标签.resize(191, 523)
        标签.move(922 + int((191 - 人物.width()) / 2), 10)

        self.百变怪选项 = QCheckBox(trans('百变怪'), self.main_frame1)
        self.百变怪选项.move(660, 613)
        self.百变怪选项.resize(80, 24)
        self.百变怪选项.setToolTip(
            '<font size="3" face="宋体">{}</font>'.format('仅在极速模式和套装模式下生效'))
        self.百变怪选项.setStyleSheet(复选框样式)

        self.计算模式选择 = MyQComboBox(self.main_frame1)
        self.计算模式选择.addItems(['计算模式:极速模式', '计算模式:套装模式', '计算模式:单件模式'])
        self.计算模式选择.move(750, 613)
        self.计算模式选择.resize(235, 24)
        self.计算模式选择.setStyleSheet(下拉框样式)
        self.计算模式选择.setToolTip('<font size="3" face="宋体">{}</font>'.format(
            trans(
                '极速模式:533和3332(散搭) (不含智慧产物)<br><br>套装模式:533、3332(散搭)和3233(双防具) (不含智慧产物)<br><br>单件模式:所有组合 (不含百变怪)'
            )))

        self.切装模式选项 = QCheckBox(trans('一觉切1件装备'), self.main_frame1)
        self.切装模式选项.move(875, 580)
        self.切装模式选项.resize(105, 24)
        self.切装模式选项.setToolTip('<font size="3" face="宋体">{}</font>'.format(
            trans('仅对极速/套装模式中的3332散搭组合生效<br><br>默认相同打造')))
        self.切装模式选项.setStyleSheet(复选框样式)

        self.神话排名选项 = QCheckBox(trans('神话排名模式'), self.main_frame1)
        self.神话排名选项.move(990, 580)
        self.神话排名选项.resize(100, 24)
        self.神话排名选项.setToolTip('<font size="3" face="宋体">{}</font>'.format(
            trans('仅显示有神话的组合，且每件神话装备只会出现一次')))
        self.神话排名选项.setStyleSheet(复选框样式)

        self.最大使用线程数 = thread_num
        self.线程数选择 = MyQComboBox(self.main_frame1)
        self.线程数选择.move(660, 580)
        self.线程数选择.resize(80, 24)
        for i in range(thread_num, 0, -1):
            self.线程数选择.addItem(trans('进程:') + str(i))
        if thread_num > 1:
            self.线程数选择.setCurrentIndex(1)

        self.禁用存档 = QCheckBox(trans('禁用自动存档'), self.main_frame1)
        self.禁用存档.move(990, 545)
        self.禁用存档.resize(100, 24)
        self.禁用存档.setStyleSheet(复选框样式)

        重置按钮 = QPushButton(trans('全局重置'), self.main_frame1)
        重置按钮.clicked.connect(lambda state: self.全局重置())
        重置按钮.move(880, 545)
        重置按钮.resize(100, 24)
        重置按钮.setStyleSheet(按钮样式)

        self.排行参数 = MyQComboBox(self.main_frame1)
        self.排行参数.addItems(['提升率排行', '面板排行', '力智排行', '三攻排行'])
        self.排行参数.move(770, 545)
        self.排行参数.resize(100, 24)

        self.存档选择 = MyQComboBox(self.main_frame1)
        self.存档选择.move(660, 545)
        self.存档选择.resize(90, 24)
        self.存档选择.currentIndexChanged.connect(lambda state: self.存档更换())

        # 一键修正按钮添加
        self.一键站街设置输入.append(QLineEdit(self.main_frame1))
        self.一键站街设置输入[0].setAlignment(Qt.AlignCenter)
        self.一键站街设置输入[0].setStyleSheet(输入框样式)
        self.一键站街设置输入[0].resize(45, 24)
        self.一键站街设置输入[0].move(750, 580)

        self.一键修正按钮 = QPushButton(trans('一键修正'), self.main_frame1)
        self.一键修正按钮.clicked.connect(lambda state: self.一键修正())
        self.一键修正按钮.move(800, 580)
        self.一键修正按钮.resize(70, 24)
        self.一键修正按钮.setStyleSheet(按钮样式)

        增幅选项 = []
        for i in range(12):
            combo = self.装备打造选项[i + 12]
            combo.currentIndexChanged.connect(
                lambda: store.emit("/{type}/data/amplifies"))
            增幅选项.append(combo)
        store.compute("/{type}/data/amplifies",
                      lambda: [i.currentIndex() for i in 增幅选项], None)

    def 界面2(self):
        # increase_counter(ga_category="buffer界面", name="技能/符文/其它")
        # 第二个布局界面
        self.main_frame2 = QWidget()

        # 技能等级、次数输入

        self.护石第一栏 = MyQComboBox(self.main_frame2)
        self.护石第二栏 = MyQComboBox(self.main_frame2)
        self.护石第三栏 = MyQComboBox(self.main_frame2)

        self.等级调整 = []
        self.次数输入 = []

        num = 0
        for skill in self.角色属性A.技能表.values():
            level_combo = MyQComboBox(self.main_frame2)
            enable_combo = MyQComboBox(self.main_frame2)

            level_min = 0 if skill.所在等级 == 50 or skill.所在等级 == 85 else -skill.基础等级
            level_max = skill.等级上限 - skill.基础等级 + 1

            for j in range(level_min, level_max):
                level_combo.addItem(str(j))
            for j in range(2):
                enable_combo.addItem(str(j))
            enable_combo.activated.connect(
                lambda state, index=num: self.BUFF次数输入填写(index))
            self.等级调整.append(level_combo)
            self.次数输入.append(enable_combo)
            num += 1
        横坐标 = 30
        纵坐标 = 0
        横坐标偏移量 = 60
        纵坐标偏移量 = 30
        词条框宽度 = 48
        行高 = 20

        counter = 0
        for i in trans(['契约满级', '等级调整', '是否适用']):
            x = QLabel(i, self.main_frame2)
            x.move(横坐标 + 横坐标偏移量 - 30 + 50 * counter, 纵坐标 + 5)
            x.setStyleSheet(标签样式)
            counter += 1

        纵坐标 += 20

        num = 0
        for skill in self.角色属性A.技能表.values():
            x = QLabel(self.main_frame2)
            x.setPixmap(self.技能图片[num])
            x.resize(28, 28)
            tempstr = '<font size="3" face="宋体"><font color="#FF6666">' + \
                      skill.名称 + skill.备注 + '</font><br>'
            tempstr += '所在等级:' + str(skill.所在等级) + '<br>'
            tempstr += '等级上限:' + str(skill.等级上限) + '</font>'
            x.setToolTip(tempstr)
            x.move(横坐标, 纵坐标 + 7)
            横坐标 += 40
            x = QLabel('Lv' + str(skill.基础等级), self.main_frame2)
            x.resize(40, 28)
            x.move(横坐标, 纵坐标 + 7)
            x.setStyleSheet(标签样式)
            横坐标 += 40
            self.等级调整[num].resize(词条框宽度, 行高)
            self.等级调整[num].move(横坐标, 纵坐标 + 10)
            横坐标 -= 80
            纵坐标 += 纵坐标偏移量
            num += 1

        横坐标 = 横坐标 + 80 + 50
        纵坐标 = 30

        for i in range(len(self.角色属性A.技能表)):
            self.次数输入[i].resize(词条框宽度, 行高)
            self.次数输入[i].move(横坐标, 纵坐标)
            纵坐标 += 纵坐标偏移量

        self.护石第一栏.addItems(self.护石选项)
        self.护石第二栏.addItems(self.护石选项)
        self.护石第三栏.addItems(self.护石选项)
        self.护石栏 = [self.护石第一栏, self.护石第二栏, self.护石第三栏]

        横坐标 = 395
        纵坐标 = 20
        行高 = 18
        x = QLabel(trans("护石") + "Ⅰ", self.main_frame2)
        x.move(横坐标, 纵坐标)
        x.setStyleSheet(标签样式)
        纵坐标 += 21
        self.护石第一栏.move(横坐标, 纵坐标)
        self.护石第一栏.resize(130, 行高)

        横坐标 = 565
        纵坐标 = 20
        x = QLabel(trans("护石") + "Ⅱ", self.main_frame2)
        x.move(横坐标, 纵坐标)
        x.setStyleSheet(标签样式)
        纵坐标 += 21
        self.护石第二栏.move(横坐标, 纵坐标)
        self.护石第二栏.resize(130, 行高)

        横坐标 = 395
        纵坐标 = 70
        行高 = 18
        x = QLabel(trans("护石") + "Ⅲ", self.main_frame2)
        x.move(横坐标, 纵坐标)
        x.setStyleSheet(标签样式)
        纵坐标 += 21
        self.护石第三栏.move(横坐标, 纵坐标)
        self.护石第三栏.resize(130, 行高)

        self.辟邪玉选择 = []
        self.辟邪玉数值 = []
        x = QLabel(trans("辟邪玉选择"), self.main_frame2)
        x.move(395, 115 + 5)
        x.setStyleSheet(标签样式)
        for i in range(4):
            x = MyQComboBox(self.main_frame2)
            for j in 辟邪玉列表:
                # '[' + str(j.编号) + ']' +
                x.addItem(j.名称)
            x.resize(200, 20)
            x.move(395, 140 + i * 25)
            x.currentIndexChanged.connect(
                lambda state, index=i: self.辟邪玉数值选项更新(index))
            self.辟邪玉选择.append(x)
            y = MyQComboBox(self.main_frame2)
            y.resize(80, 20)
            y.move(615, 140 + i * 25)
            self.辟邪玉数值.append(y)

        self.复选框列表 = []
        for i in 选项设置列表:
            self.复选框列表.append(QCheckBox(trans(i.名称), self.main_frame2))

        横坐标 = 395
        纵坐标 = 240

        x = QLabel(trans("武器融合:"), self.main_frame2)
        x.move(横坐标, 纵坐标 + 5)
        x.resize(300, 20)
        x.setStyleSheet(标签样式)

        self.希洛克武器选择 = MyQComboBox(self.main_frame2)
        self.希洛克武器选择.addItems(['武器词条:无', '自适应最高值', '自选词条数值'])
        self.希洛克武器选择.resize(120, 20)
        self.希洛克武器选择.move(横坐标 + 60, 纵坐标 + 5)
        self.希洛克武器选择.currentIndexChanged.connect(
            lambda state: self.希洛克武器选择更新())
        纵坐标 += 10
        self.武器融合属性A = MyQComboBox(self.main_frame2)
        for j in 武器属性A列表:
            self.武器融合属性A.addItem(j.固定属性描述)
        self.武器融合属性A.resize(60, 20)
        self.武器融合属性A.move(横坐标, 纵坐标 + 25)

        self.武器融合属性A1 = MyQComboBox(self.main_frame2)
        self.武器融合属性A1.resize(90 + 75, 20)
        self.武器融合属性A1.move(横坐标 + 110 - 50 + 5, 纵坐标 + 25)

        self.武器融合属性A2 = MyQComboBox(self.main_frame2)
        self.武器融合属性A2.resize(50, 20)
        self.武器融合属性A2.move(横坐标 + 205 + 20 + 10, 纵坐标 + 25)
        self.武器融合属性A.currentIndexChanged.connect(
            lambda: self.希洛克武器随机词条更新(self.武器融合属性A.currentIndex()))

        x = QLabel(trans("择优方向"), self.main_frame2)
        x.move(横坐标 + 335, 纵坐标 + 15)
        x.resize(300, 20)
        x.setStyleSheet(标签样式)

        self.觉醒择优方向 = MyQComboBox(self.main_frame2)
        self.觉醒择优方向.addItem('自选觉醒择优系数')
        self.觉醒择优方向.addItem('续航向:觉醒0.7系数')
        self.觉醒择优方向.addItem('爆发向:觉醒1.0系数')
        self.觉醒择优方向.resize(138, 20)
        self.觉醒择优方向.move(横坐标 + 300, 纵坐标 + 40)
        self.觉醒择优方向.currentIndexChanged.connect(
            lambda index: self.调整觉醒择优方向(index))

        self.觉醒择优系数 = MyQComboBox(self.main_frame2)
        self.觉醒择优系数.resize(138, 20)
        self.觉醒择优系数.move(横坐标 + 440, 纵坐标 + 40)
        for i in range(21):
            self.觉醒择优系数.addItem(str(round(i / 10, 1)))
        self.觉醒择优系数.setCurrentIndex(10)

        纵坐标 = 纵坐标 + 30
        self.武器融合属性B = MyQComboBox(self.main_frame2)
        for j in 武器属性B列表:
            self.武器融合属性B.addItem(j.固定属性描述)
        self.武器融合属性B.resize(60, 20)
        self.武器融合属性B.move(横坐标, 纵坐标 + 25)

        self.武器融合属性B1 = MyQComboBox(self.main_frame2)
        self.武器融合属性B1.resize(90 + 75, 20)
        self.武器融合属性B1.move(横坐标 + 110 - 50 + 5, 纵坐标 + 25)

        self.武器融合属性B2 = MyQComboBox(self.main_frame2)
        self.武器融合属性B2.resize(50, 20)
        self.武器融合属性B2.move(横坐标 + 205 + 20 + 10, 纵坐标 + 25)
        self.武器融合属性B.currentIndexChanged.connect(
            lambda: self.希洛克武器随机词条更新(self.武器融合属性B.currentIndex(), 1))

        纵坐标 = 纵坐标 + 60
        标签 = QLabel(trans('黑鸦遴选词条'), self.main_frame2)
        标签.setStyleSheet(标签样式 + 'QLabel{font-size:13px;}')
        标签.resize(410, 20)
        标签.move(横坐标, 纵坐标)
        标签.setAlignment(Qt.AlignCenter)

        名称 = trans(['武　　器', '戒　　指', '辅助装备', '下　　装'])
        纵坐标 = 纵坐标 + 25
        self.黑鸦词条选项 = []
        for i in range(4):
            this_index = i
            x = QLabel(名称[i], self.main_frame2)
            x.setStyleSheet(标签样式 +
                            'QLabel{font-size:13px;};text-align: justify;')
            # x.setStyleSheet('text-align: justify')
            x.resize(55, 20)
            x.move(横坐标, 纵坐标 + i * 25)
            tem = []
            tem.append(MyQComboBox(self.main_frame2))
            if i == 0:
                tem[0].addItems(['无', '计算最高', '自选数值', '自选数值-觉醒'])
                tem[0].resize(91, 20)
                tem[0].move(横坐标 + 60, 纵坐标 + 25 * i)
                tem[0].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦词条更新(index))
            else:
                tem[0].addItems(['无', '计算最高', '自选数值'])
                tem[0].resize(91, 20)
                tem[0].move(横坐标 + 60, 纵坐标 + 25 * i)
                tem[0].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦词条更新(index))
            tem.append(MyQComboBox(self.main_frame2))
            tem[1].resize(60, 20)
            tem[1].move(横坐标 + 156, 纵坐标 + 25 * i)

            tem.append(MyQComboBox(self.main_frame2))
            tem[2].resize(90 + 75, 20)
            tem[2].move(横坐标 + 266 - 50 + 5, 纵坐标 + 25 * i)

            tem.append(MyQComboBox(self.main_frame2))
            tem[3].resize(50, 20)
            tem[3].move(横坐标 + 361 + 20 + 10, 纵坐标 + 25 * i)
            if i > 0:
                for item in 装备变换属性列表:
                    tem[1].addItem(item.固定属性描述)
                tem[1].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦随机词条更新(index, 1))
            else:
                for item in 武器变换属性列表:
                    tem[1].addItem(item.固定属性描述)
                tem[1].currentIndexChanged.connect(
                    lambda state, index=i: self.黑鸦随机词条更新(index))
            self.黑鸦词条选项.append(tem)
            self.黑鸦词条更新(i)

        横坐标 = 740
        纵坐标 = 30
        self.希洛克套装按钮 = []
        self.希洛克单件按钮 = []
        self.希洛克遮罩透明度 = []
        self.希洛克选择状态 = [0] * 15

        count = 0
        for i in 希洛克套装:
            self.希洛克套装按钮.append(QPushButton(trans(i), self.main_frame2))
            self.希洛克套装按钮[count].setStyleSheet(按钮样式)
            self.希洛克套装按钮[count].resize(50, 22)
            self.希洛克套装按钮[count].move(横坐标, 纵坐标 + 3 + count * 40)
            self.希洛克套装按钮[count].clicked.connect(
                lambda state, index=(count + 1) * 100: self.希洛克选择(index))

            for j in range(3):
                序号 = count * 3 + j
                图片 = QLabel(self.main_frame2)
                图片.setPixmap(
                    QPixmap('./ResourceFiles/img/希洛克/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标 + 60 + j * 30, 纵坐标 + count * 40)
                self.希洛克遮罩透明度.append(QGraphicsOpacityEffect())
                self.希洛克遮罩透明度[序号].setOpacity(0.5)

                siroco_button = QPushButton(self.main_frame2)
                siroco_button.setStyleSheet("background-color: rgb(0, 0, 0)")
                siroco_button.resize(28, 28)
                siroco_button.move(横坐标 + 60 + j * 30, 纵坐标 + count * 40)
                siroco_button.setGraphicsEffect(self.希洛克遮罩透明度[序号])
                siroco_button.clicked.connect(
                    lambda state, index=序号: self.希洛克选择(index))
                self.希洛克单件按钮.append(siroco_button)
            count += 1

        横坐标 = 395
        纵坐标 = 480
        self.奥兹玛套装按钮 = []
        self.奥兹玛单件按钮 = []
        self.奥兹玛遮罩透明度 = []
        self.奥兹玛选择状态 = [0] * 25

        T = deepcopy(self.初始属性)

        T.装备描述 = 1

        count = 0
        for i in 奥兹玛套装:
            self.奥兹玛套装按钮.append(QPushButton(trans(i), self.main_frame2))
            self.奥兹玛套装按钮[count].setStyleSheet(按钮样式)
            self.奥兹玛套装按钮[count].resize(75, 22)
            self.奥兹玛套装按钮[count].move(横坐标, 纵坐标 + 3 + count * 32)
            self.奥兹玛套装按钮[count].clicked.connect(
                lambda state, index=(count + 1) * 100: self.奥兹玛选择(index))

            ozma = OzmaList[count]

            for j in range(5):
                序号 = count * 5 + j
                图片 = QLabel(self.main_frame2)
                图片.setPixmap(
                    QPixmap('./ResourceFiles/img/奥兹玛/' + str(序号) + '.png'))
                图片.resize(28, 28)
                图片.move(横坐标 + 60 + j * 30 + 20, 纵坐标 + count * 32)
                self.奥兹玛遮罩透明度.append(QGraphicsOpacityEffect())
                self.奥兹玛遮罩透明度[序号].setOpacity(0.5)

                tooltip = trans('<font color="#00A2E8">{奥兹玛融合属性}：</font><br>')
                tooltip += ozma(T)
                tooltip = tooltip_trim(tooltip)

                ozma_button = QPushButton(self.main_frame2)
                ozma_button.setStyleSheet("background-color: rgb(0, 0, 0)")
                ozma_button.setToolTip(tooltip)
                ozma_button.resize(28, 28)
                ozma_button.move(横坐标 + 60 + j * 30 + 20, 纵坐标 + count * 32)
                ozma_button.setGraphicsEffect(self.奥兹玛遮罩透明度[序号])
                ozma_button.clicked.connect(
                    lambda state, index=序号: self.奥兹玛选择(index))
                self.奥兹玛单件按钮.append(ozma_button)
            count += 1

        counter = 0
        for i in self.复选框列表:
            i.setStyleSheet(复选框样式)
            i.resize(180, 20)
            i.move(930, 25 + counter * 28)
            if counter < 1:
                i.setChecked(True)
            counter += 1

        self.排行选项 = []
        for i in range(4):
            self.排行选项.append(MyQComboBox(self.main_frame2))
        self.排行选项[0].setEditable(True)
        for i in [
                3000, 3500, 4000, 4500, 5000, 5500, 6000, 7000, 8000, 10000,
                12000, 15000, 20000
        ]:
            self.排行选项[0].addItem(trans('C力智:') + str(i))
        self.排行选项[0].setCurrentIndex(4)

        self.排行选项[1].setEditable(True)
        for i in [
                2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900,
                3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900,
                4000, 4200, 4400, 4600, 4800, 5000
        ]:
            self.排行选项[1].addItem(trans('C三攻:') + str(i))
        self.排行选项[1].setCurrentIndex(10)

        for i in ['物理百分比', '魔法百分比', '物理固伤', '魔法固伤']:
            self.排行选项[2].addItem(i)

        for i in ['无系统奶', '希洛克系统奶', '黑鸦系统奶']:
            self.排行选项[3].addItem(i)

        counter = 0
        for i in self.排行选项:
            i.resize(100, 20)
            i.move(990, 490 + counter * 28)
            counter += 1

        self.计算按钮2 = QPushButton(trans('开始计算'), self.main_frame2)
        self.计算按钮2.clicked.connect(lambda state: self.计算())
        self.计算按钮2.move(990, 610)
        self.计算按钮2.resize(100, 30)
        self.计算按钮2.setStyleSheet(按钮样式)

        self.觉醒选择状态 = 2
        self.一觉遮罩透明度 = QGraphicsOpacityEffect()
        self.一觉遮罩透明度.setOpacity(0.5)
        self.二觉遮罩透明度 = QGraphicsOpacityEffect()
        self.二觉遮罩透明度.setOpacity(0.0)
        x = 250
        y = 230
        self.觉醒选择 = QLabel(self.main_frame2)
        self.觉醒选择.setPixmap(QPixmap('./ResourceFiles/img/觉醒选择.png'))
        self.觉醒选择.resize(120, 100)
        self.觉醒选择.move(x, y - 20)
        self.一觉图片 = QLabel(self.main_frame2)
        self.一觉图片.setPixmap(self.技能图片[self.初始属性.一觉序号])
        self.一觉图片.resize(28, 28)
        self.一觉图片.move(x + 7, y + 8)
        self.二觉图片 = QLabel(self.main_frame2)
        self.二觉图片.setPixmap(self.技能图片[self.初始属性.二觉序号])
        self.二觉图片.resize(28, 28)
        self.二觉图片.move(x + 52, y + 8)
        self.一觉遮罩 = QPushButton(self.main_frame2)
        self.一觉遮罩.resize(38, 50)
        self.一觉遮罩.move(x + 2, y + 5)
        self.一觉遮罩.setStyleSheet(
            "QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}"
        )
        self.一觉遮罩.setGraphicsEffect(self.一觉遮罩透明度)
        self.一觉遮罩.clicked.connect(lambda state, index=1: self.强化觉醒选择(index))
        self.二觉遮罩 = QPushButton(self.main_frame2)
        self.二觉遮罩.resize(38, 50)
        self.二觉遮罩.move(x + 47, y + 5)
        self.二觉遮罩.setStyleSheet(
            "QPushButton{background-color:rgb(0,0,0);border:1px;border-radius:3px;}"
        )
        self.二觉遮罩.setGraphicsEffect(self.二觉遮罩透明度)
        self.二觉遮罩.clicked.connect(lambda state, index=2: self.强化觉醒选择(index))
        self.武器融合属性A.setEnabled(False)
        self.武器融合属性A1.setEnabled(False)
        self.武器融合属性A2.setEnabled(False)
        self.武器融合属性A.setStyleSheet(下拉框样式)
        self.武器融合属性A1.setStyleSheet(下拉框样式)
        self.武器融合属性A2.setStyleSheet(下拉框样式)
        # 武器融合属性B禁用
        self.武器融合属性B.setEnabled(False)
        self.武器融合属性B1.setEnabled(False)
        self.武器融合属性B2.setEnabled(False)
        self.武器融合属性B.setStyleSheet(下拉框样式)
        self.武器融合属性B1.setStyleSheet(下拉框样式)
        self.武器融合属性B2.setStyleSheet(下拉框样式)

    def 界面3(self):
        # increase_counter(ga_category="buffer界面", name="基础/细节/修正")
        # 第三个布局界面
        self.main_frame3 = QWidget()

        self.属性设置输入 = []
        self.技能设置输入 = []

        宽度 = 43

        列名称1 = trans(["智力", "体力", "精神"])
        行名称1 = trans([
            "工会属性", "训练官BUFF", "戒指", "婚房", "冒险团", "晶体契约", "收集箱", "勋章", "名称装饰卡",
            "快捷栏纹章", "宠物装备-红", "  宠物装备-蓝  ", "  宠物装备-绿  ", "宠物附魔", "皮肤",
            "站街修正", "进图修正", "登记修正", ''
        ])

        column_count = len(列名称1)
        row_count = len(行名称1)

        名称 = QLabel(trans("基础细节"), self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(标签样式)
        名称.resize(80, 25)
        名称.move(10, 5)

        for i in range(column_count):
            名称 = QLabel(列名称1[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(宽度, 25)
            名称.move(95 + i * (宽度 + 5), 5)

        Linelist = [[], [], []]

        for j in range(row_count):
            名称 = QLabel(行名称1[j], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(80, 25)
            名称.move(10, 35 + j * 30)

            for i in range(column_count):
                Linelist[i].append(QLineEdit(self.main_frame3))
                Linelist[i][j].setAlignment(Qt.AlignCenter)
                Linelist[i][j].setStyleSheet(输入框样式)
                if 行名称1[j] != '':
                    Linelist[i][j].resize(宽度, 22)
                    Linelist[i][j].move(95 + i * (宽度 + 5), 35 + j * 30)
                else:
                    Linelist[i][j].resize(0, 0)

        self.属性设置输入.extend(Linelist)

        列名称2 = trans(["智力", "体力", "精神", "徽章智", "徽章体", "徽章精", "技能等级及选项"])
        行名称2 = trans([
            "上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "左槽", "右槽", "耳环",
            "武器", "BUFF等级补正", "穿戴称号", "穿戴光环", "武器装扮", "时装", "宠物登记补正", "光环登记补正"
        ])

        self.列名称 = 列名称1 + 列名称2
        self.行名称 = 行名称1 + 行名称2

        名称 = QLabel(trans("附魔&徽章"), self.main_frame3)
        名称.setAlignment(Qt.AlignCenter)
        名称.setStyleSheet(标签样式)
        名称.resize(80, 25)
        名称.move(7 * 宽度, 5)
        for i in range(7):
            名称 = QLabel(列名称2[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            if i == 6:
                名称.resize(150, 25)
            else:
                名称.resize(宽度, 25)
            名称.move(90 + 7 * 宽度 + i * (宽度 + 5), 5)

        for j in range(19):
            名称 = QLabel(行名称2[j], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(80, 25)
            名称.move(7 * 宽度, 35 + j * 30)

        for i in range(6):
            Linelist = []
            for j in range(19):
                Linelist.append(QLineEdit(self.main_frame3))
                Linelist[j].setAlignment(Qt.AlignCenter)
                Linelist[j].setStyleSheet(输入框样式)
                Linelist[j].resize(宽度, 22)
                Linelist[j].move(90 + 7 * 宽度 + i * (宽度 + 5), 35 + j * 30)
            self.属性设置输入.append(Linelist)

        for j in range(19):
            self.技能设置输入.append(MyQComboBox(self.main_frame3))
            self.技能设置输入[j].addItem('无')
            self.技能设置输入[j].setStyleSheet(下拉框样式)
            self.技能设置输入[j].resize(150, 22)
            self.技能设置输入[j].move(90 + 7 * 宽度 + 6 * (宽度 + 5), 35 + j * 30)

        for j in [2, 3, 4]:
            self.技能设置输入[j].addItems(['Lv1-30(主动)Lv+1', 'Lv1-50(主动)Lv+1'])

        self.技能设置输入[2].addItems(['Lv1-35(主动)Lv+1', 'Lv30-50(主动)Lv+1'])
        self.技能设置输入[3].addItem('Lv30-50(主动)Lv+1')

        # 白金
        skills = [
            trans('{$name}Lv+1', name=i.名称) for i in self.角色属性A.技能表.values()
            if i.所在等级 < 48
        ]

        for j in [8, 9]:
            self.技能设置输入[j].addItems(skills)

        self.技能设置输入[12].addItems(
            ['BUFFLv+1', 'BUFFLv+2', 'BUFFLv+3', 'BUFFLv+4'])
        self.技能设置输入[13].addItems(['Lv1-50(主动)Lv+1', '一觉Lv+1', '一觉Lv+2'])
        self.技能设置输入[14].addItems([
            'Lv1-30(所有)Lv+1', 'Lv1-50(所有)Lv+1', 'Lv1-20(所有)Lv+1',
            'Lv20-30(所有)Lv+1', 'Lv1-80(所有)Lv+1'
        ])

        skills = [
            trans('{$name}Lv+1', name=i.名称) for i in self.角色属性A.技能表.values()
            if i.所在等级 < 85
        ]

        skills_weapons = [
            trans('{$name}Lv+1', name=i.名称) for i in self.角色属性A.技能表.values()
            if (i.所在等级 in [40, 45, 60, 70, 75, 80] and i.是否主动 == 1)
        ]

        self.技能设置输入[15].addItems(skills_weapons)
        self.技能设置输入[16].addItems(skills)

        self.技能设置输入[17].addItems(['BUFF力智+3%', 'BUFF三攻+3%', 'BUFF力智、三攻+3%'])
        self.技能设置输入[18].addItem('BUFF力智+3%')

        if '智力' in self.角色属性A.类型:
            self.修正列表名称 = trans([
                '转职被动智力', 'BUFF力智%', 'BUFF三攻%', '转职被动等级', '一觉被动力智', '一觉力智%',
                '一觉力智'
            ])
        else:
            self.修正列表名称 = trans([
                '守护恩赐体精', 'BUFF力智%', 'BUFF三攻%', '守护恩赐等级', '信念光环体精', '一觉力智%',
                '一觉力智'
            ])

        Linelist = []
        for i in range(len(self.修正列表名称)):
            名称 = QLabel(self.修正列表名称[i], self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(90, 25)
            名称.move(170 + 7 * 宽度 + 9 * (宽度 + 5), 35 + i * 30)
            Linelist.append(QLineEdit(self.main_frame3))
            Linelist[i].setAlignment(Qt.AlignCenter)
            Linelist[i].setStyleSheet(输入框样式)
            Linelist[i].resize(60, 25)
            Linelist[i].move(270 + 7 * 宽度 + 9 * (宽度 + 5), 35 + i * 30)
        self.属性设置输入.append(Linelist)

        count = 0
        self.时装选项 = []
        for i in trans(['头部', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']):
            名称 = QLabel(i, self.main_frame3)
            名称.setAlignment(Qt.AlignCenter)
            名称.setStyleSheet(标签样式)
            名称.resize(90, 25)
            名称.move(170 + 7 * 宽度 + 9 * (宽度 + 5), 255 + count * 30)
            self.时装选项.append(MyQComboBox(self.main_frame3))
            self.时装选项[count].addItems(['高级', '节日', '稀有', '神器'])
            self.时装选项[count].resize(60, 22)
            self.时装选项[count].move(270 + 7 * 宽度 + 9 * (宽度 + 5),
                                  255 + count * 30)
            self.时装选项[count].currentIndexChanged.connect(
                lambda state, index=count: self.时装选项更新(index))
            count += 1

        self.时装选项.append(MyQComboBox(self.main_frame3))
        self.时装选项[8].addItems(
            format_range("{}[8]", trans(['高级套装', '节日套装', '稀有套装', '神器套装'])))
        self.时装选项[8].resize(160, 22)
        self.时装选项[8].move(170 + 7 * 宽度 + 9 * (宽度 + 5), 260 + count * 30)
        self.时装选项[8].currentIndexChanged.connect(
            lambda state, index=8: self.时装选项更新(index))

        self.计算按钮3 = QPushButton(trans('开始计算'), self.main_frame3)
        self.计算按钮3.clicked.connect(lambda state: self.计算())
        self.计算按钮3.move(990, 610)
        self.计算按钮3.resize(100, 30)
        self.计算按钮3.setStyleSheet(按钮样式)

    def 界面5(self):
        # increase_counter(ga_category="buffer界面", name="自选装备计算")
        # 第五个布局
        self.main_frame5 = QWidget()
        标签 = QLabel(trans('单件选择'), self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(240, 25)
        标签.move(70, 20)

        标签 = QLabel(trans('锁定'), self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(70, 25)
        标签.move(10, 20)

        self.图片显示 = []

        count = 0

        self.装备锁定 = []
        self.自选装备 = []
        self.自选装备结果 = []
        self.self_selects = []

        def equips_getter():
            return [i.currentData() for i in self.自选装备]

        def equips_setter(value):
            self.self_selects = value

        store.compute("/{type}/memory/equips", equips_getter, equips_setter)

        for i in 部位列表:
            锁定选择 = QCheckBox(i, self.main_frame5)
            锁定选择.setStyleSheet(复选框样式)
            锁定选择.resize(70, 22)
            锁定选择.move(10, 50 + 30 * count)
            self.装备锁定.append(锁定选择)

            combo = MyQComboBox(self.main_frame5)
            combo.resize(220, 22)
            combo.move(90, 50 + 30 * count)

            self.自选装备.append(combo)

            combo.currentIndexChanged.connect(
                lambda _: store.emit("/{type}/memory/equips"))
            combo.currentIndexChanged.connect(
                lambda index, part=count: self.自选装备更改(part))
            for j in equ.get_equ_list():
                if j.部位 == i:
                    if i == '武器':
                        if j.类型 in self.角色属性A.武器选项:
                            combo.addItem(j.名称)
                    else:
                        combo.addItem(j.名称)
            count += 1

        self.计算标识 = 1
        标签 = QLabel(trans('批量选择'), self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(160, 25)
        标签.move(330, 20)

        套装类型 = ['防具', '首饰', '特殊', '上链左', '镯下右', '环鞋指']
        count = 0
        self.自选套装 = []
        for i in 套装类型:
            combo = MyQComboBox(self.main_frame5)
            套装名称 = []
            for j in equ.get_suit_list():
                if j.名称 not in 套装名称 and j.类型 == i:
                    套装名称.append(j.名称)
            combo.addItems(套装名称)
            combo.resize(160, 22)
            combo.move(330, 50 + 30 * count)
            combo.activated.connect(
                lambda state, index=count: self.自选套装更改(index))
            self.自选套装.append(combo)
            count += 1

        self.神话部位选项 = MyQComboBox(self.main_frame5)
        self.神话部位选项.addItems(['神话部位：无', '神话部位：上衣', '神话部位：手镯', '神话部位：耳环'])
        self.神话部位选项.resize(160, 22)
        self.神话部位选项.move(330, 50 + 30 * count)
        self.神话部位选项.activated.connect(lambda state: self.神话部位更改())

        count += 1

        self.自选装备栏选项 = MyQComboBox(self.main_frame5)

        # 自行设定自选装备栏数量,最大值为20,最小值为1,默认为6
        column_count = store.get("/{type}/data/self-select/column-count", 6)
        column_count = min(max(column_count, 1), 20)

        self.last_select_column = 0

        for i in range(column_count):
            self.自选装备栏选项.addItem('{}:{}'.format(trans('自选装备栏'), i))
        self.自选装备栏选项.setCurrentIndex(-1)
        self.自选装备栏选项.resize(160, 22)
        self.自选装备栏选项.move(330, 50 + 30 * count)
        self.自选装备栏选项.activated.connect(lambda state: self.自选装备栏更改(state))

        count += 1
        # 一键修正按钮添加
        self.一键站街设置输入.append(QLineEdit(self.main_frame5))
        self.一键站街设置输入[1].setAlignment(Qt.AlignCenter)
        self.一键站街设置输入[1].setStyleSheet(输入框样式)
        self.一键站街设置输入[1].resize(45, 24)
        self.一键站街设置输入[1].move(330, 50 + 30 * count)

        self.一键修正按钮 = QPushButton(trans('一键修正'), self.main_frame5)
        self.一键修正按钮.clicked.connect(lambda state: self.一键修正(1))
        self.一键修正按钮.move(330 + 60, 50 + 30 * count)
        self.一键修正按钮.resize(80, 24)
        self.一键修正按钮.setStyleSheet(按钮样式)

        标签 = QLabel(trans('辟邪玉提升率(理论值仅供参考)'), self.main_frame5)
        标签.setAlignment(Qt.AlignCenter)
        标签.setStyleSheet(标签样式)
        标签.resize(200, 25)
        标签.move(525, 20)

        self.辟邪玉提升率1 = []
        self.辟邪玉提升率2 = []
        count = 0
        for i in 辟邪玉列表:
            if i.名称 != '无':
                if i.间隔 < 1:
                    temp = trans(i.名称) + '+' + str(i.最大值) + '%'
                else:
                    temp = trans(i.名称) + '+' + str(i.最大值)
                self.辟邪玉提升率1.append(QLabel(temp, self.main_frame5))
                self.辟邪玉提升率1[count].setAlignment(Qt.AlignCenter)
                self.辟邪玉提升率1[count].setStyleSheet(标签样式)
                self.辟邪玉提升率1[count].resize(180, 25)
                self.辟邪玉提升率1[count].move(500, 50 + 30 * count)
                self.辟邪玉提升率2.append(QLabel('0.00%', self.main_frame5))
                self.辟邪玉提升率2[count].setAlignment(Qt.AlignCenter)
                self.辟邪玉提升率2[count].setStyleSheet(标签样式)
                self.辟邪玉提升率2[count].resize(60, 25)
                self.辟邪玉提升率2[count].move(690, 50 + 30 * count)
                count += 1

        初始x = 805
        初始y = 20
        图片显示 = QLabel(self.main_frame5)
        图片显示.setPixmap(self.输出背景图片)
        图片显示.setAlignment(Qt.AlignTop)
        图片显示.resize(268, 546)
        图片显示.move(初始x, 初始y + 11)
        人物 = QLabel(self.main_frame5)
        图片 = QPixmap('./ResourceFiles/' + self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(初始x + 90 + int(45 - 图片.width() / 2), 初始y + 40)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)

        self.提升率显示 = QLabel(self.main_frame5)
        self.提升率显示.setStyleSheet(
            "QLabel{color:rgb(255,255,255);font-size:25px}")
        self.提升率显示.resize(250, 36)
        self.提升率显示.move(初始x + 10, 初始y + 517)
        self.提升率显示.setAlignment(Qt.AlignCenter)

        偏移量 = 187
        x坐标 = [
            32, 0, 0, 32, 0, 偏移量, 偏移量 + 32, 偏移量 + 32, 偏移量, 偏移量, 偏移量 + 32, 32
        ]
        y坐标 = [0, 0, 32, 32, 64, 0, 0, 32, 64, 32, 64, 64]

        for i in range(12):
            self.图片显示.append(QLabel(self.main_frame5))
            self.图片显示[i].setMovie(equ.get_img_by_name(self.self_selects[i]))
            self.图片显示[i].resize(26, 26)
            self.图片显示[i].move(初始x + 10 + x坐标[i], 初始y + 31 + y坐标[i])
            self.图片显示[i].setAlignment(Qt.AlignCenter)

        self.面板显示 = []
        for i in range(11):
            self.面板显示.append(QLabel(self.main_frame5))
        const = 139
        self.面板显示[0].move(初始x + 20, 初始y + const + 10)

        const += 36
        count = 0
        for i in [2, 3, 4, 5, 6, 7]:
            self.面板显示[i].move(初始x + 20, 初始y + const + count * 18)
            count += 1

        count = 0
        for i in [8, 9, 10]:
            self.面板显示[i].move(初始x + 155, 初始y + const + count * 18)
            count += 1

        for i in range(len(self.面板显示)):
            self.面板显示[i].setStyleSheet(
                "QLabel{font-size:12px;color:rgb(255,255,255)}")
            self.面板显示[i].resize(100, 18)
            self.面板显示[i].setAlignment(Qt.AlignLeft if i not in
                                      [2, 8] else Qt.AlignCenter)

        self.词条显示 = []
        for i in range(12):
            self.词条显示.append(QLabel(self.main_frame5))

        j = 315 + 初始y
        for i in self.词条显示:
            i.setStyleSheet("QLabel{font-size:12px;color:rgb(104,213,237)}")
            i.move(8 + 初始x, j)
            i.resize(300, 18)
            i.setAlignment(Qt.AlignLeft)
            j += 18

        # self.总伤害 = QLabel(self.main_frame5)
        # self.总伤害.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        # self.总伤害.resize(600, 36)
        # self.总伤害.move(200, 517 + 初始y)
        # self.总伤害.setAlignment(Qt.AlignCenter)

        self.套装名称显示 = []
        for i in range(9):
            self.套装名称显示.append(QLabel(self.main_frame5))
            self.套装名称显示[i].move(132 + 初始x, 138 + 180 + 20 * i + 初始y)
            self.套装名称显示[i].resize(132, 18)
            self.套装名称显示[i].setAlignment(Qt.AlignCenter)

        自选计算按钮 = QPushButton(trans('查看详情'), self.main_frame5)
        自选计算按钮.clicked.connect(lambda state: self.自选计算())
        自选计算按钮.move(995, 610)
        自选计算按钮.resize(80, 28)
        自选计算按钮.setStyleSheet(按钮样式)

        self.基准值 = []

        设置基准值 = QPushButton(trans('设为基准'), self.main_frame5)
        设置基准值.clicked.connect(lambda state: self.基准值设置())
        设置基准值.move(900, 610)
        设置基准值.resize(80, 28)
        设置基准值.setStyleSheet(按钮样式)

        清空基准值 = QPushButton(trans('清空基准'), self.main_frame5)
        清空基准值.clicked.connect(lambda state: self.基准值设置(1))
        清空基准值.move(805, 610)
        清空基准值.resize(80, 28)
        清空基准值.setStyleSheet(按钮样式)

        换装选项 = QCheckBox(trans('启用登记'), self.main_frame5)

        换装选项.toggled.connect(lambda checked: self.启用换装登记(checked))
        换装选项.move(320, 340)
        换装选项.resize(70, 28)
        换装选项.setStyleSheet(复选框样式)

        换装设置 = QPushButton(trans('登记设置'), self.main_frame5)
        换装设置.clicked.connect(lambda _: self.换装设置())
        换装设置.move(390, 340)
        换装设置.resize(80, 28)
        换装设置.setStyleSheet(按钮样式)

        名望设置 = QPushButton('名望细节', self.main_frame5)
        名望设置.clicked.connect(lambda _: self.名望设置())
        名望设置.move(710, 610)
        名望设置.resize(80, 28)
        名望设置.setStyleSheet(按钮样式)

    def 名望设置(self):
        increase_counter(ga_category="buffer详细功能使用", name="名望")

        def createClient():
            store.set("/fame/temp/property", self)
            # 设置图标和背景 临时做法
            store.const("/app/window/icon", self.icon)
            store.const("/app/window/background_image", self.主背景图片)
            store.watch("/fame/event/changed", lambda _, : self.自选计算(1))
            client = 名望窗口()
            client.初始化()
            return client

        DefaultDialogRegister.showDialog("base_fame({})".format(type(self)),
                                         createClient, self)

    def 自选装备栏更改(self, index):
        if self.计算标识 == 0:
            return

        self.计算标识 = 0

        data = store.get("/{type}/data/self_select/equips", [])
        length = len(self.自选装备)
        column_index = store.get("/{type}/data/self_select/column_index")

        defaultData = [0] * length

        while column_index >= len(data):
            data.append(defaultData)

        if column_index != index:
            data[column_index] = [i.currentIndex() for i in self.自选装备]

        column = data[index] if index < len(data) else defaultData
        for i in range(length):
            self.自选装备[i].setCurrentIndex(column[i])
        store.set("/{type}/data/self_select/column_index", index)
        store.set("/{type}/data/self_select/equips", data)

        self.计算标识 = 1
        self.自选计算(1)

    def 启用换装登记(self, checked):
        self.登记启用 = checked
        self.自选计算(1)

    def 换装设置(self):
        increase_counter(ga_category="buffer详细功能使用", name="切装")

        def createClient():
            store.compute("/{type}/temp/property_a", lambda: self.角色属性A)
            # 换装更新事件
            store.watch("/{type}/event/register_changed",
                        lambda _, : self.自选计算(1))
            # 设置图标和背景 临时做法
            store.const("/app/window/icon", self.icon)
            store.const("/app/window/background_image", self.主背景图片)
            client = 登记窗口()
            client.初始化()
            return client

        DefaultDialogRegister.showDialog("panel({})".format(type(self)),
                                         createClient, self)

    def 时装选项更新(self, index):
        if index == 8:
            count = 0
            for i in self.时装选项:
                if count != 8:
                    i.setCurrentIndex(self.时装选项[8].currentIndex())
                count += 1
            return
        else:
            智力, 体力, 精神 = 0, 0, 0
            套装字典 = {'高级': 0, '节日': 0, '稀有': 0, '神器': 0}
            for i in range(8):
                套装字典[self.时装选项[i].currentData()] = 套装字典.get(
                    self.时装选项[i].currentData(), 0) + 1
            # 套装属性
            神器 = 套装字典['神器']
            稀有 = 套装字典['稀有'] + 神器
            if 套装字典['高级'] >= 3:
                智力 += 10
                体力 += 10
                精神 += 10
            if 稀有 >= 3 and 神器 < 3:
                智力 += 40
                体力 += 40
                精神 += 40
            if 套装字典['神器'] >= 3:
                智力 += 50
                体力 += 50
                精神 += 50
            if 套装字典['高级'] >= 8:
                智力 += 10
                体力 += 10
                精神 += 10
            if 套装字典['节日'] >= 8:
                智力 += 25
                体力 += 25
                精神 += 25
            if 稀有 >= 8 and 神器 < 8:
                智力 += 40
                体力 += 40
                精神 += 40
            if 套装字典['神器'] >= 8:
                智力 += 50
                体力 += 50
                精神 += 50
            数据 = [45, 45, 55, 65]
            智力 += 数据[self.时装选项[0].currentIndex()]  # 头部
            精神 += 数据[self.时装选项[0].currentIndex()]  # 头部
            智力 += 数据[self.时装选项[1].currentIndex()]  # 帽子
            精神 += 数据[self.时装选项[1].currentIndex()]  # 帽子
            数据 = [0, 0, 55, 65]
            体力 += 数据[self.时装选项[5].currentIndex()]  # 腰带
            数据 = [45, 45, 55, 65]
            体力 += 数据[self.时装选项[7].currentIndex()]  # 鞋子

            数据 = [0, 20, 0, 0]
            智力 += 数据[self.时装选项[6].currentIndex()]  # 下装
            体力 += 数据[self.时装选项[6].currentIndex()]  # 下装
            精神 += 数据[self.时装选项[6].currentIndex()]  # 下装

            self.属性设置输入[3][16].setText(str(智力))
            self.属性设置输入[4][16].setText(str(体力))
            self.属性设置输入[5][16].setText(str(精神))

    def 希洛克武器选择更新(self):
        if self.希洛克武器选择.currentIndex() != 2:
            # 武器融合属性A禁用
            self.武器融合属性A.setEnabled(False)
            self.武器融合属性A1.setEnabled(False)
            self.武器融合属性A2.setEnabled(False)
            self.武器融合属性A.setStyleSheet(下拉框样式)
            self.武器融合属性A1.setStyleSheet(下拉框样式)
            self.武器融合属性A2.setStyleSheet(下拉框样式)
            # 武器融合属性B禁用
            self.武器融合属性B.setEnabled(False)
            self.武器融合属性B1.setEnabled(False)
            self.武器融合属性B2.setEnabled(False)
            self.武器融合属性B.setStyleSheet(下拉框样式)
            self.武器融合属性B1.setStyleSheet(下拉框样式)
            self.武器融合属性B2.setStyleSheet(下拉框样式)
        else:
            # 武器融合属性A启用
            self.武器融合属性A.setEnabled(True)
            self.武器融合属性A1.setEnabled(True)
            self.武器融合属性A2.setEnabled(True)
            self.武器融合属性A.setStyleSheet(下拉框样式)
            self.武器融合属性A1.setStyleSheet(下拉框样式)
            self.武器融合属性A2.setStyleSheet(下拉框样式)
            # 武器融合属性B启用
            self.武器融合属性B.setEnabled(True)
            self.武器融合属性B1.setEnabled(True)
            self.武器融合属性B2.setEnabled(True)
            self.武器融合属性B.setStyleSheet(下拉框样式)
            self.武器融合属性B1.setStyleSheet(下拉框样式)
            self.武器融合属性B2.setStyleSheet(下拉框样式)

    def 调整觉醒择优方向(self, index):
        if index < 1:
            self.觉醒择优系数.setVisible(True)
        else:
            self.觉醒择优系数.setVisible(False)
            self.觉醒择优系数.setCurrentText(str(1.0 if index > 1 else 0.7))

    def 希洛克武器随机词条更新(self, index, x=0):
        if x == 0:
            self.武器融合属性A1.clear()
            self.武器融合属性A2.clear()

            if index == 0:
                return

            属性A = 武器属性A列表[index]

            for item in 属性A.range():
                self.武器融合属性A2.addItem(item)
            self.武器融合属性A1.addItem(属性A.随机属性描述)

        elif x == 1:
            self.武器融合属性B1.clear()
            self.武器融合属性B2.clear()

            if index == 0:
                return

            属性B = 武器属性B列表[index]

            for item in 属性B.range():
                self.武器融合属性B2.addItem(item)
            self.武器融合属性B1.addItem(属性B.随机属性描述)

    def 黑鸦词条更新(self, index):
        if self.黑鸦词条选项[index][0].currentIndex() < 2:
            for i in range(1, 4):
                self.黑鸦词条选项[index][i].setEnabled(False)
                self.黑鸦词条选项[index][i].setStyleSheet(下拉框样式)
        elif index == 0 and self.黑鸦词条选项[index][0].currentIndex() == 3:
            for i in range(1, 4):
                self.黑鸦词条选项[0][i].setEnabled(False)
                self.黑鸦词条选项[0][i].setStyleSheet(下拉框样式)
        else:
            for i in range(1, 4):
                self.黑鸦词条选项[index][i].setEnabled(True)
                self.黑鸦词条选项[index][i].setStyleSheet(下拉框样式)

    def 黑鸦随机词条更新(self, i, x=0):
        index = self.黑鸦词条选项[i][1].currentIndex()
        self.黑鸦词条选项[i][2].clear()
        self.黑鸦词条选项[i][3].clear()
        if index == 0:
            return

        装备属性 = 武器变换属性列表[index] if x == 0 else 装备变换属性列表[index]
        temp = 装备属性.最大值
        while temp >= 装备属性.最小值:
            if 装备属性.间隔 / 10 >= 1:
                self.黑鸦词条选项[i][3].addItem(str(int(temp)))
            else:
                self.黑鸦词条选项[i][3].addItem(str(temp) + '%')
            temp -= 装备属性.间隔
        self.黑鸦词条选项[i][2].addItem(装备属性.随机属性描述)

    def BUFF次数输入填写(self, x, skill=None):
        if self.次数输入[x].currentIndex() == 2:
            self.次数输入[x].setEditable(True)
            self.次数输入[x].clearEditText()
            self.次数输入[x].setStyleSheet(下拉框样式)
        else:
            self.次数输入[x].setEditable(False)

    def 批量选择(self, index):
        if index == 1:
            if self.全选状态 == 1:
                self.全选状态 = 0
            else:
                self.全选状态 = 1
            if sum(self.装备选择状态[74:244]) == 170:
                self.批量选择(0)

        for i in equ.get_equ_list():
            if i.部位 != '武器':
                if i.品质 != '神话' or index == 0 or self.全选状态 == 0:
                    self.装备图标点击事件(equ.get_id_by_name(i.名称), index, x=0)
            elif i.类型 in self.角色属性A.武器选项:
                self.装备图标点击事件(equ.get_id_by_name(i.名称), index, x=0)

        self.装备图标点击事件(74, index)

    def 基准值设置(self, x=0):
        self.基准值.clear()
        if x == 0:
            A = deepcopy(self.初始属性)
            self.输入属性(A)
            A.穿戴装备(self.self_selects)

            self.关闭排行窗口()
            self.排行数据.clear()
            self.排行数据.append(self.self_selects + [0] + A.套装栏 + ['无'])
            self.输出界面(0, '基准值', 自选计算模式=True)
            self.基准值 = deepcopy(self.自选计算数据)
        self.自选计算(1)

    def 载入配置(self, path='set'):
        filepath = './ResourceFiles/{}/{}/'.format(self.角色属性A.实际名称, path)
        if os.path.exists(os.path.join(
                filepath, "page_1.json")) or os.path.exists(
                    os.path.join(filepath, "store.json")):
            self.载入json(path)
            return
        else:
            # 如果不存在任何存档则载入重置存档
            self.载入json(path='reset')

    def 设置技能选项(self, num, info):

        try:
            self.等级调整[num].setCurrentIndex(info['level'])
        except Exception as e:
            logger.error(e)
            pass

        try:
            self.次数输入[num].setCurrentIndex(info['count'])
        except Exception as e:
            logger.error(e)

    def 获取技能选项(self, num):
        info = {}
        try:
            info['level'] = self.等级调整[num].currentIndex()
        except Exception as e:
            info['level'] = 0
            logger.error(e)

        try:
            info['count'] = self.次数输入[num].currentIndex()
        except Exception as e:
            info['count'] = 0
            logger.error(e)
        return info

    def 载入旧版json(self, path='set', page=[0, 1, 2, 3, 4]):
        filepath = './ResourceFiles/{}/{}'.format(self.角色属性A.实际名称, path)

        if 0 in page:
            # 第一页(装备/选择/打造)
            try:
                filename = 'page_1.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                store.set("/{type}/data/title", set_data['称号'])
                store.set("/{type}/data/pet", set_data['宠物'])
                store.set('/{type}/data/compute_mode', set_data["计算模式"])
                store.set('/{type}/data/ditto_checked', set_data["百变怪"])
                store.set('/{type}/data/myth_top_checked', set_data['神话排名勾选'])
                store.set('/{type}/data/awakening_switch_checked',
                          set_data['切装模式选项'])
                store.set('/{type}/data/thread_count', set_data['线程数量'])
                store.set("/{type}/data/equip_checked", set_data['装备勾选'])
                store.set("/{type}/data/equip_forges", set_data['装备打造'])
            except Exception as error:
                logger.error(error)

        if 1 in page:
            # 第二页(技能/符文/药剂)
            try:
                filename = 'page_2.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()

                store.set("/{type}/data/awakening_binding", set_data['觉醒选择'])
                store.set("/{type}/data/talismans", set_data['护石栏'])
                store.set("/{type}/data/consumables", set_data['药剂勾选'])

                skills = {}
                技能选项 = set_data['技能选项']
                for key in 技能选项.keys():
                    skills[key] = {
                        'level': 技能选项[key]['等级'],
                        'count': 技能选项[key]['次数']
                    }
                store.set("/{type}/data/skill", skills)

                store.set("/{type}/data/weapon_fusion", [
                    set_data['武器融合属性A'], set_data['武器融合属性A2'],
                    set_data['武器融合属性B'], set_data['武器融合属性B2']
                ])
                store.set("/{type}/data/siroco_weapon", set_data['希洛克武器选择'])
                store.set("/{type}/data/jude_effects", set_data['辟邪玉效果'])
                store.set('/{type}/data/jude_values', set_data['辟邪玉数值'])
                store.set('/{type}/data/top_options', set_data['排行选项'])
                store.set('/{type}/data/black_purgatory', set_data['黑鸦选择'])
                if '希洛克选择' in set_data:
                    store.set('/{type}/data/siroco', set_data['希洛克选择'])
                if '奥兹玛选择' in set_data:
                    store.set('/{type}/data/ozma', set_data['奥兹玛选择'])
            except Exception as error:
                logger.error(error)

        if 2 in page:
            # 第三页(基础/细节/修正)
            try:
                filename = 'page_3.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()

                store.set("/{type}/data/avatar", set_data['时装选项'])
                store.set("/{type}/data/detail_values", set_data['细节数值'])
                store.set("/{type}/data/detail_options", set_data['细节选项'])
            except Exception as error:
                logger.error(error)

        if 3 in page:
            # 第四页(神话属性修正)
            try:
                filename = 'page_4.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                store.set("/{type}/data/myth_properties", set_data['神话属性修正'])
            except Exception as error:
                logger.error(error)
        if 4 in page:
            # 第五页(自选装备计算)
            try:
                filename = 'page_5.json'
                set_data = {}
                with open(os.path.join(filepath, filename),
                          encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                store.set("/{type}/data/self_select/equips",
                          [set_data['自选装备']])
                store.set("/{type}/data/self_select/column_index", 0)
                store.set("/{type}/data/self_select/locked", set_data['装备锁定'])
            except Exception as error:
                logger.error(error)

    def 载入json(self, path='set', page=[0, 1, 2, 3, 4]):

        filepath = './ResourceFiles/{}/{}'.format(self.角色属性A.实际名称, path)

        filename = os.path.join(filepath, "store.json")

        if os.path.exists(filename):
            try:
                set_data = {}
                with open(filename, encoding='utf-8') as fp:
                    set_data = json.load(fp)
                fp.close()
                store.imports(set_data)
            except Exception as error:
                logger.error(error)
        else:
            self.载入旧版json(path, page)

        if 0 in page:
            try:
                self.称号.setCurrentIndex(store.get("/{type}/data/title", 0))
            except Exception as error:
                logger.error(error)
            try:
                self.宠物.setCurrentIndex(store.get("/{type}/data/pet", 0))
            except Exception as error:
                logger.error(error)
            try:
                self.计算模式选择.setCurrentIndex(
                    store.get("/{type}/data/compute_mode", 1))
            except Exception as error:
                logger.error(error)
            try:
                self.百变怪选项.setChecked(
                    store.get("/{type}/data/ditto_checked", 1))
            except Exception as error:
                logger.error(error)
            try:
                self.神话排名选项.setChecked(
                    store.get("/{type}/data/myth_top_checked", 0))
            except Exception as error:
                logger.error(error)
            try:
                self.切装模式选项.setChecked(
                    store.get("/{type}/data/awakening_switch_checked", 1))
            except Exception as error:
                logger.error(error)
            try:
                self.线程数选择.setCurrentIndex(
                    store.get("/{type}/data/thread_count", 12))
            except Exception as error:
                logger.error(error)

            try:
                self.批量选择(0)
                num = 0
                data = store.get("/{type}/data/equip_checked", [])
                for i in data:
                    if i == 1:
                        self.装备图标点击事件(num, 1)
                    num += 1
            except Exception as error:
                logger.error(error)
            try:
                num = 0
                data = store.get("/{type}/data/equip_forges", [])
                for i in data:
                    self.装备打造选项[num].setCurrentIndex(i)
                    num += 1
            except Exception as error:
                logger.error(error)

        if 1 in page:
            try:
                try:
                    self.强化觉醒选择(store.get('/{type}/data/awakening_binding'))
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = store.get('/{type}/data/talismans')

                    for i in data:
                        self.护石栏[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = store.get('/{type}/data/consumables')
                    for i in data:
                        self.复选框列表[num].setChecked(i)
                        num += 1
                except Exception as error:
                    logger.error(error)

                data = store.get('/{type}/data/skill', {})

                num = 0
                for skill in self.角色属性A.技能表.values():
                    try:
                        self.设置技能选项(num, data[skill.名称])
                    except Exception as error:
                        logger.error(error)
                    num += 1
                try:
                    self.觉醒择优系数.setCurrentText(
                        str(
                            store.get("/{type}/data/awakening_coefficient",
                                      1.0)))
                except Exception as error:
                    logger.error(error)

                try:
                    self.觉醒择优方向.setCurrentIndex(
                        store.get("/{type}/data/awakening_direction", 0))
                except Exception as error:
                    logger.error(error)

                data = store.get('/{type}/data/weapon_fusion', [0, 0, 0, 0])

                try:
                    self.武器融合属性A.setCurrentIndex(data[0])
                except Exception as error:
                    logger.error(error)
                try:
                    self.武器融合属性A2.setCurrentIndex(data[1])
                except Exception as error:
                    logger.error(error)
                try:
                    self.武器融合属性B.setCurrentIndex(data[2])
                except Exception as error:
                    logger.error(error)
                try:
                    self.武器融合属性B2.setCurrentIndex(data[3])
                except Exception as error:
                    logger.error(error)

                try:
                    self.希洛克武器选择.setCurrentIndex(
                        store.get('/{type}/data/siroco_weapon'))
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get('/{type}/data/jude_effects')
                    num = 0
                    for i in data:
                        self.辟邪玉选择[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get('/{type}/data/jude_values')
                    num = 0
                    for i in data:
                        self.辟邪玉数值[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get('/{type}/data/top_options')
                    num = 0
                    for i in data:
                        self.排行选项[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get('/{type}/data/black_purgatory')
                    x = 0
                    for i in data:
                        y = 0
                        for j in i:
                            self.黑鸦词条选项[x][y].setCurrentIndex(j)
                            y += 1
                        x += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/siroco", [0] * 15)
                    self.希洛克选择(0, 1)
                    num = 0
                    for i in data:
                        if i == 1:
                            self.希洛克选择(num)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    data = store.get("/{type}/data/ozma", [0] * 25)
                    self.奥兹玛选择(0, 1)
                    num = 0
                    for i in data:
                        if i == 1:
                            self.奥兹玛选择(num)
                        num += 1
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)
        if 2 in page:
            try:
                try:
                    num = 0
                    data = store.get("/{type}/data/avatar")
                    for i in data:
                        self.时装选项[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
                try:
                    x = 0
                    data = store.get("/{type}/data/detail_values")
                    for i in data:
                        y = 0
                        for j in i:
                            try:
                                self.属性设置输入[x][y].setText(j)
                            except Exception as e:
                                logger.error(e)
                            y += 1
                        x += 1
                except Exception as error:
                    logger.error(error)
                try:
                    num = 0
                    data = store.get("/{type}/data/detail_options")
                    for i in data:
                        self.技能设置输入[num].setCurrentIndex(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

        if 3 in page:
            try:
                num = 0
                data = store.get("/{type}/data/myth_properties")
                for i in data:
                    self.神话属性选项[num].setCurrentIndex(i)
                    num += 1
            except Exception as error:
                logger.error(error)
        if 4 in page:
            try:
                try:
                    num = 0
                    index = store.get('/{type}/data/self_select/column_index',
                                      0)
                    self.自选装备栏选项.setCurrentIndex(index)
                    self.自选装备栏更改(index)
                except Exception as error:
                    logger.error(error)

                try:
                    num = 0
                    data = store.get('/{type}/data/self_select/locked')
                    for i in data:
                        self.装备锁定[num].setChecked(i)
                        num += 1
                except Exception as error:
                    logger.error(error)
            except Exception as error:
                logger.error(error)

    def 奥兹玛选择(self, index, x=0):
        super().奥兹玛选择(index, x)
        store.emit("/{type}/data/ozma")

    def 希洛克选择(self, index, x=0):
        super().希洛克选择(index, x)
        store.emit("/{type}/data/siroco")

    def exports_store(self, page=[0, 1, 2, 3, 4]):
        if 0 in page:
            # 第一页(装备/选择/打造)
            try:
                store.set('/{type}/data/title', self.称号.currentIndex())
                store.set("/{type}/memory/title", self.称号.currentData())
                store.set('/{type}/data/pet', self.宠物.currentIndex())
                store.set('/{type}/memory/pet', self.宠物.currentData())
                store.set('/{type}/data/compute_mode',
                          self.计算模式选择.currentIndex())
                store.set('/{type}/data/ditto_checked', self.百变怪选项.isChecked())

                store.set('/{type}/data/myth_top_checked',
                          self.神话排名选项.isChecked())
                store.set('/{type}/data/awakening_switch_checked',
                          self.切装模式选项.isChecked())
                store.set('/{type}/data/thread_count',
                          self.线程数选择.currentIndex())
                store.set('/{type}/data/equip_checked', self.装备选择状态)
                store.set('/{type}/data/equip_forges',
                          [i.currentIndex() for i in self.装备打造选项])
            except Exception as error:
                logger.error(error)

        if 1 in page:
            # 第二页(技能/符文/药剂)
            try:

                store.set('/{type}/data/awakening_binding', self.觉醒选择状态)
                store.set('/{type}/data/talismans',
                          [i.currentIndex() for i in self.护石栏])
                store.set('/{type}/data/consumables',
                          [i.isChecked() for i in self.复选框列表])

                skills = {}
                num = 0
                for skill in self.角色属性A.技能表.values():
                    skills[skill.名称] = self.获取技能选项(num)
                    num += 1
                store.set('/{type}/data/skill', skills)

                data = [
                    self.武器融合属性A.currentIndex(),
                    self.武器融合属性A2.currentIndex(),
                    self.武器融合属性B.currentIndex(),
                    self.武器融合属性B2.currentIndex(),
                ]

                store.set("/{type}/data/weapon_fusion", data)

                store.set("/{type}/data/siroco_weapon",
                          self.希洛克武器选择.currentIndex())

                store.set("/{type}/data/jude_effects",
                          [i.currentIndex() for i in self.辟邪玉选择])
                store.set("/{type}/data/jude_values",
                          [i.currentIndex() for i in self.辟邪玉数值])

                store.set("/{type}/data/black_purgatory",
                          [[j.currentIndex() for j in i] for i in self.黑鸦词条选项])

                store.set("/{type}/data/top_options",
                          [i.currentIndex() for i in self.排行选项])

                store.set("/{type}/data/awakening_coefficient",
                          float(self.觉醒择优系数.currentText()))
                store.set("/{type}/data/awakening_direction",
                          self.觉醒择优方向.currentIndex())
                store.set("/{type}/data/siroco", self.希洛克选择状态)
                store.set("/{type}/data/ozma", self.奥兹玛选择状态)
            except Exception as error:
                logger.error(error)

        if 2 in page:
            # 第三页(基础/细节/修正)
            try:
                # 时装选项
                store.set("/{type}/data/avatar",
                          [i.currentIndex() for i in self.时装选项])
                store.set("/{type}/memory/avatar",
                          [i.currentData() for i in self.时装选项])
                # 细节数值
                store.set("/{type}/data/detail_values",
                          [[j.text() for j in i] for i in self.属性设置输入])
                # 细节选项
                store.set("/{type}/data/detail_options",
                          [i.currentIndex() for i in self.技能设置输入])

            except Exception as error:
                logger.error(error)

        if 3 in page:
            # 第四页(神话属性修正)
            try:
                # 神话属性修正
                store.set("/{type}/data/myth_properties",
                          [i.currentIndex() for i in self.神话属性选项])
            except Exception as error:
                logger.error(error)

        if 4 in page:
            # 第五页(自选装备计算)
            try:
                data = store.get("/{type}/data/self_select/equips", [])
                column_index = self.自选装备栏选项.currentIndex()
                length = len(self.自选装备)
                while column_index >= len(data):
                    data.append([0] * length)

                data[column_index] = [i.currentIndex() for i in self.自选装备]

                store.set("/{type}/data/self_select/equips", data)
                store.set('/{type}/data/self_select/column_index',
                          column_index)
                store.set("/{type}/data/self_select/locked",
                          [i.isChecked() for i in self.装备锁定])
            except Exception as error:
                logger.error(error)

    def 保存json(self, path='set', page=[0, 1, 2, 3, 4]):
        self.exports_store(page)
        try:
            filepath = './ResourceFiles/{}/{}/store.json'.format(
                self.角色属性A.实际名称, path)
            set_data = store.exports(
                lambda i: str.startswith(i, "/buffer/data"))
            with open(filepath, "w", encoding='utf-8') as fp:
                json.dump(set_data, fp, ensure_ascii=False, indent=4)
            fp.close()
        except Exception as error:
            logger.error(error)

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        self.保存json(path)

    # 一键修正计算
    def 一键修正(self, x=0):
        increase_counter(ga_category="buffer详细功能使用", name="一键修正")
        sign = -1
        try:
            if self.一键站街设置输入[0].text() != '' or self.一键站街设置输入[1].text() != '':
                sign = 1
        except Exception as e:
            logger.error(e)
            pass
        if sign == -1:
            QMessageBox.information(self, "错误", "请在按钮左侧输入站街数值")
            return

        if x == 0:
            if self.组合计算(2) == 0:
                QMessageBox.information(self, "错误", "请勾选齐全身上穿戴的装备")
                return
            if self.组合计算(2) > 1:
                QMessageBox.information(self, "错误", "请勿勾选身上未穿戴的装备")
                return

        self.修正套装计算(x)
        self.角色属性B = deepcopy(self.初始属性)
        self.输入属性(self.角色属性B)
        self.角色属性B.穿戴装备(self.有效穿戴组合[0])
        self.角色属性B.排行系数 = 1
        self.角色属性B.装备属性计算()

        self.面板修正(self.角色属性B, x)

    def 面板修正(self, 属性, x):
        数据 = 0
        数据 = to_int(self.一键站街设置输入[x].text())
        if 数据 is None:
            QMessageBox.information(self, "错误", "站街面板输入格式错误,已重置为空")
            self.一键站街设置输入[x].setText('')
            数据 = 0

        if 数据 == 0:
            QMessageBox.information(self, "错误", "请输入站街面板")
            return
        self.站街面板修正(属性, 数据)
        self.click_window(2)
        QMessageBox.information(
            self, "自动修正计算完毕", "仅对站街修正进行了修改,使面板与输入一致<br>请自行核对其它页面 非智力/体力/精神条目")

    def click_window(self, index, info=''):
        if info != '':
            increase_counter(ga_category="界面使用情况", name=info)
        self.保存json(self.存档位置, page=[self.当前页面])
        self.当前页面 = index

        if self.stacked_layout.currentIndex() != index:
            self.stacked_layout.setCurrentIndex(index)
        for i in self.window_btn:
            i.setStyleSheet(页签样式)
        self.window_btn[index].setStyleSheet(页签样式_选中)

        if index == 3:
            count1 = 0
            count2 = 0
            num = 0
            width = 1100
            height = 680
            page4_height = 0
            for j in equ.get_equ_id_list():
                temp = equ.get_equ_by_id(j)
                if temp.品质 == '神话':
                    if self.装备选择状态[j] == 1 or temp.名称 in self.self_selects:
                        self.神话属性图片[num].move(
                            int(width / 7 * (count1 % 7 + 0.42)),
                            int(height / 5.2 * (count2 + 0.05)) - 3)
                        for i in range(4):
                            self.神话属性选项[num * 4 + i].move(
                                int(width / 7 * (count1 % 7) + 6),
                                int(height / 5.2 * (count2 + 0.05)) - 3 +
                                i * 22 + 32)
                        count1 += 1
                        if count1 % 7 == 0:
                            count2 += 1
                        page4_height += 1
                    else:
                        self.神话属性图片[num].move(-1000, -1000)
                        for i in range(4):
                            self.神话属性选项[num * 4 + i].move(-1000, -1000)
                    num += 1
            page4_height = max(ceil(page4_height / 7) * 130, height)
            self.main_frame4.setMinimumSize(width, page4_height)
        if index == 4:
            self.自选计算(1)

    def 神话数量判断(self, x=0):
        count = 0
        for j in equ.get_equ_id_list():
            if equ.get_equ_by_id(j).品质 == '神话':
                if self.装备选择状态[j] == 1:
                    count += 1
        if x == 0:
            return count == 0
        else:
            return count

    def 站街面板修正(self, 属性, 输入面板, x=0, append=True):
        i = ['智力', '体力', '精神'].index(属性.类型)
        修正前面板 = int(属性.站街系数)
        修正后面板 = 输入面板 - 修正前面板
        if append:
            修正面板 = to_int(self.属性设置输入[i][15 + x].text(), 0)
            修正后面板 += 修正面板
        self.属性设置输入[i][15 + x].setText(str(int(修正后面板)))

    def exports_property(self, property):
        num = 0
        for skill in property.技能表.values():
            skill.等级 = skill.基础等级 + int(self.等级调整[num].currentData())
            skill.是否启用 = self.次数输入[num].currentIndex()
            num += 1

        property.排行系数 = self.排行参数.currentIndex()
        # print(self.排行选项[0].currentText())
        # print(self.排行选项[0].currentData())
        property.C力智 = int(''.join(
            filter(str.isdigit, self.排行选项[0].currentText())))
        property.C三攻 = int(''.join(
            filter(str.isdigit, self.排行选项[1].currentText())))
        property.排行类型 = self.排行选项[2].currentData()

        if self.排行选项[3].currentIndex() == 0:
            pass
        elif self.排行选项[3].currentIndex() == 1:
            property.系统奶系数 = 1.35
            property.系统奶基数 = 7664
        elif self.排行选项[3].currentIndex() == 2:
            property.系统奶系数 = 2.31
            property.系统奶基数 = 4581

        if self.初始属性.技能表['三次觉醒'].是否启用:
            if self.觉醒选择状态 == 1:
                property.技能表['三次觉醒'].关联技能 = [property.技能表['一次觉醒'].名称]
            elif self.觉醒选择状态 == 2:
                property.技能表['三次觉醒'].关联技能 = [property.技能表['二次觉醒'].名称]

        count = 0
        for i in equ.get_equ_list():
            if i.品质 == '神话':
                i.属性1选择_BUFF = self.神话属性选项[count * 4 + 0].currentIndex()
                i.属性2选择_BUFF = self.神话属性选项[count * 4 + 1].currentIndex()
                i.属性3选择_BUFF = self.神话属性选项[count * 4 + 2].currentIndex()
                i.属性4选择_BUFF = self.神话属性选项[count * 4 + 3].currentIndex()
                count += 1

        property.护石栏 = [i.currentIndex() for i in self.护石栏]

        if self.护石第一栏.currentData() != '无':
            property.护石第一栏 = self.护石第一栏.currentData()

        if self.护石第二栏.currentData() != '无':
            property.护石第二栏 = self.护石第二栏.currentData()

        if self.护石第三栏.currentData() != '无':
            property.护石第三栏 = self.护石第三栏.currentData()

    def 换装计算(self, AWAKE: 辅助角色属性 = None) -> 辅助角色属性:
        if not self.登记启用:
            return None
        if AWAKE is None:
            AWAKE = self.角色属性A

        装备 = store.clone("/{type}/data/register/equips", self.self_selects)
        装备打造 = store.clone("/{type}/data/register/amplifies", [-1] * 12)
        奥兹玛选择状态 = store.clone("/{type}/data/register/ozma", [0] * 25)
        希洛克选择状态 = store.clone("/{type}/data/register/siroco", [0] * 15)
        黑鸦词条 = store.clone("/{type}/data/register/black_purgatory",
                           [[0] * 4] * 4)
        武器融合选项 = store.clone("/{type}/data/register/weapon_fusion", [0] * 4)
        站街面板 = store.get("/{type}/data/register/display_power")

        BUFF = deepcopy(self.初始属性)

        for i in range(len(装备)):
            if 装备[i] == '无':
                装备[i] = self.self_selects[i]
            if 装备打造[i] == -1:
                装备打造[i] = self.装备打造选项[i + 12].currentIndex()

        for i in range(4):
            if 黑鸦词条[i][0] == 0 or 黑鸦词条[i][1] == 0:
                黑鸦词条[i] = deepcopy(AWAKE.黑鸦词条[i])
                黑鸦词条[i][0] == 2

        BUFF.黑鸦词条 = 黑鸦词条
        if 希洛克选择状态 is None or len(希洛克选择状态) == 0 or sum(希洛克选择状态) == 0:
            希洛克选择状态 = self.希洛克选择状态
        BUFF.希洛克选择状态 = 希洛克选择状态

        if 奥兹玛选择状态 is None or len(奥兹玛选择状态) == 0 or sum(奥兹玛选择状态) == 0:
            奥兹玛选择状态 = self.奥兹玛选择状态
        BUFF.奥兹玛选择状态 = 奥兹玛选择状态
        self.登记希洛克 = 希洛克选择状态
        self.登记奥兹玛 = 奥兹玛选择状态
        if 武器融合选项[0] == 0:
            武器融合选项[0] = AWAKE.残香词条[0]
            武器融合选项[1] = AWAKE.残香词条[1]

        if 武器融合选项[2] == 0:
            武器融合选项[2] = AWAKE.残香词条[2]
            武器融合选项[3] = AWAKE.残香词条[3]
        BUFF.希洛克武器词条 = 2
        BUFF.残香词条 = 武器融合选项

        self.exports_property(BUFF)

        self.辟邪玉属性计算(BUFF)

        if sum(希洛克选择状态) == 3:
            BUFF.武器词条触发 = 1

        for i in range(len(self.复选框列表)):
            if self.复选框列表[i].isChecked():
                选项设置列表[i].适用效果(BUFF)

        称号列表[self.称号.currentIndex()].城镇属性_BUFF(BUFF)
        if BUFF.称号触发:
            称号列表[self.称号.currentIndex()].触发属性(BUFF)

        宠物列表[self.宠物.currentIndex()].城镇属性_BUFF(BUFF)

        for i in range(12):
            BUFF.是否增幅[i] = 1
            BUFF.强化等级[i] = 装备打造[i]
            BUFF.改造等级[i] = 装备打造[i]
        BUFF.武器锻造等级 = self.装备打造选项[36].currentIndex()
        BUFF.类型 = self.装备打造选项[37].currentData()

        self.是否计算 = 1

        self.基础属性(BUFF)

        BUFF.穿戴装备(装备)

        if 站街面板 is not None:
            站街属性 = deepcopy(BUFF)

            站街属性.排行系数 = 1
            站街属性.装备属性计算()

            self.站街面板修正(站街属性, 站街面板, 2, False)

        BUFF.预计算()
        AWAKE.替换技能(BUFF.技能表['BUFF'], 'BUFF')
        return BUFF

    def 自选计算(self, 输出=0):
        if 输出 == 0:
            self.保存配置(self.存档位置)
            self.关闭排行窗口()
            self.排行数据.clear()

        self.角色属性A = deepcopy(self.初始属性)

        self.输入属性(self.角色属性A)

        if self.是否计算 != 1:
            self.click_window(1)
            return

        装备 = self.self_selects
        C = self.站街计算(装备)

        B = deepcopy(self.角色属性A)
        B.穿戴装备(装备)
        B.预计算()

        self.换装计算(B)

        if 输出 != 0:
            D = deepcopy(self.初始属性)
            self.输入属性(D)
            D.双装备模式 = 0
            伤害列表 = []
            for i in 辟邪玉列表:
                i.当前值 = i.最大值
                temp = deepcopy(D)
                i.穿戴属性(temp)
                temp.穿戴装备(装备)
                伤害列表.append(temp.BUFF计算(0))

            辟邪玉提升率 = []
            for i in range(1, len(伤害列表)):
                if 伤害列表[0] != 0:
                    辟邪玉提升率.append(伤害列表[i] / 伤害列表[0] - 1)
                else:
                    辟邪玉提升率.append(0)

            提升率排序 = copy(辟邪玉提升率)
            提升率排序.sort(reverse=True)

            for i in range(len(辟邪玉提升率)):
                temp = str('%.2f' % (辟邪玉提升率[i] * 100)) + '%'
                self.辟邪玉提升率2[i].setText(temp)
                x = 提升率排序.index(辟邪玉提升率[i]) / len(辟邪玉提升率) * 10 - 2
                y = 1 / (1 + math.exp(-x))
                if SkinVersion == 'None':
                    颜色 = (0, 0, 0)
                else:
                    颜色 = (int(255 - 80 * y), int(245 - 100 * y),
                          int(0 + 150 * y))
                self.辟邪玉提升率1[i].setStyleSheet(
                    'QLabel{font-size:12px;color:rgb' + str(颜色) + '}')
                self.辟邪玉提升率2[i].setStyleSheet(
                    'QLabel{font-size:12px;color:rgb' + str(颜色) + '}')

        合计力量 = 0
        合计智力 = 0
        合计物攻 = 0
        合计魔攻 = 0
        合计独立 = 0

        总数据 = B.compute()

        for data in 总数据:
            if sum(data) > 0:
                合计力量 += data[3]
                合计智力 += data[4]
                合计物攻 += data[5]
                合计魔攻 += data[6]
                合计独立 += data[7]
        总奶量 = ''
        # tempstr = ''
        if 合计力量 == 合计智力:
            总奶量 += trans('力智') + '+' + str(round(合计力量))
        else:
            总奶量 += '力量+' + str(round(合计力量))
            总奶量 += ',智力+' + str(round(合计智力))

        if 合计物攻 == 合计魔攻 and 合计魔攻 == 合计独立:
            总奶量 += ',' + trans('三攻') + '+' + str(round(合计物攻))
        else:
            总奶量 += ',物攻+' + str(round(合计物攻))
            总奶量 += ',魔攻+' + str(round(合计魔攻))
            总奶量 += ',独立+' + str(round(合计独立))
            # self.总伤害.setText(str(tempstr))

        提升率 = B.提升率计算(总数据)

        x = B.BUFF面板()
        y = B.一觉面板()
        self.角色属性B = deepcopy(B)
        tempstr = self.装备描述_BUFF计算(B)
        图片列表 = self.获取装备图片(装备)
        for i in range(12):
            self.图片显示[i].setToolTip(tempstr[i])
            self.图片显示[i].setMovie(图片列表[i])

        self.面板显示[0].setText(trans('站街') + ':' + str(int(C.系数数值站街())))
        self.面板显示[1].setText('')
        self.面板显示[3].setText(trans('力量') + ':' + str(x[1]))
        self.面板显示[4].setText(trans('智力') + ':' + str(x[2]))
        self.面板显示[5].setText(trans('物攻') + ':' + str(x[3]))
        self.面板显示[6].setText(trans('魔攻') + ':' + str(x[4]))
        self.面板显示[7].setText(trans('独立') + ':' + str(x[5]))

        self.面板显示[9].setText(trans('力量') + ':' + str(y[1]))
        self.面板显示[10].setText(trans('智力') + ':' + str(y[2]))

        skill_buff = B.技能表['BUFF']
        skill_awake = B.技能表['一次觉醒']

        tempstr = []
        tempstr.append(
            trans('BUFF力量%') + ' :' + to_percent(skill_buff.BUFF力量per))
        tempstr.append(
            trans('BUFF智力%') + ' :' + to_percent(skill_buff.BUFF智力per))
        tempstr.append(
            trans('BUFF物攻%') + ' :' + to_percent(skill_buff.BUFF物攻per))
        tempstr.append(
            trans('BUFF魔攻%') + ' :' + to_percent(skill_buff.BUFF魔攻per))
        tempstr.append(
            trans('BUFF独立%') + ' :' + to_percent(skill_buff.BUFF独立per))
        tempstr.append(
            trans('一觉力智') + '  :' + str(int(round(skill_awake.一觉力智, 0))))
        tempstr.append(trans('一觉力智%') + ' :' + to_percent(skill_awake.一觉力智per))
        tempstr.append(str(总奶量))

        # if self.角色属性B.希洛克武器词条 == 1:
        #     武器词条最高值 = self.角色属性B.自适应最高值
        #     武器属性A = 武器属性A列表[武器词条最高值[0]]
        #     武器属性B = 武器属性B列表[武器词条最高值[1]]
        #     tempstr.append("属性1:" +"<font style='color:gray'>"+武器属性A.固定属性描述 + '</font>')
        #     if self.角色属性B.武器词条触发 == 1:
        #         tempstr.append("属性2:" +"<font style='color:gray'>"+武器属性B.固定属性描述 + '</font>')

        if self.角色属性B.希洛克武器词条 == 1:
            武器词条最高值 = self.角色属性B.自适应最高值
            武器属性A = 武器属性A列表[武器词条最高值[0]]
            武器属性B = 武器属性B列表[武器词条最高值[1]]
            # tempstr += '<br><br>' + "属性1:" +"<font style='color:gray'>"+武器属性A.固定属性描述 + '</font>,' + 武器属性A.随机属性描述 + str(武器属性A.最大值)+ ('%' if 武器属性A.间隔 / 10 < 1 else '')
            temp = trans("残香") + " <font style='color:gray'>" + trans(
                武器属性A.固定属性描述) + '</font>'
            if self.角色属性B.武器词条触发 == 1:
                # tempstr += "| 属性2:" +"<font style='color:gray'>"+武器属性B.固定属性描述 + '</font>,' + 武器属性B.随机属性描述 + str(武器属性B.最大值)+ ('%' if 武器属性B.间隔 / 10 <br 1 else '')
                temp += " | " + "<font style='color:gray'>" + trans(
                    武器属性B.固定属性描述) + '</font>'
            tempstr.append(temp)

        if self.角色属性B.黑鸦词条[0][0] == 1 or self.角色属性B.黑鸦词条[1][
                0] == 1 or self.角色属性B.黑鸦词条[2][0] == 1 or self.角色属性B.黑鸦词条[3][
                    0] == 1:
            temp = trans("黑鸦")
            if self.角色属性B.黑鸦词条[0][0] == 1:
                if self.角色属性B.武器变换属性自适应 > 0:
                    黑鸦武器 = 武器变换属性列表[self.角色属性B.武器变换属性自适应]
                    temp += " {}:".format(
                        trans('武器')) + "<font style='color:gray'>" + trans(
                            黑鸦武器.固定属性描述) + '</font>'
                else:
                    temp += " {}:".format(
                        trans('武器')) + "<font style='color:gray'>" + trans(
                            '觉醒') + '</font>'
            if self.角色属性B.黑鸦词条[1][0] == 1:
                黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[0]]
                temp += " {}:".format(
                    trans('戒指')) + "<font style='color:gray'>" + trans(
                        黑鸦.固定属性描述) + '</font>'

            tempstr.append(temp)

            temp = trans("黑鸦")
            if self.角色属性B.黑鸦词条[2][0] == 1:
                黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[1]]
                temp += " {}:".format(
                    trans('辅助')) + "<font style='color:gray'>" + trans(
                        黑鸦.固定属性描述) + '</font>'
            if self.角色属性B.黑鸦词条[3][0] == 1:
                黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[2]]
                temp += " {}:".format(
                    trans('下装')) + "<font style='color:gray'>" + trans(
                        黑鸦.固定属性描述) + '</font>'
            tempstr.append(temp)

        count = len(tempstr)

        for i in range(len(self.词条显示)):
            value = tempstr[i] if i < count else ''
            self.词条显示[i].setText(value)

        for i in self.套装名称显示:
            i.setText('')

            self.套装名称显示[0].setText(trans(装备[11]))
            self.套装名称显示[0].setStyleSheet(
                "QLabel{font-size:12px;color:rgb(255,255,255)}")

        套装名称 = copy(self.角色属性B.套装栏)

        神话所在套装 = []
        for i in range(11):
            if equ.get_equ_by_name(装备[i]).品质 == '神话':
                神话所在套装.append(equ.get_equ_by_name(装备[i]).所属套装)

        套装 = []
        套装件数 = []
        套装属性 = []
        for i in range(len(套装名称)):
            temp = 套装名称[i].split('[')[0]
            if temp not in 套装:
                套装.append(trans(temp))
                套装件数.append([])
                套装属性.append('')
            if len(套装名称[i].split('[')) > 1:
                件数 = 套装名称[i].split('[')[1].split(']')[0]
                套装件数[套装.index(trans(temp))].append(件数)
                套装属性[套装.index(
                    trans(temp)
                )] += '<font size="3" face="宋体"><font color="#78FF1E">' + 套装名称[
                    i] + '</font><br>' + equ.get_suit_by_name(
                        套装名称[i]).装备描述_BUFF(self.角色属性B)[:-4] + '</font><br>'

        self.角色属性B.装备描述 = 1

        sirocos = []

        temp = ''

        for i in range(15):
            if self.希洛克选择状态[i] == 1:
                siroco = SirocoList[i // 3]
                if siroco not in sirocos:
                    siroco.set_character(self.角色属性B)
                    sirocos.append(siroco)
                siroco.fuse(i % 3)
        for siroco in sirocos:
            temp += siroco.compute()
        self.角色属性B.装备描述 = 0
        套装属性.append(temp)

        for i in range(len(希洛克套装)):
            count = self.希洛克选择状态[i * 3 + 0] + \
                self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]
            if count > 1:
                套装.append("{}-{}".format(trans('希洛克'), trans(希洛克套装[i])))
                套装件数.append([count])

        for i in range(len(套装)):
            if len(套装件数[i]) > 0:
                self.套装名称显示[i + 1].setText(
                    trans(套装[i]) + '[' + str(max(套装件数[i])) + ']')
            else:
                self.套装名称显示[i + 1].setText(trans(套装[i]))
            if 套装[i] in 神话所在套装:
                self.套装名称显示[i + 1].setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(226,150,146)}")
            else:
                self.套装名称显示[i + 1].setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(255,255,255)}")
            self.套装名称显示[i + 1].setToolTip(套装属性[i][:-4])

        if len(self.基准值) != 0:
            self.提升率显示.setText(self.对比输出(提升率, self.基准值[0], 1, 1))
        else:
            self.提升率显示.setText(str(round(提升率, 2)) + '%')
        self.自选计算数据 = [提升率, 总数据]

        if 输出 == 0:
            self.排行数据.append(装备 + [0] + 套装 + ['无'])
            self.输出界面(0, 自选计算模式=True)

    def 站街计算(self, 装备名称, 套装名称=None):
        C = deepcopy(self.角色属性A)
        C.穿戴装备(装备名称, 套装名称)
        C.装备属性计算(x=1)
        C.站街计算()
        return C

    def 对比输出(self, A, B, x=0, y=0):
        if B == 0:
            return str(A)
        if x == 0:
            temp = int(A - B)
            if temp == 0:
                if y == 1:
                    return '不变'
                return '-'
            elif temp > 0:
                return '<font face="宋体" color= "#96FF1E">+' + str(
                    temp) + '</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + str(
                    temp) + '</font>'
        else:
            temp = round((A / B - 1) * 100, 2)
            if temp == 0:
                if y == 1:
                    return '不变'
                return '-'
            elif temp > 0:
                return '<font face="宋体" color= "#96FF1E">+' + str(
                    '%.2f' % temp) + '%</font>'
            else:
                return '<font face="宋体" color= "#E52E2E">' + str(
                    '%.2f' % temp) + '%</font>'

    def 输出界面(self, index, name='', 自选计算模式=False):
        装备名称 = []
        套装名称 = []
        百变怪 = self.排行数据[index][-1]
        for i in range(12):
            装备名称.append(self.排行数据[index][i])

        if not 自选计算模式:
            for i in range(13, len(self.排行数据[index]) - 1):
                套装名称.append(self.排行数据[index][i])

        C = self.站街计算(装备名称)

        self.角色属性B = deepcopy(self.角色属性A)
        self.角色属性B.穿戴装备(装备名称, 套装名称)
        # 登记 Start
        self.角色属性B.预计算(自动切装=not 自选计算模式)

        if self.登记启用 and 自选计算模式:
            登记属性 = self.换装计算(self.角色属性B)
            登记装备 = 登记属性.装备栏

            # self.输入属性(self.角色属性B)
            self.角色属性B.切换详情 = '换装详情: <br>' + '<br>'.join(
                [' , '.join(登记装备[i:i + 4]) for i in range(0, len(登记装备), 4)])
        # 登记 end

        # 最大输出界面限制
        if len(self.输出窗口列表) >= 10:
            del self.输出窗口列表[0]

        输出窗口 = QWidget()
        输出窗口.setStyleSheet('''QToolTip {
           background-color: black;
           color: white;
           border: 0px
           }''')
        输出窗口.setFixedSize(788, 546)
        pox_y = 18
        pox_y2 = 11
        temp = ''
        if name == '':
            temp += trans('详细数据') + ' 仅供参考 带节奏死个' + ' ' + get_mac_address()
        else:
            temp += name
        # temp += '（最多显示前18个技能）'+"装备版本:"+self.角色属性A.版本 + " 增幅版本:" + self.角色属性A.增幅版本
        输出窗口.setWindowTitle(temp)
        输出窗口.setWindowIcon(self.icon)
        QLabel(输出窗口).setPixmap(self.输出背景图片)
        人物 = QLabel(输出窗口)
        图片 = QPixmap('./ResourceFiles/' + self.角色属性A.实际名称 + "/人物.png")
        人物.setPixmap(图片)
        人物.move(90 + int(45 - 图片.width() / 2), 40 - pox_y2)
        人物.resize(90, 90)
        人物.setAlignment(Qt.AlignTop)

        y = self.角色属性B.一觉面板()
        x = self.角色属性B.BUFF面板()

        面板显示 = []
        for i in range(11):
            面板显示.append(QLabel(输出窗口))
        面板显示[0].setText(trans('站街') + ':' + str(int(C.系数数值站街())))

        面板显示[3].setText(trans('力量') + ':' + str(x[1]))
        面板显示[4].setText(trans('智力') + ':' + str(x[2]))
        面板显示[5].setText(trans('物攻') + ':' + str(x[3]))
        面板显示[6].setText(trans('魔攻') + ':' + str(x[4]))
        面板显示[7].setText(trans('独立') + ':' + str(x[5]))

        面板显示[9].setText(trans('力量') + ':' + str(y[1]))
        面板显示[10].setText(trans('智力') + ':' + str(y[2]))

        const = 139
        面板显示[0].move(35, const - pox_y2 + 10)

        const += 36
        count = 0
        for i in [2, 3, 4, 5, 6, 7]:
            面板显示[i].move(35, const + count * 18 - pox_y2)
            count += 1

        count = 0
        for i in [8, 9, 10]:
            面板显示[i].move(165, const + count * 18 - pox_y2)
            count += 1

        for i in range(len(面板显示)):
            面板显示[i].setStyleSheet("QLabel{font-size:12px;color:white;}")
            面板显示[i].resize(100, 18)
            面板显示[i].setAlignment(Qt.AlignLeft)

        skill_buff = self.角色属性B.技能表['BUFF']
        skill_awake = self.角色属性B.技能表['一次觉醒']

        tempstr = []
        tempstr.append(
            trans('BUFF力量%') + ' :' + to_percent(skill_buff.BUFF力量per))
        tempstr.append(
            trans('BUFF智力%') + ' :' + to_percent(skill_buff.BUFF智力per))
        tempstr.append(
            trans('BUFF物攻%') + ' :' + to_percent(skill_buff.BUFF物攻per))
        tempstr.append(
            trans('BUFF魔攻%') + ' :' + to_percent(skill_buff.BUFF魔攻per))
        tempstr.append(
            trans('BUFF独立%') + ' :' + to_percent(skill_buff.BUFF独立per))
        tempstr.append(
            trans('一觉力智') + '  :' + str(int(round(skill_awake.一觉力智, 0))))
        tempstr.append(trans('一觉力智%') + ' :' + to_percent(skill_awake.一觉力智per))

        j = 318
        for i in tempstr:
            templab = QLabel(输出窗口)
            templab.setText(i)
            templab.setStyleSheet(
                "QLabel{font-size:12px;color:rgb(104,213,237)}")
            templab.move(20, j - pox_y2)
            templab.resize(305, 18)
            templab.setAlignment(Qt.AlignLeft)
            j += 18

        位置 = 313
        间隔 = 20
        适用称号名称 = QLabel(self.称号.currentData(), 输出窗口)
        适用称号名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用称号名称.move(114, 位置 - pox_y2)
        适用称号名称.resize(150, 18)
        适用称号名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔
        适用称号名称.setToolTip(self.称号描述())

        适用宠物名称 = QLabel(self.宠物.currentData(), 输出窗口)
        适用宠物名称.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用宠物名称.move(114, 位置 - pox_y2)
        适用宠物名称.resize(150, 18)
        适用宠物名称.setAlignment(Qt.AlignCenter)
        位置 += 间隔
        适用宠物名称.setToolTip(self.宠物描述())

        适用中的套装 = QLabel(trans(装备名称[11]), 输出窗口)
        适用中的套装.setStyleSheet("QLabel{font-size:12px;color:rgb(255,255,255)}")
        适用中的套装.move(132, 位置 - pox_y2)
        适用中的套装.resize(132, 18)
        适用中的套装.setAlignment(Qt.AlignCenter)

        神话所在套装 = '无'
        for i in range(11):
            temp = equ.get_equ_by_name(装备名称[i])
            if temp.品质 == '神话':
                神话所在套装 = temp.所属套装

        套装 = []
        套装件数 = []
        套装属性 = []

        套装名称 = copy(self.角色属性B.套装栏)

        for i in range(len(套装名称)):
            temp = 套装名称[i].split('[')[0]
            if temp not in 套装:
                套装.append(temp)
                套装件数.append([])
                套装属性.append('')
            if len(套装名称[i].split('[')) > 1:
                件数 = 套装名称[i].split('[')[1].split(']')[0]
                套装件数[套装.index(temp)].append(件数)
                套装属性[套装.index(
                    temp
                )] += '<font size="3" face="宋体"><font color="#78FF1E">' + 套装名称[
                    i] + '</font><br>' + equ.get_suit_by_name(
                        套装名称[i]).装备描述_BUFF(self.角色属性B)[:-4] + '</font><br>'

        E = deepcopy(self.初始属性)

        sirocos = []

        temp = ''

        for i in range(15):
            if self.希洛克选择状态[i] == 1:
                siroco = SirocoList[i // 3]
                if siroco not in sirocos:
                    siroco.set_character(E)
                    sirocos.append(siroco)
                siroco.fuse(i % 3)
        for siroco in sirocos:
            temp += siroco.compute()

        套装属性.append(temp)

        for i in range(len(希洛克套装)):
            count = self.希洛克选择状态[i * 3 + 0] + \
                self.希洛克选择状态[i * 3 + 1] + self.希洛克选择状态[i * 3 + 2]
            if count > 1:
                套装.append("{}-{}".format(trans('希洛克'), trans(希洛克套装[i])))
                套装件数.append([count])

        for i in range(len(套装)):
            位置 += 间隔
            适用套装名称 = QLabel(输出窗口)
            if len(套装件数[i]) > 0:
                适用套装名称.setText(trans(套装[i]) + '[' + str(max(套装件数[i])) + ']')
            else:
                适用套装名称.setText(trans(套装[i]))
            适用套装名称.move(132, 位置 - pox_y2)
            适用套装名称.resize(132, 18)
            适用套装名称.setAlignment(Qt.AlignCenter)
            if 套装[i] in 神话所在套装:
                适用套装名称.setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(226,150,146)}")
            else:
                适用套装名称.setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(255,255,255)}")
            适用套装名称.setToolTip(套装属性[i][:-4])

        实际技能等级 = []

        技能表 = self.角色属性B.技能表.values()

        for skill in 技能表:
            实际技能等级.append(skill.等级)

        if len(self.基准值) != 0:
            显示模式 = 1
        else:
            显示模式 = 0

        count = 0

        统计详情 = self.角色属性B.compute()

        for 详情 in 统计详情:
            if sum(详情) != 0:
                count += 1

        self.行高 = 30
        if count > 0:
            self.行高 = min(int(440 / count), 30)
        j = -1

        num = 0
        for skill in 技能表:
            if skill.是否启用 and sum(统计详情[num]) != 0:
                j += 1
                每行详情 = []
                for k in range(11):
                    每行详情.append(QLabel(输出窗口))

                # 图片
                每行详情[0].setPixmap(self.技能图片[num])
                每行详情[0].move(302, 50 + j * self.行高 - pox_y)
                每行详情[0].resize(28, min(28, self.行高 - 2))
                # 等级
                每行详情[1].setText('Lv.' + str(实际技能等级[num]))
                每行详情[1].move(337, 50 + j * self.行高 - pox_y)
                每行详情[1].resize(30, min(28, self.行高))

                for k in range(8):
                    详情 = str(int(统计详情[num][k]))
                    if 显示模式 == 1:
                        详情 = self.对比输出(统计详情[num][k], self.基准值[1][num][k])
                    if 详情 == '0' or 详情 == 0:
                        详情 = ''
                    每行详情[k + 2].setText(详情)
                    每行详情[k + 2].move(370 + k * 40, 50 + j * self.行高 - pox_y)
                    每行详情[k + 2].resize(50, min(28, self.行高))
                if hasattr(skill, "适用数值") and skill.适用数值 != 0:
                    每行详情[10].setText("(" + str(round(skill.适用数值)) + ")")
                    每行详情[10].setStyleSheet(
                        "QLabel{font-size:12px;color:rgb(104,213,237)}")
                    每行详情[10].move(710, 50 + j * self.行高 - pox_y)
                    每行详情[10].resize(50, min(28, self.行高))

                for l in range(1, 10):
                    if self.登记启用 and skill.名称 in BUFF影响技能 and 自选计算模式:
                        每行详情[l].setStyleSheet(
                            "QLabel{font-size:12px;color:rgb(255,0,0)}")
                    else:
                        每行详情[l].setStyleSheet(
                            "QLabel{font-size:12px;color:rgb(255,255,255)}")
                    每行详情[l].setAlignment(Qt.AlignCenter)

            num += 1

        合计力量 = 0
        合计智力 = 0
        合计物攻 = 0
        合计魔攻 = 0
        合计独立 = 0

        基准值合计力量 = 0
        基准值合计智力 = 0
        基准值合计物攻 = 0
        基准值合计魔攻 = 0
        基准值合计独立 = 0

        for i in range(len(统计详情)):
            if 显示模式 == 1:
                基准值合计力量 += self.基准值[1][i][3]
                基准值合计智力 += self.基准值[1][i][4]
                基准值合计物攻 += self.基准值[1][i][5]
                基准值合计魔攻 += self.基准值[1][i][6]
                基准值合计独立 += self.基准值[1][i][7]
            合计力量 += 统计详情[i][3]
            合计智力 += 统计详情[i][4]
            合计物攻 += 统计详情[i][5]
            合计魔攻 += 统计详情[i][6]
            合计独立 += 统计详情[i][7]
        tempstr = ''
        if 显示模式 == 1:
            对比力量 = self.对比输出(合计力量, 基准值合计力量, 0, 1)
            对比智力 = self.对比输出(合计智力, 基准值合计智力, 0, 1)
            对比物攻 = self.对比输出(合计物攻, 基准值合计物攻, 0, 1)
            对比魔攻 = self.对比输出(合计魔攻, 基准值合计魔攻, 0, 1)
            对比独立 = self.对比输出(合计独立, 基准值合计独立, 0, 1)
            if 对比力量 == 对比智力:
                tempstr += trans('力智') + 对比力量
            else:
                tempstr += '力量' + 对比力量
                tempstr += ',智力' + 对比智力

            if 对比物攻 == 对比魔攻 and 对比魔攻 == 对比独立:
                tempstr += ',' + trans('三攻') + 对比物攻
            else:
                tempstr += ',物攻' + 对比物攻
                tempstr += ',魔攻' + 对比魔攻
                tempstr += ',独立' + 对比独立
        else:
            if 合计力量 == 合计智力:
                tempstr += trans('力智') + '+' + str(round(合计力量))
            else:
                tempstr += '力量+' + str(round(合计力量))
                tempstr += ',智力+' + str(round(合计智力))

            if 合计物攻 == 合计魔攻 and 合计魔攻 == 合计独立:
                tempstr += ',' + trans('三攻') + '+' + str(round(合计物攻))
            else:
                tempstr += ',物攻+' + str(round(合计物攻))
                tempstr += ',魔攻+' + str(round(合计魔攻))
                tempstr += ',独立+' + str(round(合计独立))
            if self.角色属性B.切换详情 != '无':
                tempstr += '<br><br>' + self.角色属性B.切换详情

        if self.角色属性B.希洛克武器词条 == 1:
            武器词条最高值 = self.角色属性B.自适应最高值
            武器属性A = 武器属性A列表[武器词条最高值[0]]
            武器属性B = 武器属性B列表[武器词条最高值[1]]
            # tempstr += '<br><br>' + "属性1:" +"<font style='color:gray'>"+武器属性A.固定属性描述 + '</font>,' + 武器属性A.随机属性描述 + str(武器属性A.最大值)+ ('%' if 武器属性A.间隔 / 10 < 1 else '')
            tempstr += "<br><br>" + trans("残香") +""+ \
                       "<font style='color:gray'>" + trans(武器属性A.固定属性描述) + '</font>'
            if self.角色属性B.武器词条触发 == 1:
                # tempstr += "| 属性2:" +"<font style='color:gray'>"+武器属性B.固定属性描述 + '</font>,' + 武器属性B.随机属性描述 + str(武器属性B.最大值)+ ('%' if 武器属性B.间隔 / 10 < 1 else '')
                tempstr += " | " + "<font style='color:gray'>" + trans(
                    武器属性B.固定属性描述) + '</font>'

        if self.角色属性B.黑鸦词条[0][0] == 1 or self.角色属性B.黑鸦词条[1][
                0] == 1 or self.角色属性B.黑鸦词条[2][0] == 1 or self.角色属性B.黑鸦词条[3][
                    0] == 1:
            tempstr += "<br><br>" + trans("黑鸦")
            if self.角色属性B.黑鸦词条[0][0] == 1:
                if self.角色属性B.武器变换属性自适应 > 0:
                    黑鸦武器 = 武器变换属性列表[self.角色属性B.武器变换属性自适应]
                    tempstr += " {}:".format(
                        trans('武器')) + "<font style='color:gray'>" + trans(
                            黑鸦武器.固定属性描述) + '</font>'
                else:
                    tempstr += " {}:".format(
                        trans('武器')) + "<font style='color:gray'>" + trans(
                            '觉醒') + '</font>'
            if self.角色属性B.黑鸦词条[1][0] == 1:
                黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[0]]
                tempstr += " {}:".format(
                    trans('戒指')) + "<font style='color:gray'>" + trans(
                        黑鸦.固定属性描述) + '</font>'
            if self.角色属性B.黑鸦词条[2][0] == 1:
                黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[1]]
                tempstr += " {}:".format(
                    trans('辅助')) + "<font style='color:gray'>" + trans(
                        黑鸦.固定属性描述) + '</font>'
            if self.角色属性B.黑鸦词条[3][0] == 1:
                黑鸦 = 装备变换属性列表[self.角色属性B.防具变换属性自适应[2]]
                tempstr += " {}:".format(
                    trans('下装')) + "<font style='color:gray'>" + trans(
                        黑鸦.固定属性描述) + '</font>'

        合计 = QLabel(输出窗口)
        合计.setStyleSheet("QLabel{color:rgb(104,213,237);font-size:15px}")
        合计.setText(tempstr)
        if self.登记启用 and 自选计算模式:
            合计.setStyleSheet("QLabel{color:rgb(104,213,237);font-size:12px}")
        合计.resize(450, 300)
        合计.move(280, 30 + j * self.行高 - pox_y2)
        合计.setAlignment(Qt.AlignCenter)

        初始x = 10
        初始y = 31

        图片列表 = self.获取装备图片(self.排行数据[index])

        提升率 = self.角色属性B.提升率计算(统计详情)

        提升率显示 = QLabel(输出窗口)

        提升率显示.setStyleSheet("QLabel{color:rgb(255,255,255);font-size:25px}")
        if 显示模式 == 1:
            提升率显示.setText(self.对比输出(提升率, self.基准值[0], 1, 1))
        else:
            提升率显示.setText(str(round(提升率, 2)) + '%')
        提升率显示.resize(250, 36)
        提升率显示.move(10, 517 - pox_y2)
        提升率显示.setAlignment(Qt.AlignCenter)

        图片列表 = self.获取装备图片(self.排行数据[index])
        偏移量 = 187
        x坐标 = [
            32, 0, 0, 32, 0, 偏移量, 偏移量 + 32, 偏移量 + 32, 偏移量, 偏移量, 偏移量 + 32, 32
        ]
        y坐标 = [0, 0, 32, 32, 64, 0, 0, 32, 64, 32, 64, 64]

        tempstr = self.装备描述_BUFF计算(self.角色属性B)

        for i in range(12):
            x = 初始x + x坐标[i]
            y = 初始y + y坐标[i] - pox_y2
            装备图标 = QLabel(输出窗口)
            装备图标.setMovie(图片列表[i])
            装备图标.resize(26, 26)
            装备图标.move(x, y)
            装备图标.setAlignment(Qt.AlignCenter)
            装备 = equ.get_equ_by_name(self.角色属性B.装备栏[i])
            if self.角色属性B.装备栏[i] == 百变怪:
                图标遮罩 = QLabel(输出窗口)
                图标遮罩.setStyleSheet("QLabel{background-color:rgba(0,0,0,0.5)}")
                图标遮罩.resize(26, 26)
                图标遮罩.move(x, y)
                图标遮罩.setToolTip(tempstr[i])
            else:
                装备图标.setToolTip(tempstr[i])

        for i in range(12):
            装备 = equ.get_equ_by_name(self.角色属性B.装备栏[i])
            打造状态 = QLabel(输出窗口)
            if 装备.所属套装 != '智慧产物':
                打造状态.setText('+' + str(self.角色属性B.强化等级[i]))
                if self.角色属性B.是否增幅[i] == 1:
                    打造状态.setStyleSheet(
                        "QLabel{color:rgb(228,88,169);font-size:12px;font-weight:Bold}"
                    )
                else:
                    打造状态.setStyleSheet(
                        "QLabel{color:rgb(25,199,234);font-size:12px;font-weight:Bold}"
                    )

            else:
                打造状态.setText('+' + str(self.角色属性B.改造等级[i]))
                打造状态.setStyleSheet(
                    "QLabel{color:rgb(249,141,62);font-size:12px;font-weight:Bold;}"
                )

            打造状态.move(初始x + x坐标[i] + 13, 初始y + y坐标[i] - 8 - pox_y2)

        装备 = equ.get_equ_by_name(self.角色属性B.装备栏[11])
        if 装备.所属套装 != '智慧产物' and self.角色属性B.武器锻造等级 != 0:
            打造状态 = QLabel(输出窗口)
            打造状态.setText('+' + str(self.角色属性B.武器锻造等级))
            打造状态.setStyleSheet(
                "QLabel{color:rgb(232,104,24);font-size:12px;font-weight:Bold}"
            )
            打造状态.move(初始x + x坐标[11] + 13, 初始y + y坐标[11] + 20 - pox_y2)

        if self.登记启用 and 自选计算模式:
            # 登记装备图表显示
            偏移量 = 80
            x坐标 = [
                32, 0, 0, 32, 0, 偏移量, 偏移量 + 32, 偏移量 + 32, 偏移量, 偏移量, 偏移量 + 32,
                32
            ]
            y坐标 = [0, 0, 32, 32, 64, 0, 0, 32, 64, 32, 64, 64]
            图片列表2 = self.获取装备图片(登记装备, self.登记希洛克, self.登记奥兹玛)

            def compare(i):
                if 登记装备[i] != self.排行数据[index][i]:
                    return False
                if i == 2:
                    if self.角色属性A.黑鸦词条[3][0] != self.角色属性B.黑鸦词条[3][0]:
                        return False
                elif i == 7:
                    if self.角色属性A.黑鸦词条[1][0] != self.角色属性B.黑鸦词条[1][0]:
                        return False
                elif i == 9:
                    if self.角色属性A.黑鸦词条[2][0] != self.角色属性B.黑鸦词条[2][0]:
                        return False
                elif i == 11:
                    if self.角色属性A.黑鸦词条[0][0] != self.角色属性B.黑鸦词条[0][0]:
                        return False
                return True

            for i in range(len(登记装备)):
                x = 初始x + x坐标[i] + 600
                y = 初始y + y坐标[i] - pox_y2 + 200
                装备图标 = QLabel(输出窗口)
                装备图标.setMovie(图片列表2[i])
                装备图标.resize(26, 26)
                装备图标.move(x, y)
                装备图标.setAlignment(Qt.AlignCenter)

                if compare(i):
                    图标遮罩 = QLabel(输出窗口)
                    图标遮罩.setStyleSheet(
                        "QLabel{background-color:rgba(0,0,0,0.8)}")
                    图标遮罩.resize(26, 26)
                    图标遮罩.move(x, y)
        try:
            self.exports_store()
            更新人物名望()
            # TODO: 重新布局
            总名望 = store.get("/fame/temp_result")
            名望详情 = store.get("/fame/temp_result/detail")
            if 总名望 > 0:
                bmi = pow(提升率, 2) / 1e5 / pow((总名望 / 1e4 - 0.5), 3)
                templabel = QLabel(输出窗口)
                templabel.setText("名望 {}({})".format(str(总名望),
                                                     str(round(bmi, 2))))
                templabel.setStyleSheet(
                    "QLabel{font-size:12px;color:rgb(255,255,255)}")
                templabel.move(130, 110)
                templabel.resize(100, 42)
                templabel.setToolTip(
                    '系数计算公式:bmi = pow(提升率,2) / 1e5   / pow((总名望 / 1e4 - 0.5), 3)<br>'
                    + str(名望详情))

        except Exception as e:
            logger.error(e)

        输出显示 = MainWindow(输出窗口)
        self.输出窗口列表.append(输出显示)
        输出显示.show()

    def 辟邪玉显示(self, x=0):
        temp = ''
        num = 0
        for i in range(4):
            k = self.辟邪玉选择[i].currentIndex()
            if k > 0:
                temp += trans('{$name}$value<br>',
                              name=辟邪玉列表[k].简称,
                              value=self.辟邪玉数值[i].currentData())
                num += 1
        辟邪玉颜色 = 颜色[{4: '史诗', 3: '传说', 2: '神器', 1: '稀有'}.get(num, '稀有')]
        if x == 0:
            return 辟邪玉颜色
        else:
            if num == 0:
                return ''
            else:
                return trans('<font color="$color">{辟邪玉}:<br>$effect</font>',
                             color=辟邪玉颜色,
                             effect=temp[:-4])

    def 装备描述_BUFF计算(self, property):
        tempstr = []
        希洛克选择状态 = [0] * 3
        for i in range(len(self.希洛克选择状态)):
            希洛克选择状态[i % 3] += self.希洛克选择状态[i]
        奥兹玛选择状态 = [0] * 5
        for i in range(len(self.奥兹玛选择状态)):
            奥兹玛选择状态[i % 5] += self.奥兹玛选择状态[i]
        for i in range(12):
            装备 = equ.get_equ_by_name(property.装备栏[i])
            tempstr.append(
                trans(
                    '<font size="3" face="宋体"><font color="$color"> {$name}</font><br>',
                    color=颜色[装备.品质],
                    name=装备.名称))
            if 装备.所属套装 != '无':
                if 装备.所属套装 != '智慧产物':
                    y = ' ' + 装备.所属套装
                else:
                    try:
                        y = ' ' + 装备.所属套装2
                    except Exception as e:
                        y = ' '
            else:
                y = ' '
            if i == 11:
                y += ' ' + 装备.类型

            tempstr[i] += trans('{Lv}$level {$rarity} {$name}',
                                level=装备.等级,
                                rarity=装备.品质,
                                name=y)
            if i < 5:
                x = property.防具精通计算(i)
                tempstr[i] += trans('<br>{防具精通}: ')
                for n in property.防具精通属性:
                    if n != '体力':
                        tempstr[i] += n + ' +' + str(2 * x) + ' '
                    else:
                        tempstr[i] += n + ' +' + str(x) + ' '

            if 装备.所属套装 != '智慧产物':
                if property.强化等级[i] != 0:
                    if i in [9, 10]:
                        tempstr[i] += trans(
                            '<br><font color="#68D5ED">+$value {强化}：',
                            value=property.强化等级[i])
                        tempstr[i] += trans('{四维} +$value </font>',
                                            value=左右计算(100, 装备.品质,
                                                       property.强化等级[i]))

                if property.武器锻造等级 != 0:
                    if i == 11:
                        tempstr[i] += trans(
                            '<br><font color="#B36BFF">+$value  {锻造}  ',
                            value=property.武器锻造等级)
                        tempstr[i] += trans("{四维} +$value </font>",
                                            value=锻造四维(装备.等级, 装备.品质,
                                                       property.武器锻造等级))

                if property.是否增幅[i] == 1:
                    value = 增幅计算(装备.等级, 装备.品质, property.强化等级[i], property.增幅版本)
                    if tempstr[i] != '':
                        tempstr[i] += '<br>'
                    tempstr[i] += trans('<font color="#FF00FF">+$value {增幅}：',
                                        value=property.强化等级[i])
                    if '体力' in property.类型:
                        tempstr[i] += trans('{异次元体力} +$value</font>',
                                            value=value)
                    elif '精神' in property.类型:
                        tempstr[i] += trans('{异次元精神} +$value</font>',
                                            value=value)
                    elif '智力' in property.类型:
                        tempstr[i] += trans('{异次元智力} +$value</font>',
                                            value=value)

            if tempstr[i] != '':
                tempstr[i] += '<br>'
            if 装备.所属套装 != '智慧产物':
                weapon_index = property.黑鸦词条[0][0]
                ring_index = property.黑鸦词条[1][0]
                left_index = property.黑鸦词条[2][0]
                pants_index = property.黑鸦词条[3][0]

                # 下装
                if i == 2 and pants_index != 0:
                    tempstr[i] += 装备.装备描述_变换属性_BUFF(property)
                    if pants_index == 1:
                        tempstr[i] += self.黑鸦属性描述(property.防具变换属性自适应[2], 0, 1)
                    else:
                        tempstr[i] += self.黑鸦属性描述(property.黑鸦词条[3][1],
                                                  property.黑鸦词条[3][2], 1)

                # 戒指
                elif i == 7 and ring_index != 0:
                    tempstr[i] += 装备.装备描述_变换属性_BUFF(property)
                    if ring_index == 1:
                        tempstr[i] += self.黑鸦属性描述(property.防具变换属性自适应[0], 0, 1)
                    else:
                        tempstr[i] += self.黑鸦属性描述(property.黑鸦词条[1][1], 0, 1)

                # 辅助装备
                elif i == 9 and left_index != 0:
                    tempstr[i] += 装备.装备描述_变换属性_BUFF(property)
                    if left_index == 1:
                        tempstr[i] += self.黑鸦属性描述(property.防具变换属性自适应[1], 0, 1)
                    else:
                        tempstr[i] += self.黑鸦属性描述(property.黑鸦词条[2][1],
                                                  property.黑鸦词条[2][2], 1)

                # 武器
                elif i == 11 and weapon_index != 0:

                    tempstr[i] += 装备.装备描述_变换属性_BUFF(property)

                    # 当遴选为觉醒时
                    add_awake = weapon_index == 3 or (weapon_index == 1 and
                                                      property.武器变换属性自适应 == 0)

                    # 自选觉醒
                    if add_awake:
                        tempstr[i] += 'Lv50 技能等级+2<br>'
                        tempstr[i] += 'Lv85 技能等级+2<br>'
                        tempstr[i] += 'Lv100 技能等级+2<br>'

                    if weapon_index > 0:
                        if weapon_index == 1 and property.武器变换属性自适应 != 0:
                            tempstr[i] += self.黑鸦属性描述(property.武器变换属性自适应, 0)
                        elif weapon_index == 2:
                            tempstr[i] += self.黑鸦属性描述(property.黑鸦词条[0][0],
                                                      property.黑鸦词条[0][2])

                        if 装备.名称 == '世界树之精灵':
                            tempstr[i] += 'Lv50 技能等级+2<br>'

                else:
                    tempstr[i] += 装备.装备描述_BUFF(property)

            property.装备描述 = 1

            部位 = 部位列表[i]

            希洛克title = trans('<font color="#00A2E8">{希洛克融合属性}：</font><br>')

            if 希洛克选择状态[0] == 1 and 部位 == '下装':
                # tempstr[i]+='<br>'
                tempstr[i] += 希洛克title
                tempstr[i] += BUFF增加(property, BUFF力智per=1.03)
            elif 希洛克选择状态[1] == 1 and 部位 == '戒指':
                # tempstr[i]+='<br>'
                tempstr[i] += 希洛克title
                tempstr[i] += 觉醒增加(property, 一觉力智per=1.03)
            elif 希洛克选择状态[2] == 1 and 部位 == '辅助装备':
                # tempstr[i]+='<br>'
                tempstr[i] += 希洛克title
                tempstr[i] += 被动增加(property, 被动进图加成=80)
            if self.角色属性B.希洛克武器词条 > 0 and i == 11:

                # tempstr[i]+='<br>'
                tempstr[i] += 希洛克title

                if self.角色属性B.希洛克武器词条 == 1:
                    武器词条最高值 = self.角色属性B.自适应最高值
                    武器属性A = 武器属性A列表[武器词条最高值[0]]
                    武器属性B = 武器属性B列表[武器词条最高值[1]]
                elif self.角色属性B.希洛克武器词条 == 2:
                    武器属性A = 武器属性A列表[self.武器融合属性A.currentIndex()]
                    武器属性B = 武器属性B列表[self.武器融合属性B.currentIndex()]

                tempstr[i] += trans("{属性1}：<font style='color:gray'>$a</font>,$b$c$d<br>",\
                a = 武器属性A.固定属性描述,\
                b = 武器属性A.随机属性描述,\
                c = 武器属性A.最大值,\
                d = '%' if 武器属性A.间隔 / 10 < 1 else '')
                if self.角色属性B.武器词条触发 == 1:
                    tempstr[i] += trans("{属性2}：<font style='color:gray'>$a</font>,$b$c$d<br>",\
                    a = 武器属性B.固定属性描述,\
                    b = 武器属性B.随机属性描述,\
                    c = 武器属性B.最大值,\
                    d = '%' if 武器属性B.间隔 / 10 < 1 else '')

            if 部位 in 奥兹玛部位列表:
                index = 奥兹玛部位列表.index(部位)
                cur = -1
                for j in range(0, 5):
                    if self.奥兹玛选择状态[j * 5 + index] == 1:
                        cur = j
                        break
                if cur > 0:
                    tempstr[i] += trans(
                        '<font color="#00A2E8">{奥兹玛融合属性}：</font><br>')
                    tempstr[i] += str(OzmaList[cur](property))
            property.装备描述 = 0

            tempstr[i] = tooltip_trim(tempstr[i])
            tempstr[i] += '</font>'

        return tempstr

    def 黑鸦属性描述(self, index, value=0, x=0):
        变换属性 = 武器变换属性列表[index] if x == 0 else 装备变换属性列表[index]
        value = 变换属性.最大值 - 变换属性.间隔 * value
        if value // 10 < 1:
            value = str(value) + "%"
        return "<font style='color:gray'>{},</font>,{}{}<br>".format(
            变换属性.固定属性描述, 变换属性.随机属性描述, value)

    def 黑鸦属性计算(self, 属性: 辅助角色属性):
        for i in range(4):
            if self.黑鸦词条选项[i][0].currentIndex() == 2:
                if i == 0:
                    武器属性 = 武器变换属性列表[self.黑鸦词条选项[i][1].currentIndex()]
                    武器属性数值 = self.黑鸦词条选项[i][3].currentText().replace('%', '')
                    武器属性.当前值 = int(武器属性数值 if 武器属性数值 != '' else 0)
                    武器属性.变换属性(属性)
                else:
                    装备属性 = 装备变换属性列表[self.黑鸦词条选项[i][1].currentIndex()]
                    装备属性数值 = self.黑鸦词条选项[i][3].currentText().replace('%', '')
                    装备属性.当前值 = int(装备属性数值 if 装备属性数值 != '' else 0)
                    装备属性.变换属性(属性)

    def 输入属性(self, 属性: 辅助角色属性, x=0):

        self.exports_property(属性)

        if x == 0:
            self.辟邪玉属性计算(属性)

        if sum(self.希洛克选择状态) == 3:
            属性.武器词条触发 = 1

        属性.希洛克武器词条 = self.希洛克武器选择.currentIndex()

        if 属性.希洛克武器词条 == 2:
            属性.残香词条 = [
                self.武器融合属性A.currentIndex(),
                self.武器融合属性A2.currentIndex(),
                self.武器融合属性B.currentIndex(),
                self.武器融合属性B2.currentIndex()
            ]

        for i in range(len(self.复选框列表)):
            if self.复选框列表[i].isChecked():
                选项设置列表[i].适用效果(属性)

        称号列表[self.称号.currentIndex()].城镇属性_BUFF(属性)
        if 属性.称号触发:
            称号列表[self.称号.currentIndex()].触发属性(属性)

        宠物列表[self.宠物.currentIndex()].城镇属性_BUFF(属性)

        for i in range(12):
            属性.是否增幅[i] = self.装备打造选项[i].currentIndex()
            属性.强化等级[i] = self.装备打造选项[i + 12].currentIndex()
            属性.改造等级[i] = self.装备打造选项[i + 24].currentIndex()
        属性.武器锻造等级 = self.装备打造选项[36].currentIndex()
        属性.类型 = self.装备打造选项[37].currentData()
        self.是否计算 = 1

        if self.切装模式选项.isChecked() and self.计算模式选择.currentIndex(
        ) != 2 and 属性.技能表['BUFF'].是否启用 and 属性.技能表['一次觉醒'].是否启用:
            属性.双装备模式 = 1
            pass

        黑鸦词条 = []
        for i in range(4):
            temp = [
                self.黑鸦词条选项[i][0].currentIndex(),
                self.黑鸦词条选项[i][1].currentIndex(),
                self.黑鸦词条选项[i][3].currentIndex(),
            ]
            黑鸦词条.append(temp)
        属性.黑鸦词条 = 黑鸦词条

        属性.希洛克选择状态 = self.希洛克选择状态

        属性.奥兹玛选择状态 = self.奥兹玛选择状态

        属性.觉醒择优系数 = float(self.觉醒择优系数.currentText())

        self.基础属性(属性)

    def 技能加成判断(self, name, 属性):
        if name == 'Lv1-30(主动)Lv+1':
            属性.技能等级加成('主动', 1, 30, 1)
            return
        if name == 'Lv1-50(主动)Lv+1':
            属性.技能等级加成('主动', 1, 50, 1)
            return
        if name == 'Lv1-35(主动)Lv+1':
            属性.技能等级加成('主动', 1, 35, 1)
            return
        if name == 'Lv30-50(主动)Lv+1':
            属性.技能等级加成('主动', 30, 50, 1)
            return
        if name == 'Lv1-30(所有)Lv+1':
            属性.技能等级加成('所有', 1, 30, 1)
            return
        if name == 'Lv1-50(所有)Lv+1':
            属性.技能等级加成('所有', 1, 50, 1)
            return
        if name == 'Lv1-20(所有)Lv+1':
            属性.技能等级加成('所有', 1, 20, 1)
            return
        if name == 'Lv20-30(所有)Lv+1':
            属性.技能等级加成('所有', 20, 30, 1)
            return
        if name == 'Lv1-80(所有)Lv+1':
            属性.技能等级加成('所有', 1, 80, 1)
            return

        if name == '一觉Lv+1':
            属性.一觉Lv += 1
            return
        if name == '一觉Lv+2':
            属性.一觉Lv += 2
            return
        if name == 'BUFFLv+1':
            属性.BUFFLv += 1
            return
        if name == 'BUFFLv+2':
            属性.BUFFLv += 2
            return
        if name == 'BUFFLv+3':
            属性.BUFFLv += 3
            return
        if name == 'BUFFLv+4':
            属性.BUFFLv += 4
            return
        for skill in 属性.技能表.values():
            if name == skill.名称 + 'Lv+1':
                skill.等级加成(1)
                return
        if name == 'BUFF力智+3%':
            属性.BUFF增加(BUFF力量per=1.03, BUFF智力per=1.03)
        if name == 'BUFF三攻+3%':
            属性.BUFF增加(BUFF物攻per=1.03, BUFF魔攻per=1.03, BUFF独立per=1.03)
        if name == 'BUFF力智、三攻+3%':
            属性.BUFF增加(BUFF力量per=1.03,
                      BUFF智力per=1.03,
                      BUFF物攻per=1.03,
                      BUFF魔攻per=1.03,
                      BUFF独立per=1.03)

    def 基础属性(self, 属性):
        for i in range(3):
            for j in range(16):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except Exception as e:
                        logger.error(e)
                        QMessageBox.information(
                            self, "错误", self.行名称[j + 17 if i > 2 else j] +
                            ":" + self.列名称[i] + "  输入格式错误,已重置为空")
                        self.属性设置输入[i][j].setText('')
        for i in range(3, 9):
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    try:
                        float(self.属性设置输入[i][j].text())
                    except Exception as e:
                        logger.error(e)
                        QMessageBox.information(
                            self, "错误", self.行名称[j + 17 if i > 2 else j] +
                            ":" + self.列名称[i] + "  输入格式错误,已重置为空")
                        self.属性设置输入[i][j].setText('')

        temp = []
        for j in range(len(self.属性设置输入[9])):

            if self.属性设置输入[9][j].text() != '' and j in [1, 2, 5]:
                try:
                    temp.append(float(self.属性设置输入[9][j].text()) / 100)

                    if temp[-1] > 1 or temp[-1] < -.2:
                        QMessageBox.information(
                            self, "错误",
                            self.修正列表名称[j] + " 输入数值超出[-20,100],已重置为空")
                        temp[-1] = 0.0
                        self.属性设置输入[9][j].setText('')
                except Exception as e:
                    temp.append(0.0)
                    QMessageBox.information(self, "错误",
                                            self.修正列表名称[j] + " 输入格式错误,已重置为空")
                    self.属性设置输入[9][j].setText('')
            elif self.属性设置输入[9][j].text() != '' and j in [0, 3, 4, 6]:
                try:
                    temp.append(int(self.属性设置输入[9][j].text()))
                except Exception as e:
                    temp.append(0.0)
                    QMessageBox.information(self, "错误",
                                            self.修正列表名称[j] + " 输入格式错误,已重置为空")
                    self.属性设置输入[9][j].setText('')
            else:
                temp.append(0.0)
        # 神话补正
        if 属性.类型 == '智力':
            属性.转职被动智力 += int(temp[0])
            属性.一觉被动力智 += int(temp[4])
        else:
            属性.守护恩赐体精 += int(temp[0])
            属性.信念光环体精 += int(temp[4])

        属性.BUFF力量per *= 1 + temp[1]
        属性.BUFF智力per *= 1 + temp[1]
        属性.BUFF物攻per *= 1 + temp[2]
        属性.BUFF魔攻per *= 1 + temp[2]
        属性.BUFF独立per *= 1 + temp[2]
        属性.转职被动Lv += int(temp[3])
        属性.一觉力智per *= 1 + temp[5]
        属性.一觉力智 += int(temp[6])
        for i in [0, 3, 6]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 3 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 0 and j in [1, 9, 16]:
                        属性.进图智力 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.智力 += int(self.属性设置输入[i][j].text())
            for j in range(17, 19):
                if self.属性设置输入[i][j].text() != '':
                    属性.BUFF补正力智 += int(self.属性设置输入[i][j].text())
        for i in [1, 4, 7]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 4 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 1 and j in [1, 9, 16]:
                        属性.进图体力 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.体力 += int(self.属性设置输入[i][j].text())
            for j in range(17, 19):
                if self.属性设置输入[i][j].text() != '':
                    属性.BUFF补正体力 += int(self.属性设置输入[i][j].text())
        for i in [2, 5, 8]:
            for j in range(17):
                if self.属性设置输入[i][j].text() != '':
                    if i == 5 and j == 12:
                        属性.BUFF适用面板 += int(self.属性设置输入[i][j].text())
                        continue
                    if i == 2 and j in [1, 9, 16]:
                        属性.进图精神 += int(self.属性设置输入[i][j].text())
                    else:
                        属性.精神 += int(self.属性设置输入[i][j].text())
            for j in range(17, 19):
                if self.属性设置输入[i][j].text() != '':
                    属性.BUFF补正精神 += int(self.属性设置输入[i][j].text())
        for i in self.技能设置输入:
            self.技能加成判断(i.currentData(), 属性)
        属性.护石计算()
