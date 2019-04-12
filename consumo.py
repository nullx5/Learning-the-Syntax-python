# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consumo.ui'
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
        Dialog.resize(844, 615)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 60, 211, 371))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 162, 311))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.enero = QtGui.QLineEdit(self.formLayoutWidget)
        self.enero.setObjectName(_fromUtf8("enero"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.enero)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtGui.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtGui.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_12)
        self.febrero = QtGui.QLineEdit(self.formLayoutWidget)
        self.febrero.setObjectName(_fromUtf8("febrero"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.febrero)
        self.marzo = QtGui.QLineEdit(self.formLayoutWidget)
        self.marzo.setObjectName(_fromUtf8("marzo"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.marzo)
        self.abril = QtGui.QLineEdit(self.formLayoutWidget)
        self.abril.setObjectName(_fromUtf8("abril"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.abril)
        self.mayo = QtGui.QLineEdit(self.formLayoutWidget)
        self.mayo.setObjectName(_fromUtf8("mayo"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.mayo)
        self.junio = QtGui.QLineEdit(self.formLayoutWidget)
        self.junio.setObjectName(_fromUtf8("junio"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.junio)
        self.julio = QtGui.QLineEdit(self.formLayoutWidget)
        self.julio.setObjectName(_fromUtf8("julio"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.julio)
        self.agosto = QtGui.QLineEdit(self.formLayoutWidget)
        self.agosto.setObjectName(_fromUtf8("agosto"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.agosto)
        self.septiembre = QtGui.QLineEdit(self.formLayoutWidget)
        self.septiembre.setObjectName(_fromUtf8("septiembre"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.septiembre)
        self.octubre = QtGui.QLineEdit(self.formLayoutWidget)
        self.octubre.setObjectName(_fromUtf8("octubre"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.octubre)
        self.noviembre = QtGui.QLineEdit(self.formLayoutWidget)
        self.noviembre.setObjectName(_fromUtf8("noviembre"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.noviembre)
        self.diciembre = QtGui.QLineEdit(self.formLayoutWidget)
        self.diciembre.setObjectName(_fromUtf8("diciembre"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.diciembre)
        self.grafico = MatplotlibWidget11_sin(Dialog)
        self.grafico.setGeometry(QtCore.QRect(300, 60, 501, 381))
        self.grafico.setObjectName(_fromUtf8("grafico"))
        self.boton = QtGui.QPushButton(Dialog)
        self.boton.setGeometry(QtCore.QRect(300, 460, 501, 101))
        self.boton.setObjectName(_fromUtf8("boton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Consumo de gas mensual", None))
        self.groupBox.setTitle(_translate("Dialog", "Consumo", None))
        self.label.setText(_translate("Dialog", "Enero", None))
        self.label_2.setText(_translate("Dialog", "Febrero", None))
        self.label_3.setText(_translate("Dialog", "Marzo", None))
        self.label_4.setText(_translate("Dialog", "Abril", None))
        self.label_5.setText(_translate("Dialog", "Mayo", None))
        self.label_6.setText(_translate("Dialog", "Junio", None))
        self.label_7.setText(_translate("Dialog", "Julio", None))
        self.label_8.setText(_translate("Dialog", "Agosto", None))
        self.label_9.setText(_translate("Dialog", "Septiembre", None))
        self.label_10.setText(_translate("Dialog", "Octubre", None))
        self.label_11.setText(_translate("Dialog", "Noviembre", None))
        self.label_12.setText(_translate("Dialog", "Diciembre", None))
        self.boton.setText(_translate("Dialog", "Generar grafico", None))

from clases_mpl_pyqt import MatplotlibWidget11_sin
