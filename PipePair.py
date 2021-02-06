import pygame 
from pygame.locals import *

windowWidth = 568
windowHeight = 512


class PipePair(pygame.sprite.Sprite):
    Width = 80
    Height = 32
    ADD_INTERVAL = 3000


    def __init__(self, pipEndImg, pipeBodyImg):
        self.x = float(windowWidth - 1)
        self.scoreCounted = False
        
        self.image = pygame.Surface((PipePair.Width, windowHeight), SRCALPHA)
        self.image.convert()
        self.image.fill((0,0,0,0))