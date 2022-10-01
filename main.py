import pygame
from home_screen import HomeScreen
from game import Game
from winning_screen import WinningScreen
from lore_page import LorePage

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

        is_quit = False

        # Get the homescreen
        if (not is_quit):
            is_quit = HomeScreen(surface).mainloop()

        # go to the lore page
        if (not is_quit):
            is_quit = LorePage(surface).mainloop()

        # start from level 1
        if (not is_quit):
            is_quit = Game(surface, 1).mainloop()

        # once the player passed all the game levels
        if (not is_quit):
            is_quit = WinningScreen(surface).mainloop()

        # quit the game properly
        pygame.quit()

if (__name__ == "__main__"):
    App()
