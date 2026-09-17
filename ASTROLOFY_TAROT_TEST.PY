print("=" * 10 + " ASTROLOGY READINGS " + "=" * 10)

operacao = int(input("How many times you want to use our data? "))

for quantidade in range(operacao):
    print("=" * 10 + f" READING NUMBER # {quantidade + 1}" + "=" * 10)

    print("1 - Tarot Personal Arcana")
    print("3 - Exit")

    opcao_entrada = int(input("Type your option: "))

    if opcao_entrada == 1:
        data = input("Enter your birthday (DD/MM/YYYY): ")
        soma = sum(int(d) for d in data if d.isdigit())

        while soma > 22:
            soma = sum(int(d) for d in str(soma))

        print(f"Your Personal Arcana is: {soma}")

    elif opcao_entrada == 3:
        print("Exiting...")
        break

    else:
        print("Invalid option.")