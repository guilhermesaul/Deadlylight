import pygame
import os
from .config import *

pygame.font.init()

class Hud:
    def __init__(self):
        self.mostrar = False
        self.mensagem = "100"
        self.tamanho_40 = 40
        self.tamanho_28 = 28
        self.cor = (0, 0, 0)
        self.fonte_40 = pygame.font.SysFont("arial", self.tamanho_40, True)
        self.fonte_28 = pygame.font.SysFont("arial", self.tamanho_28, True)
        self.texto_formatado_40 = self.fonte_40.render(self.mensagem, True, self.cor)
        self.municao = "| 12 munições"
        self.texto_munição = self.fonte_40.render(self.municao, True, self.cor)
        
    def exibe_vida(self, tela):
        self.caminho = os.path.join(os.path.dirname(__file__), "..", "data", "images", "hud", "coracao1.png")
        self.imagem = pygame.image.load(self.caminho)
        self.imagem = pygame.transform.scale(self.imagem, (16*2.75, 16*2.75))
        tela.blit(self.imagem, (940, 22.5))
        return tela.blit(self.texto_formatado_40, (990, 20))

    def exibe_fome(self, tela):
        self.caminho = os.path.join(os.path.dirname(__file__), "..", "data", "images", "hud", "fome1.png")
        self.imagem = pygame.image.load(self.caminho)
        self.imagem = pygame.transform.scale(self.imagem, (16*2, 16*2))
        tela.blit(self.imagem, (1065, 30))
        return tela.blit(self.texto_formatado_40, (1100, 20))
    
    def exibe_sede(self, tela):
        self.caminho = os.path.join(os.path.dirname(__file__), "..", "data", "images", "hud", "sede1.png")
        self.imagem = pygame.image.load(self.caminho)
        self.imagem = pygame.transform.scale(self.imagem, (16*2.75, 16*2.75))
        tela.blit(self.imagem, (1160, 21))
        return tela.blit(self.texto_formatado_40, (1200, 20))
    
    def exibir_arma(self, tela, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    self.mostrar = not self.mostrar
        if self.mostrar:
            self.caminho = os.path.join(os.path.dirname(__file__), "..", "data", "images", "glock.png")
            self.imagem = pygame.image.load(self.caminho)
            self.imagem = pygame.transform.scale(self.imagem, (32*2, 32*2))
            tela.blit(self.imagem, (70, 20))
            tela.blit(self.texto_munição, (140, 25))

    def exibe_entrar(self, tela):
        self.mensagem_entrar = "Aperte 'E' para entrar."
        self.texto_entrar = self.fonte_28.render(self.mensagem_entrar, True, self.cor)
        self.rect_texto_entrar = self.texto_entrar.get_rect()
        self.rect_texto_entrar.centerx =  larguraTela // 2
        self.rect_texto_entrar.top = 30
        return tela.blit(self.texto_entrar, self.rect_texto_entrar)
    
    def draw(self, tela):
        self.exibe_vida(tela)
        self.exibe_fome(tela)
        self.exibe_sede(tela)
        self.exibe_entrar(tela)