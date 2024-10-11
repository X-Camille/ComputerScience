from reconstruir_polinomio import reconstruir_polinomio

def ejecutar_pruebas():
    grado_polinomio = 2
    puntos_suficientes = [(26, 25790), (11, 6455), (10, 5646)]
    puntos_faltantes = [(26, 25790), (11, 6455)]  # Menos de 3 puntos
    puntos_sobrantes = [(26, 25790), (11, 6455), (10, 5646), (85, 232821)]  # Más de 3 puntos
    
    clave_secreta = 856
    
    print("Primera prueba: Puntos suficientes")
    resultado = reconstruir_polinomio(puntos_suficientes, grado_polinomio)
    if resultado is not None:  # Solo imprimir si el resultado no es None
        print(resultado)
    print(f"Salida esperada: {clave_secreta}\n")
    
    print("Segunda prueba: Puntos faltantes")
    resultado = reconstruir_polinomio(puntos_faltantes, grado_polinomio)
    if resultado is not None:  # Solo imprimir si el resultado no es None
        print(resultado)
    print(f"Salida esperada: No se puede reconstruir el polinomio. Se requieren al menos 3 puntos.")
    
    print("\nTercera prueba: Puntos sobrantes")
    resultado = reconstruir_polinomio(puntos_sobrantes, grado_polinomio)
    if resultado is not None:  # Solo imprimir si el resultado no es None
        print(resultado)
    print(f"Salida esperada: {clave_secreta}")
