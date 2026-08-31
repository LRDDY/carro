import pygame
from scripts.cone import Obstaculo
from scripts.jogador import Jogador
from scripts.interfaces import Texto, Botao

class Partida:
    def __init__(self, tela):
        self.tela = tela
        # Posiciona o carro perto da base inferior da tela
        self.jogador = Jogador(tela, tela.get_width() // 2 - 20, tela.get_height() - 90)
        self.obstaculo = Obstaculo(tela)
        self.estado = 'partida'
        
        self.pontosValor = 0
        self.contador = 0
        self.pontosTexto = Texto(tela, "Pontos: 0", 10, 10, (255, 255, 255), 30)

    def atualizar(self):
        self.estado = 'partida'
        self.jogador.atualizar()
        self.obstaculo.atualizar()

        # Contador de Pontos
        self.contador += 1
        if self.contador > 30:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizarTexto(f"Pontos: {self.pontosValor}")

        self.pontosTexto.desenhar()

        # Colisão
        if self.obstaculo.detectarColisao(self.jogador.getRect()):
            self.estado = "menu"
            # Reset do jogo
            self.jogador.posicao = [self.tela.get_width() // 2 - 20, self.tela.get_height() - 90]
            self.obstaculo.resetar_posicao()
            self.pontosValor = 0
            self.pontosTexto.atualizarTexto("Pontos: 0")

        self.jogador.desenhar()
        self.obstaculo.desenhar()

        return self.estado


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "Jogo do Carro", 150, 50, (255, 255, 255), 50)
        self.botao_jogar = Botao(tela, "Jogar", 240, 200, 50, (200, 0, 0), (255, 255, 255))
        self.estado = "menu"

    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()
        self.botao_jogar.desenhar()

        if self.botao_jogar.get_click():
            self.estado = "partida"

        return self.estado