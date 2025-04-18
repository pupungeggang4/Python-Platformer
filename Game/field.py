import pygame

from primitive import *
from prototype import *

class Field():
    def __init__(self):
        self.thing = [Coin([200, 200]), Coin([280, 200]), Coin([360, 200]), Coin([440, 200])]

    def render(self, game):
        for thing in self.thing:
            thing.render(game)