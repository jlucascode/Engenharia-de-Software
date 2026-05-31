def simplificar(num, den):
    a = num
    b = den

    if b > a:
        temp = a
        a = b
        b = temp

    while b != 0:
        resto = a % b

        a = b
        b = resto

    mdc = a

    novo_num = num // mdc
    novo_den = den // mdc

    return novo_num, novo_den