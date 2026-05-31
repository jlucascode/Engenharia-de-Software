frase = input()

contador_brancos = 0

for caractere in frase:
    if caractere == ' ':
        contador_brancos = contador_brancos + 1

print(contador_brancos)