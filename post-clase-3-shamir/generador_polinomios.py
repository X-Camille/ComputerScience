import random

def generar_polinomio_aleatorio(secreto, grado): 
    coeficientes = [secreto]  # El coeficiente del término independiente es el secreto
    for _ in range(1, grado + 1):
        coeficientes.append(random.randint(1, 250))  # Coeficientes aleatorios entre 1 y 250
    return coeficientes  # Retorna solo los coeficientes

def obtener_puntos_polinomio(coeficientes, n_partes):
    puntos = []
    for _ in range(n_partes):
        valor = random.randint(1, 100)  # Valor aleatorio para evaluar el polinomio
        y = evaluar_polinomio(coeficientes, valor)
        puntos.append((valor, y)) 
    return puntos

def evaluar_polinomio(coeficientes, valor):
    resultado = sum(coef * (valor ** idx) for idx, coef in enumerate(coeficientes))
    return resultado

# Función principal que controla la generación del polinomio y las partes
def generar_partes_del_secreto(secreto, grado, n_partes):
    if n_partes < grado + 1:
        raise ValueError(f"Debe pedir al menos {grado + 1} partes para reconstruir el secreto.")
    
    coeficientes = generar_polinomio_aleatorio(secreto, grado)
    partes = obtener_puntos_polinomio(coeficientes, n_partes)
    return coeficientes, partes  # Retorna los coeficientes y las partes