import sys
from inmobiliaria import *


class MiFormulario(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.ui = Ui_Ficha()
    self.ui.setupUi(self)
    self.ui.localidad.addItems(["Logroño","Madrid","Zaragoza"])
    self.ui.tipo.addItems(["Centro","Afueras"])
    QtCore.QObject.connect(self.ui.buscar, QtCore.SIGNAL('clicked()'), self.busqueda)
    #QtCore.QObject.connect(self.ui.num_hab, QtCore.SIGNAL('valueChanged(int)'), self.busqueda)


  def busqueda(self):
    lo = self.ui.localidad.currentText()
    ti = self.ui.tipo.currentText()
    hab = self.ui.num_hab.value()
    ba = self.ui.num_ba.value()
    if self.ui.plaza_garaje.isChecked() == True:
        con_sin = " con "
    else:
        con_sin = " sin "
    self.ui.salida.setText("Su búsqueda es: En " + lo + " en " + ti.lower() + " con " + str(hab)+ \
                           " habitacion/es y " + str(ba) + " baño" + con_sin + "plaza de garaje.")


if __name__ == "__main__":
   mi_aplicacion = QtGui.QApplication(sys.argv)
   mi_app = MiFormulario()
   mi_app.show()
   sys.exit(mi_aplicacion.exec_())