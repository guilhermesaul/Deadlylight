import pygame
import os
import sys
from player import Player
from ui.hud import Hud
from ui.menus import Menu
from ui.config import * 
from ui.story import mostrar_historia
from ui.maps import Mapa
from zumbi import Zombie
from ui.tiros import Bullet


pygame.init()


tela = pygame.display.set_mode((larguraTela, alturaTela), 0)
pygame.display.set_caption("Deadlylight")
relogio = pygame.time.Clock()

player = Player()
zombies = pygame.sprite.Group()  # Group to hold multiple zombies
hud = Hud()
mapa = Mapa()

caminho_ui_loja = os.path.join(os.path.dirname(__file__), "data", "images", "loja", "ui_loja.png")
ui_loja = pygame.image.load(caminho_ui_loja)
x_ui_loja = larguraTela // 2 - ui_loja.get_width() // 2
y_ui_loja = alturaTela // 2 - ui_loja.get_height() // 2


def spawn_zombies_for_level(city_level, player_x):
    """Spawn zombies based on city level. City 1 = 4 zombies, City 2 = 5, etc."""
    zombies = pygame.sprite.Group()
    
    # Determine number of zombies based on city level
    if city_level == 9:  # Final level - zombie horde
        num_zombies = 20
    else:
        num_zombies = 3 + city_level  # City 1 = 4, City 2 = 5, etc.
    
    import random
    for i in range(num_zombies):
        # Spawn zombies at various positions, not too close to player
        if random.choice([True, False]):
            x = random.randint(player_x + 300, larguraTela - 100)
        else:
            x = random.randint(100, max(100, player_x - 300))
        y = random.randint(300, 400)
        zombie = Zombie(x, y)
        zombies.add(zombie)
    
    return zombies


def iniciar_jogo():
    mostrar_historia(tela)
    
    # Initialize zombies for the first level (city 0)
    global zombies
    zombies = spawn_zombies_for_level(0, player.rect.x)
    
    running = True
    na_loja = False
    invencibilidade_timer = 0
    while running:
        
        if invencibilidade_timer > 0:
            invencibilidade_timer -= 1

        teclas = pygame.key.get_pressed()
        relogio.tick(FPS)
        eventos = pygame.event.get()

        if na_loja:
            tela.fill((41, 40, 40))
            tela.blit(ui_loja, (x_ui_loja, y_ui_loja))
        else:
            mapa.draw(tela)

            player.bullets.update()
            player.bullets.draw(tela)

            # Update all zombies
            for zombie in zombies:
                zombie.update(player.rect)
                zombie.draw(tela)
                
                # Check bullet collisions with each zombie
                tiros_recebidos = pygame.sprite.spritecollide(zombie, player.bullets, True)
                for tiro in tiros_recebidos:
                    # Determine which body part was hit based on bullet position
                    hitbox_region = zombie.get_hitbox_region(tiro.rect.centery)
                    
                    if hitbox_region == "head":
                        zombie.vida -= 5  # Head: 2 shots to kill (10 HP / 5 damage = 2 shots)
                    elif hitbox_region == "torso":
                        zombie.vida -= 3.34  # Torso: 3 shots to kill (10 HP / 3.34 ≈ 3 shots)
                    else:  # legs
                        zombie.vida -= 2.5  # Legs: 4 shots to kill (10 HP / 2.5 = 4 shots)
                    
                    # Remove zombie if dead
                    if zombie.vida <= 0:
                        zombie.kill()
                
                # Check collision with player
                if player.rect.colliderect(zombie.rect):
                    if invencibilidade_timer == 0:
                        hud.vida -= 10
                        invencibilidade_timer = 60
                        
                        if hud.vida <= 0:
                            hud.vida = 0
                            pygame.quit()
                            sys.exit()
            hud.exibe_vida(tela)
            hud.exibe_fome(tela)
            hud.exibe_sede(tela)
            player.draw(tela)
            hud.draw(tela)
            hud.exibir_arma(tela, eventos, player.ammo)
        
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # 1 é o botão esquerdo
                    # Get mouse position for aiming
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    player.atirar(mouse_x, mouse_y)

            if event.type == pygame.KEYDOWN:
                if na_loja:
                    pass
                else: 
                    if event.key == pygame.K_1:
                        player.segurando_glock = not player.segurando_glock
                if event.key == pygame.K_e:
                    if hud.area_entrar:
                        na_loja = True
                if event.key == pygame.K_q:
                    if na_loja:
                        na_loja = False
            

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
                
                # Spawn zombies based on the current map index (city level)
                zombies.empty()  # Clear existing zombies
                zombies.update(spawn_zombies_for_level(mapa.indiceAtual, player.rect.x))
            else:
                player.x = larguraTela - player.rect.width
                player.rect.left = player.x
            
        elif player.rect.left < 0:
            if mapa.indiceAtual > 0:
                mapa.mudar_mapa("esquerda")
                player.x = larguraTela - player.rect.width - 10
                player.rect.left = player.x
                
                # Spawn zombies based on the current map index (city level)
                zombies.empty()  # Clear existing zombies
                zombies.update(spawn_zombies_for_level(mapa.indiceAtual, player.rect.x))
            else:
                player.x = 1
                player.rect.left = player.x

        pygame.display.flip()


def main():
    menu = Menu(tela, start_callback=iniciar_jogo)
    menu.run()


if __name__ == "__main__":
    main()