RESULTADO = []
cont = 0

while True:
    cont += 1
    if cont % 7 != 0 and (cont - 7) % 10 != 0:
        RESULTADO.append(cont)
    if len(RESULTADO) == 100:
        break

print(RESULTADO)