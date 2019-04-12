import sys
from consumo2 import *
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
        self.ui.junio.setText("15")
        self.ui.julio.setText("12")
        self.ui.agosto.setText("9")
        self.ui.septiembre.setText("17")
        self.ui.octubre.setText("21")
        self.ui.noviembre.setText("33")
        self.ui.diciembre.setText(("45"))
        self.ui.grafico.setVisible(False)
        #self.graficar_funcion()
        QtCore.QObject.connect(self.ui.boton, QtCore.SIGNAL('clicked()'), self.graficar_funcion)

    def graficar_funcion(self):
        self.ui.grafico.setVisible(True)
        X = [i for i in range(1, 13)]
        meses = ["E", "F", "M", "A"," M" ,"J","J","A","S","O","N","D"]
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

        self.ui.grafico.canvas.ax1.clear()
        self.ui.grafico.canvas.ax1.set_xlim([0.5,12.5])
        self.ui.grafico.canvas.ax1.set_ylim([0,max(data)* 1.1])
        self.ui.grafico.canvas.ax1.set_xticks(X)
        self.ui.grafico.canvas.ax1.set_xticklabels(meses)
        self.ui.grafico.canvas.ax1.bar(X, data, align = 'center', width = 1)

        self.ui.grafico.canvas.ax2.clear()
        self.ui.grafico.canvas.ax2.set_xlim([1,12])
        self.ui.grafico.canvas.ax2.set_ylim([0,max(data)* 1.1])
        self.ui.grafico.canvas.ax2.set_xticks(X)
        self.ui.grafico.canvas.ax2.set_xticklabels(X, fontsize = 8, color = "red")
        self.ui.grafico.canvas.ax2.yaxis.set_tick_params(labelsize= 8, labelcolor = "blue")
        self.ui.grafico.canvas.ax2.grid(axis = "both", color = "0.7", linestyle = '-')
        self.ui.grafico.canvas.ax2.plot(X, data, color ="green")

        self.ui.grafico.canvas.ax3.clear()
        self.ui.grafico.canvas.ax3.set_xlim([0.5,12.5])
        self.ui.grafico.canvas.ax3.set_ylim([0,max(data)* 1.1])
        self.ui.grafico.canvas.ax3.set_xticks(X)
        self.ui.grafico.canvas.ax3.set_xticklabels(X, fontsize = 8)
        self.ui.grafico.canvas.ax3.yaxis.set_tick_params(labelsize= 8)
        self.ui.grafico.canvas.ax3.grid(axis = "y", color = "0.3", linestyle = '-')
        self.ui.grafico.canvas.ax3.scatter(X, data, color= "magenta")

        self.ui.grafico.canvas.ax4.clear()
        self.ui.grafico.canvas.ax4.pie(data, labels = meses)
        self.ui.grafico.canvas.draw()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MiFormulario()
    myapp.show()
    sys.exit(app.exec_())
