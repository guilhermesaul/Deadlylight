import pygame
from ui.config import *
from ui.tiros import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.bullets = pygame.sprite.Group()
        self.ammo = 999  # Maximum ammo
        self.andar_direita = []
        self.andar_esquerda = []
        self.andar_direita_glock = []
        self.andar_esquerda_glock = []
        self.caminho_direita = [
            os.path.join(os.path.dirname(__file__), "data", "images", "animacao_andar", f"andar_direita{i}.png")
            for i in range(1, 6)
        ]
        for caminho in self.caminho_direita:
            self.andar_direita.append(pygame.image.load(caminho))
        
        self.caminho_esquerda = [
            os.path.join(os.path.dirname(__file__), "data", "images", "animacao_andar", f"andar_esquerda{i}.png")
            for i in range(1, 6)
        ]
        for caminho in self.caminho_esquerda:
            self.andar_esquerda.append(pygame.image.load(caminho))
            
        self.caminho_direita_glock = [
            os.path.join(os.path.dirname(__file__), "data", "images", "animacao_andar_glock", f"andando_direita_glock{i}.png")
            for i in range(1, 6)
        ]
        for caminho in self.caminho_direita_glock:
            self.andar_direita_glock.append(pygame.image.load(caminho))
            
        self.caminho_esquerda_glock = [
            os.path.join(os.path.dirname(__file__), "data", "images", "animacao_andar_glock", f"andando_esquerda_glock{i}.png")
            for i in range(1, 6)
        ]
        for caminho in self.caminho_esquerda_glock:
            self.andar_esquerda_glock.append(pygame.image.load(caminho))
            
        self.atual = 0
        self.image = self.andar_direita[self.atual]
        self.image = pygame.transform.scale(self.image, (64*3, 64*3))
        self.x = 300
        self.y = 350
        self.rect = self.image.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x
        self.velocidade = 4
        self.segurando_glock = False
        self.direcao = "direita" 
        
    def update(self, teclas, na_loja):
        self.atual += 0.2
        if na_loja:
            pass
        else:
            if self.segurando_glock:
                
                if teclas[pygame.K_d]:
                    self.x += self.velocidade
                    self.rect.left = self.x
                    if self.atual >= len(self.andar_direita_glock):
                        self.atual = 0
                    self.image = self.andar_direita_glock[int(self.atual)]
                    self.direcao = "direita"

                elif teclas[pygame.K_a]:
                    self.x -= self.velocidade
                    self.rect.left = self.x
                    if self.atual >= len(self.andar_esquerda_glock):
                        self.atual = 0
                    self.image = self.andar_esquerda_glock[int(self.atual)]
                    self.direcao = "esquerda"

            else:
                if teclas[pygame.K_d]:
                    self.x += self.velocidade
                    self.rect.left = self.x
                    if self.atual >= len(self.andar_direita):
                        self.atual = 0
                    self.image = self.andar_direita[int(self.atual)]
                    self.direcao = "direita"

                elif teclas[pygame.K_a]:
                    self.x -= self.velocidade
                    self.rect.left = self.x
                    if self.atual >= len(self.andar_esquerda):
                        self.atual = 0
                    self.image = self.andar_esquerda[int(self.atual)]
                    self.direcao = "esquerda"
                    
            if not teclas[pygame.K_a] and not teclas[pygame.K_d]:
                self.atual = 0
                if self.segurando_glock:
                    if self.direcao == "direita":
                        self.image = self.andar_direita_glock[0]
                    else:
                        self.image = self.andar_esquerda_glock[0]
                else:
                    if self.direcao == "direita":
                        self.image = self.andar_direita[0]
                    else:
                        self.image = self.andar_esquerda[0]

        self.image = pygame.transform.scale(self.image, (64*3, 64*3))
    
    def atirar(self, mouse_x, mouse_y):
        if self.segurando_glock and self.ammo > 0:
            # Calculate weapon position based on player direction and position
            if self.direcao == "direita":
                # Weapon is on the right side, slightly forward and at mid-height
                weapon_x = self.rect.centerx + 60
                weapon_y = self.rect.centery + 10
            else:
                # Weapon is on the left side
                weapon_x = self.rect.centerx - 60
                weapon_y = self.rect.centery + 10
            
            nova_bala = Bullet(weapon_x, weapon_y, self.direcao, mouse_x, mouse_y)
            self.bullets.add(nova_bala)
            self.ammo -= 1  # Consume one bullet per shot
        
    def draw(self, tela):
        tela.blit(self.image, self.rect)