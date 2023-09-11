nomes = []
cores = ['Amarelo', 'Verde','Roxo','Verde','Vermelho', 'Azul']
idade = [1,8,22,4,6,8]
# corRemove = input("Cor a remover: ")

# for cor in cores:
    
#     if cor == corRemove:
#         corExiste = True
#         if corExiste == True:
#             cores.remove(corRemove)
#             print('Cor removida!')
#             print(cores)
#     else:
#         print('Cor não encontrada')

print(cores.count("Verde"))
print(cores.index("Roxo"))
# idade.extend(cores)
# print(idade)
idade.sort()
print(idade)
print(sum(idade))