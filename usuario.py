nome = input("Informe seu Nome: ")
idade = int(input(f"Ola {nome} Informe sua Idade: "))
import webbrowser

if idade >= 18:
    print("Você é maior de idade, Acesso permitido", webbrowser.open ("https://www.roblox.com"))

else:
    print("Voce não tem idade suficiente, Acesso negado")

