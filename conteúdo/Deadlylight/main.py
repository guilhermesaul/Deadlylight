import pygame
import os
from player import Player
from ui.menus import PauseMenu

pygame.init()

player = Player()

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    relogio.tick(30)
    tela.blit(fundo, (0, 0))
    teclas = pygame.key.get_pressed()
    player.draw(tela)

    if teclas[pygame.K_ESCAPE]:
        pause = not pause
        pygame.time.wait(200)

    if not pause:
        player.update(teclas)
    else:
        pause_menu.desenhar()
        
    pygame.display.flip()