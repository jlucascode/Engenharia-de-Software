nome = input()

entrada = open(nome, "r")

saida_nome = nome + ".out"

saida = open(saida_nome, "w")

for linha in entrada:
    nova_linha = ""
    for caractere in linha:
        if caractere in "aeiouAEIOU":
            nova_linha = nova_linha + "*"
        else:
            nova_linha = nova_linha + caractere
    saida.write(nova_linha)

entrada.close()
saida.close()

saida = open(saida_nome, "r")
for linha in saida:
    print(linha, end="")
saida.close()