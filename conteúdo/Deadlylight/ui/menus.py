import pygame
import sys
import os
from .config import *

class Button:
    def __init__(self, text, pos, callback, font):
        self.text = text
        self.callback = callback
        self.font = font
        self.text_color = AMARELO
        self.hover_color = CINZA
        self.label = self.font.render(self.text, True, self.text_color)
        self.rect = self.label.get_rect(center=pos)

    def hover(self, surface, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            label = FONT.render(self.text, True, self.hover_color)
        else:
            label = self.label
        surface.blit(label, self.rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.callback()

class Menu:
    def __init__(self, screen, start_callback):
        self.screen = screen
        self.start_callback = start_callback
        self.running = True
        background = os.path.join(os.path.dirname(__file__), "..", "data", "images", "bg-tela-inicial.png")
        self.background = pygame.image.load(background).convert()
        mid_x = screen.get_width() // 2
        start_y = screen.get_height() // 2
        gap = 70
        self.buttons = [
            Button("Iniciar Jogo", (mid_x, start_y), self.start_game, FONT),
            Button("Opções", (mid_x, start_y + gap), self.show_options, FONT),
            Button("Sair", (mid_x, start_y + 2 * gap), self.exit_game, FONT),
        ]
    
    def start_game(self):
        self.running = False
        self.start_callback()

    def show_options(self):
        print("Abrindo opções...")
    
    def exit_game(self):
        pygame.quit()
        sys.exit()
    
    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for btn in self.buttons:
                        btn.check_click(mouse_pos)

            self.screen.blit(self.background, (0, 0))
            for btn in self.buttons:
                btn.hover(self.screen, mouse_pos)

            pygame.display.flip()
            clock.tick(FPS)