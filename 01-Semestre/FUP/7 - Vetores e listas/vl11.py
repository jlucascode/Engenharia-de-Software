vetor = []
for i in range(15):
    vetor.append(float(input()))
media = 0
for n in vetor:
    media += n
media /= 15
print(f"{media:.2f}")