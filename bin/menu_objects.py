#---MENU OBJECTS MODULE--

from PyQt5 import QtCore, QtGui, QtWidgets
from menu_layouts import canny_layout,left_panel_buttons
class filter:
    def __init__(self,nm = None,params = None):
        self.name = nm
        self.params = params
        self.picture = None
        self.info = "info"
        self.roi = None
        self.draw_area = None
        self.order = None
    def parameters(self):
        return self.params
class gui_filters:
    def __init__(self):
        self.reset()
    def reset (self,hint = None):
        self.namelist = []
        self.tabs = {}
        self.pictures = {}
        self.widgets = {}
        self.left_panel = {}
        self.op_filters = {}
        self.draw_are = {}
    def add_filter(self,fname):
        self.namelist.append(fname)

        self.tabs.update({fname:fname})
        self.tabs[fname] = QtWidgets.QWidget()
        self.tabs[fname].setObjectName(fname)

        self.pictures.update({fname:fname})

        self.widgets.update({fname:fname})

        self.left_panel.update({fname: fname})
        self.op_filters.update({fname:filter()})
class mainmenu_objects:
    def __init__(self,):
        pass
    def load_gui(self,gui):
        self.gui = gui
        self.filterpic = [self.gui.filterpic1,self.gui.filterpic2,self.gui.filterpic3,self.gui.filterpic4
                        ,self.gui.filterpic5,self.gui.filterpic6,self.gui.filterpic7,self.gui.filterpic8]

        self.filterpicname = [self.gui.filterpicname1,self.gui.filterpicname2,self.gui.filterpicname3,
                           self.gui.filterpicname4,self.gui.filterpicname5,self.gui.filterpicname6,
                           self.gui.filterpicname7,self.gui.filterpicname8]
        #TODO İSİMLERİ GÜNCELLE !
        self.gui_filters = gui_filters()
        #-------------------SABİT OBJELER
        """
        self.param = [self.gui.param1,self.gui.param2,self.gui.param3,self.gui.param4,self.gui.param5,
                      self.gui.param6,self.gui.param7,self.gui.param8]
        
        self.paramname = [self.gui.paramname1,self.gui.paramname2,self.gui.paramname3,self.gui.paramname4
                          ,self.gui.paramname5,self.gui.paramname6,self.gui.paramname7,self.gui.paramname8
                          ]
        """

        #***********************İCONLAR*************************

        #***************************DİNAMİK OBJELER*************

    def new_filter(self,nm = None,param = None,btn = None,load=None): # CREATES NEW NAME AND WIDGET
        if load == True:
            self.gui_filters.add_filter(nm)
            return nm
        if nm == None:
            nm = "filtre"
            default = "filtre"
        else:
            default = nm
        i = 1
        while True:
            if default in self.gui_filters.namelist:
                default = nm+ str(i)
                i += 1
                if i == 200:
                    break
            else :
                self.filtername = default
                break
        self.gui_filters.add_filter(self.filtername)
        return self.filtername

    def reset(self):
        for tab in self.gui_filters.tabs.values():
            self.gui.tabWidget.removeTab(1)
        for lp in self.gui_filters.left_panel.values():
            try:
                lp.Button.deleteLater()
            except:
                pass
        self.gui_filters.reset()
