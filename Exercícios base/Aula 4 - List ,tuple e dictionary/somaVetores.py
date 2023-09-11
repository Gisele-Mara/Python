# Escreva um programa que leia dois vetores com 3 elementos cada e gere um terceiro vetor de 6 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Ao final o programa deverá mostrar os dois vetores originais e o terceiro vetor com os valores intercalados.

import random
vetorUm = []
vetorDois = []
for x in range(3):
    vetorUm.append(random.randrange(1,20))
    vetorDois.append(random.randrange(1,20))

vetorTres = vetorUm + (vetorDois)
print(f'Vetor Um = {vetorUm}. Vetor Dois = {vetorDois}. Vetor Três = {vetorTres}')