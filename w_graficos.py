# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_graficos.ui'
#
# Created: Thu Jun  2 13:27:41 2016
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
        Dialog.resize(1124, 890)
        self.graficos_1 = QtGui.QGraphicsView(Dialog)
        self.graficos_1.setGeometry(QtCore.QRect(30, 260, 291, 281))
        self.graficos_1.setObjectName(_fromUtf8("graficos_1"))
        self.graficos_2 = QtGui.QGraphicsView(Dialog)
        self.graficos_2.setGeometry(QtCore.QRect(350, 50, 741, 801))
        self.graficos_2.setObjectName(_fromUtf8("graficos_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))

