numero_de_alunos = int(input("Digite o número de alunos: "))
list.length = numero_de_alunos
nota = []

num1 = ("Digite a nota do aluno: ")
num2 = ("Digite a nota do aluno: ")
num3 = ("Digite a nota do aluno: ")

soma = num1 + num2 + num3
media = soma / 3

lista = []
for i in range(0, numero_de_alunos):
    lista.append(nota)

print("A média dos alunos é: ", media)
