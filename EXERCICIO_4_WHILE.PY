while True:
    print("=" * 10 + " MENU PRINCIPAL " + "=" * 10)
    print("1. Cadastrar Livro")
    print("2. Listar Livro")
    print("3. Sair")

    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == "1":
        cadastro_livro = input("Informe o livro: ")
        print("Livro cadastrado com sucesso!")

    elif opcao_menu == "2":
        listar_livro = input("Livros cadastrados: ")

    elif opcao_menu == "3":
        print("Sessão encerrada!")
        break
    else:
        print("Opa! Opção inválida. Tente novamente...")