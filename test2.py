#Project pollen disaster :

import pygame,os,random
from spritesheet import Spritesheet
from gen import *
from movement import *
from render import *
from button import Button

pygame.init()

WIDTH = 1200-16
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

fireball_spritesheet = Spritesheet('img/16-bit fire ball.png')
fireball_sprites = [fireball_spritesheet.parse_sprite('16-bit fire ball0.png'),
                    fireball_spritesheet.parse_sprite('16-bit fire ball1.png'),
                    fireball_spritesheet.parse_sprite('16-bit fire ball2.png'),
                    fireball_spritesheet.parse_sprite('16-bit fire ball3.png')]

for i in range(len(fireball_sprites)):
    fireball_sprites[i] = pygame.transform.scale(fireball_sprites[i], (https://go.codetogether.com/#/6fb6fb08-0d61-49fe-bdbe-b8da727778aa/zSMKMkCPOjBKqTmalUVEFu
    int(fireball_sprites[i].get_width() * 10), int(fireball_sprites[i].get_height() * 10)))

porte1_img = pygame.image.load('img/porte.png')
porte2_img = pygame.image.load('img/porte.png')
porte3_img = pygame.image.load('img/porte.png')
porte4_img = pygame.image.load('img/porte.png')
wall_falling_img = pygame.image.load('img/wallpaper_falling.png')
wall_img = pygame.image.load('img/wall.png')
parquet_img = pygame.image.load('img/parquet.png').convert()
heart_spritesheet = Spritesheet('img/Life Heart .png')
player_spritesheet = Spritesheet('img/Hero_motionless.png')
heart_sprites = [heart_spritesheet.parse_sprite('Life Heart 0.png'),heart_spritesheet.parse_sprite('Life Heart 1.png')]
player_sprites = [player_spritesheet.parse_sprite('Hero_motionless0.png'),player_spritesheet.parse_sprite('Hero_motionless1.png')]

def transform(img,coeff,size):
    img = pygame.transform.scale(img, (int(img.get_width() * coeff / size), int(img.get_height() * coeff / size))).convert_alpha()
    return img

def transforms(sprite,coeff,size):
    for i in range(len(sprite)):
        sprite[i].set_colorkey((127, 127, 127))
        sprite[i]=pygame.transform.scale(sprite[i],(int(sprite[i].get_width()*coeff/size), int(sprite[i].get_height()*coeff/size)))

transforms(fireball_sprites,1,1)
transforms(player_sprites,2,1)
transforms(heart_sprites,2,1)

def game(size):

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    insideWIDTH = int(WIDTH-64*2)
    insideHEIGHT = int(HEIGHT-64*2)
    display = pygame.Surface((insideWIDTH,insideHEIGHT))
    launched = True

    clock = pygame.time.Clock()
    exit_time = pygame.time.get_ticks() + 1000

    speed = 3
    heart = 1
    max_heart=12

    gen_decor(screen,wall_img,wall_falling_img,WIDTH,HEIGHT)

    Walls = [pygame.Rect(0, 0, 1, insideHEIGHT), pygame.Rect(0, 0, insideWIDTH, 1), pygame.Rect(0, insideHEIGHT, insideWIDTH,1),pygame.Rect(insideWIDTH, 0, 1, insideHEIGHT)]

    player_rect = pygame.Rect(insideWIDTH // 2, insideHEIGHT // 2, 20, 20)

    Entities=[]
    Entities.append([None, pygame.Rect(WIDTH//2.4,HEIGHT//120,50,25)])
    Entities.append([None, pygame.Rect(WIDTH // 2.4, HEIGHT // 1.05, 25, 50)])
    Entities.append([None, pygame.Rect(30, HEIGHT // 2.4, 50, 50)])
    Entities.append([None, pygame.Rect(WIDTH // 1.2, HEIGHT // 2, 25, 25)])

    Fire_Projectiles=[]
    Decorations = []
    DecorationsInside=[]

    x,y=0,0
    for i in range(insideWIDTH//32):
        for j in range(insideHEIGHT//32):
            DecorationsInside.append([parquet_img,pygame.Rect(x,y,0,0)])
            y += 32
        y=0
        x += 32

    Decorations.append([porte1_img, pygame.Rect(WIDTH//2,HEIGHT//120,0,0)])
    Decorations.append([porte1_img, pygame.Rect(WIDTH // 2.2, HEIGHT // 1.05, 0, 0)])
    Decorations.append([porte1_img, pygame.Rect(10, HEIGHT // 2, 0, 0)])
    Decorations.append([porte1_img, pygame.Rect(WIDTH // 1.1, HEIGHT // 2, 0, 0)])
    heart_index = 0
    player_img_index=0
    fireball_index=0

    def flame_thrower():
        cutted = 0
        for entity in Entities:
            for fire in Fire_Projectiles:
                if pygame.Rect(fire.x, fire.y, fire.radius,fire.radius).colliderect(entity[1]):
                    cutted += 1
                    try:Entities.remove(entity)
                    except:Entities.pop()
        return cutted

    while launched:

        Structs = []
        for wall in Walls: Structs.append(wall)

        display.fill((80, 120, 80))

        mousepos, rawmousepos, rel = genMousePos(player_rect)

        player_movement = movement(speed)
        player_rect, collisions = move(player_rect, player_movement, Structs)
        for entity in Entities:
            if player_rect.colliderect(entity[1]):
                game(1)
                return None


        current_time = pygame.time.get_ticks()
        if current_time >= exit_time:
            fireball_index = (fireball_index + 1) % len(fireball_sprites)
            heart_index = (heart_index + 1) % len(heart_sprites)
            player_img_index=(player_img_index + 1) % len(player_sprites)
            exit_time = current_time + 200

        else:clock.tick(144)

        render_hearts(heart,screen,wall_falling_img,WIDTH,HEIGHT,heart_sprites,heart_index)
        renderDecoration(Decorations, screen)
        renderDecoration_inside(DecorationsInside,display)
        render_fire_projectiles(Fire_Projectiles, fireball_sprites, fireball_index, display)
        renderplayer(display, player_rect, player_sprites,player_img_index)

        for fire_proj in Fire_Projectiles:
            Fire_Projectiles=move_fire_projectiles(fire_proj,Fire_Projectiles)
            flame_thrower()

        if heart == 0: launched = end()

        events = pygame.event.get()
        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                gen_fire(rel, fireball_sprites, player_rect, Fire_Projectiles, size)

            if event.type == pygame.QUIT:
                launched = False

        screen.blit(display,(64,64))

        pygame.display.update()

game(1)