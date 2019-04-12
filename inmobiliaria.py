# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inmobiliaria.ui'
#
# Created: Thu Jun  2 04:34:02 2016
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

class Ui_Ficha(object):
    def setupUi(self, Ficha):
        Ficha.setObjectName(_fromUtf8("Ficha"))
        Ficha.resize(602, 352)
        self.gridLayoutWidget_2 = QtGui.QWidget(Ficha)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 50, 291, 194))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 5, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.tipo = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.tipo.setObjectName(_fromUtf8("tipo"))
        self.gridLayout_2.addWidget(self.tipo, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.localidad = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.localidad.setObjectName(_fromUtf8("localidad"))
        self.gridLayout_2.addWidget(self.localidad, 0, 1, 1, 1)
        self.plaza_garaje = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.plaza_garaje.setObjectName(_fromUtf8("plaza_garaje"))
        self.gridLayout_2.addWidget(self.plaza_garaje, 6, 1, 1, 1)
        self.num_ba = QtGui.QSlider(self.gridLayoutWidget_2)
        self.num_ba.setMinimum(1)
        self.num_ba.setMaximum(3)
        self.num_ba.setPageStep(1)
        self.num_ba.setOrientation(QtCore.Qt.Horizontal)
        self.num_ba.setTickPosition(QtGui.QSlider.TicksBelow)
        self.num_ba.setObjectName(_fromUtf8("num_ba"))
        self.gridLayout_2.addWidget(self.num_ba, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.num_hab = QtGui.QSlider(self.gridLayoutWidget_2)
        self.num_hab.setMinimum(1)
        self.num_hab.setMaximum(5)
        self.num_hab.setPageStep(1)
        self.num_hab.setOrientation(QtCore.Qt.Horizontal)
        self.num_hab.setTickPosition(QtGui.QSlider.TicksAbove)
        self.num_hab.setObjectName(_fromUtf8("num_hab"))
        self.gridLayout_2.addWidget(self.num_hab, 3, 1, 1, 1)
        self.salida = QtGui.QLabel(Ficha)
        self.salida.setGeometry(QtCore.QRect(50, 250, 501, 41))
        self.salida.setFrameShape(QtGui.QFrame.StyledPanel)
        self.salida.setAlignment(QtCore.Qt.AlignCenter)
        self.salida.setObjectName(_fromUtf8("salida"))
        self.buscar = QtGui.QPushButton(Ficha)
        self.buscar.setGeometry(QtCore.QRect(390, 50, 161, 151))
        self.buscar.setObjectName(_fromUtf8("buscar"))

        self.retranslateUi(Ficha)
        QtCore.QMetaObject.connectSlotsByName(Ficha)

    def retranslateUi(self, Ficha):
        Ficha.setWindowTitle(_translate("Ficha", "Inmobiliaria", None))
        self.label_12.setText(_translate("Ficha", " 1                        2                       3", None))
        self.label_2.setText(_translate("Ficha", "Número de habitaciones:", None))
        self.label_5.setText(_translate("Ficha", " 1           2           3          4           5", None))
        self.label_4.setText(_translate("Ficha", "Localidad:", None))
        self.label_6.setText(_translate("Ficha", "Número de baños/aseos:", None))
        self.plaza_garaje.setText(_translate("Ficha", "Plaza de garaje", None))
        self.label.setText(_translate("Ficha", "Tipo de inmueble:", None))
        self.salida.setText(_translate("Ficha", "Sin búsqueda", None))
        self.buscar.setText(_translate("Ficha", "Buscar", None))

