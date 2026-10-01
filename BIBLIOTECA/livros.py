livros = []


def cadastrar_livro():
    qtd = int(input("Quantos livros deseja cadastrar? "))
    for i in range(qtd):
        print(f" === LIVRO #{i + 1} === ")
        codigo = input("Informe o código: ")
        titulo = input("Informe o título: ")
        autor = input("Informe o autor: ")
        ano = int(input("Informe o ano: "))
        quantidade = int(input("Informe a quantidade: "))

        if titulo == "" or autor == "" or codigo == "":
            print("Opa! 'Título' e/ou 'Autor' não podem ficar em branco.")
        elif ano < 1000 or ano > 2026:
            print("Opa! Informe um ano válido.")
        elif quantidade <= 0:
            print("Opa! Quantidade precisa ser maior que zero.")
        else:
            livros.append({
                "codigo": codigo,
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "quantidade": quantidade,
            })
            print("Livro cadastrado com sucesso!")


def listar_livros():
    print(" === LIVROS CADASTRADOS === ")
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(f"Código: {livro['codigo']} | Título: {livro['titulo']} | "
              f"Autor: {livro['autor']} | Ano: {livro['ano']} | "
              f"Disponíveis: {livro['quantidade']}")


def buscar_livro(codigo):
    for livro in livros:
        if livro["codigo"] == codigo:
            return livro
    return None