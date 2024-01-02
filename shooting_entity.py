from entity import Entity
from bullet import Bullet


class ShootingEntity(Entity):
    """
    Class ShootingEntity used to represent entity that can shoot and be shot

    Attributes:
    -----------
    bullet_speed_coefficient: int
        integer representing which way the bullet goes
    state: int
        integer representing which state entity is on
    states: int
        integer representing number of states of squid
    score: int
        integer representing score gained after killing squid

    Methods:
    --------
    shoot(speed: int)
        method returning a bullet that was shot
    is_hit(entity: list)
        method checking if blocker was hit
    """
    def __init__(self, position: list, speed: list, size: int, image: str,
                 bullet_speed_coefficient: int, states: int, score: int):
        try:
            if (type(position) is not list or
               type(speed) is not list or
               type(size) is not int or
               type(image) is not str or
               type(bullet_speed_coefficient) is not int or
               type(states) is not int or
               type(score) is not int):
                raise TypeError

        except Exception:
            print("wrong types passed")
            quit()

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

    def shoot(self) -> Bullet:
        # Returns a bullet that given entity shot
        dist = 1
        y_position = self.position[1] - dist
        if self.bullet_speed_coefficient == 1:
            y_position += 2 * dist + self.size
        return Bullet([self.position[0] + self.size / 2, y_position],
                      self.bullet_speed_coefficient,
                      self.bullet_speed_coefficient)

    def is_hit(self, entity: Entity) -> [bool, bool]:
        # Returns if an entity was shot and if should its state change
        try:
            if entity.sender == self.bullet_speed_coefficient:
                return False, False
            if (entity.position[0] + entity.size >= self.position[0] and
                    entity.position[0] <= self.position[0] + self.size and
                    entity.position[1] + entity.size >= self.position[1] and
                    entity.position[1] <= self.position[1] + self.size):
                return True, True
            return False, False

        except Exception:
            print("Error in ShootingEntity.is_hit()")
            pass

    def next_state(self):
        # Changes a state of an entity
        self._state += 1
        if self._state == self._states:
            return self._score
        return None
