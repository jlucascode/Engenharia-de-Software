notas = []

qtd = int(input("Qtd de alunos: "))

for i in range(qtd):
    nota = float(input(f"Nota do aluno {i + 1}: "))
    notas.append(nota)
print(notas)

soma = 0
for i in range(len(notas)):
    soma += notas[i]
media = soma / len(notas)
print(f"A média é {media:.2f}")