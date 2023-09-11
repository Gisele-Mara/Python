# Criar um programa que pergunte o nome e a idade da pessoa, e se tem comorbidade (S ou N). Mostrar mensagem "Pode se vacinar!" caso a idade seja maior ou igual a 60 ou tenha comorbidade. Caso contrário, mostrar mensagem "Não pode se vacinar!".


nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
comorbidade = input("Tem comorbidade? Digite S ou N: ")


if idade >= 60 or comorbidade == 'S':
    print(f'Senhor(a) {nome}, pode se vacinar!')
else:
    print(f'Não pode se vacinar!')
