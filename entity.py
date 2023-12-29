from settings import Settings
import pygame


class Entity:
    """
    Class ShootingEntity used to represent entity that can shoot and be shot

    Attributes:
    -----------
    position: list
        list containing x and y position of an entity
    speed: list
        list containing x and y speed of an entity
    size: int
        integer representing size of an entity
    image: str
        string representing a path to an image shown as an entity

    Methods:
    --------
    set_position(new_position: list)
        sets position to given position,
        keeping the position within screen bounds
    move(time_difference: float, coefficient: int)
        moves an entity based on coefficient and time_difference
    show(screen: object)
        shows an entity
    load_image(new_image: object)
        loads new image as an entity sprite
    """
    def __init__(self, position: list, speed: list, size: int, image: int):
        self._position = position
        self._speed = speed
        self._size = size
        self.load_image(image)

    @property
    def position(self):
        return self._position

    @property
    def size(self):
        return self._size

    @property
    def image(self):
        return self._image

    @property
    def speed(self):
        return self._speed

    def set_position(self, new_position: list):
        # sets position to given position,
        # keeping the position within screen bounds
        self._position = [min(max(0, new_position[0]), Settings.window_width - self.size),
                          new_position[1]]

    def move(self, time_difference: float, coefficient: int):
        # moves an entity keeping it within bounds
        self.set_position([self.position[0] + self.speed[0] * time_difference * coefficient,
                           self.position[1] + self.speed[1] * time_difference * coefficient])

    def show(self, screen: object):
        # shows an entity
        screen.blit(self.image, (self.position[0], self.position[1]))

    def load_image(self, new_image: object):
        # loads new image as an entity sprite
        self._image = pygame.image.load(new_image)
        self._image = pygame.transform.scale(self._image, (self.size,
                                                           self.size))
