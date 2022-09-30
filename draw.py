import parse
import pygame

# The dimensions of the map is confirmed to be the 10x10
ROW = 10
COLUMN = 10

class Sprite:
    """
    Sprite class, currently these are all the sprites symbols and names:
    - W: wizard
    - R: red tile
    - G: green tile
    - P: player's dice
    - B: indicates that the tile is blocked (the tile is already passed by the player)
    """
    def __init__(self, symbol, path):
        self.symbol = symbol
        self.path = path

    def get_symbol(self):
        return self.symbol

    def get_sprite(self):
        return pygame.image.load(self.path)

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
        for i in range(ROW):
            for j in range(COLUMN):
                if (self.map[i][j] == 'P'):
                    self.starting_position = (i, j)

    def read_data(self):
        """
        Set the sprite of the map in each tile (all the tiles)
        """
        for i in range (ROW):
            for j in range(COLUMN):
                self.set_sprite(self.map[i][j],i,j)
   
    def set_sprite(self, symbol, i , j):
        """
        Set the sprite and store it into the the map
        """
        # draw the wizard sprite
        if symbol == 'W':

            if self.wizard_frame == 6:
                self.wizard_frame = 0

            sprite = pygame.image.load("./images/Vector 135.png")
            self.surface.blit (sprite , ((j*55)+315-(i*27),(i*34)+150))
                   
            wizard = pygame.image.load("./images/Idle.png")
            self.surface.blit (wizard , ((j*55)+250-(i*27),(i*34)+35),((self.wizard_frame*231),0,231,180))

            self.wizard_frame += 1
        
        # draw the tile
        elif symbol == 'T':

            tile = pygame.image.load("./images/print-tile.png")
            self.surface.blit (tile , ((j*55)+315-(i*27),(i*34)+150))
            
        # draw the player's dice
        elif symbol == 'P':

            dice = pygame.image.load("./dice/Group 39.png")
            self.surface.blit (dice , ((j*55)+315-(i*27),(i*34)+85))

    def draw(self):
        for i in range (ROW):
            for j in range(COLUMN):
                sprite = pygame.image.load("./images/Vector 36.png")
                self.surface.blit (sprite , ((j*55)+315-(i*27),(i*34)+150))
            
    def get_starting_position(self):
        """
        Get the starting position of the player
        """
        return self.starting_position
