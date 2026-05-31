def funcao(x):
    y1 = x // 3600

    segundos_restantes = x % 3600
    y2 = segundos_restantes // 60
    y3 = segundos_restantes % 60
    return y1, y2, y3