soma = 0
for numero in range(1, 233169):
    if soma % 3 == 0 or soma % 5 == 0:
        soma += numero
print(numero)
