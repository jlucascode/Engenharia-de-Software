frase = input()
frase_invertida = ""
for letra in frase:

    if letra == 'A' or letra == 'a':
        caractere_atual = '*'
    else:
        caractere_atual = letra

    frase_invertida = caractere_atual + frase_invertida
print(frase_invertida)