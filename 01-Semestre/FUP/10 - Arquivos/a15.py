def calcular_idade(dia_nasc, mes_nasc, ano_nasc, dia_hoje, mes_hoje, ano_hoje):
    idade = ano_hoje - ano_nasc
    # se ainda não fez aniversário neste ano, subtrai 1
    if (mes_hoje < mes_nasc) or (mes_hoje == mes_nasc and dia_hoje < dia_nasc):
        idade -= 1
    return idade


# programa principal
entrada_nome = input("Digite o nome do arquivo de entrada: ")
dia_hoje = int(input("Digite o dia de hoje: "))
mes_hoje = int(input("Digite o mês de hoje: "))
ano_hoje = int(input("Digite o ano de hoje: "))

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

        # determina maioridade
        if idade < 18:
            status = "menor de idade"
        elif idade > 18:
            status = "maior de idade"
        else:
            status = "entrando na maioridade"

        saida.write(f"{nome}\t{idade}\t{status}\n")

# mostra conteúdo do arquivo de saída
with open(saida_nome, "r", encoding="utf-8") as saida:
    for linha in saida:
        print(linha, end="")