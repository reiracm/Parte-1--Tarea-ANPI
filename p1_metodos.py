from sympy import *
from numpy import *
import numpy as np

def isBolsano(a, b, func):
    x = a
    fa = eval(func)
    print(fa)
    x = b
    fb = eval(func)
    print(fb)
    return (fa * fb <= 0)

def biseccion(f, a, b, tol):
    i = 0
    x = 0
    if (isBolsano(a, b, f)):
        tempA = a
        tempB = b
        e = (b - a) / 2
        while (e >= tol):
            x = (tempA + tempB) / 2
            if(isBolsano(x, tempB, f)):
              tempA = x
            elif(isBolsano(tempA, x, f)):
              tempB = x
            i = i + 1
            e = (b - a) / (2**i)
    return i, x

#biseccion("((log10(7/x)/(1/10)*ln(10))+(x*(6-x)/(((2*10**2*arccos(x/2*10)-x*sqrt(10**2-(x**2/4)))**2/2*(10*4/ln(10)))**2)*((1/(2*10**2*arccos(x/2*10)-x*sqrt(10**2-(x**2/4))))+(1/pi*10**2))))", 1, 2, 0.01)

def secante(f, x0, x1, tol):
    xCurr = x1
    xPrev = x0
    i = 1
    tempTol = 1
    while ( tempTol >= tol):
        i = i + 1
        x = xCurr
        fxCurr = eval(f)
        print(fxCurr)
        x = xPrev
        fxPrev = eval(f)
        xAprox = xCurr - ((xCurr - xPrev) / (fxCurr - fxPrev)) * fxCurr
        xPrev = xCurr
        tempTol = (abs(xAprox - xCurr) / xAprox)
        xCurr = xAprox
    return xAprox, i

#secante("log10(7/x)/(1/10)*ln(10)+x*(6-x)/((2*10**2*arccos(x/(2*10))-x*sqrt(10**2-(x**2/4)))**2/(2*(10*4/ln(10)))**2*(1/(2*10**2*arccos(x/(2*10))-x*sqrt(10**2-(x**2/4)))+(1/pi*10**2)))", 0, 1, 0.001)

def falsaPosicion(f, x0, x1, tol):
    xCurr = x1
    xPrev = x0
    i = 1
    tempTol = 1
    if(isBolsano(x0,x1,f)):
        while(tempTol >= tol):
            i = i + 1
            x = xCurr
            fxCurr = eval(f)
            x = xPrev
            fxPrev = eval(f)
            xAprox = xCurr - ((xCurr - xPrev) / (fxCurr - fxPrev)) * fxCurr
            tempTol = (abs(xAprox - xCurr) / xAprox)
            if(isBolsano(xPrev, xAprox, f)):
                xCurr = xAprox
            elif(isBolsano(xAprox, xCurr, f)):
                xPrev = xAprox
    return xAprox, i
