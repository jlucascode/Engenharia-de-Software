'''
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores e o quadrado da soma dos três valores.
'''
import math

valor1 = float(input())
valor2 = float(input())
valor3 = float(input())

soma_dos_quadrados = (valor1 * valor1) + (valor2 * valor2) + (valor3 * valor3)

soma_dos_valores = valor1 + valor2 + valor3
quadrado_da_soma = soma_dos_valores * soma_dos_valores

print(f"{soma_dos_quadrados:.2f}")
print(f"{quadrado_da_soma:.2f}")