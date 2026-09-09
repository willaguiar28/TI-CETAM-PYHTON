nome_usuario = input("DIGITE SEU NOME DE USUÁRIO: ")

print ("Indisponibilidade total do sistema - 1")
print ("Sistema funcionando, mas com lentidão ou erros - 2")
print ("Problema que não impede o trabalho - 3")
print ("Outros problemas - 4")

tipo_problema = input("ESCOLHA O NÚMERO DO PROBLEMA: ")
tempo_problema = input("INFORME OS DIAS DE PROBLEMA: ")

if tipo_problema == "1":
	prioridade = "URGENTE"
elif tipo_problema == "2":
	prioridade = "ALTA"
elif tipo_problema == "3":
	prioridade = "MÉDIA"
else:
	prioridade = "BAIXA"

print (f"Nome de Usuário: {nome_usuario}")
print (f"Tipo do Problema: {tipo_problema}")
print (f"Tempo do Problema: {tempo_problema}")
print (f"Nível de Prioridade: {prioridade}")

if prioridade == "URGENTE":
	print ("Entre em contato com nossos técnicos pelo chat em até 5 minutos.")
elif prioridade == "ALTA":
	print ("Nossa equipe entrará em contato o quanto breve!")
elif prioridade == "MÉDIA":
	print ("Problema será solucionado em até 24 horas. Aguarde!")
else:
	print ("Não urgente. Volte daqui 1 mês!")