def funcao(x, y):
    if x == y:
        return "Numeros iguais"

    elif x > y:
        return x

    else:
        return y
x = int(input())
y = int(input())
resultado = funcao(x, y)
print(resultado)