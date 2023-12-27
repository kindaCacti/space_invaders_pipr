from shooting_entity import ShootingEntity
from settings import Settings


class Squid(ShootingEntity):
    def __init__(self,
                 position: list,
                 speed: list = Settings.enemy_speed,
                 size: int = Settings.squid_size,
                 image: str = Settings.squid_image,
                 bullet_speed_coefficient: int = 1,
                 states: int = 1,
                 score: int = 40):
        super().__init__(position,
                         speed,
                         size,
                         image,
                         bullet_speed_coefficient,
                         states,
                         score)
        self._ticks = 0
        self._done_ticks = 0
        self._speed_coeff = 1

    def move(self, delta_time: float, speed_coefficient: float):
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
