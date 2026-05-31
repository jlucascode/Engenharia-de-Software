def verifica_esta_contido(x,y):
    guardar = True
    for k in range(len(y)):
        if x == y[k]:
            guardar = False
            return guardar
    return guardar
y = []
nome = input()
nome = nome.replace(' ', '')
nome = nome.replace('-', '')
for l in range(len(nome)):
    if verifica_esta_contido(nome[l], y):
        y.append(nome[l])
print(len(y))