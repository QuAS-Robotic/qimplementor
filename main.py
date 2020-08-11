import sys
import os
sys.path.append("bin")
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtGui import QIcon, QPixmap
    from iv_layout import Ui_MainWindow
    from menu_functions import mainmenu_funcs
    from menu_objects import mainmenu_objects
    from log import gui_log,errorlog
    from professor import professor
except ImportError:
    os.system("python setup.py --user")
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtGui import QIcon, QPixmap
    from iv_layout import Ui_MainWindow
    from menu_functions import mainmenu_funcs
    from menu_objects import mainmenu_objects
    from log import gui_log,errorlog
    from professor import professor
except Exception as e:
    print(e)
global mmf
mmf = mainmenu_funcs()
mmo = mainmenu_objects()
def version_control():
    app_version = "0.1"
    version_info = ""
    return app_version,version_info
class mainwin(Ui_MainWindow):
    def __init__(self,mw):
        self.setupUi(mw)
        self.clicks()
    def clicks(self):
        self.import_pic.clicked.connect(mmf._import_pic)
        #self.empty.clicked.connect(mmf.reset_all)
        #self.filter_options.clicked.connect(mmf.delete_filter)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainwin(MainWindow)
    log = gui_log(ui)
    app.setStyle("fusion")
    info = "Hoş Geldiniz ! \nUygulama Sürümü : " + version_control()[0] + "\n"
    log(info)
    process = professor()
    mmf.load_gui(gui=ui,app=app,wdg=MainWindow,log = log,proc = process) # load class features to mm func module
    mmo.load_gui(ui) # load class gui to menu objects
    MainWindow.show()
    sys.exit(app.exec_())
