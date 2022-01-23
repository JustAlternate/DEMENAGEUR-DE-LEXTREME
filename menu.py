import pygame,os,sys
from button import *
from random import randrange

def menuGame():

    pygame.init()

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((1200,849))

    icon=pygame.image.load("img/icon.png").convert()
    pygame.display.set_icon(icon)
    pygame.display.set_caption("BlackJack.py")

    pygame.display.update()

    launched = True

    boutons = []

    bg = pygame.image.load("img/background_demenageur.png").convert()
    #bg = pygame.transform.scale(bg, (1200, 849 * 4))

    clock = pygame.time.Clock()

    speed=60

    def redrawWindow(rgb,pos):
        screen.blit(bg,(0,0))

        boutons = []

        if rgb[0]<255:rgb[0]+=0.5
        else:rgb[0]=0
        if rgb[1]<255:rgb[1]+=0.5
        else:rgb[1]=0
        if rgb[2]<255:rgb[2]+=0.5
        else:rgb[2]=0

        boutons.append(Button('Play', 'center', screen.get_height() // 4, None, 'Onix', 40, rgb,(16, 74, 92), pygame, screen))
        boutons.append(Button('Settings', 'center', screen.get_height() // 2, None, 'Onix', 40, (9, 255, 45),(16, 74, 92), pygame, screen))
        boutons.append(Button('Exit', 'center', screen.get_height() // 1.3, None, 'Onix', 40, (255, 255, 255), (16, 74, 92),pygame, screen))

        for i in range (len(boutons)):
            boutons[i].draw()
            if boutons[i].isOver(pos):
                if boutons[i].name=='Play':
                    boutons[i]=Button('Play', 'center', screen.get_height() // 4, None, 'Onix', 80, rgb,(16, 74, 92), pygame, screen)
                if boutons[i].name=='Settings':
                    boutons[i]=Button('Settings', 'center', screen.get_height() // 2, None, 'Onix', 80, (9, 255, 45),(16, 74, 92), pygame, screen)
                if boutons[i].name=='Exit':
                    boutons[i]=Button('Exit', 'center', screen.get_height() // 1.3, None, 'Onix',80, (255, 255, 255), (16, 74, 92),pygame, screen)
                boutons[i].draw()

        authors = pygame.font.Font(None, int((1200 / 849) * 10)).render("Created by JustAlternate", True, (0, 255, 0))
        rect = pygame.Rect(authors.get_rect(center=(1200 / 1.2, 849 / 1.2))[0],authors.get_rect(center=(1200 / 1.3, 849 / 1.1))[1],authors.get_width(), authors.get_height())
        pygame.draw.rect(screen, (16, 74, 92), rect)
        screen.blit(authors, authors.get_rect(center=(1200 / 1.2, 849 / 1.1)))

        return rgb,boutons

    rgb = [randrange(0, 255,1), randrange(0, 255,1), randrange(0, 255,1)]

    while launched:

        try:
            pos=pygame.mouse.get_pos()
            rgb,boutons=redrawWindow(rgb,pos)
            clock.tick(speed)
        except:pass

        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for bouton in boutons:

                    if bouton.isOver(pos):

                        if bouton.name=="Exit":
                            pygame.quit()
                            launched=False
                            sys.exit()

                        elif bouton.name == 'Play':
                            menuGame()

                        elif bouton.name == 'Settings':
                            settings()
                            menuGame()

            if event.type == pygame.QUIT:
                launched = False
                sys.exit()

def settings():
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((1200,849))

    pygame.display.update()

    clock = pygame.time.Clock()

    launched = True

    boutons = []

    bg = pygame.image.load("img/background_demenageur.png").convert()

    def redrawWindow():
        screen.blit(bg,(0,0))

        boutons = []

        boutons.append(Button('Exit', screen.get_width()*0.85, screen.get_height()//20 ,None, 'Onix', 40, (255, 255, 255), (16, 74, 92),pygame, screen))

        for bouton in boutons:
            bouton.draw()

        authors = pygame.font.Font(None, int((1200 / 849) * 20)).render("Created by JustAlternate", True,(0, 255, 0))
        rect = pygame.Rect(authors.get_rect(center=(1200 / 1.2, 849 / 1.2))[0],authors.get_rect(center=(1200 / 1.3, 849 / 1.1))[1], authors.get_width(),authors.get_height())
        pygame.draw.rect(screen, (16, 74, 92), rect)
        screen.blit(authors, authors.get_rect(center=(1200 / 1.2, 849 / 1.1)))

        return boutons


    while launched:

        boutons = redrawWindow()

        speed=60
        clock.tick(speed)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for bouton in boutons:

                    if bouton.isOver(pos):

                        if bouton.name == "Exit":
                            launched = False

                        elif bouton.name == 'Play':
                            menuGame()

            if event.type == pygame.QUIT:
                launched = False

if __name__=='__main__':
    menuGame()