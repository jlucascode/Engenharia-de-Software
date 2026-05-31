vet = []
impar = []
cont = 0
for i in range(15):
    ENT = int(input())
    vet.append(ENT)

    if ENT %2 !=0:
        impar.append(ENT)
        cont +=ENT
print(cont)
for p in impar:
    print(p)