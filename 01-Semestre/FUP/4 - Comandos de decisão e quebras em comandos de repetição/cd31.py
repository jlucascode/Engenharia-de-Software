num1 = int(input())
num2 = int(input())

soma_pares = 0
multiplicacao_impares = 1

if num1 < num2:
    inicio = num1
    fim = num2
else:
    inicio = num2
    fim = num1

for numero in range(inicio, fim + 1):

    if numero % 2 == 0:
        soma_pares = soma_pares + numero
    else:
        multiplicacao_impares = multiplicacao_impares * numero

print(soma_pares)
print(multiplicacao_impares)