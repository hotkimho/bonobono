import pygame
import random
WHITE=(155,200,1)
width=1024
height=512
background_width = 1024

def drawObject(obj,x,y):
    global  gamepad
    gamepad.blit(obj,(x,y))
# kimho

def runGame():
    global gamepad,clock,hamzzi_image,background,background2
    global enemy,hodus
    x=width*0.05
    y=height*0.8
    y_change=0
    background_x=0
    background2_x=background_width

    enemy_x=width
    enemy_y=random.randrange(0,height)

    hodu_x=width
    hodu_y=random.randrange(0,height)
    random.shuffle(hodus)
    hodu=hodus[0]


    crashed= False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed =True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change=0

        y+=y_change

        gamepad.fill(WHITE)

        background_x-=2
        background2_x-=2

        enemy_x -=7
        if enemy_x <= 0:
            enemy_x=width
            enemy_y=random.randrange(0,height)

        if hodu == None:
            hodu_x -=30
        else:
            hodu_x -=15

        if hodu_x <=0:
            hodu_x=width
            hodu_y=random.randrange(0,height)
            random.shuffle(hodus)
            hodu=hodus[0]

        if background_x == -background_width:
            background_x=background_width
        if background2_x == -background_width:
            background2_x = background_width

        drawObject(background,background_x,0)
        drawObject(background2,background2_x,0)
        drawObject(hamzzi_image,x,y)
        drawObject(enemy,enemy_x,enemy_y)
        if hodu != None:
            drawObject(hodu,hodu_x,hodu_y)
        pygame.display.update()
        clock.tick(60)
        if crashed == True:
            pygame.quit()

def initGame():
    global gamepad, clock,hamzzi_image,background,background2
    global enemy,hodus

    hodus=[]
    pygame.init()
    gamepad=pygame.display.set_mode((width, height))
    pygame.display.set_caption("창꼬십팔")
    clock = pygame.time.Clock()
    hamzzi_image=pygame.image.load('res/hamzzi.jpg')
    background = pygame.image.load('res/background.jpg')
    background2 = background.copy()
    enemy= pygame.image.load('res/enemy.jpg')
    hodus.append(pygame.image.load('res/hodu.jpg'))
    hodus.append(pygame.image.load('res/hodu2.jpg'))

    for i in range(5):
        hodus.append(None)

    runGame()



if __name__ == '__main__':
    initGame()
