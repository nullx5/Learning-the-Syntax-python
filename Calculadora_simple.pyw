import sys
from Calculadora_simple import *

class MiFormulario(QtGui.QWidget):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.boton_suma, QtCore.SIGNAL('clicked()'), self.imprime_suma)
    QtCore.QObject.connect(self.ui.boton_resta, QtCore.SIGNAL('clicked()'), self.imprime_resta)
    QtCore.QObject.connect(self.ui.boton_mul, QtCore.SIGNAL('clicked()'), self.imprime_mul)
    QtCore.QObject.connect(self.ui.boton_div, QtCore.SIGNAL('clicked()'), self.imprime_div)

  def imprime_suma(self):
    if len(self.ui.num_1.text())!=0:
       numero_1 = float(self.ui.num_1.text())
    else:
       numero_1 = 0.0
    if len(self.ui.num_2.text())!=0:
       numero_2= float(self.ui.num_2.text())
    else:
       numero_2 = 0.0
    suma = numero_1 + numero_2
    self.ui.salida.setText("La suma de " + str(numero_1)+ " y " + str(numero_2)+ " es " + str(suma))

  def imprime_resta(self):
    if len(self.ui.num_1.text())!=0:
       numero_1 = float(self.ui.num_1.text())
    else:
       numero_1 = 0.0
    if len(self.ui.num_2.text())!=0:
       numero_2= float(self.ui.num_2.text())
    else:
       numero_2 = 0.0
    resta = numero_1 - numero_2
    self.ui.salida.setText("La resta de " + str(numero_1)+ " y "+ str(numero_2)+ " es " + str(resta))

  def imprime_mul(self):
    if len(self.ui.num_1.text())!=0:
       numero_1 = float(self.ui.num_1.text())
    else:
       numero_1 = 0.0
    if len(self.ui.num_2.text())!=0:
       numero_2= float(self.ui.num_2.text())
    else:
       numero_2 = 0.0
    mul = numero_1 * numero_2
    self.ui.salida.setText("La multiplicacion de " + str(numero_1)+ " y "+ str(numero_2)+ " es " + str(mul))

  def imprime_div(self):
    if len(self.ui.num_1.text())!=0:
       numero_1 = float(self.ui.num_1.text())
    else:
       numero_1 = 0.0
    if len(self.ui.num_2.text())!=0:
       numero_2= float(self.ui.num_2.text())
    else:
       numero_2 = 0.0
    div = numero_1 / numero_2
    self.ui.salida.setText("La division de " + str(numero_1)+ " y "+ str(numero_2)+ " es " + str(div))


if __name__ == "__main__":
   mi_aplicacion = QtGui.QApplication(sys.argv)
   mi_app = MiFormulario()
   mi_app.show()
   sys.exit(mi_aplicacion.exec_())
