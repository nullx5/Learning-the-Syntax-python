# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consumo_i.ui'
#
# Created: Sun Jun  5 19:51:24 2016
#      by: PyQt4 UI code generator 4.10.4
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
        Dialog.resize(844, 507)
        self.grafico = MatplotlibWidget11_sin(Dialog)
        self.grafico.setGeometry(QtCore.QRect(300, 60, 501, 381))
        self.grafico.setObjectName(_fromUtf8("grafico"))
        self.lista = QtGui.QTextEdit(Dialog)
        self.lista.setGeometry(QtCore.QRect(40, 60, 221, 381))
        self.lista.setObjectName(_fromUtf8("lista"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Ejemplo interactivo", None))

from clases_mpl_pyqt import MatplotlibWidget11_sin
