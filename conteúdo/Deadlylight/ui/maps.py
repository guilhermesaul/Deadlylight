import pygame
import os

pygame.init()

class Mapa:
    def __init__(self):
        self.caminho1 = os.path.join(os.path.dirname(__file__), "..", "data", "images", "maps", "caminho-1.png")
        self.cidade1 = os.path.join(os.path.dirname(__file__), "..", "data", "images", "maps", "cidade-1.png")
        self.caminho2 = os.path.join(os.path.dirname(__file__), "..", "data", "images", "maps", "caminho-2.png")
        self.cidade2 = os.path.join(os.path.dirname(__file__), "..", "data", "images", "maps", "cidade-2.png")
        self.caminho3 = os.path.join(os.path.dirname(__file__), "..", "data", "images", "maps", "caminho-3.png")
        self.cidade3 = os.path.join(os.path.dirname(__file__), "..", "data", "images", "maps", "cidade-3.png")
        self.caminho4 = os.path.join(os.path.dirname(__file__), "..", "data", "images", "maps", "caminho-4.png")
        self.cidade4 = os.path.join(os.path.dirname(__file__), "..", "data", "images", "maps", "cidade-4.png")
        self.caminho5 = os.path.join(os.path.dirname(__file__), "..", "data", "images", "maps", "caminho-5.png")
        self.lista_mapas = [
            self.caminho1,
            self.cidade1,
            self.caminho2,
            self.cidade2,
            self.caminho3,
            self.cidade3,
            self.caminho4,
            self.cidade4,
            self.caminho5
        ]
        
        self.mapa = []
        self.indiceAtual = 0
        
        for i in range(len(self.lista_mapas)):
            imagem_mapas = pygame.image.load(self.lista_mapas[i])
            self.mapa.append(imagem_mapas)
        
    def draw(self, tela):
        tela.blit(self.mapa[self.indiceAtual], (0, 0))
    def mudar_mapa(self, direcao):
        if direcao == "direita":
            if self.indiceAtual == len(self.mapa) - 1:
                pass
            else:
                self.indiceAtual += 1
        elif direcao == "esquerda":
            if self.indiceAtual == 0:
                pass
            else:
                self.indiceAtual -= 1