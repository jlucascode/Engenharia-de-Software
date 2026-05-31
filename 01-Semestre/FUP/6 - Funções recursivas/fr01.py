def funcao(n):
    if n == 1:
        return 1
    if n <= 0:
        return 0
    else:
        return n + funcao(n - 1)