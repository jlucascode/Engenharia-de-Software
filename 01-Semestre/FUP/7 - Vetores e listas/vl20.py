codigo = 1
VETOR = []
for c in range (100):
    VETOR.append(float(input()))
while codigo != 0:
    codigo = int(input())
    if codigo == 1:
        for v in VETOR:
            print(f"{v:.1f}")
    elif codigo == 2:
        for i in range(99, -1, -1):
            print(f"{VETOR[i]:.1f}")
    elif codigo != 0:
        print("Codigo invalido")