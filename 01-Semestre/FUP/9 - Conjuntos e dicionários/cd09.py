def programa_funcionario():
    funcionario = {}

    funcionario["nome"] = input()
    funcionario["idade"] = int(input())
    funcionario["sexo"] = input()
    funcionario["cpf"] = input()
    funcionario["nascimento"] = input()

    funcionario["setor"] = int(input())

    funcionario["cargo"] = input()

    funcionario["salario"] = float(input())

    print(funcionario)


programa_funcionario()