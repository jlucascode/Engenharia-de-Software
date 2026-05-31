TAMANHO = 70
vetor = []
for i in range(TAMANHO):
    valor = (6 * i) % (i + 1)
    vetor.append(valor)
print(vetor)
