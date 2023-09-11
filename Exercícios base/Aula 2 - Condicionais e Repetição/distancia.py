#  Crie um algoritmo no qual seja digitado a distância percorrida em quilômetros, o tipo do carro e informe ao final a média de consumo estimado de combustível. Sabendo-se que um carro do tipo A faz 8km/litro, o carro do tipo B faz 12km/litro e o tipo C faz 9km/litro. Caso seja fornecido um tipo de carro inválido (diferente de A, B ou C) o algoritmo deve mostrar uma mensagem "Tipo de carro inválido!" e encerrar.

litro = 1
distanciaPercorrida = float(input("Digite a distância percorrida em quilometros: "))
tipoCarro = input("Digite o tipo do carro: ")

match tipoCarro:
    case "A": 
        consumo = (distanciaPercorrida * litro)/ 8 
        print(f'O carro {tipoCarro} consumiu em média {consumo} litros')
    case "B": 
        consumo = (distanciaPercorrida * litro)/ 12 
        print(f'O carro {tipoCarro} consumiu em média {consumo} litros')
    case "C": 
        consumo = (distanciaPercorrida * litro)/ 9 
        print(f'O carro {tipoCarro} consumiu em média {consumo} litros')
    case _: 
       print(f'Tipo de carro inválido')

    