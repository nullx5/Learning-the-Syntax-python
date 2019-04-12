import sys 
from w_table_2 import *
from PyQt4.QtGui import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.saca_lista()
        self.ui.boton_cargar.clicked.connect(self.saca_lista)
        self.ui.boton_borrar.clicked.connect(self.ui.tabla.clear)
        self.ui.boton_modificar.clicked.connect(self.modifica)

    def saca_lista(self):
        self.ui.tabla.setGeometry(100,50,382,325)
        self.ui.tabla.setHorizontalHeaderLabels(["Enero", "Febrero", "Marzo"])
        self.ui.tabla.setVerticalHeaderLabels(["Manzanas", "Peras", "Melocotones", "Alberchigos", "Ciruelas", \
                                               "Nueces", "Avellanas", "Platanos", "Melones", "Calabazas" ])
        fila = 0
        for vector_fila in datos:
            columna = 0
            for elemento in vector_fila:
                elemento_tabla = QTableWidgetItem(str(elemento))
                self.ui.tabla.setItem(fila, columna, elemento_tabla)
                columna += 1
            fila += 1

    def modifica(self):
        self.ui.tabla.setRowCount(int(self.ui.filas.text()))
        self.ui.tabla.setColumnCount(int(self.ui.columnas.text()))



datos = [[10, 34, 21], [87, 45, 90],[56, 87, 4], [2, 8,11 ], [77, 87, 4],\
         [1, 2,32 ],[3, 21, 87], [5, 8,2 ],[88, 55, 7], [2, 4,56]]

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())