import sys
from gas import *

class MiFormulario(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.enero, QtCore.SIGNAL('editingFinished()'), self.grafico_enero)
    QtCore.QObject.connect(self.ui.febrero, QtCore.SIGNAL('editingFinished()'), self.grafico_febrero)
    QtCore.QObject.connect(self.ui.marzo, QtCore.SIGNAL('editingFinished()'), self.grafico_marzo)
    QtCore.QObject.connect(self.ui.abril, QtCore.SIGNAL('editingFinished()'), self.grafico_abril)

    QtCore.QObject.connect(self.ui.dial, QtCore.SIGNAL('valueChanged(int)'), self.grafico_volumen)

  def grafico_enero(self):
      if len(self.ui.enero.text()) != 0:
          self.ui.barra_e.setValue(int(self.ui.enero.text()))
  def grafico_febrero(self):
      if len(self.ui.febrero.text()) != 0:
          self.ui.barra_f.setValue(int(self.ui.febrero.text()))
  def grafico_marzo(self):
      if len(self.ui.marzo.text()) != 0:
          self.ui.barra_m.setValue(int(self.ui.marzo.text()))
  def grafico_abril(self):
      if len(self.ui.abril.text()) != 0:
          self.ui.barra_a.setValue(int(self.ui.abril.text()))
  def grafico_volumen(self):
      self.ui.volumen.setValue(self.ui.dial.value())


if __name__ == "__main__":
   mi_aplicacion = QtGui.QApplication(sys.argv)
   mi_app = MiFormulario()
   mi_app.show()
   sys.exit(mi_aplicacion.exec_())