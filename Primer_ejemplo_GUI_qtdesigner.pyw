
import sys
from Primer_ejemplo_GUI_qtdesigner import *

class Mi_Widget(QtGui.QWidget):
      def __init__(self, parent=None):
          QtGui.QWidget.__init__(self, parent)
          self.ui = Ui_Form()
          self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mi_app = Mi_Widget()
    mi_app.show()
    sys.exit(app.exec_())
