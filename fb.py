# Imports 
import pygame 
from pygame.locals import *
import math
import os
from random import randint
from collections import deque
from Bird.py import * 
from PipePair.py import * 


# Game Setting
windowWidth = 568
windowHeight = 512
# frames per second
FPS = 60
ANIMATION_SPEED = 0.18 





"""
    Load Images Function 
    returns : a dictioanry of loaded imgs
"""
def loadImages():
    
    """
        function is in charge of loading a single img
        prams: imgFileDir : is the address to the img
        returns: converted() img
    """
    def loadImage(imgFileDir):
        fileName = os.path.join(os.path.dirname(__file__),
                                'images', imgFileDir)
        img = pygame.image.load(fileName)
        img.convert()
        return img


    return {
        'background' : loadImage('background.png'),
        'pipe' : loadImage('pipe.png'),
        'pipe_end' : loadImage('pipe_end.png'),
        'pipe_body' : loadImage('pipe_body.png'),
        'ground' : loadImage('ground.png'),
        'bird' : loadImage('bird.png'),
        'bird_wing_up' : loadImage('bird_wing_up.png'),
        'bird_wing_down' : loadImage('bird_wing_down.png'),
    }
    






def framesToMSec(frames, fps = FPS): return 1000.0 * frames / fps

def mSecTOFrames(ms, fps = FPS): return fps * ms / 1000.0




# Main function
def main():
    pygame.init()
    surface = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Falppy Bird by Ardy")

    clock = pygame.time.Clock()
    scoreFont = pygame.font.SysFont(None, 32, bold = True)
    images = loadImages() #images is a dictionary of all imgs

    bird = Bird(50, int(windowHeight / 2 - Bird.Height / 2), 2, (images['bird_wing_up', images['bird_wing_down']]) )