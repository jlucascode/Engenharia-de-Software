def funcao(x):
    n = len(x)

    for tamanho in range(n, 1, -1):
        for i in range(n - tamanho + 1):
            for j in range(i + 1, n - tamanho + 1):
                iguais = 1
                for z in range(tamanho):
                    if x[i + z] != x[j + z]:
                        iguais = 0
                        break
                if iguais == 1:
                    return i, j, tamanho
    return -1, -1, -1