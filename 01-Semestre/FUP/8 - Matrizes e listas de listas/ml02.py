def function(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz.append(linha)

    for i in range(n):
        matriz[i][i] = 1

    return matriz
