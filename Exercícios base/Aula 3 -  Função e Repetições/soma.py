# Acumular soma até que alcance ou ultrapasse 250
numero = 0
while numero < 250:

    numeroInput = int(input("Digite um número: "))
    numero= numero + numeroInput 
    print(f'{numero}')
else:
    print("Ultrapassou 250")