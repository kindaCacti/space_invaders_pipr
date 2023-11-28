import pygame
from player import PLAYER
from enemy import ENEMIES

enemies = ENEMIES(5, 5, 200, 200)
bullets = []
pygame.init()
screen = pygame.display.set_mode((500, 650))
clock = pygame.time.Clock()
running = True
ship = PLAYER(250, 600)
dt = 0
to_show = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    enemies.move(dt)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        ship.move(-ship.movement_speed * dt)
    if keys[pygame.K_d]:
        ship.move(ship.movement_speed * dt)
    if keys[pygame.K_w]:
        bullets.append(ship.shoot())
    
    for bullet in bullets:
        bullet.move(dt)
    screen.fill("black")

    to_show.append(ship.get_show_parameters())
    tmp = enemies.get_enemies_parameters()
    for i in tmp:
        to_show.append(i)
    for bullet in bullets:
        to_show.append(bullet.get_show_parameters())

    for i in to_show:
        pygame.draw.circle(screen, i["color"], i["position"], i["radius"])
    to_show.clear()
    pygame.display.flip()

    dt = (clock.tick(60)/1000)

pygame.quit()
