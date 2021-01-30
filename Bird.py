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