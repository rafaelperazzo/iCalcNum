# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun May 22 19:04:29 2016
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

class Ui_janelaPrincipal(object):
    def setupUi(self, janelaPrincipal):
        janelaPrincipal.setObjectName(_fromUtf8("janelaPrincipal"))
        janelaPrincipal.resize(943, 577)
        self.centralwidget = QtGui.QWidget(janelaPrincipal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.cmbMetodo = QtGui.QComboBox(self.centralwidget)
        self.cmbMetodo.setGeometry(QtCore.QRect(10, 50, 191, 29))
        self.cmbMetodo.setObjectName(_fromUtf8("cmbMetodo"))
        self.cmbMetodo.addItem(_fromUtf8(""))
        self.cmbMetodo.addItem(_fromUtf8(""))
        self.cmbMetodo.addItem(_fromUtf8(""))
        self.cmbMetodo.addItem(_fromUtf8(""))
        self.txtFuncao = QtGui.QLineEdit(self.centralwidget)
        self.txtFuncao.setGeometry(QtCore.QRect(120, 20, 271, 25))
        self.txtFuncao.setObjectName(_fromUtf8("txtFuncao"))
        self.txtA = QtGui.QLineEdit(self.centralwidget)
        self.txtA.setGeometry(QtCore.QRect(10, 110, 113, 25))
        self.txtA.setObjectName(_fromUtf8("txtA"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 141, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtB = QtGui.QLineEdit(self.centralwidget)
        self.txtB.setGeometry(QtCore.QRect(10, 140, 113, 25))
        self.txtB.setObjectName(_fromUtf8("txtB"))
        self.btnCalcular = QtGui.QPushButton(self.centralwidget)
        self.btnCalcular.setGeometry(QtCore.QRect(150, 110, 91, 51))
        self.btnCalcular.setObjectName(_fromUtf8("btnCalcular"))
        self.txtResultado = QtGui.QTextEdit(self.centralwidget)
        self.txtResultado.setGeometry(QtCore.QRect(0, 170, 941, 351))
        self.txtResultado.setObjectName(_fromUtf8("txtResultado"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 50, 41, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cmbErro = QtGui.QComboBox(self.centralwidget)
        self.cmbErro.setGeometry(QtCore.QRect(240, 50, 151, 29))
        self.cmbErro.setObjectName(_fromUtf8("cmbErro"))
        self.cmbErro.addItem(_fromUtf8(""))
        self.cmbErro.addItem(_fromUtf8(""))
        self.cmbErro.addItem(_fromUtf8(""))
        self.cmbErro.addItem(_fromUtf8(""))
        self.cmbErro.addItem(_fromUtf8(""))
        janelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(janelaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 943, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        janelaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(janelaPrincipal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        janelaPrincipal.setStatusBar(self.statusbar)
        self.actionSair = QtGui.QAction(janelaPrincipal)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.menuArquivo.addAction(self.actionSair)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(janelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(janelaPrincipal)

    def retranslateUi(self, janelaPrincipal):
        janelaPrincipal.setWindowTitle(_translate("janelaPrincipal", "Zero de Funções", None))
        self.label.setText(_translate("janelaPrincipal", "Digite a função", None))
        self.cmbMetodo.setItemText(0, _translate("janelaPrincipal", "Método da bisseção", None))
        self.cmbMetodo.setItemText(1, _translate("janelaPrincipal", "Falsa Posição", None))
        self.cmbMetodo.setItemText(2, _translate("janelaPrincipal", "Newton-raphson", None))
        self.cmbMetodo.setItemText(3, _translate("janelaPrincipal", "Secante", None))
        self.label_2.setText(_translate("janelaPrincipal", "Estimativa inicial", None))
        self.btnCalcular.setText(_translate("janelaPrincipal", "Calcular", None))
        self.label_3.setText(_translate("janelaPrincipal", "Erro", None))
        self.cmbErro.setItemText(0, _translate("janelaPrincipal", "0.01", None))
        self.cmbErro.setItemText(1, _translate("janelaPrincipal", "0.1", None))
        self.cmbErro.setItemText(2, _translate("janelaPrincipal", "0.001", None))
        self.cmbErro.setItemText(3, _translate("janelaPrincipal", "0.0001", None))
        self.cmbErro.setItemText(4, _translate("janelaPrincipal", "0.00001", None))
        self.menuArquivo.setTitle(_translate("janelaPrincipal", "Arquivo", None))
        self.actionSair.setText(_translate("janelaPrincipal", "Sair", None))

