n = int(input())

soma_divisores = 0
for i in range(1, n):
    if n % i == 0:
        soma_divisores = soma_divisores + i
if soma_divisores == n:
    print("Perfeito")
else:
    print("Nao perfeito")