import math

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    print("Nao eh equacao do 2o grau")

else:
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("Nao existe raiz real")

    elif delta == 0:
        x1 = (-b) / (2 * a)

        print(f"{x1:.2f}")
        print("Raiz unica")

    else:
        raiz_delta = math.sqrt(delta)

        x2 = (-b - raiz_delta) / (2 * a)
        x1 = (-b + raiz_delta) / (2 * a)

        if x1 < x2:
            print(f"{x1:.2f}")
            print(f"{x2:.2f}")
        else:
            print(f"{x1:.2f}")
            print(f"{x2:.2f}")