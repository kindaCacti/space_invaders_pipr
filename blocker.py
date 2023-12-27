from shooting_entity import ShootingEntity
from settings import Settings


class Blocker(ShootingEntity):
    def __init__(self,
                 position: list,
                 speed: list = [0, 0],
                 size: int = Settings.blocker_size,
                 image: list = None,
                 state: int = 0,
                 bullet_speed_coefficient: int = 0,
                 states: int = 3,
                 score: int = 0):
        if image is None:
            image = [Settings.blocker_1,
                     Settings.blocker_2,
                     Settings.blocker_3]
        self._images = image
        super().__init__(position,
                         speed,
                         size,
                         self._images[state],
                         bullet_speed_coefficient,
                         states,
                         score)
        self._images = image

    def update_blocker(self):
        self.load_image(self._images[self.state])

    def is_hit(self, entity: object):
        if entity.sender == self.bullet_speed_coefficient:
            return False, True
        if (entity.position[0] + entity.size >= self.position[0] and
                entity.position[0] <= self.position[0] + self.size and
                entity.position[1] + entity.size >= self.position[1] and
                entity.position[1] <= self.position[1] + self.size):
            return True, (entity.sender == -1)
        return False, True
