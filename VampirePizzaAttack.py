#Book title: Code This Game by Tim Hall

#import libraries
import pygame
from pygame import *

#initilize pygame
pygame.init()

#Define constant variable
#to do: create a variable for the window width here
WINDOW_WIDTH = 1100
#to do: create a variable for the window height here
WINDOW_HEIGHT = 600
#to do: create a variable for the window resolution here
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
#create window
#to do: replace the argument int the set_mode method below
GAME_WINDOW=display.set_mode(WINDOW_RES)
display.set_caption('Attack of Vampire Pizzas!')

#set up the enemy image
#load the image into the program
pizza_img = image.load('./gameassets/vampire.png')
#convert the image into a surface
pizza_surf = Surface.convert_alpha(pizza_img)

#resize and display image
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (900,400))


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
