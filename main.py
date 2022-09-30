import pygame
import draw
import parse

print("--------------------")
print("Console for the game")
print("--------------------")

# initialise the pygame
pygame.init()

# create the window
surface = pygame.display.set_mode((990,660))
pygame.display.set_caption("shape-your-way")

# set the background color
color =(196, 211, 249)
rect_color = (233,226,246)

print("Creating a new window")

# get the data (level and data)
levels = parse.parse_json()
data = parse.read_map(levels[0]['path'])

print("Successfully parsing data for level 1")

# draw the map
my_map = draw.Map(data, surface)

print("Successfully created the map")

# get the starting position of the player
current_position = my_map.get_starting_position()
current_symbol = my_map.get_starting_symbol()

print(f"The player's current position: {current_position}")

# main loop
run = True
while run:



    # map game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    surface.fill(color)
    
    # get the user input
    keys = pygame.key.get_pressed()
    
    # user interaction with user input
    if keys[pygame.K_LEFT]:
        
        print("\tLEFT arrow is pressed")

        # check for out of bounds
        if (current_position[1] - 1 < 0):
            print("WARNING: out of bounds")
            continue

        # x-coor and y-coor of current position
        x = current_position[0]
        y = current_position[1]

        # check if the next tile is valid
        next_path_symbol = my_map.map[x][y - 1]
        if (my_map.has_finished() and next_path_symbol == 'E'):
            my_map.map[x] = my_map.map[x][:y-1] + "P" + "E" + my_map.map[x][y+1:]
            surface.fill(color)
            print("PLAYER has won")
            run = False
            continue

        elif (current_symbol == 'R' and next_path_symbol != 'G'):
            print("WARNING: move not allowed")
            continue

        elif (current_symbol == 'G' and next_path_symbol != 'R'):
            print("WARNING: move not allowed")
            continue
        

        # not out of bounds
        # assign the new map after the user's moved
        print(f"\tPlayer's previous position: {current_position}")
        print(f"\t previous: {my_map.map[x]}")

        my_map.map[x] = my_map.map[x][:y-1] + "P" + current_symbol + my_map.map[x][y+1:]

        # do some animation of the dice
        my_map.move()

        # update current position and current symbol
        current_position = (current_position[0], current_position[1] - 1)
        if (current_symbol == 'G'):
            current_symbol = 'R'
        else:
            current_symbol = 'G'
        my_map.update_check(x, y)
        
        print(f"\t next:     {my_map.map[x]}")
        print(f"\tPlayer's current position: {current_position}")

        if (my_map.has_finished()):
            print("PLAYER HAS PASSED ALL PATHS")




    elif keys[pygame.K_RIGHT]:

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
            my_map.map[x] = my_map.map[x][:y] + "E" + "P" + my_map.map[x][y+2:]
            surface.fill(color)
            print("PLAYER has won")
            run = False
            continue
        
        elif (current_symbol == 'R' and next_path_symbol != 'G'):
            print("WARNING: move not allowed")
            continue

        elif (current_symbol == 'G' and next_path_symbol != 'R'):
            print("WARNING: move not allowed")
            continue

        print(f"\tPlayer's previous position: {current_position}")
        print(f"\t previous: {my_map.map[x]}")
        
        # not out of bounds
        # assign the new map after the user's moved
        my_map.map[x] = my_map.map[x][:y] + current_symbol + "P" + my_map.map[x][y+2:]

        # do some animation of the dice
        my_map.move()

        # update current position
        current_position = (current_position[0], current_position[1] + 1)
        if (current_symbol == 'G'):
            current_symbol = 'R'
        else:
            current_symbol = 'G'
        my_map.update_check(x, y)

        print(f"\t next:     {my_map.map[x]}")
        print(f"\tPlayer's current position:  {current_position}")

        if (my_map.has_finished()):
            print("PLAYER HAS PASSED ALL PATHS")

      


    elif keys[pygame.K_UP]:
        
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
            my_map.map[x] = my_map.map[x][:y] + "E" + my_map.map[x][y+1:]
            surface.fill(color)
            print("PLAYER has won")
            run = False
            continue

        elif (current_symbol == 'R' and next_path_symbol != 'G'):
            print("WARNING: move not allowed")
            continue

        elif (current_symbol == 'G' and next_path_symbol != 'R'):
            print("WARNING: move not allowed")
            continue

        # check if tile is valid

        # not out of bounds
        my_map.map[x - 1] = my_map.map[x-1][:y] + "P" + my_map.map[x-1][y+1:]
        my_map.map[x] = my_map.map[x][:y] + current_symbol + my_map.map[x][y+1:]

        # do some animation of the dice
        my_map.move()

        # update current position
        current_position = (current_position[0] - 1, current_position[1])
        if (current_symbol == 'G'):
            current_symbol = 'R'
        else:
            current_symbol = 'G'
        my_map.update_check(x, y)

        print(f"\tPlayer's current position: {current_position}")

        if (my_map.has_finished()):
            print("PLAYER HAS PASSED ALL PATHS")

     

    
    elif keys[pygame.K_DOWN]:
        
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
            my_map.map[x] = my_map.map[x][:y] + "E" + my_map.map[x][y+1:]
            surface.fill(color)
            print("PLAYER has won")
            run = False
            continue
        
        elif (current_symbol == 'R' and next_path_symbol != 'G'):
            print("WARNING: move not allowed")
            continue

        elif (current_symbol == 'G' and next_path_symbol != 'R'):
            print("WARNING: move not allowed")
            continue

        # not out of bounds
        my_map.map[x + 1] = my_map.map[x+1][:y] + "P" + my_map.map[x+1][y+1:]
        my_map.map[x] = my_map.map[x][:y] + current_symbol + my_map.map[x][y+1:]

        # do some animation of the dice
        my_map.move()

        # update current position
        current_position = (current_position[0] + 1, current_position[1])
        if (current_symbol == 'G'):
            current_symbol = 'R'
        else:
            current_symbol = 'G'
        my_map.update_check(x, y)

        print(f"\tPlayer's current position: {current_position}")

        if (my_map.has_finished()):
            print("PLAYER HAS PASSED ALL PATHS")


    my_map.read_data()
    pygame.display.update()
    # delay for user interaction
    pygame.time.delay(50)
    
# quit
pygame.quit()
