import math
import pygame
import random

SW = 1000
SH = 780
PSX = 410
PSY = 420
ESYMN = 50
ESYMX = 250
ESX = 7
ESY = 24
BSY = 20
CD = 27
pygame.init()
screen = pygame.display.set_mode((SW, SH))
background = pygame.image.load("background.png")
pygame.display.set_caption("SPACE INVADERS!")

icon = pygame.image.load("UFO.png")
pygame.display.set_icon(icon)
pg = pygame.image.load("you.png")
player_X = PSX
player_Y = PSY
playerX_change = 0

eg = []
ex = []
ey = []
ex_change = []
ey_change = []
ne = 6
eg.append(pygame.image.load('invader.png'))
ex.append(random.randint(0,SW - 64))
ey.append(random.randint(ESYMN, ESYMX))
ex_change.append(ESX)
ey_change.append(ESY)

bmg = pygame.image.load("bullet")
bx = 0
by = PSY
bulletx_change = 0
bullety_change = BSY
bs = "ready"

font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
ofont = pygame.font.Font('freesansbold.ttf',64)
def show_s(x,y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    ofont = over_font.render("Game over", True, (255,255,255))
    screen.blit = ofont((200,250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def f_b(x, y):
    global bs
    bs = "fire"
    screen.blit(bulletImg,(x + 16, y + 10))

def ic(ex, ey, bx, by):
    d = math.sqrt((ex - bx) ** 2 + (ey - by) ** 2)
    return distance < CD 

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bs == "ready":
                bx = player_X
                f_b(bx, by)
        if event.key == pygame.KEY_UP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change == 0
    player_X += playerX_change
    player_X = max(0, min(player_X, SW - 64))

    for i in range (num_of_enemies):
        if ey[i] > 340:
            for j in range(num_of_enemies):
                ey[j] = 2000
            game_over_text()
            break
        ex[i] += ex_change[i]
        if ex[i] <= 0 or ex[i] >= SW - 64:
            ex_change[i] == -1
            ey[i]  += ey_change[i]

        if ic(ex[i], ey[i], bx, by):
            by = PSY
            bs = "ready"
            score_value += 1
            ex[i] = random.randint(0, SW - 64)
            ey[i] = random.randint(ESYMN, ESYMX)
        enemy = (ex[i], ey[i],i)
    if by <= 0:
        by = PSY
        bs = "ready"
    elif bs == "fire":
        f_b(bx, by)
        by = bullety_change

    player(player_X, player_Y)
    show_s(textX, textY)
    pygame.display.update()

    



             

             


            








