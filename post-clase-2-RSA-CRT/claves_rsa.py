import random
import miller_rabin

# Generación de claves RSA
# Seleccionar dos números primos grandes `p` y `q` utilizando un método de prueba de primalidad como el test de Miller-Rabin.
# De manera recomendaada se seleccionan números primos de 1024 bits

def generar_claves_rsa(bits=1024):
    p = generar_primo(bits)
    q = generar_primo(bits)
    n = p * q
    r = (p - 1) * (q - 1)
    e = encontrar_e(r)
    d = inverso_modular(e, r)
    
    # Valores adicionales para CRT
    dp = d % (p - 1)
    dq = d % (q - 1)
    q_inv = inverso_modular(q, p)

    return {
        'public_key': (e, n),
        'private_key': (d, n),
        'values': (p, q, dp, dq, q_inv)
    }

def generar_primo(bits):
    while True:
        candidato_primo = random.getrandbits(bits)
        if candidato_primo % 2 == 0:
            continue
        if miller_rabin.es_primo(candidato_primo):
            return candidato_primo
        
# El número debe ser 1 < e < r
def encontrar_e(r):
    e = 3 
    while mcd(e, r) != 1: # El M.C.D entre e y r debe ser 1
        e += 2
    return e

# Busca el M.C.D entre dos números a y b
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Calcular `d`, el inverso multiplicativo de `e` mod `φ(n)`
def inverso_modular(e, phi_n):
    mcd, x, _ = mcd_extendido(e, phi_n)
    if mcd != 1:
        raise Exception('El inverso modular no existe')
    else:
        return x % phi_n

# El algoritmo de Euclides extendido se puede utilizar para verificar si `e`  coprimo con `φ(n)`
def mcd_extendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mcd, x1, y1 = mcd_extendido(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return mcd, x, y
