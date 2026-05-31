valor =[]
for i in range(10):
    valor.append((float(input())))
quadrado = []
for n in valor:
    print(f"{n:.2f}")
for n in valor:
    quadrado.append(n**2)
    print(f"{n**2:.2f}")