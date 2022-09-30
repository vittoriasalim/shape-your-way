import pygame
import draw
import parse

# initialise the pygame
pygame.init()

# create the window
surface = pygame.display.set_mode((990,660))
pygame.display.set_caption("shape-your-way")

# set the background color
color =(164, 182, 229, 1)
surface.fill(color)
rect_color = (233,226,246)

# pygame.draw.rect(surface, rect_color, pygame.Rect(99, 66, 792, 528))
# rect_border = (233,233,255)
# pygame.draw.rect(surface, rect_border, pygame.Rect(99-10, 66-10, 792+20, 528+20),  10)

pygame.display.flip()

# get the data (level and data)
levels = parse.parse_json()
data = parse.read_map(levels[0]['path'])

print(data)
print(type(surface))

# draw the map
my_map = draw.Map(data, surface)
my_map.draw()

print(my_map.map)

# get the starting position of the player
current_position = my_map.get_starting_position()

print(current_position)

# main loop
run = True
while run:

    # delay for user interaction
    pygame.time.delay(60)

    # map game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # get the user input
    keys = pygame.key.get_pressed()
    
    # user interaction with user input
    if keys[pygame.K_LEFT]:
        
        # make a new string
        result = ""
        for j in range(len(my_map.map[current_position[0]])):
            string = my_map.map[current_position[0]][j]
            if (j == current_position[1] - 1):
                result += "P"
            elif (j == current_position[1]):
                result += " "
            else:
                result += string
        
        # assign to the current map data
        my_map.map[current_position[0]] = result

        # update the map's UI
        my_map.read_data()

    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass
    

    my_map.read_data()
    pygame.display.flip()

# quit
pygame.quit()
