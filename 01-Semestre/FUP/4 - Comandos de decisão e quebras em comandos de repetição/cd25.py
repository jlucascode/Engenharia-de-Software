soma = 0
contador = 0

while contador < 10:
    numero_lido = int(input())

    if numero_lido > 0:

        soma = soma + numero_lido
        contador = contador + 1

media = soma / 10
print(f"{media:.1f}")