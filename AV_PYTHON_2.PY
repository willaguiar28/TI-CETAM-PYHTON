print("=" * 10 + " SISTEMA DE BIBLIOTECA CETAM " + "=" * 10)

operacao = input("Quantas operações deseja realizar? ")

if not operacao.isdigit() or int(operacao) <= 0:
    print("Opa! Quantidade de operações inválida.")
else:
    operacao = int(operacao)

    for quantidade in range(operacao):
        print("=" * 10 + f" CADASTRO/EMPRÉSTIMO {quantidade + 1} " + "=" * 10)

        print("1 - Cadastro de Livro")
        print("2 - Cadastro de Aluno")
        print("3 - Realizar Empréstimo")
        print("4 - Sair")

        opcao_entrada = input("Informe a opção de escolha: ")

        if opcao_entrada == "1":
            cadastro_livro = input("Quantos livros deseja cadastrar? ")

            if not cadastro_livro.isdigit() or int(cadastro_livro) <= 0:
                print("Opa! Quantidade de livros inválida.")
            else:
                cadastro_livro = int(cadastro_livro)

                for quantidade in range(cadastro_livro):
                    print("=" * 10 + f" LIVRO #{quantidade + 1} " + "=" * 10)

                    codigo_livro = input("Informe o código: ")
                    titulo_livro = input("Informe o título: ")
                    autor_livro = input("Informe o autor: ")
                    ano_livro = input("Informe o ano: ")
                    quantidade_livro = input("Informe a quantidade: ")

                    if codigo_livro.strip() == "":
                        print("Opa! O código não foi preenchido corretamente.")
                    elif titulo_livro.strip() == "" or autor_livro.strip() == "":
                        print("Opa! 'Título' e/ou 'Autor' não podem ficar em branco.")
                    elif not ano_livro.isdigit() or int(ano_livro) < 1500 or int(ano_livro) > 2100:
                        print("Opa! Informe um ano válido.")
                    elif not quantidade_livro.isdigit() or int(quantidade_livro) <= 0:
                        print("Opa! Quantidade precisa ser maior que zero.")
                    else:
                        print("Livro cadastrado com sucesso!")

        elif opcao_entrada == "2":
            cadastro_aluno = input("Quantos alunos deseja cadastrar? ")

            if not cadastro_aluno.isdigit() or int(cadastro_aluno) <= 0:
                print("Opa! Quantidade de alunos inválida.")
            else:
                cadastro_aluno = int(cadastro_aluno)

                for quantidade in range(cadastro_aluno):
                    print("=" * 10 + f" ALUNO #{quantidade + 1} " + "=" * 10)

                    matricula_aluno = input("Informe a matrícula: ")
                    nome_aluno = input("Informe o nome: ")
                    turma_aluno = input("Informe a Turma e/ou Curso: ")

                    if matricula_aluno.strip() == "":
                        print("Opa! A matrícula não foi preenchida corretamente.")
                    elif nome_aluno.strip() == "" or turma_aluno.strip() == "":
                        print("Opa! 'Nome' e 'Turma' não podem ficar em branco.")
                    else:
                        print("Aluno(a) cadastrado com sucesso!")

        elif opcao_entrada == "3":
            print("=" * 10 + " EMPRÉSTIMO DE LIVRO " + "=" * 10)

            codigo_emprest = input("Informe o código do livro: ")
            matricula_emprest = input("Informe a matrícula: ")
            quantidade_emprest = input("Informe a quantidade disponível: ")

            if codigo_emprest.strip() == "":
                print("Opa! O código do livro não pode ficar em branco.")
            elif matricula_emprest.strip() == "":
                print("Opa! A matrícula não pode ficar em branco.")
            elif not quantidade_emprest.isdigit():
                print("Opa! Informe uma quantidade válida.")
            elif int(quantidade_emprest) > 0:
                print("Empréstimo realizado com sucesso!")
            else:
                print("Não foi possível realizar o empréstimo.")
                print("Não há exemplares disponíveis. Tente novamente mais tarde.")

        elif opcao_entrada == "4":
            print("Sessão encerrada com sucesso!")
            break

        else:
            print("Opção inválida! Tente novamente...")