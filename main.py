import pygame
import draw
import parse
pygame.init()

surface = pygame.display.set_mode((990,660))
pygame.display.set_caption("shape-your-way")
color =(164, 182, 229, 1)
surface.fill(color)
rect_color = (233,226,246)
# pygame.draw.rect(surface, rect_color, pygame.Rect(99, 66, 792, 528))
# rect_border = (233,233,255)
# pygame.draw.rect(surface, rect_border, pygame.Rect(99-10, 66-10, 792+20, 528+20),  10)


pygame.display.flip()

levels = parse.parse_json()
data =parse.read_map(levels[0]['path'])

my_map = draw.Map(data,surface)
my_map.draw()
run = True
while run:
    pygame.time.delay(500)
    my_map.read_data()
    pygame.display.flip()

    
    
    
    #map game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass

    

        
    
            

pygame.quit()
  
    