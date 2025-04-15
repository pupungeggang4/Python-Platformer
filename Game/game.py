import pygame, sys

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

    def main(self):
        while True:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

Game().run()