# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_web.ui'
#
# Created: Fri Jun  3 01:54:00 2016
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
        Dialog.resize(1127, 890)
        self.pagina_web = QtWebKit.QWebView(Dialog)
        self.pagina_web.setGeometry(QtCore.QRect(40, 80, 1041, 771))
        self.pagina_web.setUrl(QtCore.QUrl(_fromUtf8("https://www.python.org/")))
        self.pagina_web.setObjectName(_fromUtf8("pagina_web"))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 1041, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.direccion = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.direccion.setObjectName(_fromUtf8("direccion"))
        self.horizontalLayout.addWidget(self.direccion)
        self.boton_cargar = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.boton_cargar.setObjectName(_fromUtf8("boton_cargar"))
        self.horizontalLayout.addWidget(self.boton_cargar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Dirección: ", None))
        self.boton_cargar.setText(_translate("Dialog", "Cargar", None))

from PyQt4 import QtWebKit
