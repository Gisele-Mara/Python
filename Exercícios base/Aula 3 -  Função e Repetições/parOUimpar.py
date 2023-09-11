# tilizando funções, fazer um sistema que receba um número e retorne se ele é par ou ímpar.

numeroInput = float(input("Digite um número: "))

def verifica(numero):
    if numero % 2 == 0:
        return print(f'O {numero} é par!')
    else:
        return print(f'O {numero} é ímpar!')
    
verifica(numeroInput)
