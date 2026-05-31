palavra_original = input()

palavra_ALTERADA = ""

for caractere in palavra_original:
    palavra_ALTERADA = palavra_ALTERADA + chr(ord(caractere) + 1)

print(palavra_ALTERADA)