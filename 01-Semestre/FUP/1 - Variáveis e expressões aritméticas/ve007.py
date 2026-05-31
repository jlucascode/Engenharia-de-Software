'''
Faça um programa que leia a temperatura em graus Celsius e converta para Fahrenheit. Fórmula: F = C * (9.0/5.0) + 32.
'''
import math

celsius = float(input())

fahrenheit = celsius * (9.0/5.0) + 32

print(f"{fahrenheit:.2f}")