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
MAIN_MENU_MUSIC = ("./sounds/Free Game Soundtrack by cactusdude - (hurry up).ogg")
MAIN_MENU_MUSIC2 = ("./sounds/sounds_8Bit Platformer Loop.ogg")
GAME_MUSIC= ("./sounds/Dystopian.ogg")
GAME_MUSIC2 = ("./sounds/Quantum Loop.ogg")
WINNING_SCREEN_MUSIC = ("")

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
        pygame.mixer.init()
        # Get the homescreen
        if (not is_quit):
            pygame.mixer.music.load(MAIN_MENU_MUSIC2)
            pygame.mixer.music.play()
            is_quit = HomeScreen(surface).mainloop()



        # go to the lore page
        if (not is_quit):
            pygame.mixer.music.load(GAME_MUSIC2)
            pygame.mixer.music.play()
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
