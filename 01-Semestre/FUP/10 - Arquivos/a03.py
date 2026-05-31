#Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais.
nome = input("Digite o nome do arquivo: ")
arquivo = open(nome, "r")
contador = 0
for linha in arquivo:
    for caractere in linha:
        if caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u" \
        or caractere == "A" or caractere == "E" or caractere == "I" or caractere == "O" or caractere == "U":
            contador = contador + 1
arquivo.close()
print("O arquivo possui", contador, "vogais")