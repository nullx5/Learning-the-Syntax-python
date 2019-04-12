import sys
from consumo_i import *
import matplotlib as mpl
import matplotlib.patches as patches
import matplotlib.lines as lines

class MiFormulario(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.grafico.canvas.ax.axis([0,100,0,100])
        self.ui.grafico.canvas.ax.plot([0,0],[100,0], color ="blue", lw=2)
        self.ui.grafico.canvas.ax.plot([100,0],[100,100], color ="blue", lw=2)
        self.ui.grafico.canvas.ax.plot([100,100],[100,0], color ="blue", lw=2)
        self.ui.grafico.canvas.ax.plot([100,0],[0,0], color ="blue", lw=2)
        self.ui.grafico.canvas.ax.plot([0,100],[50,50], color ="blue", lw=1)
        self.ui.grafico.canvas.ax.plot([50,50],[0,100], color ="blue", lw=1)
        self.ui.grafico.canvas.ax.text(25,75,"Patatas", horizontalalignment= "center")
        self.ui.grafico.canvas.ax.text(75,75,"Alubias", horizontalalignment= "center")
        self.ui.grafico.canvas.ax.text(25,25,"Ajos", horizontalalignment= "center")
        self.ui.grafico.canvas.ax.text(75,25,"Melocotones", horizontalalignment= "center")
        self.ui.grafico.canvas.ax.axis('off')
        self.patatas = self.alubias = self.ajos = self.melocotones =  False
        self.ui.grafico.canvas.mpl_connect('button_press_event', mi_procesado)

def mi_procesado(event):
    if((0<event.xdata<50) and (50<event.ydata<100) and (myapp.patatas == False)):
        myapp.ui.lista.append("Patatas")
        myapp.ui.grafico.canvas.ax.add_patch(patches.Rectangle((0, 50), 50, 50 ,color = "green"))
        myapp.ui.grafico.canvas.draw_idle()
        myapp.patatas = True
    if((50<event.xdata<100) and (50<event.ydata<100)and (myapp.alubias == False)):
        myapp.ui.lista.append("Alubias")
        myapp.ui.grafico.canvas.ax.add_patch(patches.Rectangle((50, 50), 50, 50 ,color = "blue"))
        myapp.ui.grafico.canvas.draw_idle()
        myapp.alubias = True
    if((0<event.xdata<50) and (0<event.ydata<50)and (myapp.ajos == False)):
        myapp.ui.lista.append("Ajos")
        myapp.ui.grafico.canvas.ax.add_patch(patches.Rectangle((0, 0), 50, 50 ,color = "red"))
        myapp.ui.grafico.canvas.draw_idle()
        myapp.ajos = True
    if((50<event.xdata<100) and (0<event.ydata<50)and (myapp.melocotones == False)):
        myapp.ui.lista.append("Melocotones")
        myapp.ui.grafico.canvas.ax.add_patch(patches.Rectangle((50, 0), 50, 50 ,color = (0.7,0.5,0.7)))
        myapp.ui.grafico.canvas.draw_idle()
        myapp.melocotones = True

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MiFormulario()
    myapp.show()
    patatas = alubias = ajos = melocotones =  False
    sys.exit(app.exec_())


