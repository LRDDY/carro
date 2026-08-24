import pygame

from scripts.jogador import Jogador
from scripts.cone import Cone

pygame.init()

# Tamanho da tela
tamanhoTela = [1920, 1010]

tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("CAR GAME")

relogio = pygame.time.Clock()

corFundo = (86, 148, 214)

# Jogador
jog = Jogador(tela, 810, 600)

# 2 cones
cones = []

for i in range(2):
    cone = Cone(tela)

    # Coloca cada cone em uma faixa diferente
    cone.x = cone.linhas[i]

    # Separa os cones verticalmente
    cone.y = -500 - (i * 600)

    cones.append(cone)


while True:

    # Eventos
    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Fundo
    tela.fill(corFundo)

    # Jogador
    jog.atualizar()
    jog.desenhar()

    # Cones
    for cone in cones:
        cone.atualizar()
        cone.desenhar()

        # Colisão
        if cone.detectarColisao(jog.getRect()):
            print("BATEU!")

    pygame.display.flip()

    # 60 FPS
    relogio.tick(60)