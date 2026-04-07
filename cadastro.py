usuario_correto = "lucas"
senha_correta = 4231

input("Informe o nome de usuario: ")
int(input("Informe a senha: "))

if usuario_correto == 'lucas':
    if senha_correta == senha_correta:
        print("Conta logada com sucesso ")
    elif senha_correta != senha_correta :
        print("Senha Incorreta ")
else:
    print("Usario Incorreto ")