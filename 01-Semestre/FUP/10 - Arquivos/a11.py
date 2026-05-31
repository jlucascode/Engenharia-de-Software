def funcao(nome_arquivo, palavra):
    arquivo = open(nome_arquivo, "r")
    texto = arquivo.read()
    arquivo.close()

    t = texto.lower()
    p = palavra.lower()

    contador = 0
    i = 0
    while True:
        j = t.find(p, i)
        if j == -1:
            break
        contador += 1
        i = j + 1

    return contador