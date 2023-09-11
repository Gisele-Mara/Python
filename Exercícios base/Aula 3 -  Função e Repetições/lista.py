nomes = []
cores = ['Amarelo', 'Verde','Roxo','Verde','Vermelho', 'Azul']

print(max(cores))

corAdd = input("Cor a adicionar: ")
cores.append(corAdd)

for i in range (len(cores)):
    if i == (len(cores) - 1):
        print(f'{cores[-1]}')


cores.pop(0)
print(cores)