import pygame

# The dimensions of the map is confirmed to be the 10x10
ROW = 10
COLUMN = 10

class Map:
    """
    Map class has 4 attributes currently:
    - wizard_frame
    - dice_frame
    - map: the map of the game (with all the tiles)
    - surface: the window of the game
    """

    def __init__(self, data, surface: 'pygame.Surface'):
        """
        Initialise the Map data structure.
        It requires the map data and the surface (or window)
        
        :param data: 2d matrix (or a list of lists)
        :param surface: pygame.Surface
        """
        self.wizard_frame = 0
        self.dice_frame = 1
        self.map = data
        self.surface = surface
        self.dice = pygame.image.load("./dice/dice.png")
        self.dice_position= "default" #default /default2 / right/ down/ up /left
        for i in range(ROW):
            for j in range(COLUMN):
                if (self.map[i][j] == 'P'):
                    self.starting_position = (i, j)
                    
        self.check = []
        for i in range(ROW):
            self.check.append([])
            for j in range(COLUMN):
                if (self.map[i][j] == 'R' or self.map[i][j] == 'G'):
                    self.check[i].append(0)
                else:
                    self.check[i].append(1)
        self.check[self.starting_position[0]][self.starting_position[1]] = 1
        self.starting_symbol = 'R'

    def read_data(self):
        """
        Set the sprite of the map in each tile (all the tiles)
        """
        for i in range (ROW):
            for j in range(COLUMN):
                self.set_sprite(self.map[i][j],i,j)


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
            
    def set_direction(self,direction):

        if self.dice_position == "default":
            self.set_direction_default(direction)
        elif self.dice_position=="default2":
            self.set_direction_default2(direction)
        
    
    def move(self, direction):
        self.set_direction(direction)
            
    def get_starting_position(self):
        """
        Get the starting position of the player
        """
        return self.starting_position
        
    def get_starting_symbol(self):
        """
        Get the starting symbol of the dice
        """
        return self.starting_symbol

    def update_check(self, i, j):
        """
        Update the move by the player
        """
        self.check[i][j] = 1

    def has_finished(self):
        """
        Check whether the player has passed all red and green paths
        """
        for i in range(ROW):
            for j in range(COLUMN):
                if (self.check[i][j] != 1):
                    return False
        return True
    def get_dice_position(self):
        return self.get_dice_position
