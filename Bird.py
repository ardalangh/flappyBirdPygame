import math 
import pygame
from pygame.locals import *
"""
    The Bird class will be the sprite/user of our game
    this class is supposed represent the bird object in 
    our game.
"""
class Bird(pygame.sprite.Sprite):
    # class bird variables
    Width = 32
    Height = 32 
    SinkSpeed = 0.18
    ClimbSpeed = 0.3
    ClimbDuration = 333.3



    # consturctor 
    def __init__(self, x, y, secToClimb, images):
        super(Bird, self).__init__()
        self.x = x
        self.y = y
        self.secToClimb = secToClimb
        self._img_wingup , self._img_wingdown = images
        # mask them 
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)

     

    """
        Update the changed that happened to our bird class component of
        at every frame. 
    """
    def update(self, deltaFrame = 1):
        if self.secToClimb > 0:
            fracClimbDone = 1 - (self.secToClimb / Bird.ClimbDuration)
            self.y -= Bird.ClimbSpeed * framesToSec(deltaFrame) * (1 - math.cos(self.secToClimb * math.pi))
            self.secToClimb -= framesToSec(deltaFrame)
        else:
            self.y += Bird.SinkSpeed * framesToSec(deltaFrame)


    @property
    def image(self):
        if pygame.time.get_ticks() % 500 >= 250:
            return self._img_wingup
        else:
            return sel._img_wingdown


    @property
    def mask(self):
        if pygame.time.get_ticks() % 500 >= 250:
            return self._mask_wingup
        else:
            return sel._mask_wingdown

    @property
    def rect(self):
        return Rect(self.x, self.y, Bird.Width, Bird.Height)