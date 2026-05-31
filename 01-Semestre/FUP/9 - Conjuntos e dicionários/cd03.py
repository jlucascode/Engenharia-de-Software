#Construa um dicionário com as seguintes informações de alunos: nome, número de matrícula e curso.
#Leia do usuário a informação de n alunos, armazene em um vetor e imprima os dados na tela.
n = int(input("Quantos alunos deseja cadastrar? "))
alunos = []

for i in range(n):
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite o número de matrícula: "))
    curso = input("Digite o curso: ")
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "curso": curso
    }
    alunos.append(aluno)

for aluno in alunos:
    print(aluno)