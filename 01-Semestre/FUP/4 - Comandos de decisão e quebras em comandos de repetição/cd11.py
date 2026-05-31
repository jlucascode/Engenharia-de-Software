num1 = float(input())

operacao = input()

num2 = float(input())

if operacao == '+':
    resultado = num1 + num2
    print(f"{resultado:.2f}")

elif operacao == '-':
    resultado = num1 - num2
    print(f"{resultado:.2f}")

elif operacao == '*':
    resultado = num1 * num2
    print(f"{resultado:.2f}")

elif operacao == '/':

    if num2 == 0:
        print("Erro: Divisão por zero")
    else:
        resultado = num1 / num2
        print(f"{resultado:.2f}")
else:
    print("Operação inválida")