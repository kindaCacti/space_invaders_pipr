import pygame
from settings import SETTINGS


class BULLET:
    def __init__(self, x, y, speed_coefficient):
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image,
                                            (SETTINGS.bullet_size * 2,
                                             SETTINGS.bullet_size * 2))
        self._x = x
        self._y = y
        self._speed = SETTINGS.bullet_speed*speed_coefficient
        self._sender = speed_coefficient  # sender 1 is enemy and -1 is player

    @property
    def position(self):
        return pygame.Vector2(self._x, self._y)

    @property
    def sender(self):
        return self._sender

    def get_show_parameters(self):
        return {"position": self.position,
                "color": "white",
                "radius": SETTINGS.bullet_size}

    def show_bullet(self, screen):
        screen.blit(self.image, (self._x-SETTINGS.bullet_size,
                                 self._y-SETTINGS.bullet_size))

    def move(self, tick):
        self._y += self._speed*tick

    def within_screen(self):
        is_within = True
        if self._y < 0-SETTINGS.bullet_size:
            is_within = False
        if self._y > SETTINGS.screen_height+SETTINGS.bullet_size:
            is_within = False
        return is_within

    def does_hit(self, player, enemies):
        if self._sender == -1:
            for enemy in enemies:
                if enemy.is_hit([self._x, self._y]):
                    self._y = -1000
                    return enemy.id
        # elif self._sender == 1:
        #    if player.is_hit([self._x, self._y]):
        #        self._y = -1000
        #        return player
        return None
