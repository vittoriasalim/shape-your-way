import pygame
import parse
from home_screen import HomeScreen
from game import Game

# Constants
WHITE = (0xFF, 0xFF, 0xFF)

BG_COLOR = (62, 61, 100)
RECT_COLOR = (233, 226, 246)

SCREEN_WIDTH = 990
SCREEN_HEIGHT = 660

# Main App
class App():

    def __init__(self) -> None:

        print("--------------------")
        print("Console for the game")
        print("--------------------")

        # initialise the pygame
        pygame.init()

        print("Creating a new window")

        # create the window
        surface = pygame.display.set_mode((990,660))
        pygame.display.set_caption("Find Your Way Out")

        # Get the homescreen
        HomeScreen(surface).mainloop()

        # start from level 1
        Game(surface, 1).mainloop()

        # quit the game properly
        pygame.quit()

if (__name__ == "__main__"):
    App()
