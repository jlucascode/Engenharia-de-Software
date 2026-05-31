vet = []
vet.append(int(input()))
maior = vet[0]
menor = vet[0]
for i in range(1, 10):
    vet.append(int(input()))
    if vet[i] > maior:
        maior = vet[i]
    if vet[i] < menor:
        menor = vet[i]

print(maior)
print(menor)