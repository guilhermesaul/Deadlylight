import pygame
import os

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao):
        super().__init__()
        caminho_bullet = os.path.join(os.path.dirname(__file__), "..", "data", "images", "bullet.png")
        self.image = pygame.image.load(caminho_bullet)
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, (30, 22))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidade = 15
        self.direcao = direcao
        if self.direcao == "esquerda":
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        # A bala se move a cada frame (isso cria o efeito de repetição/movimento)
        if self.direcao == "direita":
            self.rect.x += self.velocidade
        else:
            self.rect.x -= self.velocidade
        
        # Destruir a bala se sair da tela para não pesar o jogo
        if self.rect.x > 1280 or self.rect.x < 0:
            self.kill()