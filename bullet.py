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
    def __init__(self, position: list, sender: int):
        super().__init__(position, Settings.bullet_speed,
                         Settings.bullet_size, Settings.bullet_image)
        self._sender = sender

    @property
    def sender(self):
        return self._sender
