import livros
#from alunos import cadastrar_aluno
#from emprestimos import realizar_emprestimo


print(" === SISTEMA DE BIBLIOTECA CETAM === ")

while True:
    print("1 - Cadastro de Livro")
    print("2 - Cadastro de Aluno")
    print("3 - Realizar Empréstimo")
    print("4 - Listar Livros")
    print("5 - Sair")

    opcao = input("Informe a opção de escolha: ")

    if opcao == "1":
        livros.cadastrar_livro()
    elif opcao == "2":
        cadastrar_aluno()
    elif opcao == "3":
        realizar_emprestimo()
    elif opcao == "4":
        listar_livros()
    elif opcao == "5":
        print("Sessão encerrada com sucesso!")
        break
    else:
        print("Opção inválida! Tente novamente...")