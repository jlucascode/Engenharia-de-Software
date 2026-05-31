def funcao(num1, num2):
    a = num1
    b = num2

    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a