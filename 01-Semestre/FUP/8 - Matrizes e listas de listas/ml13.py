def funcao(matriz):
    total_linhas = len(matriz)
    total_colunas = len(matriz[0])

    vetor_somas = [0] * total_colunas

    for j in range(total_colunas):
        soma_atual = 0
        for i in range(total_linhas):
            soma_atual += matriz[i][j]

        vetor_somas[j] = soma_atual

    return vetor_somas