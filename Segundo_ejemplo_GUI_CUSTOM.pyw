import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import random
from Segundo_ejemplo_GUI_CUSTOM import *

class Myform(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.trash_img)

    def aleatorio_img(self):
        img_list = ['404.png', '404_b.png', '404_c.png', 'linux.png']
        result = random.choice(img_list)
        return result

    def trash_img(self):
        self.ui.label.setPixmap(QPixmap(self.aleatorio_img()))
        

if __name__ == "__main__":
    application = QtGui.QApplication(sys.argv)
    my_APP = Myform()
    my_APP.show()
    sys.exit(application.exec_()) 