'''
Crie um dicionário representando os alunos de um determinado curso. O dicionário deve conter a matrícula do aluno, nome,
nota da primeira prova, nota da segunda prova e nota da terceira prova.
◦ Permita ao usuário entrar com os dados de 5 alunos.
◦ Encontre o aluno com maior nota da primeira prova.
◦ Encontre o aluno com maior média geral.
◦ Encontre o aluno com menor média geral.
◦ Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 7 para aprovação.
'''
alunos = []
for i in range(5):
    matricula = input()
    alunos.append(int(input(f"Digite o aluno {i}: ")))
    n1 = float(input)
    n2 = float(input)
    n3 = float(input)
    media = (n1 + n2 + n3) / 3
    aluno = {

        
    }