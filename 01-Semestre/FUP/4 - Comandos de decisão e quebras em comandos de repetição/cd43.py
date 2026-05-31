leitura = True
nome_jovem = ""
idade_jovem = 0
nome_velho = ""
idade_velho = 0

while True:
    nome = input()
    idade = int(input())
    if idade < 0:
        break

    if leitura == True:
        idade_jovem = idade
        nome_jovem = nome

        idade_velho = idade
        nome_velho = nome
        leitura = False

    else:
        if idade < idade_jovem:
            idade_jovem = idade
            nome_jovem = nome
        if idade > idade_velho:
            idade_velho = idade
            nome_velho = nome
if leitura == False:
    print(nome_jovem)
    print(idade_jovem)
    print(nome_velho)
    print(idade_velho)