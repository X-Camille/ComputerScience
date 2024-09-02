import tkinter as tk
from tkinter import messagebox

def calcular_inversa_modular(a, n):
    coeficiente_actual = 0
    coeficiente_nuevo = 1
    residuo_actual = n
    residuo_nuevo = a
    
    while residuo_nuevo != 0:
        cociente = residuo_actual // residuo_nuevo
        
        # Se actualiza coeficiente y residuo
        coeficiente_actual, coeficiente_nuevo = coeficiente_nuevo, coeficiente_actual - cociente * coeficiente_nuevo
        residuo_actual, residuo_nuevo = residuo_nuevo, residuo_actual - cociente * residuo_nuevo
    
    if residuo_actual > 1:
        return None  # No existe el inverso modular
    
    # Se ajusta el coeficiente para que sea positivo
    if coeficiente_actual < 0:
        coeficiente_actual += n
    
    return coeficiente_actual

def cifrar_mensaje(mensaje, a, b, alfabeto):
    mensaje_cifrado = []
    for letra in mensaje:
        if letra.lower() in alfabeto:
            # Obtiene la posición de la letra del mensaje en el alfabeto
            posicion_original = alfabeto.index(letra.lower())
            # Se aplica la fórmula del cifrado
            posicion_nueva = (a * posicion_original + b) % len(alfabeto)
            # Mantener el caso original de la letra
            if letra.isupper():
                mensaje_cifrado.append(alfabeto[posicion_nueva].upper())
            else:
                mensaje_cifrado.append(alfabeto[posicion_nueva])
        else:
            mensaje_cifrado.append(letra)
    return ''.join(mensaje_cifrado)

def descifrar_mensaje(mensaje, a, b, alfabeto):
    mensaje_descifrado = []
    a_inv = calcular_inversa_modular(a, len(alfabeto))
    if a_inv is None:
        messagebox.showerror("Error", "No se pudo encontrar el inverso multiplicativo de a.")
        return ""
    
    for letra in mensaje:
        if letra.lower() in alfabeto:
            # Obtiene la posición de la letra del mensaje en el alfabeto
            posicion_original = alfabeto.index(letra.lower())
            # Se aplica la fórmula del descifrado
            posicion_nueva = (a_inv * (posicion_original - b)) % len(alfabeto)
            # Mantener el caso original de la letra
            if letra.isupper():
                mensaje_descifrado.append(alfabeto[posicion_nueva].upper())
            else:
                mensaje_descifrado.append(alfabeto[posicion_nueva])
        else:
            mensaje_descifrado.append(letra)
    return ''.join(mensaje_descifrado)

def procesar_mensaje():
    mensaje = entry_mensaje.get()
    a = entry_a.get()
    b = entry_b.get()
    alfabeto = entry_alfabeto.get()

    # Verifica que a y b sean números enteros
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        messagebox.showerror("Error", "Los valores de a y b deben ser números enteros.")
        return

    if not alfabeto:
        alfabeto = "abcdefghijklmnopqrstuvwxyz"  # Alfabeto por defecto

    cifrado = cifrar_mensaje(mensaje, a, b, alfabeto)
    descifrado = descifrar_mensaje(cifrado, a, b, alfabeto)

    # Actualiza las etiquetas con los resultados
    label_original_resultado.config(text=f"Mensaje original: {mensaje}")
    label_cifrado_resultado.config(text=f"Mensaje cifrado: {cifrado}")
    label_descifrado_resultado.config(text=f"Mensaje descifrado: {descifrado}")

def crear_interfaz():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Cifrado Afín")

    # Crear y colocar los widgets
    tk.Label(ventana, text="Mensaje:").grid(row=0, column=0, padx=10, pady=5)
    global entry_mensaje
    entry_mensaje = tk.Entry(ventana, width=50)
    entry_mensaje.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Clave a:").grid(row=1, column=0, padx=10, pady=5)
    global entry_a
    entry_a = tk.Entry(ventana, width=50)
    entry_a.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Clave b:").grid(row=2, column=0, padx=10, pady=5)
    global entry_b
    entry_b = tk.Entry(ventana, width=50)
    entry_b.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Alfabeto:").grid(row=3, column=0, padx=10, pady=5)
    global entry_alfabeto
    entry_alfabeto = tk.Entry(ventana, width=50)
    entry_alfabeto.insert(0, "abcdefghijklmnopqrstuvwxyz")  # Alfabeto por defecto
    entry_alfabeto.grid(row=3, column=1, padx=10, pady=5)

    btn_procesar = tk.Button(ventana, text="Procesar", command=procesar_mensaje)
    btn_procesar.grid(row=4, column=0, columnspan=2, pady=10)

    global label_original_resultado
    label_original_resultado = tk.Label(ventana, text="Mensaje original:")
    label_original_resultado.grid(row=5, column=0, columnspan=2, pady=5)

    global label_cifrado_resultado
    label_cifrado_resultado = tk.Label(ventana, text="Mensaje cifrado:")
    label_cifrado_resultado.grid(row=6, column=0, columnspan=2, pady=5)

    global label_descifrado_resultado
    label_descifrado_resultado = tk.Label(ventana, text="Mensaje descifrado:")
    label_descifrado_resultado.grid(row=7, column=0, columnspan=2, pady=5)

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()

def probar_cifrado_descifrado():
    # Pruebas con diferentes mensajes y claves
    pruebas = [
        {"mensaje": "Cifrado César es muy útil en criptografía.", "a": 5, "b": 8, "alfabeto": "abcdefghijklmnopqrstuvwxyz"},
        {"mensaje": "Enviar al correo ejemplo@gmail.com.", "a": 7, "b": 3, "alfabeto": "abcdefghijklmnopqrstuvwxyz"},
        {"mensaje": "Mi número favorito es el 8.", "a": 9, "b": 4, "alfabeto": "abcdefghijklmnopqrstuvwxyz"},
        {"mensaje": "La Lycoris Radiata es muy linda.", "a": 3, "b": 1, "alfabeto": "abcdefghijklmnopqrstuvwxyz"},
        {"mensaje": "Pero prefiero las rosas negras.", "a": 11, "b": 6, "alfabeto": "abcdefghijklmnopqrstuvwxyz"}
    ]
    
    for prueba in pruebas:
        mensaje = prueba["mensaje"]
        a = prueba["a"]
        b = prueba["b"]
        alfabeto = prueba["alfabeto"]
        
        print(f"Prueba con el mensaje: {mensaje}")
        print(f"Clave a: {a}, Clave b: {b}, Alfabeto: {alfabeto}")
        
        # Cifrar el mensaje
        mensaje_cifrado = cifrar_mensaje(mensaje, a, b, alfabeto)
        print(f"Mensaje cifrado: {mensaje_cifrado}")
        
        # Descifrar el mensaje cifrado
        mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, a, b, alfabeto)
        print(f"Mensaje descifrado: {mensaje_descifrado}")
        
        print("-" * 50)

probar_cifrado_descifrado()

if __name__ == "__main__":
    crear_interfaz()