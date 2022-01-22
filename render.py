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

    y=2*32
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],90)
    for i in range (HEIGHT // wall_img.get_height()):
        screen.blit(randoom(L,weight), (0, y))
        screen.blit(randoom(L,weight), (32, y))
        y+=wall_img.get_height()
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],-90)
    x=0
    y=0
    for i in range (WIDTH // wall_img.get_height() +1):
        screen.blit(randoom(L,weight), (x, y))
        screen.blit(randoom(L,weight), (x, y+32))
        x+=32
    x=WIDTH-2*32
    y=2*32
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],-90)
    for i in range(HEIGHT//wall_img.get_width()+1):
        screen.blit(randoom(L,weight), (x, y))
        screen.blit(randoom(L,weight), (x+32, y))
        y+=32
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],90)
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],180)
    x=0
    y=HEIGHT-2*32
    for i in range(WIDTH//wall_img.get_width()+1):
        screen.blit(randoom(L,weight), (x, y))
        screen.blit(randoom(L,weight), (x, y+32))
        x+=32
    for i in range (len(L)):L[i]=pygame.transform.rotate(L[i],-180)

def render_hearts(heart,screen,woodenplank_small_img,WIDTH,HEIGHT,heart_sprites,heart_index):
    for i in range(heart+1):
        screen.blit(woodenplank_small_img, (64+32*i, 0))
        screen.blit(woodenplank_small_img, (64+32*i, 32))
    for i in range(heart):
        screen.blit(heart_sprites[heart_index],(64+32*i,0))

def renderDecoration(Decorations,screen):
    for deco in Decorations:
        screen.blit(deco[0], (deco[1].x, deco[1].y))

def renderDecoration_inside(DecorationsInside,display):
    for deco in DecorationsInside:
        display.blit(deco[0],(deco[1].x,deco[1].y))

def renderplayer(screen,player_rect,player_img,player_index):
    screen.blit(player_img[player_index], (player_rect.x- player_img[player_index].get_width()//4,player_rect.y-player_img[player_index].get_height()//4))

def render_fire_projectiles(Fire_Projectiles, fireball_sprites, index, display):
    for projectile in Fire_Projectiles:
        display.blit(fireball_sprites[index], (projectile.x + fireball_sprites[0].get_width() // 8, projectile.y + fireball_sprites[0].get_height() // 16))

def renderProjectiles(Projectiles,display):
    for projectile in Projectiles: pygame.draw.circle(display, projectile.color, (projectile.x, projectile.y),projectile.radius // 2, 0)
