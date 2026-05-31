def calcular_mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a


def funcao(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0

    mdc = calcular_mdc(num1, num2)

    mmc_resultado = (num1 * num2) // mdc

    return mmc_resultado