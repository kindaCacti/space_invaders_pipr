from entity import Entity
from bullet import Bullet
from settings import Settings


class ShootingEntity(Entity):
    def __init__(self,
                 position: list,
                 speed: list,
                 size: int,
                 image: str,
                 bullet_speed_coefficient: int,
                 states: int,
                 score: int):
        super().__init__(position, speed, size, image)
        self._bullet_speed_coefficient = bullet_speed_coefficient
        self._state = 0
        self._states = states
        self._score = score

    @property
    def bullet_speed_coefficient(self):
        return self._bullet_speed_coefficient

    @property
    def state(self):
        return self._state

    def shoot(self, speed: int = Settings.bullet_speed):
        dist = 1
        y_position = self.position[1] - dist
        if self.bullet_speed_coefficient == 1:
            y_position += 2 * dist + self.size
        return Bullet([self.position[0] + self.size / 2, y_position],
                      sender=self.bullet_speed_coefficient,
                      speed=[Settings.bullet_speed[0],
                             Settings.bullet_speed[1] *
                             self.bullet_speed_coefficient])

    def is_hit(self, entity: Entity):
        if entity.sender == self.bullet_speed_coefficient:
            return False, True
        if (entity.position[0] + entity.size >= self.position[0] and
                entity.position[0] <= self.position[0] + self.size and
                entity.position[1] + entity.size >= self.position[1] and
                entity.position[1] <= self.position[1] + self.size):
            return True, True
        return False, True

    def next_state(self):
        self._state += 1
        if self._state == self._states:
            return self._score
        return None
