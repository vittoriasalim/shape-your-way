import pygame
 
 
SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 10 #Frames per second
 
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
 
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
        
        
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BACKGROUND_COLOR)
        my_group.update()
        
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(20)
 
if __name__ == '__main__':
    main()
