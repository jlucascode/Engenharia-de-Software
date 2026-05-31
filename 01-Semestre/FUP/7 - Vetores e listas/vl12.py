import math

def funcao(x):
    soma = 0
    for i in range(0, len(x)):
        soma += x[i]
    y1 = soma / len(x)
    soma_quadrados = 0

    for i in range(len(x)):
        soma_quadrados += (x[i] - y1)**2
    y2 = math.sqrt(soma_quadrados / len(x))
    return y1, y2