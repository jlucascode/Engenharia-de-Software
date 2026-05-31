def funcao(matriz):
    contador = 0
    for I in matriz:
        for J in I:
            if J > 10:
                contador += 1
    return contador