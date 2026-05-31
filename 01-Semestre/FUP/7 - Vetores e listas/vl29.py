def funcao(x):
    while True:
        acabou = True
        for i in range(len(x)-1):
            if x[i] < x[i+1]:
                acabou = False
                aux = x[i]
                x[i] = x[i+1]
                x[i+1] = aux
        if acabou:
            break
    return x