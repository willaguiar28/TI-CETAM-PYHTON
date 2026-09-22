print("=" * 10 + " BIBLIOTECA CETAM " + "=" * 10)

biblioteca = []

#while True:

    print("1. Cadastrar Livro")
    print("2. Ver Lista")
    print("3. Pesquisar por Código")
    print("4. Alterar Livro")
    print("5. Excluir Livro")
    print("6. Sair")

    opcao_menu = input("Informe sua escolha: ")

    if opcao_menu == "1":
        titulo_livro = input("Informe o título: ")
        autor_livro = input("Informe o autor: ")
        ano_livro = input("Informe o ano: ")

        livros = [titulo_livro, autor_livro, ano_livro]
        biblioteca.append(livros)
        
        print("Livro cadastrado!")
        print(biblioteca)

    else:
        print("Sessão encerrada!")
        break