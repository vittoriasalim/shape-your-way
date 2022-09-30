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

class Game():
    """
    Game Screen
    """
    def __init__(self, screen, data) -> None:
        self.is_running = False
        self.screen = screen
        self.data = data
        # self.cur_level = 0
        # font for level
        # self.myfont = pygame.font.SysFont("Rammetto One",35,bold =True)
        # self.endFont = pygame.font.SysFont("Rammetto One",60,bold =True)

        # create a copy of the map
        self.static_map = []
        for i in range(ROW):
            self.static_map.append([])
            for j in range(COL):
                if (self.data[i][j] == "P"):
                    self.static_map[i].append("R")
                else:
                    self.static_map[i].append(self.data[i][j])

    def mainloop(self) -> None:

        # create the map
        my_map = draw.Map(self.data, self.screen)

        print("Successfully created the map")

        # get the starting position of the player
        current_position = my_map.get_starting_position()
        current_symbol = my_map.get_starting_symbol()

        print(f"The player's current position: {current_position}")

        # tiles that are allowed to go through
        allowed_tiles = [ 'R', 'G', 'M', 'E', 'H', 'K' ]
        
        # main loop
        press = False
        self.is_running = True
        while self.is_running:

            # frame per second
            pygame.time.delay(50)

            # map game
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.is_running = False
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
                if (my_map.has_finished() and next_path_symbol == 'E'):
                    my_map.map[x] = my_map.map[x][:y-1] + "P" + self.static_map[x][y] + my_map.map[x][y+1:]
                    self.screen.fill(BG_COLOR)
                    print("PLAYER has won")
                    continue

                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue

                # not out of bounds
                # assign the new map after the user's moved
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
                    if (self.static_map[x][y] == "G"):
                        my_map.map[x] = my_map.map[x][:y-1] + "P" + "K" + my_map.map[x][y+1:]
                    elif (self.static_map[x][y] == "R"):
                        my_map.map[x] = my_map.map[x][:y-1] + "P" + "H" + my_map.map[x][y+1:]
                    my_map.update_check(current_position[0], current_position[1])
                
                print(f"\tPlayer's current position: {current_position}")

                if (my_map.has_finished()):
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
                if (my_map.has_finished() and next_path_symbol == 'E'):
                    my_map.map[x] = my_map.map[x][:y] + self.static_map[x][y] + "P" + my_map.map[x][y+2:]
                    self.screen.fill(BG_COLOR)
                    print("PLAYER has won")
                    continue
                
                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue
                
                # not out of bounds
                # assign the new map after the user's moved
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
                    if (self.static_map[x][y] == "G"):
                        my_map.map[x] = my_map.map[x][:y] + "K" + "P" + my_map.map[x][y+2:]
                    elif (self.static_map[x][y] == "R"):
                        my_map.map[x] = my_map.map[x][:y] + "H" + "P" + my_map.map[x][y+2:]
                    my_map.update_check(current_position[0], current_position[1])

                print(f"\tPlayer's current position:  {current_position}")

                if (my_map.has_finished()):
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
                if (my_map.has_finished() and next_path_symbol == 'E'):
                    my_map.map[x - 1] = my_map.map[x-1][:y] + "P" + my_map.map[x-1][y+1:]
                    my_map.map[x] = my_map.map[x][:y] + self.static_map[x][y] + my_map.map[x][y+1:]
                    self.screen.fill(BG_COLOR)
                    print("PLAYER has won")
                    continue

                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue

                # not out of bounds
                my_map.map[x - 1] = my_map.map[x-1][:y] + "P" + my_map.map[x-1][y+1:]
                my_map.map[x] = my_map.map[x][:y] + self.static_map[x][y] + my_map.map[x][y+1:]
                
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
                    if (self.static_map[x][y] == "G"):
                        my_map.map[x] = my_map.map[x][:y] + "K" + my_map.map[x][y+1:]
                    elif (self.static_map[x][y] == "R"):
                        my_map.map[x] = my_map.map[x][:y] + "H" + my_map.map[x][y+1:]
                    my_map.update_check(current_position[0], current_position[1])

                print(f"\tPlayer's current position: {current_position}")

                if (my_map.has_finished()):
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
                if (my_map.has_finished() and next_path_symbol == 'E'):
                    my_map.map[x + 1] = my_map.map[x+1][:y] + "P" + my_map.map[x+1][y+1:]
                    my_map.map[x] = my_map.map[x][:y] + self.static_map[x][y] + my_map.map[x][y+1:]
                    self.screen.fill(BG_COLOR)
                    print("PLAYER has won")
                    continue
                
                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue

                # not out of bounds
                my_map.map[x + 1] = my_map.map[x+1][:y] + "P" + my_map.map[x+1][y+1:]
                my_map.map[x] = my_map.map[x][:y] + self.static_map[x][y] + my_map.map[x][y+1:]

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
                    if (self.static_map[x][y] == "G"):
                        my_map.map[x] = my_map.map[x][:y] + "K" + my_map.map[x][y+1:]
                    elif (self.static_map[x][y] == "R"):
                        my_map.map[x] = my_map.map[x][:y] + "H" + my_map.map[x][y+1:]
                    my_map.update_check(current_position[0], current_position[1])

                print(f"\tPlayer's current position: {current_position}")

                if (my_map.has_finished()):
                    print("PLAYER HAS PASSED ALL PATHS")

            # update user interface
            self.screen.fill(BG_COLOR)
            my_map.read_data()
            pygame.display.update()
            
        # quit
        pygame.quit()

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

    # load the levels and data
    levels = parse.parse_json()
    data = parse.read_map(levels[0]['path'])

    print("Successfully parsing data for level 1")

    # main loop in homescreen
    Game(surface, data).mainloop()

    # quit the game properly
    pygame.quit()