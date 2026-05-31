n = int(input("Digite um numero inteiro: "))
# Write your code below
for i in range(1, n+1):
    for j in range(1, n+1):
        if i * j == n:
            print(i, j)