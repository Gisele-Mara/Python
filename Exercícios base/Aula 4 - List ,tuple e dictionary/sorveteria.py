sorvete = []
sabor = False

userInput = 0
print("Olá, seja bem-vindo a sorveteria!")
while userInput != 4:
    userInput = int(input(f'Escolha uma das opções: \n1.Adicionar sabor \n2.Remover sabor \n3.Visualizar sorvete \n4.Finalizar pedido \n')) 

    match userInput:
        case 1:
            numerosSabores = len(sorvete)
            if numerosSabores < 4:
                saborAdd = (input(f'Digite o {numerosSabores + 1}º sabor do sorvete: ')).upper()
                sorvete.append(saborAdd)
                sabor = True
                print(f'O sabor {saborAdd} foi adicionado')
            else:
                print(f'Limite de sabores atingido, remova um sabor!')

        case 2:
            saborRemover = (input(f'Que sabor deseja remover?')).upper()
            if saborRemover in sorvete:
                indice = sorvete.index(saborRemover)
                if indice == (len(sorvete) - 1):            
                    sorvete.pop(indice)
                    print(f'O sabor {saborRemover} foi removido!')
                else:
                    print(f'\n O sabor{saborRemover} está na {indice + 1}ª camada.Não é possível remover esse o sabor, pois ele não está na última camada.')
            else:
                print(f'O sabor {saborRemover} não está no sorvete')
        case 3:
            if sabor:
                print(f'Seu sorvete está com esses sabores: {sorvete}')
            else:
                print(f'\nSeu sorvete não possui sabores!\n')
        case 4:
            if sabor:
                print(f'\nPedido finalizado! Sorvete com: {sorvete}')
            else:
                print(f'\nO seu sorvete está sem sabores. Adicione pelo menos um sabor!\n')
                userInput = 0
        case _:
            print(f'\nOpção inválida.\n')