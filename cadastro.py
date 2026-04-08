usuario_correto = "lucas"
senha_correta = 1313

usuario = input("Informe o nome de usuario: ")
senha = int(input("Informe a senha: "))

if usuario == usuario_correto and senha == senha_correta:
    print("Conta logada com sucesso")
    
else:
    print("Usario ou senha Incorretos ")
