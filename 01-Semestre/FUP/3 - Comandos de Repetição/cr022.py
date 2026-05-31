N = int(input())
numinicial = 1

for i in range(1, N + 1):
    for c in range(1, i + 1):
        print(numinicial, end=" ")

        numinicial = numinicial + 1

    print()