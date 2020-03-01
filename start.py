import sys
from 起始界面 import *
from PyQt5.QtWidgets import QApplication,QMainWindow

class Mymainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Mymainwindow, self).__init__(parent)
        self.setupUi(self)

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = Mymainwindow()
    myWin.show()
    sys.exit(app.exec_())