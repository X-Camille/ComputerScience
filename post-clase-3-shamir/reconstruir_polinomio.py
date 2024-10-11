from sympy import symbols, expand, N

# Por ejemplo, el polinomio es 123 + 45x + 78x^2
# Por lo tanto, el secreto es p(0) = 123
# Si el polinomio es grado 2, se necesitan 3 puntos para reconstruir
# Los puntos serán p(1)= 246, p(2) = 525 y p(3) = 960

# Se define una variable simbólica 
x = symbols('x')

def reconstruir_polinomio(lista_puntos, valor_x=None):
    c = [punto[0] for punto in lista_puntos]   # Solo oordenadas x
    c_y = [punto[1] for punto in lista_puntos] # Solo oordenadas y
    polinomio_reconstruido = 0
    for j in range(len(c)): 
        delta = base_lagrange(x, j, c) 
        polinomio_reconstruido += c_y[j] * delta 
    
    # Verificar si se ha proporcionado un valor para x
    if valor_x is not None:
        return float(N(polinomio_reconstruido.subs(x, valor_x)))  # Evaluar el polinomio en valor_x
    else:
        return expand(polinomio_reconstruido)  # Expandir el polinomio simbólicamente

def base_lagrange(x, j, c):
    numerador = 1
    denominador = 1
    for i in range(len(c)): # j es el punto fijo
        if i != j:  # Solo cuando i != j
            numerador *= (x - c[i])     # (x - x_i)
            denominador *= (c[j] - c[i]) # (x_j - x_i)
    return numerador / denominador

    
        

    