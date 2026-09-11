valor_peca = float(input("DIGITE O VALOR DA PEÇA: "))
valor_obra = float(input("DGITE O VALOR DA MÃO DE OBRA: "))

total = valor_peca + valor_obra

desconto = total * 0.10
com_desconto = total - desconto

taxa = total * 0.05
com_taxa = total + taxa

print (f"\nTotal: R$ {total:.2f}")
print (f"Com Desconto: {com_desconto:.2f}")
print (f"Com taxa (5%): {com_taxa:.2f}")