# walls.py
import pygame
from settings import LARGURA, ALTURA, ALTURA_PAINEL

def desenhar_paredes(tela):
    COR_TIJOLO = (178, 34, 34)     
    COR_ARGAMASSA = (211, 211, 211) 
    
    espessura = 20
    

    pygame.draw.rect(tela, (30, 30, 30), (0, 0, LARGURA, ALTURA_PAINEL))
    
 
    pygame.draw.rect(tela, COR_ARGAMASSA, (0, ALTURA_PAINEL, LARGURA, espessura))                 
    pygame.draw.rect(tela, COR_ARGAMASSA, (0, ALTURA - espessura, LARGURA, espessura))            
    pygame.draw.rect(tela, COR_ARGAMASSA, (0, ALTURA_PAINEL, espessura, ALTURA - ALTURA_PAINEL))   
    pygame.draw.rect(tela, COR_ARGAMASSA, (LARGURA - espessura, ALTURA_PAINEL, espessura, ALTURA - ALTURA_PAINEL)) 
    
    # Tijolinhos nas bordas horizontais
    for x in range(0, LARGURA, 40):
        pygame.draw.rect(tela, COR_TIJOLO, (x + 2, ALTURA_PAINEL + 2, 36, espessura - 4))
        pygame.draw.rect(tela, COR_TIJOLO, (x + 22, ALTURA - espessura + 2, 36, espessura - 4))
        
    # Tijolinhos nas bordas verticais
    for y in range(ALTURA_PAINEL, ALTURA, 40):
        pygame.draw.rect(tela, COR_TIJOLO, (2, y + 2, espessura - 4, 36))
        pygame.draw.rect(tela, COR_TIJOLO, (LARGURA - espessura + 2, y + 22, espessura - 4, 36))