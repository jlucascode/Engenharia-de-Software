def h(m, n):
    if m <= 0 or n <= 0:
        pass
    if n == 1:
        return m + 1
    elif m == 1:
        return n + 1
    elif m > 1 and n > 1:
        return h(m, n - 1) + h(m - 1, n)
    else:
        return 0