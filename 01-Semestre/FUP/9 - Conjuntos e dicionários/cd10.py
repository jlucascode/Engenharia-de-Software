def programa_agenda():
    agenda = []

    for i in range(5):
        pessoa = {}

        pessoa["nome"] = input()
        pessoa["endereco"] = input()
        pessoa["telefone"] = input()

        agenda.append(pessoa)

    n = len(agenda)
    for i in range(n):
        for j in range(0, n - i - 1):
            if agenda[j]["nome"] > agenda[j + 1]["nome"]:
                aux = agenda[j]
                agenda[j] = agenda[j + 1]
                agenda[j + 1] = aux

    for i in range(len(agenda)):
        print(agenda[i])


programa_agenda()