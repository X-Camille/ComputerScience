# Test de Miller-Rabin

# Dado un número primo q y un valor 2 < a < n-2, se determina si el número es posiblemente primo o compuesto.

# Retorna True si el número es posiblemente primo.

def es_primo(n):
    # Casos especiales
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Factorizar (n-1) como 2^k * m
    k = 0
    m = n - 1
    while m % 2 == 0:
        m //= 2
        k += 1

    # Bases deterministas para números menores a 3.825.123
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in bases:
        if a >= n:
            continue

        b_0 = pow(a, m, n)

        if b_0 == 1 or b_0 == n - 1:
            continue

        compuesto = True
        for _ in range(k - 1):
            b_0 = pow(b_0, 2, n)
            if b_0 == n - 1:
                compuesto = False
                break
            elif b_0 == 1:
                return False

        if compuesto:
            return False

    return True
