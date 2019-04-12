
import sys
from Segundo_ejemplo_GUI import *

class MiFormulario(QtGui.QWidget):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    self.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'), self.sacatexto)
  def sacatexto(self):
   self.ui.label.setText("Bienvenido")

if __name__ == "__main__":
   mi_aplicacion = QtGui.QApplication(sys.argv)
   mi_app = MiFormulario()
   mi_app.show()
   sys.exit(mi_aplicacion.exec_())
