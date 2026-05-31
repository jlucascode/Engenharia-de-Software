numero = int(input())

maior = numero
menor = numero

while numero >= 0:

    if numero > maior:
        maior = numero

    elif numero < menor:
        menor = numero

    numero = int(input())

if maior >= 0:
    print(maior)
    print(menor)