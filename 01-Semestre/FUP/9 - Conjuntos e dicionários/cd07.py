def programa_estudantes():
    entrada_n = input()
    if entrada_n == "":
        return
    n = int(entrada_n)

    turma = []

    for i in range(n):
        aluno = {}

        aluno["matricula"] = int(input())
        aluno["nome"] = input()
        aluno["codigo"] = input()

        n1 = float(input())
        n2 = float(input())

        aluno["nota1"] = n1
        aluno["nota2"] = n2

        media = (n1 * 1.0 + n2 * 2.0) / 3.0
        aluno["media"] = media

        turma.append(aluno)

    for i in range(len(turma)):
        print(turma[i])


programa_estudantes()