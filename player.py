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
    player_shoot(time: float)
        checks if a player can shoot a bullet and if can shoots it
    """
    def __init__(self, position: list):
        try:
            if type(position) is not list:
                raise TypeError

        except TypeError:
            print("wrong types passed to Player")
            quit()

        super().__init__(position, Settings.player_speed,
                         Settings.player_size,
                         Settings.player_image, -1, 1, 0)
        self._last_shot = -1000

    def player_shoot(self, time: float):
        """checks if a player can shoot a bullet and if can shoots it"""
        try:
            time = float(time)

        except Exception:
            print("wrong types passed to Player.player_shoot()")
            return None

        if time - self._last_shot < .3:
            return None
        self._last_shot = time
        return self.shoot()
