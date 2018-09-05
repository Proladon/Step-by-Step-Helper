import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui
from Step_Helper import Ui_MainWin


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWin()
        self.ui.setupUi(self)
        self.show()  

        
        

app = QApplication(sys.argv)
a = App()
a.show()
sys.exit(app.exec_())