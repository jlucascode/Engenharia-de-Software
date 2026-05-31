def funcao(n):
    for i in range(1, n + 1):
        numespaçamento = n - i
        espacos = " " * numespaçamento

        num_estrelas = 2 * i - 1
        estrelas = "*" * num_estrelas
        print(espacos + estrelas)