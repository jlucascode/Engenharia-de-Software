def imprime_aluno(aluno):
    print(f'Nome: {aluno['nome']}')
    print(f'Matricula: {aluno['matricula']}')
    print(f"Notas: {notas}")
  

def imprime_alunos(alunos):
    for i in range(len(alunos)):
        print(f"Aluno {i + 1}:")
        imprime_aluno(alunos[i], notas[i])

def imprime_disciplinas(disciplinas):
    print(f"nome da disciplina: {disciplina['nome']}")
    print(f"professor: {disciplina['professor']}")
    print(f"carga horaria: {disciplina['carga_horaria'][0]}")

def calcular_media(disciplina):
    qtd = len(disciplina['notas'])
    soma = 0
    for i in range(qtd):
        soma += disciplina['notas'][i]
    media = soma / qtd
    return media 


def imprime_disciplinas(disciplinas):
    for i in range(len(disciplinas)):
        disciplina = disciplinas[i]
        imprime_disciplinas(disciplina)
        print()



alunos = {}

aluno = []
aluno ['nome'] = 'lucas'
aluno ['matricula'] = 1234567
alunos.append(aluno)

disciplina = {}
disciplina ['nome'] ='fundamentos de programação'
disciplina ['professor'] = 'markos com k freitas'
disciplina ['carga_horaria'] = [32, 32, 0, 0]
disciplina ['alunos'] = alunos
disciplinas.append(disciplina)