import pygame
from ui.maps import Mapa
from ui.config import *

class Player(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
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
        
    def update(self, teclas):
        self.atual += 0.2
        if self.segurando_glock:
            if teclas[pygame.K_d]:
                self.x += self.velocidade
                self.rect.left = self.x
                if self.atual >= len(self.andar_direita_glock):
                    self.atual = 0
                self.image = self.andar_direita_glock[int(self.atual)]

            elif teclas[pygame.K_a]:
                self.x -= self.velocidade
                self.rect.left = self.x
                if self.atual >= len(self.andar_esquerda_glock):
                    self.atual = 0
                self.image = self.andar_esquerda_glock[int(self.atual)]

        else:
            if teclas[pygame.K_d]:
                self.x += self.velocidade
                self.rect.left = self.x
                if self.atual >= len(self.andar_direita):
                    self.atual = 0
                self.image = self.andar_direita[int(self.atual)]

            elif teclas[pygame.K_a]:
                self.x -= self.velocidade
                self.rect.left = self.x
                if self.atual >= len(self.andar_esquerda):
                    self.atual = 0
                self.image = self.andar_esquerda[int(self.atual)]
                
        if not teclas[pygame.K_a] and not teclas[pygame.K_d]:
            if self.segurando_glock:
                self.image = self.andar_direita_glock[0]
            else:
                self.image = self.andar_direita[0]
                
        self.image = pygame.transform.scale(self.image, (64*3, 64*3))
    mapa = Mapa()
    def verificar_entrada(self, mapa=mapa):
        if mapa.indiceAtual == 0:
            if 600 <= self.rect.left <= 800:
                return True
        return False
        
    def draw(self, tela):
        tela.blit(self.image, self.rect)