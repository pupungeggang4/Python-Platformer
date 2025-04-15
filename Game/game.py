import pygame, sys
import scenetitle, scenefield
import res

class Game():
    def run(self):
        self.init()
        self.main()

    def init(self):
        pygame.init()
        pygame.font.init()
        self.resolution = [1280, 800]
        self.screen = pygame.display.set_mode(self.resolution, pygame.SCALED, vsync=1)
        pygame.display.set_caption('Platformer')
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.scene = 'field'
        self.state = ''

    def main(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)

        elif self.scene == 'field':
            scenefield.loop(self)

Game().run()