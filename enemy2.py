import pygame
from entity import Entity
from bullet import BULLET


class Enemy(Entity):
    def __init__(self, x, y, width, height, image_path):
        super().__init__(x, y, width, height, image_path)
    
    def shoot(self):
        return BULLET(self._x, self._y, 1)