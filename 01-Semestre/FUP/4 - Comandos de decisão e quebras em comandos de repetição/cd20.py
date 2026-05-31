import math


def funcao(x):
    if x < 0:
        return False

    raiz = math.sqrt(x)

    if raiz % 1 == 0:
        return True
    else:
        return False