def funcao(y):
    if y % 2 == 1:
        return "Impar"

    else:
        return "Par"
y = int(input())

resultado = funcao(y)
print(resultado)