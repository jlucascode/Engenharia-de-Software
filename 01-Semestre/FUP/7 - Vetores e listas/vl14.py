import random
x = int(input())
random.seed(x)
vetor = []

for i in range(12):
    vetor.append(random.uniform(-10, 10))
soma = 0.0
negativo = 0

for i in vetor:
    if i > 0:
        soma+=i
    else:
        negativo+=1
print(negativo)
print(f"{soma:.2f}")