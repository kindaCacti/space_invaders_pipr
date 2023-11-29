import pygame
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

pygame.init()
clock = pygame.time.Clock()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

player = Player(50, 50, 200, 200, (255, 255, 255))
enemy = Enemy(50, 50, 50, 50)

enemy_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
screen.fill((200,200,200))
player_group.add(player)
enemy_group.add(enemy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    player_group.draw(screen)
    clock.tick(60)
