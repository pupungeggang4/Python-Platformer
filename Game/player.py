from primitive import *

class Player():
    def __init__(self):
        self.rect = Rect2D(100, 100, 64, 64)
        self.life = 0
        self.coin = 0