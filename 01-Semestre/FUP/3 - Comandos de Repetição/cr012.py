def funcao(n, k):
    if k == 0:
        return 1

    resultado = 1
    i = 1
    while i <= k:
        resultado = resultado * (n - i + 1) / i
        i = i + 1
    return int(resultado)