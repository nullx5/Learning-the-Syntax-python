# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hotel.ui'
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

class Ui_Reserva(object):
    def setupUi(self, Reserva):
        Reserva.setObjectName(_fromUtf8("Reserva"))
        Reserva.resize(602, 352)
        self.gridLayoutWidget_2 = QtGui.QWidget(Reserva)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 50, 311, 151))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.tipo_hab = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.tipo_hab.setObjectName(_fromUtf8("tipo_hab"))
        self.gridLayout_2.addWidget(self.tipo_hab, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.fecha_entrada = QtGui.QDateEdit(self.gridLayoutWidget_2)
        self.fecha_entrada.setDate(QtCore.QDate(2015, 10, 29))
        self.fecha_entrada.setCalendarPopup(True)
        self.fecha_entrada.setObjectName(_fromUtf8("fecha_entrada"))
        self.gridLayout_2.addWidget(self.fecha_entrada, 0, 1, 1, 1)
        self.fecha_salida = QtGui.QDateEdit(self.gridLayoutWidget_2)
        self.fecha_salida.setDate(QtCore.QDate(2015, 10, 29))
        self.fecha_salida.setCalendarPopup(True)
        self.fecha_salida.setObjectName(_fromUtf8("fecha_salida"))
        self.gridLayout_2.addWidget(self.fecha_salida, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.plaza_garaje = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.plaza_garaje.setObjectName(_fromUtf8("plaza_garaje"))
        self.gridLayout_2.addWidget(self.plaza_garaje, 3, 1, 1, 1)
        self.salida = QtGui.QLabel(Reserva)
        self.salida.setGeometry(QtCore.QRect(50, 250, 501, 41))
        self.salida.setFrameShape(QtGui.QFrame.StyledPanel)
        self.salida.setAlignment(QtCore.Qt.AlignCenter)
        self.salida.setObjectName(_fromUtf8("salida"))
        self.reservar = QtGui.QPushButton(Reserva)
        self.reservar.setGeometry(QtCore.QRect(390, 50, 161, 151))
        self.reservar.setObjectName(_fromUtf8("reservar"))

        self.retranslateUi(Reserva)
        QtCore.QMetaObject.connectSlotsByName(Reserva)

    def retranslateUi(self, Reserva):
        Reserva.setWindowTitle(_translate("Reserva", "Reserva de Hotel", None))
        self.label_4.setText(_translate("Reserva", "Fecha entrada", None))
        self.label.setText(_translate("Reserva", "Tipo de habitación", None))
        self.label_2.setText(_translate("Reserva", "Fecha salida", None))
        self.plaza_garaje.setText(_translate("Reserva", "Plaza de garaje", None))
        self.salida.setText(_translate("Reserva", "Aún no se ha hecho ninguna reserva", None))
        self.reservar.setText(_translate("Reserva", "Reservar", None))

