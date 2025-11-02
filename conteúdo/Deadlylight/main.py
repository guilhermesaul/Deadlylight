import pygame
import os
import sys
from player import Player
from ui.hud import Hud
from ui.menus import Menu
from ui.config import * 
from ui.story import mostrar_historia
from ui.maps import Mapa


pygame.init()


tela = pygame.display.set_mode((larguraTela, alturaTela), 0)
pygame.display.set_caption("Deadlylight")
relogio = pygame.time.Clock()

player = Player()
hud = Hud()
mapa = Mapa()

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
        hud.draw(tela)
        hud.exibir_arma(tela, eventos)
        print(player.x, player.rect.left)

        if teclas[pygame.K_ESCAPE]:
            pause = not pause
            pygame.time.wait(200)

        player.update(teclas)
        
        if mapa.indiceAtual == 1:
            if 615 <= player.rect.left <= 765:
                hud.exibe_entrar(tela)
        elif mapa.indiceAtual == 3:
            if 925 <= player.rect.left <= 1070:
                hud.exibe_entrar(tela)
        elif mapa.indiceAtual == 5:
            if 635 <= player.rect.left <= 760:
                hud.exibe_entrar(tela)
        elif mapa.indiceAtual == 7:
            if 340 <= player.rect.left <= 460:
                hud.exibe_entrar(tela)

        if player.rect.right > larguraTela:
            if mapa.indiceAtual < len(mapa.lista_mapas) - 1:
                mapa.mudar_mapa("direita")
                player.x = 10
                player.rect.left = player.x
            else:
                player.x = larguraTela - player.rect.width
                player.rect.left = player.x
                # pygame.time.wait(150) removido por enquanto, porque dá a sensação de travamento
            
        elif player.rect.left < 0:
            if mapa.indiceAtual > 0:
                mapa.mudar_mapa("esquerda")
                player.x = larguraTela - player.rect.width - 10
                player.rect.left = player.x
            else:
                player.x = 1
                player.rect.left = player.x
                # pygame.time.wait(150) removido por enquanto, porque dá a sensação de travamento

        pygame.display.flip()


def main():
    menu = Menu(tela, start_callback=iniciar_jogo)
    menu.run()


if __name__ == "__main__":
    main()