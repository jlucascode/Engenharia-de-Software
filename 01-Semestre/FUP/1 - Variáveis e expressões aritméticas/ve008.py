'''
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6 , sendo K a velocidade em km/h e M em m/s.
'''
import math

K = float(input())

M = K / 3.6

print(f"{M:.2f}")