# Crie um programa que leia três lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno. Quando os três lados forem iguais trata-se de um triângulo equilátero, dois lados iguais é um triângulo isósceles e os três lados diferentes é um triângulo escaleno.

ladoAB = int(input("Digite o a medida do lado AB do triângulo: "))
ladoBC = int(input("Digite o a medida do lado BC do triângulo: "))
ladoCA = int(input("Digite o a medida do lado CA do triângulo: "))

if ladoAB == ladoBC and ladoAB == ladoCA:
    print(f'O triângulo é equilátero')
elif ladoAB == ladoBC or ladoAB == ladoCA or ladoBC == ladoCA:
    print(f'O triângulo é isósceles')
else:
    print(f'O triângulo é escaleno')
