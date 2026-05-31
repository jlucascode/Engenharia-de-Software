nome1 = input()
nome2 = input()

nome3 = nome1 + nome2

arq1 = open(nome1, "r")
arq2 = open(nome2, "r")
arq3 = open(nome3, "w")

# copia conteúdo do primeiro
for linha in arq1:
    arq3.write(linha)

# copia conteúdo do segundo
for linha in arq2:
    arq3.write(linha)

arq1.close()
arq2.close()
arq3.close()

arq3 = open(nome3, "r")
for linha in arq3:
    print(linha, end="")
arq3.close()