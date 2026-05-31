def A(m, n):
    if m < 0 or n < 0:
        return 0
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m - 1, 1)
    else:
        resultado_interno = A(m, n - 1)
        return A(m - 1, resultado_interno)