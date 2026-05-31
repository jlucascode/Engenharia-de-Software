def funcao(x):
    meses_por_extenso = [
        "janeiro",  # Índice 0 (Mês 1)
        "fevereiro",
        "marco",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro"  # Índice 11 (Mês 12)
    ]
    str_dia = x[0] + x[1]
    str_mes = x[3] + x[4]
    str_ano = x[6] + x[7] + x[8] + x[9]

    indice_mes = int(str_mes) - 1

    dia_sem_zero = str(int(str_dia))

    nome_do_mes = meses_por_extenso[indice_mes]

    return dia_sem_zero + ' de ' + nome_do_mes + ' de ' + str_ano