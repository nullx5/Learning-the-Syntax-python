# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spin.ui'
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
        Dialog.resize(386, 348)
        self.uno = QtGui.QDoubleSpinBox(Dialog)
        self.uno.setGeometry(QtCore.QRect(50, 40, 131, 31))
        self.uno.setMaximum(100.0)
        self.uno.setSingleStep(1.0)
        self.uno.setObjectName(_fromUtf8("uno"))
        self.dos = QtGui.QDoubleSpinBox(Dialog)
        self.dos.setGeometry(QtCore.QRect(50, 100, 131, 31))
        self.dos.setMaximum(50.0)
        self.dos.setSingleStep(0.5)
        self.dos.setObjectName(_fromUtf8("dos"))
        self.tres = QtGui.QDoubleSpinBox(Dialog)
        self.tres.setGeometry(QtCore.QRect(50, 160, 131, 31))
        self.tres.setMaximum(25.0)
        self.tres.setSingleStep(0.25)
        self.tres.setObjectName(_fromUtf8("tres"))
        self.g_1 = QtGui.QProgressBar(Dialog)
        self.g_1.setGeometry(QtCore.QRect(210, 40, 131, 31))
        self.g_1.setProperty("value", 0)
        self.g_1.setObjectName(_fromUtf8("g_1"))
        self.g_2 = QtGui.QProgressBar(Dialog)
        self.g_2.setGeometry(QtCore.QRect(210, 100, 131, 31))
        self.g_2.setProperty("value", 0)
        self.g_2.setObjectName(_fromUtf8("g_2"))
        self.g_3 = QtGui.QProgressBar(Dialog)
        self.g_3.setGeometry(QtCore.QRect(210, 160, 131, 31))
        self.g_3.setProperty("value", 0)
        self.g_3.setObjectName(_fromUtf8("g_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 230, 171, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.suma = QtGui.QLineEdit(Dialog)
        self.suma.setGeometry(QtCore.QRect(220, 230, 91, 21))
        self.suma.setFrame(False)
        self.suma.setReadOnly(True)
        self.suma.setObjectName(_fromUtf8("suma"))
        self.error = QtGui.QLabel(Dialog)
        self.error.setEnabled(False)
        self.error.setGeometry(QtCore.QRect(2, 270, 381, 31))
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName(_fromUtf8("error"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "La suma de los tres elementos es:", None))
        self.error.setText(_translate("Dialog", "¡Error! Se ha sobrepasado el límite de 100 para la suma", None))

