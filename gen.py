import pygame
import random
from Projectile import *

def random_coord(minix, miniy, xscale, yscale,insideWIDTH,insideHEIGHT):
    x = random.randint(minix, int(insideWIDTH * xscale))
    y = random.randint(miniy, int(insideHEIGHT * yscale))
    return x, y

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