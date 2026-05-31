def funcao(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            produto = i * j
            linha.append(produto)
        matriz.append(linha)
    return matriz
