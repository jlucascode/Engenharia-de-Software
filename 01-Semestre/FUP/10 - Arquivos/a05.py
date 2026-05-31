#Faça um programa que receba do usuário um arquivo texto e um caractere.
#Mostre na tela quantas vezes aquele caractere ocorre dentro do arquivo.
nome = input('Digite o nome do arquivo: ')
caractere = input('Digite uma caractere: ')

arquivo = open(nome, 'r')
contador = 0

for linha in arquivo:
    for c in linha:
        if c == caractere:
            contador = contador + 1

arquivo.close()

print(contador)
