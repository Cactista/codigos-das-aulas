saldo = 0.0
print("=== Banco Sicredo - Sua conta ===\n")
while True:
    print("1 - depositar | 2 - sacar | 3 - ver saldo | 4 - sair")
    op = input("escolha: ")

    if op == '1':
        valor = float(input("Quanto Você irá depositar"))
        saldo += valor
        print("Deposito efetuado com sucesso")

    elif op == '2':
        valor = float(input("Quanto Você irá sacar"))
        if valor <= saldo:
            saldo -= valor
        print("Saque efetuado com sucesso")
    elif op == '3':
        print(f"Seu saldo é de {saldo}")
    elif op == '4':
        print("saindo")
        break
    else:
        print("Por favor insira só os numero mostrados")
