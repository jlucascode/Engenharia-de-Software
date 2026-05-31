def calcular_idade(dia_nasc, mes_nasc, ano_nasc, dia_hoje, mes_hoje, ano_hoje):
    idade = ano_hoje - ano_nasc
    # se ainda não fez aniversário neste ano, subtrai 1
    if (mes_hoje < mes_nasc) or (mes_hoje == mes_nasc and dia_hoje < dia_nasc):
        idade -= 1
    return idade


# programa principal
entrada_nome = input()
dia_hoje = int(input())
mes_hoje = int(input())
ano_hoje = int(input())

saida_nome = entrada_nome + ".out"

# abre arquivo de entrada
with open(entrada_nome, "r", encoding="utf-8") as entrada:
    linhas = entrada.readlines()

# cria arquivo de saída
with open(saida_nome, "w", encoding="utf-8") as saida:
    for linha in linhas:
        partes = linha.strip().split("\t")
        nome = partes[0]
        dia, mes, ano = map(int, partes[1].split())
        idade = calcular_idade(dia, mes, ano, dia_hoje, mes_hoje, ano_hoje)
        saida.write(f"{nome}\t{idade}\n")

# mostra conteúdo do arquivo de saída
with open(saida_nome, "r", encoding="utf-8") as saida:
    for linha in saida:
        print(linha, end="")