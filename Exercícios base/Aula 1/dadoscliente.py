# Crie um programa que peça os dados de um cliente: Nome, idade, nacionalidade, endereço. Após digitados os dados, mostrar na tela a seguinte mensagem "Cliente [Nome], com [idadeCliente] anos, [nacionalidadeCliente], reside no endereço [endereço]". Exemplo: Cliente Lucas, com 29 anos, brasileiro, reside no endereço Rua Victor Meirelles, 281, Centro, Florianópolis.


nomeCliente = input("Digite o nomeUser: ")
idadeCliente = int(input("Digite a idade: "))
nacionalidadeCliente = input("Digite a nacionalidade: ")
enderecoCliente = input("Digite o endereço: ")

texto = '''Cliente {}, com {} anos, {}, reside no endereço {}'''
print(texto.format(nomeCliente,idadeCliente,nacionalidadeCliente,enderecoCliente))