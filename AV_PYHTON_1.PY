print ("=" * 10 + " SISTEMA DE BIBLIOTECA CETAM " + "=" * 10)

operacao = int(input("Quantas operações deseja realizar? "))

for quantidade in range(operacao):
    print ("=" * 10 + f" CADASTRO/EMPRÉSTIMO {quantidade + 1} " + "=" * 10)

    print("1 - Cadastro de Livro")
    print("2 - Cadastro de Aluno")
    print("3 - Realizar Empréstimo")
    print("4 - Sair")

    opcao_entrada = input("Informe a opção de escolha: ")

    if opcao_entrada == "1":
        cadastro_livro = int(input("Quantos livros deseja cadastrar? "))

        for quantidade in range(cadastro_livro):
            print("=" * 10 + f" LIVRO #{quantidade + 1} " + "=" * 10)

            codigo_livro = input("Informe o código: ")
            titulo_livro = input("Informe o título: ")
            autor_livro = input("Informe o autor: ")
            ano_livro = int(input("Informe o ano: "))
            quantidade_livro = int(input("Informe a quantidade: "))

            if titulo_livro == "" or autor_livro == "":
                print("Opa! 'Título' e/ou 'Autor' não podem ficar em branco.")
            elif ano_livro < 1000 or ano_livro > 2026:
                print("Opa! Informe um ano válido.")
            elif quantidade_livro <= 0:
                print("Opa! Quantidade precisa ser maior que zero.")
            else:
                print("Livro cadastrado com sucesso!")

    elif opcao_entrada == "2":
        cadastro_aluno = int(input("Quantos alunos deseja cadastrar? "))

        for quantidade in range(cadastro_aluno):
            print("=" * 10 + f" ALUNO #{quantidade + 1} " + "=" * 10)

            matricula_aluno = input("Informe a matrícula: ")
            nome_aluno = input("Informe o nome: ")
            turma_aluno = input("Informe a turma e/ou curso: ")

            if matricula_aluno == "":
                print("Opa! A matrícula não foi preenchida corretamente.")
            elif nome_aluno == "" or turma_aluno == "":
                print("Opa! 'Nome' e 'Turma' não podem ficar em branco.")
            else:
                print("Aluno(a) cadastrado com sucesso!")

    elif opcao_entrada == "3":
        print("=" * 10 + " EMPRÉSTIMO DE LIVRO " + "=" * 10)
        codigo_emprest = input("Informe o código do livro: ")
        matricula_emprest = input("Informe a matrícula: ")
        quantidade_emprest = int(input("Informe a quantidade disponível: "))

        if codigo_emprest == "":
            print("Opa! Código inválido. Tente novamente.")
        elif matricula_emprest == "":
            print("Opa! Matrícula inválida ou não pode ficar em branco. Tente novamente.")
        elif quantidade_emprest > 0:
            print("Empréstimo realizado com sucesso!")
        else:
            print("Não foi possível realizar o empréstimo.")
            print("Não há exemplares disponíveis. Tente novamente mais tarde.")

    elif opcao_entrada == "4":
        print("Sessão encerrada com sucesso!")
        break

    else:
        print("Opção inválida! Tente novamente...")