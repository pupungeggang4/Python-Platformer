import pygame
import res
import UI

class Render():
    def render_menu(game):
        pygame.draw.rect(game.screen, res.COLOR_BLACK, UI.Menu.rect, 2)