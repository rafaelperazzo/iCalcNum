# -*- coding: utf-8 -*-
#TODO Organizar este arquivo!!
from __future__ import division
import math 
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def f2(funcao,x):
    return float(eval(funcao))


def f(funcao,x):
    return N(eval(funcao))

def sinalF(funcao,x):
    if (eval(funcao))<0.0:
        return '-'
    else:
        return '+'

def bissecao(funcao,a,b,erro,precisao):
    c = np.around((a+b)/2.0,decimals=precisao)
    temp = 0.0
    contador = 1
    saida = 'i\t a\t b\t c\t sf(a)[f(a)]\t\t sf(b)[f(b)]\t\t sf(c)[f(c)]\t Erro\n'    
    saida = saida + '%d\t & %.4f\t & %.4f\t & %.4f\t & (%s)[%.4f]\t & (%s)[%.4f]\t & (%s)[%.4f]\t & ---\n' % (contador,a,b,c,sinalF(funcao,a),f(funcao,a),sinalF(funcao,b),f(funcao,b),sinalF(funcao,c),f(funcao,c))    
    while (True):
        contador+=1
        if (f(funcao,a)*f(funcao,c)<0):
            b=c
        elif (f(funcao,b)*f(funcao,c)<0):
            a = c
        temp = c
        c = np.around((a+b)/2.0,decimals=precisao)
        saida = saida + '%d\t & %.4f\t & %.4f\t & %.4f\t & (%s)[%.4f]\t & (%s)[%.4f]\t & (%s)[%.4f]\t & %.4f \n' % (contador,a,b,c,sinalF(funcao,a),f(funcao,a),sinalF(funcao,b),f(funcao,b),sinalF(funcao,c),f(funcao,c),abs(temp-c))
        if abs(temp-c)<erro:
            break
    return (c,saida)
    
def regulaFalsi(funcao,a,b,erro,precisao):
    c = ((a*math.fabs(f(funcao,b)))+(b*math.fabs(f(funcao,a))))/(math.fabs(f(funcao,b))+math.fabs(f(funcao,a)))
    temp = 0.0
    contador = 1
    saida = 'i\t a\t b\t c\t sf(a)[f(a)]\t\t sf(b)[f(b)]\t\t sf(c)[f(c)]\t\t Erro\n'    
    saida = saida + '\hline %d\t & %.4f\t & %.4f\t & %.4f\t & (%s)[%.4f]\t & (%s)[%.4f]\t & (%s)[%.4f]\t & --- \\ \n' % (contador,a,b,c,sinalF(funcao,a),f(funcao,a),sinalF(funcao,b),f(funcao,b),sinalF(funcao,c),f(funcao,c))
    while (True):
        contador+=1
        if (f(funcao,a)*f(funcao,c)<0):
            b=c
        elif (f(funcao,b)*f(funcao,c)<0):
            a = c
        temp = c
        c = ((a*f(funcao,b))-(b*f(funcao,a)))/(f(funcao,b)-f(funcao,a))
        saida = saida + '\hline %d\t & %.4f\t & %.4f\t & %.4f\t & (%s)[%.4f]\t & (%s)[%.4f]\t & (%s)[%.4f]\t & %.4f \\ \n' % (contador,a,b,c,sinalF(funcao,a),f(funcao,a),sinalF(funcao,b),f(funcao,b),sinalF(funcao,c),f(funcao,c),abs(temp-c))        
        if abs(temp-c)<erro:
            break
    return (c,saida)

def newton(funcao,x0,erro,precisao):   
    derivada = str(diff(funcao)) #Calculando a derivada
    contador = 1 #Contador de iteracoes
    saida = 'i\t x0\t\t f(x0)\t\t d(x0)\t\t x1\t\t Erro\n'    
    #print('i\t x0\t f(x0)\t d(x0)\t x1\t Erro\n') #Cabeçalho dos resultados
    x1 = x0-(f(funcao,x0)/f(derivada,x0))
    x1 = round(x1,precisao)    
    #print ('%d\t %.4f\t %.4f\t %.4f\t %.4f\t %.4f\n' % (contador,x0,f(funcao,x0),f(derivada,x0),x1,np.absolute(x0-x1)))    
    saida = saida + '\hline %d\t & %f\t & %f\t & %f\t & %f\t & %f \\ \n' % (contador,x0,f(funcao,x0),f(derivada,x0),x1,np.absolute(x0-x1))
    #print ('\hline %d\t & %f\t & %f\t & %f\t & %f\t & %f \\ \n' % (contador,x0,f(funcao,x0),f(derivada,x0),x1,np.absolute(x0-x1)))
    while(np.absolute(x0-x1)>erro):
        contador+=1
        x0 = x1
        x1 = x0-(f(funcao,x0)/f(derivada,x0))
        x1 = round(x1,precisao)
        saida = saida + '\hline %d\t & %f\t & %f\t & %f\t & %f\t & %f \\ \n' % (contador,x0,f(funcao,x0),f(derivada,x0),x1,np.absolute(x0-x1))
        #print ('\hline %d\t & %f\t & %f\t & %f\t & %f\t & %f \\ \n' % (contador,x0,f(funcao,x0),f(derivada,x0),x1,np.absolute(x0-x1)))
        if(contador>1000):
            break
    return(x1,saida)
    
    
def secante(funcao,x0,x1,erro,precisao):   
    contador = 1 #Contador de iteracoes
    #print('i\t x0\t f(x0)\t x1\t f(x1)\t x2\t Erro\n') #Cabeçalho dos resultados
    saida = 'i\t x0\t f(x0)\t x1\t f(x1)\t x2\t Erro\n'    
    x2 = x1-((f(funcao,x1)*(x0-x1))/(f(funcao,x0)-f(funcao,x1)))
    x2 = round(x2,precisao)    
    #print ('%d\t %.4f\t %.4f\t %.4f\t %.4f\t %.4f\n' % (contador,x0,f(funcao,x0),f(derivada,x0),x1,np.absolute(x0-x1)))    
    #print ('\hline %d\t & %.4f\t & %.4f\t & %.4f\t & %.4f\t & %.4f  & %.4f \\ \n' % (contador,x0,f(funcao,x0),x1,f(funcao,x1),x2,np.absolute(x2-x1)))
    saida = saida + '\hline %d\t & %.4f\t & %.4f\t & %.4f\t & %.4f\t & %.4f  & %.4f \\ \n' % (contador,x0,f(funcao,x0),x1,f(funcao,x1),x2,np.absolute(x2-x1))    
    while(np.absolute(x2-x1)>erro):
        contador+=1
        x0 = x1
        x1 = x2
        x2 = x1-((f(funcao,x1)*(x0-x1))/(f(funcao,x0)-f(funcao,x1)))
        x2 = round(x2,precisao)         
        #print ('%d\t %.4f\t %.4f\t %.4f\t %.4f\t %.4f\n' % (contador,x0,f(funcao,x0),f(derivada,x0),x1,np.absolute(x0-x1)))
        #print ('\hline %d\t & %.4f\t & %.4f\t & %.4f\t & %.4f\t & %.4f  & %.4f \\ \n' % (contador,x0,f(funcao,x0),x1,f(funcao,x1),x2,np.absolute(x2-x1)))
        saida = saida + '\hline %d\t & %.4f\t & %.4f\t & %.4f\t & %.4f\t & %.4f  & %.4f \\ \n' % (contador,x0,f(funcao,x0),x1,f(funcao,x1),x2,np.absolute(x2-x1))
        if(contador>1000):
            break
    return(x2,saida)

#Testa se a raiz é única no intervalo a,b
def raizUnica(fx,a,b,qPontos):
    x = symbols('x')    
    fx = parse_expr(fx)    
    dx = diff(fx) #Primeira derivada
    dx2 = diff(dx) #Segunda derivada
    #Valores de x para serem testados
    pontos = np.linspace(a,b,qPontos)
    d = lambdify(x,dx,"numpy")
    d2 = lambdify(x,dx2,"numpy")
    if (np.shape(np.where(d(pontos)<0))[1]==qPontos or np.shape(np.where(d(pontos)>0))[1]==qPontos) and (fx.evalf(subs={x: a})*fx.evalf(subs={x: b})<0):
        return True
    else:
        return False

#Verifica se x0 tem convergencia garantida pelo método de newton
def converge(fx,x0):
    x = symbols('x')    
    fx = parse_expr(fx)    
    dx = diff(fx) #Primeira derivada
    dx2 = diff(dx) #Segunda derivada
    
    #Se f(x_0)*f''(x_0)>0, o ponto x_0 é uma boa estimativa inicial    
    if fx.evalf(subs={x: x0})*dx2.evalf(subs={x: x0})>0:
        return True
    else:
        return False
