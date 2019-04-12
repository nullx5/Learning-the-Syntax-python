# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_table.ui'
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
        Dialog.resize(578, 619)
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        __sortingEnabled = self.tabla.isSortingEnabled()
        self.tabla.setSortingEnabled(False)
        self.tabla.setSortingEnabled(__sortingEnabled)
        self.boton_cargar.setText(_translate("Dialog", "Cargar lista", None))
        self.boton_borrar.setText(_translate("Dialog", "Borrar lista", None))

