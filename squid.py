from enemy import Enemy
from settings import Settings


class Squid(Enemy):
    """
    Class Squid used to represent squid type of enemy.
    """
    def __init__(self, position: list):
        super().__init__(position, 40, Settings.squid_image)
