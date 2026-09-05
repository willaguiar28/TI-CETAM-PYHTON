salario_atual = float(input("DIGITE O SALÁRIO ATUAL: "))
percentual_reajuste = float(input("DIGITE O PERCENTUAL DE REAJUSTE (%): "))

valor_reajuste = salario_atual * (percentual_reajuste / 100)
novo_salario = salario_atual + valor_reajuste

print("SEU NOVO SALÁRIO SERÁ DE: ", novo_salario)