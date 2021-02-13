import pygame 
from pygame.locals import *
from Bird.py import *
from fb.py import * 
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
        bottomPipeEndPos = (0, bottomPipeEndy - PipePair.Height)
        self.image.blit(pipEndImg, bottomPipeEndPos)


        # top pipe 
        for i in range(self.topPiece):
            self.image.blit(pipeBodyImg, (0, bottomPipeEndy - i * PipePair.Height))

        topPipeEndy = self.topHeightPx
        self.image.blit(pipEndImg, (0, topPipeEndy))

        self.topPiece += 1
        self.bottomPiece += 1
        
        self.mask = pygame.mask.from_surface(self.image)


    @property
    def topHeightPx(self):
        return self.topPiece * PipePair.Height

    @property
    def bottomHeightPx(self):
        return self.bottomPiece * PipePair.Height

    @property
    def visible(self):
        return -1 * PipePair.Width < self.x < windowWidth

    @property
    def rect(self):
        return Rect(self.x, 0, PipePair.Width, PipePair.Height)


    def update(self, deltaFrames = 1):
        self.x -= ANIMATION_SPEED * framesToMSec(deltaFrames)
    
    def collidesWith(self, bird):
        return pygame.sprite.collide_mask(self.bird)




























# Resources : https://github.com/TimoWilken/flappy-bird-pygame/blob/master/flappybird.py