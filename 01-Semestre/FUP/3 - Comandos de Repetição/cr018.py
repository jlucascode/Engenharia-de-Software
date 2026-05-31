def funcao(P):
    fatorial = 1
    for i in range(1, P + 1):
        fatorial = fatorial * i

    soma_algarismos = 0
    fatorial_str = str(fatorial)

    for digito_char in fatorial_str:
        digito_int = int(digito_char)
        soma_algarismos = soma_algarismos + digito_int

    return soma_algarismos