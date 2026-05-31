#Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto aparece dentro do arquivo.
#Letras maiúsculas e minúsculas devem ser contadas juntas, e não separadamente.
nome = input()

arquivo = open(nome, "r")
contagem = {}

for linha in arquivo:
    for caractere in linha:
        if (caractere >= "A" and caractere <= "Z") or (caractere >= "a" and caractere <= "z"):
            letra = caractere.lower()
            if letra in contagem:
                contagem[letra] = contagem[letra] + 1
            else:
                contagem[letra] = 1

arquivo.close()

for codigo in range(ord("a"), ord("z") + 1):
    letra = chr(codigo)
    if letra in contagem:
        print(letra + ":", contagem[letra])
    else:
        print(letra + ":", 0)