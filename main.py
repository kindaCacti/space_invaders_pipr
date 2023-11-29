import pygame
from player import PLAYER
from enemy import ENEMIES
from settings import SETTINGS

enemies = ENEMIES(SETTINGS.enemies_x,
                  SETTINGS.enemies_y,
                  SETTINGS.screen_width_buffor,
                  SETTINGS.screen_height_buffor)
bullets = []
pygame.init()
screen = pygame.display.set_mode((SETTINGS.screen_width,
                                  SETTINGS.screen_height))
clock = pygame.time.Clock()
running = True
ship = PLAYER(SETTINGS.screen_width / 2, SETTINGS.screen_height-50)
dt = 0
to_show = []
clicked = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        ship.move(-ship.movement_speed * dt)
    if keys[pygame.K_d]:
        ship.move(ship.movement_speed * dt)
    if keys[pygame.K_w] and not clicked:
        bullets.append(ship.shoot())
        clicked = True
    elif not keys[pygame.K_w]:
        clicked = False

    to_delete = []
    nb = []
    for bullet in bullets:
        bullet.move(dt)
        tmp2 = bullet.does_hit("player", enemies.get_enemies())
        if tmp2 is not None:
            if bullet.sender == -1:
                print(tmp2)
                to_delete.append(tmp2)
        if bullet.within_screen():
            nb.append(bullet)
    bullets = list(nb)
    screen.fill("black")

    for i in to_delete:
        enemies.remove(i)

    tmp = enemies.move(dt)
    if tmp is not None:
        bullets.append(tmp)

    # to_show.append(ship.get_show_parameters())
    # tmp = enemies.get_enemies_parameters()
    # for i in tmp:
    #     to_show.append(i)
    # for bullet in bullets:
    #     to_show.append(bullet.get_show_parameters())
    # print(len(bullets))

    # for i in to_show:
    #     pygame.draw.circle(screen, i["color"], i["position"], i["radius"])

    for bullet in bullets:
        bullet.show_bullet(screen)
    ship.show_ship(screen)
    enemies.show_enemies(screen)
    to_show.clear()
    pygame.display.flip()

    dt = (clock.tick(SETTINGS.fps)/1000)

pygame.quit()
