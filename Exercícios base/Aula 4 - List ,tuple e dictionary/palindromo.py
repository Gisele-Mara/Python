# Palíndromo é aquele elemento que, se lido de trás para frente e de frete para trás, é o mesmo. Exemplos: 616, 2112 2442, 87655678. Criar um vetor onde deve-se digitar 6 números e verificar se o vetor é palíndromo. (DESAFIO: fazer com 7 números e com palavras).

vetor = [8,7,6,5,4,5,6,7,8]
direita = len(vetor)
palindromo = False

for x in range (len(vetor)):
    direita = direita - 1
    if vetor[x] == vetor[direita]:
        palindromo = True
    else:
       print(f'Não é palíndromo')
       palindromo = False
       break

if palindromo:
    print(f'É palíndromo!')