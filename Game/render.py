import pygame
import res
import UI

class Render():
    def render_image_at_center(sur, img, rect, cut):
        sur.blit(img, [rect.position.x - rect.size.x / 2, rect.position.y - rect.size.y / 2], cut)

    def render_menu(game):
        pygame.draw.rect(game.screen, res.COLOR_WHITE, UI.Menu.rect)
        pygame.draw.rect(game.screen, res.COLOR_BLACK, UI.Menu.rect, 2)
        game.screen.blit(res.font_neodgm_32.render('Pause', False, res.COLOR_BLACK), UI.Menu.text_pause)
        pygame.draw.rect(game.screen, res.COLOR_BLACK, UI.Menu.button_resume, 2)
        game.screen.blit(res.font_neodgm_32.render('Resume [R]', False, res.COLOR_BLACK), UI.Menu.text_resume)
        pygame.draw.rect(game.screen, res.COLOR_BLACK, UI.Menu.button_exit, 2)
        game.screen.blit(res.font_neodgm_32.render('Exit [E]', False, res.COLOR_BLACK), UI.Menu.text_exit)
