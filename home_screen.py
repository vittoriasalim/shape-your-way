import pygame

# Constants
WHITE = (0xFF, 0xFF, 0xFF)

BG_COLOR = (62, 61, 100)
RECT_COLOR = (233, 226, 246)

SCREEN_WIDTH = 990
SCREEN_HEIGHT = 660

class HomeScreen():
    """
    Home Screen (or Main Screen)
    """
    def __init__(self, screen, data):
        
        self.screen = screen
        self.data = data
        self.is_running = False
        # self.widgets = [] 
        # self.create_objects()

    def draw(self, surface):
        pass

    def mainloop(self, surface):
        
        self.is_running = True
        while (self.is_running):

            # frame per second
            pygame.time.delay(50)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            # draw
            self.draw(self.screen)

        pygame.quit()