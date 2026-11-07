# snake.py
import pygame
from settings import VERDE, LARGURA, ALTURA, ALTURA_PAINEL

class Cobra:
    def __init__(self, largura, altura):
        self.x = largura // 2
        self.y = (altura + ALTURA_PAINEL) // 2
        self.tamanho_bloco = 20
        self.lista_corpo = []
        self.comprimento = 5
        self.x_controle = 10
        self.y_controle = 0

    def atualizar_movimento(self):
        self.x += self.x_controle
        self.y += self.y_controle

        cabeca = [self.x, self.y]
        self.lista_corpo.append(cabeca)
        if len(self.lista_corpo) > self.comprimento:
            del self.lista_corpo[0]

    def desenhar(self, tela):
        for bloco in self.lista_corpo:
            pygame.draw.rect(tela, VERDE, (bloco[0], bloco[1], self.tamanho_bloco, self.tamanho_bloco))

    def verificar_colisao_propria(self):
        cabeca_atual = [self.x, self.y]
        return self.lista_corpo[:-1].count(cabeca_atual) > 0