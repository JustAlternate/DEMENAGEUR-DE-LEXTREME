import pygame
import random
pygame.font.init()

def textualmaker(text, size, color, w, h, display):
    text = pygame.font.Font('Mojito in June.ttf', int((display.get_width() / display.get_height()) * size)).render(str(text), True,color)
    display.blit(text, text.get_rect(center=(display.get_width() / w, display.get_height() / h)))

def gen_decor(screen,wall_img,wall_falling,WIDTH,HEIGHT):
    def randoom(L,weights):
        return random.choices(L, weights=weights, k=1)[0]

    L=[wall_img,wall_falling]
    weight=[10,1]

    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],180)
    x=0
    y=HEIGHT-4*32
    for i in range(WIDTH//wall_img.get_width()+1):
        screen.blit(randoom(L,weight), (x, y))
        screen.blit(randoom(L,weight), (x, y+32*2))
        x+=32*2
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],-180)

    x=0
    y=0
    for i in range (WIDTH // wall_img.get_height() +1):
        screen.blit(randoom(L,weight), (x, y))
        screen.blit(randoom(L,weight), (x, y+32*2))
        x+=32*2
    y=4*32
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],90)
    for i in range (HEIGHT // wall_img.get_height()):
        screen.blit(randoom(L,weight), (0, y))
        screen.blit(randoom(L,weight), (32*2, y))
        y+=wall_img.get_height()
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],-90)
    x=WIDTH-4*32
    y=4*32
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],-90)
    for i in range(HEIGHT//wall_img.get_width()+1):
        screen.blit(randoom(L,weight), (x, y))
        screen.blit(randoom(L,weight), (x+32*2, y))
        y+=32*2
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],90)

def render_hearts(heart,screen,woodenplank_small_img,WIDTH,HEIGHT,heart_sprites,heart_index):
    for i in range(heart+1):
        screen.blit(woodenplank_small_img, (64*2+32*2*i, 0))
        screen.blit(woodenplank_small_img, (64*2+32*2*i, 32*2))
    for i in range(heart):
        screen.blit(heart_sprites[heart_index],(64+32*i,0))

def renderDecoration(Decorations,screen):
    for deco in Decorations:
        screen.blit(deco[0], (deco[1].x, deco[1].y))

def renderDecoration_inside(DecorationsInside,display):
    for deco in DecorationsInside:
        display.blit(deco[0],(deco[1].x,deco[1].y))

def renderEntities(display,Entities,chaise_index):
    for entity in Entities:
        if entity.name=="chaise":
            display.blit(entity.sprites[chaise_index],(entity.rect.x,entity.rect.y))

def renderplayer(screen,player_rect,player_img_idle,player_img_moving,player_index,direction,moving):
    if moving:img=player_img_moving[player_index]
    else:img=player_img_idle[player_index]
    if direction:img=pygame.transform.flip(img,True,False)
    screen.blit(img, (player_rect.x-img.get_width()//5,player_rect.y))

def render_fire_projectiles(Fire_Projectiles, fireball_sprites, index, display):
    for projectile in Fire_Projectiles:
        display.blit(fireball_sprites[index], (projectile.x + fireball_sprites[0].get_width() // 8, projectile.y + fireball_sprites[0].get_height() // 16))

def renderProjectiles(Projectiles,display):
    for projectile in Projectiles: pygame.draw.circle(display, projectile.color, (projectile.x, projectile.y),projectile.radius // 2, 0)
