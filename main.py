import pygame
import math
import random
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invader Game")
playerX=WIDTH//2-25
playerY=HEIGHT-120
playerX_change=0
background=pygame.image.load("bg.webp")
player_img=pygame.image.load("space_fighter.png")
bullet_img=pygame.image.load("bullet.png")

enemy_img=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,WIDTH-50))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"
score_value=0
font=pygame.font.Font("Montserrat-Italic-VariableFont_wght.ttf",32)
textX=10
textY=10
def show_score(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
