def funcao(matriz, valor_procurado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_procurado:
                return i, j
    return -1, -1