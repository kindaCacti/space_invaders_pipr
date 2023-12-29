from shooting_entity import ShootingEntity
from settings import Settings


class Player(ShootingEntity):
    """
    Class Player used to represent Players

    Attributes:
    -----------
    last_shot: float
        time of last shot

    Methods:
    --------
    write_to_file(content: str)
        method writing content to file
    read_file()
        method reading frome file
    """
    def __init__(self, position: list):
        super().__init__(position, Settings.player_speed, Settings.player_size,
                         Settings.player_image, -1, 1, 0)
        self._last_shot = -1000

    def player_shoot(self, time: float):
        """checks if a player can shoot a bullet and if can shoots it"""
        if time - self._last_shot < .3:
            return None
        self._last_shot = time
        return self.shoot()
