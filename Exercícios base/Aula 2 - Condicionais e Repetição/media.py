# Crie um programa que peça ao usuário para digitar três notas individualmente (uma por vez), faça a média e caso a média seja igual ou maior que 7, mostre uma mensagem "Aprovado!" e a média. Caso seja menor que 7, mostre uma mensagem "Reprovado!" e a média.

notaUm = float(input("Digite a 1ª nota: "))
notaDois = float(input("Digite a 2ª nota: "))
notaTres = float(input("Digite a 3ª nota: "))

soma = notaUm + notaDois + notaTres
media = round((soma / 3),2)

if media >= 7:
    print(f'Aprovado com média {media}')
else: 
 print(f'Reprovado com {media}')
