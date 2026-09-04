
ive_members = {
    "yujin": "Líder, Dançarina Principal, Vocalista, Centro",
    "gaeul": "Dançarina Líder, Rapper, Vocalista",
    "rei": "Rapper, Vocalista",
    "wonyoung": "Centro, Vocalista, Dançarina, Visual",
    "liz": "Vocalista Principal",
    "leeseo": "Dançarina, Vocalista, Maknae"
}

nome = input("Digite o nome de uma integrante do IVE: ").strip().lower()

if nome in ive_members:
    print(f"\n{nome.title()} - Posição: {ive_members[nome]}")
else:
    print(f"\nIntegrante '{nome}' não encontrada!")
    print("Integrantes disponíveis: Yujin, Gaeul, Rei, Wonyoung, Liz, Leeseo")