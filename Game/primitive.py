import pygame

import res

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return
    
    @staticmethod
    def add(vec1, vec2):
        return Vector2D(vec1.x + vec2.x, vec1.y + vec2.y)

    @staticmethod
    def sub(vec1, vec2):
        return Vector2D(vec1.x - vec2.x, vec1.y - vec2.y)
    
    @staticmethod
    def mul(vec, a):
        return Vector2D(vec.x * a, vec.y * a)

class Rect2D():
    def __init__(self, x, y, w, h):
        self.position = Vector2D(x, y)
        self.size = Vector2D(w, h)

    def collide_with_shape(self, shape):
        if type(shape) == Rect2D:
            diff = Vector2D.sub(self.position, shape.position)
            sizeSum = Vector2D.mul(Vector2D.add(self.size, shape.size), 0.5)
            return abs(diff.x) < sizeSum.x and abs(diff.y) < sizeSum.y

    def render(self, sur):
        pygame.draw.rect(sur, res.COLOR_BLACK, [self.position.x - self.size.x / 2, self.position.y - self.size.y / 2, self.size.x, self.size.y], 1)

    @staticmethod
    def two_rect_collide(rect1, rect2):
        diff = Vector2D.sub(rect1.position, rect2.position)
        sizeSum = Vector2D.mul(Vector2D.add(rect1.size, rect2.size), 0.5)

        return abs(diff.x) < sizeSum.x and abs(diff.y) < sizeSum.y

class Circle2D():
    def __init__(self, x, y, r):
        self.position = Vector2D(x, y)
        self.radius = r
