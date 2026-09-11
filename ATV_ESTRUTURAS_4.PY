nome_aluno = input("DIGITE SEU NOME: ")
idade_aluno = int(input("DIGITE SUA IDADE: "))
cadastro = input("POSSUI CADASTRO? ")

print(f"Nome do Aluno: {nome_aluno}")
print(f"Idade do Aluno: {idade_aluno}")
print(f"Possui Cadastro Ativo: {cadastro}")

if cadastro not in ("Sim", "S", "s", "Sim.", "sim"):
    print ("Acesso negado.")
elif idade_aluno <= 14:
    print ("Acesso somente com acompanhamento.")
else:
    print ("Acesso permitido.")