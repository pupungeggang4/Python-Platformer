import pygame

import res
import UI

def loop(game):
    game.screen.fill(res.COLOR_WHITE)
    game.screen.blit(res.font_neodgm_32.render('Platformer', False, res.COLOR_BLACK), UI.Title.text_title)
    pygame.draw.rect(game.screen, res.COLOR_BLACK, UI.Title.button_start, 2)
    game.screen.blit(res.font_neodgm_32.render('Start Game', False, res.COLOR_BLACK), UI.Title.text_start)
    pygame.draw.rect(game.screen, res.COLOR_BLACK, UI.Title.button_erase, 2)
    game.screen.blit(res.font_neodgm_32.render('Erase Data', False, res.COLOR_BLACK), UI.Title.text_erase)
    pygame.display.flip()

def mouse_up(game, button, mouse):
    pass

def key_down(game, key):
    pass

def key_up(game, key):
    pass