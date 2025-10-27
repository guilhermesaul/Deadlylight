import pygame
import sys
import os
from utils.config import *

def mostrar_historia(tela):
    fonte = FONT
    
    historia = [
        "O mundo que conhecemos já não existe mais.",
        "Um vírus misterioso se espalhou rapidamente.",
        "As cidades foram abandonadas.",
        "Consumidas pelo silêncio e pelo medo.",
        "Todos morreram ou se transformaram em...",
        "Criaturas sedentas por carne humana.",
        "Você é a única sobrevivente.",
        "Sozinha, precisa lutar pela sua vida."
    ]

    caminho = os.path.join(os.path.dirname(__file__), "..", "data", "images", "bg_completo.png")
    caminho1 = os.path.normpath(caminho)
    fundo = pygame.image.load(caminho1).convert()
    altura_desejada = alturaTela
    proporcao = altura_desejada / fundo.get_height()
    nova_largura = int(fundo.get_width() * proporcao)
    fundo = pygame.transform.scale(fundo, (nova_largura, altura_desejada))
    
    largura = fundo.get_width()

    x = 0
    y = 0

    relogio = pygame.time.Clock()
    rodando = True
    frase_indice = 0
    transparencia = 0
    fade_in = True
    mostrador = 120 
    contador = 0

    texto_surface = fonte.render(historia[frase_indice], True, (255, 255, 255))
    texto_surface.set_alpha(transparencia)

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rodando = False

        x -= 5.75
        if x <= -largura + larguraTela:
            x = -largura + larguraTela  

        tela.fill((0, 0, 0))
        tela.blit(fundo, (x, y))

        if fade_in:
            transparencia += 5
            if transparencia >= 255:
                transparencia = 255
                fade_in = False
                contador = 0
        else:
            contador += 1
            if contador >= mostrador:
                transparencia -= 5
                if transparencia <= 0:
                    transparencia = 0
                    fade_in = True
                    frase_indice += 1
                    if frase_indice >= len(historia):
                        rodando = False
                        break
                    texto_surface = fonte.render(historia[frase_indice], True, (255, 255, 255))

        texto_surface.set_alpha(transparencia)
        texto_rect = texto_surface.get_rect(center=(larguraTela//2, alturaTela//2))
        texto_pular = fonte.render("Pressione ESPAÇO para pular", True, (255, 255, 255))
        texto_pular_rect = texto_pular.get_rect(center=(larguraTela//2, alturaTela - 75))
        tela.blit(texto_pular, texto_pular_rect)
        tela.blit(texto_surface, texto_rect)

        pygame.display.flip()
        relogio.tick(FPS)
