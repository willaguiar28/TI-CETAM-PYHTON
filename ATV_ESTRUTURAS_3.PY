nome_cliente = input("Digite seu nome: ")
velocidade_internet = float(input("Digite sua velocidade contratada: "))

if velocidade_internet == 50:
    resultado = "Plano Básico"
elif velocidade_internet <= 199:
    resultado = "Plano Intermediário"
elif velocidade_internet <= 499:
    resultado = "Plano Avançado"
else:
    resultado = "Plano Ultra"

print ("RESULTADO")

print (f"Nome do Cliente: {nome_cliente}")
print (f"Velocidade Contratada: {velocidade_internet}", "Mbps")
print (f"Plano Contratado: {resultado}")