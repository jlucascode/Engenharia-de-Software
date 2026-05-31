def funcao(matriz):
    n = len(matriz)
    soma = 0
    for i in range(n):
        for j in range(i):
            soma += matriz[i][j]
    return soma
