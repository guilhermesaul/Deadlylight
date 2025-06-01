import pygame
import os
from player import Player

pygame.init()

player = Player()

largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura), 0)
pygame.display.set_caption("Começando")
caminho = os.path.join(os.path.dirname(__file__), "data", "images", "background.png")
fundo = pygame.image.load(caminho)
relogio = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    relogio.tick(30)
    tela.blit(fundo, (0, 0))
    teclas = pygame.key.get_pressed()
    player.draw(tela)
    player.update(teclas)
     
    pygame.display.flip()