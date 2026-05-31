'''
Leia um valor inteiro positivo em segundos, e imprima-o em horas, minutos e segundos.
'''
import math
segundos_total = int(input())

horas = segundos_total // 3600

segundos_restantes = segundos_total % 3600

minutos = segundos_restantes // 60

segundos = segundos_restantes % 60

print(horas)
print(minutos)
print(segundos)