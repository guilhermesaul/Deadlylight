import pygame
import os

pygame.init()

BRANCO = (255, 255, 255)
CINZA = (120, 120, 120)
PRETO = (0, 0, 0)
AMARELO = (231, 225, 193)
FONTE_GRANDE = pygame.font.SysFont("arial", 40, True, False)
FPS = 60
fonte = os.path.join(os.path.dirname(__file__), "..", "data", "fonts", "Capture it.ttf")
FONT = pygame.font.Font(fonte, 48)
LARGURA = 1280
ALTURA = 720