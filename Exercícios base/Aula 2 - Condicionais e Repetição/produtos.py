# Em um determinado e-commerce, o frete para produtos possui o valor fixo de R$12,50. A loja possui benefícios para assinantes em três categorias: 1) Assinante Premium, ganha 20% de desconto e frete grátis 2) Assinante Gold, ganha 20% de desconto mas paga frete 3) Assinante Silver, ganha 10% de desconto mas paga frete. 4) Não assinante, sem benefícios. Faça um programa que solicite o valor da compra e a categoria de assinante (1, 2, 3 ou 4). Mostrar na tela o valor da compra de acordo com a opção escolhida.


frete = 12.50
valorCompra = float(input("Digite o valor da compra: "))
categoriaAssinante = int(input(f'Digite a categoria assinante: \n1) Assinante Premium\n2) Assinante Gold\n3) Assinante Silver\n4) Não assinante \n'))

match categoriaAssinante:
    case 1:
        total = valorCompra - ((valorCompra * 20)/100)
        print(f'O valor total da compra na categoria é {total} reais.')
    case 2:
        total = valorCompra + frete - ((valorCompra * 20)/100) 
        print(f'O valor total da compra na categoria é {total} reais.')
    case 3:
        total = valorCompra + frete - ((valorCompra * 10)/100) 
        print(f'O valor total da compra na categoria é {total} reais.')
    case 4:
        total = valorCompra + frete
        print(f'O valor total da compra é {total} reais.')
    case _:
        
        print(f'O pção inválida.')
    