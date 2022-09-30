import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
 
        self.image = pygame.image.load("dice/dice.png")
 
        self.index = 0

 
        self.rect = pygame.Rect(0, 0, 0, 0)
 
    def update(self):
        if self.index != 18:
            self.index += 1
 
        if self.index >= 18:
            self.index = 18
            
        self.image = pygame.image.load("dice/dice.png")
        self.image = pygame.transform.rotate(self.image,self.index*5)
        
        