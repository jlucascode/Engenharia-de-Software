def analisar_arquivo(nome_arquivo):
    import re

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    # número de caracteres
    num_caracteres = len(texto)

    # número de linhas = número de '\n'
    num_linhas = texto.count("\n")

    # número de palavras (espaço, tabulação ou nova linha)
    palavras = re.split(r"[ \t\n]+", texto.strip())
    num_palavras = 0 if texto.strip() == "" else len(palavras)

    # contagem de letras (apenas a–z, ignorando acentos)
    contagem_letras = [0] * 26
    for c in texto:
        if c.isalpha():
            c = c.lower()
            if "a" <= c <= "z":
                contagem_letras[ord(c) - ord("a")] += 1

    print(num_caracteres)
    print(num_linhas)
    print(num_palavras)
    for i in range(26):
        letra = chr(ord("a") + i)
        print(f"{letra}: {contagem_letras[i]}")


# chamada esperada pelo avaliador
entrada = input("")
analisar_arquivo(entrada)
'''ou
def analisar_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    num_caracteres = len(texto)

    num_linhas = texto.count("\n")

    num_palavras = 0
    dentro_palavra = False
    for c in texto:
        if c == " " or c == "\t" or c == "\n":
            if dentro_palavra:
                num_palavras += 1
                dentro_palavra = False
        else:
            dentro_palavra = True
    if dentro_palavra:  # última palavra
        num_palavras += 1

    # contagem de letras (apenas a–z, ignorando acentos)
    contagem_letras = [0] * 26
    for c in texto:
        if c.isalpha():
            c = c.lower()
            if "a" <= c <= "z":
                contagem_letras[ord(c) - ord("a")] += 1

    # saída
    print(num_caracteres)
    print(num_linhas)
    print(num_palavras)
    for i in range(26):
        letra = chr(ord("a") + i)
        print(f"{letra}: {contagem_letras[i]}")

entrada = input("")
analisar_arquivo(entrada)
'''