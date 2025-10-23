import pygame
import os
import sys
from player import Player
from ui.hud import Hud
from ui.menus import Menu
caminhoimagem = os.path.join(os.path.dirname(__file__), "data", "images", "mapa", "caminho-1.png")
fundo = pygame.image.load(caminhoimagem)
import utils.config as config
from ui.story import mostrar_historia
import ui.maps as maps

pygame.init()

player = Player()
hud = Hud()

tela = pygame.display.set_mode((config.LARGURA, config.ALTURA), 0)
pygame.display.set_caption("Deadlylight")
fundo = pygame.image.load(caminhoimagem)
relogio = pygame.time.Clock()

def iniciar_jogo():
    mostrar_historia(tela)
    pause = False
    running = True
    while running:
        teclas = pygame.key.get_pressed()
        relogio.tick(config.FPS)
        eventos = pygame.event.get()

        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player.segurando_glock = not player.segurando_glock

        tela.blit(fundo, (0, 0))

        tela.blit(hud.exibe_vida(tela), (990, 20))
        tela.blit(hud.exibe_fome(tela), (1100, 20))
        tela.blit(hud.exibe_sede(tela), (1200, 20))
        hud.exibir_arma(tela, eventos)
        player.draw(tela)

        if teclas[pygame.K_ESCAPE]:
            pause = not pause
            pygame.time.wait(200)

        player.update(teclas)

        pygame.display.flip()


def main():
    menu = Menu(tela, start_callback=iniciar_jogo)
    menu.run()


if __name__ == "__main__":
    main()