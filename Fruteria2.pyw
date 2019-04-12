import sys
from Fruteria2 import *

class MiFormulario(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    self.ui.precio_fruta.setText("0.25")
    self.ui.precio_verdura.setText("1.50")
    self.ui.precio_legumbre.setText("1.25")
    QtCore.QObject.connect(self.ui.cant_ma, QtCore.SIGNAL('valueChanged(int)'), self.marca_ma)
    QtCore.QObject.connect(self.ui.cant_pe, QtCore.SIGNAL('valueChanged(int)'), self.marca_pe)
    QtCore.QObject.connect(self.ui.cant_pl, QtCore.SIGNAL('valueChanged(int)'), self.marca_pl)
    QtCore.QObject.connect(self.ui.cant_ac, QtCore.SIGNAL('valueChanged(int)'), self.marca_ac)
    QtCore.QObject.connect(self.ui.cant_bo, QtCore.SIGNAL('valueChanged(int)'), self.marca_bo)
    QtCore.QObject.connect(self.ui.cant_ca, QtCore.SIGNAL('valueChanged(int)'), self.marca_ca)
    QtCore.QObject.connect(self.ui.cant_al, QtCore.SIGNAL('valueChanged(int)'), self.marca_al)
    QtCore.QObject.connect(self.ui.cant_le, QtCore.SIGNAL('valueChanged(int)'), self.marca_le)
    QtCore.QObject.connect(self.ui.cant_ga, QtCore.SIGNAL('valueChanged(int)'), self.marca_ga)

    QtCore.QObject.connect(self.ui.op_ma, QtCore.SIGNAL('clicked()'), self.ver_ma)
    QtCore.QObject.connect(self.ui.op_pe, QtCore.SIGNAL('clicked()'), self.ver_pe)
    QtCore.QObject.connect(self.ui.op_pl, QtCore.SIGNAL('clicked()'), self.ver_pl)

  def imprime(self):
    ma = float(self.ui.cant_ma.value())
    pe = float(self.ui.cant_pe.value())
    pl = float(self.ui.cant_pl.value())
    precio_fruta = float(self.ui.precio_fruta.text())
    total_fruta = (ma+pe+pl) * precio_fruta
    self.ui.total_fruta.setText(str(total_fruta))

    ac = float(self.ui.cant_ac.value())
    bo = float(self.ui.cant_bo.value())
    ca = float(self.ui.cant_ca.value())
    precio_verdura = float(self.ui.precio_verdura.text())
    total_verdura = (ac+bo+ca) * precio_verdura
    self.ui.total_verdura.setText(str(total_verdura))

    al = float(self.ui.cant_al.value())
    le = float(self.ui.cant_le.value())
    ga = float(self.ui.cant_ga.value())
    precio_legumbre = float(self.ui.precio_legumbre.text())
    total_legumbre = (al+le+ga) * precio_legumbre
    self.ui.total_legumbre.setText(str(total_legumbre))

    total_productos = 0
    if self.ui.op_ma.isChecked():
      total_productos += 1
    if self.ui.op_pe.isChecked():
      total_productos += 1
    if self.ui.op_pl.isChecked():
      total_productos += 1
    if self.ui.op_ac.isChecked():
      total_productos += 1
    if self.ui.op_bo.isChecked():
      total_productos += 1
    if self.ui.op_ca.isChecked():
      total_productos += 1
    if self.ui.op_al.isChecked():
      total_productos += 1
    if self.ui.op_le.isChecked():
      total_productos += 1
    if self.ui.op_ga.isChecked():
      total_productos += 1

    self.ui.salida.setText("La compra de " + str(total_productos) + \
                           " producto/s distintos asciende a un total de " + \
                           str(total_fruta+total_verdura+total_legumbre) + " euros" )

  def marca_ma(self):
    if self.ui.cant_ma.value() != 0:
      self.ui.op_ma.setChecked(True)
    else:
      self.ui.op_ma.setChecked(False)
    self.imprime()

  def marca_pe(self):
    if self.ui.cant_pe.value() != 0:
      self.ui.op_pe.setChecked(True)
    else:
      self.ui.op_pe.setChecked(False)
    self.imprime()

  def marca_pl(self):
    if self.ui.cant_pl.value() != 0:
      self.ui.op_pl.setChecked(True)
    else:
      self.ui.op_pl.setChecked(False)
    self.imprime()

  def marca_ac(self):
    if self.ui.cant_ac.value() != 0:
      self.ui.op_ac.setChecked(True)
    else:
      self.ui.op_ac.setChecked(False)
    self.imprime()

  def marca_bo(self):
    if self.ui.cant_bo.value() != 0:
      self.ui.op_bo.setChecked(True)
    else:
      self.ui.op_bo.setChecked(False)
    self.imprime()

  def marca_ca(self):
    if self.ui.cant_ca.value() != 0:
      self.ui.op_ca.setChecked(True)
    else:
      self.ui.op_ca.setChecked(False)
    self.imprime()
  def marca_al(self):
    if self.ui.cant_al.value() != 0:
      self.ui.op_al.setChecked(True)
    else:
      self.ui.op_al.setChecked(False)
    self.imprime()

  def marca_le(self):
    if self.ui.cant_le.value() != 0:
      self.ui.op_le.setChecked(True)
    else:
      self.ui.op_le.setChecked(False)
    self.imprime()

  def marca_ga(self):
    if self.ui.cant_ga.value() != 0:
      self.ui.op_ga.setChecked(True)
    else:
      self.ui.op_ga.setChecked(False)
    self.imprime()

  def ver_ma(self):
    if self.ui.cant_ma.value() != 0:
      self.ui.op_ma.setChecked(True)
    else:
      self.ui.op_ma.setChecked(False)

  def ver_pe(self):
    if self.ui.cant_pe.value() != 0:
      self.ui.op_pe.setChecked(True)
    else:
      self.ui.op_pe.setChecked(False)

  def ver_pl(self):
    if self.ui.cant_pl.value() != 0:
      self.ui.op_pl.setChecked(True)
    else:
      self.ui.op_pl.setChecked(False)


if __name__ == "__main__":
   mi_aplicacion = QtGui.QApplication(sys.argv)
   mi_app = MiFormulario()
   mi_app.show()
   sys.exit(mi_aplicacion.exec_())
