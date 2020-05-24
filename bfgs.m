function [lambdak, xk,error]=bfgs(f,variables,iter) 
  pkg load symbolic;
  syms x1 x2 x3 x4 x5 x6 x7 x8 ;
  variables = [x1 x2 x3 x4 x5 x6 x7 x8];
  iter = 0;
  f=sym('(x1+10*x2)**2 + 5*(x3-x4)**2 + (x2-x3)**4 + 10*(x1-x4)**4 +(x5+10*x6)**2 + 5*(x7 - x8)**2 + (x6 - x7)**4 + 10*(x5 - x8)**4');     %Convierte f (char) a symbolic
  x0=[0.00001,0.00001,0.00001,0.00001,0.00001,0.00001,0.00001,0.00001];     %Vector Inicial
  x0=reshape(x0,8,1);  % Vector Inicial dado como matriz
  xk=x0;
  lambdak=1;
  sigma1=0.0025;
  sigma2=0.005;
  
  g=gradient(f, variables); %Gradiente de f
  gxk=subs(g, variables, xk);  %Gradiente evaluado en el vector inicial, es vector columna
  error= double(norm(gxk)); 
  B=eye(8,8) ;        #Matriz Identidad
  Bk=B;
  kiter=1;
  
  while ((error>0.01)|(iter>20))
     gxk=subs(g, variables, xk);  %Gradiente evaluado en el vector inicial, es vector columna
     pk=inv(B)*-gxk;   
     numero=sigma1*lambdak* double(transpose(gxk)*pk);
     primero=double(subs(f, variables, (xk+lambdak*pk)));
     segundo=double(subs(f, variables, xk)) + sigma1*lambdak* double(transpose(gxk)*pk);
     tercero= double(double(transpose(subs(g, variables, xk+lambdak*pk)))*pk);
     cuarto=double(double(transpose(subs(g, variables,xk)))*pk)*sigma2;
        # Wolfe-type inexact line search para determinar ?k  
     while (!((primero <= segundo)&&(tercero >= cuarto)))
       lambdak=double(lambdak/(2**kiter))
       if (lambdak < 10^-5)
        break;
       endif
       primero=double(subs(f, variables, (xk+lambdak*pk)));
       segundo=double(subs(f, variables, xk)) + sigma1*lambdak* double(transpose(gxk)*pk);
       tercero= double(double(transpose(subs(g, variables, xk+lambdak*pk)))*pk);
       cuarto=double(double(transpose(subs(g, variables,xk)))*pk)*sigma2;
       kiter ++;
     endwhile
     disp("SALI")
     xk1=xk+lambdak*pk;
     sk=xk1-xk;
     yk=subs(g, variables, xk1)-subs(g, variables, xk);
     skt=transpose(sk);
     ykt=transpose(yk);
     uno=double((ykt*sk)/(norm(sk))**2);
     dos=double(norm(subs(g, variables, xk)));   
     Bk=B- ((B*sk*skt*B)/(skt*Bk*sk)) +((yk*ykt)/(ykt*sk));
     xk=xk1;
     error= double(norm(subs(g, variables, xk)))  %Gradiente evaluado en el vector inicial, es vector columna
     iter ++
     
         
  endwhile
     xk=double(xk)
endfunction

