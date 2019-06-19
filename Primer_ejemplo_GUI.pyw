
import sys
from PyQt4 import QtGui, QtCore

class primer_ejemplo_GUI(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(500, 200, 400, 400)
        self.setWindowTitle("Primer Ejemplo de GUI con PyQt")
        salir = QtGui.QPushButton("Salir", self)
        salir.setGeometry(150, 150, 100, 100)
        self.connect(salir, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))

app = QtGui.QApplication(sys.argv)
mi_app = primer_ejemplo_GUI()
mi_app.show()
sys.exit(app.exec_())
