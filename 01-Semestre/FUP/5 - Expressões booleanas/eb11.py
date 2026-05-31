def funcao(cadeia_data):
    dia = 0
    mes = 0
    ano = 0

    if len(cadeia_data) != 10:
        return dia, mes, ano

    if cadeia_data[2] != '/' or cadeia_data[5] != '/':
        return dia, mes, ano
    str_dia = cadeia_data[0] + cadeia_data[1]
    str_mes = cadeia_data[3] + cadeia_data[4]
    str_ano = cadeia_data[6] + cadeia_data[7] + cadeia_data[8] + cadeia_data[9]

    digitos = "0123456789"

    def eh_numerico_manual(sub_string):
        for char in sub_string:
            encontrou_digito = False
            for d in digitos:
                if char == d:
                    encontrou_digito = True
                    break

            if not encontrou_digito:
                return False
        return True

    if not eh_numerico_manual(str_dia) or \
            not eh_numerico_manual(str_mes) or \
            not eh_numerico_manual(str_ano):
        return dia, mes, ano

    dia = int(str_dia)
    mes = int(str_mes)
    ano = int(str_ano)

    return dia, mes, ano