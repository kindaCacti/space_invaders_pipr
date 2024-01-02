from enemy import Enemy
from player import Player
from bullet import Bullet
from settings import Settings
from blocker import Blocker
from random import randint
from file_manager import FileManager
import pygame

pygame.init()
fm = FileManager("best_score.txt")


def show_all(screen: object, *entities: list):
    # shows all given entities
    for group in entities:
        for entity in group:
            entity.show(screen)


def move_entities(delta_time: float, coefficient: int, entities: list):
    # moves all entities based on delta_time and coefficient
    for entity in entities:
        entity.move(delta_time, coefficient)


def shoot_entities(entities: list, bullets: list[Bullet]):
    # shoots a bullet by entites
    if len(entities) == 0:
        return
    entity = entities[randint(0, len(entities)-1)]
    bullets.append(entity.shoot())


def player_shoot(player: Player, time: float, bullets: list[Bullet]):
    # shoots a bullet by a player
    tmp = player.player_shoot(time)
    if tmp is None:
        return
    bullets.append(tmp)


def update_hit(bullets: list, *entities: list):
    # checks if any entity given has been hit by a bullet
    hit = []
    for group in entities:
        for entity in group:
            for bullet in bullets:
                hit_bool, changes = entity.is_hit(bullet)
                if hit_bool:
                    if changes:
                        hit.append(entity)
                    bullet.move_off_screen()
    return hit


def remove_entities(hit: list, score: int, *entities: list):
    # removes entities set and returns new score after killing them
    removed_list = []
    i = 0
    for group in entities:
        for entity in group:
            if entity in hit:
                tmp = entity.next_state()
                if tmp is None:
                    removed_list.append(entity)
                else:
                    score += tmp
                continue
            removed_list.append(entity)
        i += 1
    return removed_list, score


def load_invaders():
    # loads invaders
    invaders = []
    for y in range(Settings.rows_of_invaders):
        for x in range(Settings.invaders_in_row):
            if y == 0 or y == 1:
                invaders.append(Enemy([10+50*x, 30+50*y],
                                      Settings.squid_score,
                                      Settings.squid_image,
                                      y*.1))
                continue
            invaders.append(Enemy([10+50*x, 30+50*y],
                            Settings.enemy_score,
                            Settings.enemy_image,
                            y*.1))
    return invaders


def show_text(screen: object, content: str, position: tuple,
              size: int = 24, color: str = "white"):
    # shows given content on given position in given font size and font color
    font = pygame.font.Font(None, size)
    image = font.render(content, True, color)
    screen.blit(image, position)
    return image


def show_score(screen: object, score: int):
    # shows score on screen
    show_text(screen, f"score: {score}", (20, 20))


def show_best_score(screen: object, best_score: int):
    # shows best score on screen
    show_text(screen, f"highscore: {max(best_score, score)}", (20, 40))


def show_middle_text(screen: object, content: str, position: tuple,
                     size: int = 24, color: str = "white"):
    # shows content on screen with given position int the
    # middle using font of given size and color
    font = pygame.font.Font(None, size)
    image = font.render(content, True, color)
    width = image.get_width()
    height = image.get_height()
    new_position = (position[0]-width/2, position[1]-height/2)
    screen.blit(image, new_position)


def show_button(screen: object, position: tuple, content: str, size: int):
    # shows a button on screen on the given
    # position with given content of set size
    pygame.draw.rect(screen, "white", [position[0], position[1],
                                       size[0], size[1]])
    show_middle_text(screen, content, (position[0]+size[0]/2,
                                       position[1]+size[1]/2), color="black")
    return [position[0], position[1], position[0]+size[0], position[1]+size[1]]


def is_within(point: list[int], end_points: list[int]):
    # checks if point is within rectangle with given points
    if (point[0] > end_points[0] and
            point[0] < end_points[2] and
            point[1] > end_points[1] and
            point[1] < end_points[3]):
        return True
    return False


def check_end_condition(players: list[Player], enemies: list[Enemy]):
    # checks if end condition is satisfied
    for enemy in enemies:
        if enemy.position[1] >= players[0].position[1]:
            return True
    return False


def show_menu() -> int:
    # shows menu window and returns the next position the window should go to
    screen = pygame.display.set_mode((Settings.window_width,
                                      Settings.window_height))
    running = True
    buttons = []
    while running:
        buttons.clear()
        buttons = [[show_button(screen, (100, 200), "start", (100, 100)), 1],
                   [show_button(screen, (400, 200), "quit", (100, 100)), 0]]
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if not is_within([mouse[0], mouse[1]], button[0]):
                        continue
                    if button[1] == 0:
                        return -1
                    if button[1] == 1:
                        return 0

        show_middle_text(screen, "SPACE INVADERS", (300, 100), size=50)
        pygame.display.flip()


def show_lose_screen(score: int):
    # shows loosing score with given score
    screen = pygame.display.set_mode((Settings.window_width,
                                      Settings.window_height))
    running = True
    buttons = []
    while running:
        buttons.clear()
        buttons = [[show_button(screen, (100, 250), "restart", (100, 100)), 1],
                   [show_button(screen, (400, 250), "quit", (100, 100)), 0]]
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if not is_within([mouse[0], mouse[1]], button[0]):
                        continue
                    if button[1] == 0:
                        return -1
                    if button[1] == 1:
                        return 0

        show_middle_text(screen, "YOU LOST", (300, 100), size=50)
        show_middle_text(screen, f"your score: {score}", (300, 170), size=30)
        pygame.display.flip()


def show_game_window():
    # shows game window
    best_score = int(fm.read_file())
    bullets = []
    enemies = []
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
    score = 0
    last_shot = -1
    mul = 1
    enemies_start_ammount = Settings.invaders_in_row*Settings.rows_of_invaders

    while running:
        time_running += delta_time
        if len(enemies) == 0:
            enemies = load_invaders()

        if check_end_condition(players, enemies):
            return score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return -1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            move_entities(delta_time, -1, players)
        if keys[pygame.K_d]:
            move_entities(delta_time, 1, players)
        if keys[pygame.K_w] and not player_shot:
            player_shoot(players[0], time_running, bullets)
            player_shot = True
        elif not keys[pygame.K_w]:
            player_shot = False

        tmp, score = remove_entities(update_hit(bullets, players),
                                     score, players)
        players = tmp
        tmp, score = remove_entities(update_hit(bullets, enemies),
                                     score, enemies)
        enemies = tmp
        tmp, score = remove_entities(update_hit(bullets, blockers),
                                     score, blockers)
        blockers = tmp
        new_bullets = []
        for bullet in bullets:
            if (bullet.position[1] < -100 - Settings.bullet_size or
               bullet.position[1] > Settings.window_height +
               Settings.bullet_size + 100):
                continue
            new_bullets.append(bullet)
        bullets = new_bullets
        mul = 1 + (.1*(enemies_start_ammount-len(enemies)))
        move_entities(delta_time, 1, bullets)
        move_entities(delta_time * mul, 1, enemies)
        if (time_running-.5)//1 != last_shot:
            last_shot += 1
            shoot_entities(enemies, bullets)
        screen.fill("black")

        for blocker in blockers:
            blocker.update_blocker()

        if len(players) == 0:
            running = False
            return score
        show_all(screen, bullets, enemies, players, blockers)
        show_score(screen, score)
        show_best_score(screen, best_score)
        pygame.display.flip()
        delta_time = (clock.tick(Settings.fps)/1000)


score = -1
best_score = int(fm.read_file())

running = True
window_position = 0
pygame.display.set_caption("space invaders")
while running:
    if window_position == 0:
        if show_menu() == -1:
            running = False
        else:
            window_position = 1
    if window_position == 1:
        score = show_game_window()
        if score == -1:
            running = False
            continue
        if score > best_score:
            fm.write_to_file(str(score))
        window_position = 2
    if window_position == 2:
        if show_lose_screen(score) == -1:
            running = False
            continue
        window_position = 1

pygame.quit()
