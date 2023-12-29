from shooting_entity import ShootingEntity
from settings import Settings


class Blocker(ShootingEntity):
    """
    Class Blocker used to represent blocker.

    Attributes:
    -----------
    images: list
        list of strings paths to images representing set states of blockers

    Methods:
    --------
    update_blocker()
        method loading image of current state of blocker
    is_hit(entity: list)
        method checking if blocker was hit
    """
    def __init__(self, position: list):
        self._images = [Settings.blocker_1,
                        Settings.blocker_2,
                        Settings.blocker_3]
        super().__init__(position, [0, 0], Settings.blocker_size,
                         self._images[0], 0, 3, 0)

    def update_blocker(self):
        # method loading image of current state of blocker
        self.load_image(self._images[self.state])

    def is_hit(self, entity: object):
        # returns if blocker was hit and if its state should change
        if entity.sender == self.bullet_speed_coefficient:
            return False, False
        if (entity.position[0] + entity.size >= self.position[0] and
                entity.position[0] <= self.position[0] + self.size and
                entity.position[1] + entity.size >= self.position[1] and
                entity.position[1] <= self.position[1] + self.size):
            return True, (entity.sender == -1)
        return False, False
