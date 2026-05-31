import math


def somar(z, w):
    res = {}
    res["real"] = z["real"] + w["real"]
    res["imaginario"] = z["imaginario"] + w["imaginario"]
    return res


def subtrair(z, w):
    res = {}
    res["real"] = z["real"] - w["real"]
    res["imaginario"] = z["imaginario"] - w["imaginario"]
    return res


def multiplicar(z, w):
    res = {}
    res["real"] = (z["real"] * w["real"]) - (z["imaginario"] * w["imaginario"])
    res["imaginario"] = (z["real"] * w["imaginario"]) + (z["imaginario"] * w["real"])
    return res


def calcular_modulo(n):
    return math.sqrt(n["real"] ** 2 + n["imaginario"] ** 2)


def programa_complexos():
    z = {}
    z["real"] = float(input())
    z["imaginario"] = float(input())

    w = {}
    w["real"] = float(input())
    w["imaginario"] = float(input())

    soma = somar(z, w)
    sub = subtrair(z, w)
    prod = multiplicar(z, w)
    mod_z = calcular_modulo(z)
    mod_w = calcular_modulo(w)

    print(soma)
    print(sub)
    print(prod)
    print(f'{mod_z:.2f}')
    print(f'{mod_w:.2f}')


programa_complexos()