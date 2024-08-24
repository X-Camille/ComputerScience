import tkinter as tk
from tkinter import messagebox

def cifrar_mensaje(mensaje, key, alfabeto):
    mensaje_cifrado = []
    for letra in mensaje:
        if letra.lower() in alfabeto:
            # Obtiene la posición de la letra del mensaje en el alfabeto
            posicion_original = alfabeto.index(letra.lower())
            # Se aplica la clave de desplazamiento
            posicion_nueva = (posicion_original + key) % len(alfabeto)
            # Mantener el caso original de la letra
            if letra.isupper():
                mensaje_cifrado.append(alfabeto[posicion_nueva].upper())
            else:
                # Obtiene la nueva letra del mensaje cifrado
                mensaje_cifrado.append(alfabeto[posicion_nueva]) 
        else:
            # Si el carácter no está en el alfabeto, se agrega sin cambios
            mensaje_cifrado.append(letra)
    # Convierte la lista de caracteres en una cadena de texto
    return ''.join(mensaje_cifrado)

def descifrar_mensaje(mensaje, key, alfabeto):
    mensaje_descifrado = []
    for letra in mensaje:
        if letra.lower() in alfabeto:
            # Obtiene la posición de la letra del mensaje en el alfabeto
            posicion_original = alfabeto.index(letra.lower())
            # Se aplica la clave de desplazamiento en sentido inverso
            posicion_nueva = (posicion_original - key) % len(alfabeto)
            # Mantener el caso original de la letra
            if letra.isupper():
                mensaje_descifrado.append(alfabeto[posicion_nueva].upper())
            else:
                # Obtiene la nueva letra del mensaje descifrado
                mensaje_descifrado.append(alfabeto[posicion_nueva])
        else:
            # Si el carácter no está en el alfabeto, se mantiene sin cambios
            mensaje_descifrado.append(letra)
    # Convierte la lista de caracteres en una cadena de texto
    return ''.join(mensaje_descifrado)

def probar_cifrado():
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    # Caso 1
    mensaje1 = "La ciberseguridad de las empresas es importante para todos"
    key1 = 6
    cifrado1 = cifrar_mensaje(mensaje1, key1, alfabeto)
    descifrado1 = descifrar_mensaje(cifrado1, key1, alfabeto)
    print("Caso 1:")
    print(f"Mensaje original: {mensaje1}")
    print(f"Mensaje cifrado:  {cifrado1}")
    print(f"Mensaje descifrado: {descifrado1}")
    print()

    # Caso 2
    mensaje2 = "Cifrado César es muy útil en criptografía."
    key2 = 10
    cifrado2 = cifrar_mensaje(mensaje2, key2, alfabeto)
    descifrado2 = descifrar_mensaje(cifrado2, key2, alfabeto)
    print("Caso 2:")
    print(f"Mensaje original: {mensaje2}")
    print(f"Mensaje cifrado:  {cifrado2}")
    print(f"Mensaje descifrado: {descifrado2}")
    print()
    
    # Caso 3
    mensaje3 = "Enviar al correo ejemplo@gmail.com."
    key3 = 5
    cifrado3 = cifrar_mensaje(mensaje3, key3, alfabeto)
    descifrado3 = descifrar_mensaje(cifrado3, key3, alfabeto)
    print("Caso 3:")
    print(f"Mensaje original: {mensaje3}")
    print(f"Mensaje cifrado:  {cifrado3}")
    print(f"Mensaje descifrado: {descifrado3}")
    print()
    
    # Caso 4
    mensaje4 = "Mi número favorito es el 8."
    key4 = 2
    cifrado4 = cifrar_mensaje(mensaje4, key4, alfabeto)
    descifrado4 = descifrar_mensaje(cifrado4, key4, alfabeto)
    print("Caso 4:")
    print(f"Mensaje original: {mensaje4}")
    print(f"Mensaje cifrado:  {cifrado4}")
    print(f"Mensaje descifrado: {descifrado4}")
    print()

def procesar_mensaje():
    mensaje = entry_mensaje.get()
    key = entry_clave.get()
    alfabeto = entry_alfabeto.get()

    # Verifica que el key sea un número
    try:
        key = int(key)
    except ValueError:
        messagebox.showerror("Error", "La clave de desplazamiento debe ser un número entero.")
        return

    if not alfabeto:
        alfabeto = "abcdefghijklmnopqrstuvwxyz"  # Alfabeto por defecto

    cifrado = cifrar_mensaje(mensaje, key, alfabeto)
    descifrado = descifrar_mensaje(cifrado, key, alfabeto)

    # Actualiza las etiquetas con los resultados
    label_original_resultado.config(text=f"Mensaje original: {mensaje}")
    label_cifrado_resultado.config(text=f"Mensaje cifrado: {cifrado}")
    label_descifrado_resultado.config(text=f"Mensaje descifrado: {descifrado}")

def crear_interfaz():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Cifrado César")

    # Crear y colocar los widgets
    tk.Label(ventana, text="Mensaje:").grid(row=0, column=0, padx=10, pady=5)
    global entry_mensaje
    entry_mensaje = tk.Entry(ventana, width=50)
    entry_mensaje.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Clave de desplazamiento:").grid(row=1, column=0, padx=10, pady=5)
    global entry_clave
    entry_clave = tk.Entry(ventana, width=50)
    entry_clave.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Alfabeto:").grid(row=2, column=0, padx=10, pady=5)
    global entry_alfabeto
    entry_alfabeto = tk.Entry(ventana, width=50)
    entry_alfabeto.insert(0, "abcdefghijklmnopqrstuvwxyz")  # Alfabeto por defecto
    entry_alfabeto.grid(row=2, column=1, padx=10, pady=5)

    btn_procesar = tk.Button(ventana, text="Procesar", command=procesar_mensaje)
    btn_procesar.grid(row=3, column=0, columnspan=2, pady=10)

    global label_original_resultado
    label_original_resultado = tk.Label(ventana, text="Mensaje original:")
    label_original_resultado.grid(row=4, column=0, columnspan=2, pady=5)

    global label_cifrado_resultado
    label_cifrado_resultado = tk.Label(ventana, text="Mensaje cifrado:")
    label_cifrado_resultado.grid(row=5, column=0, columnspan=2, pady=5)

    global label_descifrado_resultado
    label_descifrado_resultado = tk.Label(ventana, text="Mensaje descifrado:")
    label_descifrado_resultado.grid(row=6, column=0, columnspan=2, pady=5)

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()

if __name__ == "__main__":
    crear_interfaz()