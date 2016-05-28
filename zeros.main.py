# -*- coding: utf-8 -*-
#http://zetcode.com/gui/pyqt4/firstprograms/
#http://rra.etc.br/MyWorks/2009/07/17/python-pyqt-03-usando-qmessagebox/
from PyQt4.QtGui import *
import sys
import zeros as z
from interface import *

def cmbMetodoChanged():
    metodo = ui.cmbMetodo.currentIndex()
    if metodo==0:
        ui.txtA.setDisabled(False)
        ui.txtB.setDisabled(False)
    elif metodo==1:
        ui.txtA.setDisabled(False)
        ui.txtB.setDisabled(False)
    elif metodo==2:
        ui.txtA.setDisabled(False)
        ui.txtB.setDisabled(True)
    elif metodo==3:
        ui.txtA.setDisabled(False)
        ui.txtB.setDisabled(False)

    
#FUNCAO DO CLICK DO BOTAO
def btnCalcularClick():
    w = QWidget()    
    funcao = str(ui.txtFuncao.text())
    erro = float(ui.cmbErro.currentText())
    precisao = 5
    a = float(ui.txtA.text())
    #b = float(ui.txtB.text())
    
    raiz = (' ',0)    
    if ui.cmbMetodo.currentIndex()==0:      
        b = float(ui.txtB.text())        
        raiz = list(z.bissecao(funcao,a,b,erro,precisao))
    elif ui.cmbMetodo.currentIndex()==1:
        b = float(ui.txtB.text())        
        raiz = list(z.regulaFalsi(funcao,a,b,erro,precisao))
    elif ui.cmbMetodo.currentIndex()==2:
        raiz = list(z.newton(funcao,a,erro,precisao))
    else:
        b = float(ui.txtB.text())           
        raiz = list(z.secante(funcao,a,b,erro,precisao))
    
    ui.txtResultado.setText(str(raiz[1]))
    ui.txtResultado.append('\n ' + 'Resultado: ' +str(raiz[0]))

    
def sair():
    quit()

#INICIANDO APLICACAO
app = QApplication(sys.argv)

#CRIANDO JANELA PRINCIPAL
window = QMainWindow()
ui = Ui_janelaPrincipal()
ui.setupUi(window)

#LIGANDO CLICK DO BOTAO A FUNCAO ACIMA
ui.btnCalcular.clicked.connect(btnCalcularClick)
ui.actionSair.triggered.connect(sair)
ui.cmbMetodo.currentIndexChanged.connect(cmbMetodoChanged)
window.show()

sys.exit(app.exec_())
