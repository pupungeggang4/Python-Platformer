import pygame
import res
from primitive import *

class Thing():
    def __init__(self):
        pass

class Collectable(Thing):
    def __init__(self):
        pass

class Coin(Collectable):
    def __init__(self, pos):
        self.rect = Rect2D(pos[0], pos[1], 40, 40)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)
        self.animation_time = 0
        self.frametime = 0.2
        self.frames = 4
        self.frame = 0

    def render(self, game):
        self.animation_time += 1.0 / game.fps
        self.frame = int(self.animation_time / self.frametime) % self.frames
        self.surface.fill([0, 0, 0, 0])
        self.surface.blit(res.Image.coin, [0, 0], [40 * self.frame, 0, 40, 40])
        game.screen.blit(self.surface, [self.rect.position.x - self.rect.size.x / 2, self.rect.position.y - self.rect.size.y / 2])

    def collect_handle(self, game):
        pass

class Wall():
    pass