import pygame
import random

class Obstaculo:
    def __init__(self, tela):
        self.tela = tela
        self.tamanho = [40, 40]
        self.imagem_original = pygame.image.load('assets/cone.png')
        self.imagem = pygame.transform.scale(self.imagem_original, self.tamanho)
        
        self.velocidade = 5
        self.resetar_posicao()

    def resetar_posicao(self):

        self.x = random.randint(0, self.tela.get_width() - self.tamanho[0])
        self.y = -self.tamanho[1]

    def atualizar(self):
        self.y += self.velocidade

        if self.y > self.tela.get_height():
            self.resetar_posicao()

    def desenhar(self):
        self.tela.blit(self.imagem, (self.x, self.y))

    def detectarColisao(self, rectJogador):
        rectObstaculo = pygame.Rect((self.x, self.y), self.tamanho)
        return rectJogador.colliderect(rectObstaculo)