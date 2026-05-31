def funcao(n):
    f_n_menos_2 = 0
    f_n_menos_1 = 1
    for i in range(1, n):
        f_n = f_n_menos_1 + f_n_menos_2

        f_n_menos_2 = f_n_menos_1
        f_n_menos_1 = f_n
    return f_n_menos_1