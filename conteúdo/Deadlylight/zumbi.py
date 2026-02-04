import pygame
import os
import random
from ui.config import larguraTela, alturaTela

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.vida = 10  # Increased to handle different damage values
        self.max_vida = 10
        self.andar_direita = []
        self.andar_esquerda = []

        # Carregando as imagens de andar para a direita
        self.caminho_direita = [
            os.path.join(os.path.dirname(__file__), "data", "images", "animacao_andar_zumbi", f"andar_direita_zumbi{i}.png")
            for i in range(1, 6)
        ]
        for caminho in self.caminho_direita:
            img = pygame.image.load(caminho)
            # Redimensionando logo no carregamento para ganhar performance
            self.andar_direita.append(pygame.transform.scale(img, (64*3, 64*3)))
            img = pygame.transform.flip(img, True, False)
            self.andar_direita.append(img)
        
        # Carregando as imagens de andar para a esquerda
        self.caminho_esquerda = [
            os.path.join(os.path.dirname(__file__), "data", "images", "animacao_andar_zumbi", f"andar_esquerda_zumbi{i}.png")
            for i in range(1, 6)
        ]
        for caminho in self.caminho_esquerda:
            img = pygame.image.load(caminho)
            img = pygame.transform.scale(img, (64*3, 64*3))
            # Se o desenho original olha para a DIREITA, inverta aqui para a lista da ESQUERDA:
            img = pygame.transform.flip(img, True, False)
            self.andar_esquerda.append(img)
        self.atual = 0
        self.image = self.andar_direita[self.atual]
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        
        # Atributos de lógica
        self.velocidade = 2 # Zumbi geralmente é mais lento que o player
        self.direcao = "direita"

    def update(self, player_rect):
        self.atual += 0.15
        
        # Se o zumbi está à esquerda do player, ele tem que ir para a DIREITA
        if self.rect.x < player_rect.x:
            self.rect.x += self.velocidade
            self.direcao = "direita"
            if self.atual >= len(self.andar_direita):
                self.atual = 0
            # SE ESTAVA INVERTIDO, TROCAMOS PARA AQUI:
            self.image = self.andar_direita[int(self.atual)]
            
        # Se o zumbi está à direita do player, ele tem que ir para a ESQUERDA
        elif self.rect.x > player_rect.x:
            self.rect.x -= self.velocidade
            self.direcao = "esquerda"
            if self.atual >= len(self.andar_esquerda):
                self.atual = 0
            # SE ESTAVA INVERTIDO, TROCAMOS PARA AQUI:
            self.image = self.andar_esquerda[int(self.atual)]
        
        else:
            self.atual = 0
            if self.direcao == "direita":
                self.image = self.andar_direita[0]
            else:
                self.image = self.andar_esquerda[0]

    def draw(self, tela):
        tela.blit(self.image, self.rect)
    
    def get_hitbox_region(self, bullet_y):
        """Determine which region of zombie was hit based on bullet Y position"""
        zombie_height = self.rect.height
        zombie_top = self.rect.top
        
        # Head region: top 25% of zombie
        head_bottom = zombie_top + (zombie_height * 0.25)
        # Torso region: 25% - 60% of zombie
        torso_bottom = zombie_top + (zombie_height * 0.60)
        # Legs region: 60% - 100% of zombie
        
        if bullet_y < head_bottom:
            return "head"
        elif bullet_y < torso_bottom:
            return "torso"
        else:
            return "legs"

    def spawn(self, lado_oposto_ao_player):
        if lado_oposto_ao_player == "direita":
            self.rect.x = larguraTela - 100
        else:
            self.rect.x = 100
        
        # Opcional: dar uma variação aleatória no X para não ser sempre igual
        self.rect.x += random.randint(-50, 50)
        self.atual = 0