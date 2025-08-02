import pygame
import os
from player import Player
from ui.hud import Hud
from ui.menus import Menu

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

def iniciar_jogo():
    pause = False
    running = True
    while running:
        teclas = pygame.key.get_pressed()
        relogio.tick(30)
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