# ui.py
import pygame
import os
from settings import PRETO, ALTURA_PAINEL, LARGURA, ALTURA
from ranking import carregar_ranking

# Caches para carregar as imagens apenas uma vez
_img_inicio = None
_img_game_over = None

def desenhar_tela_inicio(tela):
    global _img_inicio
    if _img_inicio is None:
        caminho = 'assets/tela_inicio.png'
        if os.path.exists(caminho):
            try:
                _img_inicio = pygame.transform.scale(pygame.image.load(caminho), (LARGURA, ALTURA))
            except Exception as e:
                print(f"Erro ao carregar a imagem da tela de início: {e}")
                _img_inicio = None

    if _img_inicio:
        tela.blit(_img_inicio, (0, 0))
    else:
        tela.fill((40, 40, 80))

    largura_botao = 220
    altura_botao = 60
    x_botao = (LARGURA - largura_botao) // 2
    y_botao = (ALTURA // 2) + 60

    ret_botao = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)
    
    pygame.draw.rect(tela, (0, 180, 0), ret_botao, border_radius=12)
    pygame.draw.rect(tela, (255, 255, 255), ret_botao, 3, border_radius=12)

    fonte = pygame.font.SysFont('arial', 30, bold=True)
    texto_botao = fonte.render('JOGAR', True, (255, 255, 255))
    ret_texto = texto_botao.get_rect(center=ret_botao.center)
    tela.blit(texto_botao, ret_texto)

    return ret_botao

def desenhar_placar(tela, pontos):
    fonte = pygame.font.SysFont('arial', 26, bold=True)
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, PRETO)
    
    x = 20
    y = (ALTURA_PAINEL - texto_formatado.get_height()) // 2
    ret_texto = texto_formatado.get_rect(topleft=(x, y))
    
    padding = 6
    ret_fundo = pygame.Rect(
        ret_texto.x - padding, 
        ret_texto.y - padding, 
        ret_texto.width + (padding * 2), 
        ret_texto.height + (padding * 2)
    )
    
    pygame.draw.rect(tela, (255, 255, 255), ret_fundo)
    pygame.draw.rect(tela, PRETO, ret_fundo, 2)
    
    tela.blit(texto_formatado, ret_texto)

def desenhar_cronometro(tela, segundos):
    fonte = pygame.font.SysFont('arial', 26, bold=True)
    minutos = segundos // 60
    segs = segundos % 60
    mensagem = f'Tempo: {minutos:02d}:{segs:02d}'
    texto_formatado = fonte.render(mensagem, True, PRETO)
    
    y = (ALTURA_PAINEL - texto_formatado.get_height()) // 2
    padding = 6
    
    largura_texto = texto_formatado.get_width()
    altura_texto = texto_formatado.get_height()
    
    x = LARGURA - largura_texto - 20 - padding
    
    ret_fundo = pygame.Rect(
        x - padding, 
        y - padding, 
        largura_texto + (padding * 2), 
        altura_texto + (padding * 2)
    )
    
    pygame.draw.rect(tela, (255, 255, 255), ret_fundo)
    pygame.draw.rect(tela, PRETO, ret_fundo, 2)
    
    tela.blit(texto_formatado, (x, y))

def desenhar_tela_nome(tela, nome_atual):
    global _img_game_over
    if _img_game_over is None:
        caminhos = ['assets/game_over.png', 'assets/game over.png']
        for caminho in caminhos:
            if os.path.exists(caminho):
                try:
                    _img_game_over = pygame.transform.scale(pygame.image.load(caminho), (LARGURA, ALTURA))
                    break
                except Exception as e:
                    print(f"Erro ao carregar a imagem de game over: {e}")

    # Desenha a imagem de fundo ou cor sólida de segurança
    if _img_game_over:
        tela.blit(_img_game_over, (0, 0))
    else:
        tela.fill((30, 30, 30))

    # Painel translúcido centralizado para destacar os textos sobre a imagem de fundo
    painel_w, painel_h = 460, 250
    painel_x = (LARGURA - painel_w) // 2
    painel_y = 120
    
    s = pygame.Surface((painel_w, painel_h), pygame.SRCALPHA)
    s.fill((0, 0, 0, 200)) # Fundo preto com transparência para isolar o texto
    tela.blit(s, (painel_x, painel_y))
    
    # Borda branca ao redor do painel
    pygame.draw.rect(tela, (255, 255, 255), (painel_x, painel_y, painel_w, painel_h), 2, border_radius=10)

    # Fontes
    fonte_titulo = pygame.font.SysFont('arial', 38, bold=True)
    fonte_instrucao = pygame.font.SysFont('arial', 18, bold=True)
    fonte_input = pygame.font.SysFont('arial', 26, bold=True)
    
    # Textos com alto contraste e destaque
    texto_sombra = fonte_titulo.render('FIM DE JOGO', True, (0, 0, 0))
    texto_titulo = fonte_titulo.render('FIM DE JOGO', True, (255, 50, 50)) # Vermelho vivo bem destacado
    
    texto_instrucao = fonte_instrucao.render('Digite o seu nome e pressione ENTER:', True, (255, 255, 255)) # Branco puro
    texto_nome = fonte_input.render(nome_atual + '_', True, (0, 255, 0)) # Verde brilhante
    
    # Renderiza o título com sombra no painel
    tela.blit(texto_sombra, (LARGURA // 2 - texto_titulo.get_width() // 2 + 2, painel_y + 22))
    tela.blit(texto_titulo, (LARGURA // 2 - texto_titulo.get_width() // 2, painel_y + 20))
    
    # Renderiza a instrução
    tela.blit(texto_instrucao, (LARGURA // 2 - texto_instrucao.get_width() // 2, painel_y + 90))
    
    # Caixa de texto dedicada para o nome
    caixa_w, caixa_h = 300, 42
    caixa_x = (LARGURA - caixa_w) // 2
    caixa_y = painel_y + 135
    
    pygame.draw.rect(tela, (20, 20, 20), (caixa_x, caixa_y, caixa_w, caixa_h), border_radius=6)
    pygame.draw.rect(tela, (0, 255, 0), (caixa_x, caixa_y, caixa_w, caixa_h), 2, border_radius=6)
    
    ret_nome = texto_nome.get_rect(center=(caixa_x + caixa_w // 2, caixa_y + caixa_h // 2))
    tela.blit(texto_nome, ret_nome)

def desenhar_ranking(tela):
    tela.fill((30, 30, 30))
    fonte_titulo = pygame.font.SysFont('arial', 28, bold=True)
    fonte_item = pygame.font.SysFont('arial', 20, bold=True)
    
    titulo = fonte_titulo.render(' TOP 5 MELHORES JOGADORES ', True, (255, 215, 0))
    tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 40))
    
    ranking = carregar_ranking()
    
    cabecalho = fonte_item.render('Pos | Nome       | Pontos | Tempo', True, (200, 200, 200))
    tela.blit(cabecalho, (LARGURA // 2 - 150, 100))
    pygame.draw.line(tela, (200, 200, 200), (LARGURA // 2 - 150, 125), (LARGURA // 2 + 150, 125), 2)
    
    y = 140
    for i, reg in enumerate(ranking):
        minutos = reg['tempo'] // 60
        segs = reg['tempo'] % 60
        tempo_str = f'{minutos:02d}:{segs:02d}'
        
        nome_formatado = reg['nome'][:10].ljust(10)
        linha_texto = f"{i+1}º  | {nome_formatado} | {str(reg['pontos']).ljust(6)} | {tempo_str}"
        texto_reg = fonte_item.render(linha_texto, True, (255, 255, 255))
        tela.blit(texto_reg, (LARGURA // 2 - 150, y))
        y += 40
        
    instrucao = pygame.font.SysFont('arial', 18, True).render('Pressione a tecla R para Jogar Novamente', True, (0, 255, 0))
    tela.blit(instrucao, (LARGURA // 2 - instrucao.get_width() // 2, 440))