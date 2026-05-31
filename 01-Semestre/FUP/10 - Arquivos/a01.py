# Escrita
arquivo = open("arq.txt", "w")
while True:
    linha = input()
    if linha == "0":
        break
    arquivo.write(linha + "\n")
arquivo.close()

# Leitura
arquivo = open("arq.txt", "r")
for linha in arquivo:
    print(linha, end="")
arquivo.close()
