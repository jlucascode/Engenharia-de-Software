def programa_carros():
    carros = []

    for i in range(5):
        carro = {}
        carro["modelo"] = input()
        carro["ano"] = int(input())
        carro["preco"] = float(input())
        carros.append(carro)

    while True:
        p = float(input())
        if p == 0:
            break

        for carro in carros:
            if carro["preco"] < p:
                print(carro)
programa_carros()