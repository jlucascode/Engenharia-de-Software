def funcao(matriz):
    matriz_resultado = []

    for linha in matriz:
        maior_modulo = 0
        for elemento in linha:
            if abs(elemento) > maior_modulo:
                maior_modulo = abs(elemento)

        nova_linha = []
        for elemento in linha:
            if maior_modulo != 0:
                nova_linha.append(elemento / maior_modulo)
            else:
                nova_linha.append(0.0)
        matriz_resultado.append(nova_linha)
    return matriz_resultado
