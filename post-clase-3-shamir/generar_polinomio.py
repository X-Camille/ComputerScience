import random
from sympy import symbols

# Definir la variable simbólica para el polinomio
x = symbols('x')

def generar_polinomio_aleatorio(secreto, grado): 
    coeficientes = [secreto]  # El coeficiente del término independiente es el secreto
    for _ in range(1, grado + 1):
        coeficientes.append(random.randint(1, 250))  # Coeficientes aleatorios entre 1 y 1000
    polinomio = sum(coef * (x ** idx) for idx, coef in enumerate(coeficientes))
    return polinomio, coeficientes

def obtener_puntos_polinomio(coeficientes, n_partes):
    puntos = []
    for _ in range(n_partes):
        valor = random.randint(1, 250)  # Valor aleatorio para evaluar el polinomio
        y = evaluar_polinomio(coeficientes, valor)
        puntos.append((valor, y))  # (x, y) donde x es el valor e y es la evaluación
    return puntos

def evaluar_polinomio(coeficientes, valor):
    resultado = sum(coef * (valor ** idx) for idx, coef in enumerate(coeficientes))
    return resultado

# Función principal que controla la generación del polinomio y las partes
def generar_partes_del_secreto(secreto, grado, n_partes):
    if n_partes < grado + 1:
        raise ValueError(f"Debes pedir al menos {grado + 1} partes para reconstruir el secreto.")
    
    polinomio, coeficientes = generar_polinomio_aleatorio(secreto, grado)
    partes = obtener_puntos_polinomio(coeficientes, n_partes)
    return polinomio, partes