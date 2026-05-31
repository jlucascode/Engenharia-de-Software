num1 = float(input())
num2 = float(input())
opcao = float(input())
if opcao == 1:
    media = (num1 + num2) / 2
    print(f"{media:.2f}")

elif opcao == 2:
    if num1 > num2:
        diferenca = num1 - num2
    else:
        diferenca = num2 - num1

    print(f"{diferenca:.2f}")

elif opcao == 3:
    produto = num1 * num2
    print(f"{produto:.2f}")

elif opcao == 4:
    if num2 == 0:
        print("Erro")
    else:
        divisao = num1 / num2
        print(f"{divisao:.2f}")
else:
    print("Erro")