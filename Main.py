import pygame
import random
import time
import math
# Initialize the game engine
pygame.init()
size = (1080, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("<--- Python")
clock = pygame.time.Clock()

backgroundIMG = pygame.image.load("Field.png").convert()
notpog = pygame.image.load("sadpog.png").convert()
pogchamp = pygame.image.load("Pogchamp.png").convert_alpha()
duckIMG = pygame.image.load("MalignantMallardUp.png").convert_alpha()
duckIMG2 = pygame.image.load("MalignantMallardOnItsWayDown.png").convert_alpha()
duckIMG3 = pygame.image.load("MalignantMallardMid.png").convert_alpha()
duckIMG4 = pygame.image.load("MalignantMallardDown.png").convert_alpha()
duckIMGflip = pygame.transform.flip(duckIMG, True, False)
duckIMGflip2 = pygame.transform.flip(duckIMG2, True, False)
duckIMGflip3 = pygame.transform.flip(duckIMG3, True, False)
duckIMGflip4 = pygame.transform.flip(duckIMG4, True, False)
duckIMGsmall = pygame.transform.scale(duckIMG, (33,24))
duckIMGsmall2 = pygame.transform.scale(duckIMG2, (33,24))
duckIMGsmall3 = pygame.transform.scale(duckIMG3, (33,24))
duckIMGsmall4 = pygame.transform.scale(duckIMG4, (33,24))
duckIMGbig = pygame.transform.scale(duckIMG, (132,96))
duckIMGbig2 = pygame.transform.scale(duckIMG2, (132,96))
duckIMGbig3 = pygame.transform.scale(duckIMG3, (132,96))
duckIMGbig4 = pygame.transform.scale(duckIMG4, (132,96))

regularDuckIMGList = [duckIMG, duckIMG2, duckIMG3, duckIMG4, duckIMG3]
flipDuckIMGList = [duckIMGflip, duckIMGflip2, duckIMGflip3, duckIMGflip4, duckIMGflip3]
smallDuckIMGList = [duckIMGsmall, duckIMGsmall2, duckIMGsmall3, duckIMGsmall4, duckIMGsmall3]
bigDuckIMGList = [duckIMGbig, duckIMGbig2, duckIMGbig3, duckIMGbig4, duckIMGbig3]

def startMenu():
    menu = True
    options = False
    
    while menu:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #starto buttono presso
                if not options:
                    if (mousex > 480 and mousex < 600 and mousey > 190 and mousey < 250):
                        menu = False
                        Main()
                    #option button
                    elif (mousex > 465 and mousex < 625 and mousey > 320 and mousey < 380):
                        options = True
                    #Quit button
                    elif (mousex > 465 and mousex < 625 and mousey > 450 and mousey < 510):
                        pygame.quit()

        if menu:
            pos = pygame.mouse.get_pos()
            mousex = pos[0]
            mousey = pos[1]
            screen.blit(backgroundIMG, [0, 0])
            if not options:
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
                text = font.render(("QUIT") ,True, (0, 0, 0))
                screen.blit(text, [475, 460])
            if options:
                pygame.draw.rect(screen, (40,213,255), (480, 190, 200, 60))
                font = pygame.font.SysFont('arial', 30, True, False)
                text = font.render(("DUCK SPEED") ,True, (0, 0, 0))
                screen.blit(text, [490, 200])

                pygame.draw.rect(screen, (40,213,255), (660, 190, 60, 30))
                font = pygame.font.SysFont('arial', 30, True, False)
                text = font.render(("+") ,True, (0, 0, 0))
                screen.blit(text, [660, 190])

                pygame.draw.rect(screen, (40,213,255), (665, 220, 60, 30))
                font = pygame.font.SysFont('arial', 30, True, False)
                text = font.render(("-") ,True, (0, 0, 0))
                screen.blit(text, [665, 210])

                pygame.draw.rect(screen, (40,213,255), (465, 450, 160, 60))
                font = pygame.font.SysFont('arial', 30, True, False)
                text = font.render(("BACK") ,True, (0, 0, 0))
                screen.blit(text, [475, 460])

                
        
        pygame.display.update()
        clock.tick(15)

def Main(): 
    # Loop until the user clicks the close button.
    frameCount = 0
    score = 0
    done = False
    pygame.mouse.set_visible(False)
    player = Player(16, "redCross", 1, 5)
    oleDuckyList = []
    
    #pygame.mouse.set_pos([0,0])

    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(oleDuckyList)-1, -1, -1):
                    shotVals = shootTarget(oleDuckyList[i], mousex, mousey)
                    shotPos = shotVals[0]
                    duckShot = shotVals[1]
                    #bodyshot = 0 : headshot = 1
                    #0.5 = small duck : 1 = normal duck : 2 = big duck
                    if shotPos == 0:
                        if duckShot == 1 or duckShot == 2:
                            score += 100 * player.spd_multiplier
                        elif duckShot == 0.5:
                            score += 150 * player.spd_multiplier
                        oleDuckyList.pop(i)

                    elif shotPos == 1:
                        if duckShot == 1:
                            score += 500 * player.spd_multiplier
                            player.change_lives(0.1)
                        elif duckShot == 2:
                            score += 300 * player.spd_multiplier
                            player.change_lives(0.5)
                        elif duckShot == 0.5:
                            score += 750 * player.spd_multiplier
                            player.change_lives(0.25)
                        oleDuckyList.pop(i)

        #ends the game when you run out of lives
        if player.lives == 0:
            done = True
            gameOver()

        #hi
        pos = pygame.mouse.get_pos()
        mousex = pos[0]
        mousey = pos[1]
        
        #Creates ducks based off the frame counter
        duckSpawns(frameCount, oleDuckyList, player)

        # Clear the screen and set the screen background
        screen.blit(backgroundIMG, [0, 0])

        #draw functions here v
        for i in range(len(oleDuckyList)):
            oleDuckyList[i].move_targetx(oleDuckyList[i].xspd)
            oleDuckyList[i].move_targety(oleDuckyList[i].yspd)
            drawTargets(screen, oleDuckyList[i], frameCount)

        #draws the lives on screen
        for i in range(math.floor(player.lives)):
            screen.blit(pogchamp, [0 + i * 70, 5])
        
        #draws mouse crosshair
        pygame.draw.line(screen, (255,0,0), [mousex + 9, mousey], [mousex - 8, mousey], 2)
        pygame.draw.line(screen, (255,0,0), [mousex, mousey + 9], [mousex, mousey - 8], 2)

        #draws multiplier
        font = pygame.font.SysFont('arial', 32, True, False)
        text = font.render("x" +(str(player.spd_multiplier)) ,True, (255, 0, 0))
        screen.blit(text, [960, 670])   
        #draws score
        font = pygame.font.SysFont('arial', 28, True, False)
        text = font.render((str(round(score))) ,True, (0, 0, 0))
        screen.blit(text, [960, 5]) 

        #removes offscreen ducks         
        for i in range(len(oleDuckyList)-1, -1, -1):
            if oleDuckyList[i].x > 1200 or oleDuckyList[i].x < -100 or oleDuckyList[i].y > 1000 or oleDuckyList[i].y < -100:
                player.change_lives(-1)
                oleDuckyList.pop(i)

        frameCount += 1
        pygame.display.flip()
        clock.tick(66)
    

class Target:
    def __init__(self, x, y, length, height, xspd, yspd, image, animation_frame):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.xspd = xspd
        self.yspd = yspd
        self.image = image
        self.animation_frame = animation_frame
        self.alive = True
    def move_targetx(self, xchange):
        self.x += xchange
    def move_targety(self, ychange):
        self.y += ychange

class Player:
    def __init__(self, ammo, crosshair, spd_multiplier, lives):
        self.ammo = ammo
        self.crosshair = crosshair
        self.spd_multiplier = spd_multiplier
        self.lives = lives
    def change_spd(self, spd_change):
        self.spd_multiplier += spd_change
        self.spd_multiplier = round(self.spd_multiplier, 3)
    def change_lives(self, lives):
        self.lives += lives
        self.lives = round(self.lives, 2)

def drawTargets(screen, atarget, frame):
    if frame % 10 == 0:
        atarget.animation_frame +=1
        if atarget.animation_frame > 4:
            atarget.animation_frame = 0
    if atarget.alive:
        screen.blit(atarget.image[atarget.animation_frame], [atarget.x, atarget.y]) 

def shootTarget(atarget, mousex, mousey):
    #scales the hitbox for the  different sized ducks
    xscalar = atarget.length / 66
    yscalar = atarget.height / 48
    if atarget.image[0] == duckIMGflip:
        xscalar *= -1
        
    #head hitbox             change the whole number values to fit the other duck sizes
    if (mousex > atarget.x + 37 * xscalar and mousex < atarget.x + atarget.length - 11 * xscalar and mousey > atarget.y + 11 * yscalar and mousey < atarget.y + atarget.height - 19 * yscalar):
        return 1, yscalar #headshot
    elif (mousex > atarget.x and mousex < atarget.x + atarget.length - 27 * xscalar and mousey > atarget.y + 19 * yscalar and mousey < atarget.y + atarget.height - 6 * yscalar):
        return 0, yscalar #bodyshot
    else: 
        return 10, 10
        
def duckSpawns(frame, oleDuckyList, player):
    if frame > 0:
        if frame % 250 == 0:
            oleDuckyList.append(Target(-66, 500, 66, 48, 1.5 * player.spd_multiplier, random.uniform(-1.8,0.2) * player.spd_multiplier, regularDuckIMGList, 0))
        if frame % 520 == 0:
            oleDuckyList.append(Target(230, 720, 66, 48, 1.3 * player.spd_multiplier, -0.2 * player.spd_multiplier, regularDuckIMGList, 0))
        if frame % 720 == 0:
            oleDuckyList.append(Target(1080, 600, 66, 48, -2 * player.spd_multiplier, -0.5 * player.spd_multiplier, flipDuckIMGList, 0))
        if frame % 800 == 0:
            oleDuckyList.append(Target(-66, 50, 66, 48, 3 * player.spd_multiplier, 0 * player.spd_multiplier, regularDuckIMGList, 0))
        #progressively increases duck speed
        if frame % 120 == 0:
            player.change_spd(0.01)
    if frame > 1500:
        if frame % 240 == 0:
            oleDuckyList.append(Target(1080, 660, 66, 48, -2.3 * player.spd_multiplier, random.uniform(-1.5,-0.3) * player.spd_multiplier, flipDuckIMGList, 0))
        if frame % 800 == 0:
            oleDuckyList.append(Target(-66, 250, 33, 24, 1 * player.spd_multiplier, 0 * player.spd_multiplier, smallDuckIMGList, 0))
    if frame > 2400:
        if frame % 1000 == 0:
            oleDuckyList.append(Target(-66, 20, 33, 24, 0.7 * player.spd_multiplier, 0 * player.spd_multiplier, smallDuckIMGList, 0))
        if frame % 500 == 0:
            oleDuckyList.append(Target(-66, 500, 132, 96, 3 * player.spd_multiplier, 0 * player.spd_multiplier, bigDuckIMGList, 0))
        if frame % 700 == 0:
            oleDuckyList.append(Target(400, 800, 132, 96, 0.1 * player.spd_multiplier, -3 * player.spd_multiplier, bigDuckIMGList, 0))
    if frame > 3500:
        if frame % 1200 == 0:
            oleDuckyList.append(Target(-66, 100, 33, 24, 1.6 * player.spd_multiplier, 0.2 * player.spd_multiplier, smallDuckIMGList, 0))

def gameOver():
    gameover = True
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                
        screen.blit(notpog, [0,0])
        font = pygame.font.SysFont('arial', 28, True, True)
        text = font.render(("you let them get you... you let those foul mallards run right through you...") ,True, (0, 0, 0))
        screen.blit(text, [0, 5]) 
        text = font.render(("Well, I hope you happy with yourself. But I just want you to know that you could have won. There is an end to it all, but you werent good enough to reach it. Stew on that for a while before you try again.") ,True, (0, 0, 0))
        screen.blit(text, [0, 50])
        text = font.render(("There is an end to it all, but you werent good enough to reach it. Stew on that for a while before you try again.") ,True, (0, 0, 0))
        screen.blit(text, [0, 95])

        pygame.display.update()
        clock.tick(15)
   
startMenu()