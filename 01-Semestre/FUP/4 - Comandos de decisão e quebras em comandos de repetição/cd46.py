entrada = input()

maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
frase_limpa = ""

for char in entrada:

    letra_adicionada = False

    for i in range(len(maiusculas)):
        if char == maiusculas[i]:
            frase_limpa = frase_limpa + char
            letra_adicionada = True
            break

    if letra_adicionada == False:
        for i in range(len(minusculas)):
            if char == minusculas[i]:
                frase_limpa = frase_limpa + maiusculas[i]
                break

frase_invertida = ""
for char in frase_limpa:
    frase_invertida = char + frase_invertida

if frase_limpa == frase_invertida:
    print(True)
else:
    print(False)