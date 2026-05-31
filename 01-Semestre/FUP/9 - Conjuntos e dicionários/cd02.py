'''resumido
carros = {}
modelo_economico = ""
maior_consumo = -1.0

# Leitura e identificação do mais econômico em um único bloco
for _ in range(5):
    modelo = input()
    consumo = float(input())
    carros[modelo] = consumo
    if consumo > maior_consumo:
        maior_consumo = consumo
        modelo_economico = modelo

print("Carro mais economico:", modelo_economico)

# Primeiro loop de saída: Autonomia
for m in carros:
    print("Carro", m, "percorre", "{:.2f}".format(carros[m] * 50), "kms com 50 litros")

# Segundo loop de saída: Consumo 1000km
for m in carros:
    print("Carro", m, "precisa de", "{:.2f}".format(1000 / carros[m]), "litros para percorrer 1000 kms")'''
carros = {}

ordem_modelos = []

for i in range(5):
    modelo = input()
    consumo = float(input())
    carros[modelo] = consumo
    ordem_modelos.append(modelo)

modelo_economico = ""
maior_consumo = -1.0

for m in ordem_modelos:
    if carros[m] > maior_consumo:
        maior_consumo = carros[m]
        modelo_economico = m

print("Carro mais economico:", modelo_economico)

for m in ordem_modelos:
    autonomia = carros[m] * 50

    print("Carro", m, "percorre", "{:.2f}".format(autonomia), "kms com 50 litros")

for m in ordem_modelos:
    litros_necessarios = 1000 / carros[m]
    print("Carro", m, "precisa de", "{:.2f}".format(litros_necessarios), "litros para percorrer 1000 kms")

#Faça um programa que preencha as informações dos modelos de cinco carros (exemplos de modelos: Fusca, Gol, Vectra, etc.)
# juntamente com o consumo desses carros, isto é, quantos quilômetros cada um deles faz com um litro de combustível. Calcule e mostre:
#◦ O modelo de carro mais econômico;
#◦ Quantos quilômetros cada um dos carros cadastrados percorre com 50 litros de combustível;
#◦ Quantos litros de combustível cada um dos carros cadastrados consomem para percorrer uma distância de 1.000 quilômetros.