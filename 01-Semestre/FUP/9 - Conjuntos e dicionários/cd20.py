agenda = []
def inserir_pessoa():
    pessoa = {}

    pessoa['nome'] = input("Nome: ")
    pessoa['email'] = input("E-mail: ")

    endereco = {
        'rua': input("Rua: "),
        'numero': int(input("Numero: ")),
        'complemento': input("Complemento: "),
        'bairro': input("Bairro: "),
        'cep': input("CEP: "),
        'cidade': input("Cidade: "),
        'estado': input("Estado: "),
        'pais': input("Pais: ")
    }

    telefone = {
        'ddd': int(input("DDD: ")),
        'numero': input("Telefone: ")
    }

    nascimento = {
        'dia': int(input("Dia do nascimento: ")),
        'mes': int(input("Mes do nascimento: ")),
        'ano': int(input("Ano do nascimento: "))
    }

    pessoa['endereco'] = endereco
    pessoa['telefone'] = telefone
    pessoa['nascimento'] = nascimento
    pessoa['observacao'] = input("Observacao: ")

    agenda.append(pessoa)

def buscar_por_nome():
    nome = input("Primeiro nome: ")
    for pessoa in agenda:
        primeiro_nome = pessoa['nome'].split()[0]
        if primeiro_nome.startswith(nome):
            print(pessoa)

def buscar_por_mes():
    mes = int(input("Mes de nascimento: "))
    for pessoa in agenda:
        if pessoa['nascimento']['mes'] == mes:
            print(pessoa)

def buscar_por_dia_mes():
    dia = int(input("Dia do nascimento: "))
    mes = int(input("Mes do nascimento: "))
    for pessoa in agenda:
        if (pessoa['nascimento']['dia'] == dia and
                pessoa['nascimento']['mes'] == mes):
            print(pessoa)

def imprimir_agenda():
    print("1: Imprimir apenas nome, telefone e email")
    print("2: Imprimir todos os dados")
    opcao = input("Opcao: ")

    if opcao == '1':
        for pessoa in agenda:
            print({
                'nome': pessoa['nome'],
                'telefone': pessoa['telefone'],
                'email': pessoa['email']
            })

    elif opcao == '2':
        for pessoa in agenda:
            print(pessoa)

    else:
        print("Opcao invalida")

def menu():
    while True:
        print("1: Inserir uma pessoa")
        print("2: Buscar por primeiro nome")
        print("3: Buscar por mes de nascimento")
        print("4: Buscar por dia e mes de nascimento")
        print("5: Imprimir agenda")
        print("0: Sair")

        opcao = input("Opcao: ")

        if opcao == '1':
            inserir_pessoa()
        elif opcao == '2':
            buscar_por_nome()
        elif opcao == '3':
            buscar_por_mes()
        elif opcao == '4':
            buscar_por_dia_mes()
        elif opcao == '5':
            imprimir_agenda()
        elif opcao == '0':
            break
        else:
            print("Opcao invalida")
menu()