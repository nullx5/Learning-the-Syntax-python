import sys
from Calculadora_simple_2 import *

class MiFormulario(QtGui.QWidget):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.boton_calcular, QtCore.SIGNAL('clicked()'), self.imprime)


  def imprime(self):
    if len(self.ui.num_1.text())!=0:
       numero_1 = float(self.ui.num_1.text())
    else:
       numero_1 = 0.0
    if len(self.ui.num_2.text())!=0:
       numero_2= float(self.ui.num_2.text())
    else:
       numero_2 = 0.0
    if self.ui.op_suma.isChecked() == True:
       suma = numero_1 + numero_2
       self.ui.salida.setText("La suma de " + str(numero_1)+ " y " + str(numero_2)+ " es " + str(suma))
    if self.ui.op_resta.isChecked() == True:
       resta = numero_1 - numero_2
       self.ui.salida.setText("La resta de " + str(numero_1)+ " y "+ str(numero_2)+ " es " + str(resta))
    if self.ui.op_mul.isChecked() == True:
       mul = numero_1 * numero_2
       self.ui.salida.setText("La multiplicacion de " + str(numero_1)+ " y " + str(numero_2)+ " es " + str(mul))
    if self.ui.op_div.isChecked() == True:
       div = numero_1 / numero_2
       self.ui.salida.setText("La division de " + str(numero_1)+ " y "+ str(numero_2)+ " es " + str(div))


if __name__ == "__main__":
   mi_aplicacion = QtGui.QApplication(sys.argv)
   mi_app = MiFormulario()
   mi_app.show()
   sys.exit(mi_aplicacion.exec_())
