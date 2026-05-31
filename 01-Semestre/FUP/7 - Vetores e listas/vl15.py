vetor = []
for i in range(10):
    numero = int(input())
    vetor.append(numero)

for A in range(len(vetor)):
    for B in range(A + 1, len(vetor)):
        if vetor[A] == vetor[B]:
            print(vetor[A])