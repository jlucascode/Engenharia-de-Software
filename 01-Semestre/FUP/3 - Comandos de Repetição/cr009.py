def funcao(N):
    soma_total = 0

    for i in range(0, 2 * N, 2):
        soma_total = soma_total + i
    return soma_total