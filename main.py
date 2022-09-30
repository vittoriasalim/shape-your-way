
import pygame
import draw
import parse
import player

# initialise the pygame
pygame.init()

# create the window
surface = pygame.display.set_mode((990,660))
pygame.display.set_caption("shape-your-way")

# set the background color
color =(196, 211, 249)


# get the data (level and data)
levels = parse.parse_json()
data = parse.read_map(levels[0]['path'])

# draw the map
my_map = draw.Map(data,surface)
player = player.Player()
my_player = pygame.sprite.Group(player)

# main loop
run = True
while run:



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
    

    # my_map.read_data(my_player)
    surface.fill(color)
    my_map.read_data(my_player)
    # my_player.update()
    # my_player.draw(surface)
    pygame.display.update()
    # delay for user interaction
    pygame.time.delay(60)

# quit
pygame.quit()
    