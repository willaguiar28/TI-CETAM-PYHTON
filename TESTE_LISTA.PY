print("=" * 10 + " SISTEMA DE BIBLIOTECA CETAM " + "=" * 10)

opcao = 0

while opcao != 3:
    print("\n1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Cadastro de Aluno")
    elif opcao == 2:
        print("Lista de Alunos")
    elif opcao == 3:
        print("Saindo...")
    else:
        print("Opção inválida!")