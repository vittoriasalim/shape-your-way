import pygame

class HomeScreen():
    """
    Home Screen (or Main Screen)
    """
    def __init__(self, screen, config):
        
        self.screen = screen
        self.config = config
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