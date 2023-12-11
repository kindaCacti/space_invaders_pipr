from entity import Entity
from settings import Settings


class Bullet(Entity):
    def __init__(self, position: list, sender: int, speed: list = Settings.bullet_speed, size: int = Settings.bullet_size, image: int = Settings.bullet_image):
        super().__init__(position, speed, size, image)
        self._sender = sender
    
    @property
    def sender(self):
        return self._sender