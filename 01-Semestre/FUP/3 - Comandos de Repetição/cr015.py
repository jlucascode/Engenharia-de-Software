def funcao(n):
    somaE = 1.0
    fatorial = 1

    for i in range(1, n + 1):
        fatorial = fatorial * i
        termo = 1.0 / fatorial
        somaE = somaE + termo

    return somaE