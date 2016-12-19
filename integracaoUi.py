# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'integracao.ui'
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

class Ui_janelaPrincipal(object):
    def setupUi(self, janelaPrincipal):
        janelaPrincipal.setObjectName(_fromUtf8("janelaPrincipal"))
        janelaPrincipal.resize(438, 483)
        self.centralwidget = QtGui.QWidget(janelaPrincipal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtFuncao = QtGui.QLineEdit(self.centralwidget)
        self.txtFuncao.setGeometry(QtCore.QRect(120, 20, 291, 31))
        self.txtFuncao.setObjectName(_fromUtf8("txtFuncao"))
        self.cmbMetodo = QtGui.QComboBox(self.centralwidget)
        self.cmbMetodo.setGeometry(QtCore.QRect(10, 60, 181, 22))
        self.cmbMetodo.setObjectName(_fromUtf8("cmbMetodo"))
        self.cmbMetodo.addItem(_fromUtf8(""))
        self.cmbMetodo.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 60, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtA = QtGui.QLineEdit(self.centralwidget)
        self.txtA.setGeometry(QtCore.QRect(310, 60, 101, 21))
        self.txtA.setObjectName(_fromUtf8("txtA"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 90, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtB = QtGui.QLineEdit(self.centralwidget)
        self.txtB.setGeometry(QtCore.QRect(310, 90, 101, 21))
        self.txtB.setObjectName(_fromUtf8("txtB"))
        self.txtResultado = QtGui.QTextEdit(self.centralwidget)
        self.txtResultado.setGeometry(QtCore.QRect(10, 160, 411, 271))
        self.txtResultado.setObjectName(_fromUtf8("txtResultado"))
        self.btnCalcular = QtGui.QPushButton(self.centralwidget)
        self.btnCalcular.setGeometry(QtCore.QRect(140, 120, 151, 31))
        self.btnCalcular.setObjectName(_fromUtf8("btnCalcular"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 101, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtM = QtGui.QLineEdit(self.centralwidget)
        self.txtM.setGeometry(QtCore.QRect(110, 90, 81, 21))
        self.txtM.setObjectName(_fromUtf8("txtM"))
        janelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(janelaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        janelaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(janelaPrincipal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        janelaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(janelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(janelaPrincipal)
        janelaPrincipal.setTabOrder(self.txtFuncao, self.cmbMetodo)
        janelaPrincipal.setTabOrder(self.cmbMetodo, self.txtA)
        janelaPrincipal.setTabOrder(self.txtA, self.txtB)
        janelaPrincipal.setTabOrder(self.txtB, self.txtM)
        janelaPrincipal.setTabOrder(self.txtM, self.btnCalcular)
        janelaPrincipal.setTabOrder(self.btnCalcular, self.txtResultado)

    def retranslateUi(self, janelaPrincipal):
        janelaPrincipal.setWindowTitle(_translate("janelaPrincipal", "Integração Numérica", None))
        self.label.setText(_translate("janelaPrincipal", "Digite a função", None))
        self.cmbMetodo.setItemText(0, _translate("janelaPrincipal", "Método dos Trapézios", None))
        self.cmbMetodo.setItemText(1, _translate("janelaPrincipal", "Método de Simpson", None))
        self.label_2.setText(_translate("janelaPrincipal", "Limite inferior: ", None))
        self.label_3.setText(_translate("janelaPrincipal", "Limite Superior", None))
        self.btnCalcular.setText(_translate("janelaPrincipal", "Calcular", None))
        self.label_4.setText(_translate("janelaPrincipal", "Subintervalos: ", None))

