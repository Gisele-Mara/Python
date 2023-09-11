#  Fazer um programa no qual o usuário deve montar uma salada de frutas com uma cereja no final. Deve ser perguntado em sequência “Qual fruta adicionar?”. Quando for adicionado a cereja, finalizar com a frase “Sua salada de frutas está pronta!”. Mostrar a lista das frutas

saladaFruta = []
frutaAdd = ""
while frutaAdd != "cereja":
    frutaAdd = input("Digite a fruta a adicionar: ")
    saladaFruta.append(frutaAdd)
else:
    print(f'“Sua salada de frutas está pronta! {saladaFruta}')