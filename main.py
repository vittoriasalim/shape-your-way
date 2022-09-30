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

# pygame.draw.rect(surface, rect_color, pygame.Rect(99, 66, 792, 528))
# rect_border = (233,233,255)
# pygame.draw.rect(surface, rect_border, pygame.Rect(99-10, 66-10, 792+20, 528+20),  10)



# get the data (level and data)
levels = parse.parse_json()
data = parse.read_map(levels[0]['path'])

print("Successfully parsing data for level 1")

# draw the map
my_map = draw.Map(data, surface)


print("Successfully created the map")

# get the starting position of the player
current_position = my_map.get_starting_position()

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

        # check if the tile is valid

        # not out of bounds
        # assign the new map after the user's moved
        x = current_position[0]
        y = current_position[1]

        print(f"\tPlayer's previous position: {current_position}")
        print(f"\t previous: {my_map.map[x]}")

        my_map.map[x] = my_map.map[x][:y-1] + "P" + "T" + my_map.map[x][y+1:]

        # do some animation of the dice
        my_map.move_left()

        # update current position
        current_position = (current_position[0], current_position[1] - 1)
        
        print(f"\t next:     {my_map.map[x]}")
        print(f"\tPlayer's current position: {current_position}")

        # update the map's UI
        surface.fill(color)


    elif keys[pygame.K_RIGHT]:

        print("\tRIGHT arrow is pressed")

        # check for out of bounds
        # 10 is the MAX column number
        if (current_position[1] + 1 >= 10):
            print("WARNING: out of bounds")
            continue
        
        # check if tile is valid

        # not out of bounds
        x = current_position[0]
        y = current_position[1]

        print(f"\tPlayer's previous position: {current_position}")
        print(f"\t previous: {my_map.map[x]}")
        
        my_map.map[x] = my_map.map[x][:y] + "T" + "P" + my_map.map[x][y+2:]

        # do some animation of the dice
        my_map.move_right()

        # update current position
        current_position = (current_position[0], current_position[1] + 1)

        print(f"\t next:     {my_map.map[x]}")

        print(f"\tPlayer's current position:  {current_position}")

        # update the map's UI
        surface.fill(color)


    elif keys[pygame.K_UP]:
        
        print("\tUP arrow is pressed")

        # check for out of bounds
        # 10 is the MAX column number
        if (current_position[0] - 1 < 0):
            print("WARNING: out of bounds")
            continue
        
        # check if tile is valid

        # not out of bounds
        x = current_position[0]
        y = current_position[1]
        my_map.map[x - 1] = my_map.map[x-1][:y] + "P" + my_map.map[x-1][y+1:]
        my_map.map[x] = my_map.map[x][:y] + "T" + my_map.map[x][y+1:]

        # do some animation of the dice
        my_map.move_up()

        # update current position
        current_position = (current_position[0] - 1, current_position[1])

        print(f"\tPlayer's current position: {current_position}")

        # update the map's UI
        surface.fill(color)

    
    elif keys[pygame.K_DOWN]:
        
        print("\tDOWN arrow is pressed")

        # check for out of bounds
        # 10 is the MAX column number
        if (current_position[0] + 1 >= len(my_map.map)):
            print("WARNING: out of bounds")
            continue
        
        # check if tile is valid

        # not out of bounds
        x = current_position[0]
        y = current_position[1]
        my_map.map[x + 1] = my_map.map[x+1][:y] + "P" + my_map.map[x+1][y+1:]
        my_map.map[x] = my_map.map[x][:y] + "T" + my_map.map[x][y+1:]

        # do some animation of the dice
        my_map.move_down()

        # update current position
        current_position = (current_position[0] + 1, current_position[1])

        print(f"\tPlayer's current position: {current_position}")

        # update the map's UI
        surface.fill(color)

    

    my_map.read_data()
    pygame.display.update()
    # delay for user interaction
    pygame.time.delay(100)

# quit
pygame.quit()
