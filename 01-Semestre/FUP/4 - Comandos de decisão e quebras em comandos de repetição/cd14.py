while True:
    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Saida")

    opcao = int(input())

    if opcao == 5:
        break

    elif opcao < 1 or opcao > 5:
        print("Opcao invalida. Tente novamente.")
        continue

    num1 = float(input())
    num2 = float(input())

    if opcao == 1:
        resultado = num1 + num2
        print(f"{resultado:.2f}")

    elif opcao == 2:
        resultado = num1 - num2
        print(f"{resultado:.2f}")

    elif opcao == 3:
        resultado = num1 * num2
        print(f"{resultado:.2f}")

    elif opcao == 4:
        if num2 == 0:
            print("Erro: Divisao por zero.")
        else:
            resultado = num1 / num2
            print(f"{resultado:.2f}")8