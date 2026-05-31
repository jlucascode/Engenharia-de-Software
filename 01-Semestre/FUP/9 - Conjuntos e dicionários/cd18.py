def gerenciar_estoque():
    estoque = []

    for i in range(5):
        codigo = int(input())
        nome = input()
        preco = float(input())
        quantidade = int(input())

        produto = {
            "codigo": codigo,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }
        estoque.append(produto)

    while True:
        for p in estoque:
            print(p)

        codigo_pedido = int(input())

        if codigo_pedido == 0:
            break

        quantidade_pedida = int(input())

        achou = False
        for p in estoque:
            if p["codigo"] == codigo_pedido:
                achou = True
                if p["quantidade"] >= quantidade_pedida:
                    p["quantidade"] = p["quantidade"] - quantidade_pedida
                else:
                    print("Impossivel atender ao pedido, produto sem estoque suficiente")
                break

        if not achou:
            print("Impossivel atender ao pedido, codigo nao encontrado")


gerenciar_estoque()