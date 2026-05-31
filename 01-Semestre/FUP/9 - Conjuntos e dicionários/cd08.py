import math


def converter_para_cartesiano(polar):
    cartesiano = {}

    r = polar["r"]
    a = polar["a"]

    cartesiano["x"] = r * math.cos(a)
    cartesiano["y"] = r * math.sin(a)

    return cartesiano


def programa_principal():
    r = float(input())
    a = float(input())

    ponto_polar = {}
    ponto_polar["r"] = r
    ponto_polar["a"] = a

    ponto_cartesiano = converter_para_cartesiano(ponto_polar)

    print(ponto_polar)
    print(ponto_cartesiano)


programa_principal()