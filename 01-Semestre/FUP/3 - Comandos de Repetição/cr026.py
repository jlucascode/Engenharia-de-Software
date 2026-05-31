def funcao(x, n):
    soma_total = x
    termo_anterior = x
    for i in range(1, n + 1):
        fator_ajuste = - (x * x) / ((2 * i) * (2 * i + 1))

        termo_atual = termo_anterior * fator_ajuste

        soma_total = soma_total + termo_atual

        termo_anterior = termo_atual
    return soma_total