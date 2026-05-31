def funcao(matriz, k):
    n = len(matriz)
    maior_produto = -1
    melhor_linha = 0
    melhor_coluna = 0
    melhor_direcao = ""

    direcoes = [
        (0, 1, "direita"),
        (0, -1, "esquerda"),
        (1, 0, "baixo"),
        (-1, 0, "cima"),
        (-1, 1, "direita cima"),
        (-1, -1, "esquerda cima"),
        (1, 1, "direita baixo"),
        (1, -1, "esquerda baixo")
    ]

    for r in range(n):
        for c in range(n):
            for dr, dc, nome_dir in direcoes:

                fim_r = r + (k - 1) * dr
                fim_c = c + (k - 1) * dc

                if 0 <= fim_r < n and 0 <= fim_c < n:
                    produto_atual = 1
                    for i in range(k):
                        produto_atual *= matriz[r + i * dr][c + i * dc]

                    if produto_atual > maior_produto:
                        maior_produto = produto_atual
                        melhor_linha = r
                        melhor_coluna = c
                        melhor_direcao = nome_dir

    return maior_produto, melhor_linha, melhor_coluna, melhor_direcao
