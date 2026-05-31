alunos = []

for i in range (1):
    aluno = {}
    aluno['nome'] = input ("escreva o nome do aluno: ")
    aluno['matricula'] = int(input("escreva o numero da matricula : "))#chave e valor respectivamente

    alunos.append(aluno)

disciplina = {}
disciplina ['nome'] ='fundamentos de programação'
disciplina ['professor'] = 'markos com k freitas'
disciplina ['carga_horaria'] = [32, 32, 0, 0]
disciplina ['alunos'] = alunos
print(disciplina)

disciplina2 = {'nome':'Introdução...', 'professor':'marcos vinicius', 'carga horaria': [64, 0 , 0, 0]}
