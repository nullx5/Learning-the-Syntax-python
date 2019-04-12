import sys
from PyQt4 import QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class Mpl_Canvas111(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
    def grafico(self):
        X = list(range(50))
        Y1 = [1/(x+5) for x in X]
        self.ax.plot(X, Y1)

Mi_App = QtGui.QApplication(sys.argv)
Mi_Canvas = Mpl_Canvas111()
Mi_Canvas.grafico()
Mi_Canvas.show()
sys.exit(Mi_App.exec_())

