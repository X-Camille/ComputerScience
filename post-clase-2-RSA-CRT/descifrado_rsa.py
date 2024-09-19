# Teorema del Resto Chino
def descifrar_con_crt(c, p, q, dp, dq, q_inv):
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

# Algoritmo de cambio de base a base decimal
def convertir_a_base_10(numero_str, base=10):
    if base < 2:
        raise ValueError("La base debe ser mayor o igual a 2.")
    if not numero_str:
        raise ValueError("El número no puede estar vacío.")
    
    # Definir los caracteres válidos para las bases mayores a 10
    caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Asegurarse de que el número sea válido para la base especificada
    if any(c not in caracteres[:base] for c in numero_str.upper()):
        raise ValueError(f"El número contiene dígitos no válidos para la base {base}.")
    
    # Convertir el número de la base n a base 10
    numero_base_10 = 0
    for caracter in numero_str.upper():
        valor_digito = caracteres.index(caracter)
        numero_base_10 = numero_base_10 * base + valor_digito
    
    return numero_base_10

def descifrar_mensaje_rsa(bloques_cifrados, p, q, dp, dq, q_inv, longitudes, base=10):
    bloques_descifrados = [descifrar_con_crt(bloque, p, q, dp, dq, q_inv) for bloque in bloques_cifrados]
    print(f"Bloques descifrados: {bloques_descifrados}")
    secuencia_decimal = [int(convertir_a_base_10(str(bloque), base)) for bloque in bloques_descifrados]
    print(f"Secuencia decimal: {secuencia_decimal}")
    secuencia_numeros = ''.join(f'{num:03d}' for num in secuencia_decimal)
    print(f"Secuencia de números: {secuencia_numeros}")
    mensaje_descifrado = convertir_a_mensaje(secuencia_numeros, longitudes)
    return mensaje_descifrado
