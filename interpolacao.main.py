# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
import sys
import interpolacao as z
from interpolacaoUi import *
import numpy as np
import pylab as plt
from sympy import *

reload(sys)  
sys.setdefaultencoding('utf8')

def str2list(texto):
    resultado = map(float,texto.split())
    if type(resultado) is list:
        return True
    else:
        return False

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
    if ui.txtX.text()!='':
        input1 = True
    if ui.txtY.text()!='':
        input2 = True
    if ui.txtPrecisao.text()!='':
        input3 = True
    if ui.txtPonto.text()!='':
        input4 = True
    if ui.txtQuantidade.text()!='':
        input5 = True

    try:
        if not str2list(str(ui.txtX.text())):
            input1 = False
        if not str2list(str(ui.txtY.text())):
            input2 = False    
        numerico = float(ui.txtPrecisao.text())
        numerico = float(ui.txtPonto.text())
        numerico = float(ui.txtQuantidade.text())
    except ValueError as e:
        input1 = False
    
    if input1 and input2 and input3 and input4 and input5:
        return True
    else:
        return False

def cmbMetodoChanged():
    metodo = ui.cmbMetodo.currentIndex()
    if metodo==0:
        ui.txtPonto.setDisabled(True)
    elif metodo==1:
        ui.txtPonto.setDisabled(False)
    elif metodo==2:
        ui.txtPonto.setDisabled(False)
    elif metodo==3:
        ui.txtPonto.setDisabled(False)

#FUNCAO DO CLICK DO BOTAO
def btnCalcularClick():
    if entradaValida():
        ui.txtResultado.clear()        
        eixoX = str(ui.txtX.text())
        eixoX = map(float,eixoX.split())
        eixoY = str(ui.txtY.text())
        eixoY = map(float,eixoY.split())
        precisao = int(ui.txtPrecisao.text())
        if ui.cmbMetodo.currentIndex()==0: #MINIMOS QUADRADOS   
            resultado = z.minimosQuadrados(eixoX,eixoY,precisao)
            ui.txtResultado.append('***************')        
            ui.txtResultado.append('a0')
            ui.txtResultado.append('***************')        
            ui.txtResultado.append(str(resultado[0]))
            ui.txtResultado.append('***************************')        
            ui.txtResultado.append(u'a1')
            ui.txtResultado.append('***************************')
            ui.txtResultado.append(str(resultado[1]))
            ui.txtResultado.append('***************')        
            ui.txtResultado.append(u'Função')
            ui.txtResultado.append('***************')
            ui.txtResultado.append('f(x)= ' + str(resultado[2]))
        elif ui.cmbMetodo.currentIndex()==1: #splines lineares
            ponto = float(ui.txtPonto.text())
            resultado = z.splinesLineares(eixoX,eixoY,precisao,ponto)
            ui.txtResultado.append('***************')        
            ui.txtResultado.append('Splines')
            ui.txtResultado.append('***************')        
            ui.txtResultado.append(str(resultado[0]))
            ui.txtResultado.append('***************************')        
            ui.txtResultado.append(u'Índice')
            ui.txtResultado.append('***************************')
            ui.txtResultado.append('Utilizando o spline: ' + str(resultado[1]+1))
            ui.txtResultado.append('***************')        
            ui.txtResultado.append(u'Interpolação no ponto')
            ui.txtResultado.append('***************')
            ui.txtResultado.append('f(' + str(ponto) +')= ' + str(resultado[2]))
        elif ui.cmbMetodo.currentIndex()==2: #LAGRANGE
            ponto = float(ui.txtPonto.text())
            resultado = z.lagrange(eixoX,eixoY,precisao,ponto)
            ui.txtResultado.append('***************')        
            ui.txtResultado.append('Valor interpolado no ponto')
            ui.txtResultado.append('***************')        
            ui.txtResultado.append(str(resultado[0]))
            ui.txtResultado.append('***************************')        
            ui.txtResultado.append(u'Polinômio não simplificado')
            ui.txtResultado.append('***************************')
            #expressao = sympify(resultado[1])
            #expressao = pretty(expressao,use_unicode=True)
            #ui.txtResultado.append(expressao)
            ui.txtResultado.append('f(x)= ' + str(resultado[1]))
            ui.txtResultado.append('***************')        
            ui.txtResultado.append('SIMPLIFICANDO')
            ui.txtResultado.append('***************')
            ui.txtResultado.append(pretty(resultado[2],use_unicode=True))
            
        else: #DIFERENÇAS DIVIDIDAS
            ponto = float(ui.txtPonto.text())
            resultado = z.newton(eixoX,eixoY,precisao,ponto)
            ui.txtResultado.append('***************')        
            ui.txtResultado.append(u'Diferenças divididas')
            ui.txtResultado.append('***************')        
            ui.txtResultado.append(str(resultado[3]))
            ui.txtResultado.append('***************')        
            ui.txtResultado.append('Valor interpolado no ponto')
            ui.txtResultado.append('***************')        
            ui.txtResultado.append(str(resultado[0]))
            ui.txtResultado.append('***************************')        
            ui.txtResultado.append(u'Polinômio não simplificado')
            ui.txtResultado.append('***************************')
            #expressao = sympify(resultado[1])
            #expressao = pretty(expressao,use_unicode=True)
            #ui.txtResultado.append(expressao)
            ui.txtResultado.append('f(x)= ' + str(resultado[1]))
            ui.txtResultado.append('***************')        
            ui.txtResultado.append('SIMPLIFICANDO')
            ui.txtResultado.append('***************')
            ui.txtResultado.append(pretty(resultado[2],use_unicode=True))
            #print(resultado[3])
            #print(resultado[1])
    else:
        #QMessageBox.critical(None,'Erro!',u'Entrada Inválida!',QMessageBox.Ok)
        mensagem(2,u'Erro!',u'Entrada inválida!',u'Os dados de entrada devem ser numéricos!')
        
def btnVerGraficoClick():
    btnCalcularClick()    
    eixoX = str(ui.txtX.text())
    eixoX = map(float,eixoX.split())
    eixoY = str(ui.txtY.text())
    eixoY = map(float,eixoY.split())
    precisao = int(ui.txtPrecisao.text())
    
    if ui.cmbMetodo.currentIndex()==0:
        funcao = z.minimosQuadrados(eixoX,eixoY,precisao)[2]
    elif ui.cmbMetodo.currentIndex()==2:
        funcao = z.lagrange(eixoX,eixoY,precisao,1)[2]
    elif ui.cmbMetodo.currentIndex()==3:
        funcao = z.newton(eixoX,eixoY,precisao,1)[2]
    else: 
        ponto = float(ui.txtPonto.text())        
        resultado = z.splinesLineares(eixoX,eixoY,precisao,ponto)     
        indice = resultado[1]
        funcao = resultado[0][indice]        
        #QMessageBox.information(None,u'Informação',u'Função ainda não disponível.',QMessageBox.Ok)
    
    if ui.cmbMetodo.currentIndex()==1:
        figure = plt.figure(1)
        ax1 = figure.add_subplot(111)
        ax1.axhline(linewidth=4,color="black")
        ax1.axvline(linewidth=4,color="black")
        plt.grid(True)
        fx, = plt.plot(eixoX,eixoY, 'r',label='f(x)',color='k',linewidth=2.0)
        #dx, = plt.plot(x,y2,'r', label='f\'(x)',color='k',linewidth=1.0)
        plt.show()
    else:    
        funcao = str(funcao)
        x=np.linspace(min(eixoX),max(eixoX),100)
        y2 = eval(funcao)
        figure = plt.figure(1)
        ax1 = figure.add_subplot(111)
        ax1.axhline(linewidth=4,color="black")
        ax1.axvline(linewidth=4,color="black")
        plt.grid(True)
        #plt.xlim(min(eixoX),max(eixoX))
        #plt.ylim(min(eixoY),max(eixoY))
        fx, = plt.plot(eixoX,eixoY, 'ro',label='f(x)',color='k',linewidth=2.0)
        dx, = plt.plot(x,y2,'r', label='f\'(x)',color='k',linewidth=1.0)
        plt.show()
    #janela = Window(window,eixoX,eixoY,str(funcao))
    #janela.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
    #janela.exec_()
    
def sair():
    quit()

def btnAleatorioClick():
    tamanho = int(ui.txtQuantidade.text())+1
    listaX = []
    listaY=[]
    for i in range(1,tamanho,1):
        x = np.random.randint(0,30)
        y = np.random.randint(0,50)
        while x in listaX:
            x = np.random.randint(0,30)
        while y in listaY:
            y = np.random.randint(0,30)
        listaX.append(x)
        listaY.append(y)
    
    lX = str(listaX)
    lY = str(listaY)
    lX = lX.replace('[','')
    lX = lX.replace(',',' ')
    lX = lX.replace(']','')
    lY = lY.replace('[','')
    lY = lY.replace(',',' ')
    lY = lY.replace(']','')
    ui.txtX.setText(lX)
    ui.txtY.setText(lY)

def salvar():
    fileName = QFileDialog.getSaveFileName(None, "Salvar Como")
    if (fileName!=''):
        f = open(fileName,'w')
        resultado = str(ui.txtX.text()) + '\n' + str(ui.txtY.text()) + '\n'
        resultado = resultado + str(ui.txtResultado.toPlainText()) +  '\n'
        f.write(resultado)
        f.close()

#INICIANDO APLICACAO
app = QApplication(sys.argv)

#CRIANDO JANELA PRINCIPAL
window = QMainWindow()
ui = Ui_interpolacaoPrincipal()
ui.setupUi(window)
#LIGANDO CLICK DO BOTAO A FUNCAO ACIMA
ui.btnCalcular.clicked.connect(btnCalcularClick)
ui.btnGrafico.clicked.connect(btnVerGraficoClick)
ui.btnAleatorios.clicked.connect(btnAleatorioClick)
#ui.actionSair.triggered.connect(sair)
ui.cmbMetodo.currentIndexChanged.connect(cmbMetodoChanged)
ui.actionSalvarComo.triggered.connect(salvar)
window.show()

sys.exit(app.exec_())
