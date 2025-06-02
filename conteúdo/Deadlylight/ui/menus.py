import pygame
from utils.config import FONTE_GRANDE, BRANCO

class PauseMenu:
    def __init__(self, tela):
        self.tela = tela
        self.fonte_pequena = pygame.font.SysFont("arial", 25)

    def desenhar(self):
        overlay = pygame.Surface(self.tela.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.tela.blit(overlay, (0, 0))

        texto = FONTE_GRANDE.render("JOGO PAUSADO", True, BRANCO)
        subtexto = self.fonte_pequena.render("Pressione ESC para continuar", True, BRANCO)

        self.tela.blit(texto, (
            self.tela.get_width() // 2 - texto.get_width() // 2,
            200
        ))
        self.tela.blit(subtexto, (
            self.tela.get_width() // 2 - subtexto.get_width() // 2,
            260
        ))