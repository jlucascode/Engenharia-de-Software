n1 = float(input())
n2 = float(input())
n3 = float(input())
if n1 <= n2 and n1 <= n3:
    print(int(n1))

    if n2 <= n3:
        print(int(n2))
        print(int(n3))
    else:
        print(int(n3))
        print(int(n2))

elif n2 <= n3:
    print(int(n2))

    if n1 <= n3:
        print(int(n1))
        print(int(n3))
    else:
        print(int(n3))
        print(int(n1))

else:
    print(int(n3))
    if n1 <= n2:
        print(int(n1))
        print(int(n2))
    else:
        print(int(n2))
        print(int(n1))