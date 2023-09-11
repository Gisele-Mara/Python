# Crie um vetor de 10 números e peça para o usuário qual número ele deseja verificar se existe no vetor. Caso exista, o programa deve mostrar todos os índices que ele se encontra.
import random
posicao = []
vetor = []
for x in range(10):
    vetor.append(random.randrange(0,11))

print(f'Vetor:{vetor}')

elemento = int(input(f'Digite o número que deseja verificar: '))

for x in range(len(vetor)):
    if vetor[x] == elemento:
        posicao.append(x)

if elemento in vetor:       
    print(f'O número {elemento} está no vetor, no índice: {posicao}')
else:
    print(f'O número {elemento} não está no vetor')