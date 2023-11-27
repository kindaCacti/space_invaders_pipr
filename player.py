import pygame
from settings import SETTINGS


class PLAYER:
    _movement_speed = 300

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self, nx):
        self._x += nx
        self._x = max(0, self._x)
        self._x = min(SETTINGS.screen_width, self._x)

    @property
    def xPos(self):
        return self._x

    @property
    def yPos(self):
        return self._y

    @property
    def position(self):
        return pygame.Vector2(self._x, self._y)

    @property
    def movement_speed(self):
        return self._movement_speed

    def get_show_parameters(self):
        return {"position": self.position,
                "color": "blue",
                "radius": 25}
