def funcao(matriz):
    n = len(matriz)
    soma = 0
    for i in range(n):
        soma += matriz[i][i]
    return soma