# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1269, 769)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/window_icon/pics/quas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(36, 42, 46);\n"
"border-color: rgb(186, 189, 182);\n"
"color: rgb(186, 189, 182);\n"
"gridline-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(92, 53, 102);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);\n"
"font: 25 10pt \"URW Bookman\";")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(250, 0, 1011, 561))
        self.tabWidget.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.All = QtWidgets.QWidget()
        self.All.setStyleSheet("background-color: rgb(26, 36, 39);")
        self.All.setObjectName("All")
        self.import_pic = QtWidgets.QPushButton(self.All)
        self.import_pic.setGeometry(QtCore.QRect(240, 190, 101, 25))
        self.import_pic.setObjectName("import_pic")
        self.picture_main = QtWidgets.QLabel(self.All)
        self.picture_main.setGeometry(QtCore.QRect(0, 20, 591, 381))
        self.picture_main.setStyleSheet("")
        self.picture_main.setText("")
        self.picture_main.setObjectName("picture_main")
        self.line = QtWidgets.QFrame(self.All)
        self.line.setGeometry(QtCore.QRect(600, 10, 5, 391))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.All)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 121, 17))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.All)
        self.label_6.setGeometry(QtCore.QRect(770, 0, 51, 17))
        self.label_6.setObjectName("label_6")
        self.line_4 = QtWidgets.QFrame(self.All)
        self.line_4.setGeometry(QtCore.QRect(90, 10, 895, 5))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.All)
        self.line_5.setGeometry(QtCore.QRect(980, 10, 5, 521))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_3 = QtWidgets.QFrame(self.All)
        self.line_3.setGeometry(QtCore.QRect(0, 10, 5, 401))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(self.All)
        self.line_2.setGeometry(QtCore.QRect(0, 410, 601, 5))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.filterpic1 = QtWidgets.QLabel(self.All)
        self.filterpic1.setGeometry(QtCore.QRect(611, 21, 172, 102))
        self.filterpic1.setMinimumSize(QtCore.QSize(172, 102))
        self.filterpic1.setMaximumSize(QtCore.QSize(172, 102))
        self.filterpic1.setStyleSheet("")
        self.filterpic1.setText("")
        self.filterpic1.setObjectName("filterpic1")
        self.filterpic2 = QtWidgets.QLabel(self.All)
        self.filterpic2.setGeometry(QtCore.QRect(789, 21, 172, 102))
        self.filterpic2.setMinimumSize(QtCore.QSize(172, 102))
        self.filterpic2.setMaximumSize(QtCore.QSize(172, 102))
        self.filterpic2.setStyleSheet("")
        self.filterpic2.setText("")
        self.filterpic2.setObjectName("filterpic2")
        self.filterpicname1 = QtWidgets.QPushButton(self.All)
        self.filterpicname1.setGeometry(QtCore.QRect(611, 123, 140, 25))
        self.filterpicname1.setMinimumSize(QtCore.QSize(140, 0))
        self.filterpicname1.setMaximumSize(QtCore.QSize(140, 25))
        self.filterpicname1.setMouseTracking(True)
        self.filterpicname1.setStyleSheet("background-color: rgb(41, 4, 4);")
        self.filterpicname1.setCheckable(True)
        self.filterpicname1.setChecked(False)
        self.filterpicname1.setObjectName("filterpicname1")
        self.filter_button_group = QtWidgets.QButtonGroup(MainWindow)
        self.filter_button_group.setObjectName("filter_button_group")
        self.filter_button_group.addButton(self.filterpicname1)
        self.filterpicname2 = QtWidgets.QPushButton(self.All)
        self.filterpicname2.setGeometry(QtCore.QRect(789, 123, 140, 25))
        self.filterpicname2.setMinimumSize(QtCore.QSize(140, 0))
        self.filterpicname2.setMaximumSize(QtCore.QSize(140, 25))
        self.filterpicname2.setMouseTracking(True)
        self.filterpicname2.setStyleSheet("background-color: rgb(41, 4, 4);")
        self.filterpicname2.setCheckable(True)
        self.filterpicname2.setChecked(False)
        self.filterpicname2.setObjectName("filterpicname2")
        self.filter_button_group.addButton(self.filterpicname2)
        self.filterpic3 = QtWidgets.QLabel(self.All)
        self.filterpic3.setGeometry(QtCore.QRect(611, 148, 172, 102))
        self.filterpic3.setMinimumSize(QtCore.QSize(172, 102))
        self.filterpic3.setMaximumSize(QtCore.QSize(172, 102))
        self.filterpic3.setStyleSheet("")
        self.filterpic3.setText("")
        self.filterpic3.setObjectName("filterpic3")
        self.filterpic4 = QtWidgets.QLabel(self.All)
        self.filterpic4.setGeometry(QtCore.QRect(789, 148, 172, 102))
        self.filterpic4.setMinimumSize(QtCore.QSize(172, 102))
        self.filterpic4.setMaximumSize(QtCore.QSize(172, 102))
        self.filterpic4.setStyleSheet("")
        self.filterpic4.setText("")
        self.filterpic4.setObjectName("filterpic4")
        self.filterpicname3 = QtWidgets.QPushButton(self.All)
        self.filterpicname3.setGeometry(QtCore.QRect(611, 250, 140, 25))
        self.filterpicname3.setMinimumSize(QtCore.QSize(140, 0))
        self.filterpicname3.setMaximumSize(QtCore.QSize(140, 25))
        self.filterpicname3.setMouseTracking(True)
        self.filterpicname3.setStyleSheet("background-color: rgb(41, 4, 4);")
        self.filterpicname3.setCheckable(True)
        self.filterpicname3.setChecked(False)
        self.filterpicname3.setObjectName("filterpicname3")
        self.filter_button_group.addButton(self.filterpicname3)
        self.filterpicname4 = QtWidgets.QPushButton(self.All)
        self.filterpicname4.setGeometry(QtCore.QRect(789, 250, 140, 25))
        self.filterpicname4.setMinimumSize(QtCore.QSize(140, 0))
        self.filterpicname4.setMaximumSize(QtCore.QSize(140, 25))
        self.filterpicname4.setMouseTracking(True)
        self.filterpicname4.setStyleSheet("background-color: rgb(41, 4, 4);")
        self.filterpicname4.setCheckable(True)
        self.filterpicname4.setChecked(False)
        self.filterpicname4.setObjectName("filterpicname4")
        self.filter_button_group.addButton(self.filterpicname4)
        self.filterpic5 = QtWidgets.QLabel(self.All)
        self.filterpic5.setGeometry(QtCore.QRect(611, 275, 172, 102))
        self.filterpic5.setMinimumSize(QtCore.QSize(172, 102))
        self.filterpic5.setMaximumSize(QtCore.QSize(172, 102))
        self.filterpic5.setStyleSheet("")
        self.filterpic5.setText("")
        self.filterpic5.setObjectName("filterpic5")
        self.filterpic6 = QtWidgets.QLabel(self.All)
        self.filterpic6.setGeometry(QtCore.QRect(789, 275, 172, 102))
        self.filterpic6.setMinimumSize(QtCore.QSize(172, 102))
        self.filterpic6.setMaximumSize(QtCore.QSize(172, 102))
        self.filterpic6.setStyleSheet("")
        self.filterpic6.setText("")
        self.filterpic6.setObjectName("filterpic6")
        self.filterpicname5 = QtWidgets.QPushButton(self.All)
        self.filterpicname5.setGeometry(QtCore.QRect(611, 377, 140, 25))
        self.filterpicname5.setMinimumSize(QtCore.QSize(140, 0))
        self.filterpicname5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.filterpicname5.setMouseTracking(True)
        self.filterpicname5.setStyleSheet("background-color: rgb(41, 4, 4);")
        self.filterpicname5.setCheckable(True)
        self.filterpicname5.setChecked(False)
        self.filterpicname5.setObjectName("filterpicname5")
        self.filter_button_group.addButton(self.filterpicname5)
        self.filterpicname6 = QtWidgets.QPushButton(self.All)
        self.filterpicname6.setGeometry(QtCore.QRect(789, 377, 140, 25))
        self.filterpicname6.setMinimumSize(QtCore.QSize(140, 0))
        self.filterpicname6.setMaximumSize(QtCore.QSize(140, 25))
        self.filterpicname6.setMouseTracking(True)
        self.filterpicname6.setStyleSheet("background-color: rgb(41, 4, 4);")
        self.filterpicname6.setCheckable(True)
        self.filterpicname6.setChecked(False)
        self.filterpicname6.setObjectName("filterpicname6")
        self.filter_button_group.addButton(self.filterpicname6)
        self.filterpic8 = QtWidgets.QLabel(self.All)
        self.filterpic8.setGeometry(QtCore.QRect(789, 402, 172, 102))
        self.filterpic8.setMinimumSize(QtCore.QSize(172, 102))
        self.filterpic8.setMaximumSize(QtCore.QSize(172, 102))
        self.filterpic8.setStyleSheet("")
        self.filterpic8.setText("")
        self.filterpic8.setObjectName("filterpic8")
        self.filterpicname7 = QtWidgets.QPushButton(self.All)
        self.filterpicname7.setGeometry(QtCore.QRect(611, 504, 140, 25))
        self.filterpicname7.setMinimumSize(QtCore.QSize(140, 0))
        self.filterpicname7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.filterpicname7.setMouseTracking(True)
        self.filterpicname7.setStyleSheet("background-color: rgb(41, 4, 4);")
        self.filterpicname7.setCheckable(True)
        self.filterpicname7.setChecked(False)
        self.filterpicname7.setObjectName("filterpicname7")
        self.filter_button_group.addButton(self.filterpicname7)
        self.filterpicname8 = QtWidgets.QPushButton(self.All)
        self.filterpicname8.setGeometry(QtCore.QRect(789, 504, 140, 25))
        self.filterpicname8.setMinimumSize(QtCore.QSize(140, 0))
        self.filterpicname8.setMaximumSize(QtCore.QSize(140, 25))
        self.filterpicname8.setMouseTracking(True)
        self.filterpicname8.setStyleSheet("background-color: rgb(41, 4, 4);")
        self.filterpicname8.setCheckable(True)
        self.filterpicname8.setChecked(False)
        self.filterpicname8.setObjectName("filterpicname8")
        self.filter_button_group.addButton(self.filterpicname8)
        self.filterpic7 = QtWidgets.QLabel(self.All)
        self.filterpic7.setGeometry(QtCore.QRect(611, 402, 172, 102))
        self.filterpic7.setMinimumSize(QtCore.QSize(172, 102))
        self.filterpic7.setMaximumSize(QtCore.QSize(172, 102))
        self.filterpic7.setStyleSheet("")
        self.filterpic7.setText("")
        self.filterpic7.setObjectName("filterpic7")
        self.import_pic_from_cloud = QtWidgets.QPushButton(self.All)
        self.import_pic_from_cloud.setGeometry(QtCore.QRect(240, 230, 101, 25))
        self.import_pic_from_cloud.setObjectName("import_pic_from_cloud")
        self.label_2 = QtWidgets.QLabel(self.All)
        self.label_2.setGeometry(QtCore.QRect(230, 420, 131, 17))
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.All)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 440, 158, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.crop_button = QtWidgets.QPushButton(self.layoutWidget)
        self.crop_button.setMinimumSize(QtCore.QSize(48, 48))
        self.crop_button.setMaximumSize(QtCore.QSize(48, 48))
        self.crop_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crop_button.setMouseTracking(True)
        self.crop_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic_settings/pics/crop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.crop_button.setIcon(icon1)
        self.crop_button.setIconSize(QtCore.QSize(48, 48))
        self.crop_button.setFlat(True)
        self.crop_button.setObjectName("crop_button")
        self.horizontalLayout_2.addWidget(self.crop_button)
        self.rotate_left_button = QtWidgets.QPushButton(self.layoutWidget)
        self.rotate_left_button.setMinimumSize(QtCore.QSize(48, 48))
        self.rotate_left_button.setMaximumSize(QtCore.QSize(48, 48))
        self.rotate_left_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rotate_left_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pic_settings/pics/rotate_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_left_button.setIcon(icon2)
        self.rotate_left_button.setIconSize(QtCore.QSize(48, 48))
        self.rotate_left_button.setDefault(False)
        self.rotate_left_button.setFlat(True)
        self.rotate_left_button.setObjectName("rotate_left_button")
        self.horizontalLayout_2.addWidget(self.rotate_left_button)
        self.rotate_right_button = QtWidgets.QPushButton(self.layoutWidget)
        self.rotate_right_button.setMinimumSize(QtCore.QSize(48, 48))
        self.rotate_right_button.setMaximumSize(QtCore.QSize(48, 48))
        self.rotate_right_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rotate_right_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pic_settings/pics/rotate_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_right_button.setIcon(icon3)
        self.rotate_right_button.setIconSize(QtCore.QSize(48, 48))
        self.rotate_right_button.setFlat(True)
        self.rotate_right_button.setObjectName("rotate_right_button")
        self.horizontalLayout_2.addWidget(self.rotate_right_button)
        self.layoutWidget.raise_()
        self.filterpic1.raise_()
        self.filterpic2.raise_()
        self.filterpicname1.raise_()
        self.filterpicname2.raise_()
        self.filterpic3.raise_()
        self.filterpic4.raise_()
        self.filterpicname3.raise_()
        self.filterpicname4.raise_()
        self.filterpic5.raise_()
        self.filterpic6.raise_()
        self.filterpicname5.raise_()
        self.filterpicname6.raise_()
        self.filterpic8.raise_()
        self.filterpicname7.raise_()
        self.filterpicname8.raise_()
        self.filterpic7.raise_()
        self.picture_main.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.line_4.raise_()
        self.label_6.raise_()
        self.line_5.raise_()
        self.line_3.raise_()
        self.line_2.raise_()
        self.import_pic.raise_()
        self.import_pic_from_cloud.raise_()
        self.label_2.raise_()
        self.tabWidget.addTab(self.All, "")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 241, 581))
        self.toolBox.setStyleSheet("")
        self.toolBox.setObjectName("toolBox")
        self.filtre_sirasi = QtWidgets.QWidget()
        self.filtre_sirasi.setGeometry(QtCore.QRect(0, 0, 241, 517))
        self.filtre_sirasi.setObjectName("filtre_sirasi")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.filtre_sirasi)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 0, 231, 511))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 229, 509))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 20, 231, 491))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.left_panel_filters_layout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.left_panel_filters_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.left_panel_filters_layout.setContentsMargins(0, 0, 0, 0)
        self.left_panel_filters_layout.setHorizontalSpacing(6)
        self.left_panel_filters_layout.setVerticalSpacing(2)
        self.left_panel_filters_layout.setObjectName("left_panel_filters_layout")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setStyleSheet("selection-background-color: rgb(41, 4, 4);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.left_panel_filters_layout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.comboBox)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setGeometry(QtCore.QRect(0, 0, 230, 19))
        self.checkBox.setMinimumSize(QtCore.QSize(221, 19))
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.checkBox.setIconSize(QtCore.QSize(32, 32))
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.toolBox.addItem(self.filtre_sirasi, "")
        self.process_steps = QtWidgets.QWidget()
        self.process_steps.setGeometry(QtCore.QRect(0, 0, 241, 517))
        self.process_steps.setObjectName("process_steps")
        self.label_5 = QtWidgets.QLabel(self.process_steps)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 241, 521))
        self.label_5.setStyleSheet("background-color: rgb(38, 32, 32);")
        self.label_5.setObjectName("label_5")
        self.toolBox.addItem(self.process_steps, "")
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(250, 560, 581, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_measurement = QtWidgets.QPushButton(self.layoutWidget2)
        self.new_measurement.setMinimumSize(QtCore.QSize(130, 25))
        self.new_measurement.setMaximumSize(QtCore.QSize(130, 16777215))
        self.new_measurement.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.new_measurement.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.new_measurement.setIconSize(QtCore.QSize(32, 32))
        self.new_measurement.setAutoDefault(False)
        self.new_measurement.setObjectName("new_measurement")
        self.horizontalLayout.addWidget(self.new_measurement)
        self.filter_options = QtWidgets.QPushButton(self.layoutWidget2)
        self.filter_options.setMinimumSize(QtCore.QSize(130, 25))
        self.filter_options.setMaximumSize(QtCore.QSize(130, 16777215))
        self.filter_options.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.filter_options.setObjectName("filter_options")
        self.horizontalLayout.addWidget(self.filter_options)
        self.empty = QtWidgets.QPushButton(self.layoutWidget2)
        self.empty.setMinimumSize(QtCore.QSize(130, 25))
        self.empty.setMaximumSize(QtCore.QSize(130, 16777215))
        self.empty.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.empty.setObjectName("empty")
        self.horizontalLayout.addWidget(self.empty)
        self.settings = QtWidgets.QPushButton(self.layoutWidget2)
        self.settings.setMinimumSize(QtCore.QSize(130, 25))
        self.settings.setMaximumSize(QtCore.QSize(130, 16777215))
        self.settings.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.settings.setObjectName("settings")
        self.horizontalLayout.addWidget(self.settings)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(900, 570, 271, 17))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1269, 23))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setGeometry(QtCore.QRect(294, 172, 153, 162))
        self.menuMenu.setObjectName("menuMenu")
        self.menuYeni = QtWidgets.QMenu(self.menuMenu)
        self.menuYeni.setObjectName("menuYeni")
        self.menuA = QtWidgets.QMenu(self.menuMenu)
        self.menuA.setObjectName("menuA")
        self.menuKaydet = QtWidgets.QMenu(self.menuMenu)
        self.menuKaydet.setObjectName("menuKaydet")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.console = QtWidgets.QDockWidget(MainWindow)
        self.console.setMinimumSize(QtCore.QSize(1227, 119))
        self.console.setStyleSheet("background-color: rgb(26, 36, 39);")
        self.console.setObjectName("console")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents_3)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1221, 111))
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1219, 109))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.infobox = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.infobox.setGeometry(QtCore.QRect(10, 0, 1221, 51))
        self.infobox.setMinimumSize(QtCore.QSize(1221, 51))
        self.infobox.setStyleSheet("background-color: rgb(26, 36, 39);")
        self.infobox.setText("")
        self.infobox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.infobox.setObjectName("infobox")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.console.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.console)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setWhatsThis("")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar)
        self.actionPRoje = QtWidgets.QAction(MainWindow)
        self.actionPRoje.setObjectName("actionPRoje")
        self.actionResim = QtWidgets.QAction(MainWindow)
        self.actionResim.setObjectName("actionResim")
        self.actionLoadProject = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Toolbar/pics/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadProject.setIcon(icon4)
        self.actionLoadProject.setObjectName("actionLoadProject")
        self.actionResim_2 = QtWidgets.QAction(MainWindow)
        self.actionResim_2.setObjectName("actionResim_2")
        self.actionFarkl_Kaydet = QtWidgets.QAction(MainWindow)
        self.actionFarkl_Kaydet.setObjectName("actionFarkl_Kaydet")
        self.actionRun = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/gui/resources/pics/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/run/pics/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionRun.setIcon(icon5)
        self.actionRun.setObjectName("actionRun")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Toolbar/pics/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        self.actionSave.setObjectName("actionSave")
        self.menu_toolbar_save_params = QtWidgets.QAction(MainWindow)
        self.menu_toolbar_save_params.setObjectName("menu_toolbar_save_params")
        self.menu_toolbar_save_meas = QtWidgets.QAction(MainWindow)
        self.menu_toolbar_save_meas.setObjectName("menu_toolbar_save_meas")
        self.toolbar_new = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Toolbar/pics/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolbar_new.setIcon(icon7)
        self.toolbar_new.setObjectName("toolbar_new")
        self.toolbar_plot = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Toolbar/pics/plot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolbar_plot.setIcon(icon8)
        self.toolbar_plot.setObjectName("toolbar_plot")
        self.menuYeni.addSeparator()
        self.menuYeni.addSeparator()
        self.menuYeni.addAction(self.actionPRoje)
        self.menuYeni.addAction(self.actionResim)
        self.menuA.addAction(self.actionLoadProject)
        self.menuA.addAction(self.actionResim_2)
        self.menuKaydet.addAction(self.menu_toolbar_save_params)
        self.menuKaydet.addAction(self.menu_toolbar_save_meas)
        self.menuMenu.addAction(self.menuYeni.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menuA.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menuKaydet.menuAction())
        self.menuMenu.addAction(self.actionFarkl_Kaydet)
        self.menuMenu.addSeparator()
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())
        self.toolBar.addAction(self.toolbar_new)
        self.toolBar.addAction(self.actionLoadProject)
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.toolbar_plot)
        self.infobox.setBuddy(self.infobox)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.settings, self.new_measurement)
        MainWindow.setTabOrder(self.new_measurement, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.empty)
        MainWindow.setTabOrder(self.empty, self.filterpicname1)
        MainWindow.setTabOrder(self.filterpicname1, self.filterpicname2)
        MainWindow.setTabOrder(self.filterpicname2, self.filterpicname3)
        MainWindow.setTabOrder(self.filterpicname3, self.filterpicname4)
        MainWindow.setTabOrder(self.filterpicname4, self.filterpicname5)
        MainWindow.setTabOrder(self.filterpicname5, self.filterpicname6)
        MainWindow.setTabOrder(self.filterpicname6, self.filterpicname8)
        MainWindow.setTabOrder(self.filterpicname8, self.filterpicname7)
        MainWindow.setTabOrder(self.filterpicname7, self.import_pic)
        MainWindow.setTabOrder(self.import_pic, self.filter_options)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ImView0.1_beta"))
        self.import_pic.setWhatsThis(_translate("MainWindow", "donnow"))
        self.import_pic.setText(_translate("MainWindow", "Resim Yükle"))
        self.label_4.setText(_translate("MainWindow", "Ana Resim"))
        self.label_6.setText(_translate("MainWindow", "Filtreler"))
        self.filterpicname1.setText(_translate("MainWindow", "filtername"))
        self.filterpicname2.setText(_translate("MainWindow", "filtername"))
        self.filterpicname3.setText(_translate("MainWindow", "filtername"))
        self.filterpicname4.setText(_translate("MainWindow", "filtername"))
        self.filterpicname5.setText(_translate("MainWindow", "filtername"))
        self.filterpicname6.setText(_translate("MainWindow", "filtername"))
        self.filterpicname7.setText(_translate("MainWindow", "filtername"))
        self.filterpicname8.setText(_translate("MainWindow", "filtername"))
        self.import_pic_from_cloud.setText(_translate("MainWindow", "İçeri Aktar"))
        self.label_2.setText(_translate("MainWindow", "Resmi Düzenle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.All), _translate("MainWindow", "Hepsi"))
        self.comboBox.setItemText(0, _translate("MainWindow", "+ Filtre Ekle"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Canny"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Blur"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Bilateral"))
        self.checkBox.setText(_translate("MainWindow", "Gri Filtre Uygulansın mı ?       "))
        self.toolBox.setItemText(self.toolBox.indexOf(self.filtre_sirasi), _translate("MainWindow", "Filtreler"))
        self.label_5.setText(_translate("MainWindow", "Proses Adımları"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.process_steps), _translate("MainWindow", "Proses Adımları"))
        self.new_measurement.setText(_translate("MainWindow", "Öçüm Yap"))
        self.filter_options.setText(_translate("MainWindow", "Ölçüm Ayarları"))
        self.empty.setText(_translate("MainWindow", "Yeni Resim"))
        self.settings.setText(_translate("MainWindow", "Ayarlar"))
        self.label.setText(_translate("MainWindow", "ImView |v0.01| Haziran 2020"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuYeni.setTitle(_translate("MainWindow", "Yeni"))
        self.menuA.setTitle(_translate("MainWindow", "Aç"))
        self.menuKaydet.setTitle(_translate("MainWindow", "Kaydet"))
        self.menuEdit.setTitle(_translate("MainWindow", "Düzenle"))
        self.menuRun.setTitle(_translate("MainWindow", "Çalıştır"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.infobox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionPRoje.setText(_translate("MainWindow", "Proje"))
        self.actionResim.setText(_translate("MainWindow", "Resim"))
        self.actionLoadProject.setText(_translate("MainWindow", "Proje"))
        self.actionLoadProject.setWhatsThis(_translate("MainWindow", "Proje Aç"))
        self.actionLoadProject.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionResim_2.setText(_translate("MainWindow", "Resim"))
        self.actionFarkl_Kaydet.setText(_translate("MainWindow", "Farklı Kaydet"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionRun.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.actionRun.setWhatsThis(_translate("MainWindow", "Çalıştır"))
        self.actionRun.setShortcut(_translate("MainWindow", "F5"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.actionSave.setWhatsThis(_translate("MainWindow", "Kaydet"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menu_toolbar_save_params.setText(_translate("MainWindow", "Parametreleri Kaydet"))
        self.menu_toolbar_save_meas.setText(_translate("MainWindow", "Ölçüm Bilgilerini Kaydet"))
        self.toolbar_new.setText(_translate("MainWindow", "Yeni"))
        self.toolbar_plot.setText(_translate("MainWindow", "plot"))
import toolbar_rc