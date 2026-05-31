palavra_original = input()
caractere_substituto = input()

contador_vogais = 0
nova_palavra = ""

for letra in palavra_original:
    eh_vogal = (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or
                letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U')

    if eh_vogal:
        contador_vogais = contador_vogais + 1
        nova_palavra = nova_palavra + caractere_substituto
    else:
        nova_palavra = nova_palavra + letra
print(contador_vogais)
print(nova_palavra)