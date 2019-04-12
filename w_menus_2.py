# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_menus_2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(804, 522)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.boton_calcular = QtGui.QPushButton(self.centralwidget)
        self.boton_calcular.setEnabled(False)
        self.boton_calcular.setGeometry(QtCore.QRect(130, 210, 221, 111))
        self.boton_calcular.setObjectName(_fromUtf8("boton_calcular"))
        self.sumar = QtGui.QRadioButton(self.centralwidget)
        self.sumar.setEnabled(False)
        self.sumar.setGeometry(QtCore.QRect(130, 180, 82, 17))
        self.sumar.setObjectName(_fromUtf8("sumar"))
        self.restar = QtGui.QRadioButton(self.centralwidget)
        self.restar.setEnabled(False)
        self.restar.setGeometry(QtCore.QRect(260, 180, 82, 17))
        self.restar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.restar.setObjectName(_fromUtf8("restar"))
        self.calendario = QtGui.QCalendarWidget(self.centralwidget)
        self.calendario.setEnabled(False)
        self.calendario.setGeometry(QtCore.QRect(420, 130, 281, 191))
        self.calendario.setObjectName(_fromUtf8("calendario"))
        self.resultado = QtGui.QLineEdit(self.centralwidget)
        self.resultado.setEnabled(False)
        self.resultado.setGeometry(QtCore.QRect(130, 330, 221, 41))
        self.resultado.setObjectName(_fromUtf8("resultado"))
        self.num1 = QtGui.QLineEdit(self.centralwidget)
        self.num1.setEnabled(False)
        self.num1.setGeometry(QtCore.QRect(220, 100, 113, 20))
        self.num1.setObjectName(_fromUtf8("num1"))
        self.num2 = QtGui.QLineEdit(self.centralwidget)
        self.num2.setEnabled(False)
        self.num2.setGeometry(QtCore.QRect(220, 130, 113, 20))
        self.num2.setObjectName(_fromUtf8("num2"))
        self.etiqueta1 = QtGui.QLabel(self.centralwidget)
        self.etiqueta1.setEnabled(False)
        self.etiqueta1.setGeometry(QtCore.QRect(130, 100, 81, 21))
        self.etiqueta1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.etiqueta1.setObjectName(_fromUtf8("etiqueta1"))
        self.etiqueta2 = QtGui.QLabel(self.centralwidget)
        self.etiqueta2.setEnabled(False)
        self.etiqueta2.setGeometry(QtCore.QRect(130, 130, 81, 21))
        self.etiqueta2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.etiqueta2.setObjectName(_fromUtf8("etiqueta2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(100, 70, 281, 341))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox.raise_()
        self.boton_calcular.raise_()
        self.sumar.raise_()
        self.restar.raise_()
        self.calendario.raise_()
        self.resultado.raise_()
        self.num1.raise_()
        self.num2.raise_()
        self.etiqueta1.raise_()
        self.etiqueta2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFicheros = QtGui.QMenu(self.menuBar)
        self.menuFicheros.setObjectName(_fromUtf8("menuFicheros"))
        self.menu_Desactivaciones = QtGui.QMenu(self.menuBar)
        self.menu_Desactivaciones.setObjectName(_fromUtf8("menu_Desactivaciones"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.aa = QtGui.QAction(MainWindow)
        self.aa.setObjectName(_fromUtf8("aa"))
        self.ac = QtGui.QAction(MainWindow)
        self.ac.setObjectName(_fromUtf8("ac"))
        self.da = QtGui.QAction(MainWindow)
        self.da.setObjectName(_fromUtf8("da"))
        self.dc = QtGui.QAction(MainWindow)
        self.dc.setObjectName(_fromUtf8("dc"))
        self.action1 = QtGui.QAction(MainWindow)
        self.action1.setObjectName(_fromUtf8("action1"))
        self.action2 = QtGui.QAction(MainWindow)
        self.action2.setObjectName(_fromUtf8("action2"))
        self.menuFicheros.addAction(self.aa)
        self.menuFicheros.addAction(self.ac)
        self.menu_Desactivaciones.addAction(self.da)
        self.menu_Desactivaciones.addAction(self.dc)
        self.menuBar.addAction(self.menuFicheros.menuAction())
        self.menuBar.addAction(self.menu_Desactivaciones.menuAction())
        self.toolBar.addAction(self.action1)
        self.toolBar.addAction(self.action2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.boton_calcular.setText(_translate("MainWindow", "Calcular", None))
        self.sumar.setText(_translate("MainWindow", "Sumar", None))
        self.restar.setText(_translate("MainWindow", "Restar", None))
        self.etiqueta1.setText(_translate("MainWindow", "Número 1:", None))
        self.etiqueta2.setText(_translate("MainWindow", "Número 2:", None))
        self.menuFicheros.setTitle(_translate("MainWindow", "&Activaciones", None))
        self.menu_Desactivaciones.setTitle(_translate("MainWindow", "&Desactivaciones", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.aa.setText(_translate("MainWindow", "Activar aplicación", None))
        self.aa.setStatusTip(_translate("MainWindow", "Se activarán todos los elementos de la aplicación", None))
        self.ac.setText(_translate("MainWindow", "Activar calendario", None))
        self.ac.setStatusTip(_translate("MainWindow", "Se activará el calendario", None))
        self.da.setText(_translate("MainWindow", "Desactivar aplicación", None))
        self.da.setStatusTip(_translate("MainWindow", "Se desactivarán todos los elementos de la aplicación", None))
        self.dc.setText(_translate("MainWindow", "Desactivar calendario", None))
        self.dc.setStatusTip(_translate("MainWindow", "Se desactivará el calendario", None))
        self.action1.setText(_translate("MainWindow", "1", None))
        self.action2.setText(_translate("MainWindow", "2", None))


