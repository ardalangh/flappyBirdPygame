# Imports 
import pygame 
from pygame.locals import *
import math
import os
from random import randint
from collections import deque
from bird import * 
from pipePair import *


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

    bird = Bird(50, int(windowHeight / 2 - Bird.Height / 2), 2, (images['bird_wing_up'], images['bird_wing_down']))

    pipes = deque()

    frameClock = 0 
    score = 0 
    done = pause = False

    while not done:
        clock.tick(FPS)


        if not (pause or frameClock % mSecTOFrames(PipePair.ADD_INTERVAL)):
            pipe = PipePair(images['pipe_end'],images['pipe_body'])
            pipes.append(pipe)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                done = True
                break
            elif event.type == KEYUP and event.key in (K_PAUSE, K_p):
                pause = not pause
            elif event.type == MOUSEBUTTONUP or (event.type == KEYUP and event.key in (K_UP, K_RETURN, K_SPACE)):
                bird.secToClimb = Bird.ClimbDuration

        if pause:
            continue #does not do anything just keeps going
            
        collisions = any(p.collidesWith(bird) for p in pipes)

        if collections or 0 >= bird.y or bird.y >= windowHeight - Bird.Height:
            done = True

        for x in (0, windowHeight / 2):
            surface.blit(images['background'], (x, 0))

        while pipes and not pipes[0].visible:
            pipes.popleft()

        for p in pipes:
            p.update()
            surface.blit(p.image, p.rect)

        bird.update()
        surafce.blit(bird.image, bird.rect)


        for p in pipes:
            if p.x + PipePair.Width < bird.x and not p.scoreCounted:
                score += 1 #score = score + 1
                p.scoreCounted = True
        
        scoreSurface = score_font.render(str(score), True, (255,255,255)) 
        score_x = windowWidth / 2 - scoreSurface.get_width()/ 2 
        surface.blit(scoreSurface, (score_x, PipePair.Height))

        pygame.display.flip()
        frameClock += 1
    
    print(f"Game over! Score: {score}")
    pygame.quit()


if __name__ == '__main__':    
    main()
        

        