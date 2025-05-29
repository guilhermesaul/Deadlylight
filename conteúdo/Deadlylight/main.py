import pygame

pygame.init

largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura), 0)
pygame.display.set_caption("Começando")
fundo = pygame.image.load("Deadlylight/data/images/background.png")

while True:
    tela.blit(fundo, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()