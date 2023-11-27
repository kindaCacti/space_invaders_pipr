import pygame
from player import PLAYER

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
ship = PLAYER(250, 400)
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        ship.move(-ship.movement_speed * dt)
    if keys[pygame.K_d]:
        ship.move(ship.movement_speed * dt)
    screen.fill("red")
    pygame.draw.circle(screen, "blue", ship.position, 40)
    pygame.display.flip()

    dt = (clock.tick(60)/1000)

pygame.quit()
