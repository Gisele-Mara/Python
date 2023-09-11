#  Criar um programa para calcular a densidade demográfica (habitantes por quilômetro quadrado) de uma região. Sendo, densidade igual a população (total de habitantes) dividida pela área (metros quadrados). Mostrar mensagens para densidade alta (maior ou igual a 100), média (entre 25 e 100), baixa (menor que 25).


populacao = int (input("Digite o total de habitante da região:  "))
area = float(input("Digite a área total da região:  "))

densidade = populacao / area

if densidade >= 100:
    print(f'A densidade demográfica da régiao é {densidade} e é considerada uma densidade alta.')
if densidade < 25:
    print(f'A densidade demográfica da régiao é {densidade} e é considerada uma densidade baixa.')
else:
   print(f'A densidade demográfica da régiao é {densidade} e é considerada uma densidade média.')