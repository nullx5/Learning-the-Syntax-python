import sys
from spin import *


class MiFormulario(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.uno, QtCore.SIGNAL('valueChanged(double)'), self.modifica1)
    QtCore.QObject.connect(self.ui.dos, QtCore.SIGNAL('valueChanged(double)'), self.modifica2)
    QtCore.QObject.connect(self.ui.tres, QtCore.SIGNAL('valueChanged(double)'), self.modifica3)

  def modifica1(self):
    self.ui.g_1.setValue(int(self.ui.uno.value()))
    total = self.ui.uno.value() + self.ui.dos.value() + self.ui.tres.value()
    if total > 100:
       self.ui.suma.setText(str(self.ui.uno.value() + self.ui.dos.value() + self.ui.tres.value() ) )
       self.ui.error.setEnabled(True)
       self.deshabilita_todo()
    else:
      self.ui.suma.setText(str(self.ui.uno.value() + self.ui.dos.value() + self.ui.tres.value() ) )
  def modifica2(self):
    self.ui.g_2.setValue(int(self.ui.dos.value()) * 2)
    total = self.ui.uno.value() + self.ui.dos.value() + self.ui.tres.value()
    if total > 100:
       self.ui.suma.setText(str(self.ui.uno.value() + self.ui.dos.value() + self.ui.tres.value() ) )
       self.ui.error.setEnabled(True)
       self.deshabilita_todo()
    else:
      self.ui.suma.setText(str(self.ui.uno.value() + self.ui.dos.value() + self.ui.tres.value() ) )
  def modifica3(self):
    self.ui.g_3.setValue(int(self.ui.tres.value()) * 4)
    total = self.ui.uno.value() + self.ui.dos.value() + self.ui.tres.value()
    if total > 100:
       self.ui.suma.setText(str(self.ui.uno.value() + self.ui.dos.value() + self.ui.tres.value() ) )
       self.ui.error.setEnabled(True)
       self.deshabilita_todo()
    else:
      self.ui.suma.setText(str(self.ui.uno.value() + self.ui.dos.value() + self.ui.tres.value() ) )
  def deshabilita_todo(self):
      self.ui.uno.setEnabled(False)
      self.ui.dos.setEnabled(False)
      self.ui.tres.setEnabled(False)
      self.ui.g_1.setEnabled(False)
      self.ui.g_2.setEnabled(False)
      self.ui.g_3.setEnabled(False)
      self.ui.suma.setEnabled(False)
      self.ui.label.setEnabled(False)

if __name__ == "__main__":
   mi_aplicacion = QtGui.QApplication(sys.argv)
   mi_app = MiFormulario()
   mi_app.show()
   sys.exit(mi_aplicacion.exec_())