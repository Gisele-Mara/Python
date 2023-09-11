# Faça um programa que solicite ao usuário digitar 5 números e mostre a soma da multiplicação dos números pelo maior número digitado. (Exemplo: pegar os 4 números digitados que não são o maior e multiplicá-los individualmente pelo maior. Mostrar a soma das multiplicações).
import random
soma = 0
numero= []
for x in range(5):
    numero.append(random.randrange(1,21))

numero.sort()
print(numero)
numeroMaior = max(numero)
for x in range((len(numero))):
    # print(x)
    if x < len(numero) - 1:
        soma = soma + (numeroMaior * numero[x] )
        print(f'{numeroMaior} * {numero[x]} = {soma}')


print(f'Soma das multiplicações = {soma}')

