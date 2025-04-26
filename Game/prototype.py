import pygame
import res
from primitive import *

class Thing():
    def __init__(self):
        pass

class Collectable(Thing):
    def __init__(self):
        pass

    def collect_handle(self, game):
        if self.rect.collide_with_shape(game.field.player.rect):
            game.field.player.coin += 1
            game.field.thing.remove(self)

class Coin(Collectable):
    def __init__(self, pos):
        self.rect = Rect2D(pos[0], pos[1], 40, 40)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)
        self.frametime = 200
        self.frames = 4
        self.frame = 0

    def handle_tick(self, game):
        pass

    def render(self, game):
        self.frame = int(pygame.time.get_ticks() / self.frametime) % self.frames
        self.surface.fill(res.COLOR_EMPTY)
        self.surface.blit(res.Image.coin, [0, 0], [40 * self.frame, 0, 40, 40])
        pos = [self.rect.position.x - self.rect.size.x / 2, self.rect.position.y - self.rect.size.y / 2]
        game.screen.blit(self.surface, pos)

class Wall(Thing):
    def __init__(self, rect):
        self.rect = Rect2D(rect[0], rect[1], rect[2], rect[3])
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)
        self.surface.fill(res.COLOR_EMPTY)
        for i in range(0, self.rect.size.y, 40):
            for j in range(0, self.rect.size.x, 40):
                self.surface.blit(res.Image.wall, [j, i])

    def handle_tick(self, game):
        pass

    def render(self, game):
        pos = [self.rect.position.x - self.rect.size.x / 2, self.rect.position.y - self.rect.size.y / 2]
        game.screen.blit(self.surface, pos)

class TileMap(Thing):
    pass