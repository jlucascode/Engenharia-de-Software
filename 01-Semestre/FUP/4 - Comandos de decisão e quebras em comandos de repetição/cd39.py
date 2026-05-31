p1 = input()
p2 = input()

tamanho_minimo = len(p1)
if len(p2) < tamanho_minimo:
    tamanho_minimo = len(p2)

houve_desempate = False

for i in range(tamanho_minimo):
    if p1[i] < p2[i]:
        print(p1)
        houve_desempate = True
        break

    elif p2[i] < p1[i]:
        print(p2)
        houve_desempate = True
        break

if houve_desempate == False:
    if len(p1) < len(p2):
        print(p1)
    elif len(p2) < len(p1):
        print(p2)
    else:
        print(p1)