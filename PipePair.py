import pygame 
from pygame.locals import *
from Bird.py import *
import random

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

        numPipeBody = (windowHeight - 3 * Bird.Height - 3 * PipePair.Height) / PipePair.Height

        self.bottomPiece = randint(1, numPipeBody)

        self.topPiece = numPipeBody - sel.bottomPiece


        # bottom pipe
        for i in range(1, self.bottomPiece + 1):
            piecePos = (0, windowHeight - (i * PipePair.Height))
            self.image.blit(pipeBodyImg, piecePos)

        bottomPipeEndy = windowHeight - self.bottomHeightPx

























# Resources : https://github.com/TimoWilken/flappy-bird-pygame/blob/master/flappybird.py