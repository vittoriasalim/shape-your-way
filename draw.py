import parse
import pygame

ROW = 10
COLUMN= 10


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
   
        if symbol == 'W':
            if self.wizard_frame == 6:
                self.wizard_frame = 0
      
        
            sprite = pygame.image.load("Vector 135.png")
            self.surface.blit (sprite , ((j*60)+315-(i*27),(i*34)+150))
              
            
           
            wizard = pygame.image.load("idle.png")
            self.surface.blit (wizard , ((j*60)+250-(i*27),(i*34)+35),((self.wizard_frame*231),0,231,180))
           
            # self.surface.blit(wizard,((j*66)+30,(i*66)-18),((self.wizard_frame*231),0,231,180))

            self.wizard_frame+=1
        
        elif symbol == 'P':
            dice = pygame.image.load("dice/Group 39.png")
            self.surface.blit (dice , ((j*60)+315-(i*27),(i*34)+83))
        elif symbol == 'T':
            tile = pygame.image.load("print-tile.png")
            self.surface.blit (tile , ((j*60)+315-(i*27),(i*34)+150))
            
        else:
            sprite = pygame.image.load("Vector 36.png")
            self.surface.blit (sprite , ((j*60)+315-(i*27),(i*34)+150))
            
       
        
    # def draw(self):
    #     for i in range (ROW):
    #         for j in range(COLUMN):
    #             sprite = pygame.image.load("Vector 36.png")
    #             self.surface.blit (sprite , ((j*55)+315-(i*27),(i*34)+150))
            
            
