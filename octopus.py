from enemy import Enemy
from settings import Settings


class Octopus(Enemy):
    """
    Class Squid used to represent squid type of enemy.

    Attributes:
    -----------
    ticks: float
        number of ticks since squid spawned
    done_ticks: int
        number of seconds passed
    speed_coeff: int
        speed coefficient of squid (does it go left or right)
    """
    def __init__(self, position: list):
        super().__init__(position, 20, Settings.enemy_image)
