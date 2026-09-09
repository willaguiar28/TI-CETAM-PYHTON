nome_produto = input("DIGITE O NOME DO PRODUTO: ")
quantidade_disponivel = int(input("DIGITE A QUANTIDADE DISPONÍVEL: "))

if quantidade_disponivel == 0:
	resultado = "PRODUTO ESGOTADO"
elif quantidade_disponivel <= 5:
	resultado = "ESTOQUE CRÍTICO"
elif quantidade_disponivel <= 20:
	resultado = "ESTOQUE BAIXO"
else:
    resultado = "ESTOQUE NORMAL"

print (f"Nome do Produto: {nome_produto}")
print (f"Quantidade: {quantidade_disponivel}")
print(f"Resultado do Estoque: {resultado}")

if resultado == "PRODUTO ESGOTADO":
	print ("Acionar logística para restoque URGENTE!")
elif resultado == "ESTOQUE CRÍTICO":
	print ("Atenção! Estoque com duração de 15 dias.")
elif resultado == "ESTOQUE BAIXO":
	print ("Estoque com duração de 60 dias.")
else:
	print ("Estoque com quantidade normal. Duração de até 5 meses.")