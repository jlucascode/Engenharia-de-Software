N = int(input())
for n in range(N):
    elemento_anterior = 1

    print(elemento_anterior, end=" ")

    for k in range(1, n + 1):
        elemento_atual = elemento_anterior * (n - k + 1) / k

        print(int(elemento_atual), end=" ")

        elemento_anterior = elemento_atual
    print()