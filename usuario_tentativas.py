usuario_correto = "lucas"
senha_correta = 1313

for tentativa in range(1, 4):
    usuario = input(f"Informe o nome de usuario: ").strip()
    senha = int(input("Informe a senha: "))

    if usuario == usuario_correto and senha == senha_correta:     
         print("\nConta logada com sucesso")
         print(f"Olá {usuario}! Tudo bem?")
         break
    print("\nUsario ou senha Incorretos")
else:
    print("Tentativas esgotadas")
