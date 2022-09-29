import parse
import pygame

ROW = 13
COLUMN= 13


class Map:
    def __init__(self,data,surface):
        self.wizard_frame = 0
        self.dice_frame=1
        
        self.map = data
        self.surface = surface
    
    def read_data(self):
        for i in range (ROW):
            for j in range(COLUMN):
                self.set_sprite(self.map[i][j],i,j)
          
        
            
    def set_sprite(self,symbol, i , j):
        if symbol == 'DA':
            if self.wizard_frame == 6:
                self.wizard_frame = 0
      
        
            sprite = pygame.image.load("dragon_stand.png")
           
            self.surface.blit(sprite,((j*66)+99,(i*66)+66))
        
            wizard = pygame.image.load("idle.png")
            

            self.surface.blit(wizard,((j*66)+30,(i*66)-18),((self.wizard_frame*231),0,231,180))

            self.wizard_frame+=1
        elif symbol == 'D':
            if self.wizard_frame == 6:
                self.wizard_frame = 0
      
        
            sprite = pygame.image.load("Vector 135.png")
            
           
            self.surface.blit(sprite,((j*66)+99,(i*66)+66))
        
            wizard = pygame.image.load("idle.png")
            

            self.surface.blit(wizard,((j*66)+30,(i*66)-18),((self.wizard_frame*231),0,231,180))

            self.wizard_frame+=1
        elif symbol == 'P':
            self.dice_frame+=1
            
            if self.dice_frame ==1:
    
                dice = pygame.image.load("dice/Group 39.png")
                self.surface.blit(dice,((j*62)+66,(i*35)+35))
            elif self.dice_frame ==2:
                dice = pygame.image.load("dice/Group 41.png")
                self.surface.blit(dice,((j*62)+66,(i*35)+25))
                self.dice_frame=1
            self.dice_frame = 0
            
                

            
      
            
     
        
    def draw(self):
        for i in range (ROW):
            for j in range(COLUMN):
                
                if i %2 != 0 and j >=1 :
                 
                    #draw purple
                    sprite = pygame.image.load("Vector 36.png")
                    self.surface.blit(sprite,((j*62)+70,(i*35)+100))
                    
                    
                elif i%2 == 0 and j!= (COLUMN-1):
                    #draw purple
                    sprite = pygame.image.load("Vector 36.png")
                    # self.surface.blit(sprite,((j+1)* 99,(i+1)*66))
                    self.surface.blit(sprite,((j*62)+99,(i*35)+100))
        
            
            
