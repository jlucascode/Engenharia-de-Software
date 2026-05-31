eletrodomesticos = []
for i in range(5):
    nome = input()
    potencia = float(input())
    tempo = float(input())

    eletrodomesticos.append({
        'nome': nome,
        'potencia': potencia,
        'tempo': tempo
    })

t = int(input())

consumo_total = 0
for e in eletrodomesticos:
    consumo = e['potencia'] * e['tempo'] * t
    consumo_total = consumo_total + consumo

print(f"{consumo_total:.2f}")
for e in eletrodomesticos:
    consumo = e['potencia'] * e['tempo'] * t
    percentual = (consumo / consumo_total) * 100
    print(f"{e['nome']}: {percentual:.2f}")

'''
eletrodomesticos = []
for i in range(5):
    nome = input()[:23]
    potencia = float(input())
    tempo_ativo = float(input())

    eletrodomesticos.append({
        'nome': nome,
        'potencia': potencia,
        'tempo': tempo_ativo
    })

t_dias = float(input())

consumos_individuais = []
consumo_total_casa = 0

for aparelho in eletrodomesticos:
    consumo = aparelho['potencia'] * aparelho['tempo'] * t_dias
    consumos_individuais.append(consumo)
    consumo_total_casa += consumo

print(f"{consumo_total_casa:.2f}")

for i in range(5):
    nome = eletrodomesticos[i]['nome']
    if consumo_total_casa > 0:
        relativo = (consumos_individuais[i] / consumo_total_casa) * 100
    else:
        relativo = 0
    print(f"{nome}: {relativo:.2f}")
'''