import pygame

import res
import UI
from render import Render
from prototype import *
from primitive import *

def loop(game):
    render(game)

def render(game):
    game.screen.fill(res.COLOR_WHITE)
    game.field.render(game)
    game.screen.blit(res.font_neodgm_32.render(f'{game.player.coin}', False, res.COLOR_BLACK), UI.Field.text_coin)
    if game.menu == True:
        Render.render_menu(game)
    pygame.display.flip()

def mouse_up(game, button, mouse):
    pass

def key_down(game, key):
    pass

def key_up(game, key):
    pass