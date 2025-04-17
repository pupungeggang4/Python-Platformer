import pygame

from primitive import *
from prototype import *

class Field():
    def __init__(self):
        self.thing = [Coin([200, 200])]

    def render(self, game):
        for thing in self.thing:
            thing.render(game)