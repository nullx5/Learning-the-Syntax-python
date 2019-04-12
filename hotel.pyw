import sys
from hotel import *
import datetime

class MiFormulario(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.ui = Ui_Reserva()
    self.ui.setupUi(self)
    self.ui.tipo_hab.addItems(["Individual","Doble","Familiar"])
    QtCore.QObject.connect(self.ui.reservar, QtCore.SIGNAL('clicked()'), self.reserva)

    hoy = datetime.date.today()
    entrada = QtCore.QDate()
    entrada.setYMD(hoy.year,hoy.month, hoy.day)
    self.ui.fecha_entrada.setDate(hoy)
    self.ui.fecha_salida.setDate(hoy)



  def reserva(self):
    inicio = self.ui.fecha_entrada.date()
    fin = self.ui.fecha_salida.date()

    if fin.__gt__(inicio):

      dias = inicio.daysTo(fin)
      hab = self.ui.tipo_hab.currentText().lower()
      if self.ui.plaza_garaje.isChecked() == True:
        con_sin = " con "
      else:
        con_sin = " sin "
      if self.ui.tipo_hab.currentIndex() == 0:
        cuota = 25
      elif self.ui.tipo_hab.currentIndex() == 1:
        cuota =50
      else:
        cuota = 75

      if self.ui.plaza_garaje.isChecked() == True:
        total = (dias * (cuota + 10))
      else:
        total = dias * cuota
      self.ui.salida.setText("La reserva por " + str(dias) + " noche/s en habitacion " + hab +con_sin +"plaza de garaje asciende a "+ str(total)+ " euros.")
    else:
      self.ui.salida.setText("Las fechas no son correctas. Corrijalas e intentelo de nuevo")
    #print("Hola")



if __name__ == "__main__":
   mi_aplicacion = QtGui.QApplication(sys.argv)
   mi_app = MiFormulario()
   mi_app.show()
   sys.exit(mi_aplicacion.exec_())