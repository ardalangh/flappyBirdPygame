# Imports 
import pygame 
from pygame.locals import *
import math
import os
from random import randint
from collections import deque


# Game Setting
windowWidth = 568
windowHeight = 512
# frames per second
FPS = 60
ANIMATION_SPEED = 0.18 




# Load Images Function 
def loadImages()





# Main function
def main():
    pygame.init()
    surface = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Falppy Bird by Ardy")

    clock = pygame.time.Clock()
    scoreFont = pygame.font.SysFont(None, 32, bold = True)
    images = loadImages()
