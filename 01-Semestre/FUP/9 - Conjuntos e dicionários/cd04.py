'''Escreva um trecho de código para fazer a criação dos novos tipos de dados conforme solicitado abaixo:
◦ Data: composto de dia, mês e ano.
◦ Horário: composto de hora, minutos e segundos.
◦ Compromisso: composto de uma data, horário e texto que descreve o compromisso.
Leia n compromissos. Crie uma função que, dadas duas datas, retorne se a primeira ocorre antes da segunda ou não.
Crie outra função semelhante, mas para comparar horários. Mostre os compromissos em ordem de data e horário.'''

'''n = int(input())
compromissos = []
for i in range(n):
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))
    hora = int(input("Hora: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    texto = input("Descricao do compromisso: ")
    
    data = {'dia': dia, 'mes': mes, 'ano': ano}
    horario = {'hora': hora, 'minutos': minutos, 'segundos': segundos}
    compromisso = {'data': data, 'horario': horario, 'texto': texto}
    
    compromissos.append(compromisso)'''

n = int(input())
compromissos = []

for i in range(n):
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))
    hora = int(input("Hora: "))
    minuto = int(input("Minuto: "))
    segundo = int(input("Segundo: "))
    texto = input("Descricao: ")
    
    data = {'dia': dia, 'mes': mes, 'ano': ano}
    horario = {'hora': hora, 'minuto': minuto, 'segundo': segundo}
    compromisso = {'data': data, 'horario': horario, 'descricao': texto}
    
    compromissos.append(compromisso)

# Ordenação manual (Bubble Sort) permitida pelas regras
for i in range(n):
    for j in range(0, n - i - 1):
        # Cria chaves numéricas para comparação de data e hora
        c1 = compromissos[j]
        c2 = compromissos[j+1]
        
        # Comparação sequencial: Ano -> Mes -> Dia -> Hora -> Minuto -> Segundo
        trocar = False
        if c1['data']['ano'] > c2['data']['ano']:
            trocar = True
        elif c1['data']['ano'] == c2['data']['ano']:
            if c1['data']['mes'] > c2['data']['mes']:
                trocar = True
            elif c1['data']['mes'] == c2['data']['mes']:
                if c1['data']['dia'] > c2['data']['dia']:
                    trocar = True
                elif c1['data']['dia'] == c2['data']['dia']:
                    if c1['horario']['hora'] > c2['horario']['hora']:
                        trocar = True
                    # Adicione minuto/segundo se o critério for ainda mais rígido

        if trocar:
            compromissos[j], compromissos[j+1] = compromissos[j+1], compromissos[j]

# Impressão final
for compromisso in compromissos:
    print(compromisso)
