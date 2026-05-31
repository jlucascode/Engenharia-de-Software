def verifica_esta_contido(x,y):
    guardar = True
    for k in range(len(y)):
        if x == y[k]:
            guardar = False
            return guardar
    return guardar
y = []
while True:
    x = int(input())
    if verifica_esta_contido(x, y):
        y.append(x)
    else:
        print(f"Numero {x} ja existe, escreva outro")
    if len(y) == 12:
        break
print(y)