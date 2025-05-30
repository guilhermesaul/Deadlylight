import pygame
import os

pygame.init

largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura), 0)
pygame.display.set_caption("Começando")
caminho = os.path.join(os.path.dirname(__file__), "data", "images", "background.png")
fundo = pygame.image.load(caminho)

while True:
    tela.blit(fundo, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()