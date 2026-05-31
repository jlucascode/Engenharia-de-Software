'''
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.
'''
import math

invest1 = float(input())
invest2 = float(input())
invest3 = float(input())

premio_total = float(input())

total_investido = invest1 + invest2 + invest3

proporcao1 = invest1 / total_investido
proporcao2 = invest2 / total_investido
proporcao3 = invest3 / total_investido

premio1 = proporcao1 * premio_total
premio2 = proporcao2 * premio_total
premio3 = proporcao3 * premio_total

print(f"{premio1:.2f}")
print(f"{premio2:.2f}")
print(f"{premio3:.2f}")
