import random


def funcao(semente, n):
    random.seed(semente)
    matriz_original = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(random.randint(1, 20))
        matriz_original.append(linha)

    matriz_transformada = [linha[:] for linha in matriz_original]

    for i in range(n):
        for j in range(i + 1, n):
            matriz_transformada[i][j] = 0

    return matriz_original, matriz_transformada
