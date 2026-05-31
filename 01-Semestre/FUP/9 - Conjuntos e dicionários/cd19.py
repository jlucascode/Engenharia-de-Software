def encontrar_maior_idade(cadastros):
    mais_velho = cadastros[0]
    for pessoa in cadastros:
        if pessoa['idade'] > mais_velho['idade']:
            mais_velho = pessoa
    return mais_velho


def encontrar_sexo_masculino(cadastros):
    masculinos = []
    for pessoa in cadastros:
        if pessoa['sexo'].upper() == 'M' or pessoa['sexo'].upper() == 'MASCULINO':
            masculinos.append(pessoa)
    return masculinos


def encontrar_salario_maior_que_mil(cadastros):
    ricos = []
    for pessoa in cadastros:
        if pessoa['salario'] > 1000.0:
            ricos.append(pessoa)
    return ricos


def buscar_por_identidade(cadastros, identidade_procurada):
    for pessoa in cadastros:
        if pessoa['identidade'] == identidade_procurada:
            return pessoa
    return None


def obter_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")


def obter_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada invalida. Digite um numero decimal.")


def gerenciar_cadastros():
    cadastros = []

    for i in range(5):
        nome = input("Nome: ")
        endereco_rua = input("Rua: ")
        endereco_bairro = input("Bairro: ")
        endereco_cidade = input("Cidade: ")
        endereco_estado = input("Estado: ")
        endereco_cep = input("CEP: ")
        salario = obter_float("Salario: ")
        identidade = input("Identidade: ")
        cpf = input("CPF: ")
        estado_civil = input("Estado Civil: ")
        telefone = input("Telefone: ")
        idade = obter_int("Idade: ")
        sexo = input("Sexo: ")

        endereco = {
            'rua': endereco_rua,
            'bairro': endereco_bairro,
            'cidade': endereco_cidade,
            'estado': endereco_estado,
            'cep': endereco_cep
        }

        pessoa = {
            'nome': nome,
            'endereco': endereco,
            'salario': salario,
            'identidade': identidade,
            'cpf': cpf,
            'civil': estado_civil,  # Chave alterada para 'civil' conforme saida desejada
            'telefone': telefone,
            'idade': idade,
            'sexo': sexo
        }
        cadastros.append(pessoa)

    print("Pessoa com maior idade:")
    pessoa_mais_velha = encontrar_maior_idade(cadastros)
    print(pessoa_mais_velha)

    print("Pessoas do sexo masculino:")
    homens = encontrar_sexo_masculino(cadastros)
    for homem in homens:
        print(homem)

    print("Pessoas com salario maior que 1000:")
    salarios_altos = encontrar_salario_maior_que_mil(cadastros)
    for p in salarios_altos:
        print(p)

    id_busca = input("Identidade: ")
    pessoa_encontrada = buscar_por_identidade(cadastros, id_busca)
    if pessoa_encontrada:
        print(pessoa_encontrada)


gerenciar_cadastros()