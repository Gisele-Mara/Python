# Desenvolva um programa que o usuário digite 10 números positivos e inteiros, ao final  mostre o valor do resultado do somatório da primeira metade dos números menos o somatório da segunda metade. (Somatório da primeira metade - Somatório da segunda metade)
import random
primeiraMetade = 0
segundaMetade = 0
numero = []
for x in range(10):
    numero.append(random.randrange(1,20))
    print(numero[x])
    primeiraMetade = primeiraMetade + numero[x]
   
    if x > 5:
        segundaMetade = segundaMetade + numero[x]


print(f'Números= {numero}. Primeira metade = {primeiraMetade}; Segunda Metade = {segundaMetade}. Resultado = {primeiraMetade - segundaMetade}')