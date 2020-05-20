def ssm(func,xo,tol):

    
    f = lambda x: eval(func, {'x': x, 'pi': np.pi, 'e': np.e,
                                  'exp': exp, 'sqrt': sqrt,
                                  'arccos': acos, 'sin': sin, 'tan': tan, 
                                  'ln': np.log, 'log10': math.log10})
        
    xC = xo
    itera = 0
    error = [ ]
    iteracion = [ ]
    tempTol = 1
        
    while(tempTol >= tol):

        itera += 1

        fx = f(xC)
        print(fx)
        z = f(xC +fx)
        print(z)
            
        y = xC - ((fx**2)/(z-fx))
        fy = f(y)
          
        xAprox = xC - (fx**3)/((z-fx)*(fx-fy))
            
        xC = xAprox
        tempTol = abs(xC-xAprox)
        error.append(tempTol)
        iteracion.append(itera)
            
    #if(graf == 1):
    plt.plot(iteracion,error)
    plt.ylabel('Errores')
    plt.xlabel('Iteraciones')
    plt.show()

    return xAprox, itera
