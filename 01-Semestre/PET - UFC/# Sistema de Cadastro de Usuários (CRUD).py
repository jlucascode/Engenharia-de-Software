# Sistema de Cadastro de Usuários (CRUD)
# Autor: João Lucas Miranda
# Curso: Fundamentos de Programação com Python

usuarios = []  # Lista para armazenar os usuários

def cadastrar_usuario():
    print("\n=== Cadastro de Usuário ===")
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")

    usuario = {"nome": nome, "idade": idade, "email": email}
    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!\n")

def visualizar_usuarios():
    print("\n=== Usuários Cadastrados ===")
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.\n")
    else:
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. Nome: {usuario['nome']} | Idade: {usuario['idade']} | Email: {usuario['email']}")
        print()

def editar_usuario():
    print("\n=== Editar Usuário ===")
    visualizar_usuarios()

    if len(usuarios) == 0:
        return

    try:
        indice = int(input("Digite o número do usuário que deseja editar: ")) - 1
        if 0 <= indice < len(usuarios):
            print("Deixe em branco caso não queira alterar um campo.")
            novo_nome = input(f"Novo nome ({usuarios[indice]['nome']}): ")
            nova_idade = input(f"Nova idade ({usuarios[indice]['idade']}): ")
            novo_email = input(f"Novo email ({usuarios[indice]['email']}): ")

            if novo_nome:
                usuarios[indice]['nome'] = novo_nome
            if nova_idade:
                usuarios[indice]['idade'] = nova_idade
            if novo_email:
                usuarios[indice]['email'] = novo_email

            print("\nUsuário atualizado com sucesso!\n")
        else:
            print("Usuário não encontrado.\n")
    except ValueError:
        print("Entrada inválida. Digite um número válido.\n")

def excluir_usuario():
    print("\n=== Excluir Usuário ===")
    visualizar_usuarios()

    if len(usuarios) == 0:
        return

    try:
        indice = int(input("Digite o número do usuário que deseja excluir: ")) - 1
        if 0 <= indice < len(usuarios):
            usuario_removido = usuarios.pop(indice)
            print(f"\nUsuário '{usuario_removido['nome']}' excluído com sucesso!\n")
        else:
            print("Usuário não encontrado.\n")
    except ValueError:
        print("Entrada inválida. Digite um número válido.\n")

def menu():
    while True:
        print("=== MENU ===")
        print("1 - Cadastrar Usuário")
        print("2 - Visualizar Usuários")
        print("3 - Editar Usuário")
        print("4 - Excluir Usuário")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            visualizar_usuarios()
        elif opcao == "3":
            editar_usuario()
        elif opcao == "4":
            excluir_usuario()
        elif opcao == "5":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Inicia o programa
menu()
