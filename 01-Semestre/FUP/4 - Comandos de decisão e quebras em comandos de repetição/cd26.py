numero = int(input())

maior = numero
menor = numero

for i in range(9):
    numero = float(input())

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f"{menor:.2f}")
print(f"{maior:.2f}")