from entity import Entity
from settings import Settings


class Bullet(Entity):
    """
    Class Bullet used to represent bullets.

    Attributes:
    -----------
    position: list
        list representing x and y position of a bullet
    sender: int
        integer representing who sent the bullet
    """

    def __init__(self, position: list, sender: int, speed_coefficient: int):
        super().__init__(position,
                         self.set_actual_speed(Settings.bullet_speed, speed_coefficient),
                         Settings.bullet_size, Settings.bullet_image)
        self._sender = sender

    @property
    def sender(self):
        return self._sender

    def set_actual_speed(self, speed: list, speed_coefficient: int):
        return [speed[0], speed[1] * speed_coefficient]
