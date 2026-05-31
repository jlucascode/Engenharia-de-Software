for numero in range(1000, 10000):

    A = numero // 100
    B = numero % 100

    soma = A + B
    soma_ao_quadrado = soma * soma

    if soma_ao_quadrado == numero:

        print(numero)