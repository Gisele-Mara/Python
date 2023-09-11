# Desenvolva um programa no qual o usuário deve digitar o nome e a idade de 5 pessoas. Ao final mostrar a soma das idades e a média das idades.
somaIdade = 0
i = 0
while i < 5:
    nome = input(f'Digite o nome da {i+1}º pessoa: ')
    idade= int( input(f'Digite a idade da {i+1}º pessoa: '))
    somaIdade = somaIdade + idade
    i = i + 1

media = round (( somaIdade/5), 2)

print(f'A soma das idades é {somaIdade} anos e a média é {media} anos')