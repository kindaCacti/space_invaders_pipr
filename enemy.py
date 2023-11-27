import pygame
from settings import SETTINGS


class ENEMIES:
    def _set_enemies(self, ex, ey, x_buffor, y_buffor):
        self._enemies = []
        move_space_x = (SETTINGS.screen_width-x_buffor)/ex
        move_space_y = (SETTINGS.screen_height-y_buffor)/ey
        for i in range(ex):
            for j in range(ey):
                self._enemies.append(ENEMY(i*move_space_x+SETTINGS.enemy_size,
                                           j*move_space_y+SETTINGS.enemy_size))

    def __init__(self, ex, ey, x_buffor, y_buffor):
        self._set_enemies(ex, ey, x_buffor, y_buffor)

    def get_enemies_parameters(self):
        return [enemy.get_show_parameters() for enemy in self._enemies]


class ENEMY:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def position(self):
        return pygame.Vector2(self._x, self._y)

    def get_show_parameters(self):
        return {"position": self.position,
                "color": "red",
                "radius": SETTINGS.enemy_size}

    def move(self, nx, ny):
        self._x += nx
        self._y += ny
