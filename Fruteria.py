# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fruteria.ui'
#
# Created: Tue Jul  2 02:48:13 2019
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
        Dialog.resize(771, 374)
        Dialog.setWhatsThis(_fromUtf8(""))
        Dialog.setStyleSheet(_fromUtf8("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(400, 310, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 80, 161, 111))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.op_ma = QtGui.QCheckBox(self.formLayoutWidget)
        self.op_ma.setObjectName(_fromUtf8("op_ma"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.op_ma)
        self.cant_ma = QtGui.QSpinBox(self.formLayoutWidget)
        self.cant_ma.setWrapping(False)
        self.cant_ma.setKeyboardTracking(True)
        self.cant_ma.setObjectName(_fromUtf8("cant_ma"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cant_ma)
        self.op_pe = QtGui.QCheckBox(self.formLayoutWidget)
        self.op_pe.setObjectName(_fromUtf8("op_pe"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.op_pe)
        self.cant_pe = QtGui.QSpinBox(self.formLayoutWidget)
        self.cant_pe.setObjectName(_fromUtf8("cant_pe"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cant_pe)
        self.op_pl = QtGui.QCheckBox(self.formLayoutWidget)
        self.op_pl.setObjectName(_fromUtf8("op_pl"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.op_pl)
        self.cant_pl = QtGui.QSpinBox(self.formLayoutWidget)
        self.cant_pl.setObjectName(_fromUtf8("cant_pl"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cant_pl)
        self.precio_fruta = QtGui.QLineEdit(self.formLayoutWidget)
        self.precio_fruta.setReadOnly(True)
        self.precio_fruta.setObjectName(_fromUtf8("precio_fruta"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.precio_fruta)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.formLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(240, 80, 151, 111))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.op_ac = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.op_ac.setObjectName(_fromUtf8("op_ac"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.op_ac)
        self.cant_ac = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.cant_ac.setObjectName(_fromUtf8("cant_ac"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cant_ac)
        self.op_bo = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.op_bo.setObjectName(_fromUtf8("op_bo"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.op_bo)
        self.cant_bo = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.cant_bo.setObjectName(_fromUtf8("cant_bo"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.cant_bo)
        self.op_ca = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.op_ca.setObjectName(_fromUtf8("op_ca"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.op_ca)
        self.cant_ca = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.cant_ca.setObjectName(_fromUtf8("cant_ca"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.cant_ca)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.precio_verdura = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.precio_verdura.setReadOnly(True)
        self.precio_verdura.setObjectName(_fromUtf8("precio_verdura"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.precio_verdura)
        self.formLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(420, 80, 161, 111))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.op_al = QtGui.QCheckBox(self.formLayoutWidget_3)
        self.op_al.setObjectName(_fromUtf8("op_al"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.op_al)
        self.cant_al = QtGui.QSpinBox(self.formLayoutWidget_3)
        self.cant_al.setObjectName(_fromUtf8("cant_al"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.cant_al)
        self.op_le = QtGui.QCheckBox(self.formLayoutWidget_3)
        self.op_le.setObjectName(_fromUtf8("op_le"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.op_le)
        self.cant_le = QtGui.QSpinBox(self.formLayoutWidget_3)
        self.cant_le.setObjectName(_fromUtf8("cant_le"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.cant_le)
        self.op_ga = QtGui.QCheckBox(self.formLayoutWidget_3)
        self.op_ga.setObjectName(_fromUtf8("op_ga"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.op_ga)
        self.cant_ga = QtGui.QSpinBox(self.formLayoutWidget_3)
        self.cant_ga.setObjectName(_fromUtf8("cant_ga"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.cant_ga)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.precio_legumbre = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.precio_legumbre.setReadOnly(True)
        self.precio_legumbre.setObjectName(_fromUtf8("precio_legumbre"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.precio_legumbre)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(420, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.salida = QtGui.QLabel(Dialog)
        self.salida.setGeometry(QtCore.QRect(50, 270, 701, 31))
        self.salida.setText(_fromUtf8(""))
        self.salida.setAlignment(QtCore.Qt.AlignCenter)
        self.salida.setObjectName(_fromUtf8("salida"))
        self.formLayoutWidget_4 = QtGui.QWidget(Dialog)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(60, 210, 141, 41))
        self.formLayoutWidget_4.setObjectName(_fromUtf8("formLayoutWidget_4"))
        self.formLayout_5 = QtGui.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_5.setMargin(0)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_8 = QtGui.QLabel(self.formLayoutWidget_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.total_fruta = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.total_fruta.setObjectName(_fromUtf8("total_fruta"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.total_fruta)
        self.formLayoutWidget_5 = QtGui.QWidget(Dialog)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(240, 210, 151, 41))
        self.formLayoutWidget_5.setObjectName(_fromUtf8("formLayoutWidget_5"))
        self.formLayout_6 = QtGui.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setMargin(0)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.total_verdura = QtGui.QLineEdit(self.formLayoutWidget_5)
        self.total_verdura.setObjectName(_fromUtf8("total_verdura"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.total_verdura)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget_5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_9)
        self.formLayoutWidget_6 = QtGui.QWidget(Dialog)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(420, 210, 161, 41))
        self.formLayoutWidget_6.setObjectName(_fromUtf8("formLayoutWidget_6"))
        self.formLayout_7 = QtGui.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_7.setMargin(0)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_6)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_10)
        self.total_legumbre = QtGui.QLineEdit(self.formLayoutWidget_6)
        self.total_legumbre.setObjectName(_fromUtf8("total_legumbre"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.FieldRole, self.total_legumbre)
        self.boton_pedido = QtGui.QPushButton(Dialog)
        self.boton_pedido.setGeometry(QtCore.QRect(610, 60, 141, 181))
        self.boton_pedido.setObjectName(_fromUtf8("boton_pedido"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.op_ma.setText(_translate("Dialog", "Manzanas", None))
        self.op_pe.setText(_translate("Dialog", "Peras", None))
        self.op_pl.setText(_translate("Dialog", "Plátanos", None))
        self.label_4.setText(_translate("Dialog", "Precio/unidad:", None))
        self.op_ac.setText(_translate("Dialog", "Acelga", None))
        self.op_bo.setText(_translate("Dialog", "Borraja", None))
        self.op_ca.setText(_translate("Dialog", "Cardo", None))
        self.label_5.setText(_translate("Dialog", "Precio/Kg:", None))
        self.op_al.setText(_translate("Dialog", "Alubias", None))
        self.op_le.setText(_translate("Dialog", "Lentejas", None))
        self.op_ga.setText(_translate("Dialog", "Garbanzos", None))
        self.label_6.setText(_translate("Dialog", "Precio/500g:", None))
        self.label.setText(_translate("Dialog", "Fruta", None))
        self.label_2.setText(_translate("Dialog", "Verdura", None))
        self.label_3.setText(_translate("Dialog", "Legumbre", None))
        self.label_8.setText(_translate("Dialog", "Total fruta:", None))
        self.label_9.setText(_translate("Dialog", "Total verdura:", None))
        self.label_10.setText(_translate("Dialog", "Total legumbre:", None))
        self.boton_pedido.setText(_translate("Dialog", "Hacer pedido", None))

