def ler_contatos(nome_arquivo):
    contatos = []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("\t")
            if len(partes) == 2:
                nome, telefone = partes
                contatos.append({"nome": nome, "telefone": telefone})

    # ordena pelo nome
    contatos.sort(key=lambda c: c["nome"])
    return contatos


# programa principal
entrada = input("Digite o nome do arquivo: ")
contatos = ler_contatos(entrada)

for c in contatos:
    print(c)