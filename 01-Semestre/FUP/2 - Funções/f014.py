def funcao(x):
    unidade = x % 10
    dezena = (x // 10) % 10
    centena = x // 100
    num_invertido = (unidade * 100) + (dezena * 10) + centena
    return num_invertido