# Em uma festa de família alemã, 45 pessoas foram convidadas para beber. Para tanto, foram comprados 300 litros de chopp. Criar um programa que calcule a média de litros bebidos por pessoa, considerando ainda a quantidade de chopp (litros) desperdiçado e a quantidade de chopp (litros) que sobrou. Esses dados devem ser digitados pelo usuário. Caso não tenha havido desperdício e não tenha sobrado chopp, digitar 0 para ambos. Ao final, mostrar a média de litros bebidos por pessoa na festa.


totalPessoas = 45
totalChopp = 300

litrosDesperdicado = float(input("Quantos litros de Chopp foram desperdiçados? "))
litrosRemanescente = float(input("Quantos litros de Chopp sobrou? "))

litrosConsumidos = totalChopp - litrosDesperdicado - litrosRemanescente
print(litrosConsumidos)
media = litrosConsumidos / totalPessoas

print("A média de litros bebidos por pessoa foi", round(media,2))