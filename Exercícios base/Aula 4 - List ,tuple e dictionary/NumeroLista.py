# Uma lista com números de 1 a 15 foi criada por engano, quando na verdade deveria ser apenas de 1 a 5. Desenvolver um programa que remova os números a mais para corrigi-la. Mostrar a lista corrigida na tela.

numeros = []

for x in range(1,16):
    numeros.append(x)

print(numeros)

for x in range(16, 0, -1):
    if x > 6:
        numeros.pop((len(numeros))- 1)

print(numeros)
