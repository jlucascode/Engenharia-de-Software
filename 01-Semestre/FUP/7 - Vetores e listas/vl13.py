def funcao(x):
    vetor = []
    media = 0
    for n in x:
        media += n
    media /= 15
    reprovados = 0

    for n in x:
        vetor.append(float((n - media) ** 2))
        if n < 7:
            reprovados += 1
    desvio = 0
    for y in vetor:
        desvio += y
    desvio /= 15
    return media, desvio ** (1 / 2), reprovados