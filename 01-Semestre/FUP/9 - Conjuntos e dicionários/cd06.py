def calcular_soma_vetores(v1, v2):
    resultado = {}
    resultado["x"] = v1["x"] + v2["x"]
    resultado["y"] = v1["y"] + v2["y"]
    resultado["z"] = v1["z"] + v2["z"]
    return resultado

v1 = {"x": float(input()), "y": float(input()), "z": float(input())}
v2 = {"x": float(input()), "y": float(input()), "z": float(input())}

soma = calcular_soma_vetores(v1, v2)
print(soma)