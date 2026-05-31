def funcao(n):
    result_final = 1
    result_parcial = 1

    for i in range(2, n + 1):
        result_parcial = i ** result_parcial

        result_final = result_parcial

    return result_final