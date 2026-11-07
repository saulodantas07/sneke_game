# main.py
import pygame
from sys import exit
from settings import LARGURA, ALTURA, ALTURA_PAINEL, VELOCIDADE
from snake import Cobra
from fruit import Moca
from ui import desenhar_placar, desenhar_cronometro, desenhar_tela_inicio, desenhar_tela_nome, desenhar_ranking
from background import GerenciadorFundo
from walls import desenhar_paredes
from ranking import salvar_pontuacao

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da Cobrinha Modularizado')
relogio = pygame.time.Clock()

pontos = 0
cobra = Cobra(LARGURA, ALTURA)
maca = Moca()
gerenciador_fundo = GerenciadorFundo()

# Estados do jogo: 'INICIO', 'JOGANDO', 'PEDINDO_NOME', 'RANKING'
estado_jogo = 'INICIO'
nome_jogador = ""

# Variáveis do cronómetro
tempo_inicio = 0
tempo_decorrido = 0

def iniciar_partida():
    global pontos, cobra, maca, estado_jogo, tempo_inicio
    pontos = 0
    cobra = Cobra(LARGURA, ALTURA)
    maca = Moca()
    estado_jogo = 'JOGANDO'
    tempo_inicio = pygame.time.get_ticks()

def reiniciar_jogo():
    global estado_jogo, nome_jogador
    nome_jogador = ""
    estado_jogo = 'INICIO'

while True:
    relogio.tick(30)
    
    if estado_jogo == 'INICIO':
        # Desenha a tela de início e guarda o retângulo do botão gerado
        ret_botao_jogar = desenhar_tela_inicio(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # Clicar com o rato no botão Jogar ou carregar em Enter/Espaço
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Clique esquerdo
                    if ret_botao_jogar.collidepoint(event.pos):
                        iniciar_partida()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    iniciar_partida()

    elif estado_jogo == 'JOGANDO':
        # 1. Camada de fundo e paredes
        gerenciador_fundo.desenhar(tela, pontos)
        desenhar_paredes(tela)

        # Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and cobra.x_controle != VELOCIDADE:
                    cobra.x_controle = -VELOCIDADE
                    cobra.y_controle = 0
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and cobra.x_controle != -VELOCIDADE:
                    cobra.x_controle = VELOCIDADE
                    cobra.y_controle = 0
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and cobra.y_controle != VELOCIDADE:
                    cobra.y_controle = -VELOCIDADE
                    cobra.x_controle = 0
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and cobra.y_controle != VELOCIDADE:
                    cobra.y_controle = VELOCIDADE
                    cobra.x_controle = 0

        # Atualiza o tempo decorrido em segundos
        tempo_decorrido = (pygame.time.get_ticks() - tempo_inicio) // 1000

        cobra.atualizar_movimento()

        # Colisão com as paredes
        if cobra.x < 20 or cobra.x >= LARGURA - 20 or cobra.y < ALTURA_PAINEL + 20 or cobra.y >= ALTURA - 20:
            estado_jogo = 'PEDINDO_NOME'

        ret_maca = maca.desenhar(tela)
        ret_cobra = pygame.Rect(cobra.x, cobra.y, 20, 20)

        # Colisão com a maçã
        if ret_cobra.colliderect(ret_maca):
            maca.gerar_nova_posicao()
            pontos += 1
            cobra.comprimento += 1

        # Colisão com o próprio corpo
        if cobra.verificar_colisao_propria():
            estado_jogo = 'PEDINDO_NOME'

        cobra.desenhar(tela)
        
        # Placar e cronómetro desenhados por último no painel superior
        desenhar_placar(tela, pontos)
        desenhar_cronometro(tela, tempo_decorrido)

    elif estado_jogo == 'PEDINDO_NOME':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    salvar_pontuacao(nome_jogador, pontos, tempo_decorrido)
                    estado_jogo = 'RANKING'
                elif event.key == pygame.K_BACKSPACE:
                    nome_jogador = nome_jogador[:-1]
                else:
                    if len(nome_jogador) < 10 and event.unicode.isprintable():
                        nome_jogador += event.unicode
                        
        desenhar_tela_nome(tela, nome_jogador)

    elif estado_jogo == 'RANKING':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reiniciar_jogo()
                    
        desenhar_ranking(tela)

    pygame.display.update()