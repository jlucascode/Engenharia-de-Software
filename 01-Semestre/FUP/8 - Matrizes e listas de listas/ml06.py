def funcao(matriz1, matriz2):
    resultado = []

    for i in range(len(matriz1)):
        linha_maiores = []
        for j in range(len(matriz1[i])):
            maior_valor = max(matriz1[i][j], matriz2[i][j])
            linha_maiores.append(maior_valor)

        resultado.append(linha_maiores)

    return resultado