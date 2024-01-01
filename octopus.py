from enemy import Enemy
from settings import Settings


class Octopus(Enemy):
    """
    Class Octopus used to represent octopus type of enemy.
    """
    def __init__(self, position: list):
        super().__init__(position, 20, Settings.enemy_image)
