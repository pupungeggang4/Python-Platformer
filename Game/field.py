import pygame
from player import *
from primitive import *
from prototype import *

class Field():
    def __init__(self):
        self.thing = [Coin([220, 220])]
        self.terrain = Terrain([0, 0], [20, 32])
        self.terrain.assign_tile(10, 0, 0)
        self.terrain.assign_tile(10, 1, 1)
        self.player = Player()

        self.g_accel = 1000.0

    def handle_tick(self, game):
        for thing in self.thing:
            thing.handle_tick(game)
            if isinstance(thing, Collectable):
                thing.collect_handle(game)
        self.player.handle_tick(game)

    def render(self, game):
        self.terrain.render(game)
        for thing in self.thing:
            thing.render(game)
        self.player.render(game)
