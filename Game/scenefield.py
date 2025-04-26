import pygame

import res
import UI
from render import Render
from prototype import *
from primitive import *

def loop(game):
    if game.menu == False:
        if game.state == '':
            game.field.handle_tick(game)
    render(game)

def render(game):
    game.screen.fill(res.COLOR_WHITE)
    game.field.render(game)
    game.screen.blit(res.font_neodgm_32.render(f'{game.field.player.coin}', False, res.COLOR_BLACK), UI.Field.text_coin)
    pygame.draw.rect(game.screen, res.COLOR_BLACK, UI.Field.button_menu, 2)
    if game.menu == True:
        Render.render_menu(game)
    pygame.display.flip()

def mouse_up(game, button, mouse):
    if button == 1:
        if game.menu == False:
            if game.point_inside_rect_UI(mouse, UI.Field.button_menu):
                game.menu = True

        elif game.menu == True:
            if game.point_inside_rect_UI(mouse, UI.Menu.button_resume):
                game.menu = False
            if game.point_inside_rect_UI(mouse, UI.Menu.button_exit):
                game.menu = False
                game.scene = 'title'
                game.state = ''

def key_down(game, key):
    if game.menu == False:
        if key == pygame.K_ESCAPE:
            game.menu = True
        if game.state == '':
            pass

    elif game.menu == True:
        if key == pygame.K_ESCAPE:
            game.menu = False
        if key == pygame.K_r:
            game.menu = False
        if key == pygame.K_e:
            game.menu = False
            game.scene = 'title'
            game.state = ''

def key_up(game, key):
    pass