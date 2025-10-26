import pygame
import os
import sys
from player import Player
from ui.hud import Hud
from ui.menus import Menu
from utils.config import * 
from ui.story import mostrar_historia
from ui.maps import Mapa


pygame.init()

player = Player()
hud = Hud()
mapa = Mapa()

tela = pygame.display.set_mode((LARGURA, ALTURA), 0)
pygame.display.set_caption("Deadlylight")
relogio = pygame.time.Clock()

def iniciar_jogo():
    mostrar_historia(tela)
    pause = False
    running = True
    while running:
        teclas = pygame.key.get_pressed()
        relogio.tick(FPS)
        eventos = pygame.event.get()

        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player.segurando_glock = not player.segurando_glock

        mapa.draw(tela)
        player.draw(tela)
        tela.blit(hud.exibe_vida(tela), (990, 20))
        tela.blit(hud.exibe_fome(tela), (1100, 20))
        tela.blit(hud.exibe_sede(tela), (1200, 20))
        hud.exibir_arma(tela, eventos)

        if teclas[pygame.K_ESCAPE]:
            pause = not pause
            pygame.time.wait(200)

        player.update(teclas)

        if player.rect.right >= LARGURA:
            mapa.mudar_mapa("direita")
            player.x = 10
            player.rect.left = player.x
            # pygame.time.wait(150) removido por enquanto, porque dá a sensação de travamento
        elif player.rect.left <= 0:
            mapa.mudar_mapa("esquerda")
            player.x = LARGURA - player.rect.width - 10
            player.rect.left = player.x
            # pygame.time.wait(150) removido por enquanto, porque dá a sensação de travamento

        pygame.display.flip()


def main():
    menu = Menu(tela, start_callback=iniciar_jogo)
    menu.run()


if __name__ == "__main__":
    main()