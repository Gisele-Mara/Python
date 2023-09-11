# Fazer um programa no qual o usuário digite a sua altura e o seu peso, ao final mostre o IMC (índice de massa corporal) e uma mensagem se está abaixo do peso (IMC menor que 18), na faixa de peso ideal (IMC de 18 a 25) ou acima do peso (IMC maior 25). IMC = peso / (altura * altura).

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite o sua altura: "))

imc = round((peso / altura**2),2)

if imc < 18:
    print(f'Seu IMC é {imc}. Você está abaixo peso!')
elif imc > 25:
    print(f'Seu IMC é {imc}. Você está acima peso!')
else: 
     print(f'Seu IMC é {imc}. Você está na faixa de peso ideal')
