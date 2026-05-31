agenda = []

for i in range(5):
    desc = input('Descricao: ')
    dia = int(input('Dia: '))
    mes = int(input('Mes: '))
    ano = int(input('Ano: '))

    compromisso = {
        'compromisso': desc,
        'data': {
            'dia': dia,
            'mes': mes,
            'ano': ano
        }
    }

    agenda.append(compromisso)

while True:
    M = int(input())
    if M == 0:
        break
    A = int(input())

    filtrados = []
    for c in agenda:
        if c['data']['mes'] == M and c['data']['ano'] == A:
            filtrados.append(c)

    n = len(filtrados)
    for i in range(n):
        for j in range(i + 1, n):
            if filtrados[i]['data']['dia'] > filtrados[j]['data']['dia']:
                aux = filtrados[i]
                filtrados[i] = filtrados[j]
                filtrados[j] = aux

    for c in filtrados:
        print(c)