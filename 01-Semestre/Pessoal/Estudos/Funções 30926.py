import math

def f(a,b,c,x):
    y = a * x**2 + b * x + c
    a = 200
    return y

def raizes_2°_grau(a, b, c):
    delta = b**2 - 4*a*c
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    return raiz1, raiz2

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: ")) 

x1,x2 = raizes_2°_grau(a,b,c)
print(f"As raízes da equação são: {x1} e {x2}")
