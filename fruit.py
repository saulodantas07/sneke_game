# fruit.py
import pygame
from random import randint
from settings import VERMELHO, LARGURA, ALTURA, ALTURA_PAINEL

class Moca:
    def __init__(self):
        self.tamanho = 20
        self.x = 0
        self.y = 0
        self.gerar_nova_posicao()

    def gerar_nova_posicao(self):
        self.x = randint(1, (LARGURA // 20) - 2) * 20
        self.y = randint(3, (ALTURA // 20) - 2) * 20

    def desenhar(self, tela):
        return pygame.draw.rect(tela, VERMELHO, (self.x, self.y, self.tamanho, self.tamanho))