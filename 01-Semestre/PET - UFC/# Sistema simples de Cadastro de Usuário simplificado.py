usuarios = []  
while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar usuário")
    print("2 - Visualizar usuários")
    print("3 - Editar usuário")
    print("4 - Excluir usuário")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        email = input("Email: ")
        usuarios.append([nome, idade, email])
        print("Usuário cadastrado com sucesso!")

    
    elif opcao == "2":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            print("\n--- Lista de Usuários ---")
            for i, u in enumerate(usuarios):
                print(f"{i + 1}. Nome: {u[0]} | Idade: {u[1]} | Email: {u[2]}")

    elif opcao == "3":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            for i, u in enumerate(usuarios):
                print(f"{i + 1}. {u[0]}")
            indice = int(input("Digite o número do usuário para editar: ")) - 1
            if 0 <= indice < len(usuarios):
                nome = input("Novo nome: ")
                idade = input("Nova idade: ")
                email = input("Novo email: ")
                usuarios[indice] = [nome, idade, email]
                print("Usuário atualizado com sucesso!")
            else:
                print("Usuário não encontrado.")


    elif opcao == "4":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            for i, u in enumerate(usuarios):
                print(f"{i + 1}. {u[0]}")
            indice = int(input("Digite o número do usuário para excluir: ")) - 1
            if 0 <= indice < len(usuarios):
                usuarios.pop(indice)
                print("Usuário excluído com sucesso!")
            else:
                print("Usuário não encontrado.")


    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, tente novamente.")
