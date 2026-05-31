nome = input("Digite o nome do arquivo: ")

arquivo = open(nome, "r")
vogais = 0
consoantes = 0

for linha in arquivo:
    for caractere in linha:
        if (caractere >= "A" and caractere <= "Z") or (caractere >= "a" and caractere <= "z"):
            if caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u" \
            or caractere == "A" or caractere == "E" or caractere == "I" or caractere == "O" or caractere == "U":
                vogais = vogais + 1
            else:
                consoantes = consoantes + 1

arquivo.close()

print("Vogais:", vogais)
print("Consoantes:", consoantes)