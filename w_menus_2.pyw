import sys
from w_menus_2 import *
from PyQt4 import *
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sumar.setChecked(True)
        self.ui.aa.triggered.connect(self.activa_a)
        self.ui.da.triggered.connect(self.desactiva_a)
        self.ui.ac.triggered.connect(self.activa_c)
        self.ui.dc.triggered.connect(self.desactiva_c)
        self.ui.boton_calcular.clicked.connect(self.calcular)
        self.ui.action1.triggered.connect(self.activa_a)
        self.ui.action1.triggered.connect(self.activa_c)
        self.ui.action2.triggered.connect(self.desactiva_a)
        self.ui.action2.triggered.connect(self.desactiva_c)

    def activa_a(self):
        self.ui.boton_calcular.setEnabled(True)
        self.ui.etiqueta1.setEnabled(True)
        self.ui.etiqueta2.setEnabled(True)
        self.ui.num1.setEnabled(True)
        self.ui.num2.setEnabled(True)
        self.ui.sumar.setEnabled(True)
        self.ui.restar.setEnabled(True)
        self.ui.resultado.setEnabled(True)

    def desactiva_a(self):
        self.ui.boton_calcular.setEnabled(False)
        self.ui.etiqueta1.setEnabled(False)
        self.ui.etiqueta2.setEnabled(False)
        self.ui.num1.setEnabled(False)
        self.ui.num2.setEnabled(False)
        self.ui.sumar.setEnabled(False)
        self.ui.restar.setEnabled(False)
        self.ui.resultado.setEnabled(False)

    def activa_c(self):
        self.ui.calendario.setEnabled(True)

    def desactiva_c(self):
        self.ui.calendario.setEnabled(False)

    def calcular(self):
        if len(self.ui.num1.text()) != 0:
            n1 = int(self.ui.num1.text())
        else:
            n1 =0
        if len(self.ui.num2.text()) != 0:
            n2 = int(self.ui.num2.text())
        else:
            n2 =0
        if self.ui.sumar.isChecked() == True:
            res = n1 + n2
        else:
            res = n1 - n2
        self.ui.resultado.setText(str(res))


if __name__ == "__main__": 
   app = QtGui.QApplication(sys.argv)
   myapp = MyForm()
   myapp.show() 
   sys.exit(app.exec_()) 
