#Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo possui.
nome = input()
arquivo = open(nome, "r")
contador = 0
for linha in arquivo:
    contador = contador + 1
arquivo.close()

print(contador)