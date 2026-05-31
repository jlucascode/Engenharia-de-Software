def verifica_esta_contido(x,y):
    deposito = True
    for k in range(len(y)):
        if x == y[k]:
            deposito = False
            return deposito
    return deposito
def funcao(x,y):
    uni = []
    for i in range(len(x)):
        if verifica_esta_contido(x[i], uni):
            uni.append(x[i])
    for j in range(len(y)):
        if verifica_esta_contido(y[j], uni):
            uni.append(y[j])
    return uni