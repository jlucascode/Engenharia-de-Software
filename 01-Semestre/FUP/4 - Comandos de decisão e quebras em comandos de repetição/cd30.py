N = int(input())
numero_lido = int(input())

maior = numero_lido
contador_maior = 1

for i in range(1, N):

    numero_lido = int(input())

    if numero_lido > maior:
        maior = numero_lido
        contador_maior = 1

    elif numero_lido == maior:
        contador_maior = contador_maior + 1

print(maior)
print(contador_maior)