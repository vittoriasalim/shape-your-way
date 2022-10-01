import pygame
import draw
import parse

# CONSTANTS
ROW = 10
COL = 10

WHITE = (0xFF, 0xFF, 0xFF)

BG_COLOR = (62, 61, 100)
RECT_COLOR = (233, 226, 246)

SCREEN_WIDTH = 990
SCREEN_HEIGHT = 660

MAX_LEVEL = 2

class Game():
    """
    Game Screen

    Game class has these attributes defined below:
    - is_running: to indicate whether the mainloop is running
    - screen: the window / surface on where the widgets are placed
    - cur_level: the current level of the game
    - data: the map (the level data, for example: level 1)

    - starting_position: the xy coordinate of the starting position
    - starting_symbol: kept to be 'R' for now

    Fonts:
    - myfont
    - endFont
    - buttonFont: for the button

    For each game / level:
    - static_map: it is to indicate the G/R/H/K symbols in the map
    - check: to check whether the player has passed all the required tiles
    """

    def __init__(self, screen, cur_level) -> None:

        # initialize the pygame
        pygame.init()
        
        self.is_running = False
        self.screen = screen
        self.cur_level = cur_level

        print(f"Current Level: {self.cur_level}")

        # load the levels and data according to the indicated current level
        self.levels = parse.parse_json()
        data = parse.read_map(self.levels[ self.cur_level - 1 ]['path'])
        self.data = data

        # font for the game
        self.myfont = pygame.font.SysFont("Rammetto One",35,bold =True)
        self.endFont = pygame.font.SysFont("Rammetto One",60,bold =True)
        self.buttonFont = pygame.font.SysFont("Rammetto One", 40, bold=True)

        # for the game
        for i in range(ROW):
            for j in range(COL):
                if (self.data[i][j] == 'P'):
                    self.starting_position = (i, j)
        self.starting_symbol = 'R'

        # create a copy of the map
        self.static_map = [] # a list of lists
        for i in range(ROW):
            self.static_map.append([])
            for j in range(COL):
                if (self.data[i][j] == "P"):
                    self.static_map[i].append("R")
                else:
                    self.static_map[i].append(self.data[i][j])

        # create an object to store whether the player has passed the tiles
        self.check = []
        for i in range(ROW):
            self.check.append([])
            for j in range(COL):
                if (self.data[i][j] == 'R' or self.data[i][j] == 'G'):
                    self.check[i].append(0)
                else:
                    self.check[i].append(1)
        
        self.check[self.starting_position[0]][self.starting_position[1]] = 1

    def update_check(self, i, j) -> None:
        """
        Update the move by the player
        """
        self.check[i][j] = 1

    def has_finished(self) -> bool:
        """
        Check whether the player has passed all red and green paths
        """
        for i in range(ROW):
            for j in range(COL):
                if (self.check[i][j] != 1):
                    return False
        return True

    def mainloop(self) -> None:

        # create the map
        my_map = draw.Map(self.data, self.screen,self.cur_level, self.levels)

        print("Successfully created the map")

        # get the starting position of the player
        current_position = self.starting_position
        current_symbol = self.starting_symbol

        print(f"The player's current position: {current_position}")

        # tiles that are allowed to go through
        allowed_tiles = [ 'R', 'G', 'M', 'E', 'H', 'K' ]
        
        # main loop
        press = False
        self.is_running = True
        while (self.is_running):
            
            # frame per second
            pygame.time.delay(50)

            # map game
            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    pygame.quit()
                    return True

                elif (event.type == pygame.KEYUP):
                    press = False

            # get the user input
            keys = pygame.key.get_pressed()

            # user interaction with user input
            if keys[pygame.K_LEFT] and press == False:
                
                press = True
                print("\tLEFT arrow is pressed")

                # check for out of bounds
                if (current_position[1] - 1 < 0):
                    print("WARNING: out of bounds")
                    continue

                # get the x-coor and y-coor of the current position
                x = current_position[0]
                y = current_position[1]

                # check if the next tile is valid
                next_path_symbol = my_map.map[x][y - 1]

                # player has won
                if  self.has_finished() and next_path_symbol == 'E':
                    self.is_running = False                    
                    continue
                
                elif next_path_symbol == 'W':
                    my_map.attack()
                    continue

                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue

                # not out of bounds
                # update the green color if success
                if (self.static_map[x][y] == "G" and self.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y-1] + "P" + "K" + my_map.map[x][y+1:]

                # update the red color if success
                elif (self.static_map[x][y] == "R" and self.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y-1] + "P" + "H" + my_map.map[x][y+1:]
                
                # assign the new map after the user's moved (not success)
                else:
                    my_map.map[x] = my_map.map[x][:y-1] + "P" + self.static_map[x][y] + my_map.map[x][y+1:]

                # do some animation of the dice
                my_map.move("left")
                

                # update current position 
                current_position = (current_position[0], current_position[1] - 1)

                # update current symbol
                current_symbol = my_map.get_dice_position()
                if (next_path_symbol == "R"):
                    next_path_symbol = "default"
                elif (next_path_symbol == "G"):
                    next_path_symbol = "default2"
                if (current_symbol == next_path_symbol):
                    self.update_check(current_position[0], current_position[1])
                
                print(f"\tPlayer's current position: {current_position}")

                if (self.has_finished()):
                    print("PLAYER HAS PASSED ALL PATHS")

            elif keys[pygame.K_RIGHT] and press ==False:
                press =True
                print("\tRIGHT arrow is pressed")

                # check for out of bounds
                # 10 is the MAX column number
                if (current_position[1] + 1 >= 10):
                    print("WARNING: out of bounds")
                    continue
                
                # x-coor and y-coor of current position
                x = current_position[0]
                y = current_position[1]

                # check if the next tile is valid
                next_path_symbol = my_map.map[x][y + 1]

                # player has won
                if (self.has_finished() and next_path_symbol == 'E'):
                    self.is_running = False
                    continue
                elif next_path_symbol == 'W':
                    my_map.attack()
                    continue
                
                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue
                
                # not out of bounds
                # update the green color if success
                if (self.static_map[x][y] == "G" and self.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y] + "K" + "P" + my_map.map[x][y+2:]

                # update the red color if success
                elif (self.static_map[x][y] == "R" and self.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y] + "H" + "P" + my_map.map[x][y+2:]

                # assign the new map after the user's moved (not success)
                else:
                    my_map.map[x] = my_map.map[x][:y] + self.static_map[x][y] + "P" + my_map.map[x][y+2:]

                # do some animation of the dice
                my_map.move("right")

                # update current position
                current_position = (current_position[0], current_position[1] + 1)
                
                # update current symbol
                current_symbol = my_map.get_dice_position()
                if (next_path_symbol == "R"):
                    next_path_symbol = "default"
                elif (next_path_symbol == "G"):
                    next_path_symbol = "default2"
                if (current_symbol == next_path_symbol):
                    self.update_check(current_position[0], current_position[1])

                print(f"\tPlayer's current position:  {current_position}")

                if (self.has_finished()):
                    print("PLAYER HAS PASSED ALL PATHS")

            elif keys[pygame.K_UP] and press ==False:
                press = True
                print("\tUP arrow is pressed")

                # check for out of bounds
                # 10 is the MAX column number
                if (current_position[0] - 1 < 0):
                    print("WARNING: out of bounds")
                    continue
                
                # x-coor and y-coor of current position
                x = current_position[0]
                y = current_position[1]

                # check if the next tile is valid
                next_path_symbol = my_map.map[x - 1][y]

                # player has won
                if (self.has_finished() and next_path_symbol == 'E'):
                    self.is_running = False
                    continue
                elif next_path_symbol == 'W':
                    my_map.attack()
                    continue

                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue

                # not out of bounds
                # update the green color if success
                if (self.static_map[x][y] == "G" and self.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y] + "K" + my_map.map[x][y+1:]
                
                # update the red color if success
                elif (self.static_map[x][y] == "R" and self.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y] + "H" + my_map.map[x][y+1:]
                
                # just assign
                else:
                    my_map.map[x] = my_map.map[x][:y] + self.static_map[x][y] + my_map.map[x][y+1:]
                
                # change the player's position
                my_map.map[x - 1] = my_map.map[x-1][:y] + "P" + my_map.map[x-1][y+1:]
                
                # do some animation of the dice
                my_map.move("up")

                # update current position
                current_position = (current_position[0] - 1, current_position[1])
                
                # update current symbol
                current_symbol = my_map.get_dice_position()
                if (next_path_symbol == "R"):
                    next_path_symbol = "default"
                elif (next_path_symbol == "G"):
                    next_path_symbol = "default2"
                if (current_symbol == next_path_symbol):
                    self.update_check(current_position[0], current_position[1])

                print(f"\tPlayer's current position: {current_position}")

                if (self.has_finished()):
                    print("PLAYER HAS PASSED ALL PATHS")

            elif keys[pygame.K_DOWN] and press == False:
                press = True 
                print("\tDOWN arrow is pressed")

                # check for out of bounds
                # 10 is the MAX column number
                if (current_position[0] + 1 >= len(my_map.map)):
                    print("WARNING: out of bounds")
                    continue
                
                # x-coor and y-coor of current position
                x = current_position[0]
                y = current_position[1]

                # check if the next tile is valid
                next_path_symbol = my_map.map[x + 1][y]

                # player has won
                if (self.has_finished() and next_path_symbol == 'E'):
                    self.is_running = False
                    continue
                elif next_path_symbol == 'W':
                    my_map.attack()
                    continue
                
                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue

                # not out of bounds
                # update the green color if success
                if (self.static_map[x][y] == "G" and self.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y] + "K" + my_map.map[x][y+1:]
                
                # update the red color if success
                elif (self.static_map[x][y] == "R" and self.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y] + "H" + my_map.map[x][y+1:]

                # just move normally
                else:
                    my_map.map[x] = my_map.map[x][:y] + self.static_map[x][y] + my_map.map[x][y+1:]
                    
                # just change the player's position
                my_map.map[x + 1] = my_map.map[x+1][:y] + "P" + my_map.map[x+1][y+1:]

                # do some animation of the dice
                my_map.move("down")

                # update current position
                current_position = (current_position[0] + 1, current_position[1])
                
                # update current symbol
                current_symbol = my_map.get_dice_position()
                if (next_path_symbol == "R"):
                    next_path_symbol = "default"
                elif (next_path_symbol == "G"):
                    next_path_symbol = "default2"
                if (current_symbol == next_path_symbol):
                    self.update_check(current_position[0], current_position[1])

                print(f"\tPlayer's current position: {current_position}")

                if (self.has_finished()):
                    print("PLAYER HAS PASSED ALL PATHS")
            # pygame.draw.rect(surface, rect_color, pygame.Rect(195, 100, 600, 500))
            # render text
            
            self.screen.fill(BG_COLOR)
            label = self.myfont.render("LEVEL {} ".format(self.cur_level), 1, (233,233,255,1))
            self.screen.blit(label, (750, 150))

            # update user interface

            my_map.read_data()
            pygame.display.update()

        # last level
        if (self.cur_level == MAX_LEVEL):
            print("Congratulations! You have passed all stages!")

        # to the next game
        else:
            Game(self.screen, self.cur_level + 1).mainloop()


if (__name__ == "__main__"):
    
    print("--------------------")
    print("Console for the game")
    print("--------------------")

    # initialise the pygame
    pygame.init()
    press = False

    print("Creating a new window")

    # create the window
    surface = pygame.display.set_mode((990,660))
    pygame.display.set_caption("Find Your Way Out")

    # main loop in homescreen
    Game(surface, 1).mainloop()

    # quit the game properly
    pygame.quit()