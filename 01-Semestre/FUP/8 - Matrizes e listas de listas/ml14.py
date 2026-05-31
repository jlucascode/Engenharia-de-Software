def funcao(A, B):
    linhas = len(A)
    colunas = len(A[0])
    C = []
    for i in range(linhas):
        linha_vazia = [0] * colunas
        C.append(linha_vazia)

    for i in range(linhas):
        for j in range(colunas):
            C[i][j] = A[i][j] + B[i][j]

    return C