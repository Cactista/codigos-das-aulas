for tentativa in range(1, 4):
    nome = input(f"Digite seu nome (tentativa {tentativa}/3): ").strip()
    if nome != "":
        print(f"\nOlá {nome}! Tudo bem?")
        break
    print("\nvocê não digitou seu nome")
else:
    print("Tentativas esgotadas")
