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
        itArray = []
        errArray = []
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
            itArray.append(i)
            errArray.append(e)


    plt.plot(itArray,errArray)
    plt.ylabel('Errores')
    plt.xlabel('Iteraciones')

    plt.show()
        
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
                              'ln': np.log, 'log10': np.log10})
    
    # store initial values
    i = 1
    fx0 = f(x0)
    print(fx0)
    fx1 = f(x1)
    print(fx1)
    tempTol = 1
    itArray = []
    errArray = []
    
    while tempTol >= tol:
        
        # Calcular aproximacion
        
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)

        print(x2)
        
        # Renombrar variables

        tempTol = (abs(x2 - x1) / x2)
        
        x0,  x1  = x1,  x2
        
        #Incrementar iteracion

        i += 1

        itArray.append(i)
        errArray.append(tempTol)



    plt.plot(itArray,errArray)
    plt.ylabel('Errores')
    plt.xlabel('Iteraciones')

    plt.show()
    
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
def falsaPosicion(func, x0, x1, tol):

    f = lambda x: eval(func, {'x': x, 'pi': np.pi, 'e': np.e,
                              'exp': exp, 'sqrt': sqrt,
                              'arccos': acos, 'sin': sin, 'tan': tan, 
                              'ln': np.log, 'log10': np.log10})

    #Revisar el Teorema de Bolsano
    print(f(x0))
    print(f(x1))

    fx0 = f(x0)
    fx1 = f(x1)

    itArray = []
    errArray = []
    
    
    if(fx0*fx1 <= 0):

        i = 1
        xnC = x1
        xnP = 0
        fx2 = f(xnC)
        tempTol = 1

        while( tempTol >= tol):

            #Calculo de la aproximacion
            xnC = x1 - fx1*((x1 - x0) / (fx1 - fx0))
            print(xnC)
            xnP = x1
            tempTol = abs(xnC-x1/xnC)

            if(xnC == xnP):
                
                plt.plot(itArray,errArray)
                plt.ylabel('Errores')
                plt.xlabel('Iteraciones')
                plt.show()

                return [xnC, i]
                
            
            #Escoger el nuevo subintervalo
            if(fx0*fx2):
                x1 = xnC
            else:
                x0 = xnC

            i += 1
            itArray.append(i)
            errArray.append(tempTol)

    plt.plot(itArray,errArray)
    plt.ylabel('Errores')
    plt.xlabel('Iteraciones')

    plt.show()
    return [xnC, i]

#falsaPosicion("((log10(7/x)/((1/10)*ln(10)))+(x*(6-x)/(((2*10**2*arccos(x/20)-x*sqrt(10**2-(x**2/4)))**2/(2*(40/ln(10))**2))*((1/(20**2*arccos(x/20)-x*sqrt(10**2-(x**2/4))))+(1/pi*10**2)))))", 0.1, 19, 10**(-10))

