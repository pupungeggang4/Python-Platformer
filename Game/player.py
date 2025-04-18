import pygame
import res

from primitive import *

class Player():
    def __init__(self):
        self.rect = Rect2D(100, 100, 64, 64)
        self.life = 0
        self.coin = 0
        self.speed = 200.0

    def handle_tick(self, game):
        if game.key_pressed['left'] == True:
            self.rect.position.x -= self.speed * game.delta / 1000
        if game.key_pressed['right'] == True:
            self.rect.position.x += self.speed * game.delta / 1000
        if game.key_pressed['up'] == True:
            self.rect.position.y -= self.speed * game.delta / 1000
        if game.key_pressed['down'] == True:
            self.rect.position.y += self.speed * game.delta / 1000

    def render(self, game):
        rect = [self.rect.position.x - self.rect.size.x / 2, self.rect.position.y - self.rect.size.y / 2, self.rect.size.x, self.rect.size.y]
        pygame.draw.rect(game.screen, res.COLOR_BLACK, rect, 2)