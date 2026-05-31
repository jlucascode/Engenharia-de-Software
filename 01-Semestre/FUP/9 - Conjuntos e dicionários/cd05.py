def calcular_soma_vetores(v1, v2):
    # Criando o dicionário para armazenar o resultado
    resultado = {}

    # Somando componente a componente conforme a regra dos vetores
    resultado["x"] = v1["x"] + v2["x"]
    resultado["y"] = v1["y"] + v2["y"]
    resultado["z"] = v1["z"] + v2["z"]

    return resultado


# Programa principal
# Lendo os dados do primeiro vetor
v1 = {}
v1["x"] = float(input("Digite o x do primeiro vetor: "))
v1["y"] = float(input("Digite o y do primeiro vetor: "))
v1["z"] = float(input("Digite o z do primeiro vetor: "))

# Lendo os dados do segundo vetor
v2 = {}
v2["x"] = float(input("Digite o x do segundo vetor: "))
v2["y"] = float(input("Digite o y do segundo vetor: "))
v2["z"] = float(input("Digite o z do segundo vetor: "))

# Chamando a função
soma = calcular_soma_vetores(v1, v2)

# Mostrando o resultado formatado
# Nota: Não usamos .join() nem funções embutidas de lista aqui
print(f"Resultado da soma: x={soma['x']:.2f}, y={soma['y']:.2f}, z={soma['z']:.2f}")