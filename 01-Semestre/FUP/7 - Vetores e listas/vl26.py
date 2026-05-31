def funcao(x,y):
    diferenca = []
    for i in range(len(x)):
        guardar = True
        for j in range(len(y)):
            if x[i] == y[j]:
                guardar = False
        if guardar:
            for k in range(len(diferenca)):
                if x[i] == diferenca[k]:
                    guardar = False
                    break
            if guardar:
                diferenca.append(x[i])
    return diferenca