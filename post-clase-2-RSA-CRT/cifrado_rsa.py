# Convertir el mensaje en una secuencia de números utilizando un esquema de codificación ASCII.
def convertir_a_ascii(mensaje):
    secuencia_ascii = []
    longitudes = []
    for c in mensaje:
        codigo_ascii = f'{ord(c):03d}'
        secuencia_ascii.append(codigo_ascii)
        longitudes.append(len(codigo_ascii)) 
    secuencia_ascii_concatenada = ''.join(secuencia_ascii)
    print(f"Mensaje: '{mensaje}' convertido a secuencia ASCII: {secuencia_ascii_concatenada}")
    print(f"Longitudes de códigos ASCII: {longitudes}")
    return secuencia_ascii_concatenada, longitudes

# La secuencia ASCII se divide en bloques menores que n 
def dividir_en_bloques(secuencia_ascii, longitudes, n):
    bloques = []
    i = 0
    while i < len(secuencia_ascii):
        longitud_bloque = longitudes.pop(0)
        bloque = secuencia_ascii[i:i + longitud_bloque]
        valor_bloque = int(bloque)
        
        if valor_bloque < n:
            bloques.append(valor_bloque)
            i += longitud_bloque
        else:
            raise ValueError(f"El bloque con valor {valor_bloque} es mayor o igual a n.")
    
    print(f"Secuencia ASCII dividida en bloques: {bloques}")
    return bloques

# Algoritmo de cambio de base
def convertir_a_base(numero, base=10):
    if base < 2:
        raise ValueError("La base debe ser mayor o igual a 2.")
    if numero == 0:
        return "0"
    digitos = []
    while numero:
        digitos.append(int(numero % base))
        numero //= base
    digitos.reverse()
    return ''.join(str(digito) for digito in digitos)

# Algoritmo square and multiply
def square_and_multiply(base, exponente, modulo):
    resultado = 1
    base = base % modulo
    while exponente > 0:
        if (exponente % 2) == 1:
            resultado = (resultado * base) % modulo
        exponente = exponente >> 1
        base = (base * base) % modulo
    return resultado

# Se utilizará la variable longitudes para monitorear que sean igual a 3 tanto en el cifrado como descifrado
def cifrar_mensaje_rsa(mensaje, n, e, base=10):
    secuencia_ascii, longitudes = convertir_a_ascii(mensaje) 
    bloques = dividir_en_bloques(secuencia_ascii, longitudes.copy(), n)  # Usar copia de longitudes
    bloques_en_base = [int(convertir_a_base(bloque, base)) for bloque in bloques]
    print(f"Bloques en base: {bloques_en_base}")
    bloques_cifrados = [square_and_multiply(bloque, e, n) for bloque in bloques_en_base]
    print(f"Bloques cifrados: {bloques_cifrados}")
    
    return bloques_cifrados, longitudes

