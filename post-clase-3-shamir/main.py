from generar_polinomio import generar_polinomio_aleatorio, obtener_puntos_polinomio
from reconstruir_polinomio import reconstruir_polinomio
from pruebas_seguridad import ejecutar_pruebas

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Generar polinomio aleatorio")
        print("2. Obtener clave secreta a partir de puntos")
        print("3. Ejecutar pruebas de seguridad")
        print("0. Salir")

        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            continue

        if opcion == 1:
            # Lógica para generar el polinomio aleatorio
            print("\n--- Generar Polinomio Aleatorio ---")
            secreto = int(input("Ingrese el secreto (término independiente): "))
            grado = int(input("Ingrese el grado del polinomio: "))
            n_partes = int(input("Ingrese la cantidad de partes a repartir el secreto: "))

            # Validar que el número de partes sea suficiente para reconstruir el secreto
            if n_partes < grado + 1:
                print(f"Error: Debe ingresar al menos {grado + 1} partes para poder reconstruir el secreto.")
            else:
                # Generar el polinomio aleatorio
                coeficientes = generar_polinomio_aleatorio(secreto, grado)
                partes = obtener_puntos_polinomio(coeficientes, n_partes)

                # Mostrar el polinomio
                print(f"El polinomio generado tiene coeficientes: {coeficientes}")

                # Mostrar los puntos generados
                print(f"Las partes a repartir el secreto son: {partes}")

        elif opcion == 2:
            # Lógica para reconstruir el polinomio a partir de puntos
            print("\n--- Reconstruir Polinomio ---")
            grado_polinomio = int(input("Ingrese el grado del polinomio a reconstruir: "))
            lista_puntos = input("Ingrese una lista de puntos (ejemplo: [(1, 2), (2, 3), (3, 4)]): ")

            # Convertir la entrada de puntos en una lista adecuada
            lista_puntos = eval(lista_puntos)

            # Verificar si hay suficientes puntos para el grado especificado
        
            resultado = reconstruir_polinomio(lista_puntos, grado_polinomio)
            print(f"Clave secreta del polinomio reconstruido: {resultado:.1f}")
                
        elif opcion == 3:
            ejecutar_pruebas()

        elif opcion == 0:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()