quantidade = int(input("Quantos alunos serão cadastrados? "))

contador = 0

while contador < quantidade:
    nome = input("Digite o nome do aluno: ")
    print(f"Aluno cadastrado: {nome}")
    contador += 1

print("Cadastro finalizado!")