import sys
from PyQt4 import QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

class Mpl_Canvas111(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)

class MatplotlibWidget111(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = Mpl_Canvas111()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.vbl.addWidget(self.toolbar)
        self.setLayout(self.vbl)
    def grafico(self):
        X = list(range(50))
        Y1 = [1/(x+5) for x in X]
        self.canvas.ax.plot(X, Y1)

Mi_App = QtGui.QApplication(sys.argv)
Mi_Widget = MatplotlibWidget111()
Mi_Widget.grafico()
Mi_Widget.show()
sys.exit(Mi_App.exec_())

