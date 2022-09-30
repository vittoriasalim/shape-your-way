from draw import MySprite
import pygame
import draw
import parse

# initialise the pygame
pygame.init()

# create the window
surface = pygame.display.set_mode((990,660))
pygame.display.set_caption("shape-your-way")

# set the background color
color =(196, 211, 249)
surface.fill(color)
rect_color = (233,226,246)


# get the data (level and data)
levels = parse.parse_json()
data = parse.read_map(levels[0]['path'])

# draw the map
my_map = draw.Map(data,surface)
# my_map.draw()
my_sprite = MySprite()
my_group = pygame .sprite.Group(my_sprite)



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
        pass
    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass
    

    my_map.read_data(my_group)
    pygame.display.update()

# quit
pygame.quit()
    