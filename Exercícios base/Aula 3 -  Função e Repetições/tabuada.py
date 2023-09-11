#  Faça um programa que leia um valor inteiro e mostre na tela a tabuada de 1 a 10 do valor lido.

numero = int(input("Digite o número: "))

for x in range (1, 11):
    tabuada = numero * x
    print(f'{numero} x {x} = {tabuada}')

