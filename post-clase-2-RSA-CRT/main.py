import claves_rsa
import cifrado_rsa
import descifrado_rsa

def menu_principal():
    keys = None  # Variable para almacenar las claves RSA generadas
    while True:
        print("--- Menú Principal ---")
        print("1. Generar claves RSA")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            bits = int(input("Ingrese el número de bits para los primos: "))
            keys = generar_claves(bits)
            menu_cifrado_descifrado(keys)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def generar_claves(bits):
    print("Iniciando generación de claves RSA...")
    keys = claves_rsa.generar_claves_rsa(bits=bits)
    print("Claves RSA generadas correctamente.")
    return keys

def mostrar_claves(keys):
    public_key = keys['public_key']
    private_key = keys['private_key']
    
    print("--- Claves RSA ---")
    print(f"Clave Pública (e, n): {public_key}")
    print(f"Clave Privada (d, n): {private_key}")

def menu_cifrado_descifrado(keys):
    public_key = keys['public_key']
    values = keys['values']
    
    while True:
        print("\n--- Menú Cifrado/Descifrado ---")
        print("1. Cifrar y descifrar un mensaje")
        print("2. Mostrar claves RSA")
        print("3. Atrás")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mensaje_original = input("Ingrese un mensaje de texto: ")
            base = int(input("Ingrese el valor de la base: "))
            
            # Cifrar el mensaje
            bloques_cifrados, longitudes = cifrado_rsa.cifrar_mensaje_rsa(
                mensaje_original, 
                public_key[1], 
                public_key[0], 
                base
            )
            print(f"Mensaje cifrado en bloques: {bloques_cifrados}")
            
            # Descifrar el mensaje
            mensaje_descifrado = descifrado_rsa.descifrar_mensaje_rsa(
                bloques_cifrados, 
                values[0], 
                values[1], 
                values[2], 
                values[3], 
                values[4], 
                longitudes, 
                base
            )
            print(f"Mensaje descifrado: '{mensaje_descifrado}'")    
        elif opcion == "2":
            if keys:
                mostrar_claves(keys)
            else:
                print("Primero debe generar las claves RSA.")       
        elif opcion == "3":
            print("Terminando el programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
