# background.py
import pygame
import os
from settings import LARGURA, ALTURA, BRANCO

class GerenciadorFundo:
    def __init__(self):
        self.imagens = []
        
      
        caminhos = [
            'assets/fundo_1.png',
            'assets/fundo_2.png',
            'assets/fundo_3.png',
            'assets/fundo_4.png',
            'assets/fundo_5.png',
            'assets/fundo_6.png'
        ]

        # Carrega todas as imagens que existirem na pasta
        for caminho in caminhos:
            if os.path.exists(caminho):
                try:
                    img = pygame.image.load(caminho)
                    self.imagens.append(pygame.transform.scale(img, (LARGURA, ALTURA)))
                except Exception as e:
                    print(f"Erro ao carregar a imagem '{caminho}': {e}")
            else:
                print(f"Aviso: O arquivo '{caminho}' não foi encontrado!")

    def desenhar(self, tela, pontos):
        if self.imagens:
            # A cada 5 pontos muda de fundo
            intervalo_pontos = 5
            
            # Alterna ciclicamente entre as imagens disponíveis (de 1 a 6)
            indice = (pontos // intervalo_pontos) % len(self.imagens)
            
            tela.blit(self.imagens[indice], (0, 0))
        else:
            # Fallback caso nenhuma imagem seja encontrada
            tela.fill(BRANCO)