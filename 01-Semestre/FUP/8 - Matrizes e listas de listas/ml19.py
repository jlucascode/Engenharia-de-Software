import random


def funcao(m, n, semente, inicio, fim):
    random.seed(semente)
    matriz = []
    for i in range(m):
        linha = [random.randint(inicio, fim) for _ in range(n)]
        matriz.append(linha)

    vetor = [0] * m
    for i in range(m):
        if i % 2 == 0:
            soma = sum(matriz[i])
            vetor[i] = soma / n
        else:
            contador = 0
            for x in matriz[i]:
                if x < 0 and x % 3 == 0:
                    contador += 1
            vetor[i] = contador

    return matriz, vetor
