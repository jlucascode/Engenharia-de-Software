vetor = []
pares = []
cont = 0
for i in range(15):
    ENT = int(input())
    vetor.append(ENT)

    if ENT %2 ==0:
        pares.append(ENT)
        cont +=1
print(cont)
for p in pares:
    print(p)