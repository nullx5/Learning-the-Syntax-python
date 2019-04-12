import sys
from w_listas import *

class MiFormulario(QtGui.QDialog):
  def __init__(self, parent=None):
      QtGui.QDialog.__init__(self, parent)
      self.ui = Ui_Dialog()
      self.ui.setupUi(self)
      self.ui.nombres.setFocus()
      QtCore.QObject.connect(self.ui.boton_guardar, QtCore.SIGNAL('clicked()'), self.guarda)
      QtCore.QObject.connect(self.ui.boton_editar, QtCore.SIGNAL('clicked()'), self.edita)
      QtCore.QObject.connect(self.ui.boton_borrar, QtCore.SIGNAL('clicked()'), self.borra_item)
      QtCore.QObject.connect(self.ui.boton_borrar_todo, QtCore.SIGNAL('clicked()'), self.borra_todo)

  def guarda(self):
      if len(self.ui.nombres.text()) != 0:
          self.ui.lista.addItem(self.ui.nombres.text())
          self.ui.nombres.clear()
      self.ui.nombres.setFocus()

  def edita(self):
      fila = self.ui.lista.currentRow()
      invitado , ok = QtGui.QInputDialog.getText(self, "Editar", "Introduzca corrección")
      if ok and (len(invitado) != 0):
          self.ui.lista.takeItem(self.ui.lista.currentRow())
          self.ui.lista.insertItem(fila , invitado)
  def borra_item(self):
      self.ui.lista.takeItem(self.ui.lista.currentRow())

  def borra_todo(self):
      self.ui.lista.clear()


if __name__ == "__main__":
     mi_aplicacion = QtGui.QApplication(sys.argv)
     mi_app = MiFormulario()
     mi_app.show()
     sys.exit(mi_aplicacion.exec_())