'''
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido. Exemplo: Número Lido = 123, Número Gerado = 321. Não utilize strings.
'''
import math

numero = int(input())

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

novo_numero = (unidade * 100) + (dezena * 10) + centena

print(novo_numero)
#Isolar o primeiro dígito(centena): Usa-se divisão inteira por 100 (// 100).Ex: 123 // 100 resulta em 1.