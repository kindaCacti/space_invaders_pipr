from enemy import Enemy
from player import Player
from bullet import Bullet
from settings import Settings
from blocker import Blocker
from random import randint
import pygame


def show_all(screen: object, *entities: list):
    for group in entities:
        for entity in group:
            entity.show(screen)

def move_entities(delta_time: float, coefficient: int, entities: list):
    for entity in entities:
        entity.move(delta_time, coefficient)

def shoot_entities(entities: list):
    if len(entities) == 0:
        return
    entity = entities[randint(0,len(entities)-1)]
    bullets.append(entity.shoot())

def update_hit(bullets: list, *entities: list):
    hit = []
    for group in entities:
        for entity in group:
            for bullet in bullets:
                if entity.is_hit(bullet):
                    hit.append(entity)
                    bullet.set_position([bullet.position[0], -1000])
    return hit

def remove_entities(hit, *entities):
    removed_list = []
    i = 0
    for group in entities:
        for entity in group:
            if entity in hit:
                if entity.next_state() is None:
                    removed_list.append(entity)
                continue
            removed_list.append(entity)
        i+=1
    return removed_list

def load_invaders():
    invaders = []
    for y in range(Settings.rows_of_invaders):
        for x in range(Settings.invaders_in_row):
            invaders.append(Enemy([10+50*x, 30+50*y]))
    return invaders

bullets = []
enemies = load_invaders()
players = [Player([270, 550])]
blockers = [Blocker([60, 470]),
            Blocker([170, 470]),
            Blocker([280, 470]),
            Blocker([390, 470]),
            Blocker([500, 470])]

screen = pygame.display.set_mode((Settings.window_width,
                                  Settings.window_height))
clock = pygame.time.Clock()
delta_time = 0
running = True
player_shot = False
time_running = 0
last_shot = -1

while running:
    time_running += delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        move_entities(delta_time, -1, players)
    if keys[pygame.K_d]:
        move_entities(delta_time, 1, players)
    if keys[pygame.K_w] and not player_shot:
        shoot_entities(players)
        player_shot = True
    elif not keys[pygame.K_w]:
        player_shot = False

    tmp = remove_entities(update_hit(bullets, players), players)
    players = tmp
    tmp = remove_entities(update_hit(bullets, enemies), enemies)
    enemies = tmp
    tmp = remove_entities(update_hit(bullets, blockers), blockers)
    blockers = tmp
    new_bullets = []
    for bullet in bullets:
        if (bullet.position[1] < -100 - Settings.bullet_size or
                bullet.position[1] > Settings.window_height + Settings.bullet_size + 100):
            continue
        new_bullets.append(bullet)
    bullets = new_bullets
    move_entities(delta_time, 1, bullets)
    move_entities(delta_time, 1, enemies)
    if((time_running-.5)//1 != last_shot):
        last_shot += 1
        shoot_entities(enemies)
    screen.fill("black")

    for blocker in blockers:
        blocker.update_blocker()
    
    if(len(players) == 0):
        running = False
        continue
    show_all(screen, bullets, enemies, players, blockers)

    pygame.display.flip()
    delta_time = (clock.tick(Settings.fps)/1000)

pygame.quit()
