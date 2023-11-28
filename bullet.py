import pygame
from settings import SETTINGS

class BULLET:
    def __init__(self, x, y, speed_coefficient):
        self._x = x
        self._y = y
        self._speed = SETTINGS.bullet_speed*speed_coefficient

    @property
    def position(self):
        return pygame.Vector2(self._x, self._y)

    def get_show_parameters(self):
        return {"position": self.position,
                "color": "white",
                "radius": SETTINGS.bullet_size}
    
    def move(self, tick):
        self._y += self._speed*tick