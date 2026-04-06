print("="*20 + " Lanchonete Senai " + "="*20 )

valor_burguer = 16.00
valor_refri = 4.00

cliente = input("Por Favor insira seu nome: ")
print(f"\nSeja bem vindo {cliente}")
print("-"*40)
print("=== Nosso Cardapio ===")
print(f"\nHamburguer R$ {valor_burguer}")
print(f"\nRefrigerante R$ {valor_refri}")
print("-"*40)

qtd_burger = int(input("\nQuantos Hamburgueres você deseja? "))
qtd_refri = int(input("Quantos refrigerantes você deseja? "))

total_valor = (valor_refri*qtd_refri)+(valor_burguer*qtd_burger)
total = qtd_burger + qtd_refri

print(" "*12+"Cupom Fiscal"+" "*12)
print(f"\n{cliente} você pediu {total} Itens")

print(f"O valor total é de {total_valor}R$")