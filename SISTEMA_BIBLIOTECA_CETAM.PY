livros = []

def cadastrar_livro():
    cadastro_livro = int(input("Quantos livros deseja cadastrar? "))
    for quantidade in range(cadastro_livro):
        print(f" === LIVRO #{quantidade + 1} === ")
        codigo_livro = input("Informe o código: ")
        titulo_livro = input("Informe o título: ")
        autor_livro = input("Informe o autor: ")
        ano_livro = int(input("Informe o ano: "))
        quantidade_livro = int(input("Informe a quantidade: "))

        if titulo_livro == "" or autor_livro == "" or codigo_livro == "":
            print("Opa! 'Título' e/ou 'Autor' não podem ficar em branco.")
        elif ano_livro < 1000 or ano_livro > 2026:
            print("Opa! Informe um ano válido.")
        elif quantidade_livro <= 0:
            print("Opa! Quantidade precisa ser maior que zero.")
        else:
            livros.append({
                "codigo": codigo_livro,
                "titulo": titulo_livro,
                "autor": autor_livro,
                "ano": ano_livro,
                "quantidade": quantidade_livro,
            })
            print("Livro cadastrado com sucesso!")


def cadastrar_aluno():
    cadastro_aluno = int(input("Quantos alunos deseja cadastrar? "))
    for quantidade in range(cadastro_aluno):
        print(f" ALUNO #{quantidade + 1}")
        matricula_aluno = input("Informe a matrícula: ")
        nome_aluno = input("Informe o nome: ")
        turma_aluno = input("Informe a turma e/ou curso: ")

        if matricula_aluno == "":
            print("Opa! A matrícula não foi preenchida corretamente.")
        elif nome_aluno == "" or turma_aluno == "":
            print("Opa! 'Nome' e 'Turma' não podem ficar em branco.")
        else:
            print("Aluno(a) cadastrado com sucesso!")


def realizar_emprestimo():
    print(" === EMPRÉSTIMO DE LIVRO === ")
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


def listar_livros():
    print(" === LIVROS CADASTRADOS === ")
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(f"Código: {livro['codigo']} | Título: {livro['titulo']} | "
              f"Autor: {livro['autor']} | Ano: {livro['ano']} | "
              f"Disponíveis: {livro['quantidade']}")


print(" === SISTEMA DE BIBLIOTECA CETAM === ")

while True:
    print("1 - Cadastro de Livro")
    print("2 - Cadastro de Aluno")
    print("3 - Realizar Empréstimo")
    print("4 - Listar Livros")
    print("5 - Sair")

    opcao_entrada = input("Informe a opção de escolha: ")

    if opcao_entrada == "1":
        cadastrar_livro()
    elif opcao_entrada == "2":
        cadastrar_aluno()
    elif opcao_entrada == "3":
        realizar_emprestimo()
    elif opcao_entrada == "4":
        listar_livros()
    elif opcao_entrada == "5":
        print("Sessão encerrada com sucesso!")
        break
    else:
        print("Opção inválida! Tente novamente...")