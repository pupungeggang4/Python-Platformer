import pygame

import res
import UI
from render import Render
from prototype import *
from primitive import *

def loop(game):
    game.screen.fill(res.COLOR_WHITE)
    Render.render_menu(game)
    pygame.display.flip()

def mouse_up(game, button, mouse):
    pass

def key_down(game, key):
    pass

def key_up(game, key):
    pass