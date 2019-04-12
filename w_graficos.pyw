import sys
from w_graficos import *
from PyQt4.QtGui import *
class MyForm(QtGui.QDialog):
    def __init__(self, icono1, icono2, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.escena1 = QGraphicsScene(self)
        self.escena2 = QGraphicsScene(self)
        mi_icono1 = QGraphicsPixmapItem(icono1)
        mi_icono2 = QGraphicsPixmapItem(icono2)
        self.escena1.addItem(mi_icono1)
        self.escena2.addItem(mi_icono2)
        self.ui.graficos_1.setScene(self.escena1)
        self.ui.graficos_2.setScene(self.escena2)

if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   icono1 = QtGui.QPixmap()
   icono2 = QtGui.QPixmap()
   icono1.load(r"C:\Python33\Lib\site-packages\PyQt4\examples\widgets\icons\images\designer.png")
   icono2.load(r"C:\Users\flop\Desktop\Ficheros_Python\imagen1.jpg")
   myapp = MyForm(icono1, icono2)
   myapp.show()
   sys.exit(app.exec_())
