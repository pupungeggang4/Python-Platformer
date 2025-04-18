import pygame, sys
import res

from primitive import *
from prototype import *
from player import *
from field import *

import scenetitle
import scenefield

class Game():
    def run(self):
        self.init()
        self.main()

    def init(self):
        pygame.init()
        pygame.font.init()

        res.font_neodgm_32 = pygame.font.Font('Font/neodgm.ttf', 32)

        self.load_image()

        self.resolution = [1280, 800]
        self.screen = pygame.display.set_mode(self.resolution, pygame.SCALED, vsync=1)
        pygame.display.set_caption('Platformer')
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.scene = 'title'
        self.state = ''
        self.menu = False

        self.field = Field()
        self.player = Player()

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

            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                button = event.button

                if self.scene == 'title':
                    scenetitle.mouse_up(self, button, mouse)
                if self.scene == 'field':
                    scenefield.mouse_up(self, button, mouse)

            if event.type == pygame.KEYDOWN:
                key = event.key

                if self.scene == 'title':
                    scenetitle.key_down(self, key)
                elif self.scene == 'field':
                    scenefield.key_down(self, key)

            if event.type == pygame.KEYUP:
                key = event.key

                if self.scene == 'title':
                    scenetitle.key_up(self, key)
                elif self.scene == 'field':
                    scenefield.key_up(self, key)

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)

        elif self.scene == 'field':
            scenefield.loop(self)

    def load_image(self):
        res.Image.coin = pygame.image.load('Image/Coin.png')

    def point_inside_rect_UI(self, point, rect):
        return point[0] > rect[0] and point[0] < rect[0] + rect[2] and point[1] > rect[1] and point[1] < rect[0] + rect[2]

Game().run()