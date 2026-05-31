num1 = int(input())
num2 = int(input())

quociente = 0

if num1 > num2:
    dividendo = num1
    divisor = num2
elif num2 > num1:
    dividendo = num2
    divisor = num1
else:
    if num1 != 0:
        dividendo = num1
        divisor = num2
    else:
        pass

if divisor == 0:
    print("Divisao por zero nao e permitida")
else:
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        quociente = quociente + 1

    print(quociente)