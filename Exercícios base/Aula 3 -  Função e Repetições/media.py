soma = 0
nota = []

for x in range (0,6):
    notaUser = int(input(f'Digite a {x+1}º nota: \n'))
    nota.append(notaUser)

nota.pop(0)
nota.pop(-1)
print(nota)
for i in nota:
    print(f'aqui:  {i}')
    soma = soma + i
media = soma / (len(nota))
print(f'A média das notas é {media}')
