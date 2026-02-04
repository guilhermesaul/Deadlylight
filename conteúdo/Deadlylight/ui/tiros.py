import pygame
import os
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao, target_x, target_y):
        super().__init__()
        caminho_bullet = os.path.join(os.path.dirname(__file__), "..", "data", "images", "bullet.png")
        self.image = pygame.image.load(caminho_bullet)
        
        # Make bullet bigger and more visible
        self.image = pygame.transform.scale(self.image, (20, 20))
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidade = 15
        self.direcao = direcao
        
        # Calculate trajectory based on mouse position
        dx = target_x - x
        dy = target_y - y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            self.vel_x = (dx / distance) * self.velocidade
            self.vel_y = (dy / distance) * self.velocidade
        else:
            # Default horizontal movement
            self.vel_x = self.velocidade if direcao == "direita" else -self.velocidade
            self.vel_y = 0

    def update(self):
        # Move bullet based on calculated trajectory
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Destroy bullet if it goes off screen
        if self.rect.x > 1280 or self.rect.x < 0 or self.rect.y > 720 or self.rect.y < 0:
            self.kill()