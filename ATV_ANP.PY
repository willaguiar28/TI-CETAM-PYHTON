livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Quantidade de Livros")
    print("6 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livros.append([titulo, autor])

        print("Livro cadastrado!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        for contador in livros:
            print("Título:", contador[0])
            print("Autor:", contador[1])

    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")

        for contador in livros:
            if contador[0] == pesquisa:
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])
            else:
                print("Livro não encontrado!")

    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")

        for contador in livros:
            if contador[0] == pesquisa:
                livros.remove(contador)
                print("Livro excluído!")
            else:
                print("Título incorreto ou livro não encontrado! Tenten novamente...")

    elif opcao == "5":

        quantidade = len(livros)
        print(f"Quantidade de livros cadastrados: {livros}")

    elif opcao == "6":

        print("Programa encerrado")
        break
    else:

        print("Opção inválida!")