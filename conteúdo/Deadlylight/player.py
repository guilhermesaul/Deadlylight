import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.sprites = []
        self.caminhos = [
            os.path.join(os.path.dirname(__file__), "data", "images", f"andar_direita1.png")
        ]
        for caminho in self.caminhos:
            self.sprites.append(pygame.image.load(caminho))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (64*3, 64*3))
        self.x = 300
        self.y = 343
        self.rect = self.image.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x
        self.velocidade = 5
        
    def andar(self, teclas):
        if teclas[pygame.K_d]:
            self.x += self.velocidade
            self.rect.left = self.x
            
        
    def draw(self, tela):
        tela.blit(self.image, self.rect)