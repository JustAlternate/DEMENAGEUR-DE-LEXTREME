#Project pollen disaster :

from turtle import width
import pygame,os,random
import math
from spritesheet import Spritesheet
import random
from gen import *
from Entity import *
from movement import *
from render import *
from button import Button

def game(size,porte_darrive,lvl_number):

    pygame.init()
    WIDTH = 1200-16*2
    HEIGHT = 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    fireball_spritesheet = Spritesheet('img/carton.png')
    fireball_sprites = [fireball_spritesheet.parse_sprite('carton0.png'),
                        fireball_spritesheet.parse_sprite('carton1.png'),
                        fireball_spritesheet.parse_sprite('carton2.png'),
                        fireball_spritesheet.parse_sprite('carton3.png')]

    for i in range(len(fireball_sprites)):
        fireball_sprites[i] = pygame.transform.scale(fireball_sprites[i], (
        int(fireball_sprites[i].get_width()), int(fireball_sprites[i].get_height())))

    porte1_img = pygame.image.load('img/porte.png')
    porte2_img = pygame.image.load('img/porte_open.png')
    wall_falling_img = pygame.image.load('img/wallpaper_falling.png')
    wall_img = pygame.image.load('img/wall.png')
    parquet_img = pygame.image.load('img/parquet.png').convert()
    heart_spritesheet = Spritesheet('img/Life Heart .png')
    player_spritesheet = Spritesheet('img/Hero_motionless.png')
    player_moving_spritesheet = Spritesheet('img/Hero_moving.png')
    tableau_scream_spritesheet = Spritesheet('img/Scream_haunted.png')
    tableau_joconde_spritesheet = Spritesheet('img/Joconde_haunted.png')
    chaise_spritesheet = Spritesheet('img/chaise.png')
    table_spritesheet = Spritesheet('img/table.png')
    tv_spritesheet = Spritesheet('img/tele.png')
    candle_spritesheet = Spritesheet('img/Candlestick.png')
    heart_sprites = [heart_spritesheet.parse_sprite('Life Heart 0.png'),heart_spritesheet.parse_sprite('Life Heart 1.png')]
    player_sprites = [player_spritesheet.parse_sprite('Hero_motionless0.png'),player_spritesheet.parse_sprite('Hero_motionless1.png')]
    player_sprites_moving = [player_moving_spritesheet.parse_sprite('Hero_moving0.png'),player_moving_spritesheet.parse_sprite('Hero_moving1.png')]
    tableau_scream_sprites=[tableau_scream_spritesheet.parse_sprite('Scream_haunted0.png'),tableau_scream_spritesheet.parse_sprite('Scream_haunted1.png'),tableau_scream_spritesheet.parse_sprite('Scream_haunted2.png'),tableau_scream_spritesheet.parse_sprite('Scream_haunted3.png'),tableau_scream_spritesheet.parse_sprite('Scream_haunted4.png'),tableau_scream_spritesheet.parse_sprite('Scream_haunted5.png'),tableau_scream_spritesheet.parse_sprite('Scream_haunted6.png'),tableau_scream_spritesheet.parse_sprite('Scream_haunted7.png')]
    chaise_sprites = [chaise_spritesheet.parse_sprite('chaise0.png'),chaise_spritesheet.parse_sprite('chaise1.png')]
    table_sprites = [table_spritesheet.parse_sprite('table0.png'),table_spritesheet.parse_sprite('table1.png')]
    tv_sprites = [tv_spritesheet.parse_sprite('tele0.png'), tv_spritesheet.parse_sprite('tele1.png')]
    candle_sprites = [candle_spritesheet.parse_sprite('Candlestick0.png'), candle_spritesheet.parse_sprite('Candlestick1.png')]
    tableau_joconde_sprites = [tableau_joconde_spritesheet.parse_sprite('Joconde_haunted0.png'), tableau_joconde_spritesheet.parse_sprite('Joconde_haunted1.png'), tableau_joconde_spritesheet.parse_sprite('Joconde_haunted2.png'),
                                     tableau_joconde_spritesheet.parse_sprite('Joconde_haunted3.png'), tableau_joconde_spritesheet.parse_sprite('Joconde_haunted4.png'), tableau_joconde_spritesheet.parse_sprite('Joconde_haunted5.png'),
                                     tableau_joconde_spritesheet.parse_sprite('Joconde_haunted6.png'), tableau_joconde_spritesheet.parse_sprite('Joconde_haunted7.png'),tableau_joconde_spritesheet.parse_sprite('Joconde_haunted8.png'),tableau_joconde_spritesheet.parse_sprite('Joconde_haunted9.png')]

    def transform(img,coeff,size):
        img = pygame.transform.scale(img, (int(img.get_width() * coeff / size), int(img.get_height() * coeff / size))).convert_alpha()
        return img

    def transforms(sprite,coeff,size):
        for i in range(len(sprite)):
            sprite[i].set_colorkey((127, 127, 127))
            sprite[i]=pygame.transform.scale(sprite[i],(int(sprite[i].get_width()*coeff/size), int(sprite[i].get_height()*coeff/size)))

    transforms(fireball_sprites,2,1)
    transforms(player_sprites,2,1)
    transforms(player_sprites_moving,2,1)
    transforms(heart_sprites,2,1)
    transforms(chaise_sprites,3,1)
    transforms(tv_sprites,3,1)
    transforms(table_sprites,3,1)
    transforms(tableau_scream_sprites,1,1)
    transforms(tableau_joconde_sprites,1,1)
    transforms(candle_sprites,2,1)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    insideWIDTH = int(WIDTH-64*4)
    insideHEIGHT = int(HEIGHT-64*4)
    display = pygame.Surface((insideWIDTH,insideHEIGHT))
    launched = True

    clock = pygame.time.Clock()
    exit_time = pygame.time.get_ticks() + 1000
    exit_time2 = pygame.time.get_ticks() + 1000
    exit_time3 = pygame.time.get_ticks() + 1000
    exit_time4 = pygame.time.get_ticks() + 1000
    exit_time5 = pygame.time.get_ticks() + 1000

    speed = 2
    heart = 5
    nbr_salles=0
    max_heart=12

    Walls = [pygame.Rect(0, 0, 1, insideHEIGHT), pygame.Rect(0, 0, insideWIDTH, 1), pygame.Rect(0, insideHEIGHT, insideWIDTH,1),pygame.Rect(insideWIDTH, 0, 1, insideHEIGHT)]

    if porte_darrive==0: #0 = sud, 1=droite, 2=bas, 3=gauche
        player_rect = pygame.Rect(insideWIDTH // 2, 10, player_sprites[0].get_width()//1.5, player_sprites[0].get_height())
    if porte_darrive==1: #0 = sud, 1=droite, 2=bas, 3=gauche
        player_rect = pygame.Rect(insideWIDTH-player_sprites[0].get_width()-10, insideHEIGHT//2, player_sprites[0].get_width()//1.5, player_sprites[0].get_height())
    if porte_darrive==2: #0 = sud, 1=droite, 2=bas, 3=gauche
        player_rect = pygame.Rect(insideWIDTH // 2, insideHEIGHT-player_sprites[0].get_height()-10, player_sprites[0].get_width()//1.5, player_sprites[0].get_height())
    if porte_darrive==3: #0 = sud, 1=droite, 2=bas, 3=gauche
        player_rect = pygame.Rect(10, insideHEIGHT//2, player_sprites[0].get_width()//1.5, player_sprites[0].get_height())

    Entities=[]
    Fire_Projectiles=[]
    Decorations = []
    DecorationsInside=[]
    Tableaux=[]

    def gen_enemies(chaise_sprites):
        nbr_monstre=0
        for i in range(random.randint(0,3)):
            nbr_monstre+=1
            rando_x = random.randint(0, insideWIDTH)
            rando_y = random.randint(0, insideHEIGHT)
            name=random.choice(["chaise","table","tv"])
            if name=="chaise":Entities.append(Entity_class("chaise",chaise_sprites, pygame.Rect(rando_x,rando_y,chaise_sprites[0].get_width(),chaise_sprites[0].get_height()),5))
            if name == "table": Entities.append(Entity_class("table", table_sprites, pygame.Rect(rando_x, rando_y,table_sprites[0].get_width(),table_sprites[0].get_height()),5))
            if name == "tv": Entities.append(Entity_class("tv", tv_sprites, pygame.Rect(rando_x, rando_y, tv_sprites[0].get_width(), tv_sprites[0].get_height()), 5))
        return nbr_monstre

    def parquet():
        
        x,y=0,0
        for i in range(insideWIDTH//32):
            for j in range(insideHEIGHT//32):
                DecorationsInside.append([parquet_img,pygame.Rect(x,y,0,0)])
                y += 96
            y=0
            x += 96

    def gen_tableaux():

        def check_tableau_collide(tableau_rect, other_rect,Tableaux):
            for porte in other_rect:
                if porte[1].colliderect(tableau_rect): return True
            for tableau in Tableaux:
                if tableau[1].colliderect(tableau_rect): return True
            return False

        for i in range(3):
            face=random.randint(0,3)
            sprites=random.choice([tableau_joconde_sprites,tableau_scream_sprites])
            w,h=sprites[0].get_width(),sprites[0].get_height()
            if face==0:
                x,y=random.randint(WIDTH//2,WIDTH-128-w),0
                rect=pygame.Rect(x,y,w,h)
                while check_tableau_collide(rect,Decorations,Tableaux):
                    x, y = random.randint(WIDTH//2, WIDTH-128-w), 0
                    rect = pygame.Rect(x, y, w, h)
                Tableaux.append([sprites, rect])
            if face==1:
                sprites=[pygame.transform.rotate(x,-180) for x in sprites]
                x,y=random.randint(128,WIDTH-128-w),HEIGHT-h
                rect=pygame.Rect(x,y,w,h)
                while check_tableau_collide(rect,Decorations,Tableaux):
                    x,y=random.randint(128,WIDTH-128-w),HEIGHT-h
                    rect = pygame.Rect(x, y, w, h)
                Tableaux.append([sprites, rect])
                sprites = [pygame.transform.rotate(x, 180) for x in sprites]
            if face==2:
                sprites = [pygame.transform.rotate(x, 90) for x in sprites]
                x,y=0,random.randint(128,HEIGHT-128-w)
                rect=pygame.Rect(x,y,w,h)
                while check_tableau_collide(rect,Decorations,Tableaux):
                    x,y=0,random.randint(128,HEIGHT-128-w)
                    rect = pygame.Rect(x, y, w, h)
                Tableaux.append([sprites, rect])
                sprites = [pygame.transform.rotate(x, -90) for x in sprites]
            if face==3:
                sprites = [pygame.transform.rotate(x, -90) for x in sprites]
                x,y=WIDTH-w,random.randint(128,HEIGHT-128-w)
                rect=pygame.Rect(x,y,w,h)
                while check_tableau_collide(rect,Decorations,Tableaux):
                    x,y=WIDTH-w,random.randint(128,HEIGHT-128-w)
                    rect = pygame.Rect(x, y, w, h)
                Tableaux.append([sprites, rect])
                sprites = [pygame.transform.rotate(x, 90) for x in sprites]

    def gen_porte(porte1_img):
        w,h=porte1_img.get_width(),porte1_img.get_height()
        Decorations.append([porte1_img, pygame.Rect(WIDTH//2,0,w,h)])
        porte1_img=pygame.transform.rotate(porte1_img,180)
        Decorations.append([porte1_img, pygame.Rect(WIDTH//2, HEIGHT-porte1_img.get_height(), w, h)])
        porte1_img=pygame.transform.rotate(porte1_img,180)
        porte1_img=pygame.transform.rotate(porte1_img,90)
        Decorations.append([porte1_img, pygame.Rect(0, HEIGHT//2, w, h)])
        porte1_img=pygame.transform.rotate(porte1_img,180)
        Decorations.append([porte1_img, pygame.Rect(WIDTH-porte1_img.get_width(), HEIGHT//2, w, h)])

    gen_decor(screen, wall_img, wall_falling_img, WIDTH, HEIGHT)
    gen_porte(porte1_img)
    gen_tableaux()
    parquet()
    nbr_monstre=gen_enemies(chaise_sprites)
    DecorationsInside.append([candle_sprites[random.randint(0, 1)], pygame.Rect(0, 0, 0, 0)])
    DecorationsInside.append([candle_sprites[random.randint(0, 1)], pygame.Rect(insideWIDTH-candle_sprites[0].get_width(), 0, 0, 0)])
    DecorationsInside.append([candle_sprites[random.randint(0, 1)], pygame.Rect(0, insideHEIGHT-candle_sprites[0].get_height(), 0, 0)])
    DecorationsInside.append([candle_sprites[random.randint(0, 1)], pygame.Rect(insideWIDTH-candle_sprites[0].get_width(), insideHEIGHT-candle_sprites[0].get_height(), 0, 0)])

    heart_index = 0
    chaise_index=0
    table_index=0
    tv_index=0
    player_img_index = 0
    fireball_index = 0
    joconde_index=0
    scream_index=0
    candle_index=0

    def flame_thrower(nbr_monstre):
        cutted = 0
        for entity in Entities:
            if entity.name!="porte":
                for fire in Fire_Projectiles:
                    if pygame.Rect(fire.x, fire.y, fire.radius,fire.radius).colliderect(entity.rect):
                        entity.hp-=1
                        try:Fire_Projectiles.remove(fire)
                        except:Fire_Projectiles.pop()
                        if entity.hp==0:
                            nbr_monstre-=1
                            try:Entities.remove(entity)
                            except:Entities.pop()
        return nbr_monstre

    direction=False
    fire_timing=False
    take_damage=False

    while launched:
        
        Structs = []
        for wall in Walls: Structs.append(wall)

        display.fill((80, 120, 80))
        mousepos, rawmousepos, rel = genMousePos(player_rect)

        player_movement,direction,moving = movement(speed,direction)
        player_rect, collisions = move(player_rect, player_movement, Structs)
        for entity in Entities:
            if entity.name=="porte":
                if player_rect.colliderect(entity.rect):
                    game(1,entity.porte_darrive,lvl_number+1)
                    return None

        current_time = pygame.time.get_ticks()
        if current_time >= exit_time:
            chaise_index = (chaise_index + 1) % len(chaise_sprites)
            fireball_index = (fireball_index + 1) % len(fireball_sprites)
            heart_index = (heart_index + 1) % len(heart_sprites)
            player_img_index=(player_img_index + 1) % len(player_sprites)
            table_index = (table_index + 1) % len(table_sprites)
            tv_index = (tv_index + 1) % len(tv_sprites)
            scream_index=(scream_index + 1) % len(tableau_scream_sprites)
            joconde_index=(joconde_index + 1) % len(tableau_joconde_sprites)
            candle_index = (candle_index + 1) % len(candle_sprites)
            exit_time = current_time + 200

        if current_time >= exit_time2:
            move_entity(Entities,player_rect)
            exit_time2 = current_time + 30

        if current_time >= exit_time3:
            fire_timing=True
            take_damage=True
            exit_time3 = current_time + 1000

        render_hearts(heart,screen,wall_falling_img,WIDTH,HEIGHT,heart_sprites,heart_index)
        renderDecoration(Decorations, screen)
        renderTableaux(Tableaux,screen,joconde_index,scream_index,candle_index)
        renderDecoration_inside(DecorationsInside,display)
        renderEntities(display,Entities,chaise_index,table_index,tv_index)
        render_fire_projectiles(Fire_Projectiles, fireball_sprites, fireball_index, display)
        renderplayer(display, player_rect, player_sprites,player_sprites_moving,player_img_index,direction,moving)
        text = pygame.font.Font('Mojito in June.ttf', 30).render(str("Room number : "+str(lvl_number)), True, ((128,128,128)))
        screen.blit(text,(WIDTH-300,50))


        #pygame.draw.rect(display,(255,255,0),player_rect,3,10)

        for fire_proj in Fire_Projectiles:
            Fire_Projectiles=move_fire_projectiles(fire_proj,Fire_Projectiles)
            nbr_monstre=flame_thrower(nbr_monstre)

        if nbr_monstre==-1:
            textualmaker("THE ROOM IS EMPTY",35,(0,255,0),2,2,display)

        if nbr_monstre==0:
            nbr_monstre=-1
            Entities.append(Entity_class("porte",None, pygame.Rect(insideWIDTH//2,0,porte1_img.get_width(),10),0,2))
            Entities.append(Entity_class("porte",None, pygame.Rect(insideWIDTH//2,insideHEIGHT-10,porte1_img.get_width(),10),0,0))
            Entities.append(Entity_class("porte",None, pygame.Rect(insideWIDTH-10, insideHEIGHT//2, 10, porte1_img.get_height()),0,3))
            Entities.append(Entity_class("porte",None, pygame.Rect(0, insideHEIGHT//2, 10, porte1_img.get_height()),0,1))
            gen_porte(porte2_img)

        for entity in Entities:
            if entity.name!="porte":
                if player_rect.colliderect(entity.rect) and take_damage:
                    take_damage=False
                    heart-=1

        if heart == 0: launched = end()

        events = pygame.event.get()
        for event in events:
            if ((event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)) and fire_timing:
                gen_fire(rel, fireball_sprites, player_rect, Fire_Projectiles, 1)
                fire_timing=False

            if event.type == pygame.QUIT:
                launched = False

        screen.blit(display,(64*2,64*2))
        clock.tick(60)

        pygame.display.update()

game(1,1,1)