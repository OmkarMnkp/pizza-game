#importingt he library
import pygame
import random
import math

#initilizing it
pygame.init()

#screen
screen = pygame.display.set_mode((600,345))

#caption 
pygame.display.set_caption("catch the pizza")
icon = pygame.image.load("pizza (1).png")
pygame.display.set_icon(icon)

#background
background = pygame.image.load("house.png")

#player info
playerimage = pygame.image.load("man.png")
player_x = 300
player_y = 280
playerchange_x=0
playerchange_y=0

#pizza info
pizzaimage = pygame.image.load("pizza (1).png")
pizza_x = random.randint(0,550)
pizza_y = random.randint(20,90)
pizzachange_x=0
pizzachange_y=0.7

#score
score_value =0
font = pygame.font.Font("freesansbold.ttf",32)
text_x =10
text_y = 10

#game over
over_font= pygame.font.Font("freesansbold.ttf",64)


def player(player_x,player_y):
    screen.blit(playerimage,(player_x,player_y))

def pizza (pizza_x,pizza_y):
    screen.blit(pizzaimage,(pizza_x,pizza_y))


#finding values for the collision between two objects
def iscollision(pizza_x,pizza_y,player_x,player_y):
    #to find difference between two points use d = /-(x2-x1)(y2-y1)
    distance = math.sqrt(math.pow(pizza_x-player_x,2)+(math.pow(pizza_y-player_y,2)))
    if distance<=27:
        return True
    else:
        return False

#score showing
def score(x,y):
    score = font.render("score :"+str(score_value),True,(0,0,0))
    screen.blit(score,(x,y))

#game over
def game_over():
     over = font.render("GAME OVER",True,(0,0,0))
     screen.blit(over,(200,177))

#game loop
running = True
while running:
    #background color
    screen.fill((0,0,0))

    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False
        
        #if any key is pressed
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_LEFT: #if left key is pressed
                playerchange_x-=2

            if event.key==pygame.K_RIGHT: #if right is pressed
                playerchange_x+=2
        
        #if key is not pressed 
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerchange_x = 0
            
    #setting the boundaries for the player
    if player_x<=0:
        player_x=0
    elif player_x>=550:
        player_x=550

    #pizza movement
  
    if pizza_x:
        pizza_y+=pizzachange_y
   
    #game over
    if pizza_y>335:
        pizza_y=2000
        game_over()
        
   
    #collison
    collision = iscollision(pizza_x,pizza_y,player_x,player_y)
    if collision:
        pizza_y=50
        score_value+=1
    
        pizza_x = random.randint(0,550)
        pizza_y = random.randint(20,90)
    
    pizza_x+=pizzachange_x
    player_x+=playerchange_x


    player(player_x,player_y)
    pizza(pizza_x,pizza_y)
    score(text_x,text_y)

    #updating the display
    pygame.display.update()
