import parse
import pygame

ROW = 10
COLUMN= 10

class Map:
    def __init__(self,data,surface):
        self.wizard_frame = 0
        self.dice_frame=0
        
        self.map = data
        self.surface = surface
        
    def get_map(self):
        return self.map
    
    def read_data(self,player):
        for i in range (ROW):
            for j in range(COLUMN):
                self.set_sprite(self.map[i][j],i,j,player)
          
        
            
    def set_sprite(self,symbol, i , j,player):
   
        if symbol == 'W':
            if self.wizard_frame == 6:
                self.wizard_frame = 0
      
        
            sprite = pygame.image.load("./images/Vector 135.png")
            self.surface.blit (sprite , ((j*62)+315-(i*27),(i*34)+150))
            
           
            wizard = pygame.image.load("./images/Idle.png")
            
            self.surface.blit (wizard , ((j*62)+250-(i*27),(i*34)+35),((self.wizard_frame*231),0,231,180))
           

            self.wizard_frame+=1
        elif symbol == 'R':
            tile = pygame.image.load("./images/red.png")
            self.surface.blit (tile , ((j*62)+315-(i*27),(i*34)+150))
        elif symbol == 'G':
            tile = pygame.image.load("./images/green.png")
            self.surface.blit (tile , ((j*62)+315-(i*27),(i*34)+150))
        elif symbol == 'E':
            tile = pygame.image.load("./images/end.png")
            self.surface.blit (tile , ((j*62)+315-(i*27),(i*34)+150))
            
        elif symbol == 'P':
            dice = pygame.image.load("./dice/dice.png")
            # print(self.dice_frame)
            dice =pygame.transform.rotate(dice, self.dice_frame*-20) 
            if self.dice_frame <9:
                self.dice_frame +=1
            if self.dice_frame ==9:
                self.dice_frame=9
            
            self.surface.blit (dice , ((j*62)+315-(i*27),(i*34)+85))
            player.update()
            player.draw(self.surface)
        elif symbol == 'M':
            sprite = pygame.image.load("./images/Vector 36.png")
            self.surface.blit (sprite , ((j*62)+315-(i*27),(i*34)+150))
            
            

