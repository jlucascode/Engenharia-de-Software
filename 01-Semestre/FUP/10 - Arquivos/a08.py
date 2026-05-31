entrada_nome = input("Digite o nome do arquivo de entrada: ")
saida_nome = input("Digite o nome do arquivo de saída: ")

# abre o arquivo de entrada para leitura
entrada = open(entrada_nome, "r")

# abre o arquivo de saída para escrita
saida = open(saida_nome, "w")

for linha in entrada:
    # converte toda a linha para maiúscula
    saida.write(linha.upper())

entrada.close()
saida.close()

# mostra o conteúdo do arquivo de entrada
print("Conteúdo do arquivo de entrada:")
entrada = open(entrada_nome, "r")
for linha in entrada:
    print(linha, end="")
entrada.close()

# mostra o conteúdo do arquivo de saída
print("\nConteúdo do arquivo de saída:")
saida = open(saida_nome, "r")
for linha in saida:
    print(linha, end="")
saida.close()
