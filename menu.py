# inicializamos a variavel opção
opcao = 0

while opcao != 3:
    print("\n--- Menu do Sistema ---")
    print("\nn1 - Saudação")
    print("\nn2 - Informações do sistema")
    print("\nn3 - sair")

# recebendo entrada do usuario
    try: opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Por favor digite apenas Numeros")

    #estrututras de decisão
    if opcao == 1:
        print("\n Ola é um prazer ajudar você.")
    elif opcao == 2:
        print("\n Sistema: python 3.10")
        print("\n Status: Operacional")
    elif opcao == 3:
        print("\nSaindo ... Até logo")
    else:
        print("\n")