import math

alunos = 5

notas = []

for i in range(0, alunos):
    nota = float(input(f"Escreva a nota do aluno {i+1}: "))
    notas.append(nota)
print(notas)

soma = 0
for i in range(0, len(notas)):
    soma += notas[i]
media = soma/len(notas)
print(media)

soma = 0
for i in range(0, len(notas)):
    soma += (notas[i] - media)**2
dp = math.sqrt(soma)/len(notas)
print(dp)