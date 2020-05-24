function Bk=bfgs(f,variables,iter) 
  pkg load symbolic;
  syms x y;

  f=sym(f);     %Convierte f (char) a symbolic
  x0=[1,1];     %Vector Inicial
  x0=reshape(x0,2,1);  % Vector Inicial dado como matriz
  xk=x0;
  lambdak=1;
  sigma1=0.25;
  sigma2=0.5;
  
  g=gradient(f, variables); %Gradiente de f
  gxk=subs(g, variables, xk);  %Gradiente evaluado en el vector inicial, es vector columna
  error= double(norm(gxk)); 
  B=eye(2,2) ;        #Matriz Identidad
  
  while ((iter>0))
     gxk=subs(g, variables, xk);  %Gradiente evaluado en el vector inicial, es vector columna
     pk=-inv(B)*gxk;   
     numero=sigma1*lambdak* double(transpose(gxk)*pk);
     primero=double(subs(f, variables, (xk+lambdak*pk)));
     segundo=double(subs(f, variables, xk)) + sigma1*lambdak* double(transpose(gxk)*pk);
     tercero= double(double(transpose(subs(g, variables, xk+lambdak*pk)))*pk);
     cuarto=double(double(transpose(subs(g, variables,xk)))*pk)*sigma2;
        # Wolfe-type inexact line search para determinar ?k  
     while ((primero<segundo)&&(tercero > cuarto))
       lambdak=double(lambdak/2);
     endwhile
     xk1=xk+lambdak*pk;
     sk=xk1-xk;
     yk=subs(g, variables, xk1)-subs(g, variables, xk);
     skt=transpose(sk);
     ykt=transpose(yk);
     uno=double((ykt*sk)/(norm(sk))**2)
     dos=double(norm(subs(g, variables, xk)))
     if (((ykt*sk)/(norm(sk))**2)>norm(subs(g, variables, xk)))
       Bk=B- ((B*sk*skt*B)/(skt*Bk*sk)) +((yk*ykt)/(ykt*sk));
     else
       Bk=B;
     endif
     xk=xk1
     error= double(norm(subs(g, variables, xk)))  %Gradiente evaluado en el vector inicial, es vector columna
     iter=iter-1
     
    
  endwhile

 
endfunction