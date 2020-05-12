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
    
    f = lambda x: eval(func, {'x': x, 'pi': np.pi, 'e': np.e,
                              'exp': exp, 'sqrt': sqrt,
                              'arccos': acos, 'sin': sin, 'tan': tan, 
                              'ln': np.log,
                              'log10': np.log10})  
    
    fa = f(a)
    fb = f(b)
    
    print("------------")
    print(fa)
    print()
    print(fb)
    print("------------")

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
   #Inicializacion de la variable i que cuenta las iteraciones y x que es la aproximacion 
    
    i = 0
    x = 0
    
    if (isBolsano(a, b, f)):
        
        #Si cumple con el teorema el metodo continúa ejecutandose
        
        tempA = a
        tempB = b
        e = (b - a) / 2
        while (e >= tol):
            
            #Mientras no haya alcanzado el margen de error sigue dividiendo los intervalos que cumplan  con el teorema
            
            x = (tempA + tempB) / 2
            if(isBolsano(x, tempB, f)):
                tempA = x
            elif(isBolsano(tempA, x, f)):
                tempB = x
            i = i + 1
            e = (b - a) / (2**i)
    return i, x

#biseccion("((log10(7/x)/((1/10)*ln(10)))+(x*(6-x)/(((2*10**2*arccos(x/20)-x*sqrt(10**2-(x**2/4)))**2/(2*(40/ln(10))**2))*((1/(20**2*arccos(x/20)-x*sqrt(10**2-(x**2/4))))+(1/pi*10**2)))))", 0.1, 19, 10**(-10))
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
def secante(func, x0, x1, tol):

    f = lambda x: eval(func, {'x': x, 'pi': np.pi, 'e': np.e,
                              'exp': exp, 'sqrt': sqrt,
                              'arccos': acos, 'sin': sin, 'tan': tan, 
                              'ln': np.log,
                              'log10': np.log10})
    
    # store initial values
    i = 1
    fx0 = f(x0)
    print(fx0)
    fx1 = f(x1)
    print(fx1)
    tempTol = 1
    
    while tempTol >= tol:
        
        # Calcular aproximacion
        
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)

        print(x2)
        
        # Renombrar variables

        tempTol = (abs(x2 - x1) / x2)
        
        x0,  x1  = x1,  x2
        
        #Incrementar iteracion

        i += 1
        
    return x2,i

#secante("((log10(7/x)/((1/10)*ln(10)))+(x*(6-x)/(((2*10**2*arccos(x/20)-x*sqrt(10**2-(x**2/4)))**2/(2*(40/ln(10))**2))*((1/(20**2*arccos(x/20)-x*sqrt(10**2-(x**2/4))))+(1/pi*10**2)))))", 0.1, 19, 10**(-10))

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
