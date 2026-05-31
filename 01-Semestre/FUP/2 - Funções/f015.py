def funcao(x):
    milhar = x // 1000
    centena = (x // 100) % 10
    dezena = (x // 10) % 10
    unidade = x % 10
    return milhar, centena, dezena, unidade
