from tabnanny import check
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
    def __init__(self, screen, data, levels) -> None:
        self.is_running = False
        self.screen = screen
        self.data = data
        self.cur_level = 0
        self.levels = levels
        # font for level
        self.myfont = pygame.font.SysFont("Rammetto One",35,bold =True)
        self.endFont = pygame.font.SysFont("Rammetto One",60,bold =True)
        self.buttonFont = pygame.font.SysFont("Rammetto One", 40, bold=True)
        self.levels = parse.parse_json()
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
        while True:
            

            # frame per second
            pygame.time.delay(50)
            
            if not self.is_running:
        
                pygame.draw.rect(self.screen, RECT_COLOR, pygame.Rect(195, 100, 600, 500))
                label = self.endFont.render("GAME OVER", 1, BG_COLOR)
                self.screen.blit(label, (362, 310))
                pygame.quit()
                continue

            # map game
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.is_running = False
                    continue

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
                    self.cur_level+=1
                    if self.cur_level == len(self.levels):
                        self.is_running = False
                        continue
                    data = parse.read_map(self.levels[self.cur_level]['path'])
                    my_map = draw.Map(data, self.screen)
                    # get the starting position of the player
                    current_position = my_map.get_starting_position()
                    current_symbol = my_map.get_starting_symbol()
                    continue

                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue

                # not out of bounds
                # update the green color if success
                if (self.static_map[x][y] == "G" and my_map.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y-1] + "P" + "K" + my_map.map[x][y+1:]

                # update the red color if success
                elif (self.static_map[x][y] == "R" and my_map.check[x][y] == 1):
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
                    
                    self.cur_level+=1
                    if self.cur_level == len(self.levels):
                        self.is_running = False
                        continue
                    data = parse.read_map(self.levels[self.cur_level]['path'])
                    my_map = draw.Map(data, self.screen)
                    # get the starting position of the player
                    current_position = my_map.get_starting_position()
                    current_symbol = my_map.get_starting_symbol()
                    continue
                
                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue
                
                # not out of bounds
                # update the green color if success
                if (self.static_map[x][y] == "G" and my_map.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y] + "K" + "P" + my_map.map[x][y+2:]

                # update the red color if success
                elif (self.static_map[x][y] == "R" and my_map.check[x][y] == 1):
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
                 
                    self.cur_level+=1
                    if self.cur_level == len(self.levels):
                        self.is_running = False
                        continue

                    data = parse.read_map(self.levels[self.cur_level]['path'])

                    my_map = draw.Map(data, self.screen)
                    # get the starting position of the player
                    current_position = my_map.get_starting_position()
                    current_symbol = my_map.get_starting_symbol()
                    continue

                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue

                # not out of bounds
                # update the green color if success
                if (self.static_map[x][y] == "G" and my_map.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y] + "K" + my_map.map[x][y+1:]
                
                # update the red color if success
                elif (self.static_map[x][y] == "R" and my_map.check[x][y] == 1):
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
                
                    self.cur_level+=1
                    if self.cur_level == len(self.levels):
                        self.is_running = False
                        continue
                    data = parse.read_map(self.levels[self.cur_level]['path'])
                    my_map = draw.Map(data, self.screen)
                    # get the starting position of the player
                    current_position = my_map.get_starting_position()
                    current_symbol = my_map.get_starting_symbol()
                    continue
                    
                
                elif (next_path_symbol not in allowed_tiles):
                    print("WARNING: move not allowed")
                    continue

                # not out of bounds
                # update the green color if success
                if (self.static_map[x][y] == "G" and my_map.check[x][y] == 1):
                    my_map.map[x] = my_map.map[x][:y] + "K" + my_map.map[x][y+1:]
                
                # update the red color if success
                elif (self.static_map[x][y] == "R" and my_map.check[x][y] == 1):
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
                    my_map.update_check(current_position[0], current_position[1])

                print(f"\tPlayer's current position: {current_position}")

                if (my_map.has_finished()):
                    print("PLAYER HAS PASSED ALL PATHS")
            # pygame.draw.rect(surface, rect_color, pygame.Rect(195, 100, 600, 500))
            # render text
            
            self.screen.fill(BG_COLOR)
            label = self.myfont.render("LEVEL {} ".format(self.cur_level+1), 1, (233,233,255,1))
            self.screen.blit(label, (750, 150))

            # update user interface

            my_map.read_data()
            pygame.display.update()
            
        # quit
        pygame.quit()

    def mainmenu(self):
        title_font = pygame.font.SysFont("Rammetto One", 60, bold=True)
        run = True
        while run:
            pygame.draw.rect(self.screen, RECT_COLOR, pygame.Rect(195, 60, 600, 550))
            label = self.endFont.render("ROLL YOUR WAY", 1, BG_COLOR)
            self.screen.blit(label, (300, 200))
            pygame.draw.rect(self.screen, (164, 182, 229, 1), pygame.Rect(195, 60, 600, 550), 10)
            pygame.draw.rect(self.screen, (164, 182, 229, 1), pygame.Rect(423, 340, 150, 50))
            pygame.draw.rect(self.screen, BG_COLOR, pygame.Rect(423, 340, 150, 50), 5)
            mouse = pygame.mouse.get_pos()
            if 450 <= mouse[0] <= 600 and 350 <= mouse[1] <= 400:
                label_button = self.buttonFont.render("START", 1, WHITE)
            else:
                label_button = self.buttonFont.render("START", 1, BG_COLOR)
            self.screen.blit(label_button, (450, 350))

            # title_label = title_font.render("Press Enter to begin the game", 1, (255,255,255))
            # surface.blit(title_label, ((990/2)-380,(660/2)))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the
                    # button the game is terminated
                    if 450 <= mouse[0] <= 600 and 350 <= mouse[1] <= 400:
                        self.mainloop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.mainloop()

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
    Game(surface, data, levels).mainloop()

    # quit the game properly
    pygame.quit()