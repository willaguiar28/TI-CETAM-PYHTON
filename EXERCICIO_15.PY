salario_atual = float(input("DIGITE O SALÁRIO ATUAL: "))
salario_reajuste = float(input("DIGITE O VALOR DO REAJUSTE: "))


salario_reajuste = salario_atual / 100
novo_salario = (salario_atual * salario_reajuste) / 100

print("O NOVO SALÁRIO SERÁ DE: R$", novo_salario)
