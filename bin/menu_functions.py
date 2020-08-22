from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QLineEdit,QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from program_files import program_files
from log import printlog,errorlog
from menu_objects import mainmenu_objects,filter
from menu_layouts import canny_layout,blur_layout,left_panel_buttons,confirmation_dialog,\
    measure_settings,show_image,crop_image_layout
from filters import Canny,Blur,Bilateral
from log import gui_log,errorlog
import analysis
import time
global pf
import os
from save import save,load_filters
import measure as measure
import qcamera
import json
import numpy as np
from cloud_ import firebase
pf = program_files("bin/appdb")

class mainmenu_funcs():
    def __init__(self):
        self.crop_flag = False
        self.rotate_right = None
        self.rotate_left = None
        self.project = None
        self.main_image = None
        self.main_pic = None
        self.gate = False
        self.status()
        self.mmo = mainmenu_objects()
        self.settings = {"c_style":"TREE","width":16.6}
        self.save_file = None
        self.measure_database = analysis.database()
    def load_gui (self,gui,app,wdg,log,proc):
        self.gui = gui
        self.log = log
        self.log.gui = self.gui
        self.gui.comboBox.activated[str].connect(self.add_filter_from_panel)
        self.gui.comboBox.setCurrentIndex(0)
        #self.gui.import_pic_from_cloud.hide()
        self.gui.import_pic_from_cloud.clicked.connect(self.import_pic_from_cloud)
        self.gui.new_measurement.clicked.connect(self.measure)
        self.gui.filter_options.clicked.connect(lambda: measure_settings(settings = self.settings,gui = self.widget))
        self.gui.crop_button.clicked.connect(lambda : self.crop())
        self.gui.actionRun.triggered.connect(lambda: measure.run(picture =
                                                                 self.professor.output_image,
                                                                 width = self.settings["width"]))
        self.gui.actionLoadProject.triggered.connect(self.load_project)
        self.gui.actionSave.triggered.connect(lambda: save(dbpath = self.save(),
                                                            filterlist = self.mmo.gui_filters.op_filters))

        self.gui.settings.clicked.connect(self.emp)
        self.gui.launch_camera_btn.clicked.connect(qcamera.launch)
        self.gui.rotate_left_button.clicked.connect(lambda: self.rotate(hint = "left"))
        self.gui.rotate_right_button.clicked.connect(lambda: self.rotate(hint = "right"))
        self.gui.actionPRoje.triggered.connect(self.reset_all)
        self.gui.empty.clicked.connect(self._import_pic)
        self.gui.toolbar_plot.triggered.connect(self.analysis_)
        self.app = app
        self.widget = wdg
        self.mmo.load_gui(self.gui)
        self.pictures()
        self.professor = proc
        self.professor.pf = pf
        self.control()
    def emp(self):
        print(self.settings.values())
        self.resize(size = None)
    def load_menu(self,menu):
        self.menu = menu
    def save(self,):
        if self.save_file == None:
            self.save_file =  QFileDialog.getSaveFileName(self.widget, 'Kaydet')[0]
        return self.save_file
    def load_project(self):
        def to_array(list):
            if list == "None" or list == None:
                return None
            else :

                out = []
                out.append(np.array(list))
                return out
        def convert_to_list(str):
            if str == "None" or str == None:
                return None
            else :
                return json.loads(str)
        """   
        if not self.s_main_image == None :
            buttonReply = confirmation_dialog(widget=self.widget, title="Dikkat !",
                                              message= "Yeni bir proje açarsanız, tüm ilerlemeniz kaybolacak onaylıyor musunuz ?")
            if not buttonReply == True:
                return
        """
        while True:
            self.save_file = QFileDialog.getExistingDirectory(self.widget, 'Projeyi içeren dosyayı seçiniz:',
                                                          '', QFileDialog.ShowDirsOnly)
            if self.save_file == "" or self.save_file is None:
                break
            loading_filters = load_filters(self.save_file)
            if loading_filters == None:
                continue #TODO: kafam karıştı
            else :
                self.reset_all(hint="dont_touch_image")
                i = 0
                for filter in loading_filters:
                    self.mmo.new_filter(nm = filter[0],load= True)
                    self.add_filter(i= i,new_filter=filter[0],params=convert_to_list(filter[1]),
                                 picture=None,info = filter[3] ,
                                roi = convert_to_list(filter[4]),draw_area = convert_to_list(filter[5])) #TODO:Order eklenecek
                    self.mmo.gui_filters.widgets[filter[0]].update_params(params = convert_to_list(filter[1]),
                                                                          roi = to_array(convert_to_list(filter[4])),
                                                                           draw_area = to_array(convert_to_list(filter[5])))
                    if filter[4] is None or filter[4] == [] or filter[4] == "None":
                        pass
                    else:
                        self.mmo.gui_filters.op_filters[filter[0]].roi = np.array(convert_to_list(filter[4]))
                    if filter[5] is None or filter[5] == [] or filter[4] == "None":
                        pass
                    else:
                        self.mmo.gui_filters.op_filters[filter[0]].draw_area = np.array(convert_to_list(filter[5]))
                    i += 1

                self.control()
                break
    def reset_all(self,hint = None):
        self.rotate_right = None
        self.rotate_left = None
        self.crop_flag = None
        if confirmation_dialog(widget = self.widget,title = "Dikkat !",message = "Tüm veriler temizlenecek onaylıyor musunuz ?") == False :
            return
        self.status(hint="reset")
        if not hint == "dont_touch_image":
            self.save_file = None #TODO:SAVE FILE RESETINI AYARLA
            self.s_main_image = None
            self.main_image = None
            self.gui.picture_main.clear()
        self.mmo.reset()
        self.run()
        self.control()
    def status(self, hint=None, var=None, action=None):
        if hint == None:
            self.s_main_image = False  # TODO Reset sistemi getirilecek
            self.s_filterlist = []
            self.s_filternmlist = []
            self.s_filtertablist = []
            self.varlist = {"main_image": self.s_main_image, "filter_list": self.s_filterlist}
        if hint == "reset":
            #self.save_file = None
            for elm in self.varlist.values():
                elm = None
        if var != None and action != None:
            try:
                self.varlist[var] = action
            except:
                errorlog()

    def control(self,hint=None):
        if self.s_main_image == None or self.main_pic == None:
            self.gate = False
        else :
            self.gate = True
        for filter_ in self.mmo.gui_filters.op_filters.values():
            if self.s_main_image == None:
                break
            if filter_.picture == None and  self.main_pic != None:
                filter_.picture = pf.copy(path=self.main_pic,
                                         to_path=pf.join(pf.temp, filter_.name))
        if hint == "filter":
            self.professor.filterlist = []
            if self.gui.checkBox.checkState() == 2:
                self.professor.gray_filter = True
            else:
                self.professor.gray_filter = False

            for filter in self.mmo.gui_filters.op_filters.values():
                self.professor.filterlist.append(filter)
            return
        elif hint == "post-process":
            self.output_image = self.professor.output_image_path
        elif hint == "update_pics":
            pass
        i = 0

        if self.s_main_image != True:
            self.gui.import_pic.show()
        else:
            self.gui.import_pic.hide()
        for f in self.mmo.filterpic + self.mmo.filterpicname:
            f.hide()
        for fp in self.s_filterlist + self.s_filternmlist:
            fp.show()
        self.professor.filterlist = []

#**********************************  MAIN TAB FUNCS  ******************************
    def import_pic_from_cloud(self):
        path = os.getcwd() + str("/gui/img")
        firebase().download(path)
    def _import_pic(self):
        filePath = QFileDialog.getOpenFileName(self.widget,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)")
        path = filePath[0]
        self.main_pic = path
        name = filePath[0].split("/")[-1]
        self.professor.main_image_name = name
        self.professor.temp_image_path = pf.copy(path=self.main_pic, to_path=pf.join(path = pf.temp,path2=name))
        self.professor.main_image_path = self.professor.temp_image_path
        self.main_pic = self.professor.temp_image_path
        if self.rotate_left == True:
            self.rotate(hint = "left")
        elif self.rotate_right == True:
            self.rotate(hint = "right")
        if self.crop_flag == True:
            self.crop(hint = "auto")
        else:
            self.set_pic(self.gui.picture_main,name)
        self.s_main_image = True
        self.control()
        self.log("Resim içeri aktarıldı")
    def set_pic(self,label,pic,size_hint = "label"):
        size = label.size()
        pf.goto(pf.temp)
        self.main_pixmap = QPixmap(pic)
        self.main_pixmap_scaled = self.main_pixmap.scaled(size, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(self.main_pixmap_scaled)
        filter_pic = self.main_pixmap.scaled(self.gui.filterpic3.size(), QtCore.Qt.KeepAspectRatio)
        for fp in self.mmo.filterpic:
            fp.setPixmap(filter_pic)
        pf.goto(pf.main)
    def pictures(self):
        pf.goto(pf.gui_img)
        self.main_pixmap = QPixmap("saved_img.jpg")

        self.main_pixmap = self.main_pixmap.scaled(self.gui.picture_main.size(), QtCore.Qt.KeepAspectRatio)
        pf.goto(pf.main)
    def delete_filter (self,fname):
        buttonReply = confirmation_dialog(widget = self.widget,title = "Dikkat !",message = fname + "Filtresini sileceksiniz. Onaylıyor musunuz ?")
        if buttonReply == True:
            print('Filtre silinecek.')
        else:
            print('İptal edildi.')

    def add_filter_from_panel(self,fname):
        self.log("Filtre Eklendi")
        if fname == "+ Filtre Ekle":
            return
        if self.s_main_image == False:
            self.gui.comboBox.setCurrentIndex(0)
            QMessageBox.information(self.widget,"HATA !","Filtrelenecek resminiz bulunmuyor !")
            return
        self.gui.comboBox.setCurrentIndex(0)
        for i in range (0,len(self.s_filterlist)+1):# MAIN MENUDEKİ BOŞ FİLTRE ALANLARI
            if i == len(self.s_filterlist) and i < len(self.mmo.filterpic):
                new_filter = self.mmo.new_filter(nm = fname)
                path_to_filter = new_filter+os.path.splitext(self.main_pic)[-1]
                self.add_filter(i= i,new_filter = new_filter,params =[7,7,7],picture=pf.copy(path=self.main_pic, to_path=pf.join(pf.temp,path_to_filter))   )
                break
        self.control()
    def add_filter(self,i,new_filter,params,picture,info = None,roi = None,draw_area = None):
        self.s_filterlist.append(self.mmo.filterpic[i])
        self.s_filternmlist.append(self.mmo.filterpicname[i])# SABİT RESİMLERİN AKTİF OLMASI


        if new_filter[0:4] == "Blur":
          self.mmo.gui_filters.widgets[new_filter] = \
              blur_layout(mmf=self, tab=self.gui.tabWidget, fname=new_filter,
                           ftab=self.mmo.gui_filters.tabs[new_filter])


        elif new_filter[0:5] == "Canny":
            self.mmo.gui_filters.widgets[new_filter] = \
                       canny_layout(mmf=self,tab = self.gui.tabWidget,fname = new_filter,
                                    ftab= self.mmo.gui_filters.tabs[new_filter])


        self.mmo.filterpicname[i].setText(new_filter) #CONSTANT
        self.mmo.gui_filters.left_panel[new_filter] = left_panel_buttons(mmf = self,gui= self.gui, fname = new_filter)
        self.mmo.gui_filters.widgets[new_filter].update_input_image(im = self.main_pixmap) #TODO:İsimleri güncelle
        self.mmo.gui_filters.op_filters[new_filter].name = new_filter
        self.mmo.gui_filters.op_filters[new_filter].params = params #TODO: Daha iyi bir çözüm bul.(başlangıçta parametrelerin None olması
        self.mmo.gui_filters.op_filters[new_filter].picture = picture

        #self.s_filtertablist.append(self.mmo.filtertab[i]) #TODO tablist oluştur
        self.log(new_filter + " isimli filtre eklendi !")

#**********************************  CANNY LAYOUT TAB FUNCTIONS  ******************************

    def canny_parameters(self,filter = None,hint = None):
        if hint == "input1":
            input1 = filter.canny_para1_input.text()
            try:
                if int(input1) < 0 : return
            except: return
            filter.canny_para1.setValue(int(input1))
        elif hint == "input2":
            input2 = filter.canny_para2_input.text()
            try:
                if int(input2) < 0 : return
            except Exception as e:
                print(e)
                return
            filter.canny_para2.setValue(int(input2))
        elif hint == "aperture":
            if not filter.canny_aperture_size.value() in (3,5,7):
                filter.canny_aperture_size.setValue(filter.canny_aperture_size.value()+1)
        para1 = filter.canny_para1.value()
        para2 = filter.canny_para2.value()
        ap    = filter.canny_aperture_size.value()
        filter.canny_para1_val.setText(str(para1))
        filter.canny_para2_val.setText(str(para2))
        self.mmo.gui_filters.op_filters[filter.name].params = [para1,para2,ap]
        if self.run() == False:
            return
        filter.filter_pixmap = QPixmap(self.mmo.gui_filters.op_filters[filter.name].picture)
        filter.update_input_image(filter.filter_pixmap)
        filter.update_output_image(QPixmap(self.output_image))

    def blur_parameters(self,filter,hint = None):
        if hint == "input1":
            filter.blur_para1.setValue(int(filter.blur_para1_input.text()))
        elif hint == "input2":
            filter.blur_para2.setValue(int(filter.blur_para2_input.text()))
        kernel1 = filter.blur_para1.value()
        kernel2 = filter.blur_para2.value()
        if kernel1 %2 == 0 :
            return filter.blur_para1.setValue(kernel1+1)
        if kernel2 %2 == 0:
            return filter.blur_para2.setValue(kernel2+1)
        filter.blur_para1_val.setText(str(kernel1))
        filter.blur_para2_val.setText(str(kernel2))
        self.mmo.gui_filters.op_filters[filter.name].params = [kernel1,kernel2]
        if self.run() == False:
            return
        filter.filter_pixmap = QPixmap(self.mmo.gui_filters.op_filters[filter.name].picture)
        filter.update_input_image(filter.filter_pixmap)
        filter.update_output_image(QPixmap(self.output_image))
    def draw_area(self,filter,hint):
        if self.run() == False:
            return
        if hint == "circle":
            self.mmo.gui_filters.op_filters[filter.name].draw_area = self.professor.select_ROI_circle(self.mmo.gui_filters.op_filters[filter.name].picture)
        elif hint == "rect":
            self.mmo.gui_filters.op_filters[filter.name].draw_area = self.professor.select_ROI(self.mmo.gui_filters.op_filters[filter.name].picture)

        self.run()
    def select_roi(self,filter,hint):
        if self.run() == False  :
            return
        if hint == "rect":
            filter.roi = self.professor.select_ROI(self.mmo.gui_filters.op_filters[filter.name].picture)
        elif hint == "circle":
            filter.roi = self.professor.select_ROI_circle(self.mmo.gui_filters.op_filters[filter.name].picture)

        self.mmo.gui_filters.op_filters[filter.name].roi = filter.roi
        self.run()
    def resize(self,size): #TODO: Size seçim penceresi ekle
        self.professor.resize(image =self.professor.main_image_path,size = size)
        self.s_main_image = True
        self.control()
    def crop(self,hint = None):
        self.crop_flag = True

        if hint != "auto":
            self.crop_roi = self.professor.select_ROI(image=self.professor.main_image_path,
                                                                hint="one")
        self.professor.crop_image(image=self.professor.main_image_path,
                                  roi=self.crop_roi)
        self.set_pic(self.gui.picture_main, self.professor.main_image_name)
        self.s_main_image = True
        self.control()
    def rotate(self,hint):
        if hint == "right":
            self.rotate_right =True
        elif hint == "left":
            self.rotate_left = True
        self.professor.rotate(image = self.professor.main_image_path,type = hint)
        self.set_pic(self.gui.picture_main, self.professor.main_image_name)
        self.s_main_image = True
        self.control()
    def run(self):
        self.control(hint= "filter")
        if not self.gate == True:
            return False
        self.professor.run()
        self.control(hint="post-process")

    def measure(self):
        try:
            results = measure.run(picture=self.professor.output_image,
                        width=self.settings["width"],
                        hint=self.settings["c_style"])
            self.measure_database.save_measurement(results)
        except:
            pass
        #self.measure_database.print_db("Obje1")

    def analysis_(self):
        analysis.analysis().auto(self.measure_database.cur)
