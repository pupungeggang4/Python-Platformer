import pygame
import res
import UI

class Render():
    def render_menu(game):
        pygame.draw.rect(game.screen, res.COLOR_WHITE, UI.Menu.rect)
        pygame.draw.rect(game.screen, res.COLOR_BLACK, UI.Menu.rect, 2)
        game.screen.blit(res.font_neodgm_32.render('Pause', False, res.COLOR_BLACK), UI.Menu.text_pause)
        pygame.draw.rect(game.screen, res.COLOR_BLACK, UI.Menu.button_resume, 2)
        game.screen.blit(res.font_neodgm_32.render('Resume', False, res.COLOR_BLACK), UI.Menu.text_resume)
        pygame.draw.rect(game.screen, res.COLOR_BLACK, UI.Menu.button_exit, 2)
        game.screen.blit(res.font_neodgm_32.render('Exit', False, res.COLOR_BLACK), UI.Menu.text_exit)