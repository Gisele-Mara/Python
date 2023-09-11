# Importa biblioteca Pygame
import pygame
import random
import sys

# Inicializa a biblioteca
pygame.init()
pygame.font.init()
fonts = pygame.font.get_fonts()

#Define a fonte 
fontPontos = pygame.font.SysFont('didot.ttc',22)
fontGameover = pygame.font.Font('Bullpen3D.ttf',45)
fontTitulo = pygame.font.Font('Bullpen3D.ttf',65)

# Define cor branca para o fundo
corFundo = (255, 255, 255)
corPreto = (0,0,0)
corVermelho = (255,0,0)

# #Define a cor dos objetos
# jogadorCor = (0,0,0)
objetoCor = (186,90,100)
gasolinaCor = (238, 75, 43)

# Define o tamanho da tela Largura, Altura (em pixels)
tamanhoTela = (293, 700)

# Armazena método que contém o clock do jogo, em uma variável 
clock = pygame.time.Clock()

# Cria uma tela com o tamanho definido anteriormente
tela = pygame.display.set_mode(tamanhoTela)

# Define um título para a janela
pygame.display.set_caption("V&F! Desafio em Python >:/")



# Define posição inicial do jogador
posicaoX = 208
posicaoY = 550

objetoPosicaoX = 115
objetoPosicaoY = 200

# Define o tamanho do jogador
larguraJogador = 40
alturaJogador = 50
limiteEsquerda = 10
limiteDireita = 243

# Define o tamanho e posição do jogador e objetos - Rect(left, top, width, height)
jogador = pygame.Rect(posicaoX, posicaoY, 0, 0)
objeto = pygame.Rect(objetoPosicaoX, objetoPosicaoY, 0, 0)
objeto2 = pygame.Rect(15, 115, 0, 0)
gasolina = pygame.Rect(15, 550, 0, 0)


# Carrega a imagem dos objetos
carro_img = pygame.image.load("carrocorrida.jpg")
carro_img = pygame.transform.scale(carro_img, (60, 80))
objeto_img =pygame.image.load('obj.jpg')
objeto_img = pygame.transform.scale(objeto_img, (60, 60))
gasolina_img = pygame.image.load('gas.jpg')
gasolina_img = pygame.transform.scale(gasolina_img, (30, 40))
objeto2_img = pygame.image.load('policia.jpg')
objeto2_img = pygame.transform.scale(objeto2_img, (100, 80))



objetoPosicoes = [15,115,208]
# Define a velocidade do jogador  e objetos
jogadorVelocidade = 0
velocidadeObjeto = 1

aceleracao = 5
tempo = 60
pontos = 0
textoGameover= fontGameover.render(f'', False, ((0,0,0)) )
textoTitulo= fontTitulo.render(f'Velozes e Furiosos! \nDesafio em Python ', True, ((0,0,0)) )

# calculate exit time: 5000ms = 5s
    
current_time = pygame.time.get_ticks()
exit_time = 5000

# Define variável de jogo rodando para verdadeiro
gameRun = True
# Define status de jogo para "Rodando"
while gameRun:

    
    ### Movimentação Objetos ###
    velocidadeObjeto+= 0.05
    objeto.y = objeto.y + velocidadeObjeto
    objeto2.y = objeto2.y + velocidadeObjeto
    gasolina.y = gasolina.y + velocidadeObjeto

    if objeto.y >= 700:
        objeto.y = 0
        aceleracao = aceleracao+ 0.10
        velocidadeObjeto = aceleracao
        objeto.x = objetoPosicoes[(random.randrange(0,3))]

    if objeto2.y >= 700:
        objeto2.y = 0
        objeto2.x = objetoPosicoes[(random.randrange(0,3))]

    if gasolina.y >= 700:
        gasolinaRandom = (random.randrange(0,100))
        if gasolinaRandom >= 0 and gasolinaRandom <=2:
            gasolina.x = objetoPosicoes[gasolinaRandom]
            gasolina.y = 0
        
    #Taxa de tempo
    tempoRec= pygame.Rect(210, 30, tempo, 20)
    tempo = tempo - 0.05
    
    ## MENSAGEM NA TELA
    #Pontos
    textoTela = fontPontos.render(f'Pontos: {pontos} ', True, ((0,0,0)) )

    # Condição para aumentar o tempo(tocar na gasolina):   
    if jogador.x == gasolina.x and (gasolina.y > 550 and gasolina.y < 600):
        tempo = 60

    #Aumento da pontuação 
        pontos = pontos + 1
   
    # Game over
    if jogador.x == objeto.x and (objeto.y > 550 and objeto.y < 600):
        clock.tick(3)
        textoGameover= fontGameover.render(f'GAME\nOVER', True, corVermelho )
        current_time = pygame.time.get_ticks()
        if current_time >= exit_time:
            gameRun = False
    if jogador.x == objeto2.x and (objeto2.y > 550 and objeto2.y < 600):
        clock.tick(3)
        textoGameover= fontGameover.render(f'GAME\nOVER', True, corVermelho)
        if current_time >= exit_time:
            gameRun = False
            
   
    if tempo <= 0:
        textoGameover= fontGameover.render(f'GAME\nOVER', True, corVermelho)
        if current_time >= exit_time:
            gameRun = False
    
    # Define loop para verificar eventos na Pygame
    for event in pygame.event.get():
        ##### Movimentação objeto ######
       
        # Se o evento for igual a QUIT, finaliza o jogo
        if event.type == pygame.QUIT:
            pygame.quit()

           
        
        # Se o evento for de tecla pressionada
        if event.type == pygame.KEYDOWN:

            # Se a tecla pressionada for SETA ESQUERDA
            if event.key == pygame.K_LEFT:
              
                if jogador.x > 97 and jogador.x < 190:
                    jogador.x = 15
                  
                if jogador.x > 190 and jogador.x < 283:
                    jogador.x = 115
                # Movimenta o jogador para esquerda
                jogadorVelocidade = jogadorVelocidade - 5

            # Se a tecla pressionada for SETA DIREITA
            if event.key == pygame.K_RIGHT:
                    
                if jogador.x >= 97 and jogador.x <= 190:
                    jogador.x = 208
                    
                if jogador.x > 10 and jogador.x < 97:
                    jogador.x = 115
             
         # Se o evento for de tecla soltada
        if event.type == pygame.KEYUP:
            objeto.y = objeto.y + 1
            # Se a tecla pressionada for SETA ESQUERDA
            if event.key == pygame.K_LEFT:
           

                # Movimenta o jogador para esquerda
                jogadorVelocidade = jogadorVelocidade + 5

            # Se a tecla pressionada for SETA DIREITA
            if event.key == pygame.K_RIGHT:

                # Movimenta o jogador para direita
                jogadorVelocidade = jogadorVelocidade - 5

    # Atualiza a posição do jogador de acordo com a velocidade
     
        
    # jogador.x = jogador.x + jogadorVelocidade

    # Limitação de movimento ------------
    if jogador.x < 10:
        jogador.x = limiteEsquerda
    if jogador. x >= 243:
        jogador.x = limiteDireita
        
   

  

##### Área para desenhos ##### 
# # Define preenchimento da tela com a cor de fundo
    tela.fill(corFundo) 
    
# Desenha o jogador e objetos na tela
    tela.blit(carro_img, jogador)
    tela.blit(objeto_img, objeto)
    tela.blit(objeto2_img, objeto2)
    tela.blit(gasolina_img, gasolina)

    tela.blit(textoTela,((15),(30)))
    tela.blit(textoGameover,((208/2),(700/2)))
 # # Desenha o jogador na tela a cada tick, de acordo com os dados do jogador
    pygame.draw.rect(tela, (0,0,0), jogador)

#Objetos
    pygame.draw.rect(tela, objetoCor, objeto)
    pygame.draw.rect(tela, objetoCor, objeto2)
    pygame.draw.rect(tela, gasolinaCor, gasolina)
    pygame.draw.rect(tela, (0,0,0), tempoRec)


# Limites pista
    pygame.draw.line(tela, corPreto,(10, 10), (10, 700))
    pygame.draw.line(tela, corPreto,(390, 10), (390, 700))

# Pista 
    pygame.draw.line(tela, corPreto,(97, 10), (97, 700))
    pygame.draw.line(tela, corPreto,(190, 10), (190, 700))
    pygame.draw.line(tela, corPreto,(283, 10), (283, 700))

##### Área para desenhos #####

    # Atualiza a tela de acordo com o clock
    pygame.display.update()

    # Define a taxa de renderização (FPS) 
    clock.tick(60)

 

# Finaliza o jogo
pygame.quit()