def funcao(matriz):
    n = len(matriz)
    soma = 0
    for i in range(n):
        for j in range(i + 1, n):
            soma += matriz[i][j]
    return soma