from shooting_entity import ShootingEntity
from settings import Settings


class Squid(ShootingEntity):
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

    Methods:
    --------
    move(delta_time: float, speed_coefficient: int)
        method taking care of a specific movement of a squid
    """
    def __init__(self, position: list):
        super().__init__(position, Settings.enemy_speed,
                         Settings.squid_size, Settings.squid_image, 1, 1, 40)
        self._ticks = 0
        self._done_ticks = 0
        self._speed_coeff = 1

    def move(self, delta_time: float, speed_coefficient: int):
        # Moves an entity depending on given delta_time
        self._ticks += delta_time
        if self._ticks > 1:
            self._ticks -= 1
            self._done_ticks += 1
            if self._done_ticks == 11:
                self._position[1] += 60
                self._speed_coeff *= -1
                self._done_ticks = 0
            else:
                self._position[0] += 30*self._speed_coeff
