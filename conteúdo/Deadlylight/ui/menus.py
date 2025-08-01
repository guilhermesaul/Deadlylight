import pygame
import sys
import utils.config as config

class Button:
    def __init__(self, text, pos, callback, font):
        self.text = text
        self.callback = callback
        self.font = font
        self.text_color = config.BRANCO
        self.hover_color = config.CINZA
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