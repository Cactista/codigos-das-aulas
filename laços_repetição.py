procurar = input("pesquisar peça: ")
estoque = ["prego","porca","arruela","parafuso","mola","rebite"]
for item in estoque:
    if item == procurar:
        print("Item encontrado no estoque")
        break
else:
    print("Item não encontrado apos varredura completa!")
