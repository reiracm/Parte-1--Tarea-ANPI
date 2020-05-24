function T=prueba(funcion)
  pkg load symbolic
  syms x y;
  gradienteR = gradient(funcion, [x])
  respuesta=matlabFunction(gradienteR);
  [cf,T] = coeffs(gradienteR);
  V = cf .* T    ;
  T=transpose(V);
  resultado=subs(T, {x}, {5});
  class(T);
endfunction