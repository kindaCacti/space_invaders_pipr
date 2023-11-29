import pygame
from settings import SETTINGS
from bullet import BULLET


class PLAYER():
    _movement_speed = 300

    def __init__(self, x, y):
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image,
                                            (SETTINGS.player_size * 2,
                                             SETTINGS.player_size * 2))
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
                "radius": SETTINGS.player_size}

    def show_ship(self, screen):
        screen.blit(self.image, (self._x - SETTINGS.player_size,
                                 self._y - SETTINGS.player_size))

    def shoot(self):
        return BULLET(self._x, self._y - 25, -1)
