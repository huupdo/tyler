#Book title: Code This Game by Tim Hall

#import libraries
import pygame
from pygame import *

#initilize pygame
pygame.init()

#Define constant variable
#to do: create a variable for the window width here
WINDOW_WIDTH = 900
#to do: create a variable for the window height here
WINDOW_HEIGHT = 400
#to do: create a variable for the window resolution here
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
#create window
#to do: replace the argument int the set_mode method below
GAME_WINDOW=display.set_mode(WINDOW_RES)
display.set_caption('Attack of Vampire Pizzas!')



#-----------------------------------------------
#Start Main Game Loop
game_running=True

#game loop
while game_running:

#Check for events
    for event in pygame.event.get():
        if event.type==QUIT:
            game_running=False
    display.update()

#End of main game loop

#-----------------------------------------------

#Clean up game
pygame.quit()
