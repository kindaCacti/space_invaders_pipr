from enemy import Enemy
from settings import Settings


class Squid(Enemy):
    """
    Class Squid used to represent squid type of enemy.
    """
    def __init__(self, position: list, tick_offset: int):
        try:
            if (type(position) is not list or
               type(tick_offset) is not int):
                raise TypeError

        except TypeError:
            print("wrong types passed to Squid")

        super().__init__(position, 40, Settings.squid_image)
        self._set_ticks(tick_offset)
