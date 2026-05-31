import math
numero = float(input())

if numero > 0:
    raiz = math.sqrt(numero)
    print(f"{raiz:.2f}")
elif numero <= 0:
    print("Numero invalido")