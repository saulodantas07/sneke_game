import pygame

class Menu:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
        # Carrega a imagem da tela de início (ajuste o nome do arquivo se necessário)
        try:
            self.imagem_fundo = pygame.image.load("assets/tela inicio.png")
            self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, (largura, altura))
        except Exception:
            self.imagem_fundo = None # Fallback caso ocorra erro no caminho/nome
            
        # Define a área e o visual do botão "Play"
        self.botao_rect = pygame.Rect(largura // 2 - 100, altura // 2 + 50, 200, 50)
        self.cor_botao = (0, 200, 0) # Verde
        self.cor_texto = (255, 255, 255) # Branco
        self.fonte = pygame.font.SysFont(None, 36)

    def desenhar(self, tela):
        # Desenha a imagem de fundo ou uma cor sólida se não carregar
        if self.imagem_fundo:
            tela.blit(self.imagem_fundo, (0, 0))
        else:
            tela.fill((20, 20, 30))

        # Desenha o botão Play
        pygame.draw.rect(tela, self.cor_botao, self.botao_rect, border_radius=10)
        
        # Renderiza e centraliza o texto no botão
        texto = self.fonte.render("JOGAR", True, self.cor_texto)
        texto_rect = texto.get_rect(center=self.botao_rect.center)
        tela.blit(texto, texto_rect)

    def verificar_clique(self, evento):
        # Verifica se o jogador clicou com o mouse em cima do botão Play
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_rect.collidepoint(evento.pos):
                return True
        return False