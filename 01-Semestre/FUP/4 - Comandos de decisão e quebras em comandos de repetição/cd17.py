import math  # para math.sqrt

while True:
    numero = float(input())

    if numero <= 0:
        break

    quadrado = numero ** 2
    cubo = numero ** 3
    raiz_quadrada = math.sqrt(numero)

    print(f"{quadrado:.2f}")
    print(f"{cubo:.2f}")
    print(f"{raiz_quadrada:.2f}")