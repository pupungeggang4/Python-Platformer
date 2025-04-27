import pygame
import res

from primitive import *

class Player():
    def __init__(self):
        self.rect = Rect2D(100, 100, 64, 64)
        self.life = 0
        self.coin = 0
        self.speed = 200.0
        self.velocity = Vector2D(0, 0)
        self.term_speed = 800.0

    def handle_tick(self, game):
        self.handle_move(game)

    def handle_move(self, game):
        position = self.rect.position
        temp_position = Vector2D(position.x, position.y)

        self.velocity.x = 0
        if game.key_pressed['left'] == True:
            self.velocity.x -= self.speed

        if game.key_pressed['right'] == True:
            self.velocity.x += self.speed

        self.velocity.y += game.field.g_accel * game.delta / 1000
        if self.velocity.y > self.term_speed:
            self.velocity.y = self.term_speed

        temp_position.x += self.velocity.x * game.delta / 1000
        temp_position.y += self.velocity.y * game.delta / 1000

        self.rect.position = temp_position

    def render(self, game):
        rect = [self.rect.position.x - self.rect.size.x / 2, self.rect.position.y - self.rect.size.y / 2, self.rect.size.x, self.rect.size.y]
        pygame.draw.rect(game.screen, res.COLOR_BLACK, rect, 2)
