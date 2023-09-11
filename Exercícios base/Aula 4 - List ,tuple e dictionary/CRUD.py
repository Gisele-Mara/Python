vetor = []
inputUser = 0
while inputUser != 5:
    inputUser = int(input(f'Escolha umas das opções: \n1.Cadastrar usuário \n2.Editar usuário \n3.Excluir \n4.Listar \n5.Sair\n'))
    match inputUser:
        case 1:
          cadastro = input(f'Digite o nome para cadastrar: ')
          vetor.append(cadastro)
        case 2:
            nomeEditar = input(f'Digite qual nome deseja editar: ')
            if nomeEditar in vetor:
                indice = vetor.index(nomeEditar)
                print(indice)
                vetor[indice] = input("Digite o novo nome: ")
                print(f'{nomeEditar} foi adicionado a lista de cadastro')
            else:
                print(f' O nome {nomeEditar} não está cadastrado')
        case 3:
            nomeExcluir = input(f'Digite o nome que deseja excluir: ')
            if nomeExcluir in vetor:
                indice = vetor.index(nomeExcluir)
                vetor.pop(indice)
                print(f'{nomeExcluir} foi removido da lista de cadastro')
            else:
                 print(f' O nome {nomeExcluir} não está cadastrado')
        case 4:
            print(f'Usuários cadastrados {vetor}')
        case 5:
            print(f'Adeus!')
        case _:
            print(f'Opção inválida')
