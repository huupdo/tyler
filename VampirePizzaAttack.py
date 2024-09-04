#import libraries
import pygame
from pygame import *
pygame.init()
GAME_WINDOW=display.set_mode((900,400))
display.set_caption('Attack of Vampire Pizzas!')
#-----------------------------------------------
#Start Main Game Loop
game_running=True
#while game_running
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
