num1 = float(input())
num2 = float(input())
num3 = float(input())
if num1 >= num2:

    if num1 >= num3:
        print(num1)

    else:
        print(num3)

elif num2 >= num3:
    print(num2)

else:
    print(num3)