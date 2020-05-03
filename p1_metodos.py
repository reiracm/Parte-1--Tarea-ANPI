from sympy import *
from numpy import *
import numpy as np
'''
    Parametros:
        | ------
        | a:
        |    Valor a a evaluar
        | b:
        |    Valor b a evaluar
        | func:
        |   Función a evaluar
    Salidas:
        | --------
        |   bool :
        |       Booleano que indica si cumple el teorema de Bolzano
    '''
def isBolsano(a, b, func):
    x = a
    fa = eval(func)
    print(fa)
    x = b
    fb = eval(func)
    print(fb)
    return (fa * fb <= 0)

'''
    Parametros:
        | ------
        | f:
        |    Función de una variable a evaluar
        | a:
        |    Valor a del intervalo
        | b:
        |    Valor b del intervalo
        | tol:
        |   Tolerancia
    Salidas:
        | --------
        |   i :
        |       Número de iteraciones realizadas para llegar a la solución
        |   x :
        |       Valor al que converge la función
    '''
def biseccion(f, a, b, tol):
    i = 0
    x = 0
    
    #Si cumple con el Teorema de Bolzano, calcula el error y procede con la división de intervalos
    
    if (isBolsano(a, b, f)):
        tempA = a
        tempB = b
        e = (b - a) / 2
        
        #Mientras el error sea mayor a la tolerancia, la iteración continúa.
        
        while (e >= tol):
            x = (tempA + tempB) / 2
            if(isBolsano(x, tempB, f)):
              tempA = x
            elif(isBolsano(tempA, x, f)):
              tempB = x
            i = i + 1
            e = (b - a) / (2**i)
            
    #Finaliza el ciclo y retorna el resultado        
            
    return i, x

#biseccion("((log10(7/x)/(1/10)*ln(10))+(x*(6-x)/(((2*10**2*arccos(x/2*10)-x*sqrt(10**2-(x**2/4)))**2/2*(10*4/ln(10)))**2)*((1/(2*10**2*arccos(x/2*10)-x*sqrt(10**2-(x**2/4))))+(1/pi*10**2))))", 1, 2, 0.01)

'''
    Parametros:
        | ------
        | f:
        |    Función de una variable a evaluar
        | x0:
        |    Valor x0 inicial
        | x1:
        |    Valor x1 inicial
        | tol:
        |   Tolerancia
    Salidas:
        | --------
        |   i :
        |       Número de iteraciones realizadas para llegar a la solución
        |   xAprox :
        |       Valor al que converge la función
    '''
def secante(f, x0, x1, tol):
    xCurr = x1
    xPrev = x0
    i = 1
    tempTol = 1
    
    #Se evalúa la función con los valores de X anterior y actual hasta que cumpla con el margen de error deseado
    
    while ( tempTol >= tol):
        i = i + 1
        x = xCurr
        fxCurr = eval(f)
        x = xPrev
        fxPrev = eval(f)
        xAprox = xCurr - ((xCurr - xPrev) / (fxCurr - fxPrev)) * fxCurr
        xPrev = xCurr
        tempTol = (abs(xAprox - xCurr) / xAprox)
        xCurr = xAprox
    return xAprox, i

#secante("log10(7/x)/(1/10)*ln(10)+x*(6-x)/((2*10**2*arccos(x/(2*10))-x*sqrt(10**2-(x**2/4)))**2/(2*(10*4/ln(10)))**2*(1/(2*10**2*arccos(x/(2*10))-x*sqrt(10**2-(x**2/4)))+(1/pi*10**2)))", 0, 1, 0.001)


'''
    Parametros:
        | ------
        | f:
        |    Función de una variable a evaluar
        | x0:
        |    Valor x0 inicial
        | x1:
        |    Valor x1 inicial
        | tol:
        |   Tolerancia
    Salidas:
        | --------
        |   i :
        |       Número de iteraciones realizadas para llegar a la solución
        |   xAprox :
        |       Valor al que converge la función
    '''
def falsaPosicion(f, x0, x1, tol):
    
    #Posición anterior y actual de la aproximación
    
    xCurr = x1
    xPrev = x0
    i = 1
    tempTol = 1
    
     #Si cumple con el Teorema de Bolzano, calcula el error y procede con la división de intervalos
    
    if(isBolsano(x0,x1,f)):
        
        #Se evalúa la función con los valores de X anterior y actual hasta que cumpla con el margen de error deseado
        
        while(tempTol >= tol):
            i = i + 1
            x = xCurr
            fxCurr = eval(f)
            x = xPrev
            fxPrev = eval(f)
            
            #Calculo de la siguiente aproximación
            
            xAprox = xCurr - ((xCurr - xPrev) / (fxCurr - fxPrev)) * fxCurr
            tempTol = (abs(xAprox - xCurr) / xAprox)
            
            #Calculo de los nuevos valores del intervalo
            
            if(isBolsano(xPrev, xAprox, f)):
                xCurr = xAprox
            elif(isBolsano(xAprox, xCurr, f)):
                xPrev = xAprox
    return xAprox, i
