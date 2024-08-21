import pygame, sys

#setting up 

pygame.init()
clock = pygame.time.Clock()

#setting up main window

screen_width = 960
screen_height = 560

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

##################################################
# RECTANGLES/SPRITES FOR THE GAME
##################################################

ball = pygame.Rect(screen_width/2-15, screen_height/2-15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('black')
light_grey = pygame.Color('white')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #drawing
    screen.fill(bg_color)

    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    #ingame clock
    pygame.display.flip()
    clock.tick(60)