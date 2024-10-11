from sympy import symbols, expand
from reconstruir_polinomio import reconstruir_polinomio
from generar_polinomio import generar_partes_del_secreto 

# Definir la variable simbólica para el polinomio
x = symbols('x')

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Generar polinomio aleatorio")
        print("2. Reconstruir polinomio a partir de puntos")
        print("3. Obtener clave secreta a partir de puntos")
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

            # Generar el polinomio aleatorio
            polinomio, partes = generar_partes_del_secreto(secreto, grado, n_partes)

            # Mostrar el polinomio
            print(f"El polinomio generado es: {expand(polinomio)}")

            # Mostrar los puntos generados
            print(f"Los partes a repartir el secreto son: {partes}")

        elif opcion == 2:
            # Lógica para reconstruir el polinomio a partir de puntos
            print("\n--- Reconstruir Polinomio ---")
            grado_polinomio = int(input("Ingrese el grado del polinomio a reconstruir: "))
            lista_puntos = input("Ingrese una lista de puntos (ejemplo: [(1, 2), (2, 3), (3, 4)]): ")

            # Convertir la entrada de puntos en una lista adecuada
            lista_puntos = eval(lista_puntos)

            # Verificar si hay suficientes puntos para el grado especificado
            if len(lista_puntos) < grado_polinomio + 1:
                print(f"No se puede reconstruir el polinomio. Se requieren al menos {grado_polinomio + 1} puntos.")
            else:
                resultado = expand(reconstruir_polinomio(lista_puntos))
                print(f"Polinomio reconstruido: {resultado}")


        elif opcion == 3:
            # Lógica para obtener la clave secreta (evaluando el polinomio en x=0)
            print("\n--- Obtener Clave Secreta ---")
            grado_polinomio = int(input("Ingrese el grado del polinomio a reconstruir: "))
            lista_puntos = input("Ingrese una lista de puntos (ejemplo: [(1, 246), (2, 525), (3, 960)]): ")
            lista_puntos = eval(lista_puntos)  # Convierte el string a una lista de tuplas

            # Verificar si hay suficientes puntos para el grado especificado
            if len(lista_puntos) < grado_polinomio + 1:
                print(f"No se puede reconstruir el polinomio. Se requieren al menos {grado_polinomio + 1} puntos.")
            else:
                secreto = reconstruir_polinomio(lista_puntos).subs(x, 0)  # Evaluar el polinomio en x=0
                print(f"Clave secreta obtenida (p(0)): {float(secreto)}")


        elif opcion == 0:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
