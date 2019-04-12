# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_table_2.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(978, 634)
        self.tabla = QtGui.QTableWidget(Dialog)
        self.tabla.setGeometry(QtCore.QRect(130, 50, 324, 325))
        self.tabla.setRowCount(10)
        self.tabla.setColumnCount(3)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        item = QtGui.QTableWidgetItem()
        self.tabla.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tabla.setItem(0, 1, item)
        self.tabla.horizontalHeader().setVisible(True)
        self.boton_cargar = QtGui.QPushButton(Dialog)
        self.boton_cargar.setGeometry(QtCore.QRect(129, 390, 326, 82))
        self.boton_cargar.setObjectName(_fromUtf8("boton_cargar"))
        self.boton_borrar = QtGui.QPushButton(Dialog)
        self.boton_borrar.setGeometry(QtCore.QRect(130, 480, 326, 82))
        self.boton_borrar.setObjectName(_fromUtf8("boton_borrar"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(530, 170, 341, 251))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.filas = QtGui.QLineEdit(self.groupBox)
        self.filas.setGeometry(QtCore.QRect(192, 60, 81, 20))
        self.filas.setObjectName(_fromUtf8("filas"))
        self.columnas = QtGui.QLineEdit(self.groupBox)
        self.columnas.setGeometry(QtCore.QRect(192, 100, 81, 20))
        self.columnas.setObjectName(_fromUtf8("columnas"))
        self.boton_modificar = QtGui.QPushButton(self.groupBox)
        self.boton_modificar.setGeometry(QtCore.QRect(70, 150, 201, 61))
        self.boton_modificar.setObjectName(_fromUtf8("boton_modificar"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 60, 111, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 111, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        __sortingEnabled = self.tabla.isSortingEnabled()
        self.tabla.setSortingEnabled(False)
        self.tabla.setSortingEnabled(__sortingEnabled)
        self.boton_cargar.setText(_translate("Dialog", "Cargar lista", None))
        self.boton_borrar.setText(_translate("Dialog", "Borrar lista", None))
        self.groupBox.setTitle(_translate("Dialog", "Modificar número de filas y columnas", None))
        self.boton_modificar.setText(_translate("Dialog", "Modificar", None))
        self.label.setText(_translate("Dialog", "Número de filas:", None))
        self.label_2.setText(_translate("Dialog", "Número de columnas:", None))

