import pygame
import parse
from game import Game

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
        self.endFont = pygame.font.SysFont("Rammetto One", 60, bold=True)
        self.buttonFont = pygame.font.SysFont("Rammetto One", 40, bold=True)

    def draw(self):

        # Create header "Roll Your Way" on home screen
        pygame.draw.rect(self.screen, RECT_COLOR, pygame.Rect(195, 60, 600, 550))
        label = self.endFont.render("ROLL YOUR WAY", 1, BG_COLOR)
        self.screen.blit(label, (300, 200))

        # Create "Start" button
        pygame.draw.rect(self.screen, (164, 182, 229, 1), pygame.Rect(195, 60, 600, 550), 10)
        pygame.draw.rect(self.screen, (164, 182, 229, 1), pygame.Rect(423, 340, 150, 50))
        pygame.draw.rect(self.screen, BG_COLOR, pygame.Rect(423, 340, 150, 50), 5)
        mouse = pygame.mouse.get_pos()
        if 450 <= mouse[0] <= 600 and 350 <= mouse[1] <= 400:
            label_button = self.buttonFont.render("START", 1, WHITE)
        else:
            label_button = self.buttonFont.render("START", 1, BG_COLOR)
        self.screen.blit(label_button, (450, 350))

    def mainloop(self):


        self.is_running = True
        while (self.is_running):

            # frame per second
            pygame.time.delay(50)

            # events
            mouse = pygame.mouse.get_pos()
            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()

                # checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the
                    # button, go to the game page
                    if 450 <= mouse[0] <= 600 and 350 <= mouse[1] <= 400:
             
                        self.is_running = False

            # draw
            self.screen.fill(BG_COLOR)
            self.draw()
            pygame.display.update()


            


