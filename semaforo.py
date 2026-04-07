semaforo = input("\nQual luz esta acesa? ")

if semaforo == 'verde':
    print("prosseguir")
elif semaforo == 'amarelo':
    print("reduza a velocidade")
elif semaforo == 'vermelho':
    print("Pare")
else:
    print("Cor Invalida")