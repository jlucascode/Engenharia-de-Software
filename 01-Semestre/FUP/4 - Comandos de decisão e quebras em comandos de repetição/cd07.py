salario = float(input())
prestacao = float(input())

limite = salario * 0.20

if prestacao > limite:
    print("Emprestimo nao concedido")

else:
    print("Emprestimo concedido")