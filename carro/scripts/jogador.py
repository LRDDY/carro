import pygame


class Jogador:
    def __init__(self, tela, x, y):
        self.tela = tela

        self.tamanho = [300, 300]

        imagem = pygame.image.load('assets/carro.png')
        imagem = pygame.transform.scale(imagem, self.tamanho)

        self.listaImagens = [imagem]
        self.imagemAtual = 0

        self.y = y

        # 3 faixas: esquerda, centro e direita
        self.linhas = [
            300,   # esquerda
            810,   # centro
            1320   # direita
        ]

        # Começa no centro
        self.linhaAtual = 1

        self.posicao = [
            self.linhas[self.linhaAtual],
            self.y
        ]

        self.rect = pygame.Rect(
            self.posicao,
            self.tamanho
        )

        # Para detectar apenas quando a tecla for apertada
        self.teclaAnteriorEsquerda = False
        self.teclaAnteriorDireita = False

    def desenhar(self):
        self.tela.blit(
            self.listaImagens[self.imagemAtual],
            self.posicao
        )

    def atualizar(self):
        teclas = pygame.key.get_pressed()

        esquerda = teclas[pygame.K_LEFT]
        direita = teclas[pygame.K_RIGHT]

        # Apertou esquerda
        if esquerda and not self.teclaAnteriorEsquerda:
            if self.linhaAtual > 0:
                self.linhaAtual -= 1

        # Apertou direita
        if direita and not self.teclaAnteriorDireita:
            if self.linhaAtual < 2:
                self.linhaAtual += 1

        # Atualiza a posição instantaneamente
        self.posicao[0] = self.linhas[self.linhaAtual]

        self.rect = pygame.Rect(
            self.posicao,
            self.tamanho
        )

        # Guarda o estado anterior das teclas
        self.teclaAnteriorEsquerda = esquerda
        self.teclaAnteriorDireita = direita

    def getRect(self):
        return self.rect