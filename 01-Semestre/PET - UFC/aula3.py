numero_de_alunos = int(input("Digite o número de alunos: "))
numero_de_alunos = 0
try:
	numero_de_alunos = int(input("Digite o número de alunos: "))
except ValueError:
	print("Número de alunos inválido. Use um inteiro.")
	raise SystemExit(1)

if numero_de_alunos <= 0:
	print("Nenhum aluno para processar.")
	raise SystemExit(0)

medias_alunos = []

for i in range(1, numero_de_alunos + 1):
	print(f"\nAluno {i}:")
	notas = []
	for j in range(1, 4):
		while True:
			entrada = input(f"  Digite a nota {j}: ")
			try:
				nota = float(entrada.replace(',', '.'))
				notas.append(nota)
				break
			except ValueError:
				print("  Nota inválida. Digite um número (ex: 7.5). Tente novamente.")

	media_aluno = sum(notas) / 3
	medias_alunos.append(media_aluno)
	print(f"  Média do aluno {i}: {media_aluno:.2f}")

media_turma = sum(medias_alunos) / len(medias_alunos)
print(f"\nA média da turma é: {media_turma:.2f}")