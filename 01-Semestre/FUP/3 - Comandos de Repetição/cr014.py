def funcao(n):
    soma_harmonica = 0.0
    for i in range(1, n + 1):
        termo = 1.0 / i
        soma_harmonica = soma_harmonica + termo

    return soma_harmonica