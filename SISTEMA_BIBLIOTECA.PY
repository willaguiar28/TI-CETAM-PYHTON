print ("=" * 10 + "SISTEMA DE BIBLIOTECA CETAM" + "=" * 10)

biblioteca = []
alunos = []
emprestimo = []

while True:
    print ("=" * 10 + "MENU PRINCIPAL" + "=" * 10)
    print("1. Cadastro de Livros")
    print("2. Cadastro de Alunos")
    print("3. Realizar Empréstimo")
    print("4. Listar Livros")
    print("5. Pesquisar Livros")
    print("6. Alterar Livro")
    print("7. Excluir Livro")
    print("8. Sair/Encerrar Sessão")

    opcao = input("Digite a opção de escolha: ")

    if opcao == "1":
        codigo_livro = input("Informe o código: ")
        titulo_livro = input("Informe o título: ")
        autor_livro = input("Informe o autor: ")
        ano_livro = int(input("Inforem o ano: "))
        quantidade_livro = input("Informe a quantidade: ")

        if titulo_livro == "" or autor_livro == "":
            print("Opa! 'Título' e/ou 'Autor' não podem ficar em branco.")
        elif ano_livro < 1000 or ano_livro > 2026:
            print("Opa! Informe um ano válido.")
        elif quantidade_livro <= 0:
            print("Opa! Quantidade precisa ser maior que zero")
        else:
            codigo_repetido = False
            for livro in biblioteca:
                if livro[0] == codigo_livro:
                    codigo_repetido == True
                    break

        if codigo_repetido:
            print("Opa! Já existe um livro com esse código")
        else:
            biblioteca.append([codigo, titulo, autor, ano, quantidade])
            print("Livro cadastrado com sucesso!")
    elif opcao == "2":
        matricula_aluno = input("Digite a matrícula: ")
        nome_aluno = input("Informe o nome: ")
        turma_aluno = input("Digite a turma e/ou curso: ")

        if matricula_aluno == "" or nome_aluno == "":
            print("Opa! Matrícula/Nome não podem ficar em branco.")
          
