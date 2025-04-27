import pygame
import res
from primitive import *
from render import *

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

class TerrainCell(Thing):
    def __init__(self):
        super().__init__()

class EmptyCell(TerrainCell):
    def __init__(self, pos):
        super().__init__()
        self.rect = Rect2D(pos[0], pos[1], 40, 40)

    def render(self, terrain):
        self.rect.render(terrain.surface)

class SolidCell(TerrainCell):
    def __init__(self, pos, tile_type):
        super().__init__()
        self.rect = Rect2D(pos[0], pos[1], 40, 40)
        self.tile_type = tile_type

    def render(self, terrain):
        if self.tile_type == 0:
            Render.render_image_at_center(terrain.surface, res.Image.terrain_plains, self.rect, [0, 0, 40, 40])
        elif self.tile_type == 1:
            Render.render_image_at_center(terrain.surface, res.Image.terrain_plains, self.rect, [40, 0, 40, 40])
        self.rect.render(terrain.surface)

class Terrain():
    def __init__(self, start, size):
        self.start = Vector2D(start[0], start[1])
        self.size = [size[0], size[1]]
        self.tile = []
        self.surface = pygame.surface.Surface([self.size[1] * 40, self.size[0] * 40], pygame.SRCALPHA)
        for i in range(self.size[0]):
            temp = []
            for j in range(self.size[1]):
                temp.append(EmptyCell([self.start.x + j * 40 + 20, self.start.y + i * 40 + 20]))
            self.tile.append(temp)

    def assign_tile(self, row, col, tile_type):
        if tile_type >= 0:
            self.tile[row][col] = SolidCell([self.start.x + col * 40 + 20, self.start.y + row * 40 + 20], tile_type)
        else:
            self.tile[row][col] = EmptyCell([self.start.x + col * 40 + 20, self.start.y + row * 40 + 20])

    def render(self, game):
        self.surface.fill(res.COLOR_EMPTY)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.tile[i][j].render(self)
        game.screen.blit(self.surface, [self.start.x, self.start.y])

