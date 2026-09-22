print("=" * 10 + " ÁREA DE LOGIN " + "=" * 10)

while True:
    senha = input("Digite sua senha: ")
    if senha != "3108":
        print("Acesso negado! Tente novamente...")
    else:
        print("Acesso permitido!")
        break