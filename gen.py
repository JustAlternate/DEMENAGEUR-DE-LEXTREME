import pygame
import random
from Projectile import *

def random_coord(minix, miniy, xscale, yscale,insideWIDTH,insideHEIGHT):
    x = random.randint(minix, int(insideWIDTH * xscale))
    y = random.randint(miniy, int(insideHEIGHT * yscale))
    return x, y


def lookforcollided(rect,Decorations,Flowers):
    for deco in Decorations:
        if deco[0].colliderect(rect): return True
    for flower in Flowers:
        if flower[1].colliderect(rect): return True
    else:
        return False


def gendecoration(n1, n2,Decorations,Flowers,herbe_imgs,arbre_img,insideWIDTH,insideHEIGHT,size):
    nbrherbe = random.randint(5, n2*2)
    if nbrherbe > 50: nbrherbe=50
    nbrarbre = random.randint(0, int(n1 // 8))
    for i in range(nbrherbe):
        x, y = random_coord(20, 20, 1, 1,insideWIDTH,insideHEIGHT)
        while lookforcollided(pygame.Rect(x - 10 // size, y - 15 // size, 20 // size, 30 // size),Decorations,Flowers):
            x, y = random_coord(20, 20, 1, 1,insideWIDTH,insideHEIGHT)
        Decorations.append([pygame.Rect(x - 10 // size, y - 15 // size, 20 // size, 30 // size),
                            herbe_imgs[random.randint(0, len(herbe_imgs) - 1)]])
    for i in range(nbrarbre):
        x, y = random_coord(40, 40, 0.8, 0.75,insideWIDTH,insideHEIGHT)
        while lookforcollided(pygame.Rect(x - 10 // size, y - 15 // size, 20 // size, 30 // size),Decorations,Flowers):
            x, y = random_coord(20, 20, 1, 1,insideWIDTH,insideHEIGHT)
        Decorations.append([pygame.Rect(x - 10 // size, y - 15 // size, 20 // size, 30 // size), arbre_img])

def genprojectiles(Flowers,Projectiles,violet_flower_sprites,size):
    for flower in Flowers:
        Projectiles.append(Projectile("flower",(255,255,255),flower[0].x+violet_flower_sprites[0].get_width()//2, flower[0].y+violet_flower_sprites[0].get_height()//4, 30//size, random.randint(0, 7),1))
    return len(Projectiles)

def gen_fire(rel,fireball_sprites,player_rect,Fire_Projectiles,size):
    rel=[rel[0]-fireball_sprites[0].get_width()//2*size,rel[1]-fireball_sprites[0].get_height()//2*size]
    speed = int(5//size)
    if speed < 2:speed = 2
    Fire_Projectiles.append(Projectile("fire",(255,0,0),player_rect.x,player_rect.y,50,rel,speed))

def genMousePos(player_rect):
    rawmousepos = pygame.mouse.get_pos()
    mousepos = [rawmousepos[0], rawmousepos[1]]
    rel_x, rel_y = mousepos[0] - (player_rect.x + player_rect.w), mousepos[1] - (player_rect.y+player_rect.h)  # will be used to know where the player look
    return mousepos, rawmousepos, [rel_x,rel_y]