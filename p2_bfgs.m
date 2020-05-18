function gradienteR=p2_bfgs(f,variables,pk,x0) 
  pkg load symbolic;
  syms x,y;  
  #Se necesita encontrar el gradiente de la funcion f primero
  xk=x0
  B=eye(4,4)         #Matriz Identidad
  Bk=B
  lambdak=1;         #Considerar el valor inicial de lambda 1
  sigma1=0.5;
  sigma2=0.2;   
  error= norm(g)   # El error es la norma del gradiente de f
  
  #METODO BFGS
  
  while(error>0.00001)
    g = gradient(f,x) 
    gT= transpose(g)   #Traspuesta del Gxk que es el gradiente
    pk=inv(B)*gk       #Matriz Inversa por gk
    
    # Wolfe-type inexact line search para determinar ?k
    
    while (f(xk+lambdak*pk) > f(xk)+ sigma1*lambdak*gT(xk)*pk & gT(xk+lambdakpk)*pk < sigma2*gT(xk)*pk)
      lambdak=lambdak/2;
    endwhile
    
    xk1 = xk + lambdak*pk
    sk = xk1 + xk
    
    # Determinar Bk+1
    ykT=transpose(yk)
    if (ykT*sk>0)
      skT=transpose(sk)
      Bk= B- ((B*sk*skT*B)/(skT*B*sk)) + ((ykt*yk)/(ykt*sk))
    else
      Bk=B
    endif
    
    xk=xk1
    error=transpose(gradient(funcion,x))
    # yk=  NO SE A QUIEN SE ACTUALIZA

  endwhile
    
  
  
  
  
endfunction