nome = input("ESCREVA SEU NOME: ")

note_1 = int(input("DIGITE PRIMEIRA NOTA: "))
note_2 = int(input("DIGITE SEGUNDA NOTA: "))
note_3 = int(input("DIGITE TERCEIRA NOTA: "))

media = (note_1 + note_2 + note_3) / 3
media_aprov = 7

if media > media_aprov:
   print(nome, "ESTÁ APROVADO(A)")
elif media >= 5.0:
    print(nome, "ESTÁ DE RECUPERAÇÃO")
else:
    print(nome, "ESTÁ REPROVADO(A)")
