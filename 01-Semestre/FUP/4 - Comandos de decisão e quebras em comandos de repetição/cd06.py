soma = 0

for i in range(3):
    numero = float(input())

    if numero > 10:
        print("Nota invalida")
        break
    elif numero < 0:
        print("Nota invalida")
        break
    else:
        soma = soma + numero
else:
    media = soma / 3

    print(f"{media:.2f}")