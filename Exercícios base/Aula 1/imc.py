# Criar um programa que calcule o IMC, no qual o usuário deve digitar o seu peso e altura, realizar o cálculo (peso / altura * altura) e mostrar o resultado na tela, com 3 casas depois da vírgula.

pesoUser = float(input("Digite o seu peso: "))
alturaUser = float(input("Digite o seu peso: "))

imc = round(pesoUser / (alturaUser*alturaUser),3)

print("O IMC é", imc)