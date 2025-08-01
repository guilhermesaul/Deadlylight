import pygame
import os
from player import Player
from ui.hud import Hud
from ui.menus import PauseMenu

pygame.init()

player = Player()
hud = Hud()

largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura), 0)
pygame.display.set_caption("Começando")
caminho = os.path.join(os.path.dirname(__file__), "data", "images", "background.png")
fundo = pygame.image.load(caminho)
relogio = pygame.time.Clock()
pause_menu = PauseMenu(tela)

pause = False


while True:
    teclas = pygame.key.get_pressed()
    relogio.tick(30)
    tela.blit(fundo, (0, 0))
    eventos = pygame.event.get()
    
    for event in eventos:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                player.segurando_glock = not player.segurando_glock
            
    tela.blit(hud.exibe_vida(tela), (990, 20))
    tela.blit(hud.exibe_fome(tela), (1100, 20))
    tela.blit(hud.exibe_sede(tela), (1200, 20))
    hud.exibir_arma(tela, eventos)
    player.draw(tela)

    if teclas[pygame.K_ESCAPE]:
        pause = not pause
        pygame.time.wait(200)

    if not pause:
        player.update(teclas)
    else:
        pause_menu.desenhar()
        
    pygame.display.flip()