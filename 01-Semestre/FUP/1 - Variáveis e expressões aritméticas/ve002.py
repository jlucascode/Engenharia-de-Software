'''
Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via teclado, calcule a área e o perímetro deste retângulo.
'''
import math

lado1 = float(input())
lado2 = float(input())

area = lado1 * lado2

perimetro = 2 * (lado1 + lado2)

print(f"{area:.2f}")
print(f"{perimetro:.2f}")