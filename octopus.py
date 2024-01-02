from enemy import Enemy
from settings import Settings


class Octopus(Enemy):
    """
    Class Octopus used to represent octopus type of enemy.
    """
    def __init__(self, position: list, tick_offset: float):
        try:
            if (type(position) is not list or
               type(tick_offset) is not float):
                raise TypeError

        except TypeError:
            print("wrong types passed to Octopus")
            quit()

        super().__init__(position, 20, Settings.enemy_image)
        self._set_ticks(tick_offset)
