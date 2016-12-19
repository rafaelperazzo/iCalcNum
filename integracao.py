from __future__ import division
import math 
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def f(funcao,x):
    return float(eval(funcao))


def trapezios(funcao,a,b,m,precisao=4):
    x = []
    y = []
    h = (b-a)/m
    x.append(a)
    c = []
    c.append(1)
    for i in range(1,m+1,1):
        x.append(x[i-1]+h)
    
    for i in range(0,len(x),1):
        y.append(f(funcao,x[i]))
    
    for i in range(1,len(x)-1,1):
        c.append(2)
    c.append(1)
    
    soma = 0
    saida2 = 'i\t x_i\t y_i\t c_i\t \n'
    saida = '<table border="1">\n<tr><td>i</td><td>x</td><td>y</td><td>c</td></tr>\n'
    for i in range(0,len(x),1):
        soma = soma + c[i]*y[i]
        saida = saida + '<tr>\n'
        saida2 = saida2 + '%d\t %.4f\t %.4f\t %d\t \n' % (i,x[i],y[i],c[i])
        saida = saida + '<td>%d</td> <td>%.4f</td> <td>%.4f</td> <td>%d</td>\n' % (i,x[i],y[i],c[i])
        saida = saida + '</tr>\n'
    
    resultado = h/2*(soma)
    saida = saida + '</table>\n'
    return (round(resultado,precisao),saida,saida2)
    

def simpson(funcao,a,b,m,precisao=4):
    x = []
    y = []
    h = (b-a)/m
    x.append(a)
    c = []
    c.append(1)
    for i in range(1,m+1,1):
        x.append(x[i-1]+h)
    
    for i in range(0,len(x),1):
        y.append(f(funcao,x[i]))
    
    for i in range(1,len(x)-1,1):
        if i%2==1:
            c.append(4)
        else:
            c.append(2)
    
    c.append(1)
    
    soma = 0
    saida2 = 'i\t x_i\t y_i\t c_i\t \n'
    saida = '<table border=1>\n<tr><td>i</td><td>x</td><td>y</td><td>c</td></tr>\n'
    for i in range(0,len(x),1):
        soma = soma + c[i]*y[i]
        saida = saida + '<tr>\n'
        saida2 = saida2 + '%d\t %.4f\t %.4f\t %d\t \n' % (i,x[i],y[i],c[i])
        saida = saida + '<td>%d</td> <td>%.4f</td> <td>%.4f</td> <td>%d</td>\n' % (i,x[i],y[i],c[i])
        saida = saida + '</tr>\n'
    
    resultado = h/3*(soma)
    saida = saida + '</table>\n'
    return (round(resultado,precisao),saida,saida2)


#a=0
#b=1
#m=4
##funcao = '1/(1+x**2)'
#print simpson(funcao, a, b, m)[1]
#print simpson(funcao, a, b, m)[0]
