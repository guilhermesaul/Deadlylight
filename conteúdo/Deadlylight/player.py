import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.andar_direita = []
        self.andar_esquerda = []
        self.caminho_direita = [
            os.path.join(os.path.dirname(__file__), "data", "images", f"andar_direita{i}.png")
            for i in range(1, 6)
        ]
        for caminho in self.caminho_direita:
            self.andar_direita.append(pygame.image.load(caminho))
        
        self.caminho_esquerda = [
            os.path.join(os.path.dirname(__file__), "data", "images", f"andar_esquerda{i}.png")
            for i in range(1, 6)
        ]
        for caminho in self.caminho_esquerda:
            self.andar_esquerda.append(pygame.image.load(caminho))
            
        self.atual = 0
        self.image = self.andar_direita[self.atual]
        self.image = pygame.transform.scale(self.image, (64*3, 64*3))
        self.x = 300
        self.y = 337
        self.rect = self.image.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x
        self.velocidade = 7
        
    def update(self, teclas):
        if teclas == pygame.key.get_pressed():
            self.atual += 0.2
            if teclas[pygame.K_d]:
                self.x += self.velocidade
                self.rect.left = self.x
                if self.atual >= len(self.andar_direita):
                    self.atual = 0
                self.image = self.andar_direita[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (64*3, 64*3))
            if teclas[pygame.K_a]:
                self.x -= self.velocidade
                self.rect.left = self.x
                if self.atual >= len(self.andar_esquerda):
                    self.atual = 0
                self.image = self.andar_esquerda[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (64*3, 64*3))
    
            
            
            
        
    def draw(self, tela):
        tela.blit(self.image, self.rect)