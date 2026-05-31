entrada_nome = input()
saida_nome = entrada_nome + ".out"

entrada = open(entrada_nome, "r")

cidades = []

for linha in entrada:
    partes = linha.strip().split("\t")  # separa por tabulação
    nome = partes[0]
    habitantes = int(partes[1])
    cidades.append({"nome": nome, "habitantes": habitantes})

entrada.close()

mais_populosa = cidades[0]
for c in cidades:
    if c["habitantes"] > mais_populosa["habitantes"]:
        mais_populosa = c

saida = open(saida_nome, "w")
saida.write(mais_populosa["nome"] + "\t" + str(mais_populosa["habitantes"]) + "\n")
saida.close()

for c in cidades:
    print(c)

saida = open(saida_nome, "r")
for linha in saida:
    print(linha, end="")
saida.close()