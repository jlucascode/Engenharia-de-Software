'''
Faça um programa que receba o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 21,37 %.
'''
import math

salario = float(input())

novo_salario = salario * 1.2137

print(f"{novo_salario:.2f}")

# Multiplicar o salário por 1.2137 já inclui o valor original mais o aumento. O 1 + 0,2137.
#Simplificando, basta somar 1 ao valor decimal da porcentagem e multiplicar o valor original por esse resultado.