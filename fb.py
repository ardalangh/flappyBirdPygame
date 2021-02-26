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






def framesToMSec(frames, fps = FPS): return 1000.0 * frames / fps

def mSecTOFrames(ms, fps = FPS): return fps * ms / 1000.0















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
            self.y -= Bird.ClimbSpeed * framesToMSec(deltaFrame) * (1 - math.cos(self.secToClimb * math.pi))
            self.secToClimb -= framesToMSec(deltaFrame)
        else:
            self.y += Bird.SinkSpeed * framesToMSec(deltaFrame)


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
            return self._mask_wingdown

    @property
    def rect(self):
        return Rect(self.x, self.y, Bird.Width, Bird.Height)






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

        self.topPiece = numPipeBody - self.bottomPiece


        # bottom pipe
        for i in range(1, self.bottomPiece + 1):
            piecePos = (0, windowHeight - (i * PipePair.Height))
            self.image.blit(pipeBodyImg, piecePos)

        bottomPipeEndy = windowHeight - self.bottomHeightPx
        bottomPipeEndPos = (0, bottomPipeEndy - PipePair.Height)
        self.image.blit(pipEndImg, bottomPipeEndPos)


        # top pipe 
        for i in range(int(self.topPiece)):
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
        return pygame.sprite.collide_mask(self, bird)






































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

        if collisions or 0 >= bird.y or bird.y >= windowHeight - Bird.Height:
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
        

        