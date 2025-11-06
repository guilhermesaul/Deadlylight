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

caminho_ui_loja = os.path.join(os.path.dirname(__file__), "data", "images", "loja", "ui_loja.png")
ui_loja = pygame.image.load(caminho_ui_loja)
x_ui_loja = larguraTela // 2 - ui_loja.get_width() // 2
y_ui_loja = alturaTela // 2 - ui_loja.get_height() // 2


def iniciar_jogo():
    mostrar_historia(tela)
    running = True
    na_loja = False
    while running:
        teclas = pygame.key.get_pressed()
        relogio.tick(FPS)
        eventos = pygame.event.get()

        if na_loja:
            tela.fill((41, 40, 40))
            tela.blit(ui_loja, (x_ui_loja, y_ui_loja))
        else:
            mapa.draw(tela)
            player.draw(tela)
            hud.draw(tela)
            hud.exibir_arma(tela, eventos)
        
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if na_loja:
                    pass
                else: 
                    if event.key == pygame.K_1:
                        player.segurando_glock = not player.segurando_glock
                if event.key == pygame.K_e:
                    if hud.area_entrar:
                        na_loja = True

        player.update(teclas, na_loja)
        
        #print(player.x)
        
        if mapa.indiceAtual == 1:
            if 615 <= player.rect.left <= 765 and na_loja == False:
                hud.exibe_entrar(tela)
                hud.area_entrar = True
            elif na_loja == True: 
                hud.area_entrar = True
            else: 
                hud.area_entrar = False
        elif mapa.indiceAtual == 3:
            if 925 <= player.rect.left <= 1070 and na_loja == False:
                hud.exibe_entrar(tela)
                hud.area_entrar = True
            elif na_loja == True: 
                hud.area_entrar = True
            else: 
                hud.area_entrar = False
        elif mapa.indiceAtual == 5:
            if 620 <= player.rect.left <= 780 and na_loja == False:
                hud.exibe_entrar(tela)
                hud.area_entrar = True
            elif na_loja == True: 
                hud.area_entrar = True
            else: 
                hud.area_entrar = False
        elif mapa.indiceAtual == 7:
            if 330 <= player.rect.left <= 465 and na_loja == False:
                hud.exibe_entrar(tela)
                hud.area_entrar = True
            elif na_loja == True: 
                hud.area_entrar = True
            else: 
                hud.area_entrar = False

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