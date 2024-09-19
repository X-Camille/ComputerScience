# Teorema del Resto Chino
def descifrar_con_crt(c, p, q, d, dp, dq, q_inv):
    # Calcular m1 y m2
    m1 = square_and_multiply(c, dp, p)
    m2 = square_and_multiply(c, dq, q)
    
    # Combinar m1 y m2
    h = (q_inv * (m2 - m1)) % p
    m = m1 + h * p
    return m

# Algoritmo square and multiply (para descifrado)
def square_and_multiply(base, exponente, modulo):
    resultado = 1
    base = base % modulo
    while exponente > 0:
        if (exponente % 2) == 1:
            resultado = (resultado * base) % modulo
        exponente = exponente >> 1  # División entera por 2
        base = (base * base) % modulo
    return resultado

# Convertir la base `n` a base decimal
def convertir_a_decimal(numero_base_n, base):
    return int(str(numero_base_n), base)

# Convertir la secuencia de números a mensaje ASCII
def convertir_a_mensaje(secuencia_numeros, longitudes):
    mensaje = ""
    i = 0
    while i < len(secuencia_numeros):
        if not longitudes:  # Verifica si longitudes está vacío
            break
        
        longitud = longitudes.pop(0)
        bloque = secuencia_numeros[i:i + longitud]
        mensaje += chr(int(bloque))
        i += longitud
    print(f"Secuencia numérica convertida a mensaje: '{mensaje}'")
    return mensaje

def descifrar_mensaje_rsa(bloques_cifrados, n, d, p, q, dp, dq, q_inv, longitudes):
    bloques_base_decimal = [convertir_a_decimal(bloque, 10) for bloque in bloques_cifrados]
    bloques_descifrados = [descifrar_con_crt(bloque, p, q, d, dp, dq, q_inv) for bloque in bloques_cifrados]
    secuencia_decimal = [convertir_a_decimal(bloque, 10) for bloque in bloques_descifrados]
    secuencia_numeros = ''.join(f'{num:03d}' for num in secuencia_decimal)
    mensaje_descifrado = convertir_a_mensaje(secuencia_numeros, longitudes)
    print(f"Bloques descifrados: {bloques_descifrados}")
    return mensaje_descifrado
