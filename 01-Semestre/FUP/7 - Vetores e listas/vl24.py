def funcao(x,y):
    interseccao = []
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                guardar = True
                for k in range(len(interseccao)):
                    if x[i] == interseccao[k]:
                        guardar = False
                        break
                if guardar:
                    interseccao.append(x[i])
    return interseccao