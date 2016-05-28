# -*- coding: utf-8 -*-

from sympy import *

def minimosQuadrados(x,y,precisao):
    Sx = 0
    Sy=0
    Sxy=0
    Sxx=0
    for i in range(0,len(x),1):
        Sx = Sx + x[i]
        Sy = Sy + y[i]
        Sxy = Sxy + x[i]*y[i]
        Sxx = Sxx + x[i]**2
    
    n = len(x)
    a1 = ((n*Sxy)-(Sx*Sy))/((n*Sxx)-(Sx*Sx))
    a0 = ((Sxx*Sy)-(Sxy*Sx))/((n*Sxx)-(Sx**2))
    a0 = round(a0,precisao)
    a1 = round(a1,precisao)    
    expr = str(a1) + '*x + (' + str(a0) + ')'
    return (a0,a1,expr)


def splinesLineares(x1,y,precisao,ponto):
    splines=[]
    x = symbols('x')
    for i in range(0,len(x1)-1,1):
        spline = '((x-'+str(x1[i+1])+')/(' + str(x1[i]) + '-' + str(x1[i+1]) + '))*' + str(y[i])
        spline = spline + '+ ((x-' + str(x1[i]) + ')/(' + str(x1[i+1]) + '-' + str(x1[i]) + '))*' + str(y[i+1])
        spline = simplify(spline)        
        splines.append(spline)
    
    indice=-1
    for i in range(0,len(x1)-1,1):
        if ponto>x1[i] and ponto<x1[i+1]:
            indice = i
    resultado = round(splines[indice].subs(x,ponto),precisao)
    return (splines,indice,resultado)

def lagrange(x1,y1,precisao,ponto):
    x = symbols('x')    
    soma = 0
    sProduto = ''
    sSoma = ''
    for i in range(0,len(x1),1):
        produto = 1
        sProduto=''
        for j in range(0,len(x1),1):
            if j!=i:
                produto = produto*((ponto-x1[j])/(float(x1[i]-x1[j])))
                if sProduto=='':                  
                    sProduto = sProduto + '(' + 'x' + '-' + str(x1[j]) + ')/(' + str(x1[i]) + '-' + str(x1[j]) + ') ' 
                else:
                    sProduto = sProduto + '*(' + 'x' + '-' + str(x1[j]) + ')/(' + str(x1[i]) + '-' + str(x1[j]) + ') ' 
        soma = soma + y1[i]*produto
        sProduto = '(' + sProduto + ')'        
        if sSoma=='':            
            sSoma = sSoma + str(y1[i]) + '*' + str(sProduto)
        else: 
            sSoma = sSoma + ' + ' + str(y1[i]) + '*' + str(sProduto)
    return (round(soma,precisao),sSoma,simplify(sSoma))


def diferencasDivididas(x1,y1):
    coeficientes = []
    lista = list(y1)
    proxima = []
    ordem = len(x1)-1
    k=1
    m=1
    diferencas = ''
    while ordem>=0:
        coeficientes.append(lista[0])
        k=m
        diferencas = diferencas + '\n ' + str(lista)
        for i in range(0,len(lista)-1,1):
            proxima.append((lista[i+1]-lista[i])/(x1[k]-x1[k-m]))
            k+=1
        m+=1
        ordem-=1
        lista = list(proxima)
        proxima = []
    
    return (coeficientes,diferencas)
                
def newton (x1,y1,precisao,ponto):
    x = symbols('x')    
    diferencas = diferencasDivididas(x1,y1)[0]
    #print(diferencasDivididas(x1,y1)[0])
    soma = 0
    resultado = ''
    for i in range(0,len(x1),1):
        produto = 1        
        for j in range(0,i,1):
            produto = produto * (ponto-x1[j])
            if j==0:
                resultado = resultado + '(' + 'x' + '-' + str(x1[j]) + ')'
            else:
                resultado = resultado + '*(' + 'x' + '-' + str(x1[j]) + ')'
        produto = produto * diferencas[i]
        if i==0:        
            resultado = resultado + '(' + str(diferencas[i])
        else:
            resultado = resultado + '*(' + str(diferencas[i])
        soma = soma + produto
        if i!=len(x1)-1:        
            resultado = resultado + ')+'
        else:
            resultado = resultado + ')'
    #resultado = simplify(resultado)
    return (soma,resultado,simplify(resultado))
    
'''init_printing(use_unicode=True)
x = [0,30,70,100]
y= [0.94,1.05,1.17,1.28]

print(minimosQuadrados(x,y,4))

x = [8,11,15,18]
y= [5,9,10,8]

print(splinesLineares(x,y,4,12.7))

cx = [1,2,4,5,7]
cy= [52,5,-5,-40,10]
cx = [1,2,4]
cy= [52,5,-5]
print(lagrange(cx,cy,4,3)[0])
print(lagrange(cx,cy,4,3)[1])
print(lagrange(cx,cy,4,3)[2])


cx = [1,2,4,5,7]
cy= [52,5,-5,-40,10]
print(splinesLineares(cx,cy,4,3))
#print(diferencasDivididas(cx,cy,4,3)[1])
'''