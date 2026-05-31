def funcao(n1, n2, n3, tipo):
    if tipo == 'A':
        media_aritimética = (n1 + n2 + n3) / 3
        return media_aritimética

    elif tipo == 'P':

        numerador = (n1 * 5) + (n2 * 3) + (n3 * 2)

        denominador = 5 + 3 + 2

        media_ponderada = numerador / denominador

        return media_ponderada

    else:
        return 0.0