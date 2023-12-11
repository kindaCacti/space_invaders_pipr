from shooting_entity import ShootingEntity
from settings import Settings


class Player(ShootingEntity):
    def __init__(self,
                 position: list,
                 bullet_speed_coefficient: int = -1,
                 speed: list = Settings.player_speed,
                 size: int = Settings.player_size,
                 image: str = Settings.player_image,
                 states: int = 1):
        super().__init__(position, speed, size, image, bullet_speed_coefficient, states)