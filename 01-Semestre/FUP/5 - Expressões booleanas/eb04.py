numero = int(input())

divisivel_por_3 = (numero % 3 == 0)
divisivel_por_5 = (numero % 5 == 0)

condicao_ou = divisivel_por_3 or divisivel_por_5

condicao_nao_simultaneo = not (divisivel_por_3 and divisivel_por_5)

resultado = condicao_ou and condicao_nao_simultaneo

if resultado:
    print("True")
else:
    print("False")