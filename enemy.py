import pygame
from settings import SETTINGS


class ENEMIES:
    def _set_enemies(self, ex, ey, x_buffor, y_buffor):
        self._mx = 10
        self._my = 10
        self._ex = ex
        self._ey = ey
        self._time_passed = 0
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

    def get_enemies_parameters(self):
        return [enemy.get_show_parameters() for enemy in self._enemies]
    
    def next_move(self, moves):
        for enemy in self._enemies:
            enemy.move(moves)

    def generate_move(self):
        print(f'{self._ex} : {self._ey}\n')
        if self._ex!=self._mx and self._ey%2:
            self._ex += 1
            return [1, 0]
        elif self._ex!=1 and self._ey%2!=1:
            self._ex -= 1
            return [-1, 0]
        else:
            self._ey += 1
            return[0, 1]
        
    
    def move(self, tick):
        self._time_passed += tick
        print(self._time_passed)
        move = [0,0]
        if self._time_passed//1 >= 1:
            self._time_passed -= 1
            move = self.generate_move()
        self.next_move(move)


class ENEMY:
    def __init__(self, x, y, msx, msy):
        self._x = x
        self._y = y
        self._msx = msx
        self._msy = msy

    @property
    def position(self):
        return pygame.Vector2(self._x, self._y)

    def get_show_parameters(self):
        return {"position": self.position,
                "color": "red",
                "radius": SETTINGS.enemy_size}
    
    def move(self, move):
        self._x += move[0] * self._msx
        self._y += move[1] * self._msy
