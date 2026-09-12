print ("=" * 25)
print ("SISTEMA DE BIBLIOTECA - CADASTRO")
print ("=" * 25)

print ("1 - Cadastrar Livros")
print ("2 - Cadastrar Alunos")
print ("3 - Realizar Empréstimo")
print ("4 - Sair")

opcao_login = input("DIGITE A OPÇÃO DE ESCOLHA: ")

if opcao_login == "1":
    cadastro_livro = int(input("DIGITE A QUANTIDADE DE LIVROS PARA CADASTRO: "))
    for quantidade in range (cadastro_livro):
        print(f"LIVRO NÚMERO {quantidade + 1}")

        codigo_livro = int(input("DIGITE O CÓDIGO: "))
        titulo_livro = input("DIGITE O TÍTULO DO LIVRO: ")
        autor_livro = input("DIGITE O NOME DO AUTOR: ")
        ano_livro = int(input("DIGITE O ANO DE PUBLICAÇÃO: "))
        quantidade_livro_cadastro = int(input("DIGITE A QUANTIDADE DE LIVROS: "))


    if titulo_livro == "":
        print("TÍTULO NÃO PODE FICAR EM BRANCO!")
    elif autor_livro == "":
        print ("AUTOR NÃO PODE FICAR EM BRANCO!")
    elif ano_livro <0:
        print("DIGITE UM ANO VÁLIDO!")
    elif quantidade_livro_cadastro <0:
        print("QUANTIDADE PREICSA SER MAIOR QUE 0!")
    else:
        print("LIVRO CADASTRADO COM SUCESSO!")


        
        