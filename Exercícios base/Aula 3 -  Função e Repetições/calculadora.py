# Criar uma calculadora utilizando funções para cada operação. O usuário deve digitar o primeiro número, o segundo número e em seguida a operação que deseja realizar (1 - Soma 2 - Subtração 3 - Multiplicação 4 - Divisão). O resultado deve ser mostrado na tela.

text = ""
primeiroNumero = float (input("Digite o primeiro número: "))
segundoNumero = float (input("Digite o segundo número: "))
operacaoInput = (input("Digite o simbolo da operação desejada:  \nSoma(+)\nSubtração(-)\nMultiplicação(*)\nDivisão(/)\nExponenciação(^) "))


def calculadora(a,b,operacao):
    match operacao:
        case "+": 
            return a+b
        
        case "-": 
            return a-b
        
        case "*": 
            return a*b
        
        case "/": 
            return a/b
       
        case "^": 
            return a**b
        
        case _:
            return "Operação indisponível"
 
print(f'Resultado: {calculadora(primeiroNumero, segundoNumero, operacaoInput)}')