import sys
from consumo import *
import matplotlib.ticker as ticker

class MiFormulario(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.enero.setText("62")
        self.ui.febrero.setText("67")
        self.ui.marzo.setText("51")
        self.ui.abril.setText("42")
        self.ui.mayo.setText("29")
        self.ui.junio.setText("10")
        self.ui.julio.setText("9")
        self.ui.agosto.setText("3")
        self.ui.septiembre.setText("14")
        self.ui.octubre.setText("21")
        self.ui.noviembre.setText("33")
        self.ui.diciembre.setText(("45"))
        QtCore.QObject.connect(self.ui.boton, QtCore.SIGNAL('clicked()'), self.graficar_funcion)

    def graficar_funcion(self):
        meses = ["Ene", "Feb", "Mar", "Abr"," May" ,"Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
        X = [i for i in range(12)]
        data = []
        data.append(int(self.ui.enero.text()))
        data.append(int(self.ui.febrero.text()))
        data.append(int(self.ui.marzo.text()))
        data.append(int(self.ui.abril.text()))
        data.append(int(self.ui.mayo.text()))
        data.append(int(self.ui.junio.text()))
        data.append(int(self.ui.julio.text()))
        data.append(int(self.ui.agosto.text()))
        data.append(int(self.ui.septiembre.text()))
        data.append(int(self.ui.octubre.text()))
        data.append(int(self.ui.noviembre.text()))
        data.append(int(self.ui.diciembre.text()))
        self.ui.grafico.canvas.ax.clear()
        self.ui.grafico.canvas.ax.axis([-0.5,11.5, 0,max(data)+10])
        self.ui.grafico.canvas.ax.xaxis.set_major_locator(ticker.FixedLocator((X)))
        self.ui.grafico.canvas.ax.xaxis.set_major_formatter(ticker.FixedFormatter((meses)))
        self.ui.grafico.canvas.ax.bar(X, data, align = 'center', width = 1)
        self.ui.grafico.canvas.draw()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MiFormulario()
    myapp.show()
    sys.exit(app.exec_())
