import pygame

class Jogador:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.posicao = [x, y]
        self.tamanho = [40, 70] # Ajustado para proporção do carro
        self.rect = pygame.Rect(self.posicao, self.tamanho)
        self.velocidade = 5
        
        imagem_original = pygame.image.load('assets/carro.png')
        self.imagem = pygame.transform.scale(imagem_original, self.tamanho)

    def desenhar(self):
        self.tela.blit(self.imagem, self.posicao)

    def atualizar(self):
        teclas = pygame.key.get_pressed()
        

        if teclas[pygame.K_LEFT] and self.posicao[0] > 0:
            self.posicao[0] -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.posicao[0] < self.tela.get_width() - self.tamanho[0]:
            self.posicao[0] += self.velocidade

        self.rect = pygame.Rect(self.posicao, self.tamanho)

    def getRect(self):
        return self.rect