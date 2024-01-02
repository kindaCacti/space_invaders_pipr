from shooting_entity import ShootingEntity
from settings import Settings


class Enemy(ShootingEntity):
    """
    Class Enemy used to represent first type of enemy.

    Attributes:
    -----------
    ticks: float
        number of ticks since enemy spawned
    done_ticks: int
        number of seconds passed
    speed_coeff: int
        speed coefficient of an enemy (does it go left or right)

    Methods:
    --------
    move(delta_time: float, speed_coefficient: int)
        method taking care of a specific movement of an enemy
    _set_ticks(ticks: float)
        method setting tick offset for specific enemy
    """
    def __init__(self, position: list, score: int, image: str):
        try:
            if (type(position) is not list or
               type(score) is not int or
               type(image) is not str):
                raise TypeError

        except TypeError:
            print("wrong type passed to Enemy")

        super().__init__(position, Settings.enemy_speed, Settings.enemy_size,
                         image, 1, 1, score)
        self._ticks = 0
        self._done_ticks = 0
        self._speed_coeff = 1

    def _set_ticks(self, ticks: float):
        # sets ticks to offset movement
        print(ticks)
        self._ticks = ticks

    def move(self, delta_time: float, speed_coefficient: float):
        # moves enemy based on delt_time
        try:
            if delta_time < 0:
                raise ValueError
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

        except ValueError:
            print("delta_time cannot be less than zero in Enemy.move()")
            pass
