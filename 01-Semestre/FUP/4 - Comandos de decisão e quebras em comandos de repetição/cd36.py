def funcao(numero):
    if numero <= 1:
        if numero == 1:
            return 1
        else:
            return 0
    maior_fator_primo = 1

    while numero % 2 == 0:
        maior_fator_primo = 2
        numero = int(numero / 2)

    i = 3

    while i * i <= numero:

        while numero % i == 0:
            maior_fator_primo = i
            numero = int(numero / i)

        i = i + 2

    if numero > 2:
        maior_fator_primo = numero
    return int(maior_fator_primo)