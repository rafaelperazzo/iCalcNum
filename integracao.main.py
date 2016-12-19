# -*- coding: utf-8 -*-
import sys
import integracao as z
from integracaoUi import *
import numpy as np
import pylab as plt
from sympy import *
from PyQt4.QtGui import *

reload(sys)  
sys.setdefaultencoding('utf8')

def mensagem(tipo,titulo,texto,detalhes):
    msg = QMessageBox()
    if tipo==0:
        msg.setIcon(QMessageBox.Information)
    elif tipo==1:
        msg.setIcon(QMessageBox.Warning)
    elif tipo==2:
        msg.setIcon(QMessageBox.Critical)
    
    msg.setText(texto)
    msg.setInformativeText(u'Informações adicionais')
    msg.setWindowTitle(titulo)
    msg.setDetailedText(detalhes)
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()

def entradaValida():
    input1 = False   
    input2 = False
    input3 = False
    input4 = False
    input5 = False
    if ui.txtFuncao.text()!='':
        input1 = True
    if ui.txtA.text()!='':
        input2 = True
    if ui.txtB.text()!='':
        input3 = True

    try:
        numerico = float(ui.txtA.text())
        numerico = float(ui.txtB.text())
        
    except ValueError as e:
        input2 = False
    
    if input1 and input2 and input3:
        return True
    else:
        return False


#FUNCAO DO CLICK DO BOTAO
def btnCalcularClick():
    if entradaValida():
        ui.txtResultado.clear()        
        funcao = str(ui.txtFuncao.text())
        inferior = float(ui.txtA.text())
        superior = float(ui.txtB.text())
        subintervalos = int(ui.txtM.text())
        if ui.cmbMetodo.currentIndex()==0: #TRAPÉZIOS 
            resultado = z.trapezios(funcao,inferior,superior,subintervalos,5)
            ui.txtResultado.append('TABELA') 
            ui.txtResultado.append('***************')             
            ui.txtResultado.append(str(resultado[2]))
            ui.txtResultado.append('***************************')        
            ui.txtResultado.append(u'Resultado: ')
            ui.txtResultado.append('***************************')
            ui.txtResultado.append(str(resultado[0]))
            ui.txtResultado.append('***************')        
            ui.txtResultado.append(u'Função')
            ui.txtResultado.append('***************')
            ui.txtResultado.append('f(x)= ' + funcao)
        elif ui.cmbMetodo.currentIndex()==1: #Simpson
            resultado = z.simpson(funcao,inferior,superior,subintervalos,5)
            ui.txtResultado.append('***************')             
            ui.txtResultado.append(str(resultado[2]))
            ui.txtResultado.append('***************************')        
            ui.txtResultado.append(u'Resultado: ')
            ui.txtResultado.append('***************************')
            ui.txtResultado.append(str(resultado[0]))
            ui.txtResultado.append('***************')        
            ui.txtResultado.append(u'Função')
            ui.txtResultado.append('***************')
            ui.txtResultado.append('f(x)= ' + funcao)
            #ui.txtResultado.append(pretty(funcao,use_unicode=True))
        
    else:
        #QMessageBox.critical(None,'Erro!',u'Entrada Inválida!',QMessageBox.Ok)
        mensagem(2,u'Erro!',u'Entrada inválida!',u'Os dados de entrada devem ser numéricos!')



#INICIANDO APLICACAO
app = QApplication(sys.argv)

#CRIANDO JANELA PRINCIPAL
window = QMainWindow()
ui = Ui_janelaPrincipal()
ui.setupUi(window)
#LIGANDO CLICK DO BOTAO A FUNCAO ACIMA
ui.btnCalcular.clicked.connect(btnCalcularClick)
#ui.btnGrafico.clicked.connect(btnVerGraficoClick)
#ui.btnAleatorios.clicked.connect(btnAleatorioClick)
#ui.actionSair.triggered.connect(sair)
#ui.cmbMetodo.currentIndexChanged.connect(cmbMetodoChanged)
#ui.actionSalvarComo.triggered.connect(salvar)
window.show()

sys.exit(app.exec_())