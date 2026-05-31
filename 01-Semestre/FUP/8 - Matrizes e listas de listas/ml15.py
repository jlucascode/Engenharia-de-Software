def funcao(A, B):
    p = len(A)
    q = len(A[0])
    r = len(B[0])

    C = []
    for i in range(p):
        linha_vazia = [0] * r
        C.append(linha_vazia)

    for i in range(p):
        for j in range(r):
            soma_produto = 0
            for k in range(q):
                soma_produto += A[i][k] * B[k][j]

            C[i][j] = soma_produto
    return C