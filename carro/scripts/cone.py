import pygame
import random


class Cone:
    def __init__(self, tela):
        self.tamanho = [300, 300]

        self.imagem = pygame.image.load('assets/cone.png')
        self.imagem = pygame.transform.scale(
            self.imagem,
            self.tamanho
        )

        self.tela = tela

        # 3 faixas
        self.linhas = [300, 810, 1320]

        # Escolhe uma faixa
        self.x = random.choice(self.linhas)

        # Começa acima da tela
        self.y = random.randint(
            -1500,
            -300
        )

        # Velocidade maior
        self.velocidade = 8

    def atualizar(self):
        self.y += self.velocidade

        # Se sair da tela
        if self.y > self.tela.get_height():

            self.y = random.randint(-1200, -300)

            self.x = random.choice(self.linhas)

    def desenhar(self):
        self.tela.blit(
            self.imagem,
            (self.x, self.y)
        )

    def detectarColisao(self, rectJogador):
        rectCone = pygame.Rect(
            (self.x, self.y),
            self.imagem.get_size()
        )

        return rectJogador.colliderect(rectCone)