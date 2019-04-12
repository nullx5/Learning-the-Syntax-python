import sys
from w_web import *
from PyQt4 import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.boton_cargar, QtCore.SIGNAL('clicked()'), self.cargar)

    def cargar(self):
        print(self.ui.direccion.text())
        self.ui.pagina_web.load(QtCore.QUrl(self.ui.direccion.text()))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())