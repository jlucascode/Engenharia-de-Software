def programa_livros():
    livros = []

    for i in range(5):
        livro = {}
        livro["titulo"] = input()
        livro["autor"] = input()
        livro["ano"] = int(input())
        livros.append(livro)

    busca = input().upper()

    encontrou = False
    for livro in livros:
        if busca in livro["titulo"].upper():
            print(livro)
            encontrou = True
programa_livros()
