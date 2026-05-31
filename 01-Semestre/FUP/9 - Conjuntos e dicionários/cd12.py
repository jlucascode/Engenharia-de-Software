def filtrar_alunos():
    turma_total = []

    for i in range(10):
        aluno = {}
        aluno["nome"] = input()
        aluno["matricula"] = int(input())
        aluno["media"] = float(input())

        turma_total.append(aluno)

    aprovados = []
    reprovados = []

    for i in range(len(turma_total)):
        aluno_atual = turma_total[i]

        if aluno_atual["media"] >= 5.0:
            aprovados.append(aluno_atual)
        else:
            reprovados.append(aluno_atual)

    for i in range(len(aprovados)):
        print(aprovados[i])

    for i in range(len(reprovados)):
        print(reprovados[i])


filtrar_alunos()