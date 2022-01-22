import pygame
from math import sqrt


def movement(speed):

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

    if speed < 2: speed = 2

    if moving_right:
        player_movement[0] += speed

    if moving_left:
        player_movement[0] -= speed

    if moving_up:
        player_movement[1] -= speed

    if moving_down:
        player_movement[1] += speed

    player_movement = [round(player_movement[0], 2), round(player_movement[1], 2)]

    return player_movement


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

def move_projectiles(projectile,vent):  # facing : 0 = left , 1 = up , 2 = right , 3 = down, 4 = diago gauche haute, 5 = diago droite haute, 6 = diago basse droite, 7 = diago basse gauche
    if projectile.facing == 0:
        projectile.x -= projectile.speed
    elif projectile.facing == 1:
        projectile.x += projectile.speed
    elif projectile.facing == 2:
        projectile.y -= projectile.speed
    elif projectile.facing == 3:
        projectile.y += projectile.speed
    elif projectile.facing == 4:
        projectile.x -= projectile.speed
        projectile.y -= projectile.speed
    elif projectile.facing == 5:
        projectile.x += projectile.speed
        projectile.y -= projectile.speed
    elif projectile.facing == 6:
        projectile.x -= projectile.speed
        projectile.y += projectile.speed
    elif projectile.facing == 7:
        projectile.x += projectile.speed
        projectile.y += projectile.speed


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