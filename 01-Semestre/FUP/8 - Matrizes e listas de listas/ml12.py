def funcao(matriz):
    m = len(matriz)
    n = len(matriz[0])
    transposta = []
    for i in range(n):
        linha_vazia = [0] * m
        transposta.append(linha_vazia)

    for i in range(m):
        for j in range(n):
            transposta[j][i] = matriz[i][j]

    return transposta
