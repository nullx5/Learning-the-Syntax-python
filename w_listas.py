# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_listas.ui'
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
        Dialog.resize(895, 520)
        self.lista = QtGui.QListWidget(Dialog)
        self.lista.setGeometry(QtCore.QRect(440, 70, 360, 251))
        self.lista.setObjectName(_fromUtf8("lista"))
        self.nombres = QtGui.QLineEdit(Dialog)
        self.nombres.setGeometry(QtCore.QRect(210, 70, 191, 31))
        self.nombres.setObjectName(_fromUtf8("nombres"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 70, 131, 31))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(440, 30, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.boton_guardar = QtGui.QPushButton(Dialog)
        self.boton_guardar.setGeometry(QtCore.QRect(210, 130, 191, 191))
        self.boton_guardar.setObjectName(_fromUtf8("boton_guardar"))
        self.boton_editar = QtGui.QPushButton(Dialog)
        self.boton_editar.setGeometry(QtCore.QRect(210, 340, 191, 101))
        self.boton_editar.setObjectName(_fromUtf8("boton_editar"))
        self.boton_borrar = QtGui.QPushButton(Dialog)
        self.boton_borrar.setGeometry(QtCore.QRect(410, 340, 191, 101))
        self.boton_borrar.setObjectName(_fromUtf8("boton_borrar"))
        self.boton_borrar_todo = QtGui.QPushButton(Dialog)
        self.boton_borrar_todo.setGeometry(QtCore.QRect(610, 340, 191, 101))
        self.boton_borrar_todo.setObjectName(_fromUtf8("boton_borrar_todo"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Nombre del invitado/a:", None))
        self.label_2.setText(_translate("Dialog", "Lista de invitados", None))
        self.boton_guardar.setText(_translate("Dialog", "Guardar nombre", None))
        self.boton_editar.setText(_translate("Dialog", "Editar nombre", None))
        self.boton_borrar.setText(_translate("Dialog", "Eliminar un invitado", None))
        self.boton_borrar_todo.setText(_translate("Dialog", "Eliminar todos los invitados", None))

