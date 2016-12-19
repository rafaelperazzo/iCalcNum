# -*- coding: utf-8 -*-
#http://zetcode.com/gui/pyqt4/firstprograms/
#http://rra.etc.br/MyWorks/2009/07/17/python-pyqt-03-usando-qmessagebox/
from PyQt4.QtGui import *
import sys
import zeros as z
from interface import *
import pylab as plt
import numpy as np
import math
from sympy import *


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


def calcularY(funcao,valoresX):
    y = []
    for i in range(0,len(valoresX),1):
        x = valoresX[i]
        valor = N(eval(funcao))
        y.append(valor)
    return y
    

def btnGraficoClick():
    x1 = float(ui.txtX1.text())
    x2 = float(ui.txtX2.text())
    funcao = str(ui.txtFuncao.text())
    x = np.linspace(x1,x2,50)
    #Escreva a função que será plotada.
    y = calcularY(funcao,x)
    fig = plt.figure(1)
    ax1 = fig.add_subplot(111)
    ax1.axhline(linewidth=4,color="black")
    ax1.axvline(linewidth=4,color="black")
    plt.grid(True)
    plt.xlim(x1,x2)
    #plt.ylim(-1.5,4)
    fx = plt.plot(x,y, '-',label='f(x)',color='k',linewidth=2.0)
    #plt.legend([fx], ['f(x) - funcao', ])
    #plot.ylim(-20,20)
    plt.show()
    
    
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
ui.btnGrafico.clicked.connect(btnGraficoClick)
ui.actionSair.triggered.connect(sair)
ui.cmbMetodo.currentIndexChanged.connect(cmbMetodoChanged)
window.show()

sys.exit(app.exec_())
