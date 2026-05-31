def funcao(data):
    dia_completo = data[0:2]
    mes_numero = data[3:5]
    ano = data[6:10]

    if dia_completo == "01":
        dia = "1"
    elif dia_completo == "02":
        dia = "2"
    elif dia_completo == "03":
        dia = "3"
    elif dia_completo == "04":
        dia = "4"
    elif dia_completo == "05":
        dia = "5"
    elif dia_completo == "06":
        dia = "6"
    elif dia_completo == "07":
        dia = "7"
    elif dia_completo == "08":
        dia = "8"
    elif dia_completo == "09":
        dia = "9"
    else:
        dia = dia_completo

    if mes_numero == "01":
        mes_extenso = "janeiro"
    elif mes_numero == "02":
        mes_extenso = "fevereiro"
    elif mes_numero == "03":
        mes_extenso = "marco"
    elif mes_numero == "04":
        mes_extenso = "abril"
    elif mes_numero == "05":
        mes_extenso = "maio"
    elif mes_numero == "06":
        mes_extenso = "junho"
    elif mes_numero == "07":
        mes_extenso = "julho"
    elif mes_numero == "08":
        mes_extenso = "agosto"
    elif mes_numero == "09":
        mes_extenso = "setembro"
    elif mes_numero == "10":
        mes_extenso = "outubro"
    elif mes_numero == "11":
        mes_extenso = "novembro"
    elif mes_numero == "12":
        mes_extenso = "dezembro"
    else:
        mes_extenso = "Mes Invalido"

    return dia + " de " + mes_extenso + " de " + ano