from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sys
class canny_layout :
    def __init__(self,mmf,tab,ftab,fname,):
        self.name = fname
        self.filter_picture = None
        self.filter_pixmap = None
        self.roi = None
        self.draw_area = None
        ftab.setStyleSheet("background-color: rgb(38, 32, 32);")
        self.canny_filter_pic = QtWidgets.QLabel(ftab)
        self.canny_filter_pic.setGeometry(QtCore.QRect(0, 20, 481, 341))
        self.canny_filter_pic.setStyleSheet("")
        self.canny_filter_pic.setText("")
        self.canny_filter_pic.setObjectName("canny_filter_pic")

        self.canny_output_pic = QtWidgets.QLabel(ftab)
        self.canny_output_pic.setGeometry(QtCore.QRect(510, 20, 481, 341))
        self.canny_output_pic.setStyleSheet("")
        self.canny_output_pic.setText("")
        self.canny_output_pic.setObjectName("canny_output_pic")

        self.label = QtWidgets.QLabel(ftab)
        self.label.setGeometry(QtCore.QRect(10, 0, 67, 17))
        self.label.setObjectName("label")
        self.label.setText("Filtre")

        self.label_2 = QtWidgets.QLabel(ftab)
        self.label_2.setGeometry(QtCore.QRect(520, 0, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Çıkış İmgesi")

        self.canny_para1 = QtWidgets.QSlider(ftab)
        self.canny_para1.setGeometry(QtCore.QRect(61, 436, 151, 16))
        self.canny_para1.setOrientation(QtCore.Qt.Horizontal)
        self.canny_para1.setObjectName("canny_para1")
        self.canny_para1.setMaximum(300)
        self.canny_para1.setMinimum(0)
        self.canny_para1.valueChanged.connect(lambda: mmf.canny_parameters(filter=self,))

        self.constant_lbl_2 = QtWidgets.QLabel(ftab)
        self.constant_lbl_2.setGeometry(QtCore.QRect(60, 400, 151, 20))
        self.constant_lbl_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.constant_lbl_2.setToolTipDuration(-1)
        self.constant_lbl_2.setStatusTip("")
        self.constant_lbl_2.setObjectName("constant_lbl_2")
        self.constant_lbl_2.setText("Minimum Değer ")

        self.constant_lbl_3 = QtWidgets.QLabel(ftab)
        self.constant_lbl_3.setGeometry(QtCore.QRect(280, 400, 151, 20))
        self.constant_lbl_3.setMouseTracking(True)
        self.constant_lbl_3.setObjectName("constant_lbl_3")
        self.constant_lbl_3.setText("Maximum Değer")

        self.canny_para2 = QtWidgets.QSlider(ftab)
        self.canny_para2.setGeometry(QtCore.QRect(274, 436, 151, 16))
        self.canny_para2.setOrientation(QtCore.Qt.Horizontal)
        self.canny_para2.setObjectName("canny_para2")
        self.canny_para2.valueChanged.connect(lambda: mmf.canny_parameters(filter=self,))
        self.canny_para2.setMaximum(300)
        self.canny_para2.setMinimum(0)

        self.canny_para1_val = QtWidgets.QLabel(ftab)
        self.canny_para1_val.setGeometry(QtCore.QRect(120, 460, 61, 17))
        self.canny_para1_val.setObjectName("canny_para1_val")
        self.canny_para1_val.setText("0")

        self.canny_para2_val = QtWidgets.QLabel(ftab)
        self.canny_para2_val.setGeometry(QtCore.QRect(350, 460, 51, 17))
        self.canny_para2_val.setObjectName("canny_para2_val")
        self.canny_para2_val.setText("0")

        self.constant_lbl = QtWidgets.QLabel(ftab)
        self.constant_lbl.setGeometry(QtCore.QRect(175, 370, 150, 17))
        self.constant_lbl.setObjectName("constant_lbl")
        self.constant_lbl.setText("Hysterysis Eşik Değeri")

        self.canny_para1_input = QtWidgets.QLineEdit(ftab)
        self.canny_para1_input.setGeometry(QtCore.QRect(80, 478, 85, 25))
        self.canny_para1_input.setStyleSheet("background-color: rgb(136, 138, 133);\n"
                                             "color: rgb(41, 4, 4);")
        self.canny_para1_input.returnPressed.connect(lambda : mmf.canny_parameters(filter=self,hint="input1"))
        self.canny_para1_input.setObjectName("canny_para1_input")
        self.canny_para2_input = QtWidgets.QLineEdit(ftab)
        self.canny_para2_input.setGeometry(QtCore.QRect(310, 478, 85, 25))
        self.canny_para2_input.setStyleSheet("background-color: rgb(136, 138, 133);\n"
                                             "color: rgb(41, 4, 4);")
        self.canny_para2_input.setObjectName("canny_para2_input")
        self.canny_para2_input.returnPressed.connect(lambda : mmf.canny_parameters(filter=self,hint="input2"))

        self.constant_lbl_4 = QtWidgets.QLabel(ftab)
        self.constant_lbl_4.setGeometry(QtCore.QRect(470, 400, 150, 17))
        self.constant_lbl_4.setObjectName("constant_lbl3")
        self.constant_lbl_4.setText("Aperture Değeri")

        self.canny_aperture_size = QtWidgets.QSlider(ftab)
        self.canny_aperture_size.setGeometry(QtCore.QRect(530, 430, 16, 50))
        self.canny_aperture_size.setOrientation(QtCore.Qt.Vertical)
        self.canny_aperture_size.setMaximum(7)
        self.canny_aperture_size.setMinimum(3)
        self.canny_aperture_size.setSingleStep(2)
        self.canny_aperture_size.valueChanged.connect(lambda : mmf.canny_parameters(filter=self,hint="aperture"))
#***************************** ÇİZİM VE ROI SEÇİMİ**************************************************
        self.constant_lbl_5 = QtWidgets.QLabel(ftab)
        self.constant_lbl_5.setGeometry(QtCore.QRect(720, 460, 70, 17))
        self.constant_lbl_5.setObjectName("constant_lbl_5")
        self.constant_lbl_5.setText("ROI Seçiniz")

        self.constant_lbl_6 = QtWidgets.QLabel(ftab)
        self.constant_lbl_6.setGeometry(QtCore.QRect(880, 460, 67, 17))
        self.constant_lbl_6.setObjectName("constant_lbl_6")
        self.constant_lbl_6.setText("Boyama")
        self.roi_circle = QtWidgets.QToolButton(ftab)
        self.roi_circle.setGeometry(QtCore.QRect(700, 490, 26, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/drawings/pics/circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.roi_circle.setIcon(icon1)
        self.roi_circle.setObjectName("roi_circle")
        self.roi_circle.clicked.connect(lambda: mmf.select_roi(filter=self,hint="circle"))

        self.roi_rect = QtWidgets.QToolButton(ftab)
        self.roi_rect.setGeometry(QtCore.QRect(740, 490, 26, 24))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/drawings/pics/rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.roi_rect.setIcon(icon2)
        self.roi_rect.setObjectName("roi_rect")
        self.roi_rect.clicked.connect(lambda: mmf.select_roi(filter=self, hint="rect"))

        self.roi_line = QtWidgets.QToolButton(ftab)
        self.roi_line.setGeometry(QtCore.QRect(780, 490, 26, 24))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/drawings/pics/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.roi_line.setIcon(icon3)
        self.roi_line.setObjectName("roi_line")

        self.draw_circ = QtWidgets.QToolButton(ftab)
        self.draw_circ.setGeometry(QtCore.QRect(860, 490, 26, 24))
        self.draw_circ.setIcon(icon1)
        self.draw_circ.setObjectName("draw_circ")
        self.draw_circ.clicked.connect(lambda: mmf.draw_area(filter=self, hint="circle"))

        self.draw_rect = QtWidgets.QToolButton(ftab)
        self.draw_rect.setGeometry(QtCore.QRect(900, 490, 26, 24))
        self.draw_rect.setIcon(icon2)
        self.draw_rect.setObjectName("draw_rect")
        self.draw_rect.clicked.connect(lambda: mmf.draw_area(filter=self,hint = "rect"))

        self.draw_line = QtWidgets.QToolButton(ftab)
        self.draw_line.setGeometry(QtCore.QRect(940, 490, 26, 24))
        self.draw_line.setIcon(icon3)
        self.draw_line.setObjectName("draw_line")
        self.line_6 = QtWidgets.QFrame(ftab)
        self.line_6.setGeometry(QtCore.QRect(670, 530, 161, 2))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(ftab)
        self.line_7.setGeometry(QtCore.QRect(670, 460, 2, 70))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(ftab)
        self.line_8.setGeometry(QtCore.QRect(670, 460, 161, 2))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(ftab)
        self.line_9.setGeometry(QtCore.QRect(830, 460, 2, 70))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_19 = QtWidgets.QFrame(ftab)
        self.line_19.setGeometry(QtCore.QRect(840, 460, 140, 2))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(ftab)
        self.line_20.setGeometry(QtCore.QRect(840, 530, 140, 2))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(ftab)
        self.line_21.setGeometry(QtCore.QRect(840, 460, 2, 70))
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(ftab)
        self.line_22.setGeometry(QtCore.QRect(980, 460, 2, 70))
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")

        tab.addTab(ftab, "")
        tab.setTabText(tab.indexOf(ftab), fname)
    def update_input_image(self,im):
        im = im.scaled(self.canny_filter_pic.size(), QtCore.Qt.KeepAspectRatio)
        self.canny_filter_pic.setPixmap(im)
    def update_output_image(self,im):
        im = im.scaled(self.canny_filter_pic.size(), QtCore.Qt.KeepAspectRatio)
        self.canny_output_pic.setPixmap(im)

    def update_params(self, params=None, roi=None, draw_area=None):
        if params == None:
            return
        self.canny_para1.setValue(params[0])
        self.canny_para1_val.setText(str(params[0]))
        self.canny_para2.setValue(params[1])
        self.canny_para2_val.setText(str(params[1]))
        self.roi = roi
        self.draw_area = draw_area
class blur_layout :
    def __init__(self,mmf,tab,ftab,fname):
        self.name = fname
        self.filter_picture = None
        self.filter_pixmap = None
        self.roi = None
        self.draw_area = None
        ftab.setStyleSheet("background-color: rgb(38, 32, 32);")
        self.blur_filter_pic = QtWidgets.QLabel(ftab)
        self.blur_filter_pic.setGeometry(QtCore.QRect(0, 20, 481, 341))
        self.blur_filter_pic.setStyleSheet("")
        self.blur_filter_pic.setText("")
        self.blur_filter_pic.setObjectName("blur_filter_pic")

        self.blur_output_pic = QtWidgets.QLabel(ftab)
        self.blur_output_pic.setGeometry(QtCore.QRect(510, 20, 481, 341))
        self.blur_output_pic.setStyleSheet("")
        self.blur_output_pic.setText("")
        self.blur_output_pic.setObjectName("blur_output_pic")

        self.label = QtWidgets.QLabel(ftab)
        self.label.setGeometry(QtCore.QRect(10, 0, 67, 17))
        self.label.setObjectName("label")
        self.label.setText("Filtre")

        self.label_2 = QtWidgets.QLabel(ftab)
        self.label_2.setGeometry(QtCore.QRect(520, 0, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Çıkış İmgesi")

        self.blur_para1 = QtWidgets.QSlider(ftab)
        self.blur_para1.setGeometry(QtCore.QRect(61, 436, 151, 16))
        self.blur_para1.setOrientation(QtCore.Qt.Horizontal)
        self.blur_para1.setObjectName("blur_para1")
        self.blur_para1.setValue(1)
        self.blur_para1.setMinimum(1)
        self.blur_para1.setMaximum(63)
        self.blur_para1.setSingleStep(2)
        self.blur_para1.valueChanged.connect(lambda: mmf.blur_parameters(filter=self))
        self.constant_lbl_2 = QtWidgets.QLabel(ftab)
        self.constant_lbl_2.setGeometry(QtCore.QRect(60, 400, 151, 20))
        self.constant_lbl_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.constant_lbl_2.setToolTipDuration(-1)
        self.constant_lbl_2.setStatusTip("")
        self.constant_lbl_2.setObjectName("constant_lbl_2")
        self.constant_lbl_2.setText("Kernel Yükseklik")

        self.constant_lbl_3 = QtWidgets.QLabel(ftab)
        self.constant_lbl_3.setGeometry(QtCore.QRect(280, 400, 151, 20))
        self.constant_lbl_3.setMouseTracking(True)
        self.constant_lbl_3.setObjectName("constant_lbl_3")
        self.constant_lbl_3.setText("Kernel Genişlik")

        self.blur_para2 = QtWidgets.QSlider(ftab)
        self.blur_para2.setGeometry(QtCore.QRect(274, 436, 151, 16))
        self.blur_para2.setOrientation(QtCore.Qt.Horizontal)
        self.blur_para2.setObjectName("canny_para2")
        self.blur_para2.setValue(1)
        self.blur_para2.setMinimum(1)
        self.blur_para2.setMaximum(45)
        self.blur_para2.setSingleStep(2)
        self.blur_para2.valueChanged.connect(lambda: mmf.blur_parameters(filter=self))

        self.blur_para1_val = QtWidgets.QLabel(ftab)
        self.blur_para1_val.setGeometry(QtCore.QRect(120, 460, 61, 17))
        self.blur_para1_val.setObjectName("blur_para1_val")
        self.blur_para1_val.setText("0")

        self.blur_para2_val = QtWidgets.QLabel(ftab)
        self.blur_para2_val.setGeometry(QtCore.QRect(350, 460, 51, 17))
        self.blur_para2_val.setObjectName("blur_para2_val")
        self.blur_para2_val.setText("0")

        self.constant_lbl = QtWidgets.QLabel(ftab)
        self.constant_lbl.setGeometry(QtCore.QRect(175, 370, 150, 17))
        self.constant_lbl.setObjectName("constant_lbl")
        self.constant_lbl.setText("Blur Kernel Değerleri")

        self.blur_para1_input = QtWidgets.QLineEdit(ftab)
        self.blur_para1_input.setGeometry(QtCore.QRect(80, 478, 85, 25))
        self.blur_para1_input.setStyleSheet("background-color: rgb(136, 138, 133);\n"
                                             "color: rgb(41, 4, 4);")
        self.blur_para1_input.returnPressed.connect(lambda : mmf.blur_parameters(filter=self,hint = "input1"))
        self.blur_para1_input.setObjectName("blur_para1_input")

        self.blur_para2_input = QtWidgets.QLineEdit(ftab)
        self.blur_para2_input.setGeometry(QtCore.QRect(310, 478, 85, 25))
        self.blur_para2_input.setStyleSheet("background-color: rgb(136, 138, 133);\n"
                                             "color: rgb(41, 4, 4);")
        self.blur_para2_input.setObjectName("blur_para2_input")
        self.blur_para2_input.returnPressed.connect(lambda : mmf.blur_parameters(filter=self,hint ="input2"))

        self.constant_lbl_5 = QtWidgets.QLabel(ftab)
        self.constant_lbl_5.setGeometry(QtCore.QRect(720, 460, 70, 17))
        self.constant_lbl_5.setObjectName("constant_lbl_5")
        self.constant_lbl_5.setText("ROI Seçiniz")

        self.constant_lbl_6 = QtWidgets.QLabel(ftab)
        self.constant_lbl_6.setGeometry(QtCore.QRect(880, 460, 67, 17))
        self.constant_lbl_6.setObjectName("constant_lbl_6")
        self.constant_lbl_6.setText("Boyama")
        self.roi_circle = QtWidgets.QToolButton(ftab)
        self.roi_circle.setGeometry(QtCore.QRect(700, 490, 26, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/drawings/pics/circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.roi_circle.setIcon(icon1)
        self.roi_circle.setObjectName("roi_circle")
        self.roi_circle.clicked.connect(lambda: mmf.select_roi(filter=self,hint="circle"))

        self.roi_rect = QtWidgets.QToolButton(ftab)
        self.roi_rect.setGeometry(QtCore.QRect(740, 490, 26, 24))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/drawings/pics/rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.roi_rect.setIcon(icon2)
        self.roi_rect.setObjectName("roi_rect")
        self.roi_rect.clicked.connect(lambda: mmf.select_roi(filter=self, hint="rect"))

        self.roi_line = QtWidgets.QToolButton(ftab)
        self.roi_line.setGeometry(QtCore.QRect(780, 490, 26, 24))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/drawings/pics/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.roi_line.setIcon(icon3)
        self.roi_line.setObjectName("roi_line")

        self.draw_circ = QtWidgets.QToolButton(ftab)
        self.draw_circ.setGeometry(QtCore.QRect(860, 490, 26, 24))
        self.draw_circ.setIcon(icon1)
        self.draw_circ.setObjectName("draw_circ")
        self.draw_circ.clicked.connect(lambda: mmf.draw_area(filter=self, hint="circle"))

        self.draw_rect = QtWidgets.QToolButton(ftab)
        self.draw_rect.setGeometry(QtCore.QRect(900, 490, 26, 24))
        self.draw_rect.setIcon(icon2)
        self.draw_rect.setObjectName("draw_rect")
        self.draw_rect.clicked.connect(lambda: mmf.draw_area(filter=self,hint = "rect"))

        self.draw_line = QtWidgets.QToolButton(ftab)
        self.draw_line.setGeometry(QtCore.QRect(940, 490, 26, 24))
        self.draw_line.setIcon(icon3)
        self.draw_line.setObjectName("draw_line")
        self.line_6 = QtWidgets.QFrame(ftab)
        self.line_6.setGeometry(QtCore.QRect(670, 530, 161, 2))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(ftab)
        self.line_7.setGeometry(QtCore.QRect(670, 460, 2, 70))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(ftab)
        self.line_8.setGeometry(QtCore.QRect(670, 460, 161, 2))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(ftab)
        self.line_9.setGeometry(QtCore.QRect(830, 460, 2, 70))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_19 = QtWidgets.QFrame(ftab)
        self.line_19.setGeometry(QtCore.QRect(840, 460, 140, 2))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(ftab)
        self.line_20.setGeometry(QtCore.QRect(840, 530, 140, 2))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(ftab)
        self.line_21.setGeometry(QtCore.QRect(840, 460, 2, 70))
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(ftab)
        self.line_22.setGeometry(QtCore.QRect(980, 460, 2, 70))
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")

        tab.addTab(ftab, "")
        tab.setTabText(tab.indexOf(ftab), fname)

    def update_input_image(self,im):
        im = im.scaled(self.blur_filter_pic.size(), QtCore.Qt.KeepAspectRatio)
        self.blur_filter_pic.setPixmap(im)
    def update_output_image(self,im):
        im = im.scaled(self.blur_filter_pic.size(), QtCore.Qt.KeepAspectRatio)
        self.blur_output_pic.setPixmap(im)
    def update_params(self,params = None,roi = None,draw_area = None):
        if params == None:
            return
        self.blur_para1.setValue(params[0])
        self.blur_para1_val.setText(str(params[0]))
        self.blur_para2.setValue(params[1])
        self.blur_para2_val.setText(str(params[1]))
        self.roi = roi
        self.draw_area = draw_area
class left_panel_buttons:
    def __init__(self,mmf,gui,fname):
        self.fname = fname
        self.Button = QtWidgets.QPushButton(gui.layoutWidget1) # TODO : Sol paneli QT 'den güncelle ve layoutwidget i değiştir.
        self.Button.setText(fname)
        self.Button.clicked.connect(lambda: mmf.delete_filter(self.fname))
        gui.left_panel_filters_layout.addWidget(self.Button)

def confirmation_dialog(widget,title ,message,):
    buttonReply = QMessageBox.question(widget,title, message,
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if buttonReply == QMessageBox.Yes:
        return True
    else:
        return False
def measure_settings(settings,gui):
    class PopUpDLG(QtWidgets.QDialog): #Credit : Achayan/stackeroweflow
        def __init__(self,parent,settings):
            #super().__init__(parent)
            super(PopUpDLG, self).__init__(parent)
            self.settings = settings
            self.setObjectName("self")
            self.resize(500, 150)
            self.setMinimumSize(QtCore.QSize(500, 250))
            self.setMaximumSize(QtCore.QSize(500, 250))
            self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
            #icon = QtGui.QIcon()
            #icon.addPixmap(QtGui.QPixmap("Icons/Plus-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            #self.setWindowIcon(icon)
            self.contour_style = QtWidgets.QComboBox(self)
            items = ["DEFAULT","CCOMP","TREE"]
            self.contour_style.addItems(items)
            self.contour_style.activated[str].connect(lambda : self.update_setting(key = "c_style",value=self.contour_style.currentText()))
            self.gridLayout = QtWidgets.QGridLayout(self)
            self.gridLayout.setObjectName("gridLayout")
            self.label = QtWidgets.QLabel(self)
            self.label.setObjectName("label")
            self.label.setText("Metot Seçiniz :")
            self.gridLayout.addWidget(self.contour_style, 0, 1, 1, 1)
            self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

            self.label2 = QtWidgets.QLabel(self)
            self.label2.setObjectName("label2")
            self.label2.setText("Referans Ölçüsü Giriniz :")
            self.ref_input = QtWidgets.QLineEdit(self)
            self.ref_input.setGeometry(QtCore.QRect(80, 478, 85, 25))
            self.ref_input.textChanged.connect(lambda : self.update_setting(key="width",
                                                                            value=self.ref_input.text()))
            self.gridLayout.addWidget(self.ref_input, 1, 1, 1, 1)
            self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)

            self.ok = QtWidgets.QPushButton(self)
            self.ok.setObjectName("ok")
            self.ok.setText("Tamam")

            self.gridLayout.addWidget(self.ok, 2, 0, 1, 1)
            self.cancel = QtWidgets.QPushButton(self)
            self.cancel.setObjectName("cancel_link")
            self.gridLayout.addWidget(self.cancel, 2, 1, 1, 1)
            self.cancel.setText("İptal")
            self.cancel.clicked.connect(self.reject_)
            self.ok.clicked.connect(self.done_)
            self.upd_content()
        def done_ (self,*args,**kwargs):
            self.close()
            return
        def reject_(self):
            self.close()
            return
        def upd_content(self):
            if self.settings["c_style"] == "TREE":
                self.contour_style.setCurrentIndex(2)
            elif self.settings["c_style"] == "CCOMP":
                self.contour_style.setCurrentIndex(1)
        def update_setting (self,key,value):

            if not self.settings is None:
                if key == "c_style":
                    if value == "DEFAULT":
                        return
                    self.settings[key] = value
                elif key == "width":
                    try:
                        value = float(value)
                    except:
                        return
                    if value <0:
                        return
                    self.settings[key] = value

    popup = PopUpDLG(gui,settings)
    popup.show()
#****************************************POPUP WINDOW IMAGE *******************************
class PopUpDLG(QtWidgets.QDialog): #Credit : Achayan/stackeroweflow
    def __init__(self,parent,image):
        super(PopUpDLG, self).__init__(parent)
        self.setObjectName("self")
        self.resize(parent.size())
        self.setMinimumSize(QtCore.QSize(parent.size()))
        self.setMaximumSize(QtCore.QSize(parent.size()))
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("Icons/Plus-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.setWindowIcon(icon)
        self.image = QtWidgets.QLabel(self)
        self.image.setGeometry(QtCore.QRect(0, 0, 1200, 740))
        self.image.setObjectName("image")
        image = image.scaled(parent.size(), QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(image)
        self.ok = QtWidgets.QPushButton(self)
        self.ok.setObjectName("ok")
        self.ok.setText("Tamam")
        self.ok.setGeometry(20,30,40,150)
        self.horzlayout = QtWidgets.QHBoxLayout(self)
        self.horzlayout.setContentsMargins(0, 0, 0, 0)
        #self.horzlayout.setGeometry(QtCore.QRect(parent.size().height()-40,0,40,parent.size().width()))
        self.horzlayout.setGeometry(QtCore.QRect(460, 720, 281, 31))
        self.horzlayout.setObjectName("horzlayout")
        self.horzlayout.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setObjectName("cancel_link")
        self.horzlayout.addWidget(self.cancel)
        self.cancel.setText("İptal")
        self.cancel.setGeometry(0, 0, 40, 150)
        self.cancel.clicked.connect(self.reject_)
        self.ok.clicked.connect(self.done_)
        self.upd_content()
    def done_ (self,*args,**kwargs):
        self.close()
        return
    def reject_(self):
        self.close()
        return
    def upd_content(self):
        pass
    def update_setting (self,key,value):
        pass
class Poppi(QtWidgets.QDialog):
    def __init__(self,parent,image):
        super(Poppi, self).__init__(parent)
        self.resize(1200, 756)
        self.image = QtWidgets.QLabel(self)
        self.image.setGeometry(QtCore.QRect(0, 0, 1200, 721))
        self.image.setText("")
        self.image.setObjectName("label")

        self.lbl = QtWidgets.QLabel(self)
        self.lbl.setGeometry(QtCore.QRect(0, 730, 201, 17))
        self.lbl.setObjectName("label_2")
        self.lbl.setText("Kesme işlemi için alan seçiniz.")
        image = image.scaled(parent.size(), QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(image)
        self.boxWid = QtWidgets.QWidget(self)
        self.box = QtWidgets.QHBoxLayout(self.boxWid)
        self.box.addWidget(self.image)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(460, 720, 281, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ok.setStyleSheet("background-color: rgb(17, 103, 2);\n"
                                        "color: rgb(186, 189, 182);")
        self.ok.setObjectName("ok")
        self.ok.setText("OK")
        self.horizontalLayout.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel.setStyleSheet("background-color: rgb(93, 10, 10);\n"
                                      "color: rgb(186, 189, 182);")
        self.cancel.setObjectName("cancel")
        self.cancel.setText("İptal")
        self.horizontalLayout.addWidget(self.cancel)

def show_image(gui,image):
    popup = Poppi(gui,image)
    popup.show()
def crop_image_layout(gui,image):
    class crop_pp (Poppi):
        def __init__(self,gui,image):
            super(crop_pp,self).__init__(gui,image)
            self.setMouseTracking(True)
            self.i = 0
            self.ok.clicked.connect(self.close)
            self.cancel.clicked.connect(self.close)
        def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
            print(a0.x(),a0.y())

            """   
            def wheelEvent(self, a0: QtGui.QWheelEvent) -> None:
                newHeight = self.image.geometry().height() - a0.angleDelta().y()
                width = self.image.geometry().width() - a0.angleDelta().y()
                self.image.resize(width, newHeight)
            """
    popup = crop_pp(gui,image)
    popup.show()