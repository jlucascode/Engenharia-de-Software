def funcao(n):
    S = 0.0
    for i in range(1, n + 1):
        numerador = (i ** 2) + 1
        denominador = i + 3
        termo = numerador / denominador

        S = S + termo
    return S