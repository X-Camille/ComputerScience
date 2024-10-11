def reconstruir_polinomio(lista_puntos, grado_polinomio):
    if len(lista_puntos) < grado_polinomio + 1:
        print(f"No se puede reconstruir el polinomio. Se requieren al menos {grado_polinomio + 1} puntos.")
    else:
        # Truncar la lista de puntos si hay más de los necesarios
        lista_puntos = lista_puntos[:grado_polinomio + 1]  # Mantener solo los necesarios
        c = [punto[0] for punto in lista_puntos]   # Solo coordenadas x
        c_y = [punto[1] for punto in lista_puntos] # Solo coordenadas y
        polinomio_reconstruido = 0

        for j in range(len(c)): 
            delta = base_lagrange(j, c) 
            polinomio_reconstruido += c_y[j] * delta 

        # Evaluar el polinomio en x = 0
        return round(polinomio_reconstruido, 1)  # Retorna el valor del polinomio en x=0

def base_lagrange(j, c):
    numerador = 1
    denominador = 1
    for i in range(len(c)):  # j es el punto fijo
        if i != j:  # Solo cuando i != j
            numerador *= (0 - c[i])     # (0 - x_i) evaluado en x = 0
            denominador *= (c[j] - c[i]) # (x_j - x_i)
    return numerador / denominador

    
        

    