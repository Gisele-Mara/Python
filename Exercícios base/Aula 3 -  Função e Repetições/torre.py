#  Em um jogo de Tower Defense, o castelo (torre) tem um total de 500 de HP. Faça um programa no qual o usuário possa escolher entre 3 tipos de ataque e um de defesa:

# 1) Ataque Bomba -100HP
# 2) Ataque Granada -80HP
# 3) Ataque Arqueiro -40HP
# 4) Defesa Escudo +20HP

# Mostrar o HP do castelo atualizado a cada rodada. Caso o HP do castelo acabe, mostrar "Jogo encerrado, com X rodadas!"

hpTotal = 500
rodadas = 0

while hpTotal > 0:
    escolha = int(input("Digite a jogada: \n1) Ataque Bomba -100HP \n2) Ataque Granada -80HP\n3) Ataque Arqueiro -40HP\n4) Defesa Escudo +20HP\n"))

    match escolha:
        case 1:
            hpTotal = hpTotal - 100
            print(f'\nPerdeu 100 de HP! HP total: {hpTotal}')
            rodadas = rodadas + 1
        case 2:
             hpTotal = hpTotal - 80
             print(f'\nPerdeu 80 de HP! HP total: {hpTotal}')
             rodadas = rodadas + 1
        case 3:
             hpTotal = hpTotal - 40
             print(f'\nPerdeu 40 de HP! HP total: {hpTotal}')
             rodadas = rodadas + 1
        case 4:
            hpTotal = hpTotal + 20
            print(f'\nGanhou 20 de HP! HP total: {hpTotal}')
            rodadas = rodadas + 1
        case _ :
            print("\nOpção inválida!")
else:
    print(f'Jogo encerrado, com {rodadas} rodadas')

    