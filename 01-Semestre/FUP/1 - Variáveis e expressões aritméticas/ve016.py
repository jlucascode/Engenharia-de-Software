'''
Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua distância da origem (0, 0).
'''
import math

x = float(input())
y = float(input())

distancia = math.sqrt((x * x) + (y * y))

print(f"{distancia:.2f}")