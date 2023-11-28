import pygame
from settings import SETTINGS
from random import randint
from bullet import BULLET
import itertools


class ENEMIES:
    def _set_enemies(self, ex, ey, x_buffor, y_buffor):
        self._mx = 10
        self._my = 10
        self._ex = ex
        self._ey = ey
        self._time_passed = 0
        self._time_last_shot = 0
        self._last_time = 0
        self._enemies = []
        move_space_x = (SETTINGS.screen_width-x_buffor)/ex
        move_space_y = (SETTINGS.screen_height-y_buffor)/ey
        for i in range(ex):
            for j in range(ey):
                self._enemies.append(ENEMY(i*move_space_x+SETTINGS.enemy_size,
                                           j*move_space_y+SETTINGS.enemy_size,
                                           move_space_x,
                                           move_space_y))

    def __init__(self, ex, ey, x_buffor, y_buffor):
        self._set_enemies(ex, ey, x_buffor, y_buffor)

    def get_enemies(self):
        return list(self._enemies)

    def get_enemies_parameters(self):
        return [enemy.get_show_parameters() for enemy in self._enemies]

    def next_move(self, moves):
        for enemy in self._enemies:
            enemy.move(moves)

    def generate_move(self):
        # print(f'{self._ex} : {self._ey}\n')
        if self._ex != self._mx and self._ey % 2:
            self._ex += 1
            return [1, 0]
        elif self._ex != 1 and self._ey % 2 != 1:
            self._ex -= 1
            return [-1, 0]
        else:
            self._ey += 1
            return [0, 1]

    def shoot(self):
        if self._time_passed - self._time_last_shot >= 2.5:
            # print("hii")
            self._time_last_shot += 2
            random = randint(0, len(self._enemies) - 1)
            return self._enemies[random].shoot()
        return None

    def move(self, tick):
        self._time_passed += tick
        # print(self._time_passed)
        move = [0, 0]
        if self._time_passed//1 != self._last_time:
            self._last_time += 1
            move = self.generate_move()
        self.next_move(move)
        return self.shoot()

    def remove(self, enemy):
        print(enemy)
        pos = -1
        for i in range(len(self._enemies)):
            if self._enemies[i].id == enemy:
                pos = i
                break
        if pos == -1:
            return None
        del self._enemies[pos]


class ENEMY:
    id_obj = itertools.count()

    def __init__(self, x, y, msx, msy):
        self._x = x
        self._y = y
        self._msx = msx
        self._msy = msy
        self._id = next(ENEMY.id_obj)

    @property
    def position(self):
        return pygame.Vector2(self._x, self._y)

    @property
    def id(self):
        return self._id

    def get_show_parameters(self):
        return {"position": self.position,
                "color": "red",
                "radius": SETTINGS.enemy_size}

    def move(self, move):
        self._x += move[0] * self._msx
        self._y += move[1] * self._msy

    def shoot(self):
        return BULLET(self._x, self._y-SETTINGS.enemy_size, 1)

    def is_hit(self, bullet_position):
        # print("here")
        if (bullet_position[1] + SETTINGS.bullet_size < self._y + SETTINGS.enemy_size and
                bullet_position[1] - SETTINGS.bullet_size > self._y - SETTINGS.enemy_size):
            print("almost hit")
            if (bullet_position[0] + SETTINGS.bullet_size > self._x - SETTINGS.enemies_x and
                    bullet_position[0] - SETTINGS.bullet_size < self._x - SETTINGS.enemies_x):
                print("hit")
                return True
        return False
