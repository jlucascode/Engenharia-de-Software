import math
def funcao(x):
    y1 = x // 100
    x = x % 100
    y2 = x // 50
    x = x % 50
    y3 = x // 20
    x = x % 20
    y4 = x // 10
    x = x % 10
    y5 = x // 5
    x = x % 5
    y6 = x // 2
    x = x % 2
    y7 = x // 1
    return y1, y2, y3, y4, y5, y6, y7