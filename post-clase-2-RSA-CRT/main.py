import claves_rsa, cifrado_rsa, descifrado_rsa
        
def main():
    print("Iniciando generación de claves RSA...")
    # Generar claves RSA
    keys = claves_rsa.generar_claves_rsa(bits=1024)
    public_key = keys['public_key']
    private_key = keys['private_key']
    values = keys['values']

    mensaje_original = "Hola"
    
    # Cifrar el mensaje
    bloques_cifrados, longitudes =cifrado_rsa.cifrar_mensaje_rsa(mensaje_original, public_key[1], public_key[0])
    
    # Descifrar el mensaje
    mensaje_descifrado = descifrado_rsa.descifrar_mensaje_rsa(
        bloques_cifrados, 
        private_key[1], 
        private_key[0], 
        values[0], 
        values[1], 
        values[2], 
        values[3], 
        values[4],
        longitudes
    )
    print(f"Mensaje descifrado: '{mensaje_descifrado}'")

if __name__ == "__main__":
    main()

    


