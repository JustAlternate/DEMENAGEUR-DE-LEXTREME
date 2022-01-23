import pygame
from math import sqrt


def move_entity(Entities, player_rect):
    for entity in Entities:
        if entity.name != "porte":

            #entity.rect.x
            #entity.rect.y

            #player_rect.x
            #player_rect.y

            #player_rect.width
            #player_rect.height

            #entity.rect.width
            #entity.rect.height

            if not entity.rect.x==player_rect.x:

                if entity.rect.x < player_rect.x:
                    entity.rect.x += 1
                else:
                    entity.rect.x -= 1

            if not entity.rect.y==player_rect.y:

                if entity.rect.y < player_rect.y:
                    entity.rect.y += 1
                else:
                    entity.rect.y -= 1

def movement(speed,direction):

    player_movement = [0, 0]
    if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_q]:
        moving_left = True
    else:
        moving_left = False
    if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
        moving_right = True
    else:
        moving_right = False
    if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_z]:
        moving_up = True
    else:
        moving_up = False
    if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
        moving_down = True
    else:
        moving_down = False

    moving=False
    if moving_left:
        direction=False
        moving=True
    if moving_right:
        direction=True
        moving=True
    if moving_down or moving_up:
        moving=True

    if speed < 3: speed = 3

    if moving_right:
        player_movement[0] += speed

    if moving_left:
        player_movement[0] -= speed

    if moving_up:
        player_movement[1] -= speed

    if moving_down:
        player_movement[1] += speed

    player_movement = [round(player_movement[0], 2), round(player_movement[1], 2)]

    return player_movement,direction,moving


def collision_test(rect, Structs):  # FROM PYGAME DAFLUFFYPOTATO TUTORIALS
    hit_list = []
    for struct in Structs:
        if rect.colliderect(struct):
            hit_list.append(struct)
    return hit_list


def move(rect, movement, Structs):  # FROM PYGAME DAFLUFFYPOTATO TUTORIALS
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, Structs)
    for struct in hit_list:
        if movement[0] > 0:
            rect.right = struct.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = struct.right
            collision_types['left'] = True

    rect.y += movement[1]
    hit_list = collision_test(rect, Structs)
    for struct in hit_list:
        if movement[1] > 0:
            rect.bottom = struct.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = struct.bottom
            collision_types['top'] = True

    return rect, collision_types


def move_fire_projectiles(projectile,Fire_Projectiles):

    dist = sqrt((projectile.facing[0] ** 2) + (projectile.facing[1] ** 2))

    if projectile.facing[0] < 0 and not projectile.facing[0] > projectile.speed:
        projectile.x += (projectile.facing[0] / dist) * projectile.speed

    if projectile.facing[0] > 0 and not -projectile.facing[0] > projectile.speed:
        projectile.x += (projectile.facing[0] / dist) * projectile.speed

    if projectile.facing[1] < 0 and not projectile.facing[1] > projectile.speed:
        projectile.y += (projectile.facing[1] / dist) * projectile.speed

    if projectile.facing[1] > 0 and not -projectile.facing[1] > projectile.speed:
        projectile.y += (projectile.facing[1] / dist) * projectile.speed

    if projectile.speed > 0 : projectile.speed -= 0.01
    else : Fire_Projectiles.remove(projectile)

    return Fire_Projectiles