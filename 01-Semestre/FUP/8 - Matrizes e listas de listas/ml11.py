def funcao(matriz):
    n = len(matriz)
    soma = 0
    for i in range(n):
        soma += matriz[i][n - 1 - i]
    return soma