import pygame
from player import *
from primitive import *
from prototype import *

class Field():
    def __init__(self):
        self.thing = [Coin([200, 200]), Coin([240, 200]), Coin([280, 200]), Coin([320, 200]), Coin([200, 240]), Coin([240, 240]), Coin([280, 240]), Coin([320, 240]), Wall([200, 400, 400, 80]), Wall([600, 120, 80, 240])]
        self.player = Player()

    def handle_tick(self, game):
        for thing in self.thing:
            thing.handle_tick(game)
            if isinstance(thing, Collectable):
                thing.collect_handle(game)
        self.player.handle_tick(game)

    def render(self, game):
        for thing in self.thing:
            thing.render(game)
        self.player.render(game)