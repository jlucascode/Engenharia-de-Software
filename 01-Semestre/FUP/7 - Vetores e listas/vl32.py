def alu_pes(a, nomes):
    result = []
    for i in range(len(nomes)):
        if nomes[i].find(a) != -1:
            result.append(nomes[i])
            result.append(i)

    return result

nomes= []
nomes.append(input("Aluno: "))
for i in range(4):
    seguir = input("Deseja inserir novo aluno? [S/N] ")
    if seguir.upper() == "N":
        break
    nomes.append(input("Aluno: "))
pesquisa = input("Aluno para pesquisa: ")

result = alu_pes(pesquisa, nomes)
for _ in range(len(result)):
    print(result[_])