contador = 1
maior = 0
menor = 0
primeiro = 1
Numero = int(input())
while contador < Numero:
    numero = float(input())
    if primeiro == 1:
        menor = numero
        maior = numero
        primeiro = 0

    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
        contador += 1
if primeiro == 0:
    print(f"{menor:.2f}")
    print(f"{maior:.2f}")
else:
    print()