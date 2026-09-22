print ("=" * 10 + " MENU PRINCIPAL " + "=" * 10)

menu = int(input("Quantos livros deseja cadastrar: "))

contador = 0
while contador < menu: 

    titulo_livro = input("Informe o título: ")
    autor_livro = input("Informe o autor: ")
    ano_publi = input("Informe o ano de publicação: ")

    print("\nLivro cadastrado com sucesso!")

    contador += 1