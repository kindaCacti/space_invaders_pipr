from entity import Entity
from settings import Settings


class Bullet(Entity):
    """
    Class Bullet used to represent bullets.

    Attributes:
    -----------
    position: list
        list representing x and y position of a bullet
    sender: int
        integer representing who sent the bullet

    Methods:
    -----------
    move_off_screen()
        moves bullet off screen
    """

    def __init__(self, position: list, sender: int, speed_coeff: int):
        try:
            if (type(position) is not list or
               type(sender) is not int or
               type(speed_coeff) is not int):
                raise TypeError

        except TypeError:
            print("wrong type passed to Bullet")
            quit()

        super().__init__(position,
                         self.new_speed(Settings.bullet_speed, speed_coeff),
                         Settings.bullet_size, Settings.bullet_image)
        self._sender = sender

    @property
    def sender(self):
        return self._sender

    def new_speed(self, speed: list, speed_coefficient: int):
        try:
            if (type(speed) is not list or
               type(speed_coefficient) is not int):
                raise TypeError
            return [speed[0], speed[1] * speed_coefficient]
        except TypeError:
            print("wront type passed to function Bullet.new_speed()")
            pass

    def move_off_screen(self):
        # moves bullet off screen
        self._position[0] = -1000
        self._position[1] = -1000
