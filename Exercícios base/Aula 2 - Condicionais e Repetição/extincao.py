# Elaborar um programa que alerte sobre os riscos de animais em extinção. O usuário deve digitar o nome da espécie e a sua população (total de indivíduos). Populações entre 200 e 500 indivíduos, são classificadas como "Espécie criticamente em perigo", populações entre 500 e 1000 indivíduos, são classificadas como "Espécie em perigo" e populações entre 1000 e 5000 indivíduos, são classificadas como "Espécie vulnerável!"

nomeEspecie = input("Digite o nome da especie: ")
população = input(f'Digite o total de indivíduos {nomeEspecie}: ')


if população >= 200 and população < 500:
    print(f'A Espécie de {nomeEspecie} está criticamente em perigo')
elif população >= 500 and população < 1000:
    print(f'A Espécie de {nomeEspecie} está  em perigo')
if população >= 1000 and população < 5000:
    print(f'A Espécie de {nomeEspecie} está  vulnerável')
if população >= 5000:
    print(f'A Espécie de {nomeEspecie} está ok!')
else: 
    print(f'A Espécie de {nomeEspecie} está em extinção')
