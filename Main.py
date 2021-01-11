import pygame
import random

# Initialize the game engine
pygame.init()
size = (1080, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("<--- Python")
clock = pygame.time.Clock()

backgroundIMG = pygame.image.load("Field.png").convert()

def startMenu():

    menu = True

    while menu:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #starto buttono presso
                if (mousex > 480 and mousex < 600 and mousey > 190 and mousey < 250):
                    menu = False
                    Main()
                #option button
                elif (mousex > 465 and mousex < 625 and mousey > 320 and mousey < 380):
                    print("hi")
                    
        
        pos = pygame.mouse.get_pos()
        mousex = pos[0]
        mousey = pos[1]

        screen.blit(backgroundIMG, [0, 0])
        font = pygame.font.SysFont('arial', 50, False, False)
        text = font.render(("Holy Crap!! Its Freaking Duck Hunt") ,True, (0, 0, 0))
        screen.blit(text, [140, 50])


        pygame.draw.rect(screen, (40,213,255), (480, 190, 120, 60))
        font = pygame.font.SysFont('arial', 30, True, False)
        text = font.render(("START") ,True, (0, 0, 0))
        screen.blit(text, [490, 200])

        pygame.draw.rect(screen, (40,213,255), (465, 320, 160, 60))
        font = pygame.font.SysFont('arial', 30, True, False)
        text = font.render(("OPTIONS") ,True, (0, 0, 0))
        screen.blit(text, [475, 330])

        pygame.draw.rect(screen, (40,213,255), (465, 450, 160, 60))
        font = pygame.font.SysFont('arial', 30, True, False)
        text = font.render(("BYE BYE") ,True, (0, 0, 0))
        screen.blit(text, [475, 460])
    
        
        pygame.display.update()
        clock.tick(15)


def Main(): 
    # Loop until the user clicks the close button.
    done = False
    pygame.mouse.set_visible(False)
    honk = pygame.mixer.Sound("honk.mp3")

    oleDuckyList = []
    for i in range(7):
        oleDuckyList.append(Target(random.randint(0,100), random.randint(i* 75, i * 100), 66, 48, pygame.image.load("MalignantMallardUp.png"), 1))
    
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(7):
                    shootTarget(oleDuckyList[i], mousex, mousey, honk)

        pos = pygame.mouse.get_pos()
        mousex = pos[0]
        mousey = pos[1]
        
        # Clear the screen and set the screen background
        screen.blit(backgroundIMG, [0, 0])

        #draw the things you shoot
        for i in range(7):
            oleDuckyList[i].move_targetx(3)
            drawTargets(screen, oleDuckyList[i])
    
        pygame.draw.line(screen, (255,0,0), [mousex + 9, mousey], [mousex - 8, mousey], 2)
        pygame.draw.line(screen, (255,0,0), [mousex, mousey + 9], [mousex, mousey - 8], 2)
        
        pygame.display.flip()
        clock.tick(144)
    pygame.quit()
#  #end of main lol

class Target:
    def __init__(self, x, y, length, height, image, health):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.image = image
        self.health = health
        self.alive = True
    def change_health(self, health_change):
        if self.health > 0:
            self.health -= health_change 
        if self.health < 1:
            self.alive = False
    def move_targetx(self, xchange):
        self.x += xchange

class Player:
    def __init__(self, ammo, crosshair, score):
        self.ammo = 12
        self.crosshair = crosshair
        self.score = 0


def drawTargets(screen, atarget):
    if atarget.alive:
        screen.blit(atarget.image, [atarget.x, atarget.y]) 

def shootTarget(atarget, mousex, mousey, honk):
    if (mousex > atarget.x and mousex < atarget.x + atarget.length and mousey > atarget.y and mousey < atarget.y + atarget.height):
        atarget.change_health(1)
        print(atarget.health)

# def displayScore()

startMenu()