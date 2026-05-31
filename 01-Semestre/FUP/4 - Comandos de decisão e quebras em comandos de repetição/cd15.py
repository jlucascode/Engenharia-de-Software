numero = int(input())

soma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        soma_divisores = soma_divisores + i
print(soma_divisores)