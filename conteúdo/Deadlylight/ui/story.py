import pygame
import sys
import os
import utils.config as config

def mostrar_historia(tela):
    fonte = config.FONT
    
    historia = [
        "O mundo que conhecemos já não existe mais.",
        "Um vírus misterioso se espalhou rapidamente.",
        "As cidades foram abandonadas.",
        "Consumidas pelo silêncio e pelo medo.",
        "Todos morreram ou se transformaram em...",
        "Criaturas sedentas por carne humana.",
        "Você é o único sobrevivente.",
        "Sozinho, precisa lutar pela sua vida."
    ]

    caminho = os.path.join(os.path.dirname(__file__), "..", "data", "images", "bg_completo.jpeg")
    caminho1 = os.path.normpath(caminho)
    fundo = pygame.image.load(caminho1).convert()
    altura_desejada = config.ALTURA
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
                if event.key == pygame.K_ESCAPE:
                    rodando = False

        x -= 1
        if x <= -largura + config.LARGURA:
            x = -largura + config.LARGURA  

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
        texto_rect = texto_surface.get_rect(center=(config.LARGURA//2, config.ALTURA//2))
        tela.blit(texto_surface, texto_rect)

        pygame.display.flip()
        relogio.tick(30)
