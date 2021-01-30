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

    #  Stop here until next week 