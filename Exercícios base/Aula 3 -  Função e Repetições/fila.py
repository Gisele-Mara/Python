fila = []
numeroFila = 0
nomePessoa = ''
while numeroFila < 5:
    nomePessoa = input("Digite o nome da pessoa\n")
    escolha = int(input("Escolha uma opção: \n1.Entrou pessoa \n2.Saiu pessoa"))
    
    match escolha:
        case 1:
            print("Entrou uma pessoa")
            fila.append(nomePessoa)
            numeroFila = numeroFila + 1
            print(fila)
        case 2:
            if nomePessoa in fila: #Se tem nome na fila
                print("Saiu uma pessoa")
                fila.remove(nomePessoa)
                numeroFila = numeroFila - 1
                print(fila)    
            else:
                print(f'{nomePessoa} não está na lista')
else: 
    print(f'Fila cheia! Ordem: {fila}')