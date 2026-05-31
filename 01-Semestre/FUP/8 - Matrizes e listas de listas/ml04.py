def funcao(matriz):
    maior_valor = matriz[0][0]
    linha_maior = 0
    coluna_maior = 0
    total_linhas = len(matriz)
    for i in range(total_linhas):
        total_colunas = len(matriz[i])
        for j in range(total_colunas):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                linha_maior = i
                coluna_maior = j

    return maior_valor, linha_maior, coluna_maior