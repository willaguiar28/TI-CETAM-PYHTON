while True:
    idade_menu = int(input("Informe sua idade: "))

    if idade_menu <= 0 or idade_menu >= 120:
        print("Idade inválida! Tente novamente")
    else:
        print(f"Ok, você tem {idade_menu} anos. Cadastro concluído!")
        break