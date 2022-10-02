import pygame
import parse

# The dimensions of the map is confirmed to be the 10x10
ROW = 10
COLUMN = 10

# sound effects
WIZARD_ATTACK_SOUND = "./sounds/Retro Magic 06.wav"
MOVEMENT_SOUND = "./sounds/Retro Impact Punch 07.wav"

class Map:
    
    """
    Map class has 4 attributes currently:
    - wizard_frame
    - dice_frame
    - map: the map of the game (with all the tiles)
    - surface: the window of the game
    """

    def __init__(self, data, surface, cur_level, levels):
        """
        Initialise the Map data structure.
        It requires the map data and the surface (or window)
        
        :param data: 2d matrix (or a list of lists)
        :param surface: pygame.Surface
        """

        # initialize the mixer
        pygame.mixer.init()

        self.wizard_frame = 0
        self.cur_level = cur_level
        self.dice_frame = 1
        self.map = data
        self.surface = surface
        self.levels =levels
        self.dice = pygame.image.load("./dice/dice.png")
        self.dice_position= "default" # default /default2 / right/ down/ up /left
        self.time = levels[cur_level-1]['time']
        self.tick = 0
        self.myfont = pygame.font.SysFont("Rammetto One",35,bold =True)
        self.wizard_attack =False
        self.reset = False
        self.attack_position = (-1,-1)
        self.attack_frame =0
        
    
    def read_data(self):
        """
        Set the sprite of the map in each tile (all the tiles)
        """
        if self.time <= 0 :
            # print(self.cur_level)
            self.map = parse.read_map(self.levels[ self.cur_level - 1 ]['path'])
            self.time = self.levels[self.cur_level-1]['time']
            self.reset = True
        else:
            for i in range (ROW):
                for j in range(COLUMN):
                    self.set_sprite(self.map[i][j],i,j)

    def get_reset(self):
        return self.reset
    
    def set_reset(self, reset):
        self.reset = reset
    
    def set_sprite(self, symbol, i: int, j: int):
        """
        Set the sprite and store it into the the map
        Formula:
        x-coor: (j * 62) + 315 - (i * 27)
        y-coor: i * 34 + 150
        Args:
            symbol (_type_): the symbol from the map
            i (_type_): row
            j (_type_): column
        """
        clock = pygame.image.load("./images/clock.png")
        label = self.myfont.render("{}".format(self.time), 1, (233,233,255,1))
        self.surface.blit(label, (295, 100))
        self.surface.blit(clock, (240, 96))
        
        
        self.tick+=1
        if self.tick == 1600:
            self.tick =0
            self.time -=1
        if self.wizard_attack and i == self.attack_position[0] and j == self.attack_position[1]:

            if self.attack_frame >= 8:
        
                self.attack_position = (-1,-1)
                self.wizard_attack = False
                self.attack_frame = 0
            sprite = pygame.image.load("./images/Vector 135.png")
            self.surface.blit (sprite , ((j*62)+315-(i*27),(i*34)+150))
 
            wizard = pygame.image.load("./images/attack.png")    
            self.surface.blit (wizard , ((j*62)+250-(i*27),(i*34)+35),((self.attack_frame*231),0,231,180))
            self.attack_frame +=1
        
        elif symbol == 'W':
            
             
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
        elif symbol == 'T':
            tile = pygame.image.load("./images/teleport.png")
            self.surface.blit (tile , ((j*62)+315-(i*27),(i*34)+150))

        elif symbol == 'E':
            tile = pygame.image.load("./images/end.png")
            self.surface.blit (tile , ((j*62)+315-(i*27),(i*34)+150))
            
        elif symbol == 'P':
            self.surface.blit (self.dice , ((j*62)+315-(i*27),(i*34)+85))
            
        elif symbol == 'M':
            sprite = pygame.image.load("./images/floor.png")
                                  
            self.surface.blit (sprite , ((j*62)+315-(i*27),(i*34)+150))
        # elif symbol == ''
        elif symbol == 'H':
            sprite = pygame.image.load("./images/red-success.png")
            self.surface.blit (sprite , ((j*62)+315-(i*27),(i*34)+150))
        elif symbol == 'K':
            sprite = pygame.image.load("./images/green-success.png")
            self.surface.blit (sprite , ((j*62)+315-(i*27),(i*34)+150))
        elif symbol == 'L':
            sprite = pygame.image.load("./images/red-fail.png")
            self.surface.blit (sprite , ((j*62)+315-(i*27),(i*34)+150))
        elif symbol == 'N':
            sprite = pygame.image.load("./images/green-fail.png")
            self.surface.blit (sprite , ((j*62)+315-(i*27),(i*34)+150))

        elif symbol == 'T':
            sprite = pygame.image.load("./images/teleport.png")
            self.surface.blit (sprite, ((j*62)+315-(i*27),(i*34)+150))
           
    def set_direction_default(self,direction):
        if direction == "right" :
            self.dice =pygame.image.load("./dice/right.png")
            self.dice_position = "right"
        elif direction == "left":
            self.dice =pygame.image.load("./dice/left.png")
            self.dice_position="left"
        elif direction == "up":
            self.dice =pygame.image.load("./dice/up.png")
            self.dice_position ="up"
        elif direction == "down":
            self.dice =pygame.image.load("./dice/down.png")
            self.dice_position ="down"
    def set_direction_default2(self,direction):
        if direction == "right" :
            self.dice =pygame.image.load("./dice/left.png")
            self.dice_position ="left"
        elif direction == "left":
            self.dice =pygame.image.load("./dice/right.png")
            self.dice_position ="right"
        elif direction == "up":
            self.dice =pygame.image.load("./dice/down.png")
            self.dice_position ="down"
        elif direction == "down":
            self.dice =pygame.image.load("./dice/up.png")
            self.dice_position ="up"
    def set_direction_right(self,direction):
        if direction == "right" :
            self.dice =pygame.image.load("./dice/dice2.png")
            self.dice_position ="default2"
        elif direction == "left":
            self.dice =pygame.image.load("./dice/dice.png")
            self.dice_position ="default"
        elif direction == "up":
            self.dice =pygame.image.load("./dice/right.png")
            self.dice_position ="right"
        elif direction == "down":
            self.dice =pygame.image.load("./dice/right.png")
            self.dice_position ="right"
            
    def set_direction_left(self,direction):
        if direction == "right" :
            self.dice =pygame.image.load("./dice/dice.png")
            self.dice_position ="default"
        elif direction == "left":
            self.dice =pygame.image.load("./dice/dice2.png")
            self.dice_position ="default2"
        elif direction == "up":
            self.dice =pygame.image.load("./dice/left.png")
            self.dice_position ="left"
        elif direction == "down":
            self.dice =pygame.image.load("./dice/left.png")
            self.dice_position ="left"
    def set_direction_up(self,direction):
        if direction == "right" :
            self.dice =pygame.image.load("./dice/up.png")
            self.dice_position ="up"
        elif direction == "left":
            self.dice =pygame.image.load("./dice/up.png")
            self.dice_position ="up"
        elif direction == "up":
            self.dice =pygame.image.load("./dice/dice2.png")
            self.dice_position ="default2"
        elif direction == "down":
            self.dice =pygame.image.load("./dice/dice.png")
            self.dice_position ="default"
    def set_direction_down(self,direction):
        if direction == "right" :
            self.dice =pygame.image.load("./dice/down.png")
            self.dice_position ="down"
        elif direction == "left":
            self.dice =pygame.image.load("./dice/down.png")
            self.dice_position ="down"
        elif direction == "up":
            self.dice =pygame.image.load("./dice/dice.png")
            self.dice_position ="default"
        elif direction == "down":
            self.dice =pygame.image.load("./dice/dice2.png")
            self.dice_position ="default2"
            
    def set_direction(self,direction):

        if self.dice_position == "default":
            self.set_direction_default(direction)
        
        elif self.dice_position == "default2":
            self.set_direction_default2(direction)
        elif self.dice_position=="right":
            self.set_direction_right(direction)
        elif self.dice_position=="left":
            self.set_direction_left(direction)
        elif self.dice_position=="up":
            self.set_direction_up(direction)
        elif self.dice_position=="down":
            self.set_direction_down(direction)
        
    
    def move(self, direction):
        self.set_direction(direction)

        # while playing background music, play the movement sound as well
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(MOVEMENT_SOUND), maxtime=500)
        
    def attack(self, i , j):
        self.wizard_attack = True
        self.time -= 5
        self.attack_position =(i,j)
        
        # while playing background music, play wizard attack sound as well
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(WIZARD_ATTACK_SOUND), maxtime=500)
        

    def get_dice_position(self):
        """
        Return the dice's position
        """
        return self.dice_position
    
